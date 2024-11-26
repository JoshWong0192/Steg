from random import seed
from random import randint

def generate_key(key):
  
  for i in range(0,length):  
       seed(i+1)   
       #print("The seed is:",i+1)
       value = randint(0, 255) #generate a number between 0 - 255 in Decimal which is 0 - FF in Hex
       key.append(value)
       
  #print(key)
  return key


def encryptmsg(intlst,length,key):
     
     encryptlst = [] #The list to store the encrypted numbers
     
     for i in range(0,length):
     
       encrypt = intlst[i] ^ key[i] #Encrypted number by operating XOR to the ascii code and the key
       #print("Encrypted integer: ",encrypt)
       encryptlst.append(encrypt)
     #print("The encrypted list is",encryptlst)
     ciphertext = ''.join(chr(i) for i in encryptlst) #Turn the encrypted number list to cipher text
     
     return encryptlst, ciphertext

def decryptmsg(ciphertext,key):
    cipherlst = list(ciphertext) #Turn the cipher text into a list
    length = len(cipherlst) #The length of the cipher text
    intlst = [] #To store the bit of each character
    decryptlst = [] #To store the decrypted ascii code

    for i in range(0,length):
      intlst.append((ord(cipherlst[i])))

    #print("The integers in the list of converted cipher text:",intlst)

    for i in range(0,length):
      decrypt = intlst[i] ^ key[i]
      decryptlst.append(decrypt)
    
    decrypt_text = ''.join(chr(i) for i in decryptlst) #Turn the decrypted list back to a string
    print("The decrypted text is:", decrypt_text)

def dec_to_binlst(n): #Function to turn decimal to binary list
    
    
    bintemp = [int(x) for x in list('{0:0b}'.format(n))]
    #print("before check bin temp:", binlst)
    while len(bintemp) < 8: #Convert to a 8-bit list
      bintemp.insert(0, 0)
      #print("bin temp:", bintemp)
    
    #print("Bin Temp after insert:", bintemp)
    
    return bintemp    

def get_index_positions(list_of_elems, element):
    ''' Find the position of certain element within a list '''
    index_pos_list = []
    for i in range(len(list_of_elems)):
        if list_of_elems[i] == element:
            index_pos_list.append(i)

    return index_pos_list

def hide_message(textlst,binlst):
 
 position = get_index_positions(textlst, ' ') #Get the position of the spaces within the text

 for i in range(0, len(binlst)):

   if i < len(position): #Check if there are any spaces to be replaced with blank character, if all spaces have been replaced then the blank character will be appended at the end of the text.

     if binlst[i] == 1:
              
         textlst[position[i]] = 'ﾠ' #Unicode-65440 for '1', replace the space with blank character
    
     elif binlst[i] == 0:
                
         textlst[position[i]] = '⠀' #Unicode-10240 for '0'

   else: #If there is no more space left in the text, append the character at the end of the text
     if binlst[i] == 1:
              
         textlst.append('ﾠ') #Unicode-65440 for '1'
    
     elif binlst[i] == 0:
                
         textlst.append('⠀') #Unicode-10240 for '0'
    
    
 steg_text = ''.join(textlst)
 

 return steg_text

def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    
    return decimal


def decrypt_stego(steg_text,key):
    
    unconverted_ascii = [] #To store the decimal number which the number hasn't converted by the key 
    temp = [] #To store the binary numbers extracted from the stego text
    ascii_lst = [] #Store the ascii code
    char_lst = [] #Store the character which converted from ascii list
    for i in range(0,len(steg_text)):
      if steg_text[i] == 'ﾠ':
        temp.append(1)
      elif steg_text[i] == '⠀':
        temp.append(0)
      
      
      if len(temp)==8:
        str_ints =  [str(int) for int in temp]
        binary = int("".join(str_ints))
        print("Binary:",binary)
        decimal = binaryToDecimal(binary)
        print("The decimal num:",decimal)
        unconverted_ascii .append(decimal)

        temp.clear()
        
    
    
    for i in range(0,len(unconverted_ascii )):
      decryptnum = unconverted_ascii[i] ^ key[i]
      ascii_lst.append(decryptnum)
    
    print(ascii_lst)

    for i in range(0,len(ascii_lst)):
      char = chr(ascii_lst[i])
      char_lst.append(char)
    
    print(char_lst)
    decrypted_message = ''.join(char_lst)

    return decrypted_message






secretmsg="meet@9"
 

l = list(secretmsg) #transfer the string into the list
length = len(l)
#print("length: ", length)
print("l is: ", l)
intlst = [] #Store the ascii code of the every characters
key = [] #generate the key for encryption
bintemp = []
binlst = [] #To store the binary numbers in a list
cover_text = "How are you today? I had a very busy day! I travelled 400 miles returning to London. It was windy and rainy. The traffic was bad too. I managed to finish my job, ref No 3789. But I am really tired. If possible, can we cancel tonight’s meeting?"
textlst = list(cover_text) #Convert the cover text into a list in order to insert the secret message

for i in range(0,length): #Turn every characters of the string to the integers
     
     intlst.append((ord(l[i]))) #Turn the character to ASCII code and append it to the list
      
print("ASCII orgin text lst",intlst)    

key = generate_key(key) #generate the key for encrypt and decrypt the text

encryptlst, ciphertext = encryptmsg(intlst,length,key)

for i in range(0,len(encryptlst)): #Turn the encrpyted integers to binary

  bintemp = dec_to_binlst(encryptlst[i]) #Transfer every single character to 8-bit binary

  for x in range(0,len(bintemp)):

    binlst.append(bintemp[x])

print("The encrypted list is",encryptlst)
print("The bin list:", binlst)  


steg_text = hide_message(textlst,binlst) #Generate the steg text 

print("The steg text:", steg_text)

decrypt_message = decrypt_stego(steg_text,key)

print("The decrypted message from the stego text:",decrypt_message)



