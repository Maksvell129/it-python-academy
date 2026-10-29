def save_device_info(model, **stats):
    print(model)
    for key, value in stats.items():
        print(f"Характеристика [{key}]: {value}")

# save_device_info(brand="Apple", model="iPhone 15", ram="8GB")

DATABASE = {}

# def get_users_from_db(**filters):
# 
#     DATABASE.get(filters)
#
#     # change status filters.get("user_ids")
#
# get_users_from_db(user_ids=[111,222,333,444], name_starts_with="A", name_ends_with="B")
