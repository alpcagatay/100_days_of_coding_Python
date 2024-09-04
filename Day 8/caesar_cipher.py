

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.





# def encrypt(original_text,shift_amount):



# # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
# #  by the shift amount and print the encrypted text.
#     cipher_text = ""
#     for char in original_text:
#         new_char = alphabet.index(char) + int(shift_amount)
#         if new_char > 25:
#             new_char -= 25
#         cipher_text += alphabet[new_char]
#     print(f"Here is the encoded result {cipher_text}")
#if direction == "encode":
#    encrypt(text,shift)

# def decrypt(original_text, shift_amount):
#     decrypted_text = ""

#     for char in original_text:
#         new_char = alphabet.index(char) - int(shift_amount)
#         if new_char > 25:
#             new_char -= 25
#         decrypted_text += alphabet[new_char]
#     print(f"Here is the decoded result {decrypted_text}")

# def ceasar(direction,text,shift):

#     if direction == "encode":
#         encrypt(text,shift)
#     elif direction == "decode":
#         decrypt(text,shift)

def ceasar (original_text, shift_amount,encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode =="decode":
            shift_amount*= -1
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

ceasar(original_text=text,shift_amount=shift,encode_or_decode=direction)


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

