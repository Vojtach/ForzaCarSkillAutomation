# Forza Skill Buy Automation
import pyautogui as gui
import vgamepad as vg
import time

gp = vg.VX360Gamepad()
car_count = 165
menu_op_time = 0.5

def gp_update():
  gp.update()
  time.sleep(0.1)

def gp_move_right():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
  gp_update()
  time.sleep(menu_op_time)

def gp_move_left():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
  gp_update()
  time.sleep(menu_op_time)

def gp_move_up():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
  gp_update()
  time.sleep(menu_op_time)

def gp_move_down():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
  gp_update()
  time.sleep(menu_op_time)

def gp_shoulder_right():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
  gp_update()
  time.sleep(menu_op_time)

def gp_shoulder_left():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
  gp_update()
  time.sleep(menu_op_time)

def gp_button_A():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
  gp_update()
  time.sleep(menu_op_time)

def gp_button_X():
  gp.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
  gp_update()
  gp.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
  gp_update()
  time.sleep(menu_op_time)

def open_menu():
  gui.press('esc')
  time.sleep(menu_op_time)

def open_cars():
  open_menu()
  gp_shoulder_right()
  gp_shoulder_right()

def open_car_collection():
    open_cars()
    gp_move_left()
    gp_button_A()

def open_car_mastery():
  open_cars()
  gp_move_right()
  gp_move_down()
  gp_button_A()
  time.sleep(0.5)

  gp_move_down()
  gp_move_down()
  gp_move_down()

  gp_move_left()
  gp_move_left()
  gp_move_left()

def handle_car_mastery():
  open_car_mastery()
  gp_button_A()
  time.sleep(1.5)
  gui.press('esc')
  time.sleep(menu_op_time)
  gui.press('esc')
  time.sleep(menu_op_time)
  gui.press('esc')
  time.sleep(menu_op_time)

def select_car():
  gui.press('enter')
  time.sleep(menu_op_time)
  gui.press('enter')
  time.sleep(menu_op_time)
  gui.press('enter')
  time.sleep(9)

def set_car_filter_value():
  gp_button_X()

  gp_move_down()
  gp_move_down()
  gp_move_down()
  gp_button_A()

# gui.displayMousePosition()
gui.moveTo(1000, 1000, 1)
gui.leftClick()
gui.press('esc')
time.sleep(menu_op_time)

car_iterator = 1
while(car_iterator <= car_count):
    open_car_collection()
    time.sleep(1.5)
    set_car_filter_value()

    gp_move_up()
    gp_move_left()

    select_car()
    handle_car_mastery()

    car_iterator += 1

car_iterator = 1
while(car_iterator <= car_count):
    open_car_collection()
    time.sleep(1.5)
    set_car_filter_value()

    gp_move_down()
    gp_move_left()

    select_car()
    handle_car_mastery()

    car_iterator += 1