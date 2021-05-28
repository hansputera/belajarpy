def cekPrima(input: int):
	if input <= 1:
		return False
	elif input == 2:
		return True
	else:
		for i in range(2, input):
			if input % i == 0:
				return False
		return True

def totalprima(input: int, debug = False):
	i=0
	temp=[]
	if debug: print("# CHECK PRIME TEST CASE")
	while(len(temp) < input):
		if debug: print('-',i,cekPrima(i))
		temp.append(i) if cekPrima(i) == True else None
		i+=1
	if debug:
	    print("# --------------------")
	    print(f"# Result: {temp}")
	total=0
	for x in temp:
		total+=x
	if debug: print(f"# Hasil Total: {total}")
	return total

print(totalprima(2))
print(totalprima(5))
print(totalprima(10))