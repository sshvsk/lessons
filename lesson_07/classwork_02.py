



import random


from datetime import datetime


from time import sleep


def my_decorator(func):
    def execute_time():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print("Execution time", end_time - start_time)
    return execute_time

@my_decorator
def random_delay():
    sleep(random.randint(1, 5))


if __name__ == "__main__":
    random_delay()


