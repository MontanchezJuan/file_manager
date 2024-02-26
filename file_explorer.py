import os
import re
from enum import Enum

class Explorer:
    def __init__(self, folder_path, search_word) -> None:
        self.folder_path = folder_path
        self.search_word = search_word
        self.files = []

    def get_files(self):
        try:
            for file_name in os.listdir(self.folder_path):
                if self.validate_extension(file_name):
                    file_path = os.path.join(self.folder_path, file_name)
                    self.files.append([file_path, file_name])
                else:
                    print(f"El archivo {file_name} no corresponde a un archivo de texto")
        except Exception:
            print("\nLa ruta ingresada no existe en su dispositivo")
            return

    def validate_extension(self, file_name: str):
        for ext in Extension:
            if file_name.lower().endswith(ext.value):
                return True
        return False

    def search_word_in_files(self):
        if len(self.files) > 0:
            total_count = 0
            print(f"\nPalabra buscada: {self.search_word}")
            print("Resultado esperado:")
            for file in self.files:
                file_instance = File(file_path=file[0])
                file_instance.read_content()
                count = file_instance.count_words(search_word=self.search_word)
                print(f"{file[1]}: {count} veces")
                total_count += count
            print(f"Total: {total_count}\n")

class File:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.extension = ""
        self.content = ""

    def read_content(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"No se pudo encontrar el archivo: {self.file_path}")
            return 0
        except Exception as e:
            print(f"Error al leer el archivo {self.file_path}: {e}")
            return 0

    def count_words(self, search_word):
        try:
            matches = re.findall(r'\b' + re.escape(search_word) + r'\b', self.content, re.IGNORECASE)
            return len(matches)
        except:
            print("Error al contar las palabras")

class Extension(Enum):
    TEXT = ".txt"
    XML = ".xml"
    JSON = ".json"
    CSV = ".csv"

if __name__ == "__main__":
    try:
        folder_path = input("Ingrese la ruta de la carpeta (por ejemplo, c:/datos/archivos): ")
        search_word = input("Ingrese la palabra que desea buscar: ")
        explorer = Explorer(folder_path=folder_path, search_word=search_word)
        explorer.get_files()
        explorer.search_word_in_files()
    except Exception as e:
        print(e)
