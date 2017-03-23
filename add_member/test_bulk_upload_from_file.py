from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_member.models import Person, PersonFile
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from spfa_mt import settings
from django.core.files import File
from rest_framework.test import APIClient
import json



# region Tests for Creating a person
class PersonUploadTestCase(TestCase):
    """Test multiple users can be uploaded from an excel file"""

    def __init__(self, *args, **kwargs):
        super(PersonUploadTestCase, self).__init__(*args, **kwargs)
        self.factory = APIRequestFactory()
        self.CONST_FILE_PATH = settings.STATIC_ROOT + 'add_member/%s'
        self.test_xlsx = self.CONST_FILE_PATH % 'member_upload.xlsx'
        self.invalid_file = self.CONST_FILE_PATH % 'member_upload_invalid_file.jpeg'
        self.path_largefile = self.CONST_FILE_PATH % 'dummylarge.xlsx'
        self.path_emptyfile = self.CONST_FILE_PATH \
                              % 'empty.xlsx'
        self.json_test_file = self.CONST_FILE_PATH % 'json_test.json'


    def setUp(self):
        """Setup method to initialize essential Objects"""
        f = open(self.path_largefile, "wb")
        f.seek(settings.MAX_FILE_SIZE+1)
        f.write("\0")
        f.close()

        f = open(self.path_emptyfile, "wb")
        f.write("")
        f.close()
    #
    # '''
    # Name:       test_user_can_upload_excel_file
    # Function:   Test user is able to upload an excel file (.xlsx)
    # '''
    # def test_user_can_upload_excel_file(self):
    #     fp = open(self.test_xlsx, "rb")
    #     xlsx_file = File(fp)
    #
    #     factory = APIClient()
    #
    #     f_request = factory.post(reverse('add_member:excel-upload'), {'file': xlsx_file})
    #     f_data = f_request.data['id']
    #     person = PersonFile.objects.get(pk=f_data)
    #
    #     self.assertTrue(isinstance(person, PersonFile))
    #
    #
    #
    #
    # '''
    # Name:       test_user_cannot_upload_other_file_formats
    # Function:   Test user is not able to upload any other file format
    # '''
    # def test_user_cannot_upload_other_file_formats(self):
    #     fp = open(self.invalid_file, "rb")
    #     invalid_file = File(fp)
    #     factory = APIClient()
    #     f_request = factory.post(reverse('add_member:excel-upload'), {'file': invalid_file})
    #     self.assertEqual( json.loads(f_request.content), {'detail': 'The file is an invalid format.'
    #                                                                 ' Please supply a valid excel sheet.'} )


    '''
    Name:       test_user_sees_preview_table_with_member_information
    Function:   Test user is shown a preview table with member information after
                they upload an excel file
    '''
    def test_user_sees_preview_table_with_member_information(self):
        fp = open(self.test_xlsx, "rb")
        xlsx_file = File(fp)

        factory = APIClient()

        f_request = factory.post(reverse('add_member:excel-upload'), {'file': xlsx_file})
        f_data = f_request.data['id']
        f_request = factory.get(reverse('add_member:excel-to-json', args=[f_data,]))
        fp.close()
        fp = open(self.json_test_file, "r")
        json_data = fp.read()
        self.assertEqual(f_request.content, json_data)

    # '''
    # Name:       test_preview_table_displays_all_member_information
    # Function:   Test preview table displays all member information that came
    #             from the excel file
    # '''
    # def test_preview_table_displays_all_member_information(self):
    #     """
    #         1. Upload the xlsx file to the endpoint url
    #         2. Parse the request to json
    #         3. Send the primary key of the uploaded xlsx file to the xlsx-to-json endpoint
    #         4. Parse the request response to json
    #         5. Verify if the json response can be represented as a table.
    #     """
    #     pass

    '''
    Name:       test_user_cannot_upload_files_greater_than_500mb
    Function:   Test user cannot upload files that are greater than 500mb
    '''
    def test_user_cannot_upload_files_greater_than_500mb(self):
        fp = open(self.path_largefile, "rb")
        very_large = File(fp)

        factory = APIClient()
        f_request = factory.post(reverse('add_member:excel-upload'), {'file': very_large})
        self.assertEqual( json.loads(f_request.content), {'detail': 'The file is an invalid format.'
                                                                        ' Please supply a valid excel sheet.'} )
    #
    # '''
    # Name:       test_preview_table_is_not_shown_if_excel_file_is_empty
    # Function:   Test that member info preview table is not shown if uploaded excel file is empty
    # '''
    # def test_preview_table_is_not_shown_if_excel_file_is_empty(self):
    #     fp = open(self.path_emptyfile, "r")
    #     empty_file = File(fp)
    #
    #     request = self.factory.post('{{endpoint_url}}', {'file': empty_file}, format='json')
    #     self.assertTrue(request.status_code == 400)  # Bad request
    #
    # '''
    # Name:       test_members_are_created_if_non_required_fields_are_missing_in_file
    # Function:   Test members are created and inputted into database if excel file has missing member info
    #             (ex: no address, no phone number) etc
    # '''
    # def test_members_are_created_if_non_required_fields_are_missing_in_file(self):
    #     """
    #         1. Upload the xlsx file to the endpoint url
    #         2. Parse the request to json
    #         3. Send the primary key of the uploaded xlsx file to the xlsx-to-json endpoint
    #         4. Parse the request response to json
    #         5. Verify if the json response can be represented as a table.
    #         6. Check to see if the list of members included witht he xlsx file now exists on the DB
    #     """
    #     pass
    #
    # '''
    # Name:       test_members_are_not_created_if_file_is_invalid_format
    # Function:   Test members are not created and not inputted into database if file is invalid format
    #             (ex: file has improper headers: no header for address, sin, ID, etc)
    # '''
    # def test_members_are_not_created_if_file_is_invalid_format(self):
    #     """
    #         1. Upload the xlsx file to the endpoint url
    #         2. Parse the request to json
    #         3. Send the primary key of the uploaded xlsx file to the xlsx-to-json endpoint
    #         4. Parse the request response to json
    #         5. Check if json response contains an error attribute
    #     """
    #     pass
