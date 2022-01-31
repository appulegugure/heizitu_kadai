def all_userinfo():
    pass


def add_user():
    pass


def main():
    while True:
        command = str(input('どんな操作'))
        if command == 'A':
            print('A')
            add_user()
        elif command == 'S':
            print('S')
            all_userinfo()
        elif command == 'Q':
            print('ループを抜けます')
            break
        else:
            print(f"{command}: command not found")


if __name__ == '__main__':
    main()

print(
    """
    ===== Welcome to CRM Application =====
    [S]how: Show all users inf
    [A]dd: Add new use
    [Q]uit: Quit The Applicatio
    =====================================
    """
)
