Role Name
=========

`install-docker`

This Ansible Role installs Docker, Docker Machine and Compose on a Linux
host. I wrote this to reuse roles between various docker projects.

Requirements
------------

- Vagrant (recommended)
- An Ubuntu or CentOS Vagrant box.

This role has been tested on the vagrant boxes `lattice/ubuntu-trusty-64` and `perconajayj/centos-x86_64`.

Role Variables
--------------

```
docker_user: the default user for docker
docker_api_port: the default port on which docker listens

```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

```
    - hosts: servers
      roles:
      - { role: ansible-roles/install-docker, docker_user: vagrant }
```
License
-------

BSD

Author Information
------------------

http://github.com/savishy
