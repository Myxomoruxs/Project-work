import pandas as pd
from bot.utils.excel_reader import read_excel_file


def process_students(file_path: str) -> dict:
    df = read_excel_file(file_path)

    students = []

    for _, row in df.iterrows():
        homework = row.get('Homework', None)
        classroom = row.get('Classroom', None)

        if pd.notna(homework) and pd.notna(classroom):
            try:
                homework_val = float(homework)
                classroom_val = float(classroom)

                if homework_val <= 1 and classroom_val < 3:
                    student_info = {
                        'fio': row.get('FIO', 'Не указано'),
                        'group': row.get('Группа', 'Не указана'),
                        'homework': homework_val,
                        'classroom': classroom_val
                    }
                    students.append(student_info)
            except (ValueError, TypeError):
                continue

    return {
        "students": students,
        "total": len(students)
    }
