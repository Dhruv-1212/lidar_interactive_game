# import pygame
#
# # Initialize Pygame
# pygame.init()
#
# # Set screen size
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# # Set circle color
# circle_color = (255, 0, 0)  # Red
#
# # Set circle radius (adjust as needed)
# circle_radius = 10
#
# # Set drawing flag
# drawing = False
#
# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         # Quit event
#         if event.type == pygame.QUIT:
#             running = False
#
#         # Left mouse click event
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 # Get mouse position
#                 mouse_pos = pygame.mouse.get_pos()
#                 # Set drawing flag to True
#                 drawing = True
#
#     # Fill screen with white
#     screen.fill((255, 255, 255))
#
#     # Draw circle if drawing flag is True
#     if drawing:
#         pygame.draw.circle(screen, circle_color, mouse_pos, circle_radius)
#
#     # Update display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()


import pygame
import time
import math
import numpy as np
from hokuyo.driver import hokuyo
from hokuyo.tools import serial_port
import serial
import queue
import threading
from pygame import mixer
import time
import pygame.font

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Set circle color
circle_color = (255, 0, 0)  # Red
circle_color2=(0,0,0)
# Set circle radius (adjust as needed)
circle_radius = 10
circle_radius2 = 5

# Create a list to store circle positions
circle_positions = []

# Game loop

uart_port = '/dev/ttyACM0'
uart_speed = 19200

# Main game loop
list_all_coordinates_transformed=[]
class DataPublisher(threading.Thread):
    def __init__(self, name, coordinate_queue,  list_all_coordinates_transformed):
        super().__init__()
        self.name = name;
        self.coordinate_queue = coordinate_queue
        self.list_all_coordinates_transformed=list_all_coordinates_transformed
        laser_serial = serial.Serial(port=uart_port, baudrate=uart_speed, timeout=0.5)
        port = serial_port.SerialPort(laser_serial)
        self.laser = hokuyo.Hokuyo(port)

        self.angle_in_radians = math.radians(0)
        self.transformation_matrix = np.array([[math.cos(self.angle_in_radians), -math.sin(self.angle_in_radians), 230],
                                               [math.sin(self.angle_in_radians), math.cos(self.angle_in_radians), -110],
                                               [0, 0, 1]])

    def transform_coordinates(self, item):
        angle = math.radians(item[0])
        point = np.array([item[1] * math.sin(angle), item[1] * math.cos(angle), 1])
        result = np.dot(self.transformation_matrix, point)
        return result.tolist()

    def run(self):
        self.laser.laser_on()

        while True:
            data = self.laser.get_single_scan()
            list_cord = []
            key_avg = 0
            value_avg = 0
            l = 0
            # list_key=[]
            # list_value=[]
            if (data is not None):
                for key, value in data.items():
                    if -65 < key < 70 and 70 < value < 500:
                        # list_key.append(key)
                        # list_value.append(value)
                        # l += 1
                        list_cord.append((key, value))
                        ans=self.transform_coordinates([key,value])
                        if(ans[0]>0 and ans[0]<540) and (ans[1]>0 and ans[1]< 360):
                            self.list_all_coordinates_transformed.append(ans)
                        # key_avg += key
                        # value_avg += value

            # # print("length: ", l)
            # for i in range(len(list_key)):
            #     ans=self.transform_coordinates([list_key[i],list_value[i]])
            #     list_all_coordinate.append(ans)
            # if l != 0:
            #     key_avg = key_avg / l
            #     value_avg = value_avg / l
            # final_data = self.transform_coordinates([key_avg, value_avg])


            sorted_data = sorted(list_all_coordinates_transformed, key=lambda x: x[1])
            final_coord=[]
            final_coord.apped(sorted_data[0])
            for i in range(len(sorted_data)):
                if(final_coord[0][0]-10<sorted_data[i][0] and final_coord[0][0]+10>sorted_data[i][0] and final_coord[0][1]+10<sorted_data[i][1]):
                    final_coord.append(sorted_data[i])

            # if final_data is not None and l != 0:
            #     self.coordinate_queue.put(final_data[0])
            #     self.coordinate_queue.put(final_data[1])
            avg_x=0
            avg_y=0
            # if(len(self.list_all_coordinates_transformed)!=0):
            #     for i in list_all_coordinates_transformed:
            #         avg_x+=i[0]
            #         avg_y+=i[1]
            #     avg_x=avg_x/len(self.list_all_coordinates_transformed)
            #     avg_y=avg_y/len(self.list_all_coordinates_transformed)

            if(len(final_coord)!=0):
                for i in final_coord:
                    avg_x+=i[0]
                    avg_y+=i[1]
                avg_x=avg_x/len(final_coord)
                avg_y=avg_y/len(final_coord)


            if(avg_x!=0):
                self.coordinate_queue.put(avg_x)
                self.coordinate_queue.put(avg_y)
            self.list_all_coordinates_transformed=[]
            time.sleep(.1)

coordinate_queue = queue.Queue()
thread1 = DataPublisher(name="Thread 1", coordinate_queue=coordinate_queue,  list_all_coordinates_transformed=list_all_coordinates_transformed)
thread1.start()
queue_not_empty=0
finger=(0,0)
running = True
while running:
    if(coordinate_queue.empty()):
        queue_not_empty=0
        finger=(0,0)
    else:
        print("yes")
        queue_not_empty=1
        x=coordinate_queue.get()
        y=coordinate_queue.get()
        print(x,y)
        coord_x=int((1200/505)*x)
        coord_y=int((700/360)*y)
        finger=(coord_x, coord_y)

    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            running = False

        # Left mouse click event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # Append mouse position to list
                circle_positions.append(mouse_pos)
    if(queue_not_empty):
        circle_positions.append(finger)
    # Fill screen with white
    screen.fill((255, 255, 255))
    for i in range(len(list_all_coordinates_transformed)):
        x=list_all_coordinates_transformed[i][0]
        y=list_all_coordinates_transformed[i][1]
        coord_x=int((1200/505)*x)
        coord_y=int((700/360)*y)
        finger=(coord_x, coord_y)

        pygame.draw.circle(screen, circle_color2, finger, circle_radius2)

    # Draw all circles from the list
    for position in circle_positions:
        pygame.draw.circle(screen, circle_color, position, circle_radius)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

