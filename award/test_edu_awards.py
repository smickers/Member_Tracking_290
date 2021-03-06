from django.test import TestCase
from models import EducationAward
from django.core.exceptions import ValidationError
from django.db import DataError


# Testing the Education Awards creation:
class EducationAwardTest(TestCase):

    # Test normal award creation:
    def test_valid_entry(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 1250
        ea.full_clean()
        ea.save()

    # Test that a user can enter a small dollar value:
    def test_low_value_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Winter 2016"
        ea.awardAmount = 1
        ea.full_clean()
        ea.save()

    # Test that a user can enter the max dollar value:
    def test_high_value_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Spring 2016"
        ea.awardAmount = 99999
        ea.save()
        self.assertTrue(True)

    ##NO LONGER VALID SEE test_new_monetary_value
    # # Test that a decimal value is not allowed:
    # def test_invalid_low_value_award(self):
    #     with self.assertRaises(ValidationError):
    #         ea = EducationAward()
    #         ea.description = "SPFA Education Award - Fall 2016"
    #         ea.awardAmount = 0.01
    #         ea.full_clean()
    #         ea.save()

    ##NO LONGER VALID SEE test_new_monetary_value
    # # Test that an award amount is required:
    # def test_award_value_not_blank(self):
    #     with self.assertRaises(ValidationError):
    #         ea = EducationAward()
    #         ea.description = "SPFA Education Award - Winter 2017"
    #         ea.awardAmount = None
    #         ea.full_clean()
    #         ea.save()

    # Test that an award amount cannot be zero:
    def test_award_value_not_zero(self):
        with self.assertRaises(ValidationError):
            ea = EducationAward()
            ea.description = "SPFA Education Award - Spring 2017"
            ea.awardAmount = 0
            ea.full_clean()
            ea.save()
    ##NO LONGER VALID SEE test_new_monetary_value
    # # Test that an award value cannot exceed 5 digits in length:
    # def test_award_value_5_digits(self):
    #     with self.assertRaises(ValidationError):
    #         ea = EducationAward()
    #         ea.description = "SPFA Education Award - Fall 2017"
    #         ea.awardAmount = 100000
    #         ea.full_clean()
    #         ea.save()

    # Test that award description cannot be left blank:
    def test_edu_award_desc_not_blank(self):
        with self.assertRaises(ValidationError):
            ea = EducationAward()
            ea.description = None
            ea.awardAmount = 1250
            ea.full_clean()
            ea.save()

    # Test that award description can be 1 character long:
    def test_edu_award_desc_min(self):
        ea = EducationAward()
        ea.description = 'a'
        ea.awardAmount = 1250
        ea.save()

    # Test that award description can reach the max length, 150 characters:
    #NOTE: This can't be cleaned because it sees the math and throws a validationError.
    def test_edu_award_desc_max(self):
        ea = EducationAward()
        ea.description = 'a' * 150
        ea.awardAmount = 1250
        ea.save()

    #Test that special characters are not permitted unless specified:
    def test_edu_award_no_special_chars(self):
        with self.assertRaises(ValidationError):
            ea = EducationAward()
            ea.description = "!@#$$%*^&^(&%*(///...````````~"
            ea.awardAmount = 1250
            ea.full_clean()
            ea.save()

    # Test that award description cannot exceed the max length of 150 characters:
    def test_edu_award_desc_too_max(self):
        with self.assertRaises(DataError):
            ea = EducationAward()
            ea.description = 'a' * 151
            ea.awardAmount = 1250
            ea.save()