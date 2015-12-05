import subprocess

class Window():
    width = 1366
    heigth = 768
    menu_height = 80
    screen_width = width
    screen_height = heigth - menu_height
    half_screen_width = int(screen_width / 2)
    half_screen_heigth = int(screen_height / 2)
    sh = str(screen_height)
    sh2 = str(heigth - 50 )
    # middle_h_point = ( screen_height / 2 - menu_height)
    middle_h_point = ( screen_height / 2 + menu_height / 2 / 2)
    mhp = str( int(middle_h_point))
    hha = str( int(screen_height / 2) )
    w = str(width)
    h = str(heigth)
    hsw = str(half_screen_width)
    hsh = str(half_screen_heigth)


    def window_resize_up(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz", shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1,0,0," + self.w +"," + self.hha , shell=True)

    def window_resize_down(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz" , shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1,0," + self.mhp + "," + self.w + "," + self.hha , shell=True)

    def window_resize_up_left(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz" , shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1,0,0," + self.hsw +"," + self.hha , shell=True)
        # subprocess.call( "wmctrl -r :ACTIVE: -e 1,0,0,682,384" , shell=True)

    def window_resize_up_right(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz" , shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1," + self.hsw + ",0," + self.hsw +"," + self.hha , shell=True)
        # subprocess.call( "wmctrl -r :ACTIVE: -e 1,0,0,682,384" , shell=True)

    def window_resize_down_left(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz" , shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1,0," + self.mhp + "," + self.hsw + "," + self.hha , shell=True)
        # subprocess.call( "wmctrl -r :ACTIVE: -e 1,682,384,682,324" , shell=True)


    def window_resize_down_right(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz" , shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1," + self.hsw + "," + self.mhp + "," + self.hsw + "," + self.hha , shell=True)
        # subprocess.call( "wmctrl -r :ACTIVE: -e 1,682,384,682,324" , shell=True)

    def window_resize_left(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz" , shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1,0,0," + self.hsw + "," + self.sh2 , shell=True)
        # subprocess.call( "wmctrl -r :ACTIVE: -e 1,682,384,682,324" , shell=True)

    def window_resize_right(self):
        subprocess.call( "wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz" , shell=True)
        subprocess.call( "wmctrl -r :ACTIVE: -e 1," + self.hsw + ",0," + self.hsw + "," + self.sh2 , shell=True)
        # subprocess.call( "wmctrl -r :ACTIVE: -e 1,682,384,682,324" , shell=True)



    def resize_window(self, layout):
        if layout == 'left':
            self.window_resize_left()
        elif layout == 'right':
            self.window_resize_right()
        elif layout == 'right':
            self.window_resize_right()
        elif layout == 'top':
            self.window_resize_up()
        elif layout == 'bottom':
            self.window_resize_down()
        elif layout == 'up_left':
            self.window_resize_up_left()
        elif layout == 'up_right':
            self.window_resize_up_right()
        elif layout == 'bottom_left':
            self.window_resize_down_left()
        elif layout == 'bottom_right':
            self.window_resize_down_right()