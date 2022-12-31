
ch = input("Enter the character:")

if ch.isupper() :
    ch = ch.lower()
    print("Upper character converted to lowercase: ",ch)

elif ch.islower() :
    ch = ch.upper()
    print("Lowercase character converted to uppercase:",ch)

elif ch.isdigit() :
    print("its a number")
    
else :
    print("its a special character")
