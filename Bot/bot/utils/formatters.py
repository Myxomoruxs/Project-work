def format_schedule_report(data: dict) -> str:
    text = "📊 Отчет по расписанию\n\n"
    text += f"Группа: {data['group']}\n\n"
    text += "Дисциплины:\n"

    for subject, count in sorted(data['subjects'].items(), key=lambda x: x[1], reverse=True):
        text += f"• {subject} - {count} {'пара' if count == 1 else 'пары' if count < 5 else 'пар'}\n"

    text += f"\nВсего: {data['total']} {'пара' if data['total'] == 1 else 'пары' if data['total'] < 5 else 'пар'}"
    return text


def format_topics_report(data: dict) -> str:
    if data['total_errors'] == 0:
        return "✅ Все темы занятий оформлены корректно!"

    text = "⚠️ Отчет по темам занятий (некорректный формат)\n\n"
    text += f"Найдено несоответствий: {data['total_errors']}\n"
    text += f"Всего проверено: {data['total_checked']}\n\n"

    for i, error in enumerate(data['errors'][:50], 1):  # Ограничиваем 50 записями
        text += f"{i}. Дата: {error['date']}\n"
        text += f"   Преподаватель: {error['teacher']}\n"
        text += f"   Предмет: {error['subject']}\n"
        text += f"   Группа: {error['group']}\n"
        text += f"   Тема: \"{error['topic']}\"\n"
        text += f"   ❌ Ожидается: \"Урок № X. Тема: ...\"\n\n"

    if data['total_errors'] > 50:
        text += f"... и ещё {data['total_errors'] - 50} несоответствий"

    return text


def format_students_report(data: dict) -> str:
    if data['total'] == 0:
        return "✅ Студентов с низкой успеваемостью не найдено!"

    text = "📋 Отчет по студентам с низкой успеваемостью\n\n"
    text += f"Найдено студентов: {data['total']}\n"
    text += f"Критерии: Домашняя работа ≤ 1, Классная работа < 3\n\n"

    for i, student in enumerate(data['students'], 1):
        text += f"{i}. {student['fio']}\n"
        text += f"   Группа: {student['group']}\n"
        text += f"   Домашняя работа: {student['homework']}\n"
        text += f"   Классная работа: {student['classroom']}\n\n"

    return text


def format_attendance_report(data: dict) -> str:
    if data['total'] == 0:
        return "✅ Преподавателей с посещаемостью ниже 40% не найдено!"

    text = "📉 Отчет по посещаемости (ниже 40%)\n\n"
    text += f"Найдено преподавателей: {data['total']}\n\n"

    for i, teacher in enumerate(data['teachers'], 1):
        text += f"{i}. {teacher['fio']}\n"
        text += f"   Посещаемость: {teacher['attendance']}%\n"
        if 'total_pairs' in teacher and teacher['total_pairs']:
            text += f"   Всего пар: {teacher['total_pairs']}\n"
        text += "\n"

    return text


def format_homework_check_report(data: dict) -> str:
    period_name = "месяц" if data['period'] == "month" else "неделю"

    if data['total'] == 0:
        return f"✅ Все преподаватели проверяют более 70% заданий за {period_name}!"

    text = f"📝 Отчет по проверенным ДЗ за {period_name}\n\n"
    text += f"Преподаватели с процентом проверки < 70%:\n"
    text += f"Найдено: {data['total']}\n\n"

    for i, teacher in enumerate(data['teachers'], 1):
        text += f"{i}. {teacher['fio']}\n"
        text += f"   Получено: {teacher['received']}\n"
        text += f"   Проверено: {teacher['checked']}\n"
        text += f"   Процент: {teacher['percentage']}%\n\n"

    return text


def format_homework_submit_report(data: dict) -> str:
    if data['total'] == 0:
        return "✅ Все студенты выполняют более 70% заданий!"

    text = "📚 Отчет по сданным ДЗ студентов\n\n"
    text += f"Студенты с % выполнения < 70%:\n"
    text += f"Найдено: {data['total']}\n\n"

    for i, student in enumerate(data['students'], 1):
        text += f"{i}. {student['fio']}\n"
        text += f"   Группа: {student['group']}\n"
        text += f"   Процент выполнения: {student['percentage']}%\n\n"

    return text
