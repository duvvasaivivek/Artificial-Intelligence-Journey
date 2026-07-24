# Volumes and Bind Mounts

In the previous chapter, we learned that container data is temporary.

Docker provides two common ways to persist data:

- **Volumes**
- **Bind Mounts**

Both store data outside the container, but they work differently.

---

# Docker Volumes

A **Volume** is a Docker-managed storage location used to persist container data.

Docker creates and manages the volume automatically.

Example:

```bash
docker volume create my-volume
```

Mount it to a container:

```bash
docker run -v my-volume:/app/data nginx
```

Here:

- `my-volume` → Docker Volume
- `/app/data` → Path inside the container

Even if the container is removed, the data remains in the volume.

---

# Bind Mounts

A **Bind Mount** links a folder on your computer directly to a folder inside the container.

Example:

```bash
docker run -v C:\Projects\App:/app nginx
```

Linux/macOS:

```bash
docker run -v /home/user/app:/app nginx
```

Changes made:

- On your computer → appear inside the container.
- Inside the container → appear on your computer.

This makes bind mounts ideal for development.

---

# Anonymous Volumes

If you don't specify a volume name:

```bash
docker run -v /app/data nginx
```

Docker creates an **anonymous volume**.

It persists data, but Docker assigns it a random name, making it harder to manage.

---

# Volume vs Bind Mount

| Volume | Bind Mount |
|---------|------------|
| Managed by Docker | Managed by the Host OS |
| Stores data in Docker's storage | Uses any folder on your computer |
| Better for production | Better for development |
| Easy to back up and migrate | Easy to edit files directly |

---

# Common Commands

Create a volume:

```bash
docker volume create my-volume
```

List volumes:

```bash
docker volume ls
```

Inspect a volume:

```bash
docker volume inspect my-volume
```

Remove a volume:

```bash
docker volume rm my-volume
```

---

# When Should You Use What?

### Use Volumes

- Databases
- Production applications
- Persistent application data

### Use Bind Mounts

- Developing applications
- Editing source code
- Testing changes without rebuilding the image

---

# Summary

- **Volumes** are Docker-managed storage and are the preferred choice for persistent application data.
- **Bind Mounts** connect a host folder directly to a container and are ideal during development.
- **Anonymous Volumes** are automatically created when no volume name is provided.
- Choose the storage method based on your use case:
  - **Development → Bind Mounts**
  - **Production → Volumes**