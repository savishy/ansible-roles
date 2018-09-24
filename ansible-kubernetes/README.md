:exclamation: To Be Deleted as Elastic Kubernetes Service (EKS) or Azure Kubernetes Service (AKS) work better. 

## Introduction

* This role has been ported from https://github.com/kubernetes/contrib/tree/master/ansible.
* The port was needed because I needed a way to import this Ansible role from
  Github automatically while executing my `Vagrantfile`.

I have tested using this with Vagrant + Ansible. It works, with the caveats
listed below.


## Caveats

### Bring up all machines before provisioning them

The provisioning steps require *all machines to be up*.

### `group_vars`


### Group Names

Group names need to be *exactly* as listed in the sample inventory file `inventory/localhost.ini`.

An example of group names in your `Vagrantfile`:

```
config.vm.provision "ansible" do |ansible|
  ...
  ansible.groups = {
      "masters" => ["master0"],
      "etcd" => ["etcd0"],
      "nodes" => ["master0","worker0"]
  }
end
```
