import numpy as np 

import random 

import time 

 

 

 

def add_padding(arr, max_len): 

    num_zeros = max_len - len(arr) 

    padding =  np.zeros(num_zeros, dtype = int) 

    arr = np.append(arr,padding) 

     

    return arr 

 

 

#Generator matrix 

G_size_rows=int(input(" Size of Rows:")) 

G_size_cols=int(input(" Size of Columns :")) 

start1 = time.time() 

G_size_total=G_size_rows*G_size_cols 

G=np.random.randint(1,20,size=(G_size_rows,G_size_cols)) 

print("Generator matrix:\n"+str(G)) 

 

noprimes = set(j for i in  

               range(2, 8) for j in range(i*2, 25, i)) 

primes = [x for x in  

          range(10, 25) if x not in noprimes] 

 

#prime number selection 

P=random.choice((primes)) 

print("\nPrime number for mod operations:"+str(P)) 

 

end1=time.time() 

 

#entering the private key 

n=int(input("Enter the private key (PVK):")) 

start2 = time.time() 

#public key generation 

PB_out=np.power(G,n) 

PBK=np.mod(PB_out,P) 

print("\nPublic Key:\n") 

print(PBK) 

 

print("\nEncryption Process\n") 

end2=time.time() 

#enter the random key for encryption process 

r=int(input("Enter the random number for encryption(r):\n")) 

start3 = time.time() 

pbk_enc= np.power(PBK,r) 

                                                               # formula for encryption  e=((msg + (PBK)^r) MOD P), (G^r mod P)  

pbk_1=np.mod(pbk_enc,P)                                                          #                  C1                 C2 

print("\nPublic Key:\n")                                          # formula for decryption d=(C1-(C2^n)) mod P 

print(pbk_1)                                                       # message =  Different number of characters  

 

 

#message conversion from alphabets to 3X3 matrix  

g=[] 

w=[] 

arr=[] 

end3=time.time() 

print("\nEnter the Message to be encrypted ("+str(G_size_total)+" lettered word please):") 

start4=time.time() 

m=input() 

#n=input() 

def alphabet_position(text): 

    nums = [str(ord(x) - 96) for x in 

            text.lower() if x >= 'a' and x <= 'z'] 

    #print( " ".join(nums)) 

    g.append(nums) 

    

 

 

alphabet_position(m) 

 

 

 

 

for x in np.nditer(g): 

    

    arr.append(x) 

 

     

array=np.append(arr,w) 

 

input_size = len(array) 

 

if input_size< G_size_total: 

   array = add_padding(array, G_size_total) 

 

 

newarr=array.reshape(G_size_rows,G_size_cols) 

   

# using str() to convert each element to string  

res = [[int(ele) for ele in sub] for sub in newarr] 

   

# printing result  

print("\nMessage matrix: " + str(res)) 

 

 

#c1 generation 

enc1= np.add(pbk_1,res) 

fenc1=np.mod(enc1,26) 

 

ma=fenc1.flatten() 

 

lis=ma.tolist() 

 

for i in enumerate(lis): 

    continue 

enc1_a=(''.join(chr(i+96) for i in lis)) 

 

enc1_b=enc1_a.capitalize()   

 

 

#c2 generation 

 

ec2=(np.power(G,r)) 

c2=np.mod(ec2,P) 

 

fc2=np.mod(c2,26) 

ma=fc2.flatten() 

 

lis=ma.tolist() 

 

for i in enumerate(lis): 

    continue 

c2_a=(''.join(chr(i+96) for i in lis)) 

 

c2_b=c2_a.capitalize()   

 

 

#Encryption 

E=("\nafter encryption \n\nc1: \n{} \n  \nc2:\n {}\n".format(enc1,c2)) 

print(E)  

print("The messages after encryption are\n") 

print("c1:"+str(enc1_a)) 

print('c2:'+str(c2_a)) 

 

 

 

 

print("\nDecryption Process\n") 

 

d1_1=np.power(c2,n) 

d1_1_1=np.mod(d1_1,P) 

 

d=(enc1-d1_1_1) 

 

print("Decrypted matrix:") 

print(d) 

 

#Decrypted message 

ma=d.flatten() 

 

lis=ma.tolist() 

 

for i in enumerate(lis): 

    continue 

a=(''.join(chr(i+96) for i in lis)) 

 

if input_size< G_size_total: 

   a = a[:input_size] 

 

b=a.capitalize()   

print("\nThe message after decryption :\n")   

print(b) 

 

end4=time.time() 

final_time=((end1-start1)+(end2-start2)+(end3-start3)+(end4-start4)) 

print("Time taken is:"+str(final_time)[:5]+" MilliSeconds") 
