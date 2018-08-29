Creates a Windows or Linux VM on Azure. 

## Important Variables

Look at [defaults/main.yml](defaults/main.yml) for all the variables that can be set and their default values.

| Variable | Type | Notes |
|-|-|-|
| `rg_name` | | Resource Group Name |
| `location` | | Azure Location | 
| `vm_pubip_name, vm_nic_name, vm_vnet_name, vm_nsg_name, vm_subnet_name` | | Naming Conventions for VM Resources |
| `vm_image` | Dictionary | Offer, Publisher, SKU and Version of VM Image |
| `vm_nsg_rules` | List of Dictionaries | Rules to set in the NSG for the VM. |
