import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


def init_db():
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    print(dsn)
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('sql_dir/schema.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる。
    conn.close()


def all_userinfo():
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('sql_dir/all_userinfo.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql)

        fetch_you = cur.fetchall()
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる。
    conn.close()
    print('\n'.join([f"Name: {i[0]} Age: {i[1]}" for i in fetch_you]))


def add_user(name, age):
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('sql_dir/insert.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name, 'age': age})
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる。
    conn.close()

    print(f"add new user {name}")


def users_find(name):
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意

    with open('sql_dir/user_find.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name})
    """     
        #test1,
        cur.execute(f"SELECT * FROM users WHERE username = 'ER';")
        
        #test2,
        cur.execute(f"SELECT * FROM users WHERE username = '{name}';")
    """

    fetch_you = cur.fetchall()
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる。
    conn.close()
    print('\n'.join([f"Name: {i[0]} Age: {i[1]}" for i in fetch_you]))


def delete_user(name):
    # DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('sql_dir/user_delete.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name})
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる。
    conn.close()

    print(f"delete  user {name}")


def edit_user(name, age):
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('sql_dir/edit_user.sql', encoding="utf-8") as f:
        sql = f.read()
        # SQLを実行
        cur.execute(sql, {'name': name, 'age': age})
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる。
    conn.close()

    print(f"edit user finish")


def main():
    init_db()

    with open('print_introduction.txt', encoding="utf-8") as introduction:

        print(introduction.read())

    while True:
        command = str(input('どんな操作')).upper()
        if command == 'A':
            print('A')
            Name = str(input("名前を入力してください。> "))
            Age = int(input("年齢を入力して下さい > "))
            add_user(Name, Age)

        elif command == 'S':
            print('S')
            all_userinfo()

        elif command == 'F':
            Name = str(input("検索する名前を入力してください。> "))
            print('F')
            users_find(Name)

        elif command == 'Q':
            print('Bye!')
            break

        elif command == 'D':
            Name = str(input("削除する名前を入力してください。> "))
            print('D')
            delete_user(Name)

        elif command == 'E':
            Name = str(input("編集する人を入力してください。 > "))
            Age = input("age? > ")
            edit_user(Name, Age)

        else:
            print(f"{command}: command not found")


if __name__ == '__main__':
    main()
