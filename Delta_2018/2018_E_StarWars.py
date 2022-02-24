#	Jónas Orri Daníelsson | 2022 | Delta 2018 E

n = int(input())								# Fjöldi tala
listi = [int(i) for i in input().split()[:n]]	# Tölur
listi.sort()									# Sortera listann

fjoldi = n // 3									# Næ í fjölda staka (n / 3)

hluti1 = listi[0:fjoldi]						# Stak 1 eru fyrstu tölurnar útfrá fjölda
hluti2 = listi[fjoldi:fjoldi*2]					# Stak 2 eru miðju tölurnar
hluti3 = listi[fjoldi*2:]						# Stak 3 eru síðustu tölurnar

temp = hluti2 + hluti1 + hluti3					# Set öll stökin í einn lista
print(*temp, sep=' ')							# Prenta allt saman með bili