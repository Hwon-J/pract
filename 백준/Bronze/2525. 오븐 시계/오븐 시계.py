hour, minute = map(int, input().split())
cook = int(input())

minute = minute + cook
if minute >= 60:
    hour = hour + (minute // 60)
    minute = minute % 60
    if hour >= 24:
        hour = hour % 24
print(hour, minute)
