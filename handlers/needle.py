import math
import tkinter as tk

# Creating Analog Gauge object to creat multiple Diagram
class Speedometer(tk.Canvas):
    def __init__(self, parent,parent_width, parent_height, min_value, max_value, oval_radius_width, oval_radius_height, center_x, center_y, num_ticks_radius, ticks_radius, needle_quad_height, needle_quad_width, needle_quad_height_y3_y4, gauge_info_text, gauge_info_text_x, gauge_info_text_y):
        super().__init__(parent, width=parent_width, height=parent_height)
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        self.oval_radius_width = oval_radius_width
        self.oval_radius_height = oval_radius_height
        self.num_ticks_radius = num_ticks_radius
        self.ticks_radius = ticks_radius
        self.needle_quad_height = needle_quad_height
        self.needle_quad_width = needle_quad_width
        self.needle_quad_height_y3_y4 = needle_quad_height_y3_y4
        self.gauge_info_text = gauge_info_text
        self.gauge_info_text_x = gauge_info_text_x
        self.gauge_info_text_y = gauge_info_text_y
        
        self.center_x = center_x
        self.center_y = center_y

        # Creating basis of analog gauge with oval and information text
        self.configure(bg='#0E0E0E', highlightthickness=0)
        self.create_oval(0, 0, oval_radius_width, oval_radius_height, width=3, outline='white', fill='black', )
        self.create_text(gauge_info_text_x, gauge_info_text_y, text=self.gauge_info_text, font=('Arial', 12), fill='white')
        # self.value_text = self.create_text(150, 200, text=str(self.value), font=('Arial', 24, 'bold'), fill='white')
        
        # Add number indications
        num_ticks = 9  # Number of tick marks
        angle_range = 270  # Angle range for the tick marks
        angle_increment = angle_range / (num_ticks - 0)  # Angle increment between each tick mark

        for i in range(num_ticks):
            angle = -210 + i * angle_increment  # Calculate the angle for the tick mark
            radius = self.num_ticks_radius  # Radius for the tick mark

            x = self.center_x + radius * math.cos(math.radians(angle))
            y = self.center_y + radius * math.sin(math.radians(angle))

            value = int(min_value + (max_value - min_value) / (num_ticks - 1) * i)  # Calculate the value for the tick mark
            # values = [0,4,8,12,16,20,24,28,32,36,40]
            # value = values[i]

            self.create_text(x, y, text=str(value), font=('Arial', 10), fill='white')
            
        # Drawing big ticks on analog gauge
        for angle in range(-30, 225, 30):  # Draw ticks every 30 degrees
            radius1 = self.ticks_radius
            angle_rad = math.radians(angle)
            x1 = self.center_x + (radius1 + 5) * math.cos(angle_rad)
            y1 = self.center_y - (radius1 + 5) * math.sin(angle_rad)
            x2 = self.center_x + (radius1 + 30) * math.cos(angle_rad)
            y2 = self.center_y - (radius1 + 30) * math.sin(angle_rad)
            self.create_line(x1, y1, x2, y2, fill='white', width=2)
        
        # Drawing small ticks on analog gauge
        for angle in range(-30, 215, 5):  # Draw ticks every 5 degrees
            radius1 = self.ticks_radius
            angle_rad = math.radians(angle)
            x1 = self.center_x + (radius1 + 18) * math.cos(angle_rad)
            y1 = self.center_y - (radius1 + 18) * math.sin(angle_rad)
            x2 = self.center_x + (radius1 + 30) * math.cos(angle_rad)
            y2 = self.center_y - (radius1 + 30) * math.sin(angle_rad)
            self.create_line(x1, y1, x2, y2, fill='white', width=2)


    # Updating speed of needle
    def update_speed(self, speed):
        self.value = speed
        # self.itemconfigure(self.value_text, text=str(self.value))

        # Calculate the angle for the needle
        angle = (self.value - self.min_value) / (self.max_value - self.min_value) * 180 - 90
        angle = 55 + self.value

        # Calculate the coordinates of the quadrilateral points
        center_x = self.center_x
        center_y = self.center_y
        quad_width = self.needle_quad_width
        quad_height = self.needle_quad_height

        x1 = center_x - quad_width / 2
        y1 = center_y - quad_height / 2
        x2 = center_x + quad_width / 2
        y2 = center_y - quad_height / 2
        x3 = center_x + 1 / 2
        y3 = center_y + self.needle_quad_height_y3_y4 / 2
        x4 = center_x - 1 / 2
        y4 = center_y + self.needle_quad_height_y3_y4 / 2

        # Rotate the quadrilateral based on the angle
        rotated_points = rotate_points([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], center_x, center_y, angle)

        # Clear previous needle and draw the new quadrilateral
        self.delete('needle')
        self.create_polygon(rotated_points[0][0], rotated_points[0][1],
                            rotated_points[1][0], rotated_points[1][1],
                            rotated_points[2][0], rotated_points[2][1],
                            rotated_points[3][0], rotated_points[3][1],
                            fill='#ED7D1E', tags='needle')
        
    
    
            
# Return rotate points for needle
def rotate_points(points, center_x, center_y, angle):
    rotated_points = []
    for x, y in points:
        rotated_x = center_x + (x - center_x) * math.cos(math.radians(angle)) - (y - center_y) * math.sin(math.radians(angle))
        rotated_y = center_y + (x - center_x) * math.sin(math.radians(angle)) + (y - center_y) * math.cos(math.radians(angle))
        rotated_points.append((rotated_x, rotated_y))
    return rotated_points


# root = tk.Tk()

# speedometer = Speedometer(root, parent_width=310, parent_height=310, min_value=0, max_value=40, oval_radius_width=300, oval_radius_height=300, center_x=150, center_y=150, num_ticks_radius=110, ticks_radius=120, needle_quad_height=80, needle_quad_width=30, needle_quad_height_y3_y4 = 240, gauge_info_text="Left Break Force [kN]", gauge_info_text_x = 155, gauge_info_text_y = 230)
# speedometer.place(x=40, y=250)
# speedometer.update_speed(40)

# root.mainloop()