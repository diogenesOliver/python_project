def create_key(key):
    while len(key) < 10:
        print('Insufficient key size... Key size must be greater than ten')
        key = input('Enter a key: ')

    return key