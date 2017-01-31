from django.test import TestCase
from models import EducationAward
from django.core.exceptions import ValidationError


# Testing the Education Awards creation:
class EducationAwardTest(TestCase):

    # Test normal award creation:
    def test_valid_entry(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 1250
        ea.full_clean()
        ea.save()
        self.assertTrue(True)

    # Test that a user can enter a small dollar value:
    def test_low_value_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Winter 2016"
        ea.awardAmount = 1
        ea.full_clean()
        ea.save()
        self.assertTrue(True)

    # Test that a user can enter the max dollar value:
    def test_high_value_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Spring 2016"
        ea.awardAmount = 99999
        ea.full_clean()
        ea.save()
        self.assertTrue(True)

    # Test that a decimal value is not allowed:
    def test_invalid_low_value_award(self):
        #with self.assertRaisesRegexp(ValidationError, "Award value must be a whole number (no decimals)."):
            ea = EducationAward()
            ea.description = "SPFA Education Award - Fall 2016"
            ea.awardAmount = 0.01
            ea.full_clean()
            ea.save()

    # Test that an award amount is required:
    def test_award_value_not_blank(self):
        #with self.assertRaisesRegexp(ValidationError, "Award value is required."):
            ea = EducationAward()
            ea.description = "SPFA Education Award - Winter 2017"
            ea.awardAmount = ""
            ea.full_clean()
            ea.save()

    # Test that an award amount cannot be zero:
    def test_award_value_not_zero(self):
        #with self.assertRaisesRegexp(ValidationError, "Amount must be greater than $0 and less than $10,000."):
            ea = EducationAward()
            ea.description = "SPFA Education Award - Spring 2017"
            ea.awardAmount = 0
            ea.full_clean()
            ea.save()

    # Test that an award value cannot exceed 5 digits in length:
    def test_award_value_5_digits(self):
        #with self.assertRaisesRegexp(ValidationError, "Amount must be greater than $0 and less than $10,000."):
            ea = EducationAward()
            ea.description = "SPFA Education Award - Fall 2017"
            ea.awardAmount = 100000
            ea.full_clean()
            ea.save()

    # Test that award description cannot be left blank:
    def test_edu_award_desc_not_blank(self):
       #with self.assertRaisesRegexp(ValidationError, "Award description is required."):
            ea = EducationAward()
            ea.description = ""
            ea.awardAmount = 1250
            ea.full_clean()
            ea.save()

    # Test that award description can be 1 character long:
    def test_edu_award_desc_min(self):
        ea = EducationAward()
        ea.description = ""
        ea.awardAmount = 1250
        ea.full_clean()
        ea.save()
        self.assertTrue(True)

    # Test that award description can reach the max length, 150 characters:
    def test_edu_award_desc_min(self):
        ea = EducationAward()
        ea.description = "This is an award for being just such a smart cookie, like so smart, the smartest cookie there" \
                         " ever was now, all other cookies just seem to pale in comparison to your smart cookie-ness"
        ea.awardAmount = 1250
        ea.full_clean()
        ea.save()
        self.assertTrue(True)

    # Test that award description cannot exceed the max length of 150 characters:
    def test_edu_award_desc_min(self):
        #with self.assertRaisesRegexp(ValidationError, "Award description cannot exceed 150 characters in length."):
            ea = EducationAward()
            ea.description = "This is an award for being just such a smart cookie, like so smart, the smartest cookie" \
                             " there ever was EVER, all other cookies just seem to pale in comparison to your smart " \
                             "cookie-ness"
            ea.awardAmount = 1250
            ea.full_clean()
            ea.save()