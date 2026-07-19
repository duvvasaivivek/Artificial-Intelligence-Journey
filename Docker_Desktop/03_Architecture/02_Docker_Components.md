# Docker Components

In the previous chapter, we saw Docker's overall architecture.

Now let's understand the role of each component.

Think of Docker as a team where every member has a specific responsibility.

---

# 1. Docker Client

The **Docker Client** is what you interact with.

It accepts Docker commands like:

```bash
docker run nginx
docker build .
docker pull ubuntu
```

The client **doesn't execute** these commands—it simply sends them to the Docker Engine.

---

# 2. Docker Engine

The **Docker Engine** is the heart of Docker.

It receives commands from the Docker Client and performs the actual work, such as:

- Building images
- Creating containers
- Starting containers
- Stopping containers
- Managing networks
- Managing volumes

Without the Engine, Docker cannot function.

---

# 3. Docker Images

A **Docker Image** is a read-only template used to create containers.

Think of it as a blueprint.

Examples:

```text
python:3.12
ubuntu:24.04
mysql:9
redis:8
```

One image can create multiple containers.

---

# 4. Docker Containers

A **Container** is a running instance of an image.

Example:

```text
Image
  │
  ├──► Container 1
  ├──► Container 2
  └──► Container 3
```

Containers are where your application actually runs.

---

# 5. Docker Volumes

Containers are temporary.

If a container is deleted, its data can be lost.

**Volumes** provide persistent storage so data survives even after containers are removed.

---

# 6. Docker Networks

Networks allow containers to communicate.

Example:

```text
Frontend
     │
     ▼
Backend
     │
     ▼
Database
```

Without a network, containers cannot talk to each other.

---

# 7. Docker Registry

A **Registry** stores Docker Images.

The default public registry is **Docker Hub**.

Examples:

```bash
docker pull nginx
docker pull python
```

If an image isn't available locally, Docker downloads it from the registry.

---

# Component Relationships

```text
Docker Client
       │
       ▼
Docker Engine
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
Images Containers Networks
       │
       ▼
    Volumes

Registry
   ▲
   │
Pull / Push Images
```

---

# Summary

| Component | Responsibility |
|-----------|----------------|
| Docker Client | Accepts user commands |
| Docker Engine | Executes commands |
| Images | Blueprint for containers |
| Containers | Run applications |
| Volumes | Persistent storage |
| Networks | Container communication |
| Registry | Stores images |

In the next chapter, we'll connect all of these together and see **what happens internally when you execute a Docker command like `docker run nginx`**.