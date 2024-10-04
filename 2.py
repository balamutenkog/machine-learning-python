grade = float(input())
match grade >= float():
    case 4.0:
        print ("A")
    case 3.0:
        print ("B")
    case 2.0: 
        print ("C")
    case 1.0:
        print ("D")
    case _:
        print ("F")

if grade >= 4.0:
    print ("A")
elif grade >= 3.0:
    print ("B")
elif grade >= 2.0:
    print ("C")
elif grade >= 1.0:
    print ("D")
else:
    print ("F")