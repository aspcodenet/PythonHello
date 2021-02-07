name = input("Vad heter du?")
age = int(input("Hur gammal är du?"))

print("Hej "+ name)
if age > 48:
    print("Gamling!")
else:    
    print("Ungdom")

for x in range(0,age):
    print("Varv " , x)


