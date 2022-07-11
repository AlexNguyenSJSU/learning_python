import multiprocessing
import time
import os

def sending(messages, q):
    for each in messages:
        q.put(each)

    print('Parent Process of Sending: ', os.getppid())
    time.sleep(4)
    print('Process id of Sending: ', os.getpid())

def receiving(q):
    print("Elements in Queue are:")

    while not q.empty():
        print(q.get())
    print("Queue is now empty!!!")

    time.sleep(4)
    print('Parent Process of Receiving: ', os.getppid())
    print('Process id of Receiving: ', os.getpid())

if __name__ == "__main__":
    messages = ['Nguyen', 'Quang', 'Hai', 'Pau FC', 'END']

    q = multiprocessing.Queue()

    sending_process = multiprocessing.Process(target=sending, args=(messages, q, ))
    receiving_process = multiprocessing.Process(target=receiving, args=(q, ))

    sending_process.start()
    receiving_process.start()

    sending_process.join()
    receiving_process.join()