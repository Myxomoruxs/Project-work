import asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.states.report_states import ReportStates
from bot.keyboards.inline import get_main_menu_kb
from bot.utils.file_handler import download_file, validate_file_extension, validate_file_size, cleanup_file
from bot.utils.formatters import (
    format_schedule_report,
    format_topics_report,
    format_students_report,
    format_attendance_report,
    format_homework_check_report,
    format_homework_submit_report
)
from bot.services.schedule_service import process_schedule
from bot.services.topics_service import process_topics
from bot.services.students_service import process_students
from bot.services.attendance_service import process_attendance
from bot.services.homework_check_service import process_homework_check
from bot.services.homework_submit_service import process_homework_submit

router = Router()


@router.message(ReportStates.waiting_schedule_file)
async def process_schedule_file(message: Message, state: FSMContext):
    if not message.document:
        await message.answer("Пожалуйста, отправьте файл документом (.xls или .xlsx)")
        return

    if not validate_file_extension(message.document.file_name):
        await message.answer(
            "❌ Неподдерживаемый формат файла.\n"
            "Пожалуйста, загрузите файл в формате .xls или .xlsx"
        )
        return

    if not validate_file_size(message.document.file_size):
        await message.answer("❌ Файл слишком большой. Максимальный размер: 20 МБ")
        return

    processing_msg = await message.answer("⏳ Обрабатываю файл...")

    try:
        file_path = await download_file(message.bot, message.document.file_id, message.from_user.id)

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, process_schedule, file_path)

        report_text = format_schedule_report(result)
        await processing_msg.delete()
        await message.answer(report_text, reply_markup=get_main_menu_kb())

        cleanup_file(file_path)
        await state.clear()

    except Exception as e:
        await processing_msg.delete()
        await message.answer(
            f"❌ Ошибка при обработке файла.\n"
            f"Проверьте корректность структуры данных и попробуйте снова.\n\n"
            f"Детали: {str(e)}",
            reply_markup=get_main_menu_kb()
        )
        await state.clear()


@router.message(ReportStates.waiting_topics_file)
async def process_topics_file(message: Message, state: FSMContext):
    if not message.document:
        await message.answer("Пожалуйста, отправьте файл документом (.xls или .xlsx)")
        return

    if not validate_file_extension(message.document.file_name):
        await message.answer(
            "❌ Неподдерживаемый формат файла.\n"
            "Пожалуйста, загрузите файл в формате .xls или .xlsx"
        )
        return

    if not validate_file_size(message.document.file_size):
        await message.answer("❌ Файл слишком большой. Максимальный размер: 20 МБ")
        return

    processing_msg = await message.answer("⏳ Обрабатываю файл...")

    try:
        file_path = await download_file(message.bot, message.document.file_id, message.from_user.id)
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, process_topics, file_path)

        report_text = format_topics_report(result)
        await processing_msg.delete()
        await message.answer(report_text, reply_markup=get_main_menu_kb())

        cleanup_file(file_path)
        await state.clear()

    except Exception as e:
        await processing_msg.delete()
        await message.answer(
            f"❌ Ошибка при обработке файла.\n"
            f"Детали: {str(e)}",
            reply_markup=get_main_menu_kb()
        )
        await state.clear()


@router.message(ReportStates.waiting_students_file)
async def process_students_file(message: Message, state: FSMContext):
    if not message.document:
        await message.answer("Пожалуйста, отправьте файл документом (.xls или .xlsx)")
        return

    if not validate_file_extension(message.document.file_name):
        await message.answer(
            "❌ Неподдерживаемый формат файла.\n"
            "Пожалуйста, загрузите файл в формате .xls или .xlsx"
        )
        return

    if not validate_file_size(message.document.file_size):
        await message.answer("❌ Файл слишком большой. Максимальный размер: 20 МБ")
        return

    processing_msg = await message.answer("⏳ Обрабатываю файл...")

    try:
        file_path = await download_file(message.bot, message.document.file_id, message.from_user.id)
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, process_students, file_path)

        report_text = format_students_report(result)
        await processing_msg.delete()
        await message.answer(report_text, reply_markup=get_main_menu_kb())

        cleanup_file(file_path)
        await state.clear()

    except Exception as e:
        await processing_msg.delete()
        await message.answer(
            f"❌ Ошибка при обработке файла.\n"
            f"Детали: {str(e)}",
            reply_markup=get_main_menu_kb()
        )
        await state.clear()


@router.message(ReportStates.waiting_attendance_file)
async def process_attendance_file(message: Message, state: FSMContext):
    if not message.document:
        await message.answer("Пожалуйста, отправьте файл документом (.xls или .xlsx)")
        return

    if not validate_file_extension(message.document.file_name):
        await message.answer(
            "❌ Неподдерживаемый формат файла.\n"
            "Пожалуйста, загрузите файл в формате .xls или .xlsx"
        )
        return

    if not validate_file_size(message.document.file_size):
        await message.answer("❌ Файл слишком большой. Максимальный размер: 20 МБ")
        return

    processing_msg = await message.answer("⏳ Обрабатываю файл...")

    try:
        file_path = await download_file(message.bot, message.document.file_id, message.from_user.id)
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, process_attendance, file_path)

        report_text = format_attendance_report(result)
        await processing_msg.delete()
        await message.answer(report_text, reply_markup=get_main_menu_kb())

        cleanup_file(file_path)
        await state.clear()

    except Exception as e:
        await processing_msg.delete()
        await message.answer(
            f"❌ Ошибка при обработке файла.\n"
            f"Детали: {str(e)}",
            reply_markup=get_main_menu_kb()
        )
        await state.clear()


@router.message(ReportStates.waiting_homework_check_file)
async def process_homework_check_file(message: Message, state: FSMContext):
    if not message.document:
        await message.answer("Пожалуйста, отправьте файл документом (.xls или .xlsx)")
        return

    if not validate_file_extension(message.document.file_name):
        await message.answer(
            "❌ Неподдерживаемый формат файла.\n"
            "Пожалуйста, загрузите файл в формате .xls или .xlsx"
        )
        return

    if not validate_file_size(message.document.file_size):
        await message.answer("❌ Файл слишком большой. Максимальный размер: 20 МБ")
        return

    processing_msg = await message.answer("⏳ Обрабатываю файл...")

    try:
        data = await state.get_data()
        period = data.get('period', 'month')

        file_path = await download_file(message.bot, message.document.file_id, message.from_user.id)
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, process_homework_check, file_path, period)

        report_text = format_homework_check_report(result)
        await processing_msg.delete()
        await message.answer(report_text, reply_markup=get_main_menu_kb())

        cleanup_file(file_path)
        await state.clear()

    except Exception as e:
        await processing_msg.delete()
        await message.answer(
            f"❌ Ошибка при обработке файла.\n"
            f"Детали: {str(e)}",
            reply_markup=get_main_menu_kb()
        )
        await state.clear()


@router.message(ReportStates.waiting_homework_submit_file)
async def process_homework_submit_file(message: Message, state: FSMContext):
    if not message.document:
        await message.answer("Пожалуйста, отправьте файл документом (.xls или .xlsx)")
        return

    if not validate_file_extension(message.document.file_name):
        await message.answer(
            "❌ Неподдерживаемый формат файла.\n"
            "Пожалуйста, загрузите файл в формате .xls или .xlsx"
        )
        return

    if not validate_file_size(message.document.file_size):
        await message.answer("❌ Файл слишком большой. Максимальный размер: 20 МБ")
        return

    processing_msg = await message.answer("⏳ Обрабатываю файл...")

    try:
        file_path = await download_file(message.bot, message.document.file_id, message.from_user.id)
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, process_homework_submit, file_path)

        report_text = format_homework_submit_report(result)
        await processing_msg.delete()
        await message.answer(report_text, reply_markup=get_main_menu_kb())

        cleanup_file(file_path)
        await state.clear()

    except Exception as e:
        await processing_msg.delete()
        await message.answer(
            f"❌ Ошибка при обработке файла.\n"
            f"Детали: {str(e)}",
            reply_markup=get_main_menu_kb()
        )
        await state.clear()
