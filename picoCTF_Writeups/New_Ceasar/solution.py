
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]



def shiftBack(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]



def revert(crypt):
	i = 0
	reverse = ""
	while (i < len(crypt)):
		index1 = ALPHABET.index(crypt[i])
		index2 = ALPHABET.index(crypt[i + 1])
		index1 = index1 * 16
		add = index1 + index2
		binary1 = "{0:08b}".format(add)
		reverse += chr(add)
		i += 2
	print(reverse)



def main():
	keys = "abcdefghijklmnopqrstuvwxyz"
	for key2 in keys:
		print(key2)
		code = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"
		new = ""
		for i, c in enumerate(code):
			new += shiftBack(c, key2[i % len(key2)])
		revert(new)

main()

