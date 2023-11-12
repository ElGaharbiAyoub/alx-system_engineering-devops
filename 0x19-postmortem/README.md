# alx-system_engineering-devops


The web application experienced an outage that lasted for 2 hours and 30 minutes on November 12, 2023, from 10:00 AM to 12:30 PM (UTC+0). The outage affected the entire application, and users were unable to access the website during this time.

## Timeline:

- 10:00 AM: The issue was detected by the monitoring system, which alerted the engineering team.
- 10:05 AM: The engineering team started investigating the issue and found that the web server was down.
- 10:10 AM: The team tried to restart the web server, but it failed to start.
- 10:15 AM: The team investigated the logs and found that the web server was running out of memory.
- 10:20 AM: The team increased the memory allocation for the web server and restarted it.
- 10:25 AM: The team monitored the web server and found that it was running smoothly.
- 12:30 PM: The team declared the issue resolved.

## Root Cause and Resolution:

The root cause of the issue was that the web server was running out of memory due to a memory leak in the application code. The team fixed the issue by identifying the memory leak and patching the code. They also increased the memory allocation for the web server to prevent similar issues in the future.

## Corrective and Preventative Measures:

To prevent similar issues in the future, the team will take the following corrective and preventative measures:

- Add more monitoring alerts: The team will add more monitoring alerts to detect memory usage and other critical metrics.
- Optimize code: The team will optimize the application code to reduce memory usage and prevent memory leaks.
- Increase memory allocation: The team will increase the memory allocation for the web server to prevent similar issues in the future.
