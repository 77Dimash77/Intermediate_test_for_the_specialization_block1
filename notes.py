import argparse
import json
from datetime import datetime

def read_notes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(file_path, notes):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)

def add_note(title, message, file_path):
    notes = read_notes(file_path)
    
    # Найти наибольший id среди существующих заметок
    max_id = max([note['id'] for note in notes], default=0)
    
    note_id = max_id + 1
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_note = {'id': note_id, 'title': title, 'message': message, 'created_at': created_at}
    notes.append(new_note)
    save_notes(file_path, notes)
    print("Заметка успешно сохранена.")


def list_notes(file_path, date=None, sort_by_date=False):
    notes = read_notes(file_path)
    if date:
        filtered_notes = [note for note in notes if note['created_at'].startswith(date)]
        notes = filtered_notes
    
    if sort_by_date:
        notes = sorted(notes, key=lambda x: x['created_at'])
    
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"{note['id']}. {note['title']} - {note['message']} (Дата: {note['created_at']})")

def edit_note(note_id, title, message, file_path):
    notes = read_notes(file_path)
    note = next((n for n in notes if n['id'] == note_id), None)
    if note:
        note['title'] = title
        note['message'] = message
        save_notes(file_path, notes)
        print("Заметка успешно отредактирована.")
    else:
        print(f"Заметка с id {note_id} не найдена.")

def delete_note(note_id, file_path):
    notes = read_notes(file_path)
    note = next((n for n in notes if n['id'] == note_id), None)
    if note:
        notes.remove(note)
        save_notes(file_path, notes)
        print("Заметка успешно удалена.")
    else:
        print(f"Заметка с id {note_id} не найдена.")

def show_note_by_id(note_id, file_path):
    notes = read_notes(file_path)
    note = next((n for n in notes if n['id'] == note_id), None)
    if note:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки:\n{note['message']}")
        print(f"Дата создания: {note['created_at']}")
    else:
        print(f"Заметка с ID {note_id} не найдена.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Консольное приложение заметки")
    parser.add_argument("command", choices=['add', 'list', 'edit', 'delete', 'show'], help="Команда (add, list, edit, delete, show)")
    parser.add_argument("--id", type=int, help="Идентификатор заметки (требуется для edit, delete и show)")
    parser.add_argument("--title", help="Заголовок заметки (требуется для add и edit)")
    parser.add_argument("--message", help="Тело заметки (требуется для add и edit)")
    parser.add_argument("--date", help="Дата для фильтрации списка заметок (требуется для list)")
    parser.add_argument("--sort", action='store_true', help="Сортировать заметки по дате (требуется для list)")

    args = parser.parse_args()

    file_path = "notes.json"

    if args.command == 'add':
        add_note(args.title, args.message, file_path)
    elif args.command == 'list':
        list_notes(file_path, args.date, args.sort)
    elif args.command == 'edit':
        if not args.id:
            print("Требуется указать идентификатор заметки (--id)")
        else:
            edit_note(args.id, args.title, args.message, file_path)
    elif args.command == 'delete':
        if not args.id:
            print("Требуется указать идентификатор заметки (--id)")
        else:
            delete_note(args.id, file_path)
    elif args.command == 'show':
        if not args.id:
            print("Требуется указать идентификатор заметки (--id)")
        else:
            show_note_by_id(args.id, file_path)
