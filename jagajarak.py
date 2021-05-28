def jagaJarak(pertama:int, tengah: list, hasil: int):
	if hasil == 0:
		return True
	elif pertama >= len(tengah):
		return False
	elif jagaJarak(pertama+2, tengah, hasil - tengah[awal]):
		return True
	else:
		return jagaJarak(pertama+1, tengah, hasil)

print(jagaJarak(0, [5, 7, 11, 4], 16))
print(jagaJarak(0, [5, 7, 11, 4], 15))
print(jagaJarak(0, [5, 7, 11, 4], 9))
print(jagaJarak(0, [5, 7, 11, 4], 18))