import pandas as pd
from pathlib import Path


def read_excel_file(file_path: str) -> pd.DataFrame:
    try:
        file_extension = Path(file_path).suffix.lower()

        if file_extension == ".xlsx":
            df = pd.read_excel(file_path, engine="openpyxl")
        elif file_extension == ".xls":
            df = pd.read_excel(file_path, engine="xlrd")
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {file_extension}")

        return df

    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {str(e)}")
