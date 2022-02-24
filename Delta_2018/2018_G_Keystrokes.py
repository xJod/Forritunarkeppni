#	Jónas Orri Daníelsson | 2022 | Delta 2018 G

from collections import deque		# Importa deque
listi = list(input())				# Tek inn streng og set í lista
index = 0							# Index er 0
arr = []							# Tómur listi
for i in listi:						# Loopa í gegnum string listann
	if i == 'L':					# Ef i er L
		index -= 1					# Lækka index um 1
	elif i == 'R':					# Ef i er R
		index += 1					# Hækka index um 1
	elif i == 'B':					# Ef i er B
		arr.pop(index-1)			# Tek út þann staf sem er index-1
		index -= 1					# Lækka index um 1
	else:							# Annars
		arr.insert(index, i)		# Set inn stakið á index, i
		index += 1					# Hækka index um 1

print(''.join(arr))					# Prenta listann saman sem streng