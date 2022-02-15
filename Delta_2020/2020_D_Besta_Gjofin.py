#	Jónas Orri Daníelsson | 2022 | Delta 2020 D

fjoldiGjafa = int(input())									# Tek inn fjölda gjafa

gjafaListi = {}												# Nýtt dictionary
for i in range(fjoldiGjafa):								# Keyrir eins oft og fjöldi gjafa er
	n, r = map(str, input().split())						# Tek in nafn og einkunn
	r = int(r)												# Breyti einkunn úr string í int

	gjafaListi[n] = r										# Bæti við nafni og einkunn í dictionary-ið

print(max(gjafaListi, key = lambda x : gjafaListi[x]))		# Prenta úr hver var með bestu einkuninna útfrá hæðstu einkununni