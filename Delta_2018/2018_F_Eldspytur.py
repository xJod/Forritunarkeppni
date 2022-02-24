#	Jónas Orri Daníelsson | 2022 | Delta 2018 F

n, k = map(int, input().split())	# Fjöldi eldspýtna, mest sem má fjarlægja í einu

if n % (k + 1) != 0:				# Ef n modulus deilt með k+1 er 0
	print('Jebb')					# Prenta 'Jebb'
else:								# Annars
	print('Neibb')					# Prenta 'Neibb'