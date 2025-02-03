from rest_framework import serializers
from app_pytest.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "status",
            "last_update",
            "application_link",
            "notes",
        ]
