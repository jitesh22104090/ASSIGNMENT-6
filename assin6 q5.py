def alphord(str1):
    lst1=[a for a in str1.split("-")]
    lst1.sort()
    print("-".join(lst1))
alphord(input("Enter hyphen separated sequence: "))