import math

def getMidPoint(left_hand,right_hand):
    # print("steer handled")
    left_X,left_Y,right_X,right_Y = left_hand[9].x,left_hand[9].y,right_hand[9].x,right_hand[9].y
    mid_X,mid_Y = (left_X+right_X)/2,(left_Y+right_Y)/2
    # print(mid_X,mid_Y)
    return mid_X, mid_Y, left_X, left_Y, right_X , right_Y
    # print("here it is : ",landmarks[9].x,landmarks[9].y)

def getAngle(x1,y1,x2,y2,x3,y3,x4,y4):
    dx1, dy1 = x2-x1, y2-y1  # line 1 direction
    dx2, dy2 = x4-x3, y4-y3  # line 2 direction
    # dot = dx1*dx2 + dy1*dy2
    # mag1 = math.sqrt(dx1**2 + dy1**2)
    # mag2 = math.sqrt(dx2**2 + dy2**2)
    angle = math.degrees(math.atan2(dy2, dx2) - math.atan2(dy1, dx1))
    if angle < 0:
        angle += 360
    return angle