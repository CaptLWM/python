import numpy as np
print(np.arange(0, 10, 2)) # [0 2 4 6 8]
print(np.arange(1, 10)) # [1 2 3 4 5 6 7 8
print(np.arange(5)) # [0 1 2 3 4]
b1 = np.arange(12).reshape(4, 3)
print(b1)
'''
[[ 0 1
[ 3 4
[ 6 7
[ 9 10
'''
print(b1.shape) # (4, 3)
print(np.linspace(1, 10, 10))
# [ 1. 2. 3. 4. 5. 6. 7. 8. 9. 10.]
print(np.linspace(0, np.pi, 20))
'''
[0. 0.16534698 0.33069396 0.49604095 0.66138793 0.82673491
0.99208189 1.15742887 1.32277585 1.48812284 1.65346982 1.8188168
1.98416378 2.14951076 2.31485774 2.48020473 2.64555171 2.81089869
2.97624567 3.14159265]'''