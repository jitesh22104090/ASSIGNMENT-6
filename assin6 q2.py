def palindromechk(str1):
    if str1==str1[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
str2=input("Enter string: ")
palindromechk(str2)