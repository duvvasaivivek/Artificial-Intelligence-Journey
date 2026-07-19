# Verifying Docker Installation

After installing Docker Desktop, it's important to verify that everything is working correctly before creating or running containers.

We'll use a few simple CLI commands to check the installation.

---

# 1. Check Docker CLI

Run:

```bash
docker --version
```

Example Output:

```text
Docker version 28.3.2, build xxxxxxx
```

### What does it do?

It checks whether the Docker CLI is installed and accessible from your terminal.

If you see a version number, the CLI is installed correctly.

---

# 2. Check Docker Engine

Run:

```bash
docker info
```

This command displays information about:

- Docker Engine
- Number of Images
- Number of Containers
- Storage Driver
- CPU & Memory
- Operating System

If Docker Engine is running, you'll see detailed system information.

If it isn't, you'll likely get:

```text
Cannot connect to the Docker daemon...
```

Start Docker Desktop and try again.

---

# 3. Run Your First Container

Run:

```bash
docker run hello-world
```

If the image isn't available locally, Docker downloads it automatically.

Expected output:

```text
Hello from Docker!

This message shows that your installation appears to be working correctly.
```

---

# What Happens Internally?

When you run:

```bash
docker run hello-world
```

Docker performs these steps:

```text
1. Check if the image exists locally.
           │
           ▼
2. If not, download it from Docker Hub.
           │
           ▼
3. Create a container from the image.
           │
           ▼
4. Start the container.
           │
           ▼
5. Execute the program inside it.
           │
           ▼
6. Display the output.
           │
           ▼
7. Exit the container.
```

Notice that the container exits immediately because its task is complete.

---

# 4. Verify the Downloaded Image

Run:

```bash
docker images
```

Example:

```text
REPOSITORY     TAG       IMAGE ID
-----------------------------------------
hello-world    latest    xxxxxxxxx
```

This confirms that the image has been downloaded and stored locally.

---

# 5. Verify the Created Container

Run:

```bash
docker ps -a
```

Example:

```text
CONTAINER ID   IMAGE         STATUS
---------------------------------------------
abc123         hello-world   Exited (0)
```

Why **Exited**?

The `hello-world` program only prints a message and finishes, so the container stops automatically.

---

# Common Issues

### `docker: command not found`

The Docker CLI is not installed correctly or isn't added to your system's PATH.

---

### `Cannot connect to the Docker daemon`

Docker Desktop or Docker Engine is not running.

---

### `permission denied`

Common on Linux when the current user doesn't have permission to access Docker.

We'll cover Linux-specific setup later.

---

# Summary

To verify your Docker installation:

```bash
docker --version
docker info
docker run hello-world
docker images
docker ps -a
```

If all of these commands work as expected, your Docker environment is ready for the rest of the course.

---

# Hands-on Exercise

Run each command and answer:

1. Which command checks the Docker CLI?
2. Which command checks Docker Engine?
3. Which command downloads and runs an image?
4. Why does the `hello-world` container show an **Exited** status?
5. Can you find the `hello-world` image using `docker images`?

---

# Next Chapter

Now that Docker is installed and verified, we'll start using the **Docker CLI**, beginning with the structure of Docker commands and the most commonly used operations.