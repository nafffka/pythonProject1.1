seconds = int(input('Введите количество секунд: '))
minutes = seconds // 60
hours = minutes // 60

print('%02d:%02d:%02d' % (hours, minutes % 60, seconds % 60))
