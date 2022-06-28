'''
#import threading
#import multiprocessing
import time


def cal_square(numbers):
	print("calculate square number")
	for n in numbers:
		#lock.acquire()
		time.sleep(5.5)
		print ('square:', n*n)
		#lock.release()


def cal_cube(numbers):
	print("calculate cube number \n")
	for n in numbers:
		#lock.acquire()
		time.sleep(5.5)
		print ('cube:', n*n*n)
		#lock.release()

arr = [2,3,5,7]

try:
	#lock = threading.Lock()
	t = time.time()
	t1 = threading.Thread(target=cal_square, args=(arr,lock, ))
	t2 = threading.Thread(target=cal_cube, args=(arr,lock, ))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	cal_square(arr)
	cal_cube(arr)
	print ("done in ", time.time()- t)
except:
	print ("error")
'''
import threading
import time


def cal_square(numbers, lock):
	print("calculate square number")
	for n in numbers:
		lock.acquire()
		time.sleep(5.5)
		print ('square:', n*n)
		lock.release()


def cal_cube(numbers, lock):
	print("calculate cube number \n")
	for n in numbers:
		lock.acquire()
		time.sleep(5.5)
		print ('cube:', n*n*n)
		lock.release()

arr = [2,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]

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