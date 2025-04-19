#Importing the statistics library
import statistics as st

def analyze_temperatures(temperatures):
    temp_mean=st.mean(temperatures) #Calculating the mean of dataset
    temp_median=st.median(temperatures) #Calculating the median of dataset
    temp_stdev=st.stdev(temperatures) #Calculating the std dev of dataset
    temp_var=st.variance(temperatures) #Calculating the variance of dataset
    print(temp_mean) #Printing the mean of the dataset
    print(temp_median) #Printing the median of the dataset
    print(temp_stdev) #Printing the std dev of the dataset
    print(temp_var) #Printing the variance of the dataset
    return #Return after analysis

#Function main
def main():
    while True: #Looping over until user gives a valid input
        #First take the input which will be space separated data and split it using space as delimeter
        #Since the input by default will be strings, map each substring to an integer
        #Create a list out of the map
        temperatures = list(map(int, input("Enter the data in single line space separated").split())) #Taking input until the input is valid
        if(len(temperatures)==0 or len(temperatures)==1): #Checking for dataset size = 0 or 1, invalid for mean, var and std dev calculation
            print("Please provide more than 1 values") #Printing error message
            continue
        else:
            break
    analyze_temperatures(temperatures) #Analyzing the temperatures for mean, median stddev and var

#If the file containing the main and not the file in which this file is imported is running the program then call main
if __name__ == "__main__":
    main()