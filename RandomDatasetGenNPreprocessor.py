#Importing NumPy for dataset generation and preprocessing
import numpy as np
#Importing Matplotlib for plotting the datasets
import matplotlib.pyplot as plt
#Importing random to generate random seed
import random
#Importing math to calculate functions
import math

#Set a random seed for reproducibility
def set_random_seed(seed):
    random.seed(seed) #generating random seed using random library
    np.random.seed(seed) #setting the random generated seed

#Function to generate synthetic dataset
def generate_dataset(N, x_min, x_max):
    #Generate N random X values uniformly distributed within xmin and xmax
    X=np.random.uniform(x_min, x_max, N)
    # Randomly generate constants A, B, C, D, E, F
    #A, C and E between -10 to 10 and B, D and F between -5 to 5
    A=random.uniform(-10, 10)
    B=random.uniform(-5, 5)
    C=random.uniform(-10, 10)
    D=random.uniform(-5, 5)
    E=random.uniform(-10, 10)
    F=random.uniform(-5, 5)
    
    #Randomly choose functions f1, f2, f3 from the set
    functions = [np.sin, np.cos, np.tan, np.log, lambda x: x**2, lambda x: x**3] #Declaring the functions list as specified
    f1=random.choice(functions) #Randomly choose f1
    f2=random.choice(functions) #Randomly choose f2
    f3=random.choice(functions) #Randomly choose f3

    #Function to apply log only if x is positive
    def safe_log(x):
        return np.log(x) if x > 0 else 0  # Return 0 if x<=0

    #Condition to check for negative x using any func from NumPy
    if np.any(X <= 0):  # If there are non-positive X values, ensure log is only applied to positive X
        f1 = np.vectorize(lambda x: safe_log(B * x) if f1 == np.log else f1(x)) #Replace with safe_log for f1
        f2 = np.vectorize(lambda x: safe_log(D * x) if f2 == np.log else f2(x)) #Replace with safe_log for f2
        f3 = np.vectorize(lambda x: safe_log(F * x) if f3 == np.log else f3(x)) #Replace with safe_log for f3
        
    Y = A * f1(B * X) + C * f2(D * X) + E * f3(F * X) #Calculating and generating the values of Y
    
    return X, Y #Returning the generated dataset X and Y

#Function to plot scatter plot of X and Y using label,and scatter funcs from matplotlib
def plot_scatter(X, Y):
    plt.figure(figsize=(8, 6)) #keeping figure size 8x6
    plt.scatter(X, Y, color='blue', label='Data points') #Blue colour for the plot and label Data Points
    plt.title("Scatter Plot: X vs Y") #Title as Scatter Plot: X vs Y
    plt.xlabel("X") #Giving xlabel
    plt.ylabel("Y") #Giving ylabel
    plt.legend() #Applying legend for the label datapoints
    plt.grid(True) #Grid display
    plt.show() #Display the plot
    
#Function to plot histogram plot of X and Y using label,and hist funcs from matplotlib
def plot_histogram(X, N):
    #Use the square root rule to determine the number of bins
    bins = int(np.sqrt(N)) #Calculating the number of appropriate bins
    plt.figure(figsize=(8, 6)) #keeping teh figure size as 8x6
    plt.hist(X, bins=bins, color='green', edgecolor='black', label='X Distribution') #providing bins, color as green and label as X distribution
    plt.title("Histogram of X") #Title as Histogram of X
    plt.xlabel("X") #Giving xlabel
    plt.ylabel("Frequency") #Giving ylabel
    plt.legend() #Applying legend for the label X Distribution
    plt.grid(True) #Grid display
    plt.show() #Displaying the plot

#Function to plot box plot of X and Y using label,and boxplot funcs from matplotlib
def plot_box(Y):
    plt.figure(figsize=(8, 6)) #keeping the figure size as 8x6
    #Create the box plot without the 'label' argument since it is only for Y and not multiple data 
    box = plt.boxplot(Y, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue", color="black"), medianprops=dict(color="red", linewidth=2))
    plt.title("Box Plot of Y") #Title as Box Plot of Y
    plt.xlabel("Y") #Giving xlabel
    plt.legend([box["boxes"][0]], ['Y Values'], loc='upper right') #Adding a legend manually after the box plot is created
    plt.grid(True) #Grid display
    plt.show() #Display the plot

#Function to plot line plot of X and Y using label,and plot funcs from matplotlib
def plot_line(X, Y):
    sorted_indices = np.argsort(X) #sort the indices 
    sorted_X = X[sorted_indices] #sort X dataset
    sorted_Y = Y[sorted_indices] #sort Y dataset
    
    plt.figure(figsize=(8, 6)) #keeping teh figure size 8x6
    plt.plot(sorted_X, sorted_Y, color='red', label='Sorted X vs Y') #plotting sorted x and y, color red and label as Sorted X vs Y
    plt.title("Line Plot of Sorted X vs Y") #Title as Line plot of Sorted X vs Y
    plt.xlabel("Sorted X") #Giving xlabel
    plt.ylabel("Y") #Giving ylabel
    plt.legend() #Legend for the label Sorted X vs Y
    plt.grid(True) #Grid display 
    plt.show() #Display the plot

def main():
    set_random_seed(42) #Set the random seed for reproducibility
    N=int(input("Enter N : ")) #Taking input as N
    xmin=int(input("Enter xmin : ")) #Taking xmin input
    xmax=int(input("Enter xmax : ")) #Taking xmax input
    X, Y = generate_dataset(N, xmin, xmax) #Generating random data based on N, xmin and xmax

    plot_scatter(X, Y) #Plotting scatter plot
    plot_histogram(X, N) #Plotting histogram plot
    plot_box(Y) #Plotting box plot
    plot_line(X, Y) #Plotting line plot

#If the file containing the main and not the file in which this file is imported is running the program then call main
if __name__ == "__main__":
    main()