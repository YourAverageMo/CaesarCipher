alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_alphabet = []

# currently using "if" to wrap back around to beginning of list,
# a better way to do this is using modulo (%).


def encrypt(text, shift, direction):
    for i in range(len(alphabet)):
        if i + shift < len(alphabet):
            new_alphabet.append(alphabet[i + shift])
        elif i + shift >= len(alphabet):
            new_alphabet.append(alphabet[i + shift - len(alphabet)])

# seperate functions for wiether the user enters "encode" or "decode"


def encode(text):
    cipher = ''
    for l in text:
        cipher += new_alphabet[alphabet.index(l)]
    print(cipher)


def decode(text, shift):
    cipher = ''
    for l in text:
        cipher += alphabet[alphabet.index(l) - shift]
    print(cipher)


direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift, direction)
if direction == 'encode':
    encode(text)
elif direction == 'decode':
    decode(text, shift)


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
