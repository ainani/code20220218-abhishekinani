"""Base class for all tests to drive test logic"""
import utils
from utils.log_utils import Logger
from utils.common_utils import CommonUtils


class TestLogic:
    """
    Main driving class to test the logic
    """
    def __init__(self):
        # Create common logger object
        self.log = Logger.create_logger()

        # Create common_utils object
        self.common_util_obj = CommonUtils(self.log)

        self.data_list = None

    def parse_json(self, json_file=utils.DEFAULT_INPUT_FILE) -> None:
        """
        Method to parse the json file

        :param: json_file: JSON input file to parse. Default to project json file
        :return: None
        """
        self.data_list = self.common_util_obj.parse_json(json_file)

    def main(self) -> None:
        """
        Main method to drive the test
        :return: None
        """
        self.log.info(f" {'+' * 10} Entry point of test {'+' * 10}")

        # Do pre test
        self.do_pre_test()

        # Do test
        self.do_test()

        # Do post test
        self.do_post_test()
