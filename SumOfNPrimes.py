#Importing math library to use log function to calculate the upper bound of iteration to go till the n'th prime
import math

#Function to validate input n
def validate_input(n):
    try:
        num=int(n) #Trying to typecast n into int 
        if num<0: #Checking for negative input
            print("Please enter some non negative value") #Printing error message
            return False #Returning false for wrong n
    except ValueError: #If the typecast is unsusccessful
        print("Please enter a valid non negative integer") #Printing error message
        return False #Returning false for wrong n
    return True #Returning True if all checks pass
    

def sum_of_n_primes(n):
    primes=[] #Initializing empty list for storing the primes using the Seive algorithm
    sum_of_primes=0 #Initializing the sum variable to 0
    k=15 if n<6 else int(n * (math.log(n) + math.log(math.log(n)))) + 1 #Calculating the upper bound to iterate to reach the n'th prime
    vis=[0]*(k+1) #Initializing the visited list with 0 values to be used in Seive algorithm
    for i in range(2, k+1): #Iterating over till the calculated upper bound
        if(n==0): #Since the bound is approximate, we continue till we get the n'th prime and stop afterwards
            break; #Break the loop after getting the n'th prime
        if vis[i]==1: #If the number is marked visited then continue
            continue
        elif vis[i]==0: #If the number is not visited, then it is a prime 
            primes.append(i) #so append it to primes
            n=n-1; #and decrease n by 1 to count it as a prime
            #Now since i is a prime, mark all it's multiples as visited, since they will no longer remain prime due to i as their factor
            for j in range(i, k+1, i):
                if vis[j]==1: #If the number is already marked visited by some earlier number, then continue
                    continue
                elif vis[j]==0: #Mark the multiples visited
                    vis[j]=1
    for x in primes: #After receiving the n primes, sum them over to get the sum of n primes
        sum_of_primes+=x
    return sum_of_primes #Returning the summed result

#Function main
def main():
    
    while(True): #Looping over until user gives a valid input
        n=(input("Enter n").rstrip().lstrip()) #Prompting user for input n and truncating leading or trailing white spaces
        if validate_input(n)==False: #Continue further only if the validate_input condition holds
            continue
        else:
            break
    n=int(n) #Typecasting n to int
    sum_of_primes=sum_of_n_primes(n) #Calculating the sum of n primes
    print(sum_of_primes) #Printing the sum of n primes

#If the file containing the main and not the file in which this file is imported is running the program then call main
if __name__ == "__main__":
    main()