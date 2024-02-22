import os  # Módulo para interactuar con el sistema operativo
import re  # Módulo para trabajar con expresiones regulares

class MainProgram:
    """
    Clase principal del programa que cuenta las ocurrencias de una palabra en archivos de texto dentro de una carpeta.
    """

    def __init__(self):
        """
        Constructor de la clase MainProgram.
        Inicializa los atributos folder_path y search_word.
        """
        self.folder_path = ""  # Ruta de la carpeta proporcionada por el usuario
        self.search_word = ""  # Palabra que el usuario desea buscar en los archivos

    def run(self):
        """
        Método principal que ejecuta el programa.
        Llama a get_user_input() para obtener la ruta de la carpeta y la palabra a buscar,
        y luego llama a search_word_in_files() para buscar la palabra en los archivos.
        """
        self.get_user_input()
        self.search_word_in_files()

    def get_user_input(self):
        """
        Método para obtener la entrada del usuario.
        Solicita al usuario que ingrese la ruta de la carpeta y la palabra a buscar.
        """
        self.folder_path = input("Ingrese la ruta de la carpeta (por ejemplo, c:/datos/archivos): ")
        self.search_word = input("Ingrese la palabra que desea buscar: ")

    def search_word_in_files(self):
        """
        Método para buscar la palabra en los archivos de la carpeta.
        Itera sobre cada archivo en la carpeta y cuenta las ocurrencias de la palabra.
        Imprime los resultados en la consola.
        """
        try:
            total_count = 0  # Inicializa el contador total de ocurrencias
            print(f"\nPalabra buscada: {self.search_word}")
            print("Resultado esperado:")
            # Itera sobre cada archivo en la carpeta
            for file_name in os.listdir(self.folder_path):
                # Verifica si el archivo es de un tipo de texto válido
                if file_name.endswith(('.txt', '.xml', '.json', '.csv')):
                    file_path = os.path.join(self.folder_path, file_name)  # Ruta completa del archivo
                    count = self.count_word_in_file(file_path)  # Cuenta las ocurrencias de la palabra en el archivo
                    print(f"{file_name}: {count} veces")  # Imprime el nombre del archivo y su conteo
                    total_count += count  # Suma el conteo al total
                else:
                    print(f"El archivo {file_name} no corresponde a un archivo de texto")
            print(f"Total: {total_count}\n")  # Imprime el total de ocurrencias en la carpeta
        except Exception:
            print("\nLa ruta ingresada no existe en su dispositivo")
            return

    def count_word_in_file(self, file_path):
        """
        Método para contar las ocurrencias de la palabra en un archivo específico.
        Args:
            file_path: Ruta completa del archivo a procesar.
        Returns:
            int: Número de ocurrencias de la palabra en el archivo.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()  # Lee el contenido completo del archivo
                # Busca todas las ocurrencias de la palabra, ignorando mayúsculas y minúsculas
                matches = re.findall(r'\b' + re.escape(self.search_word) + r'\b', content, re.IGNORECASE)
                return len(matches)  # Retorna el número de ocurrencias encontradas
        except FileNotFoundError:
            print(f"No se pudo encontrar el archivo: {file_path}")
            return 0
        except Exception as e:
            print(f"Error al leer el archivo {file_path}: {e}")
            return 0

if __name__ == "__main__":
    # Instancia de la clase MainProgram y ejecución del programa
    program = MainProgram()
    program.run()
