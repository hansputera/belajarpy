#From:Augusta Clarissa Silvy Pascalin

def pasanganHuruf(text: str):
	if len(text) < 3:
		return 0
	elif text[0] == text[2]: # Jika huruf pertama dan ke tiga sama
		return 1 + pasanganHuruf(text[1:])
	else: # Jika tidak sama
		return pasanganHuruf(text[1:])

print(pasanganHuruf("ababa"))
print(pasanganHuruf("acay"))
print(pasanganHuruf("bxbxx"))
print(pasanganHuruf("kukuruyuk"))