# Scripts de Procesamiento de Datos del Repositorio MINCyT

Este repositorio contiene scripts en Python diseñados para recuperar, procesar y limpiar datos de los repositorios digitales del MINCyT (https://repositoriosdigitales.mincyt.gob.ar).
El archivo final .csv o .tsv está destinado a ser utilizado en análisis bibliométricos con la plataforma CorText.

## Descripción de los Scripts:
  **a_retrieve_and_save_mincyt_data.py**
  
  Este script realiza consultas a los repositorios digitales del MINCyT, recupera los datos de todas las páginas y los guarda en un solo archivo JSON. Cada record en el archivo es un diccionario donde cada item representa metadata de un record específico del repositorio, como un paper o una tesis de doctorado.
  
  Parámetros:
  
    query (str): La consulta de búsqueda a utilizar.
    results_per_page (str): El número de resultados a recuperar por página.
    start_page (str): El número de la página de inicio de los resultados a recuperar.
  
  **b_data_extractor.py**
  
  Este script convierte los archivos JSON del script anterior, en un archivo CSV.
  El archivo CSV final incluye las columnas: 'title', 'authors', 'date', 'subject', 'abstract', 'affiliation', 'publisher', 'language' y 'url'.
  
  **c_data_cleaning_csv.py**
  
  Este script elimina las filas que contienen una cadena especificada del archivo CSV y crea un archivo CSV limpio junto con un archivo que contiene las entradas eliminadas.
  Opcionalmente, puede eliminar el archivo original y renombrar el archivo limpio.
  
  Parámetros:
  
    string_to_remove (str): La cadena que se eliminará de las filas. La eliminación no distingue entre mayúsculas y minúsculas.
    file_name (str): El nombre del archivo CSV de entrada.
    original_file_option (str, opcional): Determina si conservar o eliminar el archivo original. Las opciones son 'keep' (predeterminado) o 'delete'.
  
  **csv_to_tsv.py**
  
  Este script convierte un archivo CSV en un archivo TSV. CorText, la plataforma utilizada para análisis bibliométricos, maneja mejor los archivos .tsv.

### Reconocimientos:
  Estos scripts fueron desarrollados por Agustín Mauro.
  Se agradece al MINCyT por proporcionar la API para la recuperación de datos.


# MINCyT Data Processing Scripts
  
  This repository contains Python scripts designed to retrieve, process, and clean data from the MINCyT digital repositories (https://repositoriosdigitales.mincyt.gob.ar).
  The final .csv or .tsv file is meant to be used in bibliometric analysis with CorText platform.
  
## Scripts Overview:
  **a_retrieve_and_save_mincyt_data.py**
  
  This script queries the MINCyT digital repositories using a specified search query, retrieves the data for all pages, and saves it to a single JSON file. Each record is a dictionary with items representing metadata for a specific repository record, such as a research paper or a thesis.
  
  Parameters:
  
    query (str): The search query to be used.
    results_per_page (str): The number of results to be retrieved per page.
    start_page (str): The starting page number of results to be retrieved.
  
  
  **b_data_extractor.py**
  
  This script converts the previous JSON files into a CSV file. 
  The final CSV file includes the following columns: 'title', 'authors', 'date', 'subject', 'abstract', 'affiliation', 'publisher', 'language', and 'url'. 
  
  **c_data_cleaning_csv.py**
  
  This script removes rows containing a specified string from a CSV file and creates a cleaned CSV file along with a file containing the removed entries.
  Optionally, it can delete the original file and rename the cleaned file.
  
  Parameters:
  
    string_to_remove (str): The string to be removed from the rows. The removal is case-insensitive.
    file_name (str): The name of the input CSV file.
    original_file_option (str, optional): Determines whether to keep or delete the original file. Options are 'keep' (default) or 'delete'.
  
  
  **csv_to_tsv.py**
  
  This script converts a CSV file to a TSV file. CorText, the platform used for bibliometric analysis, better handles .tsv files.
  
### Acknowledgments:
  These scripts were developed by Agustin Mauro.
  Thanks to the MINCyT for providing the API for data retrieval.
