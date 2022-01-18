#	Jónas Orri Daníelsson | 2022 | Delta 2016 A

t = 0           # Skilgreini t
n = 1           # Skilgreini n
flag = True     # Set flag sem True

while t < 100: # Á meðan t er minna en 100 (fjöldi frumtalna er ekki orðinn 101)
    flag = True	# kveikja á flagginu
    n += 1 # hækka n um 1 og fæ 2 til þess að byrja
    for i in range (2, n):	# loopa sem fer i gegnum allar tolur upp að 100
        if n % i == 0: # ef n er heiltöludeilanleg með loopu tölunni þá er það ekki frumtala
            flag = False # slekk á flagginu
    if flag:
        print(n) # prenta "current" frumtölu
        t += 1 # hækka t um einn og fer þá næstu umferð