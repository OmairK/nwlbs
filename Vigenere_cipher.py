def Encrypt():
    """
    Encrypt the message using Vigenere Cipher
    """
    message = input("Enter the plain text message: ")
    key = input("Enter the key: ")
    alpha_matrix = []
    for i in range(0, 26):
        beta_matrix = []
        for j in range(65, 91):
            if((j+i) > 90):
                word = (i + j) % 91 + 65
                beta_matrix.append(chr(word))
            else:
                beta_matrix.append(chr(j+i))
        alpha_matrix.append(beta_matrix)

    key_multiplier = int(len(message)/len(key))
    key_remain = len(message) % len(key)
    alpha_key = key_multiplier * key + key[0:key_remain]

    encrypted_message = ''
    for char in range(len(alpha_key)):
        a, b = message[char].upper(), alpha_key[char].upper()
        a, b = ord(a) % 65, ord(b) % 65
        encrypted_message += alpha_matrix[a][b]

    print(encrypted_message)


def Decrypt():
    """
    Decrypt the message using Vigenere Cipher
    """
    message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    alpha_matrix = []
    for i in range(0, 26):
        beta_matrix = []
        for j in range(65, 91):
            if((j+i) > 90):
                word = (i + j) % 91 + 65
                beta_matrix.append(chr(word))
            else:
                beta_matrix.append(chr(j+i))
        alpha_matrix.append(beta_matrix)

    key_multiplier = int(len(message)/len(key))
    key_remain = len(message) % len(key)
    alpha_key = key_multiplier * key + key[0:key_remain]

    decrypt_message = ''
    for char in range(len(alpha_key)):
        a = message.lower()
        b = (ord(alpha_key[char].upper())) % 65
        i = 0
        for j in range(0, 26):
            if(a[char] == alpha_matrix[b][j].lower()):
                decrypt_message += chr(i+65)
                j = 26
            else:
                i += 1
    print(decrypt_message)


def Controller():

    choice = int(input("1)Decrypt 2)Encrypt: "))
    if (choice == 1):
        Decrypt()
    elif(choice == 2):
        Encrypt()


#
if __name__ == "__main__":
    Controller()
