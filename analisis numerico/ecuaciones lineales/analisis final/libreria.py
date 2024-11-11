def EliminarFila(matriz,n,i):
     for j in range(i+1,n+1):
            division=matriz[j][i]/matriz[i][i]
            print("E",j,"--->E",j,"-",[division],"*E",i)
            for k in range (n+2):
                matriz[j][k]=matriz[j][k]-division*matriz[i][k]
def suma(i,n,m,k):
    suma=0
    for j in range(i,n+1):
        suma=suma+ m[i-1][j]*k[j]
    return suma
def cambioMatriz(matriz,n,m,i):
    x=[];y=[]
    for j in range (n+1+1):
        x.append(0)
    for j in range (n+1+1):
        y.append(0)
    for j in range (n+2):
        x[j]=(matriz[m][j])
    for j in range (n+2):
        y[j]=(matriz[i][j])
    for j in range (n+2):
        matriz[i][j]=x[j]
    for j in range (n+2):
        matriz[m][j]=y[j]
def solucion(matriz,n):
    k=[]    
    for i in range (n+1):
        k.append(0)
    k[n]=(matriz[n][n+1]/matriz[n][n])    
    for i in range(n):
        i=n-1-i
        k[i]=(matriz[i][n+1]-suma(i+1,n,matriz,k))/(matriz[i][i])
    for i in range(n+1):
        print("x",i,"=",k[i])
def maxMAtrizRenglon(renglon,matriz,n):
    x=[];
    for j in range (n+1+1):
        x.append(0)
    for j in range(n+1):
        x[j]=abs(matriz[renglon][j])
    return max(x)