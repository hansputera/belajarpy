def getBiners(text:str):
	tempat = []
	for t in text:
		try:
			if t == "1" or t == "0":
				tempat.append(int(t))
		except:
			pass
	return tempat

def binToDec(text):
	biners = getBiners(text)
	pangkat = len(biners) - 1
	desimal = 0

	for i in range(len(biners)):
		biner = biners[i]
		desimal += biner * (2**pangkat)
		pangkat-=1
	return desimal
	
print(binToDec("!1@1#1$01$%^&")) 
print(binToDec("makan 1 bakso 10.000"))
print(binToDec("[1][0][1][0]"))