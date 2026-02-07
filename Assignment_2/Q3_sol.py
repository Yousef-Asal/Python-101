import pickle as pkl
import matplotlib.pyplot as plt
import numpy as np


with open('Assignment_2/data_q3.pkl','rb') as fil:
    data = pkl.load(fil)

print(data)
fig, axes = plt.subplots(3,1,figsize=(15,10))
ax = np.ravel(axes)
ax[0].plot(data['data3_x'],data['data3_y'],color='g')
ax[0].set_title('Data 1')
ax[1].plot(data['data2_x'],data['data2_y'],color='r')
ax[1].set_title('Data 2')
ax[2].plot(data['data3_x'],data['data3_y'],color='b')
ax[2].set_title('Data 3')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(data['data1_x'],data['data1_y'],color='g',label='2*Sin(x) [data1]')
plt.plot(data['data2_x'],data['data2_y'],color='r',label='Sin(x^2) [data2]')
plt.plot(data['data3_x'],data['data3_y'],color='b',label='4*Sin(x) [data3]')
plt.title("Sinsoudal functions")
plt.xlabel("x")
plt.ylabel("sin values")
plt.legend()
plt.show()