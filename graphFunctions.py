def plotGraph(totalFloat):
	import matplotlib
	import matplotlib.pyplot as plt
	import numpy as np
	fig=plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	major_ticks = np.arange(0, 9000, 60)
	ax.set_xticks(major_ticks)
	labelsis=["Oct 18","Jan 19","Mar 19","May 19","July 19","Sep 19","Oct 19"]
	ax.set_xticklabels(labels=labelsis)
	plt.plot(totalFloat)
	plt.axhline(0)
	plt.show()
