# ansible-roles #

This is a repository of reusable ansible roles.

Frequently, I find the need to *maintain my ansible roles* in a repo away from
the application repository. This github repo serves that purpose while making
the roles:
* extensible
* as generic as possible

To pull these roles automatically when running a playbook do the following.

## Usage ##

### Modify `playbook.yml` to call `ansible-galaxy` ###

In your playbook add the line at the top, which will call `ansible-galaxy` and
pull all roles from this repository to the `roles` folder.

```
- name: download dependent roles
  command: ansible-galaxy install -r requirements.yml -p roles
```

Where
* `roles` is the name of the folder where all your Ansible roles are stored.
* `requirements.yml` lists the details of where to pull down your roles from.
  (detailed below)

### Create/Modify `requirements.yml` ###

Your `requirements.yml` is used by the `ansible-galaxy` tool to understand
what sources to use. It should list *this* github repository as the source.

(Note: you can extend this file to pull from multiple sources).


```
---
- src: https://github.com/savishy/ansible-roles/
  name: ansible-roles
  version: master
  scm: git
```

### Call the roles ###

Now all you have to do is reference these roles correctly.

E.g the following task calls the `ansible-install-docker` role from this repo
on a set of hosts called `dockerhosts`.

```
---
- name: Example of using ansible-install-docker
  hosts: dockerhosts
    roles:
      - ansible-roles/ansible-install-docker
```

# References #

1. https://github.com/ansible/ansible/issues/16804
