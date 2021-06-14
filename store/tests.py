from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product



class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Apollo', slug='Apollo')


    def test_category_model_entry(self):

        data= self.data1
        self.assertEqual(str(data), 'Apollo')

class TestCategoriesModelDois(TestCase):

    def setUp(self):
        Category.objects.create(name='Apollo', slug='Apollo')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1,title='Apollo gato',created_by_id=1,slug='Apollo-gato',price='20.00',image='Apollo')


    def test_category_model_entry(self):

        data= self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Apollo gato')
