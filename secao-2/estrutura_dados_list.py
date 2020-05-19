'''
append
insert(0, x)
pop(1)
remove('x')
len()
sort()
reverse

max()
min()
sum()
'''
# os dois códigos são o mesmo
# x = []
# x = list()

#situação 1
# idade = []

# idade.append(18)
# print(idade)

# idade = [1, 2, 3, 4, 5]
# print(idade)
# idade.append(18) #inclui o 18 no final da lista acima

# idade.insert(3, 4)
# idade.insert(3, 'Marcio')

# idade.pop() #remove o último do índice
# idade.pop(2) #remove o 3º item da lista 

# idade.remove(3)

# print(idade)

# print(len(idade))

# método sort

# idade = [2, 5, 7, 3, 0, 9, 4, 1, 6]
# idade = ['caio', 'jorge'] #ordem alfabética
# print(idade)

# #ordena os números de uma lista CRESCENTE
# idade.sort()
# print(idade)

# #ordena os números de uma lista DESCRESCENTE
# idade.sort() 
# idade.sort(reverse = True)

# print(idade)

# método reverse

# idade = [1, 2, 3, 4, 5]
# idade = ['caio', 'jorge', 'danilo', 'bernardo', 'aline'] #ordem alfabética reversa
# idade = [2, 4,6,7,8,3,5,7]

# idade.sort()
# idade.reverse()
# # OU
# idade.sort(reverse=True)

# print(idade)

# outras funções MAX, MIN, SUM.
idade = [1, 2, 3, 4, 5]

print(max(idade)) # o maior númeror dentro da lista
print(min(idade)) # o menor númeror dentro da lista
print(sum(idade)) # a soma de todos os números da lista


