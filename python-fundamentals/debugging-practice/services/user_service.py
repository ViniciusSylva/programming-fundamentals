from data.users import USERS

def get_user_by_id(user_id):
    for user in USERS:
        if user["id"] == user_id:
            return user

    print("Usuário não encontrado")
    return None