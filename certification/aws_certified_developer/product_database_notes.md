*********************************
Database Management Service (DMS)
*********************************

-Migrate existing DB to AWS
-Data type transformations, compression, transfer
-AWS schema conversion tool

*********************************
Relational Database Service (RDS)
*********************************

DB Engines
-MariaDB
-Postgre SQL
-Amazon Aurora
-MySQL
-Oracle
-Microsoft SQL server

Online Transaction Processing (OLTP)
-Query data for order 1234 including name, date, address

Online Analytics Processing (OLAP)
-Query data for net profits in a region & product

***********
Elasticache
***********

-In memory cache in the cloud
-Improve web performance
-Get data from cache vs database query

Solutions
-Memcached
-Redis

********
DynamoDB
********

fast - flexible No sql database - single digit ms latency, fully managed, supports document and key-value (web, gaming, ad-tech, IOT)..

(T) table
(I) item (row)
(A) attribute (key - value)

Limits:
tables per region = 256 (initial limit)
local secondary indexes per table = 5
global secondary indexes per table = 5
partition key & sort key length
-min = 1 byte
-max = 2048 bytes

There is no practical limit on the number of distinct partition key values, for tables or for secondary indexes.
400kb = length of string or binary

Eventual Consistent Reads vs Strongly Consistent Reads

Read Capacity Units, Write Capacity Units (can be scaled up) - push button scalability

Writes are written to 3 different location / facilities/ datacenter (synchronous) - Amazon DynamoDB synchronously replicates data across three facilities in an AWS Region, giving you high availability and data durability.

Table Names and Secondary Index Names
Names for tables and secondary indexes must be at least 3 characters long, but no greater than 255 characters long. Allowed characters are:
A-Z
a-z
0-9
_ (underscore)
- (hyphen)
. (dot)

Two types of primary key

Single Attribute (think unique id)
Partition Key (Hash Key) composted of 1 attribute (no nesting allowed here) - Partition key will help determine the physical location of data.

Composite key (think unique id and range)
Partition Key(Hash Key) & Sort Key (Range key - e.g date) - composed of 2 attributes - if two data have same partition key (same location) it must have a different sort key, and they will be stored together on single location.

Secondary Indexes

Local Secondary Index
can only be created while creating the table, cannot be added/removed or modified later
-Same Partition Key
PLUS
-Different Sort Key

Global Secondary Index
can be created during the table creation or can be added later or removed / modified later
-Different Partition Key
PLUS
-Different Sort Key

API
-CreateTable/UpdateTable/DeleteTable
-BatchGetItem
-BatchWriteItem
-DescribeLimits
-Query
-Scan

DynamoDB Streams

use to capture any kinda modification to the dynamo db table, Lambda can capture events and push notifications thru SES

Table can be exported to csv (either select all items )

Query vs Scan

Query operation finds item in a table using only primary key attribute values , must provide partition attribute name and the value to search for, you can optionally provide a sort key attribute name and value to refine search results (e.g. all the forums with this ID since last 7 days). By default Query returns all the data attributes for those items with specified primary keys. You can further use ProjectionExpression parameter to only return a selected attributes.

Query results are always sorted by the sort key (ascending for both numbers and string by default). To reverse the sort order set the ScanIndexForward parameter to false

By Default Queries are going to be Eventually consistent but can be changed to StronglyConsistent.

Scan operation is basically examines every item - e.g. dumping the entire table, by default Scan returns all the data attributes but we could use ProjectionExpression parameter to only return a selected attributes.

Query operation is more efficient than scan operation

For quick response time design your table in a way that you can use Query Get or BatchGetItem API (read multiple items - can get upto 100 items or up to 1MB of data) ,

Alternatively design your application to use scan operation in a way that minimize impact of your table’s request rate since it can use up the entire table’s provisioned throughput in a single scan operation

When you exceed your maximum allowed provisioned throughput for a table or one or more global secondary index you will get 400 HTTP Status code - ProvisionedThroughputExceededException

AssumeRolewithWebIdentity role

Idempotent conditional write

Atomic counters - always need to increment so its not idempotent

if data is critical and no margin of error then must use Idempotent conditional write.

Only Tables(256 table per region) and ProvisionedThroughput(80 K read, 80K write per account for US east, 20K for other regions) limits can be increased
