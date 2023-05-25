# brsrstck

A test of browserstack using pytest. This is derived from [Browserstack's Pytest Demo](https://github.com/browserstack/pytest-browserstack)

## Prerequisites

* Python3 with Pip and venv

## Setup

* Clone the repo with `git clone -b sdk https://github.com/kentonself/brsrstck.git`
* It is recommended to use a virtual environment to install dependencies. To create a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate # on Mac or Linux
  env\Scripts\activate # on Windows
  ```
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by providing your username and access key in the `browserstack.yml` configuration file, or by setting the `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` environment variables. Additionally the user login and password for automate.browserstack.com are kept in `BSTACK_USER`  and `BSTACK_PASSWORD`

## Run in parallel:
* To run the test in the configuration file run:
```
  browserstack-sdk pytest -s tests/test.py
```


## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
