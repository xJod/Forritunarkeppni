#	Jónas Orri Daníelsson | 2022 | Delta 2019 F

k, q = map(int, input().split())			# Tek inn fjölda dæma og fjölda leystra dæma

dicta = {}									# Nýtt dictionary
for i in range(1, k + 1):					# Loopa k+1 oft
	dicta[i] = 0							# Set öll stökin á 0 í dict-inu

for i in range(q):							# Loopa q oft
	a, b = map(int, input().split())		# Tek inn liðsnúmer og fjöldi leystra dæma
	dicta[b] = dicta[b] + 1					# Hækka stakið um einn fyrir viðeigandi dæmi

print(min(dicta.values()))					# Prenta lægsta gildið