# Docker CLI Basics

So far, we've primarily interacted with Docker through Docker Desktop.

However, in real-world development, Docker is mostly used through the **Command Line Interface (CLI)**.

The CLI is faster, scriptable, and available on every machine—from your laptop to production servers.

---

# What is Docker CLI?

The **Docker Command Line Interface (CLI)** is a tool that lets you communicate with the Docker Engine using commands.

For example:

```bash
docker run nginx
```

Here, the CLI sends your request to the Docker Engine, which performs the actual work.

---

# Docker Command Structure

Almost every Docker command follows the same format:

```bash
docker <command> [options] [arguments]
```

Example:

```bash
docker run nginx
```

| Part | Description |
|------|-------------|
| `docker` | Docker CLI |
| `run` | Command |
| `nginx` | Argument |

Another example:

```bash
docker stop my-container
```

| Part | Description |
|------|-------------|
| `docker` | Docker CLI |
| `stop` | Command |
| `my-container` | Argument |

---

# Commands, Options & Arguments

A Docker command has three parts.

### Command

Defines the action.

Examples:

```bash
run
pull
build
stop
images
```

---

### Option (Flag)

Changes how the command behaves.

Examples:

```bash
-d
-it
-p
--name
```

Example:

```bash
docker run -d nginx
```

Here:

- `-d` → Run in detached mode (background).

---

### Argument

The resource the command acts on.

Example:

```bash
docker run nginx
```

`nginx` is the argument.

---

# Getting Help

Docker has built-in documentation.

General help:

```bash
docker --help
```

Help for a specific command:

```bash
docker run --help
```

or

```bash
docker image --help
```

Whenever you're unsure about a command, use `--help`.

---

# Docker Command Groups

Docker organizes commands into categories.

| Category | Examples |
|----------|----------|
| Containers | `run`, `ps`, `stop`, `start`, `exec` |
| Images | `pull`, `push`, `images`, `rmi` |
| Networks | `network` |
| Volumes | `volume` |
| System | `system`, `info`, `version` |

We'll explore each category in the upcoming chapters.

---

# Docker CLI vs Docker Desktop

| Docker CLI | Docker Desktop |
|------------|----------------|
| Command-line interface | Graphical interface |
| Faster | Easier for beginners |
| Scriptable | Manual interaction |
| Used in production | Mainly used during development |

Both communicate with the same Docker Engine.

---

# Summary

- Docker CLI is the primary way to interact with Docker.
- Every command follows the format:

```bash
docker <command> [options] [arguments]
```

- Commands perform actions.
- Options modify behavior.
- Arguments specify the target resource.
- Use `docker --help` whenever you need assistance.

From the next chapter onward, we'll start using Docker CLI to create, manage, and inspect containers.