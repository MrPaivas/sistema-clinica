import bcrypt
from mongo.mongo import domains

def create_domain(name, cnpj):
    domain = {
        "name": name,
        "cnpj": cnpj,
        "users": []
    }
    domains.insert_one(domain)

def read_domain(cnpj):
    domain = domains.find_one({"cnpj": cnpj})
    return domain
# Função para criar um novo usuário
# Função para criar um novo usuário com senha criptografada
def create_user(domain_cnpj, username, password, role):
    # Hash da senha usando bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = {
        "username": username,
        "password": hashed_password,
        "role": role
    }
    update_query = {"$push": {'users': {'$each': user}}}
    domains.update_one({"cnpj": domain_cnpj}, update_query)

# Função para verificar a senha de um usuário
def check_password(username, password):
    user = domains.find_one({"username": username})
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