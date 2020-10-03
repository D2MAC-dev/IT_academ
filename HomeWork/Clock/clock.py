import datetime
from number import *
from time import sleep

def get_current_time():
    # get and return current time some how
    cur_t = datetime.datetime.now().time()
    #print(cur_t.hour, cur_t.minute, cur_t.second)
    return cur_t.hour, cur_t.minute, cur_t.second

def print_digits(cur_t):
#     while True:
#         if  a == 2:
#             yield number['0'][0]
#             yield number['0'][1]
#             yield number['0'][2]
#             yield number['0'][3]
#             yield number['0'][4]
#             yield clear()
#         else:
#             StopIteration

# generator = my_generator()
# for i in generator:
#     print(i)

    
def clear_screen():
    pass

def sleep_for_a_while(period):
    pass

if __name__ == "__main__":
    while True:
        cur_t = get_current_time()
        print_digits(cur_t)
        clear_screen()
        sleep(0.3)


