import utils
from test_logic import TestLogic
from lib.lib_bmi_health import LibBmiHealth


class TestDefaultInput(TestLogic):
    """Test class to check default input file."""
    def __init__(self):
        super(TestDefaultInput, self).__init__()
        self.bmi_lib_obj = None

    def do_pre_test(self) -> None:
        """
        Method to do any pre test activities

        :return: None
        """
        # Parse json file
        self.parse_json(json_file=utils.DEFAULT_INPUT_FILE)

        # Creating BMI Library object
        self.bmi_lib_obj = LibBmiHealth(self.log, self.common_util_obj, self.data_list)

    def do_test(self) -> None:
        """
        Method to execute test case

        :return: None
        """
        # Fill BMI index in dict
        self.bmi_lib_obj.fill_bmi_index()

        # Fill BMI category and health risk in dict
        self.bmi_lib_obj.fill_bmi_category_and_health_risk()

        # Calculate no. of overweight persons
        self.bmi_lib_obj.calculate_overweight_count()

    def do_post_test(self) -> None:
        """
        Method to process and post test activity

        :return: None
        """
        # Print modified data
        self.bmi_lib_obj.print_results()


if __name__ == "__main__":
    obj = TestDefaultInput()
    obj.main()
