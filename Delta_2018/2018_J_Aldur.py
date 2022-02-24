#	Jónas Orri Daníelsson | 2022 | Delta 2018 J

n = int(input())		# Fjöldi vina

ageList = []			# Listi fyrir alla aldur
for i in range(n):		# Loopa n oft
	a = int(input())	# Aldur vin nr i
	ageList.append(a)	# Set aldurinn í listann

print(min(ageList))		# Prenta minnsta stakið í listanum