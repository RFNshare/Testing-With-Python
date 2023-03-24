# Web-Automation-With-Python

A place for me to write down all of the little things I learn every day. This serves largely as a way for me to remember
little things I'd otherwise have to keep looking up.

Many of these will be technical. Many of these will not.

Behold my periodic learnings, and judge me for my ignorance.

## Tech and Team

"Worky" things. Mostly (or entirely) technical related to Web Automation with python selenium learnings.

### Python Basic

* Basics of python language.
* Datatypes & Variables
* Flow Control & OOP
* Read & Write
* Exception Handling Mechanism

### Web Automation Basic

* Usage of Python selenium library.
* Execute Script Into Different Browser (Chrome, Firefox, Edge).
* Explore Selenium Locators (XPATH, CSS, ID, Name, ClassName, LinkText/Partial LinkText).
* Static Drop Using Select Class For Select Tag(By Index, By Visible Text, By Value).
* Handle Dynamic Dropdown Using Loop & Elements.
* Fetch Text & Attribute Value For Assertion.
* Handle Dynamic Checkbox(By Loop, By Index) & Validate.
* Assert is_selected, is_displayed.
* Handling Alerts(Switch Alert Mode, Accept/Dismiss, Grab Text).
* Explicit & Implicit Wait(Using WebDriverWait For Explicit Wait).
* Chaining Web Element.
* Functional Testing with GREEN-KART Site(Add To Cart, Validate Sum & Discount, Matching Prod Names List)
* Actions (Click & Hold, Contex CLick, Double Click, Long-press, Drag & Drop, Hover) Using ActionChains.
* Handling Windows(Switch/Back Window Mode To Child/Parent By Index).
* Functional Testing with login-pagePractise Site(Parent/ChildWindow Handle, Email Extract, Explicit Wait & Assert).
* iFrame Handle, switch to frame. Go to default mode.
* Execute JavaScript, Added Chrome Argument(headless, handle ssl certificate etc.).
* Table Sorting & Validation, Chrome Options Details Explore.
* E2E Functional Testing (AngularPractice Shop)[Execute With All Topics Included].

## Selenium Python Framework Design Plan

* Pytest Unit Testing Framework
  * Basic Pytest
    * pytest file should start with test_ or end with _test.
    * pytest method names should start with test & any code wrapped in method only. Every method behave like one test case.
    * run ``py.test -v -s`` to run all test cases in a directory. v=verbose, s=console log.
    * run ``py.test -v -s test_file_name.py`` to run specific file.
    * run ``py.test -v -s -k method_partial_name`` to run module based on module name regex match.
    * run ``py.test -v -s -m smoke`` to run module based on pytest mark(tag) in pytest.ini file.
    * combine run `py.test -v -s -k card -m smoke` based on module partial name with mark(tag).
    * silent run `pytest -q`
    * use `@pytest.mark.skip` to skip a test case module.
    * use `@pytest.mark.xfail` to skip report but method will be executed.
  * Pytest Fixtures 
    * use `@pytest.fixture()` mark to set up pre-requisite method `setup` to run before execute the test cases.
    * use `yield` in setup method to teardown/cleanup after execute all test cases.
    * use method name (setup) into test method parameter will execute fixture.
    * use `conftest` to generalize fixture for every pytest test file in a directory.
    * use `@pytest.mark.usefixtures("setup")` into TestClass for use fixture to all test methods in a class.
    * Scope: can be sharing fixtures across classes, modules, packages or session
    * use `@pytest.fixture(scope="class")` for Onetime Setup & Teardown into TestClass where group of testcases contains.
    * Data driven fixtures to load data into tests. Use fixture data into testcases(drivers, data's)
    * return fixture data with yield like this `yield your_data`
    * cross browser testing using `@pytest.fixture(params=["chrome", "firefox", "edge"])`
    * send fixture multiple data one single run like this `@pytest.fixture(params=[("chrome", "raju", "pass"), "firefox", "edge"])`. Parameterized with multiple value.
    * command line arguments (pending)
* Understand Logging and HTML Reports
  * To generate html report use `pytest -q --html=regression_report.html`. If you need with filter then ` pytest -q -m smoke --html=smoke_report.html`
  * Generate including CSS in same file `pytest --html=report.html --self-contained-html`
  * using `logging` module & conf file to create a log file and insert `debug, info, error, warning, critical` log.
  * connecting those log into html report by using log in test method.
* Implement Selenium Python Framework (PageObject DesignPattern)
  * 
* Integrating Framework to Jenkins and setup job parameters
* Data Driven Framework with Excel to Selenium Python Tests

### Miscellaneous

* GIT Version Control