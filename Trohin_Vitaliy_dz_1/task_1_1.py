def convert_time(duration: int):
    seconds = duration
    day = seconds // 86400
    hour = (seconds - day * 86400) // 3600
    minute = (seconds - hour * 3600) // 60 % 60
    second = seconds % 60
    return f'{day} дн {hour} час {minute} мин {second} сек'

duration = 400153
result = convert_time(duration)
print(result)
