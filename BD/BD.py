from django.db import models

#Задача 1

class Car(models.Model):
    BrandCar = models.CharField()
    NumberCar = models.CharField()
    ColorCar = models.CharField()
    DataCar = models.DateField()
    MileageCar = models.FloatField()
    
class Driver(models.Model):
    NameDriver = models.CharField()
    SurnameDriver = models.CharField()
    
class DriverCar(models.Model):
    DriverID = models.ForeignKey('Driver')
    CarID = models.ForeignKey('Car')
    
class GradeFuel(models.Model):
    NameFuel = models.CharField()
    
class InfoShipping(models.Model):
    DataShipping = models.DateField('Data shipping')
    
    DriverCarID = models.ForeignKey('DriverCar')
    GradeFuelID = models.ForeignKey('GradeFuel')
    
    
    
#Задача 2

class InfoFlightSchedule(models.Model): #расписание рейсов
    FlightNumber = models.IntegerField() #номер рейса
    TypeAircraft = models.CharField() #тип самолета
    StartPunct = models.CharField()
    EndPunkt = models.CharField()
    DepartureDate = models.DateTimeField() #время и дата вылета
    FlightTime = models.FloatField() #время полета
    Price = models.FloatField() #цена билета
    
class InfoFreePlaces(models.Model): #свободные места в рейсе
    AllPlaces = models.IntegerField() #общее количество мест
    FreePlaces = models.IntegerField() #количество свободных мест
    
    InfoFlightScheduleID = models.ForeignKey('InfoFlightSchedule')
    
class PassengerPlaces(model.Models): #рейс пассажира
    InfoFreePlacesID = models.ForeignKey('InfoFreePlaces')
    PassengerID = models.ForeignKey('InfoPassenger')
    
class InfoPassenger(models.Model): #данные пассажира 
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
    
class Vacancy(models.Model):
    Position = models.CharField()
    Salary = models.FloatField()  
    OrganizationID = models.ForeignKey('Organization')
    
class Organization(models.Model):
    NameOrganization = models.CharField()
    
#class OrganizationVacancy(models.Model):
    #AgencyID = models.ForeignKey('Agency')
    #OrganizationVID = models.ForeignKey('Organization')
    
#Вопрос, нужен ли класс class OrganizationVacancy я имел ввиду
#что после того как вакансии и заявки были приняты агенством
#они передают данные классу class OrganizationVacancy где уже
#организация самостоятельно отбирает нужную заявку 


#ЗАДАЧА 4
class Firma(models.Model): #фирма
    NameOrganization = models.CharField()

class Goods(models.Model): #товары
    NameGoods = models.CharField()
    UniqueCode = models.IntegerField()
    Data = models.DateTimeField()
    GuaranteePeriod = models.IntegerField()
    UnitMeasure = models.CharField()

class FirmaGoods(models.Model): #товары фирмы
    GoodsID = models.ForeignKey('Goods')
    FirmaID = models.ForeignKey('Firma')
    NumberGoods = models.IntegerField()
    PriceGood = models.FloatField()
    
class Party(models.Model): #партия товаров
    FirmaGoodsID = models.ManyToManyField('FirmaGoods')
    NumberParty = models.IntegerField()
    TheSupplier = models.BooleanField() #с предоплатой или нет

    

    
# ЗАДАЧА 5


class Customer(models.Model): #предприятия 
    NameOrganization = models.CharField() #Имя 
    
class Equipment(models.Model): #оборудование
    NameEquipment = models.CharField()
    
class Bid(models.Model): #заявка
    CustomerID = models.ForeignKey('Customer')
    EquipmentID = models.ForeignKey('Equipment')
    
    NumberEquipment = models.IntegerField()
    
class Order(models.Model): #Заказ
    NameOrder = models.CharField()
    Price = models.FloatField() #Цена заказа
    Date = models.DateField() #Срок выполнения заказа    
    BidID = models.ForeignKey('Bid')
    
class SupplyEquipment(models.Model):
    NameCustomerID = models.ForeignKey('Customer')
    OrderID = models.ManyToManyField('Order')
    
# ЗАДАЧА 6

class Client(models.Model):
    CodeClient = models.IntegerField()
    NameClient = models.CharField()
    Surname = models.CharField()
    Country = models.CharField()
    Sity = models.CharField()
    TelephoneNumber = models.IntegerField()
    
class Room(models.Model):
    NumberRoom = models.IntegerField()
    NumberClass = models.IntegerField()
    PriceRoomDay = models.FloatField()
     
class InfoCach(models.Model):
    Date = models.DateTimeField()
    NumberDay = models.IntegerField()
    
    ClientID = models.ForeignKey('Client')
    RoomID = models.ForeignKey('Room')
    
class OtherServices(models.Model):
    TypeService = models.CharField() #вид услуги
    Date = models.DateTimeField()
    Price = models.FloatField()     
    
class Services(models.Model):
    OtherServicesID = models.ForeignKey('OtherServices')    
    CodeClientID = models.ForeignKey('Client')
    

# ЗАДАЧА 7
  
class Client(models.Model):
    InfoUser = models.BooleanField() # часное лици или организация
    NamePersone = models.CharField()
    SurnamePersone = models.CharField()
    Adress = models.CharField()
    TelephoneNumber = models.IntegerField()
    Fax = models.IntegerField()
    
class InfoOrder(models.Model):
    NumberOrder = models.IntegerField()
    ClientID = models.ForeignKey('Client')
    PrintedProducts = models.CharField()#вид печатной продукции
    
    EditionID = models.ForeignKey('InfoEdition') #издание
    PrintingHouseID = models.ForeignKey('InfoPrintingHouse') #Типография
    
    DateReceivingOrder = models.DateTimeField() #дата приема заказа
    PerformMark = models.BooleanField() #отметка о выполнении
    DateOrder = models.DateTimeField() #дата выполнения заказа
    
class InfoEdition(models.Model):
    CodeEdition = models.IntegerField() #код издания
    
    AuthorID = models.ForeignKey('Author') #Автор
    
    NameEdition = models.CharField() #название
    CapacityList = models.IntegerField() 
    Printing = models.IntegerField() #тираж
    NumberOrder = models.IntegerField() #номер заказа
    
class Author(models.Model):
    NameAuthor = models.CharField()
    SurName = models.CharField()
    HomeAdress = models.CharField()
    TelephonNumber = models.IntegerField()
    OtherInfo = models.CharField()
    
    
class InfoPrintingHouse(models.Model):
    NamePrintingHouse = models.CharField()
    AdressPrintingHouse = models.CharField()
    TelephonePrintingHouse = models.IntegerField()

#ЗАДАЧА 8

class Patient(models.Model):
    NumberMedicalHistory = models.IntegerField()
    NamePatient = models.CharField()
    SurNamePatient = models.CharField()
    HomeAdressPatient = models.CharField()
    TelephonePatient = models.IntegerField()
    
class Specialist(models.Model):
    NumberSpecialist = models.IntegerField()
    NameSpecialist = models.CharField()
    SurNameSpecialist = models.CharField()
    HomeAdressSpecialist = models.CharField()
    TelephoneSpecialist = models.IntegerField()    
    
class Visits(models.Model):
    PatientID = models.ForeignKey('Patient')
    SpecialistID = models.ForeignKey('Specialist') 
    NewVisit = models.BooleanField()
    DateVisit = models.DateTimeField()
    History = models.CharField() #анамнез
    Diagnosis = models.CharField()
    Treatment = models.CharField()#лечение
    PriceMedicine = models.FloatField() #Стоимость лекарств 
    PriceServices = models.FloatField() #СТоимость услуг 
    
    
class Archive(models.Model):
    VisitsID = models.ForeignKey('Visits')
    
