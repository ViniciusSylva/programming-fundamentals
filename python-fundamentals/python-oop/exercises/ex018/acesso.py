import sqlite3

busca = input("Quem está buscando? ").strip()

try:
    with sqlite3.connect("banco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))
        # list = cur.fetchall()
        # print(list)

        total = 0
        for total, amigo in enumerate(cur, start=1):
            print(f"{amigo['nome']} nasceu em {amigo['nascimento']}")

        print(f"Ao todo encontrei {total} com a busca '{busca}'")
except sqlite3.Error as erro:
    print(f"Erro ao acessar o banco de dados: {erro}")
except Exception as erro:
    print(f"Erro inesperado: {erro}")