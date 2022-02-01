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
    
    return print("CREATE TABLE")


def all_userinfo(conn, cur):
    with open('sql_dir/all_userinfo.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)

        fetch_user = cur.fetchall()
    # 実行状態を保存
    conn.commit()

    return print('\n'.join([f"Name: {i[0]} Age: {i[1]}" for i in fetch_user]))


def add_user(name, age, conn, cur):
    with open('sql_dir/insert.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name, 'age': age})

    # 実行状態を保存
    conn.commit()

    return print(f"add new user {name}")


def users_find(name, conn, cur):
    with open('sql_dir/user_find.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name})

    # fetch
    fetch_user = cur.fetchall()
    # 実行状態を保存
    conn.commit()

    return print('\n'.join([f"Name: {i[0]} Age: {i[1]}" for i in fetch_user]))


def delete_user(name, conn, cur):
    with open('sql_dir/user_delete.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name})

    # 実行状態を保存
    conn.commit()

    return print(f"delete  user {name}")


def edit_user(name, age, conn, cur):
    with open('sql_dir/edit_user.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name, 'age': age})

    # 実行状態を保存
    conn.commit()

    return print(f"edit user finish")


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
        command = str(input('どんな操作')).upper()
        if command == 'A':

            print('A')
            Name = str(input("名前を入力してください。> "))
            Age = int(input("年齢を入力して下さい > "))
            # cur = conn.cursor()
            add_user(Name, Age, conn, cur)

        elif command == 'S':

            print('S')
            # cur = conn.cursor()
            all_userinfo(conn, cur)

        elif command == 'F':

            Name = str(input("検索する名前を入力してください。> "))
            print('F')
            # cur = conn.cursor()
            users_find(Name, conn, cur)

        elif command == 'Q':
            print('Bye!')
            conn.close()
            break

        elif command == 'D':
            Name = str(input("削除する名前を入力してください。> "))
            print('D')
            # cur = conn.cursor()
            delete_user(Name, conn, cur)

        elif command == 'E':
            Name = str(input("編集する人を入力してください。 > "))
            Age = input("age? > ")
            # cur = conn.cursor()
            edit_user(Name, Age, conn, cur)

        else:
            print(f"{command}: command not found")


if __name__ == '__main__':
    main()
