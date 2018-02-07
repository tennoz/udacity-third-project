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
8. Load the data `psql -d news -f newsdata.sql`
9. Load the views queries `psql -d news -f views.sql`
10. Download `logs_analysis.py` from this repo.
11. Run the application `python logs_analysis.py`

## Expected output
Top three articles:

"Candidate is jerk, alleges rival" -- 338647 views

"Bears love berries, alleges bear" -- 253801 views

"Bad things gone, say good people" -- 170098 views


Top authors:

"Ursula La Multa" -- 507594 views

"Rudolf von Treppenwitz" -- 423457 views

"Anonymous Contributor" -- 170098 views

"Markoff Chaney" -- 84557 views


Days with errors > 1%

Jul 17, 2016 -- 2.26% errors