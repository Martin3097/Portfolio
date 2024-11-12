from math import factorial
from math import e
def poisson (x,lamda):
    return e**(-lamda)*(lamda)**x/factorial(x)

def probabilidad(la,va):
    l=[];v=[];p=[1,2,3]
    empate=0; visita=0; local=0;
    for i in range(20):
        l.append(poisson(i,la))
        v.append(poisson(i,va))
    for i in range (20):
        empate += (l[i])*(v[i])
    for i in range(20):
        for k in range(20):
            if k<i:
                local += (l[i])*(v[k])
    for i in range(20):
        for k in range(20):
            if k>i:
                visita += (l[i])*(v[k])
    p[0]=local;p[1]=empate;p[2]=visita;
    return p
    
def LEV(g1,e1,p1,g2,e2,p2):
    proba2=[0,1,2]
    total1=g1+e1+p1; total2=g2+e2+p2
    g1=g1/total1; e1=e1/total1; p1=p1/total1
    g2=g2/total2; e2=e2/total2; p2=p2/total2

    g=g1*1/2+1/2*p2
    e=e1*1/2+1/2*e2
    p=g2*1/2+1/2*p1
    proba2[0]=g; proba2[1]=e; proba2[2]=p
    return proba2
    
def metodo(la,lm,lg,le,lp,va,vm,vg,ve,vp):
    p=[1,2,3]
    L=(1/2)*((1/2)*(probabilidad(la,va)[0])+(1/2)*(probabilidad(lm,vm)[2]))+1/2*LEV(lg,le,lp,vg,ve,vp)[0]
    E=(1/2)*((1/2)*(probabilidad(la,va)[1])+(1/2)*(probabilidad(lm,vm)[1]))+1/2*LEV(lg,le,lp,vg,ve,vp)[1]
    V=(1/2)*((1/2)*(probabilidad(la,va)[2])+(1/2)*(probabilidad(lm,vm)[0]))+1/2*LEV(lg,le,lp,vg,ve,vp)[2]
    p[0]=L;p[1]=E;p[2]=V;
    print("p(l)=",L,"p(e)=",E,"p(v)=",V)