import numpy as np

# input signal
I = np.array([[1, 2, 3], [4, 5, 6]])
print('I: ', I.shape)
print(I)

 # filter 
F = np.array([[10, 20], [30, 40]])
print('F: ',F.shape)
print(F)
# number columns and rows of the input 
I_row_num, I_col_num = I.shape 

# number of columns and rows of the filter
F_row_num, F_col_num = F.shape

#  calculate the output dimensions
output_row_num = I_row_num + F_row_num - 1
output_col_num = I_col_num + F_col_num - 1
print('output dimension:', output_row_num, output_col_num)
# zero pad the filter
F_zero_padded = np.pad(F, ((output_row_num - F_row_num, 0),
                           (0, output_col_num - F_col_num)),
                        'constant', constant_values=0)
print('F_zero_padded: ', F_zero_padded)
from scipy.linalg import toeplitz

# use each row of the zero-padded F to creat a toeplitz matrix. 
#  Number of columns in this matrices are same as numbe of columns of input signal
toeplitz_list = []
for i in range(F_zero_padded.shape[0]-1, -1, -1): # iterate from last row to the first row
    c = F_zero_padded[i, :] # i th row of the F 
    r = np.r_[c[0], np.zeros(I_col_num-1)] # first row for the toeplitz fuction should be defined otherwise
                                                        # the result is wrong
    toeplitz_m = toeplitz(c,r) # this function is in scipy.linalg library
    toeplitz_list.append(toeplitz_m)
    print('F '+ str(i)+'\n', toeplitz_m)