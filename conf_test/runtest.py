import os
import subprocess
import sys
from conf_test.general_functions import *

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utilities.excel_utils import *
from conf_test.send_email import send_report
from conf_test.run_configuration import *

configuration_data = read_configuration_data_from_excel("../testData/test_data.xlsx")
parallel = configuration_data["parallel_run"]
test_item = configuration_data["test_item"].casefold()
type = test_type + "_" + test_item
ui_report_file_name_prefix = (
    f"{'ui' if test_item == 'both' else test_item}_{read_date()}_{read_time()}"
)
command = (
    f"pytest ../tests/ --html=../output/reports/{test_type}_{ui_report_file_name_prefix}_report.html -v "
    f"--junitxml=../output/reports/{test_type}_{ui_report_file_name_prefix}_report.xml"
    f"-s --alluredir=../output/allure_reports/{ui_report_file_name_prefix}"
)


def individual_ui_testcases_run():
    """
    Run the test cases based on the test item sequentially
    :return:
    """
    subprocess.run(command, shell=True)


# decide which mode to run the test cases
if parallel == "no" and test_item == "ui":
    individual_ui_testcases_run()

# send report if generated
html_reports = get_html_reports(type)

# send report to receivers email
project_name = configuration_data["project_name"]
report_receiver_email = configuration_data["report_receiver"]
# send_report(report_receiver_email, html_reports, project_name)

# allure report serve
ui_allure_serve_command = (
    f"allure serve ../output/allure_reports/{ui_report_file_name_prefix}"
)

if test_item == "ui":
    subprocess.run(ui_allure_serve_command, shell=True)
