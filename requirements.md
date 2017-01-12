# Allure Report Consolidator - Requirements
## Problem statement - Checkout acceptance projects locally from SVN, run tests in different categories and send the consolidated results from the modules to 1 central VM and run the stand-alone Allure report generator on that central VM and host the consolidated results.
### SVN
1. Should be able to connect to the SVN repo - http://svn.proddev.cccis.com:8090/svn/QA/trunk/acceptance-projects/
1. The user should be able to list the acceptance modules from the repository to choose from and run.
1. The projects should be checked out in the user.home/workspace directory in both Win and Mac.
1. If the project was already checked out, then selecting the same for the current execution should update the project to the latest revision from SVN and then execute the tests.


### Maven
1. The tool should run the selected projects as a maven build along with the supplied category.
1. The tool should generate the allure-results by supplying the allure maven goal by default.
1. All the projects should have the maven copy resources plug-in in them and configured to copy the allure results to the user.home/allure-results/release directory, where the `release` argument value is provided by the user to the tool, which in turn provides this to the maven goal.

... The maven copy resources plug-in have been incorporated in the base and sample-project acceptance projects. Here's how they look

```

		<plugins>
			<plugin>
				<artifactId>maven-resources-plugin</artifactId>
				<version>3.0.2</version>
				<executions>
					<execution>
						<id>copy-resources</id>
						<!-- here the phase you need -->
						<phase>test</phase>
						<goals>
							<goal>copy-resources</goal>
						</goals>
						<configuration>
							<outputDirectory>${user.home}/allure-results</outputDirectory>
							<resources>
								<resource>
									<directory>${basedir}/target/allure-results</directory>
									<filtering>true</filtering>
								</resource>
							</resources>
						</configuration>
					</execution>
				</executions>
			</plugin>

```

### Allure Results
1. The tool should copy the allure results created in the user.home/allure-results/release directory to the central VM user.home/allure-results/release directory, at the end of each test.

### Consolidated-Allure_Report
1. A web based reporting tool has to be created and hosted on a web server hosted o the central VM which has all the allure results per release.
1. The URL of this web server needs to be accessible from anywhere within the CCC network, which includes any VMs or computers connected to the CCC network.
1. The home page of the web report should have a drop down which has the releases as it's items.
1. When the user selects a release, then the allure command line tool has to be invoked to run a report on that directory under the user.home/allure-results location.
1. The local host allure results generated has to be routed to the web server so that it generates it on page refresh.

