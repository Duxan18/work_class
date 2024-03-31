def imprimir_matriz(n, m):
    for i in range(n):
        for j in range(m - i):
            if (i + j) % 2 == 0:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print("")

def main():
    imprimir_matriz(20, 20)

main()