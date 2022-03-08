import re


a=int(input())
b=int(input())
bm=b
am=a
bin=1
listBin=[]
listA=[]
listB=[]
listR=[]
valbin=0 
resultat=0
t=0
if a<=b:
    while (bin<=a): 
        listBin.append(bin)  
        listB.append(bm)     
        bin=bin+bin  
        bm=bm+bm    
        t=t+1    
        print('t=',t)
    while(am>0):
        valbin=listBin[t-1]
        print('valbin=',valbin)       
 
        if(am-valbin>=0):
            am=am-valbin
            print('am=',am)
            listR.append(t-1)
        print('t=',t)
        t=t-1
    print('listR=',listR)
    print('listBin=',listBin)
    print('listB=',listB)
    for i in listR:
        resultat=resultat+listB[i]
    print('resultat=',resultat)
if b<=a:
    while(bin<=b):
        listBin.append(bin)
        listA.append(am)
        bin=bin+bin
        am=am+am
        t=t+1
    while (bm>0):
        valbin=listBin[t-1]
        if(bm-valbin>=0):
            bm=bm-valbin
            listR.append(t-1)
        t=t-1
    for i in listR:
        resultat=resultat+listA[i]
    print('resultatB=',resultat)

    
  

    
