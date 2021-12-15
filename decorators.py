from datetime import datetime

def execution_time(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('The execution time was ' + str(time_elapsed.total_seconds()) + 'seconds')
    return wrapper


@execution_time
def random_func():
    for _ in range(1,10000000):
        pass


random_func()