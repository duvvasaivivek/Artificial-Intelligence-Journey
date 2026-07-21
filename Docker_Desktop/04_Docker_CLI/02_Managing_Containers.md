# Container Commands

Containers are the heart of Docker.

An **Image** is a blueprint.

A **Container** is a running instance of that blueprint.

This chapter covers the commands you'll use most often while working with containers.

---

# 1. Run a Container

```bash
docker run <image-name>
```

Example:

```bash
docker run nginx
```

This command:

1. Checks if the image exists locally.
2. Downloads it if necessary.
3. Creates a container.
4. Starts the container.

---

# Common Options

## Detached Mode

Run the container in the background.

```bash
docker run -d nginx
```

---

## Interactive Mode

Allows you to interact with the container.

```bash
docker run -it ubuntu
```

Example:

```text
root@container:/#
```

Useful for testing and debugging.

---

## Give a Custom Name

```bash
docker run --name my-nginx nginx
```

Instead of Docker generating a random name, the container will be named **my-nginx**.

---

## Port Mapping

```bash
docker run -p 8080:80 nginx
```

Meaning:

```text
Host Port      : 8080
Container Port : 80
```

You can now access Nginx using:

```text
http://localhost:8080
```

---

# 2. List Containers

Running containers only:

```bash
docker ps
```

Example:

```text
CONTAINER ID   IMAGE    STATUS
--------------------------------
ab12cd34       nginx    Up 2 minutes
```

---

All containers:

```bash
docker ps -a
```

This includes stopped containers.

---

# 3. Stop a Container

```bash
docker stop <container-name>
```

Example:

```bash
docker stop my-nginx
```

The container moves from **Running** to **Exited**.

---

# 4. Start a Container

Start an existing stopped container.

```bash
docker start my-nginx
```

---

# 5. Restart a Container

```bash
docker restart my-nginx
```

Equivalent to:

```text
Stop
 ↓
Start
```

---

# 6. Remove a Container

```bash
docker rm my-nginx
```

The container must be stopped before removing it.

To stop and remove in one command:

```bash
docker rm -f my-nginx
```

---

# 7. View Logs

Display the output produced by a container.

```bash
docker logs my-nginx
```

Useful for debugging applications.

---

# 8. Execute Commands Inside a Running Container

Open a terminal inside the container.

```bash
docker exec -it my-nginx bash
```

or

```bash
docker exec -it my-nginx sh
```

Example:

```text
root@container:/#
```

This lets you inspect files, install packages (temporarily), or debug the application.

---

# 9. Inspect a Container

View detailed information about a container.

```bash
docker inspect my-nginx
```

This returns information such as:

- Container ID
- IP Address
- Mounted Volumes
- Networks
- Environment Variables

The output is in JSON format.

---

# 10. View Resource Usage

Monitor CPU and memory usage.

```bash
docker stats
```

Example:

```text
CONTAINER     CPU %     MEMORY
-----------------------------------
nginx         0.10%     25 MB
redis         0.05%     12 MB
```

Press **Ctrl + C** to stop monitoring.

---

# Container Lifecycle

```text
docker run
      │
      ▼
Running
  │   │
  │   ├──────────────┐
  ▼                  ▼
Stop             Restart
  │                  │
  ▼                  ▼
Exited───────────────┘
  │
  ▼
Remove
```

---

# Commands Covered

| Command | Purpose |
|----------|---------|
| `docker run` | Create & start a container |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop` | Stop a container |
| `docker start` | Start a stopped container |
| `docker restart` | Restart a container |
| `docker rm` | Remove a container |
| `docker logs` | View logs |
| `docker exec` | Execute commands inside a container |
| `docker inspect` | Detailed container information |
| `docker stats` | Monitor resource usage |

---

# Summary

These are the container commands you'll use almost every day.

A typical workflow looks like this:

```text
Run
 ↓
List
 ↓
Inspect
 ↓
Logs
 ↓
Exec
 ↓
Stop
 ↓
Start / Restart
 ↓
Remove
```

Master these commands before moving on, as almost every Docker project relies on them.