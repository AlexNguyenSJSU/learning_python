#import threading
import multiprocessing
import time


def cal_square(numbers):
	print("calculate square number")
	for n in numbers:
		print ('square:', n*n)


def cal_cube(numbers):
	print("calculate cube number \n")
	for n in numbers:
		print ('cube:', n*n*n)

arr = [2,3,7,9]

try:
	t = time.time()
	t1 = multiprocessing.Process(target=cal_square, args=(arr,))
	t2 = multiprocessing.Process(target=cal_cube, args=(arr,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print ("done in ", time.time()- t)
except:
	print ("error")

print("Số lượng cpu : ", multiprocessing.cpu_count())