#	Jónas Orri Daníelsson | 2022 ||Delta 2018 D

a, b, c = map(int, input().split())		# Tek inn 3 hliðar

if a**2 + b**2 == c**2:					# Ef a^2 + b^2 = c^2
	print(int((a * b) // 2))			# Prenta flatamál
else:									# Annars
	print(-1)							# Prenta -1