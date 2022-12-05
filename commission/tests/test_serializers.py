from django.test import TestCase
from commission.models import Commission
from commission.serializers import CommissionSerializer


class CommissionSerializerTestCase(TestCase):

    def setUp(self):
        self.commission = Commission(
            week_day=1,
            commission_min=100,
            commission_max=1000,
        )

        self.serializer = CommissionSerializer(instance=self.commission)

    def test_to_verify_fields_serialization(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys(
        )), set(['id', 'week_day', 'commission_min', 'commission_max', 'created_at', 'updated_at']))

    def test_to_verify_fields_serialization_values(self):
        data = self.serializer.data
        self.assertEqual(data['week_day'], self.commission.week_day)
        self.assertEqual(data['commission_min'],
                         self.commission.commission_min)
        self.assertEqual(data['commission_max'],
                         self.commission.commission_max)
        self.assertEqual(data['created_at'], self.commission.created_at)
        self.assertEqual(data['updated_at'], self.commission.updated_at)
