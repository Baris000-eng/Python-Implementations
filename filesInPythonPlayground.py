file= open("file.txt", "r")#read mode 
print(file.readline())#Reads the first line
print(file.read())#Reads the rest of the lines
file.close()#Closing file
#Instead of the above print statements, to read all of the lines in the file.txt, we can call print(file.read()) once 


##################################################
myFile= open("myCustomFile.txt","a")#Append mode 
myFile.write("123456") #Writes 123456 to the end of the file called "myCustomFile.txt"
myFile.close()
##When we run this code multiple times, we can see that 123456's are appended to each other in 1 line at the end of the myCustomFile.txt.

#file.readlines() takes each line of a file and put them inside an array. This function returns an array. 


#file.readlines()[0], this gives the first element having the index 0 in the array.


mainFile= open("mainFile.txt","w")#Write mode, w
mainFile.write("111\n")
mainFile.write("222\n")
mainFile.write("333\n")
mainFile.write("444")#These write methods writes some strings to the lines of the file called "mainFile".
mainFile.close()#Closes the file




