print("Welcome to The Message encryptor and Decryptor Program \n")

a = int(input("Please Enter \n 1. For Encrypting : \n 2. For Decrypting : \n"))
if a==1:
    c = input("Please Enter your message to be encrypted(only text in smallcase for proper encryption and decryption: \n ")
    g = int(input("Please Enter the type of security from 26 to 64, remember this number to tell the decryptor: \n")) 
    k=c
    for j in range(97,123):
       
        k = k.replace(chr(j),chr(j-g))
    print(k)
if a==2:
    d = input("Please Enter the encrypted code to display the message : \n")
    x = int(input("Please Enter the type of security received from the encryptor(Sender Side) : \n"))
    l=d
    for h in range(97-x,123-x):
        l=l.replace(chr(h),chr(h+x))
    print(l)

f = input("Please press any key to exit : \n")
