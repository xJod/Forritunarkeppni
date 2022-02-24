#	Jónas Orri Daníelsson | 2022 | Delta 2018 L

n = int(input())													# Tek inn input
listi = []															# Tómur listi
tupla = ()															# Ný tupla
for x in range(n):													# Loopa n oft
	tupla = tuple(map(int, input().split(' ')))						# Tek hnit sem input og set í tuple
	listi.append(tupla)												# Set tupluna í lista
q = int(input())													# Tek inn q
teljari = 0															# Nýr teljari sem byrjar á 0
for x in range(q):													# Loopa q oft
	s = int(input())												# Tek inn s
	for i in range(len(listi)):										# Loopa lengdina á listanum
		if listi[i][0]*listi[i][0]+listi[i][1]*listi[i][1] < s*s:	# Ef staðsetningin er inní svæðinu
			teljari += 1											# Hækka teljarann um einn
	print(teljari)													# Prenta teljarann
	teljari = 0														# Núllstilli teljarann