#!/usr/bin/env python3
### Trixing with Fibonacci Sequence ###
# V1

import sys
from modules import plot_fibo_bar_values as pv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np




def fibo(n):
	return n if n <=1 else (fibo(n-1) + fibo(n-2))



def display_sequence(num_arr):
	counter = 0
	fibo_arr = []
	for x in num_arr:
		fibo_arr.append(fibo(x))
		counter += 1
	return fibo_arr



def main():
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	fibo_out = []
	fibo_out = display_sequence(nums)
	for x in fibo_out:
		print(x)
	
	plt_values = pv.Plot_values(nums, fibo_out)
	plt_values.plot_fibo_values()
	plt_values.ebonanacci_plot()



if __name__ == "__main__":
	print(" Fibonacci Sequence and Trixing ")
	main()


