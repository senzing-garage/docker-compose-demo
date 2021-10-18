# postgresql-kafka-multi-node

**FIXME:**
On this page will be instruction to guide a user to set up:

1. [loader](loaders/)
1. [redoer](redoer/)
1. [api](api/)
1. [webapp](webapp/)
1. [utilities](utilities/)

## Single-node demonstration

Although this demonstration is for multi-node (i.e. multiple real or virtual machines) deployment,
the deployment can be done on a single machine for educational or testing purposes.

The single-node demonstration will use "mock" PostgreSQL and Kafka services
deployed as additional docker containers.
This alleviates the need to set up the services separately.

### Mock services

The docker-compose.yaml files require PostgreSQL and Kafka backing services.
In addition, the PostgreSQL database needs to have a schema defined
and initialized with Senzing configuration.
Finally, a set of mock data, 100K records, is sent to Kafka for demonstration purposes.

1. To set up these "mock" services and data, follow steps in [mocks](mocks/).

### Loading Senzing Model

Once source records are available in Kafka,
[stream-loaders](https://github.com/Senzing/stream-loader)
are deployed to read from the Kafka Topic and send
to the Senzing Engine which manages the Senzing Model.

1. To create the set of stream-loaders, follow steps in [loader](loader/).

### Redo

The Senzing Model is monitored for any re-evaluations that are needed.
The [redoers](https://github.com/Senzing/redoer)
processes those re-evaluations.

1. To create the set of redoers, follow steps in [redo](redo/).

### Querying Senzing Model

The Senzing Model can be queried via a RESTful HTTP API
delivered by the
[Senzing API Server](https://github.com/Senzing/senzing-api-server).

1. To create the set of senzing-api-servers, follow steps in [api](api/).

### Viewing Senzing Model

The Senzing Model can be visualized using the
[Senzing Entity Search Web App](https://github.com/Senzing/entity-search-web-app).

1. To create an entity-search-web-app, follow steps in [webapp](webapp/).

### Utilities

Utilities programs include a
[console](https://github.com/Senzing/docker-senzing-console) container
and
[SwaggerUI](https://www.github.com/swagger-api/swagger-ui).

1. To create utilities, follow steps in [utilities](utilities/).
