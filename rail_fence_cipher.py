def encrypt():

    message = input('Enter the message you want to encrypt: ')
    key = input('Enter the key to be used for encryption: ')
    key = int(key)
    message_length = len(message)
    encryption_matrix = []
    for t in range(key):
        encryption_matrix_row = [None]*message_length
        encryption_matrix.append(encryption_matrix_row)
    print(encryption_matrix)
    j = 0

    for i in range(message_length):
        if(j != key):
            print(encryption_matrix[j][i])
            encryption_matrix[j][i] = message[i]
            j = j + 1
        elif(j == key):
            k = key - 1
            if(k != 0):
                k = k - 1
                encryption_matrix[k][i] = message[i]
                
                if (k == 0):
                    j = 0

    for i in range(message_length):
        

    print(encryption_matrix)


# def main()


if __name__ == '__main__':
    encrypt()
