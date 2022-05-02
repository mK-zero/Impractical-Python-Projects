import sys, random

print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
        "Bob 'Stinkbug'")

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater')

while True:
    firstName = random.choice(first)

    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit\n ")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")