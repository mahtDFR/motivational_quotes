import random, time, sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.075)

with open("quotes.txt") as quotes:
    a = [line.rstrip() for line in quotes]
    quotes.close()

# print("welcome! getting list...")
# print(len(a), "items in list")
# time.sleep(3)

while True:
    if len(a) > 0:
        quote = random.choice(a)
        # print(quote)
        # time.sleep(0.1)
        print_slow(quote)
        print()
        a.remove(quote)
        time.sleep(1)
    else:
        print("That's enough motivation for now.")
        break
