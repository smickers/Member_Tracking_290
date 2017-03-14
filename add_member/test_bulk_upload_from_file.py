from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_member.models import Person

# region Tests for Creating a person
class PersonUploadTestCase(TestCase):
    """Test multiple users can be uploaded from an excel file"""

    def setUp(self):
        """Setup method to initialize essential Objects"""

    '''
    Name:       test_user_can_upload_excel_file
    Function:   Test user is able to upload an excel file (.xlsx)
    '''
    def test_user_can_upload_excel_file(self):
        pass

    '''
    Name:       test_user_cannot_upload_other_file_formats
    Function:   Test user is not able to upload any other file format
    '''
    def test_user_cannot_upload_other_file_formats(self):
        pass

    '''
    Name:       test_user_sees_preview_table_with_member_information
    Function:   Test user is shown a preview table with member information after
                they upload an excel file
    '''
    def test_user_sees_preview_table_with_member_information(self):
        pass

    '''
    Name:       test_preview_table_displays_all_member_information
    Function:   Test preview table displays all member information that came
                from the excel file
    '''
    def test_preview_table_displays_all_member_information(self):
        pass

    '''
    Name:       test_user_cannot_upload_files_greater_than_500mb
    Function:   Test user cannot upload files that are greater than 500mb
    '''
    def test_user_cannot_upload_files_greater_than_500mb(self):
        pass

    '''
    Name:       test_preview_table_is_not_shown_if_excel_file_is_empty
    Function:   Test that member info preview table is not shown if uploaded excel file is empty
    '''
    def test_preview_table_is_not_shown_if_excel_file_is_empty(self):
        pass

    '''
    Name:       test_members_are_created_if_non_required_fields_are_missing_in_file
    Function:   Test members are created and inputted into database if excel file has missing member info
                (ex: no address, no phone number) etc
    '''
    def test_members_are_created_if_non_required_fields_are_missing_in_file(self):
        pass

    '''
    Name:       test_members_are_not_created_if_file_is_invalid_format
    Function:   Test members are not created and not inputted into database if file is invalid format
                (ex: file has improper headers: no header for address, sin, ID, etc)
    '''
    def test_members_are_not_created_if_file_is_invalid_format(self):
        pass
