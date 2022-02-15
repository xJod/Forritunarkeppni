#	Jónas Orri Daníelsson | 2022 | Delta 2020 Q

n = int(input())									# Fjöldi Tik Tok stjarna

stjornur = {}										# Nýtt dict fyrir allar stjörnurnar

for i in range(n):									# Loopa n sinnum
	s, a = input().split()							# Tek inn stjarna, Áhorf
	a = int(a)										# Breyti a í int

	if s not in stjornur:							# Ef stjarnan er ekki í stjörnu listanum
		stjornur[s] = 0								# Bæti honum við og set stig í núll
	stjornur[s] = stjornur[s] + a					# Bæti við stigum fyrir viðeigandi nafn

print(max(stjornur, key = lambda x: stjornur[x]))	# Prenta nafnið á þeim sem er með flest áhorf