import bcrypt
from mongo.mongo import domains, users

def create_domain(name, cnpj):
    domain = {
        "name": name,
        "cnpj": cnpj
    }
    domains.insert_one(domain)
    return domain

def read_domain(name):
    domain = domains.find_one({"name": name})
    return domain


# Função para criar um novo usuário com senha criptografada
def create_user(domain, username, password, role):
    # Hash da senha usando bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = {
        "domain": domain,
        "username": username,
        "password": hashed_password,
        "role": role
    }
    users.insert_one(user)

# Função para verificar a senha de um usuário
def check_password(username, password):
    user = users.find_one({"username": username})
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    if user and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False


# Função para ler informações de um usuário
def read_user(username):
    user = domains.find_one({"username": username})
    return user

# Função para atualizar a senha de um usuário
def update_password(username, new_password):
    domains.update_one({"username": username}, {"$set": {"password": new_password}})

# Função para excluir um usuário
def delete_user(username):
    domains.delete_one({"username": username})

# Exemplo de uso das funções:
create_domain("faculdade paiva", "9999999999")
#create_user("user1", "password123")
#create_user("user2", "securepass")

# Verificando a senha de um usuário
#if check_password("user1", "password123"):
    #print("Senha correta para user1")
#else:
    #print("Senha incorreta para user1")

# Atualizando a senha de um usuário
#update_password("user1", "newpassword456")

# Deletando um usuário
#delete_user("user2")