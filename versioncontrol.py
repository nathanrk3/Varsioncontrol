# Nathan King
# COP3502C
# Section 30145
# version control
def encode_password(user_input):
    empty_string = ''
    for x in user_input:
        # add 3, make case of > 7
        empty_string += str((int(x)+3) % 10)
    return empty_string



def main():

    # make while loop
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # make input
        user_choice = input("Please enter an option:")
        if user_choice == '1':
            non_coded = input("Please enter your password to encode:")

            #encode the password
            password = encode_password(non_coded)
            print("Your password has been encoded and stored!")

        elif user_choice == '3':
            break

if __name__ == "__main__":
    main()