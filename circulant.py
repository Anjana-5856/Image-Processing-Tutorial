# Python program to compute circular  
# convolution of two arrays 
MAX_SIZE = 10; 
  
# Function to find circular convolution 
def convolution(x, h, n, m): 
    row_vec = [0] * MAX_SIZE; 
    col_vec = [0] * MAX_SIZE; 
    out = [0] * MAX_SIZE; 
    circular_shift_mat = [[0 for i in range(MAX_SIZE)]  
                            for j in range(MAX_SIZE)] ; 
  
    # Finding the maximum size between the 
    # two input sequence sizes 
    if(n > m ): 
        maxSize = n; 
    else: 
        maxSize = m; 
  
    # Copying elements of x to row_vec and padding 
    # zeros if size of x < maxSize 
    for i in range(maxSize): 
        if (i >= n): 
            row_vec[i] = 0; 
        else: 
            row_vec[i] = x[i]; 
          
    # Copying elements of h to col_vec and padding 
    # zeros if size of h is less than maxSize 
    for i in range(maxSize): 
        if (i >= m): 
            col_vec[i] = 0; 
        else: 
            col_vec[i] = h[i]; 
          
    # Generating 2D matrix of 
    # circularly shifted elements 
    k = 0; 
    d = 0; 
  
    for i in range(maxSize): 
        curIndex = k - d; 
        for j in range(maxSize): 
            circular_shift_mat[j][i] = \
    row_vec[curIndex % maxSize]; 
            curIndex += 1; 
          
        k = maxSize; 
        d += 1; 
  
    # Computing result by matrix 
    # multiplication and printing results 
    for i in range(maxSize): 
        for j in range(maxSize): 
            out[i] += circular_shift_mat[i][j] * \
        col_vec[j]; 
          
        print(out[i], end = " "); 
  
# Driver program 
if __name__ == '__main__': 
    x = [ 5, 7, 3, 2 ]; 
    n = len(x); 
    h = [ 1, 5 ]; 
    m = len(h); 
  
    convolution(x, h, n, m); 