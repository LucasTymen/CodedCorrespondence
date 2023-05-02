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



message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

# Now we'll print the output of `caeser_decode()` for the first message with an offset of 10
print(caesar_decode(message_one, 10))

# Now we know what offset to use for the second message, so we use that to solve.
message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(caesar_decode(message_two, 14))
