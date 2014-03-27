string = input("\nDigite o texto para ser cifrado: ")
n = int(input("\nDigite a chave numerica: "))
output = ""
string = string.lower()
for c in string:
	if(c != " "):
		if(ord(c) + n > 122):
			c = chr(96+(ord(c)+n-122))
		else:
			c = chr(ord(c) + n)
	output += c
print (output)