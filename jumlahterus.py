def jumlahTerus(input: int):
	s = str(input)
	total = 0
	for i in s:
		total += int(i)
		while(len(str(total)) > 1):
			total = jumlahTerus(total)
	return total

print(jumlahTerus(12345))