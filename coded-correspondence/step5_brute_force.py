alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_decode(message, offset):
  decoded_message = ""

  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      decoded_message += alphabet[(character_value + offset) % 26]
    else:
      decoded_message += character

  return decoded_message

def caesar_encode(message, offset):
  encoded_message = ""

  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      encoded_message += alphabet[(character_value - offset) % 26]
    else:
      encoded_message += character

  return encoded_message



message_one = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# Now we'll print the output of `caeser_decode()` for the first message with an offset of 10
print(caesar_decode(message_one))

brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(caesar_decode(brute_force_message, i)))
