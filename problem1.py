'''
@author: Pratik Soni
'''

import math
from math import ceil

def message_encryption(message):
    """
    Funtion Use to Encrypt the message
    Input parameter : Message to encrypt
    Return : Number of possible columns and encrypted messages
    """
    value = int(ceil(math.sqrt(len(message))))
    matrix = [[0 for i in range(value)] for j in range(value)]
    count = 0
    encrypt_msg = ''
    for i in range(value):
        for j in range(value):
            matrix[j][i] = message[count] if count < len(message) else '+'
            count += 1

    for i in range(len(matrix)):
        if i%2 == 0:
            for j in range(len(matrix)):
                encrypt_msg += matrix[i][j]

        else:
            for k in range(len(matrix)-1, -1, -1):
                encrypt_msg += matrix[i][k]

    return value, encrypt_msg


def message_decryption(message):
    """
    Funtion Use to decrypt the message
    Input parameter : Message to decrypt
    Return : Number of possible columns and decrypted message
    """
    value = int(ceil(math.sqrt(len(message))))
    matrix = [[0 for i in range(value)] for j in range(value)]
    count = 0
    decypt_message = ''

    for i in range(len(matrix)):
        if i%2 == 0:
            for j in range(len(matrix)):
                matrix[i][j] = message[count] if count < len(message) else ''
                count += 1

        else:
            for k in range(len(matrix)-1, -1, -1):
                matrix[i][k] = message[count] if count < len(message) else ''
                count += 1

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            decypt_message += matrix[j][i]

    return value, decypt_message.replace('+', '')

if __name__ == '__main__':
    MESSAGE = raw_input("Enter the message to Enrypt :")
    ENCRYPTED_MESSAGE = message_encryption(MESSAGE)
    print ENCRYPTED_MESSAGE
    DECRYPTED_MESSAGE = message_decryption(ENCRYPTED_MESSAGE[1])
    #DECRYPTED_MESSAGE = message_decryption('coct?ruandypey')
    print DECRYPTED_MESSAGE
