from django.test import TestCase

from unittest.mock import Mock
from pms.models import Room

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


        

