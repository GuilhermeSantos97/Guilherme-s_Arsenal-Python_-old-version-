
# <------------ATUALIZAÇÃO PYTHON ----------->
#python -m pip install --upgrade pip

# <------INSTALAÇÃO DAS BIBLIOTECA-------->
# pip install rembg.

# -----Biblioteca de imagens ---------
#python -m pip install --upgrade Pillow

import os

from tkinter.filedialog import askdirectory
from rembg import remove
from PIL import Image


def main():

    # Localizar a pasta que será feita a seleção da foto.
    foto = askdirectory(title="Selecione uma foto para remover o fundo")
    print(foto)


    # 2 Variáveis chamas de "input_path" e "output_path".
    # Input é entrada.
    # Output mais para saida.

    input_path = 'test.jpg'
    output_path = 'output.png'

    # Aqui será definido a entrada da Imagem (Input).
    input = Image.open(input_path)

    # O "OutPut" será definido como saida.
    # Ele vai Remover fundo da imagem através de uma variável chamada (input_path).
    output = remove(input) 
    output.save(output_path)


    # Os 2 iguais são definidos como resposta ao main.
if __name__ == "__main__":
    main()