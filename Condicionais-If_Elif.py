#!/usr/bin/env python
# coding: utf-8

# Condicionais:
# 
# # If

# In[1]:


if 5 > 2:
    print("Python é top")


# In[3]:


if 5 < 2:
   print("Python funciona!")
else:
   print("Algo está errado!")


# In[5]:


if 5 == 5:
    print("Testando Python!")
if True:
    print('Parece que Python funciona!')


# #Cndicionais aninhados

# In[11]:


idade = 18  #variavel
if idade > 17:
   print("Você pode dirigir!")


# In[15]:


Nome = "Bob"
if idade > 13:
 if Nome == "Bob":   #aqui temos um if dentro de outro if (aninhado), o segundo if ´so será executado se o primeiro if for true.
    print("Ok Bob, você está autorizado a entrar!")
 else:
   print("Desculpe, mas você não pode entrar!")


# In[21]:


idade = 13
Nome = "Bob"
if idade >= 13 and Nome == "Bob":  #uso do AND(operador lógico), aqui as duas condições tem que ser true.
    print("Ok Bob, você está autorizado a entrar!")


# In[22]:


idade = 12
Nome = "Bob"
if (idade >= 13) or (Nome == "Bob"):    #uso do OR(operador lógico), aqui basta q uma condição seja true.
    print("Ok Bob, você está autorizado a entrar!")


# # Elif

# In[25]:


dia = "Quarta"
if dia == "Segunda":
  print("Hoje fará sol!")
else:
  print("Hoje vai chover!")


# In[26]:


if dia == "Segunda":        # uso do elif: se for segunda..hj fará sol. Se for terça..hj vai chover. SE FOR QUALQUER OUTRO DIA.."Sem previsão do tempo para o dia selecionado"
  print("Hoje fará sol!")
elif dia == "Terça":
  print("Hoje vai chover!")
else:
  print("Sem previsão do tempo para o dia selecionado")


# In[ ]:




