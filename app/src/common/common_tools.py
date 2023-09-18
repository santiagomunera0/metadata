import os, sys
from src.extract.extract_metadata import extract_metadata

parameters = {
    'path': os.path.dirname(sys.path[0]),
    'path_in': os.path.join(os.path.dirname(sys.path[0]), '01_data'),
    'path_out': os.path.join(os.path.dirname(sys.path[0]), '02_output'),
    'docs': os.path.join(os.path.dirname(sys.path[0]), '01_data', 'docs'),
    'raw': os.path.join(os.path.dirname(sys.path[0]), '01_data', 'raw'),
    'curated': os.path.join(os.path.dirname(sys.path[0]), '01_data', 'curated')
}

def check_directories(dict_):
    """
    Check and create directories if they do not exist.

    Parameters
    ----------
    dict_ : dict
        A dictionary containing directory paths to be checked and created if necessary.

    Notes
    -----
    This function checks the existence of directories specified in the provided dictionary. If a directory does not exist,
    it creates the directory using the `os.mkdir()` function. The dictionary keys represent the names of the directories,
    and the values represent the corresponding paths.
    """
    for path in dict_.values():
        if not os.path.exists(path):
            os.mkdir(path)



""" def multiple_files(files):
    all_metadata = []  # Lista para almacenar metadatos de todos los archivos
    for file in files:
        metadata = extract_metadata(file)
        if metadata:
            all_metadata.append(metadata)  # Agrega los metadatos a la lista
    return all_metadata """