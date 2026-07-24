# Data Persistence

By default, **Docker containers are temporary (ephemeral)**.

This means that any data stored inside a container can be lost when the container is removed.

This behavior is one of the biggest differences between running an application directly on your computer and running it inside a container.

---

# The Problem

Imagine you're running a MySQL container.

```bash
docker run mysql
```

You create a database and insert thousands of records.

Everything works perfectly.

Now you remove the container:

```bash
docker rm mysql-container
```

Create a new container from the same image.

```bash
docker run mysql
```

Your database is gone.

Why?

Because the data was stored **inside the container**, and removing the container also removed its writable layer.

---

# Container Storage

Every container has its own writable layer.

```text
Docker Image
      │
      ▼
Container
      │
      ▼
Writable Layer
```

Any new files or changes made while the container is running are stored in this writable layer.

Once the container is deleted, this layer is deleted as well.

---

# What is Data Persistence?

**Data Persistence** means storing data in a way that it remains available even after an application or container is stopped, restarted, or removed.

Examples of persistent data include:

- Databases
- User uploads
- Log files
- Configuration files

This data should survive beyond the life of a single container.

---

# Why Do We Need Persistence?

Without persistence:

- Restarting a database would erase all records.
- Uploaded files would disappear.
- Logs would be lost.
- Every new container would start with empty data.

For many applications, this is unacceptable.

---

# The Solution

Docker provides dedicated storage mechanisms that exist **outside the container**.

This allows data to remain safe even if containers are recreated.

The two most common options are:

- **Volumes**
- **Bind Mounts**

We'll explore both in the next chapter.

---

# Summary

- Containers are **ephemeral** by default.
- Data stored inside a container's writable layer is lost when the container is removed.
- **Data Persistence** ensures important data survives container recreation.
- Docker solves this using **Volumes** and **Bind Mounts**, which store data outside the container.