#	Jónas Orri Daníelsson | 2022 | Delta 2018 A

n = int(input())					# Fjöldi stafa
k = str(input()[:1])				# Stafur til þess að leita af
m = str(input()[:n])				# Orð

if k in m:							# Athuga hvort að stafurinn sé í orðinu
	print('Unnar fann hana!')		# Prenta
else:								# Annars
	print('Unnar fann hana ekki!')	# Prenta