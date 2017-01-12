from django.test import TestCase

class GrievanceFile_UploadTest(TestCase):
    def setUp(self):
        pass

    def test_user_can_upload_single_grievance_document(self):
        """
        Test if a user can associate a single document to a grievance ruling
        :return: None
        """
        pass

    def test_user_can_upload_multiple_grievance_docs(self):
        """
        Test if user can associate multiple documents to a grievance  ruling
        :return: None
        """
        pass

    def test_user_uploaded_document_is_in_the_correct_path_in_the_server(self):
        """
        Test if user’s uploaded file exists in the server
        :return: None
        """
        pass

    def test_user_can_upload_if_the_total_file_size_is_less_than_500MB(self):
        """
        Test if users’s uploaded file is less than 500MB
        :return: None
        """
        pass


    def test_user_cannot_upload_if_the_total_file_size_is_greater_than_500MB(self):
        """
        Test if users’s uploaded file is less than 500MB
        :return: None
        """
        pass

    def test_user_can_only_upload_files_with_valid_extension(self):
        """
        Test if user’s uploaded file only has the following extension:
        .docx, .pptx, .xlsx, .csv, .pdf, .txt and .msg
        :return: None
        """
        pass

    def test_db_tracks_the_file_upload_date(self):
        """
        Test if the database tracks the date when the file is uploaded.
        It must be in the format of DD/MM/YYYY
        :return: None
        """
        pass

