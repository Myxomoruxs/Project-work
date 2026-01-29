import pandas as pd
from bot.utils.excel_reader import read_excel_file


def process_homework_submit(file_path: str) -> dict:
    df = read_excel_file(file_path)
    students = []
    percentage_column = None
    for col in df.columns:
        if 'Percentage Homework' in str(col):
            percentage_column = col
            break

    if percentage_column is None:
        return {"students": [], "total": 0}

    for _, row in df.iterrows():
        percentage_raw = row.get(percentage_column, None)

        if pd.notna(percentage_raw):
            try:
                if isinstance(percentage_raw, str):
                    percentage_val = float(percentage_raw.strip().replace('%', '').replace(' ', ''))
                else:
                    percentage_val = float(percentage_raw)

                if percentage_val < 70:
                    student_info = {
                        'fio': row.get('FIO', 'Не указано'),
                        'group': row.get('Группа', 'Не указана'),
                        'percentage': round(percentage_val, 1)
                    }
                    students.append(student_info)
            except (ValueError, TypeError):
                continue

    return {
        "students": students,
        "total": len(students)
    }
