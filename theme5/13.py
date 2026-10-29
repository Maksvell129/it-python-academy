users_db = {
    "hacker_pro": {"role": "user", "warnings": 3, "status": "active"},
    "admin_main": {"role": "admin", "warnings": 0, "status": "active"},
    "shadow_bot": {"role": "guest", "warnings": 5, "status": "active"},
}

for username, data in users_db.items():
    if data["warnings"] >= 4:
        data["status"] = "blocked"
        print(f"Забанен: {username}")
    else:
        print(f"{username}: {data['status']}")
