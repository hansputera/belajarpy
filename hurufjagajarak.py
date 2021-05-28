def hurufJagaJarak(input: str) -> str:
	temp = []
	[temp.append(k) for k in input if k not in temp]
	return "".join(temp)

print(hurufJagaJarak("ooookkkkkkeeeeee"))