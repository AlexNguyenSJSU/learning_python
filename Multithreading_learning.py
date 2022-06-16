import threading
import multiprocessing
import time


def cal_square(numbers, lock):
	print("calculate square number")
	for n in numbers:
		lock.acquire()
		time.sleep(0.5)
		print ('square:', n*n)
		lock.release()


def cal_cube(numbers, lock):
	print("calculate cube number \n")
	for n in numbers:
		lock.acquire()
		time.sleep(0.5)
		print ('cube:', n*n*n)
		lock.release()

arr = [2,3,7,9]

try:
	lock = threading.Lock()
	t = time.time()
	t1 = threading.Thread(target=cal_square, args=(arr,lock, ))
	t2 = threading.Thread(target=cal_cube, args=(arr,lock, ))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print ("done in ", time.time()- t)
except:
	print ("error")

print("Số lượng cpu : ", multiprocessing.cpu_count())