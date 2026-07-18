class Usuario():
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def login(self, email_tentativa, senha_tentativa):
        if self.email == email_tentativa and self.__senha == senha_tentativa:
            print(f'Logado com sucesso!!')
        else: 
            print(f'Dados inválidos!!')