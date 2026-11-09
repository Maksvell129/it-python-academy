from functools import wraps



def repeat(num_times: int):

    def decorator_repeat(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(num_times):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator_repeat



@repeat(num_times=3)
def greet(name: str):
    """Приветствует пользователя."""
    print(f"Привет, {name}!")


@repeat(num_times=2)
def bye(name: str):
    """Приветствует пользователя."""
    print(f"Пока, {name}!")


@repeat(num_times=2)
def heavy_computation(n: int) -> int:
    """heavy_computation docs"""
    print("вызов")
    return sum(i ** 2 for i in range(n))

# greet("Alex")
# bye("Bob")
print(heavy_computation(1000))
