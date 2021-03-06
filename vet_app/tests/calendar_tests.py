import unittest
from models.calendar import Calendar
from models.appointment import Appointment
from models.vet import Vet
from models.pet import Pet
from models.owner import Owner
import datetime

class CalendarTest(unittest.TestCase):
    def setUp(self):
        self.owner1 = Owner("Sara", "Humphries", "01234", "21, Millar Crescent")
        self.vet1 = Vet("Anna", "Hall")
        self.pet1 = Pet("Squeak", "13/04/2020", "Small animal", self.owner1, self.vet1, "good rat") 
        self.appointment1 = Appointment(datetime.date(2021,3,14), 4, "check up", self.vet1, self.pet1, True)
        self.appointment2 = Appointment(datetime.date(2021,4,4), 4, "check up", self.vet1, self.pet1, True)
        self.appointment3 = Appointment(datetime.date(2021,4,4), 4, "check down", self.vet1, self.pet1, True)

        appointments = [self.appointment1]
        self.calendar = Calendar(appointments)

    def test_calendar_has_appointment_list(self):
        self.assertEqual(1, len(self.calendar.appointments))

    def test_calender_creates_appointments_by_day__one_app(self):
        self.assertEqual([{
            'date': datetime.date(2021,3,14),
            'appointments' : [self.appointment1]
        }] ,self.calendar.appointments_by_day())

    def test_calender_creates_appointments_by_day__two_app_diffday(self):
        calendar = Calendar([self.appointment1, self.appointment2])
        self.assertEqual([{
            'date': datetime.date(2021,3,14),
            'appointments' : [self.appointment1]
            },
            {
            'date': datetime.date(2021,4,4),
            'appointments': [self.appointment2]

            }
            ], calendar.appointments_by_day())
    


    def test_calender_creates_appointments_by_day__multi_app_sameday(self):
        calendar = Calendar([self.appointment1, self.appointment2, self.appointment3])
        self.assertEqual([{
            'date': datetime.date(2021,3,14),
            'appointments' : [self.appointment1]
            },
            {
            'date': datetime.date(2021,4,4),
            'appointments': [self.appointment2, self.appointment3]

            }
            ], calendar.appointments_by_day())

    def test_calender_creates_appointments_by_day__order(self):
        calendar = Calendar([self.appointment2, self.appointment3, self.appointment1])
        self.assertEqual([{
            'date': datetime.date(2021,3,14),
            'appointments' : [self.appointment1]
            },
            {
            'date': datetime.date(2021,4,4),
            'appointments': [self.appointment2, self.appointment3]

            }
            ], calendar.appointments_by_day())
    
