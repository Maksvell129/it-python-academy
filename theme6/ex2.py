def process_telemetry(device_id: str, status: str = 'stable', *args: float) -> float | str | int | None:
    if status == 'critical':
        return f'Критический сбой оборудования {device_id}!'

    if not args:
        return 0

    return sum(args) / len(args)

log1 = process_telemetry('d1', 'critical',36.6, 120.0)
print(f'Пример 1: {log1}')
log3 = process_telemetry('d3')
print(f'Пример 3: {log3}')


def process_telemetry(device_id: str, status: str = "stable", *args: float):
    if status == "critical":
        return f"Критический сбой оборудования {device_id}!"
    if not args:
        return 0

    average = sum(args) / len(args)
    return average


print(process_telemetry("b00047378", "critical"))
print(process_telemetry("b00047378", "stable", 26, 25, 98))