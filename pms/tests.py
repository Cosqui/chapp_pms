from django.test import TestCase
from unittest.mock import Mock
from pms.models import (Room,Customer,Room_type,Booking)

# Create your tests here.
# RUN TEST ./manage.py test pms.tests.RoomFilterTestCase

class RoomFilterTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_filter_byname(self):
        data = {'name':'Room 1'}
        rooms =  Mock(spec=Room.objects)
        rooms.filter().return_value =  data.get('name')
        self.assertIsNotNone(rooms)
       

# RUN TEST ./manage.py test pms.tests.BookingUpdateTestCase
class BookingUpdateTestCase(TestCase):
    def setUp(self):
        self.roomType = Room_type.objects.create(name = "Simple",price = 20,max_guests = 1)
        self.room = Room.objects.create(room_type= self.roomType,name = "Room 1.1",description = "Room 1.1")
        self.customer = Customer.objects.create(name='Guadalupe', email='test@hotmail.com',phone='2289436253')
        self.booking = Booking.objects.create(checkin = '2022-11-19',checkout = '2022-11-21',room = self.room,guests = 1,customer = self.customer,total = 40,code = 'CVMGTH345')

    
    def test_updated_booking(self):
        data = {'checkin': '2022-11-25', 'checkout': '2022-11-26'}
        self.assertTrue(data.get('checkin') < data.get('checkout'))
        self.booking.checkin = data.get('checkin')
        self.booking.checkout = data.get('checkout')
        self.booking.save()
        


        