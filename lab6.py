
def encode(data):
    pw_list = [int(digit) for digit in data]
    encoded_list = [(digit + 3) % 10 for digit in pw_list]
    encoded_pw = ''.join(map(str, encoded_list))
    return encoded_pw


def decode(data):
    encoded_list = [int(digit) for digit in data]
    decoded_list = [(digit + 7) % 10 for digit in encoded_list]
    decoded_pw = ''.join(map(str, decoded_list))
    return decoded_pw


def main():

    menu = ['Encode',
            'Decode',
            'Quit']

    contn = True

    while contn:
        print('Menu')
        print('-------------')

        for i in range(len(menu)):
            print(f'{i + 1}.', menu[i])
        print()
        opt = int(input('Please enter an option: '))

        if opt == 1:
            pw = input('Please enter your password to encode: ')
            encode(pw)
            print('Your password has been encoded and stored!')
            print()

        elif opt == 2:
            print(f'The encoded password is {encode(pw)}, and the original password is {decode(pw)}.')
            print()

        elif opt == 3:
            contn = False


if __name__ == '__main__':
    main()

