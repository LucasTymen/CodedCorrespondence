letters = "abcdefghijklmnopqrstuvwxyz"
message = "ok, i've decoded your message. now let's go with next steps on our journey to python."
traduction = ""

for char in message:
    if char in letters:
        char_value = letters.find(char)
        traduction += letters[(char_value - 10) % 26]
    else:
        traduction += char

print(traduction)
