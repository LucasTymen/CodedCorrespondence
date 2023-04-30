letters = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
traduction = ""

for char in message:
    if char in letters:
        char_value = letters.find(char)
        traduction += letters[(char_value + 10) % 26]
    else:
        traduction += char

print(traduction)
