
from threading import Thread
import threading

def info(title):
    print('\n',title)
    print('module name: ',__name__)
    print('current thread name: ', threading.current_thread().name)  

def myfunc(name):
    info("--myfunc--")
    print("Hello ", name)

if __name__ == '__main__':
    
    info("--main--")
    thread1 = Thread(target=myfunc, args=('Ganesha S',))
    thread2 = Thread(target=myfunc, args=('Anjali B',))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print()

