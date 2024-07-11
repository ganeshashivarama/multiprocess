
import concurrent.futures
import threading

def task1(name, num):
    print(name, ' start')
    thread_name = threading.current_thread().name  
    for n in range(num):
        print(thread_name," => Line ",n)
    print(name,' end')

def task2(name, num):
    print(name, ' start')
    thread_name = threading.current_thread().name  
    for n in range(num):
        print(thread_name," => Line ",n)
    print(name,' end')

def task3(name, num):
    print(name, ' start')
    thread_name = threading.current_thread().name  
    for n in range(num):
        print(thread_name," => Line ",n)
    print(name,' end')

if __name__ == '__main__':

    print(threading.current_thread().name, " start")
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    pool.submit(task1, 'task1', 6)
    pool.submit(task2, 'task2', 8)
    pool.submit(task3, 'task3', 10)

    pool.shutdown(wait=True) # wait till all task completed

    print(threading.current_thread().name, " continue 1...")
    print(threading.current_thread().name, " continue 2...")
    print(threading.current_thread().name, " continue 3...")

    print(threading.current_thread().name, " end")
