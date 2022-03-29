import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    # %2d是将数字按宽度为2，采用右对齐方式输出，若数据位数不到2位，则左边补空格。
    # %02d，和% 2d差不多，只不过左边补0
    print('%2d ->' % new_item, my_list)
