from typing import List, Dict, Optional, Union
from pydantic import PositiveInt, NegativeInt, NonNegativeInt, NonPositiveInt, NegativeFloat, EmailStr

# 1. Аннотация списков и словарей (до Python 3.9)
# В Python 3.9+ можно просто: list[str], dict[str, int]
def process_users(users: List[str]) -> Dict[str, int]:
    return {user: len(user) for user in users}

def process_users2(users: list[EmailStr]) -> dict[str, int]:
    return {user: len(user) for user in users}



# 2. Множественные типы (Union или оператор | в Python 3.10+)
# Аргумент может быть либо целым числом, либо дробным
def scale_score(score: Union[PositiveInt, float]) -> Union[int, float]: # Python 3.10+: int | float
    return score * 1.5

def scale_score2(score: int | float) -> int | float: # Python 3.10+: int | float
    return score * 1.5


# 3. Необязательные значения (Optional или | None)
# Означает, что значение может быть строкой ИЛИ None
def find_user(user_id: int) -> Optional[str, int]: # Python 3.10+: str | None
    if user_id == 1:
        return "Алексей"
    return None


def find_user2(user_id: int) -> str | None: # Python 3.10+: str | None
    if user_id == 1:
        return "Алексей"
    return None
