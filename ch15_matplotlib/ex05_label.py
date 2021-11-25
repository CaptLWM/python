# 라벨, 제목, 격자, 범례, 문자열 표시
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4.5, 5, 0.5)
y = 2*x**3

plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

x = np.arange(0,5,1)
y1=x
y2=x+1
y3=x+2
y4=x+3

plt.plot(x,y1,'>-r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['data1','data2','data3','data4'],loc='lower right')
plt.grid(True)
plt.show()

import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

plt.plot(x,y1,'>-r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['data1','data2','data3','data4'],loc='lower right')
plt.grid(True)
plt.show()

plt.plot(x,y1,'>-r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.text(0,6,'문자열 출력1')
plt.text(0,5,'문자열 출력2')
plt.text(3,1,'문자열 출력3')
plt.text(3,0,'문자열 출력4')
plt.show()

