from usuario import *

def main():
    u1 = Usuario('teste@gmail.com', 'vini2005')
    print(u1.email)
    u1.login('teste@gmail.com', 'vini')

if __name__ == "__main__": 
    main()