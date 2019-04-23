import sys

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])


except:
    n1 = int(input(">> "))
    n2 = int(input(">> "))
    print('S == Sim [nome do arquivo.?] & N == nao')
    ar = str(input("\nDeseja salvar esse Arquivo S/N "))
    ar2 = ar.split()
    ar1 = ar[0].upper()


def i2():
    print("nenhum parametro passado")


print('bem vindo ao tabuada 2.0'.capitalize())


def i(n1, n2):
    if sys.platform == "win32" or sys.platform == "win":
        import os
        verde = os.system("color 0a")
    elif sys.platform == "linux":
        verde = "\033[0;31"
        verde
    for i in range(n1 + 1):
        for i2 in range(n2 + 1):
            arq = "{}X{}={}".format(i, i2, i * i2)
            print(len(arq) * "=")
            print(arq)
            s = len(sys.argv) -1
            try:
                if  s == 2:
                    try:
                        aprint("exit")
                    except:
                        pass
                        
                elif sys.argv[3] == "enviar":
                    try:
                        arq1 = open(sys.argv[4], "a")
                        arq1.write(len(arq) * "=" + "\n" + arq + "\n")
                    except:
                        print("voce nao colocou o nome do arquivo a ser salvo e ele sera salvo no arquivo 'tabuada.txt'")
            
            except:
                if ar1 == "S":
                    try:
                        arq2 = open(ar2[1], "a")
                        arq2.write(len(arq) * "=" + "\n" + arq + "\n")
                    except:
                        print(
                            "voce nao colocou o nome do arquivo a ser salvo e ele sera salvo no arquivo 'tabuada.txt'1 ")


i(n1, n2)




