# --------------
#Code starts here

#Function to read file
def read_file(path):
    f=open(file_path,'r')
    sentence=f.read()
    f.close()
    return sentence
sample_message=read_file(file_path)
print(sample_message)
    #Opening of the file located in the path in 'read' mode
    
    #Reading of the first line of the file and storing it in a variable
    
    #Closing of the file
    
    #Returning the first line of the file
    
    

#Calling the function to read file

#Printing the line of the file


#Function to fuse message
def read_file(path):
    f=open(file_path_1,mode='r')
    sentence=f.read()
    f.close()
    return sentence
def read_file1(path):
    g=open(file_path_2,mode='r')
    sent=g.read()
    g.close()
    return sent
message_1=read_file(file_path_1)
message_2=read_file1(file_path_2)
print(message_1)
print(message_2)
def fuse_msg(message_a,message_b):
    message_a=int(message_a)
    message_b=int(message_b)
    quotient=message_b//message_a
    return str(quotient)
secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)
    
    #Integer division of two numbers
    
    #Returning the quotient in string format
    
#Calling the function to read file  

#Calling the function to read file


#Calling the function 'fuse_msg'


#Printing the secret message 



#Function to substitute the message
def read_file2(path):
    f=open(file_path_3,mode='r')
    liness=f.read()
    f.close()
    return liness
message_3=read_file2(file_path_3)
print(message_3)

def substitute_msg(message_c):
    if message_c=='Red':
        sub="Army General"
    elif message_c=='Green':
        sub="Data Scientist"
    elif message_c=='Blue':
        sub="Marine Biologist"
    return sub

secret_msg_2=substitute_msg(message_3)  
print(secret_msg_2)
    #If-else to compare the contents of the file
    
    
    #Returning the substitute of the message
    
    

#Calling the function to read file


#Calling the function 'substitute_msg'


#Printing the secret message



#Function to compare message
def read_file3(path):
    f=open(file_path_4,mode='r')
    linesss=f.read()
    f.close()
    return linesss
def read_file4(path):
    g=open(file_path_5,mode='r')
    linessss=g.read()
    g.close()
    return linessss
message_4=read_file3(file_path_4)
message_5=read_file4(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[i for i in a_list if i not in b_list]
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
    
    #Splitting the message into a list
    
    
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file


#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message


#Function to filter message
def read_file6(path):
    f=open(file_path_6,mode='r')
    lines=f.read()
    f.close()
    return lines
message_6=read_file6(file_path_6)
print(message_6)

def extract_msg(message_f):
    a_list=message_f.split()
    even_words=lambda x: len(x)%2==0
    b_list=list(filter(even_words,a_list))
    final_msg=" ".join(b_list)
    return final_msg
secret_msg_4=extract_msg(message_6)
print(secret_msg_4)


    
    #Splitting the message into a list

    
    #Creating the lambda function to identify even length words
    
    
    #Splitting the message into a list
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]




# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message


#Function to write inside a file
secret_msg=" ".join(message_parts)

def write_file(secret_msg,path):
       z=open(file_path,'a+')
       z.write(secret_msg)
       z.close()
write_file(secret_msg,file_path)
print(secret_msg)
    #Opening a file named 'secret_message' in 'write' mode


    #Writing to the file


    #Closing the file


#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


