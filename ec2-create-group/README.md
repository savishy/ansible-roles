Role Name
=========

Create EC2 Security Group with predefined port rules.

Requirements
------------

* Python, pip and Boto get automatically installed by this role.

Role Variables
--------------

**Variables from System Environment**

The following role variables are picked up from your system's environment variables:

```
aws_access_key: picked up from "AWS_ACCESS_KEY"
aws_secret_key: picked up from "AWS_SECRET_KEY"
```

**Automatically Calculated Variables**

The `host_ip` role variable contains your machine's IP address.
It is automatically calculated.

**EC2-specific variables**

The following EC2-specific variables have some default values.

```
ec2_group_name
ec2_region
ec2_vpc_id
```

The following variable is a list of ports and protocols to open up.
ec2_ports:
   - { proto: "tcp", from: "80", to: "80" }
   - { proto: "tcp", from: "22", to: "22" }
   - { proto: "tcp", from: "8080", to: "8080" }
   - { proto: "tcp", from: "8081", to: "8081" }
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
