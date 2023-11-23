from django.test import TestCase
from super_teacher.models import Service

class ServiceTests(TestCase):
    def test_create_service(self):
        service = Service(subject="English", description="English course for students...", price=123)
        service.save()

        self.assertEqual(Service.objects.count(), 1)
        self.assertEqual(service.subject, "English")
        self.assertEqual(service.description, "English course for students...")
        self.assertEqual(service.price, 123)

    def test_service_str(self):
        service = Service(subject="English", description="English course for students...", price=123)
        service.save()

        self.assertEqual(service.__str__(), "English")
