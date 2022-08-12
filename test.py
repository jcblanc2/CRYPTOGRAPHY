import numpy as np

alphabet = [' ', 'a', 'an', 'b', 'ch', 'd', 'e', 'en', 'è', 'f', 'g', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'on', 'ou', 'ò', 'p', 'r', 's', 't', 'v', 'w', 'y', 'z']
exception = ['ch', 'en', 'on', 'ou', 'an']

text = input("Enter text: ").lower()
signal = False

last = text[len(text) - 1]  # The last letter

simple_matrix = []

for letter in text:
    special = ""
    index_letter = text.index(letter)  # get index af latter

    if signal:
        signal = False
        continue

    try:
        # if there's a letter after
        if text[text.index(letter) + 1] is not None:
            second_letter = text[index_letter + 1]  # get the next letter
            special = letter + second_letter  # special combine the actual letter and the next one

        # check if combine in exception
        if special in exception:
            simple_matrix.append(alphabet.index(special))
            text = text[index_letter + 1:]
            signal = True
        else:
            simple_matrix.append(alphabet.index(letter))
            text = text[index_letter + 1:]

    except IndexError:
        special = letter + last

        if special in exception:
            simple_matrix.append(alphabet.index(special))
            text = text[index_letter + 1:]
            signal = True
        else:
            simple_matrix.append(alphabet.index(letter))
            text = text[index_letter + 1:]

while len(simple_matrix) % 3 != 0:
    simple_matrix.append(0)

n = 3
main_matrix = [simple_matrix[i:i + n] for i in range(0, len(simple_matrix), n)]  # make a matrix 3 X 3

# invertible matrix
a = np.array([[1, -2, 2],
              [-1, 1, 3],
              [1, -1, -4]])

# Gauss-Jordan elimination to find a-1
a_1 = np.array([[-1, -10, -8],
                [-1, -6, -5],
                [0, -1, -1]])


# Method to encode a message
def encoding(matrix):
    list_coded_row = []
    for row in matrix:
        row = np.array(row).reshape(np.array(row).shape[0], 1)
        coded_row = np.dot(a, row)
        list_coded_row.append(coded_row)
    return list_coded_row


# Method to display the encoded message
def display_encoded_message():
    list1 = []
    for row in encoding(main_matrix):
        list1.append([str(row).replace("[", "").replace("]", "").replace("array", "").replace("(", "").replace(")",
                                                                                                               "").replace(
            "\n", "")])
    print(list1)


# Method to decode a message
def decoding(matrix):
    list_decoded_row = []
    for row in matrix:
        row = np.array(row).reshape(np.array(row).shape[0], 1)
        decoded_row = np.dot(a_1, row)
        list_decoded_row.append(decoded_row)
    return list_decoded_row


# Method to display the encoded message
def display_decoded_message():
    list2 = []
    for row in decoding(encoding(main_matrix)):
        list2.append([str(row).replace("[", "").replace("]", "").replace("array", "").replace("(", "").replace(")",
                                                                                                               "").replace(
            "\n", "")])
    print(list2)


print("Matrix:")
print(main_matrix)
print("---------------------------------------------------------------------------------------------------------------")
print()
print("Encoded matrix:")
display_encoded_message()
print()
print("---------------------------------------------------------------------------------------------------------------")
print("Decoded matrix:")
display_decoded_message()

# Natacha ansent
