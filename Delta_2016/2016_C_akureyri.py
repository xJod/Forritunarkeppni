#	Jónas Orri Daníelsson | 2022 | Delta 2016 C

n = int(input())	                                    # tek in fjölda af fólki
sveitaf = []	                                        # nýr listi fyrir öll sveitafjélög sem verða skráð

for i in range(n):	                                    # loopa sem keyrir n mörgum sinnum
    nafn = input()	                                    # tek in nafn
    sveitaf.append(input())	                            # tek in sveitafélag og set í lista

stokSf = []	                                            # nýr listi fyrir sveitafélög þar sem er bara eitt pláss fyrir hvert og eitt
for i in range(len(sveitaf)):                           # loopa sem keyrir í gegnum lengdina á fyrri listanum
    if sveitaf[i] not in stokSf:	                    # checkar hvort að sveitafélagið sé nú þegar í nýja listanum
        stokSf.append(sveitaf[i])	                    # ef ekki þá er það sett í nýja listann

for i in range(len(stokSf)):	                        # loopar í gegnum seinni listann til þess að loks telja öll mismunandi sveitafélög
    print(f'{stokSf[i]} {sveitaf.count(stokSf[i])}')	# prenta svo út sveitafélag og fjölda