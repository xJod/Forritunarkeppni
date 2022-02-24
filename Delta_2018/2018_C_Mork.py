#	Jónas Orri Daníelsson | 2022 | Delta 2018 C

n = int(input())	# Fjöldi marka
m = int(input())
# 0 ef hvorugt liðið skoraði, 1 ef bara annað liðið skoraði og 2 ef bæði liðin skoruðu

if n == 0 or (n == 2 and m == 2):	# Ef n er 0 eða n er 2 og m er 2
	print('Jebb')
else:								# Annars
	print('Neibb')