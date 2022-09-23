import os

search_path = r'C:\Users\vitor\Desktop\Coisas'
term = 'txt'
cont = 0


def size_format(size: float) -> str:
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = 'B'

    elif size < mega:
        size /= kilo
        text = 'KB'

    elif size < giga:
        size /= mega
        text = 'MB'

    elif size < tera:
        size /= giga
        text = 'GB'

    elif size < peta:
        size /= tera
        text = 'TB'

    else:
        size /= peta
        text = 'PB'

    size = round(size, 2)
    return f'{size}{text}'


for root, directory, arquivos in os.walk(search_path):
    for arquivo in arquivos:
        if term in arquivo:
            try:
                cont += 1
                complete_path = os.path.join(root, arquivo)  # Gets file path
                file_name, file_extension = os.path.splitext(arquivo)
                size = os.path.getsize(complete_path)
                print()
                print("I've found the file you're looking for")
                print(f'File: {arquivo}')
                print(f'Caminhos: {complete_path}')
                print(f'Name: {file_name}')
                print(f'Extension: {file_extension}')
                print(f'Size: {size}')
                print(f'Fixed size: {size_format(size)}')
            except PermissionError:
                print('Not allowed')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido', e)

print('Arquivos encontrados: ', cont)
