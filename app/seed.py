
import requests

documents = [
    "How to restart nginx service using systemctl",
    "Configure SSL certificates in nginx with Let's Encrypt",
    "Troubleshooting 502 Bad Gateway errors in nginx",
    "Setting up virtual hosts in Apache web server",
    "How to check active network connections in Linux",
    "Using journalctl to view system logs",
    "Managing system services with systemctl",
    "How to create a new Linux user account",
    "Setting file permissions using chmod",
    "Understanding Linux process management",
    "How to monitor CPU usage in Linux",
    "Checking memory consumption with free command",
    "Disk space analysis using df and du",
    "Creating and restoring PostgreSQL backups",
    "Configuring PostgreSQL replication",
    "Optimizing PostgreSQL query performance",
    "Troubleshooting PostgreSQL connection issues",
    "How to create a database in PostgreSQL",
    "Managing PostgreSQL users and roles",
    "Using pg_dump for database exports",
    "Introduction to Docker containers",
    "Building custom Docker images",
    "Managing Docker volumes and persistent storage",
    "Docker container networking basics",
    "Troubleshooting Docker container crashes",
    "Deploying applications with Docker Compose",
    "Viewing logs from running Docker containers",
    "Container resource limits in Docker",
    "Introduction to Kubernetes deployments",
    "Scaling applications in Kubernetes",
    "Managing Kubernetes pods and services",
    "Troubleshooting Kubernetes cluster issues",
    "Configuring ingress controllers in Kubernetes",
    "Using kubectl to manage workloads",
    "Monitoring applications with Prometheus",
    "Setting up Grafana dashboards",
    "Understanding Prometheus alert rules",
    "Configuring Alertmanager notifications",
    "Investigating server downtime incidents",
    "Incident response workflow for production systems",
    "How to rotate logs using logrotate",
    "SSH key authentication setup guide",
    "Securing Linux servers with firewall rules",
    "Managing cron jobs for scheduled tasks",
    "Troubleshooting DNS resolution problems",
    "Understanding TCP and UDP protocols",
    "Configuring load balancing with HAProxy",
    "Backup and disaster recovery planning",
    "Monitoring server health with Nagios",
    "Analyzing application performance bottlenecks",

    "Installing and configuring Redis cache server",
    "Redis persistence and backup strategies",
    "Troubleshooting Redis memory issues",
    "Setting up MySQL database replication",
    "Managing MySQL users and privileges",
    "How to optimize MySQL queries",
    "Understanding Linux kernel modules",
    "Managing packages with apt package manager",
    "Managing packages with yum package manager",
    "Configuring static IP addresses in Linux",
    "Troubleshooting network latency problems",
    "Understanding routing tables in Linux",
    "Configuring VLANs on network switches",
    "Introduction to network troubleshooting",
    "Analyzing packet captures using Wireshark",
    "Monitoring network traffic with tcpdump",
    "How to use netstat for diagnostics",
    "Using ss command to inspect sockets",
    "Understanding DNS records and zones",
    "Setting up Bind DNS server",

    "Deploying FastAPI applications with Gunicorn",
    "Serving FastAPI behind nginx reverse proxy",
    "Troubleshooting FastAPI deployment issues",
    "Managing Python virtual environments",
    "Creating REST APIs with FastAPI",
    "Implementing JWT authentication in FastAPI",
    "Background task processing with Celery",
    "Connecting FastAPI to PostgreSQL",
    "Database migrations using Alembic",
    "Understanding asynchronous programming in Python",

    "Setting up CI CD pipelines with GitHub Actions",
    "Automating deployments using Jenkins",
    "Managing source code with Git",
    "Resolving merge conflicts in Git",
    "Understanding Git branching strategies",
    "Using Terraform for infrastructure provisioning",
    "Managing cloud resources with Terraform",
    "Deploying virtual machines on AWS",
    "Introduction to Amazon EC2 instances",
    "Configuring security groups in AWS",
    "Managing storage with Amazon S3",
    "Monitoring AWS infrastructure with CloudWatch",
    "Understanding IAM roles and permissions",
    "Creating snapshots for disaster recovery",
    "Setting up VPN access for remote workers",

    "Introduction to cybersecurity fundamentals",
    "Detecting suspicious login attempts",
    "Configuring intrusion detection systems",
    "Hardening Linux servers for production",
    "Managing SSL and TLS certificates",
    "Understanding brute force attacks",
    "Investigating failed authentication logs",
    "Monitoring unauthorized file changes",
    "Performing vulnerability assessments",
    "Security best practices for system administrators"
]


url = "http://127.0.0.1:8000/documents"

def seed():
    count = 0

    for doc in documents:
        res = requests.post(url, json={"text":doc})

        count += 1

    print(f"{count} documents inserted successfully")


if __name__ == "__main__":
    seed()