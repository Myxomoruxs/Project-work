import pandas as pd
from bot.utils.excel_reader import read_excel_file


def process_attendance(file_path: str) -> dict:
    df = read_excel_file(file_path)

    teachers = []

    for _, row in df.iterrows():
        attendance_raw = row.get('Средняя посещаемость', None)

        if pd.notna(attendance_raw):
            try:
                if isinstance(attendance_raw, str):
                    attendance_val = float(attendance_raw.strip().replace('%', '').replace(' ', ''))
                else:
                    attendance_val = float(attendance_raw)

                if attendance_val < 40:
                    teacher_info = {
                        'fio': row.get('ФИО преподавателя', 'Не указан'),
                        'attendance': round(attendance_val, 1),
                        'total_pairs': row.get('Всего пар', None)
                    }
                    teachers.append(teacher_info)
            except (ValueError, TypeError):
                continue

    return {
        "teachers": teachers,
        "total": len(teachers)
    }
