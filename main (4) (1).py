#DAY 2 - CAESAR CIPHER
#Encrypts message by shifting the letters by a given number
#def encrypt(msg, shift):
  #Variable initilization, need string with the alphabet and a result string

  #Loop through each letter
    #If its a letter
      #Add the shifted letter to the result
    #If its something else like punctuation
      #Add the space / punctuation to the result
  #Return the result


#Decrypts by shifting back the letters by a given number
#def decrypt(msg, shift):
  #Variable initilization, need string with the alphabet and a result string

  #Loop through each letter
    #If its a letter
      #Get the position of the letter in alpha
        #If it didnt loop around (d to a)
          #subtract the pos by shift
        #If it did loop around (z to c) 
          #subtract also, but add 26

    #Add it to the result
  #Return the result




#ASCII CAESAR CIPHER
#Encrypts message by shifting the ascii by a given number
#def encryptAscii(msg, shift):
  #Create a result string

  #Loop through each character
    #Add shifted ascii letter to result

  #Return result


#Decrypts by shifting back the ascii value by a given number
#def decryptAscii(msg, shift):
  #Create a result string

  #Loop through each letter
    #Add reverted ascii letter to result

  #Return the result
