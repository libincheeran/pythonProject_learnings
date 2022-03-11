import time


# NOTE - this does not work
def my_timer(fun):
    start = time.time_ns()
    fun()
    end = time.time_ns()
    print(f"total time {end - start}")


def my_timer_wrapper(fun):
    def wrapper():
        start = time.time_ns()
        fun()
        end = time.time_ns()
        print(f"total time {end - start}")
    return wrapper




@my_timer_wrapper
def my_real_fun():
    print("hello there")

my_real_fun()