# Ansible Role - azurevm

* Creates a Windows or Linux VM on Azure, mapped to an _existing_ VNET.
* Each VM gets a Public IP, NIC, NSG and Managed OS Disk on Azure. 
* For Windows VMs, Remoting is enabled on SSL (port 5986). 

**Does not create VNETs.**

Use the `azure-vnet` role to do that.

**Linux by default**

The OS created is Linux by default. 

**Vaulted OS Password**

The password is stored encrypted, in the role variables.
Execute with `--ask-vault-pass` to enable the role to decrypt the password.

**NSG Rules**: 

The Ansible controller's IP is stored in a fact `ansible_controller_ip` if you wish to open NSG rules only from your Ansible controller machine. Look at the `defaults/main.yml` for an example.

## How to use

Read the top-level README file.

## Important Variables

Look at [defaults/main.yml](defaults/main.yml) for all the variables that can be set and their default values.

| Variable | Type | Notes |
|-|-|-|
| `rg_name` | | Resource Group Name |
| `location` | | Azure Location | 
| `vm_pubip_name, vm_nic_name, vm_vnet_name, vm_nsg_name, vm_subnet_name` | | Naming Conventions for VM Resources |
| `vm_image` | Dictionary | Offer, Publisher, SKU and Version of VM Image. Set this to a Windows or Linux image as appropriate. |
| `vm_nsg_rules` | List of Dictionaries | Rules to set in the NSG for the VM. |
| `vm_os_type` | Change to "Windows" to enable Windows-specific tasks to run. |

