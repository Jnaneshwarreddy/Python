#need to upadte server.conf file when maximum-connections is 200 and need to write the program to update this 200 to 500.
#1) read the file
#2) create a list variable
#3) open the file in write mode & update maximumu connection its only for update things using if condition.


def update_server_config(file_path, key, value):

    with open (file_path, "r") as file:
      lines = file.readlines()


    with open (file_path, "w") as file:
       for line in lines:
          if key in line:
             file.write(key + "=" +  value + "\n")
          else:
             file.write(line)



update_server_config("server.conf", "MAX_CONNECTIONS", "1000")          
    






