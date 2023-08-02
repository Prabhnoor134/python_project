# import tkinter module
from tkinter import *
import base64
import numpy as np
import random
import time

# creating root object
root = Tk()
# defining size of window
root.geometry("1200x6000")
# setting up the title of window
root.title("Message Encryption and Decryption")
Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="Encryption-Decryption \n Code-Warriors",
                fg="Brown", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

# Initializing variables
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


# labels for the message
lblMsg = Label(f1, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)
# Entry box for the message
txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="light green", justify='right')


txtMsg.grid(row=1, column=1)
# labels for the key
lblkey = Label(f1, font=('arial', 16, 'bold'),
               text="KEY (Only Integer)", bd=16, anchor="w")

lblkey.grid(row=2, column=0)


# Entry box for the key
txtkey = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="light green", justify='right')

txtkey.grid(row=2, column=1)

# labels for the mode
lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)
# Entry box for the mode
txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="light green", justify='right')

txtmode.grid(row=3, column=1)

# labels for the result
lblResult = Label(f1, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, anchor="w")

lblResult.grid(row=2, column=2)

# Entry box for the result
txtResult = Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="light green", justify='right')

txtResult.grid(row=2, column=3)
############################################################################
g=[] 
w=[]
arr=[]
enc=[]
enc1=[]
c2=[]
# res=[[]]

G_size_cols=6
G_size_rows=6
input_size=0
G_size_total=G_size_rows*G_size_cols

noprimes = set(j for i in  range(2, 8) for j in range(i*2, 25, i))
primes = [x for x in  range(10, 25) if x not in noprimes]

   #prime number selection
P=random.choice((primes))
print("\nPrime number for mod operations:"+str(P))

def add_padding(arr, max_len):
   num_zeros = max_len - len(arr)
   padding =  np.zeros(num_zeros, dtype = int)
   arr = np.append(arr,padding)
   return arr

#n=input()
def alphabet_position(text):
   g=[] 
   w=[]
   arr=[]
   nums = [str(ord(x) - 96) for x in text.lower() if x>='a' and x<='z']
   #print( " ".join(nums))
   g.append(nums)
   
   for x in np.nditer(g):
      
      arr.append(x)
      
   
   array=np.append(arr,w)
   input_size = len(array)
   if input_size< G_size_total:
      array = add_padding(array, G_size_total)
   
   newarr=array.reshape(G_size_rows,G_size_cols)
   # using str() to convert each element to string  
   res = [[int(ele) for ele in sub] for sub in newarr]
   return res

####################################################################
def encode(key, msg):
   #Generator matrix
   G=np.random.randint(1,20,size=(G_size_rows,G_size_cols))
   print("Generator matrix:\n"+str(G))

   

  

   #public key generation
   PB_out=np.power(G,int(key))
   PBK=np.mod(PB_out,P)
   print("\nPublic Key:\n")
   print(PBK)
   print("\nEncryption Process\n")

   #enter the random key for encryption process
   ran_list=range(1,10)
   r=random.choice(ran_list)
   print(r)
   pbk_enc= np.power(PBK,r)
   pbk_1=np.mod(pbk_enc,P)                                                          #                  C1                 C2
   print("\nPublic Key:\n")                                          # formula for decryption d=(C1-(C2^n)) mod P
   print(pbk_1)                                                       # message =  Different number of characters  

   #message conversion from alphabets to 3X3 matrix  
   print("\nEnter the Message to be encrypted ("+str(G_size_total)+" lettered word please):")
   # m=input()

   res=alphabet_position(msg)
  

   # printing result  
   print("\nMessage matrix: " + str(res))
   #c1 generation
   enc1= np.add(pbk_1,res)   ###################### C1 matrix
   print('enc1:',enc1)
   fenc1=np.mod(enc1,26)
   print('fenc1:',fenc1)
   ma=fenc1.flatten()
   lis=ma.tolist()
   print('lis:',lis)
   for i in enumerate(lis):
      continue
   enc1_a=(''.join(chr(i+96) for i in lis))

   #c2 generation
   ec2=(np.power(G,r))
   print(G,', ',r)
   print(ec2)
   c2=np.mod(ec2,P)
   print(P)
   print(c2)              ##################### C2 matrix
   fc2=np.mod(c2,26)
   print(fc2)
   ma=fc2.flatten()
   lis=ma.tolist()
   print(lis)
   for i in enumerate(lis):
      continue
   c2_a=(''.join(chr(i+96) for i in lis))
   print(c2_a)

   # print("c1:"+str(enc1_a))
   # print('c2:'+str(c2_a))
   enc = str(enc1_a)+".,.,.,."+str(c2_a)
   print(enc)
   return enc
######################################################################

def decode(key, enc):
   enc=enc.split(".,.,.,.")
   enc1=enc[0]
   c2=enc[1]
   enc1=alphabet_position(enc1)
   c2=alphabet_position(c2)
   print(enc1)
   print(c2)
   
   enc1=np.power(enc1,1)
   d1_1=np.power(c2,int(key))
   
   d1_1_1=np.mod(d1_1,P)
   print(d1_1_1)   
   
   
   
   d=np.zeros((len(enc1),len(enc1[0])))
   for i in range(len(enc1)):
    for j in range(len(enc1[0])):
        
        d[i][j] = abs((enc1[i][j]) - (d1_1_1[i][j]))
        #print(enc1[i][j],', ',d1_1_1[i][j],'=',d[i][j])
   
   d=d.astype(int)
   
   print("Decrypted matrix:")
   print(d)
   
   # Decrypted message
   ma=d.flatten()
   lis=ma.tolist()
   #lis=lis.astype(int)
   
   
   for i in enumerate(lis):
      continue
   a=(''.join(chr(i+96) for i in lis))
   input_size=6
   print(input_size)
   
   if input_size< G_size_total:
      a = a[:input_size]   
   print("\nThe message after decryption :\n")   
   print(a)
   print("dec:", a)
   return "".join(a)


#########################################################################

def Results():
    # print("Message= ", (Msg.get()))

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))

# exit function


def qExit():
    root.destroy()

# Function to reset the window


def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# Show message button
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="powder blue",
                  command=Results).grid(row=7, column=1)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)

# keeps window alive
root.mainloop()
