"""Library to perform BMI health records calculation"""


class LibBmiHealth:
    """Class library for BMI health records calculation"""
    def __init__(self, logger, common_util_obj: object, data_info: dict):
        self.data_info = data_info
        self._log = logger
        self.common_util_obj = common_util_obj

    def fill_bmi_index(self) -> None:
        """
        Method to fill calculated BMI index of person

        :return: None
        """
        for idx, item in enumerate(self.data_info):
            bmi_idx = self.common_util_obj.bmi_calculator(item['WeightKg'], item['HeightCm'])
            self.data_info[idx].update({'BMIIndex': bmi_idx})

    def fill_bmi_category_and_health_risk(self) -> None:
        """
        Method to fill BMI category and health risk

        :return: None
        """
        for idx, item in enumerate(self.data_info):
            health_dict = self.common_util_obj.bmi_category_and_health_risk(item['BMIIndex'])
            self.data_info[idx].update({'BMICategory': health_dict['bmi_category'],
                                        'HealthRisk': health_dict['health_risk']})

    def calculate_overweight_count(self) -> None:
        """
        Method to calculate overweight persons

        :return: None
        """
        num_of_overweight_persons =  0
        for idx, item in enumerate(self.data_info):
            if item['BMICategory'] == "Overweight":
                num_of_overweight_persons += 1
        self._log.info(f"No. of Overweight Person: {num_of_overweight_persons}")

    def print_results(self) -> None:
        """
        Method to print modified data

        :return:None
        """
        # Printing modified dict:
        for item in self.data_info:
            self._log.info(item)


