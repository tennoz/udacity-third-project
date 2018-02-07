create view total_req as select count(*) as count, date(time) as date from log group by date order by count desc;

create view err_req as select count(*) as count, date(time) as date from log where status <> '200 OK' group by date order by count desc;

create view err_prc as select total_req.date, round((100.0*err_req.count)/total_req.count, 2) as percent from err_req join total_req on err_req.date = total_req.date;