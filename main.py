import art 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text+=char
    else:
      position = alphabet.index(char)
      if position + shift_amount<= 51:
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        print("Please start againg and choose a smaller shift number\n")
        break
        
      
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  

reset=1
while reset == 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    answer=input("Type 'yes' if you want to go again. Otherwise type 'no':\n" )
    if answer=="no":
        print("Goodbye.:\n")
        reset=0 