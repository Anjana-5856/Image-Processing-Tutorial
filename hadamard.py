from WalshHadamard import Hadamard2Walsh
import matplotlib.pyplot as plt
import numpy as np
 
M=3; n=2**M
(H,W)=Hadamard2Walsh(n)
# display Hadamard matrix followed by Walsh matrix (n=8)
print(H); print;
print(W)
 
# a visual comparison of Walsh function (j=2)
M=3;
n=2**M
_,W=Hadamard2Walsh(n)
plt.subplot(2,1,1)
plt.step(np.arange(n).tolist(),W[2],where="post")
plt.xlim(0,n)
plt.ylim(-1.1,1.1); plt.ylabel("order M=3")
 
M=8;
n=2**M
_,W=Hadamard2Walsh(n)
plt.subplot(2,1,2)
plt.step(np.arange(n).tolist(),W[2],where="post")
plt.xlim(0,n)
plt.ylim(-1.1,1.1); plt.ylabel("order M=8")
 
plt.show()