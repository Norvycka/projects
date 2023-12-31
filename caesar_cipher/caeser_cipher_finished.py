alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode": #this fixes wrong input, it will encode by default no matter what you input.
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:         #if/else to fix symbols/numbers/spaces in the given text.
          position = alphabet.index(char)
          new_position = position + shift_amount
          end_text += alphabet[new_position]
        else:
          end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)

while True:
  direction = input("Hi type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  check = input("do you want to use caesar-cipher again?\nenter Y to continue, or any other key to exit.\n")
  if check.upper()=="Y":
      continue
  print("bye")
  exit()