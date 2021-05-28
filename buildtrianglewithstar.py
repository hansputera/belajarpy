def jumlahBintangSegitiga(baris: int):
	total = 0
	for i in range(baris):
		for s in range(-6, -i):
			print(" ", end="")
		for j in range(i+1):
			total += 1
			print("* ", end="")
		print()
	return total

print(jumlahBintangSegitiga(2))