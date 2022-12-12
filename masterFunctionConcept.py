import string
from random import *

alfabe=string.ascii_letters
numeriq=string.digits
alfanimerik=alfabe+numeriq

# 1-kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def invesmo(mo):
    print(mo[::-1]) 

# 2-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
def kodalealeyatwa():
   # alfabe=string.ascii_letters
    nkarackte=randint(1, 61)
    kod=""
    for i in range(nkarackte):
        index=randint(0, 25)
        kod+=alfabe[index]  
    print(kod)    

# 3-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
def kodalealeyatwa2():
    nkarackte=randint(2,61)
    kod=""
    for i in range(nkarackte):
        index=randint(0, 25)
        if alfabe[index] in kod:
            index=randint(0, 25)
        else:    
            kod+=alfabe[index]  
    print(kod)  

#4-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.     
def kodAlfanimerik():
    nkaracte=randint(2,61 )
    kod=""
    for i in range(nkaracte):
        if alfanimerik[nkaracte] in kod:
            nkaracte=randint(2, 61)
        else:
            kod+=alfanimerik[nkaracte]
    print(kod)  

# 5- Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
def fonctionSlug():
    chenn=input("antre fraz la :;\n")
    chenn=chenn.lower()
    lotchenn=""
    slug=""
    for i in chenn:
        if i==" ":
            lotchenn=chenn.replace(" ", "-")
    for i in lotchenn:
        slug+=i        
    print(slug)      
#6 separe chak let nan on mo ak yon vigil
def separeakvigil():
    mo=input(" mete mo anh ::")
    nouvomo=""
    for i in mo:
        nouvomo+=i+","
    print(nouvomo) 
#7 fonction ki bay endex chak karakte nan yon mo
def endekstire():
    mo=input("mete mo a::")
    endeks=[]
    for i in mo:
        endeks.append(str(string.ascii_lowercase.index(i)))
    print("-".join(endeks))   
# 8- yon fonction ki bay mo lew ekri endex yo
def ekriEndeks():
    chif=input("les index::")
    mot=[]
    for i in chif.split("-"):
        mot.append(alfabe[int(i)])
    print("".join(mot))   

# 9-permitation de vale ana yon tuple

def pemutation(val1, val2):
    t=()
    t=val1,val2
    print(t[::-1])

# 10-fonktion ki pran premye let nan yon non
def premyelet():
    chan=[]
    inisyal=""
    nom=input("nom:: ")
    for i in nom:
        nom=nom.replace(" ","-")
    for i in nom.split("-"):
        chan.append(i)
    for i in chan:
        inisyal+=i[0]
    print(inisyal)

#execution

start=input("peze nenpot bgy pouw k komanse::")
while start!="":
    print("peze nimero saw vle fe a\n",
    "1-enves yon mo \n2-jwenn yon kod aleyatwa ak repetisyon \n",
    "3-yon kod aleyatwa san repetisyon\n4-kod aleywtwa alfanimwrik san repesyon\n"
    "5-jenere yon slug a pati de yon chenn\n6-separe chak let nan yon mo ak yon vigil\n",
    "7-fonction ki bay endex chak karakte nan yon mo\n8- yon fonction ki bay mo lew ekri endex yo\n",
    "9-permitation de vale ana yon tuple\n10-fonktion ki pran premye let nan yon non")
    choice=int(input("::"))
    if choice==1:
        k=input("le mot::")
        invesmo(k)
    elif choice==2:
        kodalealeyatwa()
        
    elif choice==3:
        kodalealeyatwa2()
    elif choice==4:
        kodAlfanimerik()
         
    elif choice==5:
        fonctionSlug()
    elif choice==6:
        separeakvigil()
        
    elif choice==7:
        endekstire()


    elif choice==8:
        ekriEndeks()
    elif choice==9:
        n1=input("premier valeur::")
        n2=input("dexieme valeur::")
        pemutation(n1, n2)
    elif choice==10:
        premyelet()
    else:
        print("fe sa yo diw la")    

    
    start=input("peze enter siw pap rekomanse::")
   
print("bye bye")