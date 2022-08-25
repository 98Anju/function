def vowel():
    a=input("enter any thing-: ")
    i=0 
    vowel=0
    while i<len(a):
        if (a[i] == "a" or a[i] == "A") or (a[i] == "e" or a[i] == "E") or (a[i] == "i" or a[i] == "I") or (a[i] == "o" or a[i] == "O") or (a[i] == "u" or a[i] == "U"):
            vowel=vowel+1
        i=i+1
    print(vowel)
vowel()