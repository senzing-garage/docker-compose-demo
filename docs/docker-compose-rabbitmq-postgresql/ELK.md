# Setup ELK on docker-compose

## Import Senzing dashboard on ELK stack

1. Log in to Senzing Dashboard.
    1. Go to http://localhost:5601.
    1. Create kibana account.
    1. Log in with newly created kibana account.

    ![kibana available](assets/kibana_up.png)

1. Go to saved objects page.
    1. In the left-hand navigation bar, select "Stack Management".
    1. In the left-hand navigation bar, select "Saved Objects".
    1. In upper-right, click the "Import" button.

    ![saved objects page](assets/saved_objects.png)

1. Import saved objects file
    1. Click import dialog box, select the "Select a file to import"
    1. select [export.ndjson](export.ndjson)
    1. In bottom-right, click the "Import" button.

    ![saved objects page](assets/import_ndjson.png)

1. Successful import.
    ![saved objects page](assets/import_success.png)

1. View Senzing dashboard.
    1. In upper-left, click the "elastic" home button.
    1. In the dashboard menu, click on "Senzing Dashboard"
    ![dashboard page](assets/dashboard.png)

## how to look for a specific log before or after

click on any log row to expand it

click "view surrounding documents"

to only see the logs from a specific container, scroll to the top and click + add filter

for the filter field, select container_name

select the is operator

in the value field, insert the container name that you want to see and click save

you should now see the 5 logs that was recorded before and after the log you have chosen.

you can also increase the number of logs seen, by changing the number seen at the top.


