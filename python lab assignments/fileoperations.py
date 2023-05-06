# To read or write a file using python.
# o Print everything written in a file.
# o Count, how many lines are there in a file?
# o Count, how many words are there in a file
# o read the content of web page
import  requests
import random
# try:
    
#     count = 0
#     filename = random.choice(["C:/Users/sanik/OneDrive/Desktop/index.html","file.txt"])
#     with  open(filename) as f:
       
#         lines = f.readlines() #Print everything written in a file
#         for i in lines:
#             print(i.strip())
            
#         while True:
#             count += 1
#             line = f.readline()
#             if not line:
#                     break
#             print("Line:",count,line.strip()) #Count, how many lines are there in a file?
#         f.seek(0)
      
#         word = []
#         for line in f:
#             for w in line.split():
#                       word.append(w)
#         print(len(word)," ",word) #Count, how many words are there in a file
        
#         url = "https://www.example.com"
#         response = requests.get(url)
#         if response.status_code == 200:
#             content = response.content
#             print(content,"\n")
            
#         else:
#             print(f"fetching error in responsing {url} : {response.status_code}")
        
        

# except FileNotFoundError:
#     with open("file.txt","w") as f:
#         for i in range(int(input("Enter the number of lines to write in file: "))):
#             print(f.write(input()+"\n"))
def readfile(fname):
    file = open(fname,"r")
    if file:
            for i in file.readlines():
                print(i.strip())
    file.close()
    
    
def writefile(fname):
    with open(fname,"w") as filew:
                for i in range(int(input("How many lines?"))):
                    print(filew.write(input()+"\n"))
                    
def appendfile(fname):
    with open(fname,"a") as filea:
                for i in range(int(input("How many lines to be appended in file?"))):
                    print(filea.write(input()+"\n"))
                    
def readifexistsfile(fname):
   
    readfile(fname)
    file = open(fname,"r+")
    lines = file.readlines()
    file.seek(0)
    for i in range(len(lines)):
        file.write("HPCSA "+lines[i]) 
    file.close()    
            
def writenotexistsfile(fname):
    
    file = open(fname,"w+")
    for i in range(int(input("How many lines you want to write?"))):
        file.write("hpcsa "+input()+"\n")
    file.close()
    readfile(fname)
    
    
while(True):
    try:
    
        menu = int(input("Enter the options : \n1.read the file \n2.write into the file \n3.append the file \
            \n4.if file exists then read and concate 'HPCSA' on each line and then overwrite.\
            \n and if file does not exists then take user input and concate 'hpcsa' and then write into the file.\
            \n6.exit\n"))
        if menu == 1:
            fname = input("Enter the file name : ")
            readfile(fname)           
            print("*****************************************************")
        elif menu == 2:
            fname = input("Enter the file name: ") 
            writefile(fname)
            print("*****************************************************")            
        elif menu == 3:
            fname = input("Enter the filename : ")
            appendfile(fname)
            print("*****************************************************")
        elif menu == 4:
            fname = input("Enter the file name: ")
            if open(fname):
                readifexistsfile(fname)
                print("*****************************************************")
                
                
        elif menu == 6:
            break
        
        else:
            print("Invalid choice!")
            
                
    except FileNotFoundError:
        print("file not found!")
        print("*****************************************************")
        writenotexistsfile(fname)