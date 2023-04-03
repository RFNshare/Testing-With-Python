import imaplib
import re
import glob
import os
from datetime import datetime


# Read current date
def read_date():
    return str(datetime.today().strftime("%Y-%m-%d"))


# function to read current date and time
def read_datetime():
    return str(datetime.today().strftime("%Y-%m-%d-%H-%M-%S"))


# function to read raw time
def get_raw_time():
    return str(datetime.today().strftime("%Y%d%H%M%S"))


def read_time():
    return str(datetime.today().strftime("%I-%M-%S-%p"))


def get_html_reports(report_type):
    reports = []
    if not report_type == "both":
        try:
            report = os.path.abspath(
                glob.glob(f"../output/reports/{report_type}_*.html")[-1]
            )
            reports.append(report)
        except Exception as e:
            print("Report not ready, Error", e)
    else:
        try:
            report1 = os.path.abspath(glob.glob(f"reports/api_report_html/*.html")[-1])
            report2 = os.path.abspath(glob.glob(f"reports/ui_report_html/*.html")[-1])
            # logs = os.path.abspath(glob.glob("logs/*.log")) # get logs
            reports.append(report1)
            reports.append(report2)
        except Exception as e:
            print("Reports are not ready, Error", e)
    return reports


# function to read last email message
def get_otp_from_email(email_credentials=None):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(email_credentials["email"], email_credentials["password"])
    mail.select("INBOX")
    result, data = mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    re_match = re.search(r"Your OTP is (\d{6})", str(raw_email))
    otp = re_match.groups()[0]
    return otp
