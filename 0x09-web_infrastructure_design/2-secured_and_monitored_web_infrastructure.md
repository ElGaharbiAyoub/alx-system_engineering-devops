# 2-secured_and_monitored_web_infrastructure

![](https://github.com/ElGaharbiAyoub/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png)

## Explanation of Additional Elements:

- Firewalls: Added for security. They restrict unauthorized access and protect communication paths.
- HTTPS: Ensures encrypted data transmission, safeguarding user privacy and preventing data interception.
- Monitoring: Monitors system health, security, and performance to detect and address issues proactively.

## Issues with the Infrastructure:

### Terminating SSL at the Load Balancer:

- Terminating SSL at the load balancer might expose decrypted data to potential security risks within the internal network.

### Single MySQL Server for Writes:

- Having only one MySQL server capable of accepting writes introduces a single point of failure for write operations.

### Uniform Server Components:

- Using identical server components for web, application, and database functions could lead to resource contention and scalability challenges.
