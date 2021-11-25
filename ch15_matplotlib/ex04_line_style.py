# 출력 형식 지정
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,1)
y1 = x
y2 = x+1
y3 = x+2
y4 = x+3

plt.plot(x,y1,x,y2,x,y3,x,y4)
plt.show()

plt.plot(x,y1,'m',x,y2,'y',x,y3,'k',x,y4,'c') # 색상변경
plt.show()

plt.plot(x,y1,'o',x,y2,'^',x,y3,'s',x,y4,'d') # 점만 찍기
plt.show()

plt.plot(x,y1,'-',x,y2,'--',x,y3,':',x,y4,'-.') # 선모양
plt.show()

plt.plot(x,y1,'>-r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.xc') # 선모양
plt.show()

