import string


def encrypt (text, num):
    alphabet = list(string.ascii_lowercase)
    index = [i for i in range(26)]
    indexed_dictionary = dict(zip(alphabet, index))
    reversed_indexed_dictionary = dict(zip(index, alphabet))

    current_indices = [] #Indices of text characters acc to indexed_dictionary
    encrypted_indices = [] #Indices after adding num to each item
    encrypted_letters = []
    split_text = list(text.lower())

    final_output_string = ""

    for letter in split_text:
        if letter in alphabet:
            current_indices.append(indexed_dictionary[letter])
    for index in current_indices:
        if (index + num) > 25:
            encrypted_indices.append((index + num) % 26)
        else:
            encrypted_indices.append(index + num)
    for index in encrypted_indices:
        encrypted_letters.append(reversed_indexed_dictionary[index])
    for letter in encrypted_letters:
        final_output_string += letter
    return final_output_string.upper()

def decrypt (text, num):
    alphabet = list(string.ascii_lowercase)
    index = [i for i in range(26)]
    indexed_dictionary = dict(zip(alphabet, index))
    reversed_indexed_dictionary = dict(zip(index, alphabet))

    current_indices = [] #Indices of text characters acc to indexed_dictionary
    decrypted_indices = [] #Indices after adding num to each item
    decrypted_letters = []
    split_text = list(text.lower())

    final_output_string = ""

    for letter in split_text:
        if letter in alphabet:
            current_indices.append(indexed_dictionary[letter])
    for index in current_indices:
        if (index - num) < 0:
            decrypted_indices.append(26 + (index - num))
        else:
            decrypted_indices.append(index - num)
    for index in decrypted_indices:
        decrypted_letters.append(reversed_indexed_dictionary[index])
    for letter in decrypted_letters:
        final_output_string += letter
    return final_output_string.upper()