import pandas as pd
from bot.utils.excel_reader import read_excel_file
from bot.utils.validators import validate_topic_format

def process_topics(file_path: str) -> dict:
    df = read_excel_file(file_path)

    errors = []
    total_checked = 0

    for _, row in df.iterrows():
        if pd.notna(row.get('Тема урока')):
            total_checked += 1
            topic = str(row['Тема урока']).strip()

            if not validate_topic_format(topic):
                error_info = {
                    'date': row.get('Date', 'Не указана'),
                    'teacher': row.get('ФИО преподавателя', 'Не указан'),
                    'subject': row.get('Предмет', 'Не указан'),
                    'group': row.get('Группа', 'Не указана'),
                    'topic': topic
                }
                errors.append(error_info)

    return {
        "errors": errors,
        "total_errors": len(errors),
        "total_checked": total_checked
    }
