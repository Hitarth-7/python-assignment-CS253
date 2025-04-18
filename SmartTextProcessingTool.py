#Function to validate input
def validate_input(n, s):
    try: #trying to convert given n to integer
        num=int(n)
        if(num<=0): #Checking for a positive integer n
            print("Please enter a valid registration number") #Printing error message
            return False #Terminate the check since n is wrong input
    except ValueError: #If unable to convert n to integer type successfully
        print("Please enter a valid registration number") #Printing error message
        return False #Terminate the check since n is wrong input
        
    #Initializing capital and small lists for checking if the string contains only letters    
    cap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    smol=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    #Checking for an empty string
    if(s==""):
        print("Please enter a non-empty string") #Printing error message
        return False #Terminate the check since s is wrong input
    else:
        for i in s: #Iterating over the given s char by char
            if i not in cap and i not in smol: #Cheking if each char of s is in cap or smol to pass the letter check
                print("Please enter a valid string that contains only letters") #Printing error message
                return False #Terminate the check since s is wrong input
    
    return True #If all checks passed, return True

#Function to process the string on the basis of parity of n
def process_string(n, s):
    #Declaring vowel and consonant lists to check and replace for odd n condition
    vowels=['a', 'e', 'i', 'o', 'u']
    consonants=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    #declaring result string
    new_s=""
    #Applying checks
    if(n%2):
        for i in range(len(s)): #Iterating over each char of s and processing it for vowels and consonants
            if s[i] in vowels: #If small vowel then capitalize
                new_s+=s[i].upper()
            elif s[i] in consonants: #If capital consonant then convert to small
                new_s+=s[i].lower()
            else:
                new_s+=s[i] #Else copy the string as it is
    else:
        new_s=s[::-1] #If even n condition, then reverse the string
    return new_s #Returning the processed string

#Function to count the set bits of n
def count_set_bits(n):
    ctr=0; #Initializing the counter for counting the set bits
    while(n>0): #iterating over n till it is 0
        if(n%2): #Condition for setting the bit and counting it
           ctr+=1 #Incrementing the counter for set bit
        n=int(n/2) #After each iteration n gets halved
    return ctr #Returning the count of set bits

#Function to extract the substrings of s based on given k
def extract_substrings(s, k):
    substrs=[] #Initilaizing the empty list for substrings
    for i in range(len(s)-k+1): #Iterating over s till len(s)-k+1(exclusive) because the last substring of length k will be at this position
        substrs.append(s[i:i+k]) #Slicing the string at i'th position of size k so start at i and end at i+k(exclusive)
    return substrs #Returning the substrings extracted

#Function for sorting or reversing the substring list on the basis of n and k
def sort_or_reverse(n, s, substrs):
    if (n&len(s)==0): #Check for the condition n&len(s) (bitwise AND)
        new_subs=sorted(substrs) #Sort the list if the condition holds
    else:
        new_subs=substrs[::-1] #Reverse the list if the condition fails
    return new_subs #Returning the processed substring list

#Main function declaration
def main():
    n=input("Enter the registration number") #Taking the registration number input
    '''
    Assuming the string needs to be the main content and not the leading or trailing spaces and hence ignoring them. If the test case needs to
    incorporate the leading and trailing spaces, then the lstrip and rstrip functions can be avoided by commenting them and the validate input
    function will take care of the spaces since the string needs to have letters only.
    '''
    clean_n=n.rstrip() #Cleaning the trailing white spaces
    clean_n=n.lstrip() #Cleaning the leading white spaces
    
    s=input("Enter your content string") #Taking the string s as input
    clean_s=s.rstrip().lstrip() #Cleaning the leading and trailing white spaces
    
    if(validate_input(clean_n, clean_s)): #Proceed further only if the validate input condition holds
        n=int(clean_n) #Setting n as int type for cleaned value
        s=clean_s #Setting s as clean_s
        proc_s=process_string(n, s) #Obtaining the processed string from process_string
        k=count_set_bits(n) #Obtaining k as the set bits of n
        substrs=extract_substrings(proc_s, k) #Extracting substrings of proc_s
        new_subs=sort_or_reverse(n, proc_s, substrs) #Obtaining the final processed substring list
        print(new_subs) #Printing the final output

#If the file containing the main and not the file in which this file is imported is running the program then call main
if __name__ == "__main__":
    main()