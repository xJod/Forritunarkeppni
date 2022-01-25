#	Jónas Orri Daníelsson | 2022 | Delta 2019 I

manudir = {				# Dictionary fyrir alla mánuði
	'1': 31,
	'2': 28,			# Gert er ráð fyrir að þetta dagatal er fyrir 2019 þannig að það er ekki hlaupár
	'3': 31,
	'4': 30,
	'5': 31,
	'6': 30,
	'7': 31,
	'8': 31,
	'9': 30,
	'10': 31,
	'11': 30,
	'12': 31
}

n = int(input())		# Mánuður í númeri d. 10

print(manudir[str(n)])	# Prenta fjölda daga út frá n