from functools import wraps
from time import time
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., Optional[T]]]:
    def wrapper(func: Callable[..., T]) -> Callable[..., Optional[T]]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Optional[T]:
            try:
                time1 = time()
                result = func(*args, **kwargs)
                time2 = time()
                name_func = func.__name__
                log_message = (
                    f"Начало работы функции: {time1}\n"
                    f"{name_func} ок.\n"
                    f"Результат: {result}\n"
                    f"Конец работы функции: {time2}\n\n"
                )
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                name_func = func.__name__
                error_message = f"{name_func} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(error_message)
                else:
                    print(error_message)
                return None

        return inner

    return wrapper
