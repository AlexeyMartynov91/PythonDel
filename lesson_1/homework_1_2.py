time = int(input("Вводите время в секундах: "))
seconds = time
minutes = seconds // 60
hours = minutes // 60
print(f"Введенное время: {hours:02d}:{minutes % 60:02d}:{seconds% 60:02d}")
