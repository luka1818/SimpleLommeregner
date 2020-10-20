#Simple lommeregner
while True:
    print("Regn a + b")
    in1 = input ("a=")
    in2 = input("b=")

    if in1 == "quit":
        break
    
    a = int(in1)
    b = int(in2)
    c = a+b
    if a == 1:
         print("kage")
    else:
        output= "{}+{}={}".format(a,b,c)
        print(output)

