import users_wrapper as u

opcao = True

while opcao:
    opcao = input("1 - Listar usuários\n2 - Ler usuário\n3 - Editar usuário\n4 - Excluir usuário\n5 - Criar usuário\n6 - Sair\nDigite a opção desejada: ")
    if opcao == "1":
        print("Lista de usuários:")
        users = u.list()
        if users:
            for user in users:
                print(f"ID: {user['id']}, Nome: {user['name']}")
        else:
            print("Nenhum usuário encontrado.")

    if opcao == "2":
        user_id = input("Digite o ID do usuário: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
        else:
            print("Usuário não encontrado.")

    if opcao == "3":
        user_id = input("Digite o ID do usuário: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            user["name"] = input("Digite o novo nome do usuário: ")
            user["email"] = input("Digite o novo email do usuário: ")
            user["phone"] = input("Digite o novo telefone do usuário: ")
            novo_usuario = u.update(user_id, user)
            if novo_usuario:
                print(f"Usuário {novo_usuario['name']} atualizado com sucesso.")
            else:
                print("Erro ao atualizar usuário.")

    if opcao == "4":
        user_id = input("Digite o ID do usuário: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            confirmacao = input("Deseja excluir este usuário? (s/n): ")
            if confirmacao == "s":
                u.delete(user_id)
                print("Usuário excluído com sucesso.")
            else:
                print("Exclusão cancelada.")

    if opcao == "5":
        print("Digite os dados do novo usuário:")
        user = {}
        user["name"] = input("Nome: ")
        user["email"] = input("Email: ")
        user["phone"] = input("Telefone: ")
        confirmacao = input("Deseja criar este usuário? (s/n): ")
        if confirmacao == "s":
            novo_usuario = u.create(user)
            if novo_usuario:
                print(f"Usuário {novo_usuario['name']} criado com sucesso.")
            else:
                print("Erro ao criar usuário.")

    if opcao == "6":
        print("Saindo...")
        opcao = False