import pandas as pd
from bot.utils.excel_reader import read_excel_file


def process_homework_check(file_path: str, period: str = "month") -> dict:
    df = read_excel_file(file_path)

    teachers = []
    columns = df.columns.tolist()

    df_data = df.iloc[1:]

    for _, row in df_data.iterrows():
        fio = row.iloc[1] if len(row) > 1 else None

        if pd.isna(fio) or fio == 'ФИО преподавателя':
            continue

        try:
            if period == "month":
                received = row.iloc[4]
                checked = row.iloc[5]
            else:
                received = row.iloc[9]
                checked = row.iloc[10]

            received_val = float(received) if pd.notna(received) else 0
            checked_val = float(checked) if pd.notna(checked) else 0

            if received_val > 0:
                percentage = (checked_val / received_val) * 100
            else:
                percentage = 100

            if percentage < 70 and received_val > 0:
                teacher_info = {
                    'fio': fio,
                    'received': int(received_val),
                    'checked': int(checked_val),
                    'percentage': round(percentage, 1)
                }
                teachers.append(teacher_info)
        except (ValueError, TypeError, IndexError):
            continue

    return {
        "teachers": teachers,
        "period": period,
        "total": len(teachers)
    }
