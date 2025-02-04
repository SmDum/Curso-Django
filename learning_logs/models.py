from django.db import models

# Create your models here.

class Topic(models.Model):
    '''Um assunto sobre o qual o usuário está aprendendo.'''
    text = models.CharField(max_length=200) #Cria um campo de texto com um limite de 200 caracteres
    date_added = models.DateTimeField(auto_now_add=True) #Cria um campo de data e hora que armazena a data e hora atuais sempre que o usuário criar um novo tópico
    
    def __str__(self):
        '''Devolve uma representação em string do modelo.'''
        return self.text