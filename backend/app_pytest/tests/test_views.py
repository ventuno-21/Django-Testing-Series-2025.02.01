from django.test import TestCase, Client
from django.urls import reverse
import json
from app_pytest.models import Company
import pytest_django
import pytest


class BasicCompanyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Because we use viewset and routers to get list of items in testing should do as below:
        # Get all data = {basename}-list
        router_basename = "companies"
        self.companies_url = reverse(f"app_pytest:{router_basename}-list")


# @pytest.mark.django_db
class TestGetCompanies(BasicCompanyAPITestCase):

    def test_zero_companies_should_return_empty_list(self):
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_suceed(self):
        ventuno = Company.objects.create(name="Ventuno")
        response = self.client.get(self.companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), "Ventuno")
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")


class TestPostCompany(BasicCompanyAPITestCase):
    def test_create_company_without_arguments_which_should_fail(self):
        response = self.client.post(path=self.companies_url)
        self.assertEqual(response.status_code, 400)
        # "This field is required." => is an error that will be shown by django if we dont fill required fields
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_create_existing_company_which_should_fail(self):
        Company.objects.create(name="google")
        response = self.client.post(path=self.companies_url, data={"name": "google"})
        self.assertEqual(response.status_code, 400)
        # "company with this name already exists.." => is an error that will be shown by django if we send a same data for unique fields
        self.assertEqual(
            json.loads(response.content),
            {"name": ["company with this name already exists."]},
        )

    def test_create_company_with_only_name_all_fields_should_be_default(self):
        response = self.client.post(path=self.companies_url, data={"name": "apple"})
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("name"), "apple")
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

    def test_create_company_with_layoffs_should_be_successfull(self):
        response = self.client.post(
            path=self.companies_url, data={"name": "celery", "status": "Layoffs"}
        )
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("name"), "celery")
        self.assertEqual(response_content.get("status"), "Layoffs")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

    def test_create_company_with_wrong_status_should_fail(self):
        response = self.client.post(
            path=self.companies_url, data={"name": "celery", "status": "wongstatus"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("wongstatus", str(response.content))
        self.assertIn("is not a valid choice", str(response.content))

    # these below two methodds will be fails ifwe test them with out pytest in terminal
    @pytest.mark.xfail
    def test_should_be_ok_if_fails(self):
        self.assertEqual(1, 2)

    @pytest.mark.skip
    def test_should_be_skipped(self):
        self.assertEqual(1, 2)
