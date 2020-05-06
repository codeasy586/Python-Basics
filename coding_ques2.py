'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
#input the number of test cases
num_test_cases = input("Enter total number of test cases: ")
#list to hold all your test cases
inp_list = list()
for i in range(int(num_test_cases)):
    inp_list.append(input("Enter test case: "))
print(inp_list)

#the output list to hold the number of occurences of a character
out_list = list()

#dictionaries to hold intermediate values
samp_dict = dict()
out_dict = {}
samp_list = list()
global set
global out_var

#function to check if character is already present in the dictionary
def checkKey(samp_dict,key):
    if(key not in samp_dict.keys()):
         set = True
    else:
        set = False
    return set

#function to convert all uppercase character to lowercase characters
def upperTOlower(in_str):
    str_conv = ""
    str_conv = in_str.lower()
    return str_conv

#function to convert final output list to string for representation purposes
def listTostring(list):
    str1 = ""
    for read in list:
        str1 = str1 + read[0] + str(read[1]) + " "
    return str1

for case in inp_list:
    print(case)
    leng = int(len(case))
    i=0
    while(i<leng-1):
        out_var = upperTOlower(case[i])
        hel = checkKey(out_dict,out_var)
        if(hel==True):
            count = 1
            j = i + 1
            while(j<=leng-1):
                if(out_var==case[j]):
                    count = count + 1
                    j = j + 1
                else:
                    j = j + 1
            out_dict[out_var] = count
            i = i + 1
        else:
            i = i + 1
    if(i==leng-1):
        out_var = upperTOlower(case[i])
        count=1
        yo = checkKey(out_dict,out_var)
        if(yo==True):
            out_dict[out_var] = count
    for key,value in out_dict.items():
        out_list.append([key,value])

    out_str = listTostring(out_list)
    print(out_str)

    out_list.clear()
    out_dict.clear()
