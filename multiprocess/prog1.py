
from multiprocessing import Process
import os

def info(title):
    print('\n',title)
    print('module name: ',__name__)
    print('parent process id: ', os.getppid())
    print('process id: ', os.getpid())    

def myfunction(name):
    info('--myfunction--')
    print("Hello ",name)

if __name__ == '__main__':
    info('--main--')
    proc = Process(target=myfunction, args=('Ganesha S',))
    proc.start()
    proc.join()