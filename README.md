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

### download the roles ###

If you are using Vagrant + Ansible this is how you would do it:

```
config.vm.provision "ansible" do |ansible|
    ansible.galaxy_role_file = "requirements.yml"
    ansible.galaxy_roles_path = "./roles"
    ansible.groups = {
    # some groups of hosts to execute the playbook on
    }

    ansible.verbose = "vvvv"
    ansible.playbook = "playbook.yml"
end
```

This provisioning mechanism will first download `ansible-roles` from Github
into your `pwd/roles` directory.

### reference the roles ###

```

- name: setup monitoring
  hosts: monitors
  roles:
    - ansible-roles/ansible-install-docker
    - ansible-roles/ansible-efk-docker
```



# References #

1. https://github.com/ansible/ansible/issues/16804
1. https://www.vagrantup.com/docs/provisioning/ansible_common.html#galaxy_command
