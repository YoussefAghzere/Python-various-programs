import pyttsx3

book = open(r"book.txt")

book_text = book.readlines()

finalText = book_text[0]

finalText = []


i = 0
for i in range(len(book_text)):
    tmp = book_text[i].split(" ")
    finalText = finalText + tmp

other = []
for i in range(len(finalText)):
    if i%3 == 1:
        finalText[i - 2] += finalText[i-1]
        finalText[i - 2] += finalText[i]

        other.append(finalText[i-2])

engine = pyttsx3.init()

engine.setProperty("rate", 110)
engine.setProperty("voice", 'english')
for i in book_text:
    engine.say(i)
    engine.runAndWait()


