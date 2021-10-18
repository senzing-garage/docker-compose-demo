# postgresql-kafka-multi-node

**FIXME:**
On this page will be instruction to guide a user to set up:

1. "loader"
1. "redoer"
1. "api"
1. "webapp"
1. "utilities"

This page will also show how to set up a system using "mocks" for PostgreSQL and Kafka
to facilitate testing on a local workstation.

## Single-node demonstration

### Mock services

The docker-compose.yaml files require PostgreSQL and Kafka backing services.
In addition, the PostgreSQL database needs to have a schema defined
and initialized with Senzing configuration.
Finally, a set of mock data, 100K records, is sent to Kafka for demonstration purposes.

1. To set up these "mock" services and data, follow steps in [mocks](mocks/).

### Loading Senzing Model

Once source records are available in Kafka,
"stream-loaders" are deployed to
read from the Kafka Topic and send to the Senzing Engine
which manages the Senzing Model.

1. To create the set of stream-loaders, follow steps in [loader](loader/).

### Redo

The Senzing Model is monitored for any re-evaluations that are needed.
The "redoer" processes those re-evaluations.

1. To create the set of redoers, follow steps in [redo](redo/).

### Querying Senzing Model

The Senzing Model can be queried via a RESTful HTTP API
delivered by the Senzing API Server.

1. To create the set of senzing-api-servers, follow steps in [api](api/).

### Viewing Senzing Model

The Senzing Model can be visualized using the Senzing Entity Search Web App.

1. To create an entity-search-web-app, follow steps in [webapp](webapp/).
