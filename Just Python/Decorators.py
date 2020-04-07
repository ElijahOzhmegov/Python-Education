def my_decorator(func):
    def wrapper(word):
        print("Something is happening before the function is called.")
        func(word)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee(word):
    print("Whee!")
    print(word)


if __name__ == '__main__':
    say_whee("foobar")
