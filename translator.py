# my own language
# vowles=V
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.upper() in "AEIOU":
            if letter.isupper():
             translation=translation+"V"
            else :
              translation=translation+"v"
        else:
            translation=translation+letter
    return translation
print(translate(input("Enter a phrase to translate:")))