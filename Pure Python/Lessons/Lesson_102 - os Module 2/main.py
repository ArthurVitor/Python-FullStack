import os, shutil

caminho_original = r'C:\Users\vitor\Desktop\Coisas'
caminho_novo = r'C:\Users\vitor\Desktop\New'

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.txt' in file:
            with open(file, 'r') as arq:
                for c in arq:
                    print(c)
