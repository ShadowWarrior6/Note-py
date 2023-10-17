import json
import datetime

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": timestamp,
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            break
    else:
        print("Заметка с указанным ID не найдена.")

def list_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['message']}")
        print(f"Дата/Время: {note['timestamp']}\n")

def edit_notes():
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Новый заголовок: ")
            new_message = input("Новое тело: ")
            note["title"] = new_title
            note["message"] = new_message
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            break
    else:
        print("Заметка с указанным ID не найдена.")

if __name__ == "__main__":
    notes = load_notes()
    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            edit_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
