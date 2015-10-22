from django.db import models

#Задача 1

class Car(models.Model):
    BrandCar = models.CharField()
    NumberCar = models.CharField()
    ColorCar = models.CharField()
    DataCar = models.DateField()
    MileageCar = models.FloatField()
    
class DriverCar(models.Model):
    NameDriver = models.CharField()
    SurnameDriver = models.CharField()
    
class GradeFuel(models.Model):
    NameFuel = models.CharField()
    
class InfoShipping(models.Model):
    
    CarID = models.ForeignKey('Car')
    DriverCarID = models.ForeignKey('DriverCar')
    GradeFuelID = models.ForeignKey('GradeFuel')
    DataShipping = models.DateField('Data shipping')
    
    
#Задача 2

class InfoFlightSchedule(models.Model): #расписание рейсов
    FlightNumber = models.IntegerField() #номер рейса
    TypeAircraft = models.CharField() #тип самолета
    StartPunct = models.CharField()
    EndPunkt = models.CharField()
    DepartureDate = models.DateTimeField() #время и дата вылета
    FlightTime = models.FloatField() #время полета
    Price = models.FloatField() #цена билета
    
class InfoFreePlaces(models.Model):
    FlightScheduleID = models.ForeignKey('InfoFlightSchedule')
    PassengerID = models.OneToOneField('InfoPassenger')
    AllPlaces = models.IntegerField() #общее количество мест
    FreePlaces = models.IntegerField() #количество свободных мест
    
class InfoPassenger(models.Model):
    NumberPassport = models.IntegerField()
    Surname = models.CharField()
    Name = models.CharField()
    FatheName = models.CharField()
    
    
class Archive(models.Model):
    FreePlacesID = models.ForeignKey('InfoFreePlaces')
    SoldPlaces = models.IntegerField()#проданные места
    
    
#ЗАДАЧА 3

class Workers(models.Model):
    Name = models.CharField()
    Surname = models.CharField()
    
class Bid(models.Model):
    WorkersID = models.OneToOneField('Workers')
    Position = models.CharField()
    Salary = models.FloatField()    
    
class Agency(models.Model):
    BidID = models.ForeignKey('Bid')
    VacancyID = models.ForeignKey('Vacancy')
    OrganizationBidID = models.ForeignKey('Organization')
    
class Vacancy(models.Model):
    Position = models.CharField()
    Salary = models.FloatField()  
    OrganizationID = models.ForeignKey('Organization')
    
class Organization(models.Model):
    NameOrganization = models.CharField()
    
    
#ЗАДАЧА 4
class Firma(models.Model):
    NameOrganization = models.CharField()

class Goods(models.Model):
    NameGoods = models.CharField()
    UniqueCode = models.IntegerField()
    Data = models.DateTimeField()
    GuaranteePeriod = models.IntegerField()
    UnitMeasure = models.CharField()

class FirmaGoods(models.Model): #товары организации
    GoodsID = models.ForeignKey('Goods')
    FirmaID = models.ForeignKey('Firma')
    NumberGoods = models.IntegerField()
    PriceGood = models.FloatField()
    
class Party(models.Model):
    FirmaGoodsID = models.ForeignKey('FirmaGoods')
    NumberParty = models.IntegerField()
    TheSupplier = models.BooleanField() #с предоплатой или нет

    

    
# ЗАДАЧА 5


class Customer(models.Model):
    NameOrganization = models.CharField() #Имя 
    Price = models.FloatField() #Цена заказа
    Date = models.DateField() #Срок выполнения заказа
    
class Equipment(models.Model): #оборудование
    NameEquipment = models.CharField()
    
class Bid(models.Model): #заявка
    CustomerID = models.ForeignKey('Customer')
    EquipmentID = models.ForeignKey('Equipment')
    NumberEquipment = models.IntegerField()
    
class Order(models.Model):
    NameOrder = models.CharField()
    BidID = models.ForeignKey('Bid')
    
    
