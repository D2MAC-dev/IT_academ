import datetime

def get_current_time():
    # get and return current time some how
    cur_t = datetime.datetime.now().time()
    # return cur_t.hour, cur_t.minute, cur_t.second
    print(cur_t.hour, cur_t.minute, cur_t.second)
    # return time

def print_digits(current_time):
    
# def clear_screen():
#     pass

# def sleep_for_a_while(period):
    pass

if __name__ == "__main__":
    while True:
        current_time = get_current_time()
        print_digits(current_time)
        # clear_screen()
        # sleep_for_a_while(0.3)


