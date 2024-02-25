"""Obtendo Biblioteca"""
 
"""É necessario instalar o pacote, pip install pypdf2"""

"""Importando"""

import PyPDF2
import os

"""merger é um mesclador"""
merger = PyPDF2.PdfMerger()

"""lista os diretorios"""
lista_arquivos = os.listdir("arquivos")
print(lista_arquivos)