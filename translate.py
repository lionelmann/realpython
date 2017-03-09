#assign user input to variable
phrase = input("Enter some text: ")

#convert phrase to lowercase
phrase = phrase.lower()

#convert phrase to leetspeak
leetspeak = phrase.replace("a", "4")
leetspeak = leetspeak.replace("b", "8")
leetspeak = leetspeak.replace("e", "3")
leetspeak = leetspeak.replace("l", "1")
leetspeak = leetspeak.replace("o", "0")
leetspeak = leetspeak.replace("s", "5")
leetspeak = leetspeak.replace("t", "7")

print(leetspeak)


