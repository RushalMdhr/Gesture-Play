from pynput.keyboard import Key, Controller
import time

kb = Controller()

def control(angle, movement):
    if angle > 10 and angle < 90:
        if movement=='right':
            return 'right'
        kb.press(Key.right)
        kb.release(Key.left)
        return 'right'
    elif angle > 270 and angle < 350:
        if movement=='left':
            return 'left'
        kb.press(Key.left)
        kb.release(Key.right)
        return 'left'
    else:
        if movement=='none':
            return 'none'
        kb.release(Key.left)
        kb.release(Key.right)
        return 'none'

def pressAcc():
    kb.release(Key.down)
    kb.press(Key.up)

def goReverse():
    kb.release(Key.up)
    kb.press(Key.down)

def releaseAll():
    kb.release(Key.down)
    kb.release(Key.up)