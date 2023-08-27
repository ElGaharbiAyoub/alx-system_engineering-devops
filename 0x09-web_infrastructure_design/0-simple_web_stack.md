# 0-simple_web_stack

![](https://github.com/ElGaharbiAyoub/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png)

## Issues with the Infrastructure:

### Single Point of Failure (SPOF):

- Since the entire infrastructure relies on a single server, any failure can cause the entire website to go down.
- Hardware failures, software crashes, or other issues could lead to prolonged downtime.

### Downtime During Maintenance:

- When deploying new code or performing maintenance, the web server needs to be restarted.
- This can cause downtime, affecting user access during the maintenance window.

### Inability to Scale:

- With a single server, it's challenging to handle a significant increase in incoming traffic.
- The infrastructure cannot easily scale horizontally to accommodate more users.
