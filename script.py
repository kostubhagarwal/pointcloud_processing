#reference: https://medium.com/towards-data-science/discover-3d-point-cloud-processing-with-python-6112d9ee38e7

import numpy as np
import laspy as lp

file_cd = "C:/Users/kostu/Desktop/pointcloud_processing/factory_a.las"
output_path="C:/Users/kostu/Desktop/pointcloud_processing/"

#reading in data
point_cloud= lp.read(file_cd)

#formatting data
points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()

#processing
factor=160
decimated_points = points[::factor]

#exporting coordinates to a txt
np.savetxt(output_path+"processed_point_cloud.txt", decimated_points, delimiter=";", fmt="%s")

#visualization
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')
ax.scatter(decimated_points[:,0], decimated_points[:,1], decimated_points[:,2],s=0.01)
plt.show()

