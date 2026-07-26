from services.user_service import get_user_by_id
from services.calculator import divide_numbers
from utils.logger import log

def main():
    log("Iniciando sistema...")

    user = get_user_by_id(1)
    log(f"Usuário encontrado: {user}")

    result = divide_numbers(10, 0)

    log(f"Resultado final: {result}")

if __name__ == "__main__":
    breakpoint()  
    main()