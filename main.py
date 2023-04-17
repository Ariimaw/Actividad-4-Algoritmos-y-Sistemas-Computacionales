def arii():
    hola = "hola! cuál es tu nombre?"
    error = "pruébelo con menos letras grr"
    print(hola)
    nya = "sacapuntas"
    while 1 < 2**len(error)+283:
        miau = input("")
        if len(miau) > 4:
            print("\nnyaaa ese nombre es muy largo!!")
            print(error)
        else:
            break
    for i in range(1, 3):
        if miau == str(error[-6]+error[-1]+"i"*i):
            miau = str(True)
    print()
    if miau == str(bool("True")):
        jiji = [n for n in error if n in nya and n not in "no socks"]
        for n in jiji:
            print(n, end="")
        print(" encontrada!!")
    else:
        print("adios")
arii()
    