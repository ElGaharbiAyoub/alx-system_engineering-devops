# 1-distributed_web_infrastructure

![](https://github.com/ElGaharbiAyoub/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png)

## Issues with the Infrastructure:

### Single Point of Failure (SPOF):

- While the load balancer improves redundancy, it could still be a SPOF if not properly configured or monitored.

### Security Issues:

- No firewall mentioned, leaving the infrastructure vulnerable to unauthorized access.
- Lack of HTTPS exposes data to potential eavesdropping and security breaches.

### No Monitoring:

- The absence of monitoring tools makes it difficult to identify performance issues or failures promptly.
