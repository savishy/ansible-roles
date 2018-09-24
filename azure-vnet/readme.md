# Azure Virtual Networks

This role creates Virtual Networks (VNETs) in Azure. Several different architectures are supported; read below to understand more.

## Type 1

This creates: 

1. 1 VNET
1. 1 Subnet

## Type 2

This creates a VNET and a VPN Gateway, so that VMs can be placed in the subnet without a public IP. 

1. 1 VNET
1. 2 subnets - 1 Subnet + 1 GatewaySubnet
1. 1 VPN Gateway

## Example Playbook

```
- hosts: localhost
  vars:
    location: eastus
    azure_vnet_type: type2
  roles:
  - ansible-roles/azure-vnet
```

## References
1. https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings
