numn = int(input("Enter your numerator :"))
numd = int(input("Enter your denominator :"))

if numn%numd == 0:
    print('\n' + str(numn) + "is divisible by" + str(numd))
else:
    print('\n' + str(numn) + "isn't divisible by" + str(numd))