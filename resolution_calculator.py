'''
This program calculates the following values for Azahar, a 3DS emulator, on the Anbernic RG476H:
---Top Screen---
X-Position
Y-Position
Width
Height
---Bottom Screen---
X-Position
Y-Position
Width
Height
'''

'''
Notes: There is currently no bound checking for illegal values or anything of the sort, it will be added in a future update
'''
#RG476H
device_res_x = 1280
device_res_y = 960
device_aspect_ratio = 1.33 #4:3

#default values i.e standard values for Top and Bottom screens of the 3Ds
top_screen_aspect_ratio = 1.78 #16:9
bottom_screen_aspect_ratio = 1.33 #4:3


top_screen_res_x = 0
top_screen_res_y = 0
bottom_screen_res_x = 0
bottom_screen_res_y = 0

top_screen_pos_x = 0
top_screen_pos_y = 0
bottom_screen_pos_x = 0
bottom_screen_pos_y = 0

def reset_res():
    global top_screen_res_x
    global top_screen_res_y
    global bottom_screen_res_x
    global bottom_screen_res_y
    top_screen_res_x = 0
    top_screen_res_y = 0
    bottom_screen_res_x = 0
    bottom_screen_res_y = 0
    global top_screen_pos_x
    global top_screen_pos_y
    global bottom_screen_pos_x
    global bottom_screen_pos_y
    top_screen_pos_x = 0
    top_screen_pos_y = 0
    bottom_screen_pos_x = 0
    bottom_screen_pos_y = 0 

def get_desired_top_screen_res_x():
    desired_top_screen_res_x= input("Enter desired Top Screen Resolution (X/Horizontal value, e.g. ""1920"" from 1920x1080): ")
    return desired_top_screen_res_x

def calculate_top_screen_res_y(top_screen_res_x):
    top_y = top_screen_res_x/top_screen_aspect_ratio
    return top_y

def calculate_bottom_screen_res_y(top_screen_res_y):
    bottom_y = device_res_y - top_screen_res_y 
    return bottom_y

def calculate_bottom_screen_res_x(bottom_screen_res_y):
    bottom_x = bottom_screen_aspect_ratio * bottom_screen_res_y
    return bottom_x

def calculate_top_screen_pos_x(top_screen_res_x):
    pos_x = (device_res_x - top_screen_res_x)/2
    return pos_x

def calculate_top_screen_pos_y(top_screen_res_y):
    pos_y = 0
    return pos_y

def calculate_bottom_screen_pos_x(bottom_screen_res_x):
    pos_x = (device_res_x - bottom_screen_res_x)/2
    return pos_x

def calculate_bottom_screen_pos_y(bottom_screen_res_y):
    pos_y = device_res_y - bottom_screen_res_y
    return pos_y

def print_values(top_screen_res_x, top_screen_res_y, bottom_screen_res_y, bottom_screen_res_x,
                 top_screen_pos_x, top_screen_pos_y, bottom_screen_pos_x, bottom_screen_pos_y):
    
    print("******************************")
    print("-------TOP SCREEN-------")
    print("Top Screen X-Position: ", top_screen_pos_x)
    print("Top Screen Y-Position: ", top_screen_pos_y)
    print("Top Screen Width: ", top_screen_res_x)
    print("Top Screen Height: ", top_screen_res_y)
    print("-------BOTTOM SCREEN-------")
    print("Bottom Screen X-Position: ", bottom_screen_pos_x)
    print("Bottom Screen Y-Position: ", bottom_screen_pos_y)
    print("Bottom Screen Width: ", bottom_screen_res_x)
    print("Bottom Screen Height: ", bottom_screen_res_y)
    print("******************************")

def stretch(stretch_percentage, top_screen_res_x, bottom_screen_res_x):
    new_top_x = top_screen_res_x + (top_screen_res_x * stretch_percentage)
    new_bottom_x = bottom_screen_res_x + (bottom_screen_res_x * stretch_percentage)
    return new_top_x, new_bottom_x

def print_stretched_values(top_screen_res_x, bottom_screen_res_x, top_screen_pos_x, bottom_screen_pos_x):
    print("Top Screen X-Position: ", top_screen_pos_x)


def main():
    while (True):
        reset_res()
        top_screen_res_x = float(get_desired_top_screen_res_x())
        top_screen_res_y = float(calculate_top_screen_res_y(top_screen_res_x))
        bottom_screen_res_y = float(calculate_bottom_screen_res_y(top_screen_res_y))
        bottom_screen_res_x = float(calculate_bottom_screen_res_x(bottom_screen_res_y))
        top_screen_pos_x = float(calculate_top_screen_pos_x(top_screen_res_x))
        top_screen_pos_y = float(calculate_top_screen_pos_y(top_screen_res_y))
        bottom_screen_pos_x = float(calculate_bottom_screen_pos_x(bottom_screen_res_x))
        bottom_screen_pos_y = float(calculate_bottom_screen_pos_y(bottom_screen_res_y))

        print_values(top_screen_res_x, top_screen_res_y, bottom_screen_res_y, bottom_screen_res_x,
                     top_screen_pos_x, top_screen_pos_y, bottom_screen_pos_x, bottom_screen_pos_y)
        
        stretch_prompt = input("Do you want to stretch the screens horizontally? y/n: ")
        if stretch_prompt == 'y':
            stretch_percentage = float(input("How much do you want to stretch by(%): "))
            stretch_percentage = stretch_percentage/100 #a value now between 0 and 1
            top_screen_res_x, bottom_screen_res_x = stretch(stretch_percentage,top_screen_res_x, bottom_screen_res_x)
            top_screen_pos_x = float(calculate_top_screen_pos_x(top_screen_res_x))
            bottom_screen_pos_x = float(calculate_bottom_screen_pos_x(bottom_screen_res_x))

            print("UPDATED VALUES:")
            print_values(top_screen_res_x, top_screen_res_y, bottom_screen_res_y, bottom_screen_res_x,
                     top_screen_pos_x, top_screen_pos_y, bottom_screen_pos_x, bottom_screen_pos_y)
            

if __name__ == "__main__":
    main()