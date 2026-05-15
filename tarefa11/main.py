# Desenvolva um wrapper para o CRUD da API dos users com as funções list, create, read, update e delete.
# Desenvolva uma CLI (como no exercício anterior) que use a sua biblioteca.
# Exemplo de uso:
# import users_wrapper as users

# user = users.read(user_id)
# print(user["name"])

# # Listar usuários
# users_list = users.list()
# print(users_list)

# users.delete(user_id)

import users_wrapper as users

opcao = True
while opcao:
    opcao = input("1 - Listar usuários\n2 - Ler usuário\n3 - Criar usuário\n4 - Atualizar usuário\n5 - Excluir usuário\n6 - Sair\nDigite a opção desejada: ")
    if opcao == "1":
        print("Lista de usuários:")
        users_list = users.list()
        if users_list:
            for user in users_list:
                print(f"ID: {user['id']}, Nome: {user['name']}")
        else:
            print("Nenhum usuário encontrado.")

    if opcao == "2":
        user_id = input("Digite o ID do usuário: ")
        user = users.read(user_id)
        if user:
            print(f"ID: {user['id']}\nNome: {user['name']}")
        else:
            print("Usuário não encontrado.")