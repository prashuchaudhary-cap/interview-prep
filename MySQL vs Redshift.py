----------------------------------------------
        Redshift Vs RDS – Comparison
----------------------------------------------

"""

We have now covered the basics of AWS Relational database service and Redshift. Lets now compare
these managed services considering the most critical factors based on which a data architect will choose one of these.

"""

##############################################
          Redshift Vs RDS: Scaling
##############################################

"""

The ability to scale is one of the most critical factors to consider when making a choice between different databases. Both Redshift
and RDS allows the customers to scale as per their budget and performance requirements.  Since RDS is based on virtualized instances,
its scaling is done by reconfiguring the virtual instance capabilities. Scaling takes only a few minutes and can be done in a few
clicks in the AWS console. Redshift is based on a more complex architecture and it means scaling is not as seamless as it is in RDS.
Redshift instances with support for elastic resize can do it in a few minutes, but the database unavailable time window is certainly
higher than that of RDS. That said, the limit of scaling is higher for Redshift when it comes to storage. Redshift also has an option
called concurrency scaling which can be used to support a virtually unlimited number of concurrent users without a drop in querying
performance.

"""

##############################################
      Redshift Vs RDS: Storage Capacity
##############################################

"""

The biggest differentiator between Redshift and RDS is the storage capacity and the limit to which it can be scaled. With Redshift,
the storage can be scaled up to petabytes of data. The limit of AWS Redshift is 2 PB with its ds2.8xlarge type instance. With RDS,
since it works with individual virtualized instances, the storage limit is in the range of TBs and will vary according to the chosen
database engine. For SQL server the storage capacity is limited at 16 TB, while the aurora engine can scale up to 64 TB. All the
other engine types can scale up to 32 TB of data

"""


##############################################
      Redshift Vs RDS: Data Replication
##############################################

"""

A major workload in any ETL will be the data load from different sources. Since these services have entirely different architecture,
the procedure to load is also different. With RDS, this is closely tied to the underlying database engine that is being used.
Importing the data will use the engine specific commands. Similarly, the tools for exporting will also depend on the source and
target engine types like mysqldump for MySQL or pg_dump for Postgres.

For Redshift, importing data will involve copying the complete data to S3 and loading it using the COPY command. You may require
temporary tables if your Redshift tables already contain data. A detailed blog on how to do ETL in Redshift can be found here.

What you should note while moving data to Redshift or RDS:

First thing, you should remember that you are looking to move data into Amazon Redshift or RDS for key business processes and
insights. Hence, it becomes crucial to set up a robust system that can send data to Redshift/RDS in an accurate, reliable and secure
manner.

"""

##############################################
        Redshift Vs RDS: Performance
##############################################

"""

In a nutshell, RDS offers better performance when it comes to queries that do not test its limits; To be specific, queries that do
not span across millions of rows offer better performance in RDS. The story changes when it comes to queries that need to scan millions of rows and aggregate them.

Redshift is designed for scenarios like this and excels here, offering a comparable or even better performance in such cases.
So the argument of performance to differentiate between them is tied to the actual storage use case and should not
be considered independently.

The primary reason for this is that Redshift has a very
sophisticated query optimizer and execution planner at work before the actual query execution. For simpler or low data scan queries,
this is an overkill since query optimization in most cases takes more time than the execution.

Additionally both the databases offer performance improvement through key distribution mechanisms. RDS offers sharding capability and
with carefully designed keys, customers can extract more performance. Redshift has options for SORT KEY and DIST KEY, which if used
correctly can aid in performance improvements in joins and complex queries.

"""


##############################################
         Redshift Vs RDS: Maintenance
##############################################

"""

RDS is low on maintenance compared to Redshift because of its simpler architecture.  All the administrative tasks are automated and
there is nothing much the end-users need to do to maintain it.

Redshift needs some administrative tasks to be executed manually by the cluster administrator. It uses delete markers for DELETE and
UPDATE queries. This means there needs to be an archival process for the actual deletions and this is to be done using the VACUUM
command.  This command should be executed by the cluster administrator. Redshift also recommends executing the ANALYZE command
periodically to ensure all metadata and table statistics are kept updated.

"""


##############################################
      Redshift Vs RDS: Data Structure
##############################################

"""

Since RDS is basically a relational data store, it follows a row-oriented structure. Redshift, on the other hand, has a columnar
structure and is optimized for fast retrieval of columns. RDS querying may vary according to the engine used and Redshift conforms
to Postgres standard.

Redshift does not do a good job when it comes to enforcing unique constraints in insertion keys and it is expected that the
end-users will manage it themselves. RDS offers support for unique key constraints in all the database engines.

"""

##############################################
        Redshift Vs RDS: Security
##############################################

"""

Both RDS and Redshift offers the full suite of security and compliance. They ensure data is encrypted at rest and in transit. It is
also possible to isolate the instances using a virtual private cloud network. AWS identity and access management allow close control
of permissions enabling the customers to decide who can do what in the instance types. Support for SSL is also standard in both
cases.

For RDS, the database engine may provide additional security capabilities other than standard AWS features and it is the user’s
responsibility to manage them. The case in point here is additional security settings like Oracle native network encryption and
Oracle transparent data encryption, which are valid only for oracle database engines.

"""

##############################################
        Redshift Vs RDS – Use cases
##############################################

"""

Even though both RDS and Redshift offer database as a service, they are different in many ways as depicted in the earlier sections.
Both are designed for different use cases and excels at the said use cases. We will try to enumerate the different scenarios in
which these services work best in the below sections.

"""


When to use Redshift?
 -- You want a petabyte-scale data warehouse and is not happy with traditional database engines
 -- Your analytical and reporting workload is heavy and can interfere with your OLTP database.
 -- Your queries span across millions of rows and you anticipate even more complex queries
 -- You anticipate a constant query workload and your cluster will be running for the most part of the day.
 -- You are ready to manage the uniqueness of your insertion keys yourselves and do not expect the database to ensure it.
 -- You have a willing team to put their head into DIST KEYS and SORT KEYS and structure data so that best performance is extracted.


When to use RDS?
 -- You want to use traditional databases in the cloud and the only requirement is to offload the database management.
 -- Your data volume is in TBs and you do not anticipate a large increase in the near future. RDS hits its storage limits at 64 TB.
 -- You have an online transaction processing use case and want instant results with lesser data.
 -- You don’t have queries that span across millions of rows and the query complexity is limited.
 -- Your reporting and analytical workloads are minimal and do not interfere with your OLTP workloads.
 -- Your budget is tighter and you have no intention to spend money anticipating future astronomical workloads.


