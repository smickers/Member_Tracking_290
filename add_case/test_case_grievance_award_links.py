from django.test import TestCase


class CaseLinksToGrievanceAwards(TestCase):
    """
    Purpose: Test the connection between grievance award its case
    """

    def setUp(self):
        """
        Setup method to initialize essential Objects
        :return: None
        """
        """
        TODO: modify Case to have its case type to be an Integer. This enables us to use conditional statements
        based on the case type's numerical value.
        For example:
            GRIEVANCE AWARD case types should be mapped to value greater than 3
            and other case types less than 3
            amazing right? Not really, because now we are going to modify every single test case that uses
            the Case class. YAYYYYYYYYYkillmeYAYYYYY
        """
        pass


    def test_grievance_award_can_be_associated_with_a_single_member_if_grievance_award_type_is_of_member(self):
        """
        Purpose: test to see if grievance award can only be associated with a single member if it is of type
        member
        :return:
        """
        pass

    def test_grievance__award_cannot_be_associated_with_a_single_member_if_grievance_award_type_is_not_of_member(self):
        """
        Purpose: test to see if grievance award can only be associated with a single member if it is of type
        member
        :return:
        """
        pass

    def test_grievance_award_can_be_associated_with_multiple_member_if_grievance_award_type_is_of_policy(self):
        """
        Purpose: test to see if grievance award can only be associated with a multiple member if it is of type
        policy
        :return:
        """
        pass

    def test_grievance_award_cannot_be_associated_with_multiple_members_if_griev_aw_type_isnt_of_policy(self):
        """
        Purpose: test to see if grievance award can only be associated with a multiple member if it is of type
        policy
        :return:
        """
        pass

    def test_gr_aw_recipient_is_equal_to_the_union_of_primary_complainant_and_additional_member_of_cases(self):
        """
        Assumption: The case in this test is of type policy
        :return:
        """
        pass


    def test_gr_aw_recipient_is_equal_to_the_primary_complainant_of_the_case(self):
        """
        Assumption: The case in this test is of type member
        :return:
        """
        pass

    def test_case_eval_cases_types_returns_the_instance_of_the_case_type_it_is_related_to(self):
        """

        :return:
        """
        pass

    def test_case_cannot_exists_without_the_case_type_being_specified(self):
        """

        :return:
        """
        pass