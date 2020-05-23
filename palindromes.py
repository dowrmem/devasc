#palindrome sample

pal = input("Enter your string: ")
pCount = 0
for p in pal:
    inversep = pal[::-1]
    if pal == inversep:
        print("Palindrome!")
# pCount += 1
    else:
        print("No palindrome")




