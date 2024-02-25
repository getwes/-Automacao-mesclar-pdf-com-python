"""Obtendo Biblioteca"""
 
"""É necessario instalar o pacote, pip install pypdf2"""

"""Importando"""

import PyPDF2
import os

"""merger é um mesclador"""
merger = PyPDF2.PdfMerger()

"""lista os diretorios"""
lista_arquivos = os.listdir("arquivos")
""".sort para ordernar"""
lista_arquivos.sort()
print(lista_arquivos)

"""Criando uma condição"""
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")


"""salvando """
merger.write("PDF final.pdf")