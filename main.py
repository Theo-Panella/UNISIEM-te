import re

# Padrão de Analise
# Data | Hora | IP de requisicao | IP de Destino | Serviço | Porta | Protocolo | Username | Hostname
# Tipo de log: Erro, acesso, alteração, requisição
file = open('logs.txt', 'r')
default_words = ['sshd','nginx','node-app','mysqld','kernel','docker','CRON','systemd']


search_Acess_in_file = re.findall("Acce.+",file.read()) #Coloca o resultado em array
print(search_Acess_in_file)

for i in range(len(search_Acess_in_file)):
    for c in range(len(default_words)):
        search_default_words = re.search(default_words[c],search_Acess_in_file[i])
