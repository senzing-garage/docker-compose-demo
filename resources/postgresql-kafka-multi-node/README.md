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
Finally, a set of mock data is sent to Kafka for demonstration purposes.

1. To set up these "mock" services and data, follow steps in [mocks](mocks/).
