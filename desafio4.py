# Desafio Manipulação de Lista

frutas = ["Laranja", "Maça", "Banana"]

adicionar = input("Qual fruta deseja adicionar?")

frutas.append(adicionar)

print(frutas)

remover = input("Qual fruta remover da lista ?")

if remover in frutas:
    frutas.remove(remover)
    print("Item removida da lista. Lista atualizada:", frutas)
else:
    print("Fruta inexistente na lista")

