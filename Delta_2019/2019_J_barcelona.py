#	Jónas Orri Daníelsson | 2022 | Delta 2019 J

n = [int(i) for i in input().split()[:2]]				# [ Fjöldi taska, Taskan sem við leitum af ]

allarToskur = [int(i) for i in input().split()[:n[0]]]	# Tek inn tösku röð með hámarki n töskum og set í lista

for i in range(len(allarToskur)):						# Loopa í gegnum listann
	if i == 0:											# Ef i er fyrsta umferð í loopunni
		if n[1] == allarToskur[i]:						# Ath. hvort að taskan sem við erum að leita af er númer 1 í röðinni
			print('fyrst')								# Prenta 'fyrst'
	elif i == 1:										# Ef i er seinni umferð í loopunni
		if n[1] == allarToskur[i]:						# Ath. hvort að taskan sem við erum að leita af er númer 2 í röðinni
			print('naestfyrst')							# Prenta 'naestfyrst'
	else:												# Annars
		if n[1] == allarToskur[i]:						# Ath. hvort að taskan sem við erum að leita af er númer 'i' í röðinni
			print(f'{i+1} fyrst')						# Prenta sæti + 'fyrst'