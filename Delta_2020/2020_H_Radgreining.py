#	Jónas Orri Daníelsson | 2022 | Delta 2020 H

n, m = map(int, input().split())								# DNA Lengd, Fjöldi búta sem er búið að greina

dnalisti = []													# Nýr listi fyrir alla bitana

flag = True														# Flaggið er sett á True
for i in range(n):												# Loopa n oft
	dnalisti.append('?')										# Set ? í dnalista n oft

for i in range(m):												# Loopa m oft
	s, k = input().split()										# Tek inn s og k sem sæti og dna runu
	s = int(s)													# Breyti s í int

	for j in range(len(k)):										# Loopa lengdina á k oft
		if dnalisti[s-1] == '?' or dnalisti[s-1] == k[j]:		# Ef dnalisti sætið er ? eða dnalist sætið er stafur
			dnalisti[s-1] = k[j]								# Setja stakið á réttan stað
			s += 1												# Hækka s um einn
		else:													# Annars
			flag = False										# Set flag á False

if flag:														# Ef flag er True
	print(''.join(dnalisti))									# Prenta listann sem einn streng
else:															# Annars
	print('Villa')												# Prenta villu