char = (" ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/", "`", "~", " ")
opt = input("Encrypt or Decrypt? ")
if opt == "e":
    text = input("Enter text to encrypt: ")
    etext = ""
    for i in range(len(text)):
        etext = etext + str(char.index(str(text[i]))).zfill(2)
    print("the encoded string is : ",etext)
elif opt == "d":
    text = input("Enter text to decrypt: ")
    dtext = ""
    for i in range(0, len(text), 2):
        counter = str(text[i]) + str(text[i+1])
        dtext = dtext + char[int(counter)]

    print("the decoded string is : ",dtext)

#fin