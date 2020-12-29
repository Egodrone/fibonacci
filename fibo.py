#!/usr/bin/env python3
### Problem solving and Beer V1

### Fibonacci Sequence ###

import sys
sys.path.insert(1, "/home/hound/Desktop/hulder/fibo/modules")
import plot_fibo_bar_values as pfv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from math import e
from math import pi




def fibo(n):
	return n if n <=1 else (fibo(n-1) + fibo(n-2))



def display_sequence(num_arr):
	counter = 0
	fibo_arr = []
	for x in num_arr:
		fibo_arr.append(fibo(x))
		counter += 1
	return fibo_arr




def ebonanacci_plot(labels, fibo_out):

    tmp_arr = []
    tmp_arr = fibo_out
    counter_e = 0

    for x in fibo_out:
        fibo_out[counter_e] = fibo_out[counter_e] + (1-e**(-fibo_out[counter_e] + pi) + pi)
        print("Ebooonachiii")
        counter_e += 1

	
    x = np.arange(len(labels))
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/10, fibo_out, width*2, label="Ebonanacci Sequence", color="red")

    ax.set_ylabel('Ebonacci Output')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                              color="black",
                                                #rect.color="red",
                            ha='center', va='bottom')

    plt.xlabel("Value")
    autolabel(rects1)
    fig.tight_layout()
    plt.show()




def main():
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	fibo_out = []
	fibo_out = display_sequence(nums)
	for x in fibo_out:
		print(x)
	

	pfv.plot_fibo_values(nums, fibo_out)
	ebonanacci_plot(nums, fibo_out)






if __name__ == "__main__":
	print("Fibonacci Sequence and Trixing")
	main()


