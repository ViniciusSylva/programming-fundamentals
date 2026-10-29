import sqlite3
from datetime import date

busca = input("Quem está buscando? ").strip()
hoje = date.today()

try:
    with sqlite3.connect("banco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))
        # list = cur.fetchall()
        # print(list)

        total = 0
        for total, amigo in enumerate(cur, start=1):
            txtnasc = amigo['nascimento']

            info_nasc = ""
            if not txtnasc:
                info_nasc = "Data de nascimento não informada"
            else:
                try:
                    data = date.fromisoformat(str(txtnasc))
                    japassou = (hoje.month, hoje.day) > (data.month, data.day)
                    idade = hoje.year - data.year - (0 if japassou else 1)

                    info_nasc = f"nasceu em {data:%d/%m/%Y} e tem {idade} anos"
                except ValueError:
                    info_nasc = "Data de nascimento inválida"

            print(f"{amigo['nome']} {info_nasc}")

        print("-" * 30)
        if total == 0:
            print(f"Nenhum amigo encontrado com a busca '{busca}'")
        elif total == 1:
            print(f"Encontrei 1 amigo com a busca '{busca}'")
        else:
            print(f"Encontrei {total} amigos com a busca '{busca}'")

except sqlite3.Error as erro:
    print(f"Erro ao acessar o banco de dados: {erro}")
except Exception as erro:
    print(f"Erro inesperado: {erro}")