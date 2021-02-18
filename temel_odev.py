from math import * 


def donusturme(aci,aci_birimi = ("d","g","r"),donusecek_birim = ("d","g","r")):    
    
    if (aci_birimi == "d"):

        if (donusecek_birim == "r"):
            return radians(aci)

        elif (donusecek_birim == "g"):
            return aci * (400/360)
        
        else:
            return "Lütfen geçerli bir birim giriniz..."

    elif (aci_birimi == "g"):

        if (donusecek_birim == "d"):
            return aci * (360/400)
        
        elif (donusecek_birim == "r"):
            return aci * (pi / 200)
        
        else:
            return "Lütfen geçerli bir birim giriniz..."

    elif (aci_birimi == "r"):

        if (donusecek_birim == "d"):
            return degrees(aci)
        
        elif (donusecek_birim == "g"):
            return aci * (200/pi)

        else:
            print("Lütfen geçerli bir birim giriniz...")

def temel_odev1(Ya,Xa,semtAB,uzAB,aci_birim = ("d","g","r")):
    
    if (aci_birim == "d"):
        aci = donusturme(semtAB,"d","r")
        Yb = Ya + (uzAB * sin(aci))
        Xb = Xa + (uzAB * cos(aci))
        return "Yb = {} \nXb = {} ".format(Yb,Xb)
    elif (aci_birim == "g"):
        aci = donusturme(semtAB,"g","r")
        Yb = Ya + (uzAB * sin(aci))
        Xb = Xa + (uzAB * cos(aci))
        return "Yb = {} \nXb = {} ".format(Yb,Xb)
    elif (aci_birim == "r"):
        aci = semtAB
        Yb = Ya + (uzAB * sin(aci))
        Xb = Xa + (uzAB * cos(aci))
        return "Yb = {} \nXb = {} ".format(Yb,Xb)
    else:
        print("Lütfen parametreleri doğru giriniz...")
        

def temel_odev2(Ya,Xa,Yb,Xb,aci_birim = ("d","g")):
    
    DY = Yb - Ya
    DX = Xb - Xa
    semtAB = atan(DY / DX)
    uzAB = sqrt(DY**2 + DX**2)

    semtAB = donusturme(semtAB,"r","g")

    if (DY > 0 and DX > 0 ):
        semtAB = semtAB
    elif (DY > 0 and DX < 0):
        semtAB += 200
    elif (DY < 0 and DX < 0):
        semtAB += 200
    elif (DY < 0 and DX > 0):
        semtAB += 400

    if (aci_birim == "g"):
        return semtAB,uzAB
    elif (aci_birim == "d"):
        semtAB = donusturme(semtAB,"g","d")
        return semtAB,uzAB
    else:
        return "Lütfen geçerli bir parametre giriniz..."


def temel_odev3(semtAB,Beta,aci_birim = ("d","g")):
    semtBC = semtAB + Beta

    if (0 < semtBC <= 200):
        semtBC += 200
    elif (200 < semtBC <= 400):
        semtBC -= 200
    elif (400 < semtBC <= 600):
        semtBC -= 200
    elif (600 < semtBC <= 800):
        semtBC -= 600

    if (aci_birim == "g"): 
        return "BC Semt Açısı = {} grad".format(semtBC)
    elif (aci_birim == "d"):
        semtBC = donusturme(semtBC,"g","d")
        return "BC Semt Açısı = {} derece".format(semtBC)

def temel_odev4(Ya,Xa,Yb,Xb,Yc,Xc,aci_birim = ("d","g")):
    semtAB = temel_odev2(Ya,Xa,Yb,Xb,"g")[0]
    semtAC = temel_odev2(Ya,Xa,Yc,Xc,"g")[0]
    semtBC = temel_odev2(Yb,Xb,Yc,Xc,"g")[0]
    semtBA = temel_odev2(Yb,Xb,Ya,Xa,"g")[0]
    semtCA = temel_odev2(Yc,Xc,Ya,Xa,"g")[0]
    semtCB = temel_odev2(Yc,Xc,Yb,Xb,"g")[0]

    alfa = semtAC - semtAB #AB ve AC doğruları arasında ki açı
    beta = semtBA - semtBC #BA ve BC doğruları arasında ki açı
    teta = semtCB - semtCA #CB ve CA doğruları arasında ki açı
        
    if aci_birim == "g":
        return "Alfa açısı : {} Grad\nBeta açısı : {} Grad\nTeta açısı : {} Grad".format(alfa,beta,teta)
    elif aci_birim == "d":
        sonuc_list = []
        for i in (alfa,beta,teta):
            sonuc_list.append(donusturme(i,"g","d"))
        return "Alfa açısı : {} Derece\nBeta açısı : {} Derece\nTeta açısı : {} Derece".format(sonuc_list[0],sonuc_list[1],sonuc_list[2])


