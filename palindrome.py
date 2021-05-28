from string import punctuation, whitespace

def isPalindrome(text: str):
	return True if text.lower() == text.lower()[::-1] else False

def cleanText(text: str):
	return text.translate(str.maketrans("", "", punctuation)).translate(str.maketrans("", "", whitespace))

def palindromeAsik(text: str) -> bool:
	return isPalindrome(cleanText(text))

print(palindromeAsik("k!@!a#s()u$$rr#%u^s&%a*k"))
print(palindromeAsik("#Al#p@!rO@*)A$sik*(k$is#A$O@r@$pl$!_A"))
print(palindromeAsik("%#@$a$l%p#@rO%@S$u#@s!#a^h"))
print(palindromeAsik("_*ma$!k@!an%#%n%$@a%k!@an"))