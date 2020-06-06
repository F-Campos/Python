#!/usr/bin/env python
# coding: utf-8

# # Operadores lógicos

# In[ ]:


idade = 18
nome = "Bob"
if idade > 17:
   print("Você pode dirigir!")


# In[ ]:


idade = 18
if idade > 17 and nome == "Bob":
   print("Autorizado!")


# In[ ]:


# Usando mais de uma condição na cláusula if 

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')

if disciplina == 'Geografia' and nota_final >= '70':
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')


# In[ ]:


# Usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')


# In[ ]:





# In[ ]:




