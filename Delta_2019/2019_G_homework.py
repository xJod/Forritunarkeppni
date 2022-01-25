#	Jónas Orri Daníelsson | 2022 | Delta 2019 G

n = input()																# Inntak. dæmi: 1-3;5;7;10-13

firstSplit = n.split(';')												# tek listann í sundur þar sem ; er

allSeperated = []														# Nýr listi fyrir allar tölurnar
for i in range(len(firstSplit)):										# Loopa í gegnum fyrri listann
	if '-' in firstSplit[i]:											# Ath. hvort að hvert stak hefur '-' í því
		secondSplit = firstSplit[i].split('-')							# Nýr listi splittaður með '-'
		for ii in range(int(secondSplit[0]), int(secondSplit[1]) + 1):	# Loopa frá fyrri tölunni í seinni töluna(+1) til þess að fá allar á milli
			allSeperated.append(ii)										# Set allar tölurnar í nýrri listann
	else:																# Ef það er ekki '-' í stakinu
		allSeperated.append(int(firstSplit[i]))							# Set töluna í nýrri listann

print(len(allSeperated))												# Prenta svo fjölda dæma