from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu_kb() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="📊 Отчет по расписанию", callback_data="report:schedule")],
        [InlineKeyboardButton(text="📝 Отчет по темам занятий", callback_data="report:topics")],
        [InlineKeyboardButton(text="📋 Отчет по студентам", callback_data="report:students")],
        [InlineKeyboardButton(text="📉 Отчет по посещаемости", callback_data="report:attendance")],
        [InlineKeyboardButton(text="🗳️ Проверка ДЗ (преподаватели)", callback_data="report:homework_check")],
        [InlineKeyboardButton(text="📚 Сдача ДЗ (студенты)", callback_data="report:homework_submit")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_period_selection_kb() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text="📅 Месяц", callback_data="period:month"),
            InlineKeyboardButton(text="📆 Неделя", callback_data="period:week")
        ],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_back_to_menu_kb() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text="⬅️ Вернуться в главное меню", callback_data="back_to_menu")]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
