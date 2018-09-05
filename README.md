#Log Analysis Project
--------------------------------------

##Project Description:
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database

##Questions:
 1. **What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

 2. **Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

 3. **On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)


 ##This Project Requires a Bit of Setup:

 ####Install Dependencies / Set Up Files
1. Install Vagrant
2. Install VirtualBox
3. Download the vagrant setup files from Udacity's Github These files configure the virtual machine and install all the tools needed to run this project.
4. Download the database setup: data
5. Unzip the data to get the newsdata.sql file.
6. Put the newsdata.sql file into the vagrant directory
7. Download this project: log analysis
8. Upzip as needed and copy all files into the vagrant directory into a folder called log_analysis

####Start The Virtual Machine
1. Open Terminal and navigate to the project folders we setup above.
2. cd into the vagrant directory
3. Run vagrant up to build the VM for the first time.
4. Once it is built, run vagrant ssh to connect.
5. cd into the correct project directory: cd /vagrant/log_analysis

####Load the data into the database:
1. Load the data using the following command: psql -d news -f newsdata.sql
2. Note: Checkout Udacity's FAQ page if you are running into any errors here.

###Run The Project!
1. Make sure that your vagrant is up and connected
2. cd into the vagrant directory: cd /vagrant/Logs_Analysis
3. Run the python file with the following command: $ python reporterdb.py
