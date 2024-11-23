from app.models import User

users_db = {}

def create_user(user_id, username, password, name):
    if username in [user.username for user in users_db.values()]:
        raise ValueError("Username já existe.")
    user = User(user_id, username, password, name)
    users_db[user_id] = user
    return user

def get_user(user_id):
    return users_db.get(user_id)

def get_all_users():
    return list(users_db.values())

def update_user(user_id, username, password, name):
    if user_id not in users_db:
        raise ValueError("Usuário não encontrado.")
    user = users_db[user_id]
    user.username = username
    user.password = password
    user.name = name
    return user

def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
    else:
        raise ValueError("Usuário não encontrado.")
