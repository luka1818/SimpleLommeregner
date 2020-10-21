#Simple lommeregner
print("Hej dette er en lommeregner")
while True:
    print("Regn a + b")
    in1 = input ("a=")
    in2 = input("b=")

    if in1 == "quit":
        break
    try:
        a = int(in1)
        b = int(in2)
    except ValueError:
            print("Error: a eller b invalid")
            continue
        
    c = a+b
    if a == 1:
         print("kage")
    else:
        output= "{}+{}={}".format(a,b,c)
        print(output)

