# Allure Report Consolidator
## Steps to install (for both Win and Mac)
1. Install SVN client with Command Line Tools
1. Install the latest version of Python
1. Install the latest version of `pip`
1. Install the `svn` package using `pip`

   `pip install svn`

   If you are using mAc and have installed Python3 using HomeBrew, then you may lack permissions to run the `pip` command. In such cases, use this commnd to install any pip package:
   
   `sudo -H \usr\local\bin\pip3 install svn`

## Using the tool
1. Checkout the git project and run the command:

   `python runTest.py --help`
   
   ..to see the different options which could be used in the command line.
1. Use the `--list` option to list out the acceptance projects which you would want to select and run the tests for.
1. An example of running the sss category for the apm and cwf projects would be:

`python runTest.py --select apm-acceptance --select audit-advisor-acceptance --category AWSQASmokeTest`
