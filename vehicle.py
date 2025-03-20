# Aku
# Задание 2 (Транспорт)

print('Введите название бренда')
brand = str(input())
print('Введите название модели')
model = str(input())
print('Введите год выпуска')
year = str(input())

class Vehicle:

    def __init__(self,brand, model, year):
        self.brand = brand
        self.model= model
        self.year =year
        
    # Выводим информацию
    def info (self):
        print ("Название бренда", self.brand)
        print ("Название модели ", self.model)
        print ("Год выпуска", self.year)


class Car (Vehicle):

    def __init__(self,brand, model, year,fuel_type, max_speed, engine_capacity, rotation_speed):
        super().__init__(self,brand, model, year)
        self.fuel_type = fuel_type 
        self.max_speed= max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed
    
    
    def info(self):
        print ("Тип топлива {self.fuel_type}")
        print ("Максимальная скорость {self.max_speed}")
        print ("Обьём движка {self.engine_capacity}")
        print ("Частота вращения {self.rotation_speed}")
        
    # Мы работаем только с типом топлева бензин и дизель
    def engine_pover_calc(self): #Расчитываем мощность по обьёму
        if self.fuel_type == 'бензин' : # Если пользователь ввёл в типе топлева бензин
            pe = 0.85
            Ne = self.engine_capacity*pe*self.rotation_speed/120
            print('Мощность по обьёму=', Ne )
        else: # Если пользователь ввёл в типе топлева дизель
            pe = 1
            Ne = self.engine_capacity*pe*self.rotation_speed/120
            print('Мощность по обьёму=', Ne )


if __name__ == "__main__":
    
   ''' print('Введите название бренда')
    brand = str(input())
    print('Введите название модели')
    model = str(input())
    print('Введите год выпуска')
    year = str(input())

    print('Введите тип топлива (бензин или дизель)')
    fuel_type = str(input())
    print('Введите максимальную скорость')
    max_speed = str(input())
    print('Введите обьём движка')
    engine_capacity = str(input())
    print('Введите частоту вращения ')
    rotation_speed = str(input())'''
    
    
    








