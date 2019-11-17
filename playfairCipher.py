import collections
import string


def Encrypt():
    key = input("Enter your message here: ")+string.ascii_lowercase
    message = input("Enter your key here: ")

    key_list = []
    for char in key:
        if(char == 'j'):
            char = 'i'
        key_list.append(char)
    key_list = list(dict.fromkeys(key_list).keys())

    cipher_matrix = []
    for cnt in range(0, 25, 5):
        cipher_matrix.append(key_list[cnt:cnt+5])

    print(cipher_matrix)
    message_list = message.lower().replace(" ", "")
    message_list = list(message_list)
    if(len(message_list) % 2 != 0):
        message_list.append('x')

    for cnt in range(0, len(message_list)+1, 2):
        if(cnt+2 <= len(message_list)):
            if(message_list[cnt] == message_list[cnt+1]):
                message_list[cnt+1] = 'x'
    encrypted_message = []
    a1,a2,a3,a4 = 0,0,0,0
    for cnt in range(0,len(message_list),2):
        for cntrow in range(0,5):
            for cntcol in range(0,5):
                if(cipher_matrix[cntrow][cntcol]==message_list[cnt]):
                    a1,a2 = cntrow,cntcol
                elif(cipher_matrix[cntrow][cntcol]==message_list[cnt+1]):
                    a3,a4 = cntrow,cntcol
        encrypted_message.append(cipher_matrix[a3][a2])
        encrypted_message.append(cipher_matrix[a1][a4])

    print(encrypted_message)




Encrypt()
