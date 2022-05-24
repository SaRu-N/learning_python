# i=1
# print("printing numbers using while loop:")
# while i<=10:
#     print(i)
#     i+=+1
secret_word="secret"
guess =""
guess_count=0
guess_limit=3
rem_guesses=3
out_of_guesses=False
while guess!=secret_word and not( out_of_guesses):
    if guess_count<guess_limit:
        print("Remainig guesses: "+str(rem_guesses))
        guess=input("Guess a word!:")
        guess_count+=1
        rem_guesses=rem_guesses-1
    else:
        out_of_guesses=True
    
if out_of_guesses:
    print("Oh no! You lose")
else:
    print("WOW! YOU GUESSED IT RIGHT")
