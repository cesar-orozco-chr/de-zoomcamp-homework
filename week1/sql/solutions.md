# Exercise solutions

1. How many taxi trips were there on January 15?
```
with trips as (
	Select extract(day from cast(tpep_pickup_datetime as timestamp) ) as trip_day,
	     extract(month from cast(tpep_pickup_datetime as timestamp)) as trip_month
	from yellow_cabs
)
select count(*)
from trips
where trip_day = 15;
```

2. On which day it was the largest tip in January? (note: it's not a typo, it's "tip", not "trip")
```
Select tpep_dropoff_datetime, tip_amount
from yellow_cabs
order by tip_amount DESC
limit 1;
```

3. What was the most popular destination for passengers picked up in central park on January 14? Enter the zone name (not id). 
If the zone name is unknown (missing), write "Unknown"

```
select do_zone."zone", count(yellow_cabs."DOLocationID") as freq
from yellow_cabs
inner join zone as pu_zone on yellow_cabs."PULocationID" = pu_zone."LocationID"
inner join zone as do_zone on yellow_cabs."DOLocationID" = do_zone."LocationID"
where pu_zone."zone"= 'Central Park'
group by 1
order by count(yellow_cabs."DOLocationID") DESC
limit 1;
```

4. What's the pickup-dropoff pair with the largest average price for a ride 
(calculated based on total_amount)? 
Enter two zone names separated by a slash
For example:"Jamaica Bay / Clinton East"
If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East".
```
select concat(coalesce(pu_zone."zone", 'Unknown'),'/', coalesce(do_zone."zone",'Unknown')), AVG(total_amount)
from yellow_cabs
inner join zone as pu_zone on yellow_cabs."PULocationID" = pu_zone."LocationID"
inner join zone as do_zone on yellow_cabs."DOLocationID" = do_zone."LocationID"
group by 1
order by AVG(total_amount) DESC
limit 1;
```