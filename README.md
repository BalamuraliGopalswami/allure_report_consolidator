# Allure Report Consolidator
## Steps to install (for both Win and Mac)
1. Install Git for windows along with Git Bash.
1. Install SVN client with Command Line Tools
   This can be done by selecting the "command line tools" install options while installing the TortoiseSVN client as shown below
   
   
   ![alt text](https://github.com/sridharaiyer/allure_report_consolidator/blob/master/images/svn/command_line_tool.png "command_line_tool")

   Once installed, open your Git Bash prompt or DOS Command Line prompt and type `svn --version`
   You should see a message similar to this on Windows:
   
   ```
   svn --version
   svn, version 1.9.5 (r1770682)
   compiled Nov 26 2016, 14:22:31 on x86-microsoft-windows

   Copyright (C) 2016 The Apache Software Foundation.
   This software consists of contributions made by many people;
   see the NOTICE file for more information.
   Subversion is open source software, see http://subversion.apache.org/

   The following repository access (RA) modules are available:

   * ra_svn : Module for accessing a repository using the svn network protocol.
     - with Cyrus SASL authentication
     - handles 'svn' scheme
   * ra_local : Module for accessing a repository on local disk.
     - handles 'file' scheme
   * ra_serf : Module for accessing a repository via WebDAV protocol using serf.
     - using serf 1.3.9 (compiled with 1.3.9)
     - handles 'http' scheme
     - handles 'https' scheme

   The following authentication credential caches are available:

   * Wincrypt cache in C:\Users\pceqa\AppData\Roaming\Subversion
   ```
   
1. Install the latest version of Python
1. Install the latest version of `pip`
1. Install the `svn` package using `pip`

   `pip install svn`

   If you are using mAc and have installed Python3 using HomeBrew, then you may lack permissions to run the `pip` command. In such cases, use this commnd to install any pip package:
   
   `sudo -H \usr\local\bin\pip3 install svn`
   
   If you had used Homebrew to install software in Mac, then you can use this command to grant you access to all the packagaes installed by Homerew:
   
   `sudo chown $(whoami):admin /usr/local && sudo chown -R $(whoami):admin /usr/local`

## Using the tool
1. Checkout the git project and run the command:

   `python runTest.py --help`
   
   ..to see the different options which could be used in the command line.
1. Use the `--list` option to list out the acceptance projects which you would want to select and run the tests for.
1. An example of running the POCSmokeTest category for the base-project and sample-project acceptance projects would be:

`python runTest.py --select base-project-acceptance/ --select sample-project-acceptance/ --category POCSmokeTest`
