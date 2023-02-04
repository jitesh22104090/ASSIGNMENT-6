def pangram(str1):
    str2=set(str1.lower())
    onlyalph=[a for a in str2 if ord(a) in range(ord("a"),ord("z")+1)]
    if len(onlyalph)==26:
        print("Pangram")
    else:
        print("Not a pangram")
pangram(input("Enter a string: "))