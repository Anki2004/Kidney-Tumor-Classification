import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format=f'%(asctime)s - %(name)s - %(levelname)s : %(message)s')
project_Name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_Name}/__init__.py",  #make empty file
    f"src/{project_Name}/components/__init__.py",
    f"src/{project_Name}/utils/__init__.py",
    f"src/{project_Name}/config/__init__.py",
    f"src/{project_Name}/config/configuration.py",
    f"src/{project_Name}/pipeline/__init__.py",
    f"src/{project_Name}/entity/__init__.py",
    f"src/{project_Name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    fileDir , fileName = os.path.split(filepath)

    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating directory: {fileDir} for the file: {fileName}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
