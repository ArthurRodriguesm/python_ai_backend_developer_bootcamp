import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent # Retorna o caminho da pasta atual com um diretório acima

# os.mkdir(ROOT_PATH/'NOVO DIRETORIO') # Criando diretório

# os.rename(ROOT_PATH/'novo_arquivo.txt', ROOT_PATH/'renomeado_novo_arquivo.txt') # Renomeando arquivo

# os.remove(ROOT_PATH/'renomeado_novo_arquivo.txt') # Removendo arquivo

shutil.move(ROOT_PATH / 'arquivo.txt', ROOT_PATH / 'NOVO DIRETORIO' / 'arquivo.txt') # Movendo arquivo