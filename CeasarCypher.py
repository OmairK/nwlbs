message = input("Enter the message here : ")
key = int(input("Enter the key here: "))


def Decryptor():
    """
    Decryptor
    """
    c = ""
    for char in message:
        Ckey = key % 26
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
    print(c)


# Encryptor


def Encryptor():
    """
    Encryptor
    """
    c = ""
    for char in message:
        # a=int(char)
        Ckey = key % 26
        if ord(char) in range(97, 123):
            if (ord(char) + key > 122):
                c = c + chr(96+(122-ord(char)+Ckey))
            else:
                c = c + chr(ord(char)+Ckey)
        elif ord(char) in range(65, 91):
            if (ord(char) + Ckey > 91):
                c = c + chr(64+(90-ord(char)+Ckey))
            else:
                c = c + chr(ord(char)+Ckey)
        else:
            c = c + char
    print(c)


def control():
    choice = input(
        "E for encrypting the message \n D for Decrypting the message : ")
    if (choice=='E'):
        return Encryptor()
    elif (choice == 'D'):
        return Decryptor()
    else:
        print("Invalid Choice")
        return control()

if __name__ == "__main__":
    control()