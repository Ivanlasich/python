import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext (self):
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)



class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        s = self.body_whl
        try:
            x = float(s[0:s.find('x')])
            s = s[s.find('x') + 1:]
            y = float(s[0:s.find('x')])
            s = s[s.find('x') + 1:]
            z = float(s)
        except ValueError:
            x = 0.0
            y = 0.0
            z = 0.0

        self.body_length = x
        self.body_width = y
        self.body_height = z

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    s = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        i = 0
        for row in reader:
            if (row):
                i = i + 1
                s.append(row)

    for j in range(i):
        if s[j][0] == 'car':
            car_list.append(Car(s[j][1], s[j][3], float(s[j][5]), int(s[j][2])))
        elif s[j][0] == 'truck':
            car_list.append(Truck(s[j][1], s[j][3], float(s[j][5]), s[j][4]))
        elif s[j][0] == 'spec_machine':
            car_list.append(SpecMachine(s[j][1], s[j][3], float(s[j][5]), s[j][6]))
        else:
            pass

    return car_list

