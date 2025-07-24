
# # make the files readable using open function and given filename as parameter
#file = open('me.txt' , 'r')
#file = open('me.txt' , 'w')
#file = open('me.txt' , 'a') # to add the content we use append in the open function.
#content = file.read()
# #line = file.readline()
# lines = file.readlines()
# print(content)
# file.close()


# now I want file to be writable so for that we have to use 


# #content = file.read()
# #line = file.readline()
# lines = file.readlines()
#file.write("\n Hi am devops engineer & N/W engineer \n") # if we write the content it will override existing content or replace it.
# print(content)
# file.close()

#_______________________________________________________________________________________________________________________________________________

# folders & Directories Handling in Python


import os # it will interact with operating system
import os.path # it will check wheather the file exist or not 
import shutil # to remove the folder along with its content recursively. 
# os.mkdir('file1') # it is creatting new file called file1

# a = os.listdir('.')
# print(a)

#y = os.path.exists('me.txt') # function to check whether the file is exist or not
#y = os.path.exists('m.txt') # 
# y = os.path.exists('file1') # its for folder
# print('the folder file1 is exist :', y )

# os.rmdir('file1')
# x = os.listdir('.')
# print(x)

# shutil.rmtree('ap1') # it will do the recursive task
# s = os.listdir('.')
# print(s)





