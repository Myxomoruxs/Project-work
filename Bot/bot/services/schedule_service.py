import re
import pandas as pd
from bot.utils.excel_reader import read_excel_file


def process_schedule(file_path: str) -> dict:
    df = read_excel_file(file_path)

    group_name = df.iloc[0, 0] if pd.notna(df.iloc[0, 0]) else "Неизвестная группа"

    day_columns = [col for col in df.columns if any(day in str(col) for day in
                  ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'])]

    subjects_count = {}

    pattern = r'Предмет:\s*(.+?)(?:\n|$)'

    for col in day_columns:
        for value in df[col]:
            if pd.notna(value) and isinstance(value, str):
                matches = re.findall(pattern, value)
                for subject in matches:
                    subject = subject.strip()
                    if subject:
                        subjects_count[subject] = subjects_count.get(subject, 0) + 1

    total_pairs = sum(subjects_count.values())

    return {
        "group": group_name,
        "subjects": subjects_count,
        "total": total_pairs
    }
