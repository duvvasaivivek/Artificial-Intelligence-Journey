# Installing Docker Desktop

So far, we've built the theoretical foundation:

- What is Docker?
- Why Docker was created
- What is Containerization?
- Containers vs Virtual Machines

Now it's time to install Docker and prepare our system for the rest of this journey.

---

# What is Docker Desktop?

**Docker Desktop** is the easiest way to use Docker on your local computer.

It bundles together everything required to develop and run containers, including:

- Docker Engine
- Docker CLI
- Docker Compose
- Docker Desktop Dashboard
- Docker Extensions
- Kubernetes (Optional)

Instead of installing each component separately, Docker Desktop provides them as a single application.

> **Docker Desktop is an application. Docker Engine is the actual software that creates and runs containers.**

Think of it like this:

```
Docker Desktop
│
├── Docker Engine
├── Docker CLI
├── Docker Compose
├── Dashboard (GUI)
└── Additional Tools
```

---

# Docker Desktop vs Docker Engine

Many beginners think these are the same thing.

They are not.

| Docker Desktop | Docker Engine |
|----------------|---------------|
| Desktop application | Core container runtime |
| Includes graphical interface | No graphical interface |
| Includes Docker CLI | Executes Docker commands |
| Includes Docker Compose | Creates and manages containers |
| Mainly for development | Used in development and production |

A simple analogy:

```
VS Code  → Docker Desktop

Python Interpreter → Docker Engine
```

You write Python in VS Code, but Python executes the code.

Similarly,

Docker Desktop provides the interface,

while Docker Engine performs the actual work.

---

# System Requirements

Before installing Docker Desktop, ensure your system meets the following requirements.

## Windows

- Windows 10 or Windows 11 (64-bit)
- Hardware Virtualization Enabled
- WSL 2 Installed
- At least 4 GB RAM (8 GB or more recommended)

## macOS

- macOS 12 or later
- Apple Silicon or Intel Processor

## Linux

Linux users generally install Docker Engine directly instead of Docker Desktop, although Docker Desktop is also available.

---

# Why Does Docker Desktop Require Virtualization?

Earlier, we learned that containers share the host operating system's kernel.

So why is virtualization needed on Windows?

Because Docker containers are built around the Linux kernel.

Windows uses the Windows kernel.

To solve this mismatch, Docker Desktop creates a lightweight Linux environment using **WSL 2 (Windows Subsystem for Linux)**.

```
Windows
    │
WSL 2
    │
Linux Kernel
    │
Docker Engine
    │
Containers
```

Without WSL 2, Linux containers cannot run efficiently on Windows.

---

# Installing Docker Desktop

## Step 1

Download Docker Desktop from the official Docker website.

Choose the installer for your operating system.

---

## Step 2

Run the installer.

During installation, Docker Desktop may ask you to enable:

- WSL 2
- Virtual Machine Platform
- Hyper-V (on supported editions)

Accept the recommended options.

---

## Step 3

Restart your computer if prompted.

---

## Step 4

Launch Docker Desktop.

The first startup may take a minute while Docker initializes its components.

---

# Verifying the Installation

Open a terminal or Command Prompt.

Run:

```bash
docker --version
```

Example output:

```text
Docker version 28.x.x
```

Now check whether Docker Engine is running.

```bash
docker info
```

If Docker is running successfully, you'll see detailed information about:

- Docker Engine
- Containers
- Images
- Storage Driver
- Operating System
- CPU
- Memory

If Docker Desktop isn't running, you'll see an error similar to:

```text
Cannot connect to the Docker daemon
```

Simply start Docker Desktop and try again.

---

# Your First Docker Command

Run:

```bash
docker run hello-world
```

What happens?

1. Docker checks whether the **hello-world** image exists locally.
2. If it doesn't exist, Docker downloads it automatically.
3. Docker creates a container from that image.
4. The container runs.
5. It prints a welcome message.
6. The container exits because its job is complete.

Output:

```text
Hello from Docker!

This message shows that your installation appears to be working correctly.
```

Congratulations!

You've just run your first Docker container.

---

# What Happened Behind the Scenes?

When you executed:

```bash
docker run hello-world
```

Docker internally performed the following steps:

```
docker run hello-world
        │
        ▼
Check Local Images
        │
        ▼
Image Found?
   │
 ┌─┴──────────┐
 │            │
Yes          No
 │            │
 │       Download Image
 │            │
 └──────┬─────┘
        ▼
Create Container
        ▼
Start Container
        ▼
Run Program
        ▼
Display Output
        ▼
Exit Container
```

You didn't manually download anything.

Docker handled everything automatically.

---

# Common Installation Issues

## Docker Desktop won't start

Possible causes:

- Virtualization disabled
- WSL 2 not installed
- Outdated Windows version

---

## "docker" command not found

Usually indicates:

- Docker Desktop isn't installed correctly.
- PATH environment variable wasn't updated.
- Terminal needs to be restarted.

---

## Cannot connect to Docker daemon

This usually means Docker Engine isn't running.

Simply open Docker Desktop and wait until it finishes starting.

---

# Summary

Docker Desktop provides everything needed to develop and run containers on your local machine.

It includes Docker Engine, Docker CLI, Docker Compose, and a graphical dashboard.

On Windows, Docker Desktop uses WSL 2 to provide a Linux kernel, allowing Linux containers to run efficiently.

After installation, the `docker run hello-world` command confirms that everything is working correctly.

---

# Key Takeaways

- Docker Desktop is a complete development environment for Docker.
- Docker Engine is the component that actually creates and runs containers.
- Windows uses WSL 2 to run Linux containers.
- `docker --version` checks the Docker CLI installation.
- `docker info` checks whether Docker Engine is running.
- `docker run hello-world` verifies the complete Docker installation.

---

# Hands-on Exercise

Run the following commands one by one:

```bash
docker --version
```

```bash
docker info
```

```bash
docker run hello-world
```

Observe the output.

Try to identify which part of the workflow each command is verifying.

---

# Think Before Moving On

After running `docker run hello-world`, ask yourself:

- Where did Docker get the **hello-world** image?
- Where is the image stored?
- What exactly is an image?
- How did Docker create a container from it?

These questions naturally lead us to the next chapter:

> **Docker Desktop Tour**, where we'll explore the interface and understand what Docker Desktop is showing behind the scenes.