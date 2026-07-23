# Docker Containers

A **Docker Container** is a **running instance of a Docker Image**.

While an image is a blueprint, a container is the actual application running from that blueprint.

---

# From Image to Container

The relationship is simple:

```text
Docker Image
      │
      ▼
Docker Container
```

Every container is created from an image.

Example:

```bash
docker run nginx
```

Docker uses the **nginx** image to create and start a container.

---

# One Image, Multiple Containers

A single image can create multiple containers.

```text
          nginx Image
         /     |      \
        ▼      ▼       ▼
 Container1 Container2 Container3
```

Each container runs independently.

Stopping one container doesn't affect the others.

---

# Container Lifecycle

A container moves through different states during its lifetime.

```text
Created
   │
   ▼
Running
   │
   ▼
Stopped (Exited)
   │
   ▼
Removed
```

A stopped container can be started again unless it has been removed.

---

# Containers are Ephemeral

Containers are designed to be temporary.

If a container is deleted, the data stored inside it is also deleted.

To keep data permanently, Docker provides **Volumes**, which we'll learn later.

---

# What's Inside a Container?

A running container contains:

- Application
- Runtime
- Dependencies
- Writable Layer

Unlike an image, a container has a **writable layer**, allowing it to create or modify files while running.

---

# Summary

- A container is a running instance of an image.
- Every container is created from an image.
- One image can create multiple containers.
- Containers have a lifecycle: **Created → Running → Stopped → Removed**.
- Containers are temporary by design, so persistent data should be stored using volumes.

The next chapter will compare **Docker Images** and **Docker Containers** side by side to clearly understand their differences.