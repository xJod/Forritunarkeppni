#	Jónas Orri Daníelsson | 2022 | Delta 2020 F

n = int(input())			# Fjöldi miða

l = []						# Nýr listi
for i in range(n):			# Keyrir n oft
	s = str(input())		# Tek inn streng af stöfum
	l.append(s[::-1])		# sný orðinu við

print(''.join(l[::-1]))		# Prenta listann samsettan og snúinn við