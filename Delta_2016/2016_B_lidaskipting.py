#	Jónas Orri Daníelsson | 2022 | Delta 2016 B

n = (int(input()))	    # tek inn fjölda af keppendum sem heiltölu

if n % 3 == 0:	        # ef það er hægt að heiltöludeila fjöldanum með 3 þá er enginn sem er ekki í liði eða ekkert lið með of fáa leikmenn
    print('Jebb')       # prenta jebb
elif n % 3 != 0:        # ef það er ekki hægt að heiltöludeila þá passr fjöldinn ekki þæginlega í þryggja manna lið
    print('Neibb')      # prenta neibb