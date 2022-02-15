#	Jónas Orri Daníelsson | 2022 | Delta 2020 E

v, a, t = map(int, input().split())			# Upphafshraði, Hröðun, Tími

d = ((v*t) + (0.5*a*t**2))					# Uppgefin formúla úr dæminu

print(d)									# Prenta töluna