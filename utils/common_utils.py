"""Common utils file that contains most of the common utilities"""
import json


class CommonUtils:
    """
    Class having common utilities for project
    """
    def __init__(self, logger):
        self.bmi_index = 0.0
        self._log = logger

    def parse_json(self, file_path: str) -> list:
        """
        Method to parse json file and read in dict format
        :return: json data in list of dictionary format
        """
        self._log.info("Parsing JSON file")
        with open(file_path, "r") as data_file:
            data = data_file.read()
            json_data = json.loads(data)
        return json_data

    def bmi_calculator(self, mass_in_kg: float = 0.0, height_in_cm: float = 0.0) -> float:
        """
        Method to calculate BMI index

        :param mass_in_kg: Weight of person in Kg
        :param height_in_cm: Height of person in cm
        :return: BMI index in float
        """
        try:
            if not all([height_in_cm > 0, mass_in_kg > 0]):
                self._log.info("Invalid height or mass received")
                return self.bmi_index

            # Converting height in meter
            height_in_meter = height_in_cm / 100

            # BMI calculation formula: BMI(kg/m2) = mass(kg) / height(m)2
            self.bmi_index = round(mass_in_kg / height_in_meter ** 2, 1)

            return self.bmi_index
        except Exception as e:
            self._log.error(f"Exception occurred as [ {e} ]")

    def bmi_category_and_health_risk(self, bmi_index: float = None) -> dict:
        """
        Method to calculate BMI category and health risk based on BMI index
        :return: dict {'bmi_category', 'health_risk'}

        # referenced data:
        ---------------------------------------------------------------
        |BMI Category        | BMI Range (kg/m2) | Health risk        |
        ---------------------------------------------------------------
        |Underweight         | 18.4 and below    | Malnutrition risk  |
        |Normal weight       | 18.5 - 24.9       | Low risk           |
        |Overweight          | 25 - 29.9         | Enhanced risk      |
        |Moderately obese    | 30 - 34.9         | Medium risk        |
        |Severely obese      | 35 - 39.9         | High risk          |
        |Very severely obese | 40 and above      | Very high risk     |
        ---------------------------------------------------------------
        """
        result_dict = {'bmi_category': None,
                       'health_risk': None}
        if bmi_index is None:
            bmi_index = self.bmi_index

        if bmi_index > 0:
            if bmi_index <= 18.4:
                result_dict.update({'bmi_category': 'Underweight',
                                    'health_risk': 'Malnutrition risk'})
            elif 18.5 <= bmi_index <= 24.9:
                result_dict.update({'bmi_category': 'Normal weight',
                                    'health_risk': 'Low risk'})
            elif 25 <= bmi_index <= 29.9:
                result_dict.update({'bmi_category': 'Overweight',
                                    'health_risk': 'Enhanced risk'})
            elif 30 <= bmi_index <= 34.9:
                result_dict.update({'bmi_category': 'Moderately obese',
                                    'health_risk': 'Medium risk'})
            elif 35 <= bmi_index <= 39.9:
                result_dict.update({'bmi_category': 'Severely obese',
                                    'health_risk': 'High risk'})
            else:
                result_dict.update({'bmi_category': 'Very Serverly obese',
                                    'health_risk': 'Very high risk'})
        else:
            self._log.error(f"Invalid BMI index received: {bmi_index}")
        return result_dict
