
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_fibo_values(labels, fibo_out):
	x = np.arange(len(labels))  # the label locations
	width = 0.35  # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(x - width/10, fibo_out, width*2, label="Fibonacci Sequence", color="grey")

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Output')
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
