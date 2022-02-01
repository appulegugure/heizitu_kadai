import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


def init_db(conn, cur):
    with open('sql_dir/schema.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)

    # 実行状態を保存
    conn.commit()
    
    return 0


def all_userinfo(conn, cur):
    with open('sql_dir/all_userinfo.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)

        fetch_user = cur.fetchall()
    # 実行状態を保存
    conn.commit()

    return print('\n'.join([f"Name: {i[0]} Age: {i[1]}" for i in fetch_user]) + '\n')


def add_user(name, age, conn, cur):
    with open('sql_dir/insert.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name, 'age': age})

    # 実行状態を保存
    conn.commit()

    return print(f"add new user {name} \n")


def users_find(name, conn, cur):
    with open('sql_dir/user_find.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name})

    # fetch
    fetch_user = cur.fetchall()
    # 実行状態を保存
    conn.commit()

    if len(fetch_user) == 0:
        return print(f"Sorry, {name} is not found")
    else:
        return print(['\n'.join([f"Name: {i[0]} Age: {i[1]}" for i in fetch_user])] + '\n')


def delete_user(name, conn, cur):
    with open('sql_dir/user_delete.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name})

    # 実行状態を保存
    conn.commit()

    return print(f"delete  user {name} \n")


def edit_user(name, edit_name, edit_age, conn, cur):
    with open('sql_dir/edit_user.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name, 'editname': edit_name, 'editage': edit_age})

    # 実行状態を保存
    conn.commit()

    return print(f"update user {edit_name} \n")


def main():
    # databaseのURLを取得
    dsn = os.environ.get('DATABASE_URL')

    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    # DB CREATE
    init_db(conn, cur)

    # introduction.txt OPEN
    with open('print_introduction.txt', encoding="utf-8") as introduction:

        print(introduction.read())

    # DB OPERATION START POINT
    while True:
        command = str(input('\nChoose a operation? > ')).upper()
        if command == 'A':

            print('=== Add new user ===')
            name = str(input("Please enter new user > "))
            if name == '!q': continue

            age = int(input("Please enter user age > "))
            if age == '!q': continue

            # cur = conn.cursor()
            try:
                add_user(name, age, conn, cur)
            except psycopg2.errors.UniqueViolation:
                print(f"Duplicated user name: {name}")
            else:
                print(f"Add new user: {name}")
            finally:
                continue

        elif command == 'S':

            print('=== Show all users inf ===')
            # cur = conn.cursor()

            all_userinfo(conn, cur)


        elif command == 'F':

            print('=== Find user information ===')
            name = str(input("Please enter find user > "))
            if name == '!q': continue

            # cur = conn.cursor()
            users_find(name, conn, cur)

        elif command == 'Q':
            print('Bye!')
            conn.close()
            break

        elif command == 'D':

            print('=== delete user in users table ===')
            name = str(input("Please enter delete user > "))
            if name == '!q': continue

            # cur = conn.cursor()
            delete_user(name, conn, cur)

        elif command == 'E':
            print("=== Edit user ===")
            name = str(input("Please enter edit user > "))
            if name == '!q': continue

            edit_name = str(input("name? > "))
            if edit_name == '!q': continue

            edit_age = input("age? > ")
            if edit_age == '!q': continue

            # cur = conn.cursor()
            edit_user(name, edit_name, edit_age, conn, cur)

        else:
            print(f"{command}: command not found")


if __name__ == '__main__':
    main()
