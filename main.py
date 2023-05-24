import cryptocode

insertKey = input("Enter a key: ")
while len(insertKey) < 10:
    print('Insufficient key size... Key size must be greater than ten')
    insertKey = input("Enter a key: ")

insertMessage = input("Inser a message: ")
EncryptedMessage = cryptocode.encrypt(insertMessage, insertKey)

print("Messa crypted: " + EncryptedMessage)

insertKeyToDecryptedMessage = input("Insert one key to decrypted one message: ")
while insertKeyToDecryptedMessage != insertKey:
    print("Incorrect key")
    insertKeyToDecryptedMessage = input("Insert one key to decrypted one message: ")

DecryptedMessage = cryptocode.decrypt(EncryptedMessage, insertKey)
print(DecryptedMessage)