#	Jónas Orri Daníelsson | 2022 | Delta 2016 H

n = int(input())					# Stofur
m = int(input())					# Keppendur

fjoldi = m // n						# Heiltöli deili keppendum með stofum
eftir = m % n						# Fæ afgang ur deilingunni

for i in range(n):					# Keyri eins oft og það eru keppendur
	if n > m:						# Ef stofurnar eru færri en nemendur eru allir settir í eina stofu
		for j in range(m):			# Loopa í gegnum allar stofurnar
			print('*', end='')		# Prenta fjölda í stofunni
		break						# Hætti í loopunni
	elif eftir > 0:					# Ef það eru auka keppendur
		for j in range(fjoldi+1):	# Loopa í gegnum heildina og bæti við einum keppenda við í stofuna
			print('*', end='')		# Prenta fjölda í stofunni
		eftir -= 1					# Tek einn keppenda frá þeim sem eru eftir
	else:							# Ef það er enginn auka
		for j in range(fjoldi):		# Loopa í gegnum heildið
			print('*', end='')		# Prenta fjölda í stofunni

	print()							# Prenta nýja línu