#importing NumPy
import numpy as np

#Function to solve the linear system AX=B
def solve_linear_system(A, B):
    #Calculating augmented matrix of A|B to check for infinite solutions
    #the function reshape(-1, 1) converts the 1D matrix B to 2D matrix (kind of converts row matrix to column) which has the dimensions col(B) x 1
    #hstack function of NumPy stacks horizontally the A and reshaped B to form augmented matrix A|B kind of attaching columnar B to A at the end
    augmentedAB=np.hstack((A, B.reshape(-1,1))) 
    rank_A = np.linalg.matrix_rank(A) #Calculating the rank of matrix A using in-built function in NumPy
    rank_aug = np.linalg.matrix_rank(augmentedAB) #Calculating the rank of matrix A using in-built function in NumPy
    if(rank_A < A.shape[0]): #Checking if rank A is less than row shape of A, to check that no of independent rows is less than total rows <=> detA=0
        print("Invalid Matrix A, Please try again") #Printing error message
        return #Returing since invalid input
    A_inv = np.linalg.inv(A) #Calculating inverse using in-built inverse function in NumPy
    res=np.matmul(A_inv, B) #Multiplying the inverse of A and B to get the unique solution
    print(res) #Printing the result of solving 

#Function main
def main():
    n=int(input("Enter N : ")) #Taking input as n
     #Taking inputA, space separated and converting to int by map and converting to list
    inA = list(map(float, input("Enter entries of A, space separated and row wise in a single line").split())) #Taking input until the input is valid
    #Taking inputB, space separated and converting to int by map and converting to list
    inB = list(map(float, input("Enter entries of B, space separated and row wise in a single line").split())) #Taking input until the input is valid
    A=np.array(inA).reshape(n, n) #Converting the 1D input array A into matrix of n x n by reshape
    B=np.array(inB).reshape(n, 1) #Converting the 1D input array B into matrix of n x n by reshape
    solve_linear_system(A, B) #Solving the linear eqn AX=B

#If the file containing the main and not the file in which this file is imported is running the program then call main
if __name__ == "__main__":
    main()