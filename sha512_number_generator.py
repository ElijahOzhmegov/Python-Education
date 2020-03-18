import hashlib


if __name__ == '__main__':

    with open('foo.txt', 'w') as file:
        # for i in range(1, 1e6):
        for i in range(1, 3):
            not_hashed = str(i).encode()
            line = str(i) + ' ' + hashlib.sha512(not_hashed).hexdigest() + '\n'
            file.write(line)
