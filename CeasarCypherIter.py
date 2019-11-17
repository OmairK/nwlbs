message = input("Enter the Encrypted message here : ")

def Decryptor():
    """
    Decryptor
    """
    
    for Ckey in range(1,26):
        c = ""
        for char in message:
            # Ckey = key % 26
            if ord(char) in range(97, 123):
                if (ord(char) - Ckey < 97):
                    c = c + chr(123-(97-ord(char)+Ckey))
                else:
                    c = c + chr(ord(char)-Ckey)
            elif ord(char) in range(65, 91):
                if (ord(char) - Ckey < 65):
                    c = c + chr(91-(65-ord(char)+Ckey))
                else:
                    c = c + chr(ord(char)-Ckey)
            else:
                c = c + char
        print("The key is %d and the decrypted message is %s"c)
        print("\n")

if __name__ =='__main__':
    Decryptor()
