# 여러 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4.5, 5, 0.5)
y1 = 2*x**2
y2 = 5*x +30
y3 = 3*x**2

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
#plt.show()

plt.plot(x,y1,x,y2,x,y3)
#plt.show()

plt.plot(x,y1) # 처음 그리기 함수를 수행하면 그래프 창이 자동으로 생성된다
plt.figure() # 새로운 그래프 창을 생성한다

plt.plot(x,y2)
plt.show()