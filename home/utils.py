from datetime import datetime, time

def is_restaurant_open():
    now = datetime.now()

    current_time = now.time()
    current_day = now.weekday() # Monday = 0, Sunday = 6
    # Opening hours
    if current_day < 5: #Monday to Friday
        opening_time = time(9, 0)
        closing_time = time(22, 0)
    else: #Saturday & Sunday
        opening_time = time(10, 0)
        closing_time = time(23, 0)
        # Check if open
    if opening_time <= current_time <= closing_time:
        return True
    else:
        return False
