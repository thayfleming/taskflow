import csv, os

CSV_FILE = "tasks.csv"
HEADERS = ["title", "description", "priority", "status"]

def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

def add_task():
    title = input("Título da tarefa: ").strip()
    description = input("Descrição: ").strip()
    priority = input("Prioridade (Alta/Média/Baixa): ").strip().capitalize()
    status = "Pendente"

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([title, description, priority, status])
    print("✅ Tarefa adicionada!")

def show_tasks():
    ensure_csv()
    print("\n--- Lista de Tarefas ---")
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)
        vazio = True
        for i, row in enumerate(reader, 1):
            vazio = False
            print(f"{i}. {row[0]} | {row[1]} | {row[2]} | {row[3]}")
        if vazio:
            print("Nenhuma tarefa cadastrada.")

def main():
    ensure_csv()
    while True:
        print("\nTaskFlow - Menu")
        print("1. Adicionar Tarefa")
        print("2. Mostrar Tarefas")
        print("3. Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("Até mais! 👋")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
