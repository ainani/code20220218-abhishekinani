Project tests the BMI Category and Health risks based on BMI index range.
Takes input of json file and calculate
 - BMI Index
 - BMI category
 - Health risk
 
 
 Usage:
  - python code20220218-abhishekinani\tests\test_default_input_file.py
 
Sample Output:
 2022-02-18 16:13:52,364 - INFO - create_logger - Results are saved in C:\Users\ainanix\OneDrive - Intel Corporation\GIT_Repos\BMIPoc\logs
2022-02-18 16:13:52,364 - INFO - main -  ++++++++++ Entry point of test ++++++++++
2022-02-18 16:13:52,364 - INFO - parse_json - Parsing JSON file
2022-02-18 16:13:52,365 - INFO - calculate_overweight_count - No. of Overweight Person: 1
2022-02-18 16:13:52,365 - INFO - print_results - {'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMIIndex': 32.8, 'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}
2022-02-18 16:13:52,365 - INFO - print_results - {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'BMIIndex': 32.8, 'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}
2022-02-18 16:13:52,372 - INFO - print_results - {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'BMIIndex': 23.8, 'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'}
2022-02-18 16:13:52,372 - INFO - print_results - {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'BMIIndex': 22.5, 'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'}
2022-02-18 16:13:52,372 - INFO - print_results - {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70, 'BMIIndex': 31.1, 'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}
2022-02-18 16:13:52,372 - INFO - print_results - {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82, 'BMIIndex': 29.4, 'BMICategory': 'Overweight', 'HealthRisk': 'Enhanced risk'}

