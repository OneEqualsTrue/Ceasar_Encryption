print('Message:', end=' ')
message = input()

print('Key:', end=' ')
key = int(input())

def Ceasar(message):
	message = list(message.lower())
	
	for c in range(len(message)):
		if message[c].isalpha():
			secret = ord(message[c])

			if secret > ord('z') - key: secret = (secret + 100) % 126
			message[c] = chr(secret + key)

	return "".join(message)

print("\n", Ceasar(message))