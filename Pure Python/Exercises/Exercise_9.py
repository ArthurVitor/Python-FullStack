def addChore(todo, chore):  # Receives chore's list and chore
    todo.append(chore)


def undo(todo, last):
    last.append(todo.pop())


def redo(todo, last):
    todo.append(last[-1])
    last.pop()


if __name__ == '__main__':
    todo = []
    last = []

    esl = str(input('Choose what to do: \n'
                    'Add chore: add \n'
                    'Show chores: show \n'
                    'Undo last chore: undo \n'
                    'Redo last chore: redo \n '
                    '\t'))

    if esl == 'add':
        chore = str(input('What you want to do? '))
        addChore(todo, chore)  # Sends chore's list and chore
    elif esl == 'show':
        print(todo)
