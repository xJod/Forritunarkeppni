#	Jónas Orri Daníelsson | 2022 | Delta 2020 N

s = str(input())															# Tek inn streng

serhlodar = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']	# Listi af öllum sérhljóðum

finalS = []																	# Tómur listi
for i in range(len(s)):														# Loopa lengdina af s
	if s[i] in serhlodar:													# Ef stafurinn er í sérhljóða listanum
		finalS.append(s[i])													# Set hann í nýja listann

print(''.join(finalS))														# Prenta loka listann sem streng