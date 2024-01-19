notes = []

def add_note():
    note_text = input("Enter your note: ")
    notes.append(note_text)
    print("Note added successfully!")

def display_notes(order='earliest'):
    if order == 'earliest':
        sorted_notes = sorted(notes, key=len)
    elif order == 'latest':
        sorted_notes = sorted(notes, key=len, reverse=True)
    elif order == 'longest':
        sorted_notes = sorted(notes, key=len, reverse=True)
    elif order == 'shortest':
        sorted_notes = sorted(notes, key=len)
    else:
        print("Unknown sorting order.")
        return

    for note in sorted_notes:
        print(note)


while True:
    command = input("> ").lower()

    if command == 'add':
        add_note()

    elif command == 'earliest':
        print("From earliest to latest:")
        display_notes('earliest')

    elif command == 'latest':
        print("From latest to earliest:")
        display_notes('latest')

    elif command == 'longest':
        print("From longest to shortest:")
        display_notes('longest')

    elif command == 'shortest':
        print("From shortest to longest:")
        display_notes('shortest')

    elif command == 'exit':
         break

    else:
        print("Unknown command. Please try again.")
