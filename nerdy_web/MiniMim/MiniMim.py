import re
import yaml

# Abre arquivo de configuração do pre-filtro
with open ('config.yaml', 'r' ) as file:
    data = yaml.safe_load(file)

# Se for Flask pega os paramentros dados e aplica compile para aumentar o desempenho

regex = {}

for service, config in data.items():
    regex[service] = {
        'failure': re.compile(config.get('Failure', '')),
        'accepted': re.compile(config.get('Accepted', ''))
    }
    
    print(regex['Flask'])
    
