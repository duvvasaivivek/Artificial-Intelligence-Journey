# Docker Desktop Tour

Now that Docker Desktop is installed and working, let's understand its interface.

Docker Desktop is a graphical interface (GUI) that helps you view and manage everything Docker is doing behind the scenes. Almost everything you do here can also be done using the Docker CLI, but the GUI makes it easier to visualize resources.

---

# Home

The Home screen gives a quick overview of Docker Desktop.

You'll typically see:

- Docker Engine status (Running / Stopped)
- Quick actions
- Recent containers
- Resource usage (depending on the version)

The most important thing here is ensuring **Docker Engine is running**.

---

# Containers

This tab lists every container on your machine.

For each container, Docker Desktop shows:

- Container Name
- Image Used
- Status (Running / Exited)
- Port Mapping
- CPU & Memory Usage
- Logs
- Terminal Access

Example:

```text
CONTAINER NAME     IMAGE          STATUS
------------------------------------------------
scholarium-api     python:3.12    Running
redis-server       redis:8        Running
mysql-db           mysql:9        Exited
```

From here you can:

- Start a container
- Stop a container
- Restart it
- Delete it
- Open Logs
- Open Terminal
- Inspect Details

---

# Images

The Images tab displays all Docker images stored locally.

Example:

```text
IMAGE
-------------------------
python:3.12
redis:8
mysql:9
hello-world
ubuntu
```

From here you can:

- Delete images
- Pull new images
- Build images
- Push images to Docker Hub

Remember:

> **Image = Blueprint**
>
> **Container = Running Instance**

---

# Volumes

Volumes store persistent data.

Here you can:

- View volumes
- Delete unused volumes
- Inspect stored data

We'll study volumes in detail later.

---

# Builds

Shows recently built images and build history.

Useful when working with Dockerfiles.

---

# Extensions

Docker Desktop supports plugins called **Extensions**.

Examples include:

- Kubernetes Dashboard
- Portainer
- LocalStack
- Database tools

Extensions are optional and not required for learning Docker.

---

# Settings

This is one of the most important sections.

Common settings include:

## Resources

Configure:

- CPU Cores
- Memory
- Disk Space

Example:

```text
CPU    : 4
Memory : 8 GB
Disk   : 100 GB
```

If Docker feels slow, this is usually the first place to check.

---

## General

Contains options like:

- Start Docker on Login
- Automatically check for updates
- Send usage statistics

---

## Docker Engine

Here you'll see Docker Engine's configuration in JSON format.

Example:

```json
{
  "builder": {
    "gc": {
      "enabled": true
    }
  }
}
```

Don't modify these settings unless you understand what they do.

---

## Kubernetes

Docker Desktop can run a local Kubernetes cluster.

Keep this **disabled** unless you're learning Kubernetes, as it consumes additional system resources.

---

# Notifications

Docker Desktop reports:

- Image downloads
- Build progress
- Container errors
- Update availability

Always check notifications if something doesn't work as expected.

---

# Searching Resources

The search bar helps you quickly find:

- Containers
- Images
- Volumes

This becomes useful when you have many Docker resources.

---

# Docker Desktop vs Docker CLI

Everything you do in Docker Desktop can also be done using the command line.

For example:

| Docker Desktop | Docker CLI |
|---------------|------------|
| Start Container | `docker start` |
| Stop Container | `docker stop` |
| Delete Container | `docker rm` |
| View Images | `docker images` |
| View Logs | `docker logs` |
| Open Terminal | `docker exec -it` |

Professional developers often prefer the CLI because it's faster and scriptable, while Docker Desktop is excellent for visualization and debugging.

---

# Summary

Docker Desktop provides a visual interface for managing Docker resources.

The most frequently used sections are:

- Containers
- Images
- Volumes
- Settings

As you learn Docker, you'll use Docker Desktop mainly to **observe** what's happening, while performing most operations through the CLI.

---

# Quick Revision

✔ Home → Docker Engine status

✔ Containers → Manage running applications

✔ Images → Manage downloaded and built images

✔ Volumes → Persistent data

✔ Builds → Build history

✔ Extensions → Optional plugins

✔ Settings → Docker configuration

---

# Hands-on Exercise

1. Open Docker Desktop.
2. Navigate through every tab.
3. Locate the **hello-world** image.
4. Check whether the **hello-world** container exists.
5. Open **Settings** and identify:
   - Allocated RAM
   - CPU cores
   - Disk size

Don't change any settings yet—just become familiar with the interface.

---

# Next Chapter

Next, we'll verify the installation using Docker CLI and start learning the commands you'll use every day.