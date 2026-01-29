from aiogram.fsm.state import State, StatesGroup


class ReportStates(StatesGroup):

    waiting_schedule_file = State()
    waiting_topics_file = State()
    waiting_students_file = State()
    waiting_attendance_file = State()
    waiting_homework_check_file = State()
    waiting_homework_submit_file = State()

    selecting_period = State()
