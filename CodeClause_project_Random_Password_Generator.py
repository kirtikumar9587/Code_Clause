import random
pwd = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^(*/)-+=+.:;'><,|}{[]"
randomlen_pwd= int(input("Enter the length for password : "))
ran = "".join(random.sample(pwd,randomlen_pwd))
print("Your Password is : "+ ran)
