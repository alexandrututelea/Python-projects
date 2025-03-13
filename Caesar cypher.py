alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar_cypher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char not in alphabet:
            output_text += char
        else:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar_cypher(original_text=text,shift_amount=shift,encode_or_decode=direction)

while True:
    user_choice = input("You want to use the cypher again?('yes'/'no'): ")
    if user_choice == "yes":

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar_cypher(original_text=text,shift_amount=shift,encode_or_decode=direction)
    else:
        print("Thanks for using my cypher!")
        break
