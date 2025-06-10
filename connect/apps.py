from django.apps import AppConfig



class ConnectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connect'

    #def ready(self):
        # Importar o módulo Group aqui para evitar erro de importação antecipada
        #from django.contrib.auth.models import Group

        # Função para criação dos grupos
        #def create_groups():
         #   Group.objects.get_or_create(name='Admin')
         #   Group.objects.get_or_create(name='Manager')
         #   Group.objects.get_or_create(name='Vendas')
          #  Group.objects.get_or_create(name='Financeiro')
          #  Group.objects.get_or_create(name='Producao')
          #  Group.objects.get_or_create(name='Logistica')

        # Chamar a função de criação dos grupos
       # create_groups()
