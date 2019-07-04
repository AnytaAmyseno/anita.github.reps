#Read a list of integers from user input.
#Find all pairs of numbers in the list whose product is even and whose sum is odd.
#Print out a formatted list of the pairs.
print('-----------------------------------------------------------------------------------------')
print('|                              FINDING INTEGER PAIRS                                    |')
print('-----------------------------------------------------------------------------------------')
print('This is a program which will print pairs of integers whose product is even and sum is odd.')
print('First, user must specify the number of integer to process.')
print('-----------------------------------------------------------------------------------------')

#Initialisation of variable number
number=''

# Initalisation of integer list
integer_list=[]

# Function to check the user input
def check_input(input_str):
    isValid=True
    if not input_str:
        isValid= False
    else:
        if not input_str.isdigit():
            isValid= False
        else:
            if int(input_str)<=0:
                isValid= False
    return isValid

# Function to check integer input
def check_integer(input_str):
    isValid=True
    if not input_str:
        isValid= False
    else:
        if not input_str.lstrip("-").isdigit():
            isValid= False 
        else:
            if len(input_str)>1:
                if input_str[1]=="-":
                     isValid= False 
    return isValid

# User prompt
user_input=input("Please specify how many number you wish to enter : ")

# Checking teh user input, it will repat asking for user input if the input is incorrect
while check_input(user_input)==False:
    print("\n>>> ERROR : Please enter a valid number!. Number cannot be less than 0!")
    user_input=input("Please specify how many number you wish to enter : ")
else:
    number=int(user_input)
    for i in range(number):
        j=i+1
        integer=input("Integer no#"+str(j)+" : ")
        while check_integer(integer)==False:
            print("\n>>> ERROR : Please enter a valid integer!")
            integer=input("Integer no#"+str(j)+" : ")
        else:
            integer_list.append(int(integer))

# Printing inputted integer list
sorted_integer=list(sorted(set(integer_list)))
print("{:40}{:3}{:40}".format("Your integer list (Unique,Sorted)",":",str(sorted_integer)))

#Initilaizing all_pair_list,all_sorted_list,product_even_list and sum_odd_list
all_pair_list=[]
all_sorted_list=[]
product_even_list=[]
sum_odd_list=[]

# Creating pair of integer list
for k in range(len(sorted_integer)):
    for m in range(k+1,len(sorted_integer)):
        pair=[]
        pair.append(sorted_integer[k])
        pair.append(sorted_integer[m])
        all_pair_list.append(pair)
        m=m+1
        
# Sorting integrer pair        
for each in all_pair_list:
    sorted_list=[]
    sorted_list=sorted(set(each))
    all_sorted_list.append(sorted_list)

# Checking all pairs in all_sorted_list
for each in all_sorted_list:
    numb_1=each[0] #number 1
    numb_2=each[1] #number 2
    
    # Calculating product
    product=numb_1*numb_2
    
    # Calculating Sum
    sum_=numb_1+numb_2
    
    # Checking if the product is even
    if product%2==0:
        product_even_list.append(each)
        
    # Checking if the sum is odd
    if sum_%2>0:
        sum_odd_list.append(each)
        
# Printing the integrer list
print("{:40}{:3}{:40}".format("List of Integers pair (Sorted)",":",str(all_sorted_list)))
print("{:40}{:3}{:40}".format("List of Integers whose product is even",":",str(product_even_list)))
print("{:40}{:3}{:40}".format("List of Integers whose sum is odd",":",str(sum_odd_list)))
            
