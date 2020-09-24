creds = {'name1': 'pass1', 'name2': 'pass2'}


def auth_required(function):
    def wrapper_decorator(*args, **kwargs):
        login = input("Введите логин : ")
        password = input("Введите пароль :")
        if login not in creds or creds[login] != password:
            return "Authentication required"
        value = function(*args, **kwargs)
        return value

    return wrapper_decorator

@auth_required
def some_func(a, b):
    return a + b

if __name__ == "__main__":
    print(some_func(6, 5)) 

############################

def dec(func):
    def wrapper_decorator(*args, **kwargs):
        args = ("The " + args[0],)
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator


def new_func1():
    return print()

new_func1("Dima")

