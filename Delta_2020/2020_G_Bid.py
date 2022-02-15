#	Jónas Orri Daníelsson | 2022 | Delta 2020 G

import datetime										# Importa datetime module
hh1, mm1 = map(int, input().split(':'))				# Tek inn fyrri tímann og splitta honum með ":"
hh2, mm2 = map(int, input().split(':'))				# Tek inn seinni tímann og splitta honum með ":"

t1 = datetime.timedelta(0,0,0,0,mm1,hh1,0)			# Bý til nýja breytu sem geymir tímana á betra formi
t2 = datetime.timedelta(0,0,0,0,mm2,hh2,0)			# Bý til nýja breytu sem geymir tímana á betra formi

x = t2-t1											# Fæ mysmuninn á tímunum

print((x.seconds)//60)								# Breyti mismuninum í mínútur