nome = input("Qual seu nome? ")
cores = {"limpa":"\033[m", 
         "roxo":"\033[4;37;44m", 
         "vermelho":"\033[1;30;41m"}
print("É um prazer te conhecer, {}{}{}!".format(cores["vermelho"], nome, cores["limpa"]))