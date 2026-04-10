# WAP for addition of two time zone (HH:MM:SS) using operator overloading.
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        total_seconds = self.seconds + other.seconds
        total_minutes = self.minutes + other.minutes + total_seconds // 60
        total_hours = self.hours + other.hours + total_minutes // 60

        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24  

        return Time(hours, minutes, seconds)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


t1 = Time(5, 45, 55)
t2 = Time(6, 30, 10)

t3 = t1 + t2
print("Time 1 =", t1)
print("Time 2 =", t2)
print("Sum =", t3)
