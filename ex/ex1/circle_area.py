import math
import sys

PIE = math.pi

def circle_area(radius) :
    a = PIE * radius * radius
    return a

arg = sys.argv
if len(arg) == 1:
    print('入力値がありません')
elif not arg[1].isdigit():
    print('数字を入力してください')
else :
    result = circle_area(int(arg[1]))
    print('{0}'.format(result))