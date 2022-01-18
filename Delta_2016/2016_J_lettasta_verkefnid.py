#	Jónas Orri Daníelsson | 2022 | Delta 2016 J

n = int(input())											# Fjöldi dæma
m = int(input())											# Fjöldi liða

daemi = input().split()										# Fæ lista af öllum verkefnum 

stig = []													# Tómur listi fyrir öll stig (nested listi)
for i in range(m):											# Loopa m oft til þess að taka in öll stig frá öllum liðunum
	stig.append(list(map(int,input().split())))				# Fæ inntak með öllum stigunum og set í stig listann										

ollReiknudStig = []											# Tómur listi fyrir öll reiknuð stig fyrir hvert dæmi
for i in range(len(daemi)):									# Loopa í gegnum listan eins oft eins og fjöldi dæma
	sum = 0													# Summu breyta til þess að reykna fyrir hvert og eitt dæmi
	for j in range(len(stig)):								# Loopa í gegnum fjölda af listum í stig listanum
		sum += stig[j][i]									# Bæti "current" stigafjölda í sum breytuna
	ollReiknudStig.append(sum)								# Set sum breytuna í listann ollReiknudStig

print(daemi[ollReiknudStig.index(max(ollReiknudStig))])		# Prenta svo hvaða dæmi er auðveldast með því að finna hæðsta stigafjöldann