
import sys

type = sys.argv[1]

if type == "t2.micro":

    print("ok we will create freetier instance")
elif type == "t2.medium":
       print("ok we will create instance")

elif type == "t2.large":
       print("ok it will cost you 2 daollar per day")

elif type == "t2.mini":
       print("ok we will create instance")

elif type == "t2.xlarge":
       print("ok it will cost you 3 dollar per day")              
else:
    print("your input is not correct")
    


