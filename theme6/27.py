from typing import Any


def get_user_stats(user_id: int) -> dict[str, Any]:
    posts_count = 42
    rating = 4.8
    is_active = True

    # return posts_count, rating, is_active
    return {
        "posts_count": posts_count,
        'rating': rating,
        "is_active": is_active,
    }


# 1. Распаковка сразу в 3 отдельные переменные (Мультиприсваивание)
ddd= get_user_stats(101)
# print(f"Постов: {posts}, Рейтинг: {score}")
print(f"Постов: {ddd["posts_count"]}, Рейтинг: {ddd["rating"]}")

# 2. Игнорирование ненужных значений с помощью символа подчеркивания `_`
# posts, _, _ = get_user_stats(101)  # Нам нужен только posts, остальное игнорируем

# posts, *_, active2 = get_user_stats(101)  # Нам нужен только posts, остальное игнорируем

