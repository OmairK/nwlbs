def Encryptor():
    key_pointer = 0
    crypt_columns = {}
    temp = {}
    temp_message = ""

    message = input("Type the message here : ")
    key_i = input("Type the key here : ")

    for chars in key_i:
        temp = {f"{chars}": "", }
        crypt_columns.update(temp)
    # Assigning elements to respective keys (more like distributing cards to players one by one)
    for message_pointer in range(len(message)):
        # Use the previous chars and append a new char to it
        print(message[message_pointer])
        temp_message = crypt_columns.get(f"{key_i[key_pointer]}", "")
        temp_message += message[message_pointer]
        temp_pair = {f'{key_i[key_pointer]}': f'{temp_message}'}
        crypt_columns.update(temp_pair)  # Append the temp message
        key_pointer += 1  # To iterate over the message
        if (key_pointer == len(key_i)):
            key_pointer = 0

    # Display elements according to the column
    encrypted_message = ""
    for i in sorted(crypt_columns.keys()):
        encrypted_message += crypt_columns[i]
    print(encrypted_message)

def Decrypt():
    key_pointer = 0
    crypt_columns = {}
    key_index = {}
    key_index_pointer = 1
    temp_message = ""

     

    message = input("Type the message here : ")
    key_i = input("Type the key here : ")
    message_length = len(message)
    magic_ratio = int(len(message)//len(key_i)
    magic_remainder = int(len(message)%len(key_i))
    
    for chars in key_i:
        temp = {f"{chars}": "", }
        temp_index = {f"{chars}":f"{key_index_pointer}"}
        crypt_columns.update(temp)
        key_index.update(temp_index)
        key_index_pointer += 1
    print(key_index)
    print(crypt_columns)
    for char in sorted(crypt_columns.keys()):
        if(magic_remainder >= int(key_index[char])):
            a = key_pointer+magic_ratio+magic_remainder
            key_i[char]=message[key_pointer:a]
            key_pointer += magic_ratio + magic_remainder
        else:
            a = key_pointer+magic_ratio
            key_i[char]=message[key_pointer:a]
            key_pointer += magic_ratio
    print(crypt_columns)


if __name__ == "__main__":
    Decrypt()
