#	Jónas Orri Daníelsson | 2022 | Delta 2019 L

n, m, k = map(int, input().split())		# [ Raðir, Dálkar, Fjöldi sprengja ]

bord = []								# Nýr listi fyrir leikborðið
temp = []								# Temp listi
for i in range(n):						# Loop-a <n> sinnum
	for j in range(m):					# Loop-a <m> sinnum
		temp.append('.')				# Set punkt á viðeigandi stað
	bord.append(temp)					# Set temp listann í bord listann
	temp = []							# Hreinsa temp listann

for i in range(k):						# Loop-a k sinnum
	x, y = map(int, input().split())	# x, y hnit
	bord[x-1][y-1] = '*'				# Set sprengju á hnit

for i in bord:							# Loopa í gegnum bord listann
	print(''.join(i))					# Prenta út hverja röð "fallega"