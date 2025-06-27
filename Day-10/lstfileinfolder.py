import os



folder = input("give the list of folders names with spaces in between : ").split()

for folder in folder:

  try:
     files = os.listdir(folder)
  except FileNotFoundError:
     print ("please provide valid folder names looks like folder name is does not exist:" +  folder)
     break
  except PermissionError:
     break
  print("=== listing files for the folder: -" + folder )

  for file in files:
       print (file)
