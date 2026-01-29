import re


def validate_topic_format(topic: str) -> bool:
    if not isinstance(topic, str):
        return False

    pattern = r'^Урок\s*№\s*\d+\.\s*Тема:\s*.+'
    return bool(re.match(pattern, topic.strip()))


def is_valid_percentage(value) -> bool:
    if value is None:
        return False

    try:
        if isinstance(value, str):
            clean_value = value.strip().replace('%', '').replace(' ', '')
            float(clean_value)
            return True
        elif isinstance(value, (int, float)):
            return True
        else:
            return False
    except (ValueError, AttributeError):
        return False
