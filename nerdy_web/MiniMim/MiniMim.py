#====================================================================================
import time
import re
import yaml
from collections import deque
from watchdog.events import FileSystemEvent, FileSystemEventHandler,FileModifiedEvent
from watchdog.observers import Observer
#====================================================================================


#====================================================================================
# Variaveis Globais
lista_de_servico = ['Flask']
caminho_de_configuracao = "nerdy_web/MiniMim/config.yaml"
caminho_de_log = './flask_logs.txt'
quantidade_de_ultimas_linhas = 3
fila_de_linhas = []
#====================================================================================


#====================================================================================
# Abre o arquivo de Configuracao e compila, para melhor desempenho
#
# Ver como escalacionar o processo de compilacao (multiplas variacoes de configuracoes)

with open(caminho_de_configuracao, 'r') as arquivo_de_configuracao_puro:
    configuracao = yaml.safe_load(arquivo_de_configuracao_puro)
    Failure = re.compile(configuracao['Flask']['Failure'])
    Accepted = re.compile(configuracao['Flask']['Accepted'])
#====================================================================================


#====================================================================================
# Funcao de pre_Filtro do Flask
def flask_pre_filter(ultimas_linhas,Failure,Accepted):
    for cada_linha in ultimas_linhas:
        print(re.match(Failure,cada_linha.strip()))
        if re.search(Failure, cada_linha.strip()) or re.findall(Accepted, cada_linha.strip()):
            print('Log de Acesso encontrado')

#====================================================================================


#====================================================================================
# Classe evento do Watchdog
class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None:
        if event.src_path == "./flask_logs.txt" and event.event_type == "modified":
            print("Nova tentativa de Login detectada")
            print("Analisando log...")
            with open(caminho_de_log, "r", encoding="utf-8") as f:
                ultimas_linhas = deque(f, maxlen=quantidade_de_ultimas_linhas)
                flask_pre_filter(ultimas_linhas,Failure,Accepted)
#====================================================================================


#====================================================================================
#Chama evento e mantem em loop
event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
try:    
    while True:
        time.sleep(2)
finally:
    observer.stop()
    observer.join()
#====================================================================================