# Docker Networking

Containers are isolated from each other by default.

To allow containers to communicate with each other—or with the outside world—Docker provides **Networks**.

A Docker Network acts like a bridge that connects containers.

---

# Why Do We Need Networking?

Imagine a web application with three containers:

- Frontend
- Backend
- Database

```text
Frontend
    │
    ▼
Backend
    │
    ▼
Database
```

Without networking, these containers wouldn't be able to exchange data.

---

# Default Bridge Network

When you create a container, Docker automatically connects it to the **bridge** network.

```bash
docker run nginx
```

The container is attached to the default bridge network unless you specify another network.

View available networks:

```bash
docker network ls
```

Example:

```text
NETWORK ID     NAME      DRIVER
-----------------------------------
abc123         bridge    bridge
xyz456         host      host
pqr789         none      null
```

---

# Types of Docker Networks

## Bridge Network

- Default network
- Allows containers on the same bridge to communicate
- Best for single-host applications

---

## Host Network

The container shares the host machine's network.

No separate network namespace is created.

Useful when maximum network performance is needed.

---

## None Network

The container has **no network access**.

Useful for highly isolated workloads.

---

# Port Mapping

Containers have their own internal ports.

To access an application from your computer, map a host port to a container port.

```bash
docker run -p 8080:80 nginx
```

Meaning:

```text
Host (Your Computer)
Port 8080
      │
      ▼
Container
Port 80
```

Now you can access the application at:

```text
http://localhost:8080
```

---

# Custom Networks

Instead of using the default bridge network, you can create your own.

Create:

```bash
docker network create my-network
```

Connect a container:

```bash
docker run --network my-network nginx
```

Custom networks are recommended when multiple containers need to communicate.

---

# Useful Commands

List networks:

```bash
docker network ls
```

Inspect a network:

```bash
docker network inspect bridge
```

Remove a network:

```bash
docker network rm my-network
```

---

# Summary

- Docker Networks allow containers to communicate.
- Every container is connected to a network.
- Docker provides three common network types:
  - Bridge
  - Host
  - None
- Port mapping (`-p`) exposes container ports to your host machine.
- Custom networks are preferred for multi-container applications.

In the next chapter, we'll see **how containers communicate with each other** using Docker Networks.