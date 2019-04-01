from pynput.mouse import Listener
import logging
from win32gui import FindWindow, GetWindowRect, SetWindowPos
from win32con import HWND_TOPMOST
from win32api import GetSystemMetrics

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

hwnd = FindWindow(None, "Free Virtual Keyboard (www.FreeVirtualKeyboard.com)")

# Used to find the standard dimensions of the window
rect = GetWindowRect(hwnd)
rect_x = rect[0]
rect_y = rect[1]
rect_w = rect[2] - rect_x
rect_h = rect[3] - rect_y

# print(GetSystemMetrics(0), GetSystemMetrics(1))
is1080p = False
if GetSystemMetrics(0) == 1536 and GetSystemMetrics(1) == 864:  # if 1080p then...
    is1080p = True

if is1080p == True:
    SetWindowPos(hwnd, HWND_TOPMOST, 300, 570, 900, 300, 0)
else:
    SetWindowPos(hwnd, HWND_TOPMOST, 1, 1, 900, 300, 0)  # config this
# we may need an if for every common resolution


def on_click1(x, y, button, pressed):

    if pressed:
        # logging.info("Mouse clicked at ===> ({0}, {1})".format(x, y))

        dynamic_rect = GetWindowRect(hwnd)  # this needs to stay dynamic for if window is moved, so inside 'on_click'
        x_window = (dynamic_rect[0] + 8)  # account for difference between mouse and window xy
        y_window = (dynamic_rect[1])

        if is1080p == True:  # if 1080p then...
            # compensation for weird values from GetWindowRect(). Converting resolution to 1080p ?
            x_window = x_window / 80
            x_window = x_window * 100
            x_window = int(round(x_window))

            y_window = y_window / 80
            y_window = y_window * 100
            y_window = int(round(y_window))

        # print("Window X Y  ====>", x_window, y_window)
        # 1rsgprint("Mouse  X Y  ====>", x, y)


# !!!!!!!!!!!!!!!!!!!!!!!!!
#    Coordinate Checker for 1080p
# !!!!!!!!!!!!!!!!!!!!!!!!!

        y_window = y_window + 40  # accounts for title bar pixels

        # needs work around the very edges(1 or 2 pixels off for the sake of having round numbers in the code)

# Row 1
        if y > y_window and y < y_window + 55:  # this range of y values represents the first row in the VK
            if x > x_window and x < x_window + 75:  # these IF's move along the keys in increments of 75 (width of keys)
                print("Esc")
                # logging.info("Esc")
            if x > x_window + 75 and x < x_window + 150:
                print("F1")
                # logging.info("F1")
            if x > x_window + 150 and x < x_window + 225:
                print("F2")
                # logging.info("F2")
            if x > x_window + 225 and x < x_window + 300:
                print("F3")
                # logging.info("F3")
            if x > x_window + 300 and x < x_window + 375:
                print("F4")
                # logging.info("F4")
            if x > x_window + 375 and x < x_window + 450:
                print("F5")
                # logging.info("F5")
            if x > x_window + 450 and x < x_window + 525:
                print("F6")
                # logging.info("F6")
            if x > x_window + 525 and x < x_window + 600:
                print("F7")
                # logging.info("F7")
            if x > x_window + 600 and x < x_window + 675:
                print("F8")
                # logging.info("F8")
            if x > x_window + 675 and x < x_window + 750:
                print("F9")
                # logging.info("F9")
            if x > x_window + 750 and x < x_window + 825:
                print("F10")
                # logging.info("F10")
            if x > x_window + 825 and x < x_window + 900:
                print("F11")
                # logging.info("F11")
            if x > x_window + 900 and x < x_window + 975:
                print("F12")
                # logging.info("F12")
            if x > x_window + 975 and x < x_window + 1104:
                print("Del")
                # logging.info("Del")


# Row 2
        if y > y_window + 55 and y < y_window + 110:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 75:  # these IF's move along the keys in increments of 75 (width of keys)
                print("'")
                # logging.info("'")
            if x > x_window + 75 and x < x_window + 150:
                print("1")
                # logging.info("1")
            if x > x_window + 150 and x < x_window + 225:
                print("2")
                # logging.info("2")
            if x > x_window + 225 and x < x_window + 300:
                print("3")
                # logging.info("3")
            if x > x_window + 300 and x < x_window + 375:
                print("4")
                # logging.info("4")
            if x > x_window + 375 and x < x_window + 450:
                print("5")
                # logging.info("5")
            if x > x_window + 450 and x < x_window + 525:
                print("6")
                # logging.info("6")
            if x > x_window + 525 and x < x_window + 600:
                print("7")
                # logging.info("7")
            if x > x_window + 600 and x < x_window + 675:
                print("8")
                # logging.info("8")
            if x > x_window + 675 and x < x_window + 750:
                print("9")
                # logging.info("9")
            if x > x_window + 750 and x < x_window + 825:
                print("0")
                # logging.info("0")
            if x > x_window + 825 and x < x_window + 900:
                print("-")
                # logging.info("-")
            if x > x_window + 900 and x < x_window + 975:
                print("=")
                # logging.info("=")
            if x > x_window + 975 and x < x_window + 1104:
                print("Backspace")
                # logging.info("Backspace")


# Row 3
        if y > y_window + 110 and y < y_window + 165:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 125:  # these IF's move along the keys in increments of 75 (width of keys)
                print("Tab")
                # logging.info("Tab")
            if x > x_window + 125 and x < x_window + 200:
                print("q")
                # logging.info("q")
            if x > x_window + 200 and x < x_window + 275:
                print("w")
                # logging.info("w")
            if x > x_window + 275 and x < x_window + 350:
                print("e")
                # logging.info("e")
            if x > x_window + 350 and x < x_window + 425:
                print("r")
                # logging.info("r")
            if x > x_window + 425 and x < x_window + 500:
                print("t")
                # logging.info("t")
            if x > x_window + 500 and x < x_window + 575:
                print("y")
                # logging.info("y")
            if x > x_window + 575 and x < x_window + 650:
                print("u")
                # logging.info("u")
            if x > x_window + 650 and x < x_window + 725:
                print("i")
                # logging.info("i")
            if x > x_window + 725 and x < x_window + 800:
                print("o")
                # logging.info("o")
            if x > x_window + 800 and x < x_window + 875:
                print("p")
                # logging.info("p")
            if x > x_window + 875 and x < x_window + 950:
                print("[")
                # logging.info("[")
            if x > x_window + 950 and x < x_window + 1025:
                print("]")
                # logging.info("]")
            if x > x_window + 1025 and x < x_window + 1100:
                print("#")
                # logging.info("#")


# Row 4
        if y > y_window + 165 and y < y_window + 220:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 150:  # these IF's move along the keys in increments of 75 (width of keys
                # key_caps = True  # may need something like this for post log handling
                print("Caps")
                # logging.info("Caps")
            if x > x_window + 150 and x < x_window + 225:
                print("a")
                # logging.info("a")
            if x > x_window + 225 and x < x_window + 300:
                print("s")
                # logging.info("s")
            if x > x_window + 300 and x < x_window + 375:
                print("d")
                # logging.info("d")
            if x > x_window + 375 and x < x_window + 450:
                print("f")
                # logging.info("f")
            if x > x_window + 450 and x < x_window + 525:
                print("g")
                # logging.info("g")
            if x > x_window + 525 and x < x_window + 600:
                print("h")
                # logging.info("h")
            if x > x_window + 600 and x < x_window + 675:
                print("j")
                # logging.info("j")
            if x > x_window + 675 and x < x_window + 750:
                print("k")
                # logging.info("k")
            if x > x_window + 750 and x < x_window + 825:
                print("l")
                # logging.info("l")
            if x > x_window + 825 and x < x_window + 900:
                print(";")
                # logging.info(";")
            if x > x_window + 900 and x < x_window + 975:
                print("'")
                # logging.info("'")
            if x > x_window + 975 and x < x_window + 1104:
                # key_enter = True  # may need something like this for post log handling
                print("Enter")
                # logging.info("Enter")assdllkkkhj62d


# Row 5
        if y > y_window + 220 and y < y_window + 275:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 125:  # these IF's move along the keys in increments of 75 (width of keys
                print("Shift")
                # logging.info("Shift")
            if x > x_window + 125 and x < x_window + 200:
                print(" \ ")  # special character needs spaces(make it string variable and find function to strip spaces
                # logging.info(" \ ")
            if x > x_window + 200 and x < x_window + 275:
                print("z")
                # logging.info("z")
            if x > x_window + 275 and x < x_window + 350:
                print("x")
                # logging.info("x")
            if x > x_window + 350 and x < x_window + 425:
                print("c")
                # logging.info("c")
            if x > x_window + 425 and x < x_window + 500:
                print("v")
                # logging.info("v")
            if x > x_window + 500 and x < x_window + 575:
                print("b")
                # logging.info("b")
            if x > x_window + 575 and x < x_window + 650:
                print("n")
                # logging.info("n")
            if x > x_window + 650 and x < x_window + 725:
                print("m")
                # logging.info("m")
            if x > x_window + 725 and x < x_window + 800:
                print(",")
                # logging.info(",")
            if x > x_window + 800 and x < x_window + 875:
                print(".")
                # logging.info(".")
            if x > x_window + 875 and x < x_window + 950:
                print("/")
                # logging.info("/")
            if x > x_window + 950 and x < x_window + 1100:
                print("Shift")
                # logging.info("Shift")


# Row 6
        if y > y_window + 275 and y < y_window + 330:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 100:  # these IF's move along the keys in increments of 75 (width of keys
                print("Ctrl")
                # logging.info("Ctrl")
            if x > x_window + 100 and x < x_window + 175:  # these IF's move along the keys in increments of 75 (width of keys
                print("Win")
                # logging.info("Win")
            if x > x_window + 175 and x < x_window + 250:  # these IF's move along the keys in increments of 75 (width of keys
                print("Alt")
                # logging.info("Alt")
            if x > x_window + 250 and x < x_window + 690:  # these IF's move along the keys in increments of 75 (width of keys
                print("Space")
                # logging.info("Space")
            if x > x_window + 690 and x < x_window + 790:  # these IF's move along the keys in increments of 75 (width of keys
                print("AltGr")
                # logging.info("AltGr")
            if x > x_window + 790 and x < x_window + 875:  # these IF's move along the keys in increments of 75 (width of keys
                print("Settings")
                # logging.info("Settings")
            if x > x_window + 875 and x < x_window + 950:  # these IF's move along the keys in increments of 75 (width of keys
                print("Ctrl")
                # logging.info("Ctrl")
            if x > x_window + 950 and x < x_window + 1100:  # these IF's move along the keys in increments of 75 (width of keys
                print("Transparency Slider")
                # logging.info("Transparency Slider")








       # print("==================================")





# run continuously
with Listener(on_click=on_click1) as listener:
    listener.join()

