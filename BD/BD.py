from django.db import models

#������ 1

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
    
    
#������ 2

class InfoFlightSchedule(models.Model): #���������� ������
    FlightNumber = models.IntegerField() #����� �����
    TypeAircraft = models.CharField() #��� ��������
    StartPunct = models.CharField()
    EndPunkt = models.CharField()
    DepartureDate = models.DateTimeField() #����� � ���� ������
    FlightTime = models.FloatField() #����� ������
    Price = models.FloatField() #���� ������
    
class InfoFreePlaces(models.Model):
    FlightScheduleID = models.ForeignKey('InfoFlightSchedule')
    PassengerID = models.OneToOneField('InfoPassenger')
    AllPlaces = models.IntegerField() #����� ���������� ����
    FreePlaces = models.IntegerField() #���������� ��������� ����
    
class InfoPassenger(models.Model):
    NumberPassport = models.IntegerField()
    Surname = models.CharField()
    Name = models.CharField()
    FatheName = models.CharField()
    
    
class Archive(models.Model):
    FreePlacesID = models.ForeignKey('InfoFreePlaces')
    SoldPlaces = models.IntegerField()#��������� �����
    
    
#������ 3

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
    
    
#������ 4
class Firma(models.Model):
    NameOrganization = models.CharField()

class Goods(models.Model):
    NameGoods = models.CharField()
    UniqueCode = models.IntegerField()
    Data = models.DateTimeField()
    GuaranteePeriod = models.IntegerField()
    UnitMeasure = models.CharField()

class FirmaGoods(models.Model): #������ �����������
    GoodsID = models.ForeignKey('Goods')
    FirmaID = models.ForeignKey('Firma')
    NumberGoods = models.IntegerField()
    PriceGood = models.FloatField()
    
class Party(models.Model):
    FirmaGoodsID = models.ForeignKey('FirmaGoods')
    NumberParty = models.IntegerField()
    TheSupplier = models.BooleanField() #� ����������� ��� ���

    

    
# ������ 5


class Customer(models.Model):
    NameOrganization = models.CharField() #��� 
    Price = models.FloatField() #���� ������
    Date = models.DateField() #���� ���������� ������
    
class Equipment(models.Model): #������������
    NameEquipment = models.CharField()
    
class Bid(models.Model): #������
    CustomerID = models.ForeignKey('Customer')
    EquipmentID = models.ForeignKey('Equipment')
    NumberEquipment = models.IntegerField()
    
class Order(models.Model):
    NameOrder = models.CharField()
    BidID = models.ForeignKey('Bid')
    
    
