def clientsLists(iterableClient, list=):
    list.extend(iterableClient)
    return list

clients1 = clientsLists(['João', 'Maria', 'Eduardo'])
clients2 = clientsLists(['Marcos', 'Jonas', 'Zico'])

print(clients1)
print(clients2)