# Azure VNETs


## Type 1

1. 1 VNET
1. 1 Subnet

## Type 2

1. 1 VNET
1. 1 Subnet + 1 GatewaySubnet
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
