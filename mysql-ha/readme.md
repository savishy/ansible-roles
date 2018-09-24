# MySQL Cluster

This is currently an experiment to create a containerized MySQL HA Cluster using Ansible-managed Docker. 
The steps have been picked up from the references at the bottom of the page.

At the end of this role run, you would have:

1. MySQL Cluster Management Node
1. 2 Data Nodes
1. MySQL Server Node
1. Management Client Node.

## How to run

A sample playbook:

```
- hosts: localhost
  connection: local
  roles:
  - ansible-roles/mysql-ha
```

`ansible-playbook --ask-vault-pass playbook.yml`

## Notes

* The image used, `mysql/mysql-cluster`, has a healthcheck script [`healthcheck.sh`](https://github.com/mysql/mysql-docker/blob/mysql-cluster/7.6/healthcheck.sh).
* The script has logic to look for a file that gets placed when initialization is complete.
* However the logic seems to create that file only for containers with `mysqld` as the command.

In other words, _only the MySQL Server reports healthy status._ All other containers report unhealthy.

```
72e8dd15ba83        mysql/mysql-cluster   "/entrypoint.sh ndb_…"   10 minutes ago      Up 10 minutes (unhealthy)   1186/tcp, 2202/tcp, 3306/tcp, 33060/tcp   mysqlha_mgmt_client
0822084bdb48        mysql/mysql-cluster   "/entrypoint.sh mysq…"   10 minutes ago      Up 10 minutes (healthy)     1186/tcp, 2202/tcp, 3306/tcp, 33060/tcp   mysqlha_mysql1
3fe9b4ec2a0b        mysql/mysql-cluster   "/entrypoint.sh ndbd"    11 minutes ago      Up 11 minutes (unhealthy)   1186/tcp, 2202/tcp, 3306/tcp, 33060/tcp   mysqlha_ndb2
7726c712c0f3        mysql/mysql-cluster   "/entrypoint.sh ndbd"    11 minutes ago      Up 11 minutes (unhealthy)   1186/tcp, 2202/tcp, 3306/tcp, 33060/tcp   mysqlha_ndb1
c4f33a6bdbd2        mysql/mysql-cluster   "/entrypoint.sh ndb_…"   11 minutes ago      Up 11 minutes (unhealthy)   1186/tcp, 2202/tcp, 3306/tcp, 33060/tcp   mysqlha_mgmt
```

So one way to check health is using the Management Client:

```
docker exec -it mysqlha_mgmt_client ndb_mgm
-- NDB Cluster -- Management Client --
ndb_mgm> show
Connected to Management Server at: 172.21.0.2:1186
Cluster Configuration
---------------------
[ndbd(NDB)]	2 node(s)
id=2	@172.21.0.3  (mysql-5.7.23 ndb-7.6.7, Nodegroup: 0, *)
id=3	@172.21.0.4  (mysql-5.7.23 ndb-7.6.7, Nodegroup: 0)

[ndb_mgmd(MGM)]	1 node(s)
id=1	@172.21.0.2  (mysql-5.7.23 ndb-7.6.7)

[mysqld(API)]	1 node(s)
id=4	@172.21.0.10  (mysql-5.7.23 ndb-7.6.7)

ndb_mgm>

```

## References

1. https://hub.docker.com/r/mysql/mysql-cluster/
1. https://stackoverflow.com/questions/47528400/failed-to-allocate-nodeid-for-api-at-sql-node-ipaddr-returned-error-no-free
1. https://github.com/mysql/mysql-docker/blob/mysql-cluster/
