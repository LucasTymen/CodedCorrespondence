letters = "abcdefghijklmnopqrstuvwxyz"
message = ""
traduction = ""
char_value = 0

def decode_cipher(letters, message):
    for char in message:
        if char in letters:
            char_value = letters.find(char)
            decode_traduction += letters[(char_value + 10) % 26]
        else:
            traduction += char

def encode_cipher(letters, message):
    for char in message:
        if char in letters:
            char_value = letters.find(char)
            traduction += letters[(char_value - 10) % 26]
        else:
            encode_traduction += char

    print(encode_traduction)
