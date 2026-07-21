# System Commands

System commands help you inspect, monitor, and clean up your Docker environment.

Unlike container or image commands, these are used for maintenance and troubleshooting.

---

# 1. Docker Version

Check the installed Docker version.

```bash
docker version
```

Example Output:

```text
Client:
 Version: 28.3.2

Server:
 Engine: 28.3.2
```

Unlike `docker --version`, this displays information about both the **Client** and the **Docker Engine**.

---

# 2. Docker Information

View detailed information about your Docker installation.

```bash
docker info
```

This includes:

- Number of Images
- Number of Containers
- Docker Root Directory
- Storage Driver
- CPU & Memory
- Operating System
- Docker Version

Useful for verifying that Docker Engine is running correctly.

---

# 3. Disk Usage

Check how much space Docker is using.

```bash
docker system df
```

Example:

```text
TYPE            TOTAL
Images            12
Containers         8
Volumes            4
Build Cache      1.2 GB
```

Useful when Docker starts consuming too much storage.

---

# 4. Clean Up Unused Resources

Remove unused Docker resources.

```bash
docker system prune
```

Docker removes:

- Stopped Containers
- Unused Networks
- Dangling Images
- Build Cache

To remove everything, including unused images:

```bash
docker system prune -a
```

> **Be careful:** This permanently deletes unused Docker resources.

---

# 5. Docker Events

Monitor Docker activities in real time.

```bash
docker system events
```

You'll see events like:

```text
Container Started
Container Stopped
Image Pulled
Container Removed
```

Press **Ctrl + C** to stop monitoring.

---

# Commonly Used System Commands

| Command | Purpose |
|----------|---------|
| `docker version` | Show Docker Client & Engine versions |
| `docker info` | Display Docker system information |
| `docker system df` | Check Docker disk usage |
| `docker system prune` | Remove unused resources |
| `docker system events` | Monitor Docker events |

---

# Summary

System commands are mainly used to:

- Verify Docker installation
- Inspect Docker Engine
- Monitor Docker activity
- Free up disk space
- Troubleshoot Docker issues

Although they aren't used as frequently as container or image commands, they're essential for maintaining a healthy Docker environment.