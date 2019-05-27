import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline
%config InlineBackend.figure_format = 'svg'

''' Get directory '''
dir_data = '/home/hector/ros/tfm_ws/src/upat_follower/tests/data/'
dir_test = dir_data + 'plot/la_0-4_spd_1/'
''' Get csv files '''
default_init_path = pd.read_csv(dir_data + 'init.csv', names=['x', 'y', 'z'])
default_cubic_spline_loyal_path = pd.read_csv(dir_data + 'cubic_spline_loyal.csv', names=['x', 'y', 'z'])
default_cubic_spline_path = pd.read_csv(dir_data + 'cubic_spline.csv', names=['x', 'y', 'z'])
default_trajectory = pd.read_csv(dir_data + 'trajectory.csv', names=['x', 'y', 'z'])
normal_dist_linear_interp = pd.read_csv(dir_test + 'normal_dist_linear_interp.csv', names=['Time', 'Spline', 'Linear'])
normal_dist_cubic_spline = pd.read_csv(dir_test + 'normal_dist_cubic_spline.csv', names=['Time', 'Spline', 'Linear'])
normal_dist_cubic_loyal = pd.read_csv(dir_test + 'normal_dist_cubic_loyal_spline.csv', names=['Time', 'Spline', 'Linear'])
normal_dist_trajectory = pd.read_csv(dir_test + 'normal_dist_trajectory.csv', names=['Time', 'Spline', 'Linear'])
current_path_linear_interp = pd.read_csv(dir_test + 'current_path_linear_interp.csv', names=['x', 'y', 'z'])
current_path_cubic_spline = pd.read_csv(dir_test + 'current_path_cubic_spline.csv', names=['x', 'y', 'z'])
current_path_cubic_loyal = pd.read_csv(dir_test + 'current_path_cubic_loyal_spline.csv', names=['x', 'y', 'z'])
current_trajectory = pd.read_csv(dir_test + 'current_trajectory.csv', names=['x', 'y', 'z'])
''' Plot linear interpolation '''
fig1 = plt.figure()
ax1 = Axes3D(fig1)
ax1.plot(default_init_path.x, default_init_path.y, default_init_path.z, 'o', color="0.5")
#ax1.plot(default_init_path.x, default_init_path.y, default_init_path.z, 'y')
ax1.plot(default_init_path.x, default_init_path.y, default_init_path.z, '--', color="0")
ax1.plot(current_path_linear_interp.x, current_path_linear_interp.y, current_path_linear_interp.z, color="0.4")
#plt.title('Linear interpolation')
ax1.legend(['Waypoints', 'Generated path', 'Actual path'])
# fig1.savefig('overleaf/pathmode0.eps', format='eps', dpi=1200)
plt.figure()
#plt.axis([0, 90, 0, 1.8])
plt.plot(normal_dist_linear_interp.Time, normal_dist_linear_interp.Linear)
#plt.title('Normal distance through path')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.ylim(0, 1)
#plt.legend(["Linear"])
# plt.savefig('overleaf/ndistmode0.eps', format='eps', dpi=1200)
plt.show()
print('Linear -> max: {:.3f}, min: {:.3f}, mean: {:.3f}, std: {:.3f}, var: {:.3f}'.format(np.max(normal_dist_linear_interp.Linear), np.min(normal_dist_linear_interp.Linear), np.mean(normal_dist_linear_interp.Linear), np.std(normal_dist_linear_interp.Linear), np.var(normal_dist_linear_interp.Linear)))
print('---------------------------------------------------------------------')
''' Plot cubic loyal spline '''
fig2 = plt.figure()
ax2 = Axes3D(fig2)
ax2.plot(default_init_path.x, default_init_path.y, default_init_path.z, 'o', color="0.5")
#ax2.plot(default_cubic_spline_loyal_path.x, default_cubic_spline_loyal_path.y, default_cubic_spline_loyal_path.z, 'y')
ax2.plot(default_cubic_spline_loyal_path.x, default_cubic_spline_loyal_path.y, default_cubic_spline_loyal_path.z, '--', color="0")
ax2.plot(current_path_cubic_loyal.x, current_path_cubic_loyal.y, current_path_cubic_loyal.z, 'c', color="0.4")
#plt.title('Cubic loyal spline')
ax2.legend(['Waypoints', 'Generated path', 'Actual path'])
# fig2.savefig('overleaf/pathmode1.eps', format='eps', dpi=1200)
plt.figure()
plt.plot(normal_dist_cubic_loyal.Time, normal_dist_cubic_loyal.Spline)
#plt.plot(normal_dist_cubic_loyal.Time, normal_dist_cubic_loyal.Linear)
#plt.title('Normal distance through loyal cubic path')
plt.xlabel('Time')
plt.ylabel('Distance')
#plt.legend(["Spline", "Linear"])
plt.ylim(0, 1)
# plt.savefig('overleaf/ndistmode1.eps', format='eps', dpi=1200)
plt.show()
print('Linear -> max: {:.3f}, min: {:.3f}, mean: {:.3f}, std: {:.3f}, var: {:.3f}'.format(np.max(normal_dist_cubic_loyal.Linear), np.min(normal_dist_cubic_loyal.Linear), np.mean(normal_dist_cubic_loyal.Linear), np.std(normal_dist_cubic_loyal.Linear), np.var(normal_dist_cubic_loyal.Linear)))
print('Spline -> max: {:.3f}, min: {:.3f}, mean: {:.3f}, std: {:.3f}, var: {:.3f}'.format(np.max(normal_dist_cubic_loyal.Spline), np.min(normal_dist_cubic_loyal.Spline), np.mean(normal_dist_cubic_loyal.Spline), np.std(normal_dist_cubic_loyal.Spline), np.var(normal_dist_cubic_loyal.Spline)))
print('---------------------------------------------------------------------')
''' Plot cubic spline '''
fig3 = plt.figure()
ax3 = Axes3D(fig3)
ax3.plot(default_init_path.x, default_init_path.y, default_init_path.z, 'o', color="0.5")
#ax3.plot(default_cubic_spline_path.x, default_cubic_spline_path.y, default_cubic_spline_path.z, 'y')
ax3.plot(default_cubic_spline_path.x, default_cubic_spline_path.y, default_cubic_spline_path.z, '--', color="0")
ax3.plot(current_path_cubic_spline.x, current_path_cubic_spline.y, current_path_cubic_spline.z, 'c', color="0.4")
#plt.title('Cubic spline')
ax3.legend(['Waypoints', 'Generated path', 'Actual path'])
# fig3.savefig('overleaf/pathmode2.eps', format='eps', dpi=1200)
plt.show()
plt.figure()
plt.plot(normal_dist_cubic_spline.Time, normal_dist_cubic_spline.Spline)
#plt.plot(normal_dist_cubic_spline.Time, normal_dist_cubic_spline.Linear)
#plt.title('Normal distance through natural cubic spline')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
#plt.legend(["Spline", "Linear"])
plt.ylim(0, 1)
# plt.savefig('overleaf/ndistmode2.eps', format='eps', dpi=1200)
plt.show()
print('Linear -> max: {:.3f}, min: {:.3f}, mean: {:.3f}, std: {:.3f}, var: {:.3f}'.format(np.max(normal_dist_cubic_spline.Linear), np.min(normal_dist_cubic_spline.Linear), np.mean(normal_dist_cubic_spline.Linear), np.std(normal_dist_cubic_spline.Linear), np.var(normal_dist_cubic_spline.Linear)))
print('Spline -> max: {:.3f}, min: {:.3f}, mean: {:.3f}, std: {:.3f}, var: {:.3f}'.format(np.max(normal_dist_cubic_spline.Spline), np.min(normal_dist_cubic_spline.Spline), np.mean(normal_dist_cubic_spline.Spline), np.std(normal_dist_cubic_spline.Spline), np.var(normal_dist_cubic_spline.Spline)))
print('---------------------------------------------------------------------')
''' Plot trajectory '''
#fig = plt.figure()
#ax = Axes3D(fig)
#ax.plot(default_trajectory.x, default_trajectory.y, default_trajectory.z)
#ax.plot(current_trajectory.x, current_trajectory.y, current_trajectory.z)
#plt.title('Trajectory')
#plt.show()
#plt.figure()
#plt.plot(normal_dist_trajectory.Time, normal_dist_trajectory.Spline)
#plt.plot(normal_dist_trajectory.Time, normal_dist_trajectory.Linear)
#plt.title('Normal distance through trajectory')
#plt.xlabel('Time (s)')
#plt.ylabel('Distance (m)')
#plt.legend(["Spline", "Linear"])
#plt.show()
#print('Linear -> max: {:.3f}, min: {:.3f}, mean: {:.3f}, std: {:.3f}, var: {:.3f}'.format(np.max(normal_dist_trajectory.Linear), np.min(normal_dist_trajectory.Linear), np.mean(normal_dist_trajectory.Linear), np.std(normal_dist_trajectory.Linear), np.var(normal_dist_trajectory.Linear)))
#print('Spline -> max: {:.3f}, min: {:.3f}, mean: {:.3f}, std: {:.3f}, var: {:.3f}'.format(np.max(normal_dist_trajectory.Spline), np.min(normal_dist_trajectory.Spline), np.mean(normal_dist_trajectory.Spline), np.std(normal_dist_trajectory.Spline), np.var(normal_dist_trajectory.Spline)))
#print('---------------------------------------------------------------------')
