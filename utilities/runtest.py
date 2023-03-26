import os

from utilities.run_configuration import *

command = f"pytest ../tests/ --browser_name={browser_name} --env_name={env} --h={headless_mode} --html=../output/reports" \
          f"/{test_type}_report.html -v --junitxml=../output/reports/report.xml"

os.system(command)