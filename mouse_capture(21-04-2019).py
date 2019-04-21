from pynput.mouse import Listener
import logging
from win32gui import FindWindow, GetWindowRect, SetWindowPos
from win32con import HWND_TOPMOST
from win32api import GetSystemMetrics

caps = 0

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

hwnd = FindWindow(None, "Free Virtual Keyboard (www.FreeVirtualKeyboard.com)")

# Used to find the dimensions of the window
rect = GetWindowRect(hwnd)
rect_x = rect[0]
rect_y = rect[1]
rect_w = rect[2] - rect_x
rect_h = rect[3] - rect_y

# print(GetSystemMetrics(0), GetSystemMetrics(1))
is1080p = False
if GetSystemMetrics(0) == 1536 and GetSystemMetrics(1) == 864:  # if 1080p then...
    is1080p = True

if is1080p:
    SetWindowPos(hwnd, HWND_TOPMOST, 384, 648, 768, 216, 0)  # may need another inside 'on_click' for consistent size

else:
    # 1600x900     position_XY(^^^ / 100)* 96      size_XY (^^^ / 83.33 * 100   not exact? slight adjustment
    SetWindowPos(hwnd, HWND_TOPMOST, 330, 650, 952, 254, 0)  # may need another inside 'on_click' for consistent size


# change caps value f
def changer():
    global caps  # need 'global' keyword to change value of global variable
    caps = (caps + 5) % 10


# lower case keyboard
lower_list = [["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Del"],
              ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "Backspace"],
              ["Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "#"],
              ["Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "Enter"],
              ["Shift", "\ ", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "Shift"],
              ["Ctrl", "Win", "Alt", "Space", "AltGr", "Settings", "Ctrl", "Slider"]]

# upper case keyboard
upper_list = [["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Del"],
              ["¬", "!", "DoubleQuote", "£", "$", "%", "^", "&", "*", "(", ")", "_", "+", "Backspace"],
              ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "~"],
              ["Caps", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "@", "Enter"],
              ["Shift", "|", "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "Shift"],
              ["Ctrl", "Win", "Alt", "Space", "AltGr", "Settings", "Ctrl", "Slider"]]

# keyboard to be used
case_list = [[]]


def on_click1(x, y, button, pressed):

    if pressed:

        # logging.info("Mouse clicked at ===> ({0}, {1})".format(x, y))

        dynamic_rect = GetWindowRect(hwnd)  # this needs to stay dynamic for if window is moved, so inside 'on_click'
        x_window = (dynamic_rect[0] + 10)  # account for difference between mouse and window xy
        y_window = (dynamic_rect[1])

        # if shift/caps is pressed set appropriate keyboard
        if caps == 0:
            case_list = lower_list
        if caps == 5:
            case_list = upper_list

        # Coordinate Checker for 1080p
        if is1080p:  # if 1080p then...
            # Converting VK range of XY 1920x1080
            x_window = x_window / 80
            x_window = x_window * 100
            x_window = int(round(x_window))

            y_window = y_window / 80
            y_window = y_window * 100
            y_window = int(round(y_window))

            y_window = y_window + 40  # accounts for title bar pixels
            x_window = x_window - 3  # need this for

        else:
            y_window = y_window + 30  # title bar pixels - same calc as ^res^ ((40 / 100) * 83.33)
            x_window = x_window - 4

        # needs work around the very edges(1 or 2 pixels off for the sake of having round numbers in the code)

# Row 0
        if y > y_window and y <= y_window + 36:  # this range of y values represents the first row in the VK
            if x > x_window and x < x_window + 64:  # these IF's move along the keys in increments of 64 (width of keys)
                print(case_list[0][0])
                # logging.info("Esc")
            if x > x_window + 64 and x < x_window + 128:
                print(case_list[0][1])
                # logging.info("F1")
            if x > x_window + 128 and x < x_window + 192:
                print(case_list[0][2])
                # logging.info("F2")
            if x > x_window + 192 and x < x_window + 256:
                print(case_list[0][3])
                # logging.info("F3")
            if x > x_window + 256 and x < x_window + 320:
                print(case_list[0][4])
                # logging.info("F4")
            if x > x_window + 320 and x < x_window + 384:
                print(case_list[0][5])
                # logging.info("F5")
            if x > x_window + 384 and x < x_window + 448:
                print(case_list[0][6])
                # logging.info("F6")
            if x > x_window + 448 and x < x_window + 512:
                print(case_list[0][7])
                # logging.info("F7")
            if x > x_window + 512 and x < x_window + 576:
                print(case_list[0][8])
                # logging.info("F8")
            if x > x_window + 576 and x < x_window + 640:
                print(case_list[0][9])
                # logging.info("F9")
            if x > x_window + 640 and x < x_window + 704:
                print(case_list[0][10])
                # logging.info("F10")
            if x > x_window + 704 and x < x_window + 768:
                print(case_list[0][11])
                # logging.info("F11")
            if x > x_window + 768 and x < x_window + 832:
                print(case_list[0][12])
                # logging.info("F12")
            if x > x_window + 832 and x < x_window + 9401:
                print(case_list[0][13])
                # logging.info("Del")


# Row 1
        if y > y_window + 36 and y <= y_window + 72:  # range moves up by 36 for next row
            if x > x_window and x <= x_window + 64:  # these IF's move along the keys in increments of 64(width of keys)
                print(case_list[1][0])
                # logging.info("'")
            if x > x_window + 64 and x <= x_window + 128:
                print(case_list[1][1])
                # logging.info("1")
            if x > x_window + 128 and x <= x_window + 192:
                print(case_list[1][2])
                # logging.info("2")
            if x > x_window + 192 and x <= x_window + 256:
                print(case_list[1][3])
                # logging.info("3")
            if x > x_window + 256 and x <= x_window + 320:
                print(case_list[1][4])
                # logging.info("4")
            if x > x_window + 320 and x <= x_window + 384:
                print(case_list[1][5])
                # logging.info("5")
            if x > x_window + 384 and x <= x_window + 448:
                print(case_list[1][6])
                # logging.info("6")
            if x > x_window + 448 and x <= x_window + 512:
                print(case_list[1][7])
                # logging.info("7")
            if x > x_window + 512 and x <= x_window + 576:
                print(case_list[1][8])
                # logging.info("8")
            if x > x_window + 576 and x <= x_window + 640:
                print(case_list[1][9])
                # logging.info("9")
            if x > x_window + 640 and x <= x_window + 704:
                print(case_list[1][10])
                # logging.info("0")
            if x > x_window + 704 and x <= x_window + 768:
                print(case_list[1][11])
                # logging.info("-")
            if x > x_window + 768 and x <= x_window + 832:
                print(case_list[1][12])
                # logging.info("=")
            if x > x_window + 832 and x <= x_window + 940:  # not sure why this isn't 960 (diagram)
                print(case_list[1][13])
                # logging.info("Backspace")


# Row 2
        if y > y_window + 72 and y <= y_window + 108:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 108:  # these IFs move along the keys in increments of 75 (width of keys)
                print(case_list[2][0])
                # logging.info("Tab")
            if x > x_window + 108 and x < x_window + 172:
                print(case_list[2][1])
                # logging.info("q")
            if x > x_window + 172 and x < x_window + 236:
                print(case_list[2][2])
                # logging.info("w")
            if x > x_window + 236 and x < x_window + 300:
                print(case_list[2][3])
                # logging.info("e")
            if x > x_window + 300 and x < x_window + 364:
                print(case_list[2][4])
                # logging.info("r")
            if x > x_window + 364 and x < x_window + 428:
                print(case_list[2][5])
                # logging.info("t")
            if x > x_window + 428 and x < x_window + 492:
                print(case_list[2][6])
                # logging.info("y")
            if x > x_window + 492 and x < x_window + 556:
                print(case_list[2][7])
                # logging.info("u")
            if x > x_window + 556 and x < x_window + 620:
                print(case_list[2][8])
                # logging.info("i")
            if x > x_window + 620 and x < x_window + 684:
                print(case_list[2][9])
                # logging.info("o")
            if x > x_window + 684 and x < x_window + 748:
                print(case_list[2][10])
                # logging.info("p")
            if x > x_window + 748 and x < x_window + 812:
                print(case_list[2][11])
                # logging.info("[")
            if x > x_window + 812 and x < x_window + 876:
                print(case_list[2][12])
                # logging.info("]")
            if x > x_window + 876 and x < x_window + 940:
                print(case_list[2][13])
                # logging.info("#")


# Row 3
        if y > y_window + 108 and y <= y_window + 144:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 128:  # these IF's move along the keys in increments of 75 (width of keys
                # print(case_list[3][0])
                # logging.info("Caps")
                changer()  # calls function to alternate caps value between 0 and 5(upper/lower)

            if x > x_window + 128 and x < x_window + 192:
                print(case_list[3][1])
                # logging.info("a")
            if x > x_window + 192 and x < x_window + 256:
                print(case_list[3][2])
                # logging.info("s")
            if x > x_window + 256 and x < x_window + 320:
                print(case_list[3][3])
                # logging.info("d")
            if x > x_window + 320 and x < x_window + 384:
                print(case_list[3][4])
                # logging.info("f")
            if x > x_window + 384 and x < x_window + 448:
                print(case_list[3][5])
                # logging.info("g")
            if x > x_window + 448 and x < x_window + 512:
                print(case_list[3][6])
                # logging.info("h")
            if x > x_window + 512 and x < x_window + 576:
                print(case_list[3][7])
                # logging.info("j")
            if x > x_window + 576 and x < x_window + 640:
                print(case_list[3][8])
                # logging.info("k")
            if x > x_window + 640 and x < x_window + 704:
                print(case_list[3][9])
                # logging.info("l")
            if x > x_window + 704 and x < x_window + 768:
                print(case_list[3][10])
                # logging.info(";")
            if x > x_window + 768 and x < x_window + 832:
                print(case_list[3][11])
                # logging.info("'")
            if x > x_window + 832 and x < x_window + 940:
                # key_enter = True  # may need something like this for post log handling
                print(case_list[3][12])
                # logging.info("Enter")


# Row 4
        if y > y_window + 144 and y <= y_window + 180:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 108:  # these IF's move along the keys in increments of 75 (width of keys
                print(case_list[4][0])
                # logging.info("Shift")
            if x > x_window + 108 and x < x_window + 172:
                print(case_list[4][1])
                # logging.info(" \ ")
            if x > x_window + 172 and x < x_window + 236:
                print(case_list[4][2])
                # logging.info("z")
            if x > x_window + 236 and x < x_window + 300:
                print(case_list[4][3])
                # logging.info("x")
            if x > x_window + 300 and x < x_window + 364:
                print(case_list[4][4])
                # logging.info("c")
            if x > x_window + 364 and x < x_window + 428:
                print(case_list[4][5])
                # logging.info("v")
            if x > x_window + 428 and x < x_window + 492:
                print(case_list[4][6])
                # logging.info("b")
            if x > x_window + 492 and x < x_window + 556:
                print(case_list[4][7])
                # logging.info("n")
            if x > x_window + 556 and x < x_window + 620:
                print(case_list[4][8])
                # logging.info("m")
            if x > x_window + 620 and x < x_window + 684:
                print(case_list[4][9])
                # logging.info(",")
            if x > x_window + 684 and x < x_window + 748:
                print(case_list[4][10])
                # logging.info(".")
            if x > x_window + 748 and x < x_window + 812:
                print(case_list[4][11])
                # logging.info("/")
            if x > x_window + 812 and x < x_window + 940:
                print(case_list[4][12])
                # logging.info("Shift")


# Row 5
        if y > y_window + 180 and y <= y_window + 216:  # range moves up by 55 for next row
            if x > x_window and x < x_window + 86:  # these IF's move along the keys in increments of 75 (width of keys
                print(case_list[5][0])
                # logging.info("Ctrl")
            if x > x_window + 86 and x < x_window + 150:
                print(case_list[5][1])
                # logging.info("Win")
            if x > x_window + 150 and x < x_window + 214:
                print(case_list[5][2])
                # logging.info("Alt")
            if x > x_window + 214 and x < x_window + 588:  # these IF's move along the keys in increments of 75 (width of keys
                print(case_list[5][3])
                # logging.info("Space")
            if x > x_window + 588 and x < x_window + 673:  # these IF's move along the keys in increments of 75 (width of keys
                print(case_list[5][4])
                # logging.info("AltGr")
            if x > x_window + 673 and x < x_window + 748:  # these IF's move along the keys in increments of 75 (width of keys
                print(case_list[5][5])
                # logging.info("Settings")
            if x > x_window + 748 and x < x_window + 812:  # these IF's move along the keys in increments of 75 (width of keys
                print(case_list[5][6])
                # logging.info("Ctrl")
            if x > x_window + 812 and x < x_window + 940:  # these IF's move along the keys in increments of 75 (width of keys
                print(case_list[5][7])
                # logging.info("Transparency Slider")

#
# run continuously?
with Listener(on_click=on_click1) as listener:
    listener.join()

