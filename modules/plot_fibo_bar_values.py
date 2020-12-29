
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_fibo_values(labels, fibo_out):
	x = np.arange(len(labels))
	width = 0.35

	fig, ax = plt.subplots()
	rects1 = ax.bar(x - width/10, fibo_out, width*2, label="Fibonacci Sequence", color="grey")

	ax.set_ylabel('Output')
	ax.set_xticks(x)
	ax.set_xticklabels(labels)
	ax.legend()

	def autolabel(rects):
		for rect in rects:
		    height = rect.get_height()
		    ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() / 2, height),
		                xytext=(0, 3),
		                textcoords="offset points",
		                color="black",
		                ha='center', va='bottom')

	plt.xlabel("Value")
	autolabel(rects1)
	fig.tight_layout()
	plt.show()
