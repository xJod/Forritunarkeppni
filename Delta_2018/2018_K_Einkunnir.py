#	Jónas Orri Daníelsson | 2022 | Delta 2018 K

s, n = map(int, input().split())							# Fjöldi spurininga, Fjöldi nemenda
svor = [str(i) for i in input().split()[:s]]				# Svar lykill (A, B, C, D)

allirNemendur = {}											# Nýtt dictionary
for i in range(n):											# Loopa n oft
	nafn = input()											# Tek inn nafn
	svarad = [str(i) for i in input().split()[:s]]			# Tek inn svör frá nemendum og set í lista
	allirNemendur[nafn] = svarad							# Bæti nafni og svarblaði í dictionary-ið

nemendurEinkunnir = {}										# Nýtt dictionary fyrir nafn og reyknaða einkunn
for i in allirNemendur:										# Loopa yfir alla nemendur
	rightAnswer = 0											# Rétt svör byrja sem 0
	for j in range(len(allirNemendur[i])):					# Loopa lengdina á svarblaði nemenda
		if allirNemendur[i][j] == svor[j]:					# Ef svarið hjá nemenda passar við svar lykilinn
			rightAnswer += 1								# Hækka rétt svör um einn

	finalGrade = round((rightAnswer / len(svor) * 10)*2)/2	# Breyti svo einkunni í rétt "format" 2.67 -> 3.0, 3.21 -> 3.5
	nemendurEinkunnir[i] = finalGrade						# Set svo einkunina með nemendanum

for i in nemendurEinkunnir:									# Loopa í gegnum alla nemendur
	print(f'{i}: {nemendurEinkunnir[i]}')					# Prenta nafn og einkunn