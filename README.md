
# log-analysis-project

**project overview**

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report. _**(text from Udacity Project page)**_

## Prerequisites
To run a Python you need below:
1) Python 2 or 3 version from [click here](https://www.python.org/downloads/).
2) Virtual box (last update) [click here](https://www.virtualbox.org/wiki/Downloads)
3) Vagrant (last update) [click here](https://www.vagrantup.com/downloads.html).
4) command line (Git Bash for windows) [click here](https://git-scm.com/downloads).
5) Google & github to search if you stuck in any steps [click here](https://github.com/).
6) Python Pip to check the python code format [click here](https://pip.pypa.io/en/stable/installing/).

## Installing:

follow the instruction in the download page for installing the programs.

### Steps:

1) Download and install (Python, vagrant & Virtual Box "don't lunch the program").

2) open Gitbash or the command line you use and access the path you add the directory in. like
```
$cd Documents/log-analysis-project-Nora
```
3) Write the below to add the initial vagrantfile.
```
$cd vagrant init
```

4) Write the below to upload the vagrant file. it will update if there is any update need or any change you made in the file.
(better to search in google about the vagrant file which already been used to avoid the issue in psql)

```
$vagrant up
```
5) better to write (Vagrant provision) to make sure the vagrant connect to the virtual box + all the update done.
```
$vagrant provision
```
6) Write the vagrant ssh to connect the vagrant with the file to share the data.
```
$vagrant ssh
```
7) if it connected, go the vagrant file you have by typing
```
$cd /vagrant
```
Below 8 & 9 if you need to modify the SQL database.

8) load the database by writing
```
$psql -d news -f newsdata.sql
```
9) To connect the vagrant with the SQL database. write
```
$psql -d news
```

10) if you want to fetch the Data.
- if you already added the 7 & 8 and you want to go back , just type ctrl+d to go back or control & C to cancel the request you sent to the Database.
- if you already in step 7 and wants to fetch the data just put the Python file by writing
```
$python log-analysis-project.py
```
11) The page will give you the available queries which added and select which one you need.
12) It will fetch and print all the data and will send you back to the step 6.

## The Views:

Views help you to arrange the data you are working on and to avoid many syntax error that appears while you are coding.
In this project I've created 2 views only for the 3rd query (Error query):

**Not_found_error VIEW:**

```
CREATE VIEW Not_found_error AS
SELECT (time::timestamp::date) AS error_time,
       status, count(status) AS error_per_day
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY error_time,
         status
ORDER BY error_per_day desc;
```

>In the above view we need to count how many times we git 404 not found error while log in,
the sql is taking the time & status from log table and to summarize it as per the count of the error per day.

**total_status VIEW:**

```
CREATE VIEW total_status AS
SELECT (time::timestamp::date) AS status_time,
       count(status) AS status_per_day
FROM log
GROUP BY status_time
ORDER BY status_per_day;
```
> in this view, we need the information of the total status the system give everyday
to use both views to find the ratio of error + normal log within the each day.

## Authors
Nora Almotairy
