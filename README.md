# Logs Analysis Tool

## Description
This is a reporting tool which analyse database entries. It solves the following three questions;

1. What are the most famous articles and their views?
2. Who are the most famous writers and how often were their articles viewed?
3. On which day was the error rate more than 1%?

## How to run?
In order to run this application you first need to do the following:

1. Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads "Virtualbox")
2. Install [Vagrant](https://www.vagrantup.com/downloads.html "Vagrant")
3. Download [Vagrant setup files](https://github.com/udacity/fullstack-nanodegree-vm)
to configure the VM
4. Download [Database File](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), then extract the file and put it in the vagrant directory.
5. Open your terminal and change directory to the vagrant folder we downloaded.
6. Run `vagrant up`
7. Run `vagrant ssh`
8. Load the data `psql -d news -f newsdata.sql
9. Open postgresql `psql -d news`
10. Run the following queries:
`create view total_req as select count(*) as count, date(time) as date from log group by date order by count desc;`\s \s
`create view err_req as select count(*) as count, date(time) as date from log where status <> '200 OK' group by date order by count desc;` \s \s
`create view err_prc as select total_req.date, round((100.0*err_req.count)/total_req.count, 2) as percent from err_req join total_req on err_req.date = total_req.date;`\s \s
11. Exit psql `ctrl + d`
12. Download `logs_analysis.py` from this repo.
13. Run the application `python logs_analysis.py`

## Expected output
Top three articles: \s \s
"Candidate is jerk, alleges rival" -- 338647 views \s \s
"Bears love berries, alleges bear" -- 253801 views \s \s
"Bad things gone, say good people" -- 170098 views \s \s

Top authors: \s \s
"Ursula La Multa" -- 507594 views \s \s
"Rudolf von Treppenwitz" -- 423457 views \s \s
"Anonymous Contributor" -- 170098 views \s \s
"Markoff Chaney" -- 84557 views \s \s

Days with errors > 1% \s \s 
Jul 17, 2016 -- 2.26% errors