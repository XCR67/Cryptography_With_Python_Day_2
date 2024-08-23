#DAY 2 - CAESAR CIPHER
#Encrypts message by shifting the letters by a given number
def encrypt(msg, shift):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""
  for i in range(len(msg)): #Go through each letter
    if msg[i].upper() in alpha: #If its a letter
      pos = alpha.index(msg[i].upper())
      result += alpha[(pos + shift) % 26] #Add the shifted letter to the result
    else:
      result += msg[i] #Add the space / punctuation to the result
  return result
#Decrypts my shifting back the letters by a given number
def decrypt(msg, shift):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""
  for i in range(len(msg)): #Go through each letter
    if msg[i].upper() in alpha: #If its a letter
      pos = alpha.index(msg[i].upper()) #Get the position of the letter in alpha
      if pos - shift >= 0: #If it didnt loop around (d to a)
        result += alpha[(pos - shift)]
      else: #If it did loop around (z to c)
        result += alpha[(pos - shift) + 26]
    else:
      result += msg[i] #Add it to the result
  return result
#Caesar Cipher in action
message = encrypt("Hello World!", 15)
print(message)
print(decrypt(message, 15))

#ASCII CAESAR CIPHER
#Encrypts message by shifting the ascii by a given number
def encryptAscii(msg, shift):
  result = ""
  for i in range(len(msg)): #Go through each letter
    #Add shifted ascii letter to result
    result += chr(ord(msg[i]) + shift)
  return result
#Decrypts by shifting back the ascii value by a given number
def decryptAscii(msg, shift):
  result = ""
  for i in range(len(msg)): #Go through each letter
    #Add reverted ascii letter to result
    result += chr(ord(msg[i]) - shift)
  return result
#Caesar Cipher Ascii in action
message = encryptAscii("Hello World!", 15)
print(message)
print(decryptAscii(message, 15))
