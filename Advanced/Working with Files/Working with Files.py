# Python has several functions for creating, reading,
# updating, and deleting files.

#There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# File is in the same place as Python file, if not then would have to add path for text file
f = open("textfile.txt", 'r') # opening
print(f.name,'was opened and its contents is:\n')
print(f.read(),'\n')               # reading
f.close()                     # closing

f = open("textfile.txt", 'r') 
print(f.read(5),'\n')              # Return the first 5 characters
f.close()

f = open("textfile.txt", 'r') 
f.seek(5)                       #Changes the file position to 5
print(f.readline(),'\n')        #Prints the rest of the line
f.close()

# readline captures lines at string values
f = open("textfile.txt", 'r') 
print(f.readline())           # Read first line
print(f.readline(),'\n')      # Read second line
f.close()

# readlines() Reads all lines and captures each line as an element in a list
f = open("textfile.txt", 'r') 
print(f.readlines())      
f.close() 

f = open("textfile.txt", 'r')
for x in f:
  print(x)
f.close()

f = open("textfile_2.txt", 'a')
f.write("The file now has more content.")
f.close()

f = open("textfile_2.txt", 'r')
print(f.read(),'\n')
f.close()

f = open('textfile_2.txt', 'w')
f.write("The content has changed\n")
lines = ['first new line\n','second new line\n']
f.writelines(lines) #writelines[] takes a list and writes it to the file
f.close()

f = open('textfile_2.txt', 'r')
print(f.read(),'\n')
f.close()

f = open('newfile.txt', 'x')
f.close()

# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove('newfile.txt')

# Check if the file exists, then delete it to avoid an error
import os
if os.path.exists("newfile.txt"):
  os.remove("newfile.txt")
else:
  print("The file does not exist")

# To delete an entire folder, use the os.rmdir() method:
# os.rmdir("myfolder")
