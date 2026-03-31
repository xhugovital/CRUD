tasks = []
task_id = 1

menu_options = [
    "1. Adicionar tarefa",
    "2. Listar tarefas",
    "3. Atualizar tarefa",
    "4. Deletar tarefa",
    "5. Sair"
]

while True:
    print("\n--- GERENCIADOR DE TAREFAS ---")
    for option in menu_options:
        print(option)

    choice = input("Escolha uma opção: ")

    if choice == "1":
        desc = input("Digite a descrição da tarefa: ")
        tasks.append({"id": task_id, "desc": desc})
        task_id += 1
        print("✅ Tarefa adicionada!")

    elif choice == "2":
        if not tasks:
            print("⚠️ Nenhuma tarefa cadastrada.")
        else:
            print("\n📋 Suas tarefas:")
            for t in tasks:
                print(f"[{t['id']}] {t['desc']}")

    elif choice == "3":
        tid = input("ID da tarefa a atualizar: ")
        if tid.isdigit():
            tid = int(tid)
            for t in tasks:
                if t["id"] == tid:
                    t["desc"] = input("Digite a nova descrição: ")
                    print("✏️ Tarefa atualizada!")
                    break
            else:
                print("❌ ID não encontrado.")
        else:
            print("⚠️ Digite um número válido.")

    elif choice == "4":
        tid = input("ID da tarefa a deletar: ")
        if tid.isdigit():
            tid = int(tid)
            for t in tasks:
                if t["id"] == tid:
                    tasks.remove(t)
                    print("🗑️ Tarefa deletada!")
                    break
            else:
                print("❌ ID não encontrado.")
        else:
            print("⚠️ Digite um número válido.")

    elif choice == "5":  
        print("👋 Até logo!")
        break

    else:
        print("⚠️ Opção inválida, tente novamente.")
