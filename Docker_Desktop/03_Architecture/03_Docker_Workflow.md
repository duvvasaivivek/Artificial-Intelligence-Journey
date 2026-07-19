# Docker Workflow

You've learned Docker's architecture and its components.

Now let's connect everything together.

This chapter answers one question:

> **What happens internally when you execute a Docker command?**

We'll use the most common command:

```bash
docker run nginx
```

---

# Step 1 — Docker Client Receives the Command

You execute:

```bash
docker run nginx
```

The Docker CLI receives the command and sends it to the Docker Engine.

```text
You
 │
 ▼
Docker CLI
```

---

# Step 2 — Docker Engine Processes the Request

The Docker Engine checks whether the required image already exists locally.

```text
Docker Engine
      │
      ▼
Image Exists?
```

---

# Step 3 — Download the Image (If Needed)

If the image doesn't exist, Docker downloads it from the configured registry (Docker Hub by default).

```text
Image Not Found
       │
       ▼
Docker Hub
       │
       ▼
Download Image
```

If the image already exists, Docker skips this step.

---

# Step 4 — Create the Container

Docker creates a new container using the downloaded (or existing) image.

```text
Image
   │
   ▼
Container
```

Remember:

> **Images are templates. Containers are running instances of those templates.**

---

# Step 5 — Configure the Container

Before starting it, Docker sets up:

- Filesystem
- Network
- Environment Variables
- Volumes (if specified)

Everything the container needs is prepared automatically.

---

# Step 6 — Start the Container

Docker starts the application's main process.

```text
Container
     │
     ▼
Application Starts
```

If it's an Nginx image, the Nginx server starts.

If it's a Python application, Python starts.

---

# Complete Workflow

```text
docker run nginx
        │
        ▼
Docker CLI
        │
        ▼
Docker Engine
        │
        ▼
Image Available?
   │
 ┌─┴─────────┐
 │           │
Yes         No
 │           │
 │      Pull Image
 │           │
 └─────┬─────┘
       ▼
Create Container
       ▼
Configure Network
       ▼
Attach Volumes
       ▼
Start Application
       ▼
Running Container
```

---

# Other Common Workflows

## `docker build`

```text
Dockerfile
      │
      ▼
Docker Engine
      │
      ▼
Build Image
      │
      ▼
Store Image Locally
```

---

## `docker pull`

```text
Docker Hub
      │
      ▼
Download Image
      │
      ▼
Store Locally
```

---

## `docker push`

```text
Local Image
      │
      ▼
Docker Hub
```

---

## `docker stop`

```text
Running Container
        │
        ▼
Stop Main Process
        │
        ▼
Container Status = Exited
```

---

## Summary

Almost every Docker command follows this pattern:

```text
User
   │
   ▼
Docker CLI
   │
   ▼
Docker Engine
   │
   ▼
Docker Resources
(Images, Containers, Networks, Volumes)
```

The Docker CLI simply forwards commands.

The Docker Engine performs all the actual work behind the scenes.

Once you understand this workflow, every Docker command becomes much easier to reason about.