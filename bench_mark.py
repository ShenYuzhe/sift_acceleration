import numpy as np
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt


img_sizes = [27600, 39000, 50232, 65450, 228000]


extract_naive = [0.000616, 0.000591, 0.000753, 0.000701, 0.000792]
extract_1D = [0.000674, 0.000866, 0.000997, 0.000872, 0.001211]
extract_2D = [0.000733, 0.000841, 0.001397, 0.000901, 0.000876]
extract_path = "scaling_extract_max_min"
plt.gcf()
plt.plot(img_sizes, extract_naive, color='blue')
plt.plot(img_sizes, extract_1D, color='red')
plt.plot(img_sizes, extract_2D, color='black')
plt.xlabel('image size (pixel)')
plt.ylabel('run time (second)')
plt.title('scaling of extracting maxima and minima')
plt.legend(('naive', '1D tile', '2D tile'), loc = 'upper right')
plt.gca().set_xlim((min(img_sizes), max(img_sizes)))
plt.savefig(extract_path)
plt.close()

keypoints_naive = [0.001154, 0.001234, 0.001262, 0.001159, 0.001709]
keypoints_1D = [0.001278, 0.001004, 0.002272, 0.001211, 0.001288]
keypoints_2D = [0.001301, 0.001298, 0.001243, 0.001197, 0.001794]
keypoints_path = "scaling_keypoints"
plt.gcf()
plt.plot(img_sizes, keypoints_naive, color='blue')
plt.plot(img_sizes, keypoints_1D, color='red')
plt.plot(img_sizes, keypoints_2D, color='black')
plt.xlabel('image size')
plt.ylabel('run time (second)')
plt.title('scaling of updating keypoints (pixel)')
plt.legend(('naive', '1D tile', '2D tile'), loc = 'upper right')
plt.gca().set_xlim((min(img_sizes), max(img_sizes)))
plt.savefig(keypoints_path)
plt.close()
