from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.keyboards.inline import get_main_menu_kb, get_period_selection_kb
from bot.states.report_states import ReportStates

router = Router()


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = "Выберите тип отчета:"
    await callback.message.edit_text(text, reply_markup=get_main_menu_kb())
    await callback.answer()


@router.callback_query(F.data == "report:schedule")
async def select_schedule_report(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ReportStates.waiting_schedule_file)
    text = (
        "📊 Отчет по расписанию\n\n"
        "Загрузите Excel-файл с расписанием группы.\n"
        "Бот подсчитает количество пар по каждой дисциплине."
    )
    await callback.message.edit_text(text)
    await callback.answer()


@router.callback_query(F.data == "report:topics")
async def select_topics_report(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ReportStates.waiting_topics_file)
    text = (
        "📝 Отчет по темам занятий\n\n"
        "Загрузите Excel-файл с темами занятий.\n"
        "Бот найдет все темы с некорректным форматом.\n\n"
        "Правильный формат: \"Урок № X. Тема: ...\""
    )
    await callback.message.edit_text(text)
    await callback.answer()


@router.callback_query(F.data == "report:students")
async def select_students_report(callback: CallbackQuery, state: FSMContext):

    await state.set_state(ReportStates.waiting_students_file)
    text = (
        "📋 Отчет по студентам\n\n"
        "Загрузите Excel-файл с информацией о студентах.\n"
        "Бот найдет студентов с низкой успеваемостью:\n"
        "• Домашняя работа ≤ 1\n"
        "• Классная работа < 3"
    )
    await callback.message.edit_text(text)
    await callback.answer()


@router.callback_query(F.data == "report:attendance")
async def select_attendance_report(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ReportStates.waiting_attendance_file)
    text = (
        "📉 Отчет по посещаемости\n\n"
        "Загрузите Excel-файл с посещаемостью.\n"
        "Бот найдет преподавателей с посещаемостью < 40%."
    )
    await callback.message.edit_text(text)
    await callback.answer()


@router.callback_query(F.data == "report:homework_check")
async def select_homework_check_report(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ReportStates.selecting_period)
    text = (
        "✅ Проверка ДЗ (преподаватели)\n\n"
        "Выберите период для анализа:"
    )
    await callback.message.edit_text(text, reply_markup=get_period_selection_kb())
    await callback.answer()


@router.callback_query(F.data == "report:homework_submit")
async def select_homework_submit_report(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ReportStates.waiting_homework_submit_file)
    text = (
        "📚 Сдача ДЗ (студенты)\n\n"
        "Загрузите Excel-файл с данными о выполнении ДЗ студентами.\n"
        "Бот найдет студентов с процентом выполнения < 70%."
    )
    await callback.message.edit_text(text)
    await callback.answer()


@router.callback_query(F.data.startswith("period:"))
async def select_period(callback: CallbackQuery, state: FSMContext):
    period = callback.data.split(":")[1]  # month или week
    await state.update_data(period=period)
    await state.set_state(ReportStates.waiting_homework_check_file)

    period_name = "месяц" if period == "month" else "неделю"
    text = (
        f"✅ Проверка ДЗ за {period_name}\n\n"
        f"Загрузите Excel-файл с данными о проверке ДЗ.\n"
        f"Бот найдет преподавателей с процентом проверки < 70%."
    )
    await callback.message.edit_text(text)
    await callback.answer()
