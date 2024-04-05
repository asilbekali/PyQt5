class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def output(self):
        print(self.hour*60+self.minute+self.second/60, "minut bor\n\n")

    def minute_count(self):
        return self.hour * 60 + self.minute

    def add_10_minutes(self):
        total_minutes = self.minute_count() + 10
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

objects = []
for i in range(5):
    hour, minute, second = map(int, input(f"Obyekt {i+1}: Soat:Daqiqa:Sekund : orqalik kiriting ").split(":"))
    time_obj = Time(hour, minute, second)
    objects.append(time_obj)

for obj in objects:
    if obj.hour == 23 and obj.minute > 49:
        obj.hour = (obj.hour + 1) % 24
    obj.output()
    obj.add_10_minutes()
    print("Obyekt", objects.index(obj)+1, "uchun 10 daqiqa qo'shilgandan kigin:", obj.hour, "soat", obj.minute, "daqiqa")
