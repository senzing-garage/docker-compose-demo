# Setup ELK on docker-compose

A quick guide on how to use the setup and use the ELK stack to sift through Senzing's logs.

## Contents

1. [Import Senzing dashboard on ELK stack](#Import-Senzing-dashboard-on-ELK-stack)
1. [View surrounding logs](#View-surrounding-logs)

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
    1. In the import dialog box, select the "Select a file to import"
    1. select [export.ndjson](export.ndjson)
    1. In bottom-right, click the "Import" button.

    ![saved objects page](assets/import_ndjson.png)

1. Successful import.
    ![saved objects page](assets/import_success.png)

1. View Senzing dashboard.
    1. In upper-left, click the "elastic" home button.
    1. In the dashboard menu, click on "Senzing Dashboard"
    ![dashboard page](assets/dashboard.png)

## View surrounding logs

1. View logs surrounding selected log 
    1. click on log row to expand it
    1. click "view surrounding documents"
    ![view surrounding documents](assets/surround_doc.png)

1. Filter logs by container name
    1. In top-left, click the "+ Add filter" button.
    1. In the import dialog box, select "container_name" as the filter field
    1. Select "is" in the operator field
    1. Insert container name (e.g. senzing-stream-loader) into the value field
    1. In bottom-right, click the "Save" button.
    ![filter by container name](assets/filter_log.png)

1. Increase number of logs before/after selected log
    1. In top-left, click on the up arrow key to increase the logs see before
    ![increase before log view](assets/increase_before_log.png)
    1. In bottom-left, click on the up arrow key to increase the logs see before
    ![increase after log view](assets/increase_after_log.png)




