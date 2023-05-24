keyTest = "testingFunctionThatVerifyKey"

def verify_key(key):
    input('Insert one key to decrypted one message: ')
    while key != keyTest:
        key = input("Incorrect key \n Insert one key to decrypted one message: ")
    
    return key