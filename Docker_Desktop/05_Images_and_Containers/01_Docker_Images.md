# Docker Images

A **Docker Image** is a **read-only template** used to create Docker containers.

It contains everything an application needs to run, including:

- Application Code
- Runtime
- Libraries
- Dependencies
- Configuration

Think of an image as a **blueprint**.

Just as a blueprint is used to build multiple houses, one Docker image can create multiple containers.

---

# Why Do We Need Images?

Imagine installing an application from scratch every time you wanted to run it.

You would need to:

- Install the programming language
- Install dependencies
- Configure the environment
- Copy the application code

Docker Images eliminate this repetition by packaging everything once and reusing it whenever needed.

---

# Image Structure

A Docker Image typically contains:

```text
Docker Image
│
├── Application
├── Runtime
├── Libraries
├── Dependencies
└── Configuration
```

Once built, an image becomes a reusable package.

---

# Image Layers

Docker Images are built using **layers**.

Each instruction in a Dockerfile creates a new layer.

Example:

```text
Layer 4 → Application Code
Layer 3 → Python Packages
Layer 2 → Python Runtime
Layer 1 → Ubuntu Base Image
```

This layered design makes Docker efficient because unchanged layers can be reused instead of being rebuilt.

We'll study layers in detail when we learn Dockerfiles.

---

# Read-Only Nature

A Docker Image cannot be modified while it's being used.

If changes are needed, Docker creates a new image rather than altering the existing one.

This ensures images remain consistent and reusable.

---

# Official vs Custom Images

### Official Images

Provided and maintained by trusted organizations.

Examples:

```text
python
nginx
ubuntu
mysql
redis
```

Download using:

```bash
docker pull python
```

---

### Custom Images

Images you build for your own applications.

Example:

```text
my-portfolio
scholarium
fraud-detector
```

These are created using a **Dockerfile**.

---

# Summary

- A Docker Image is a read-only template.
- Images contain everything required to run an application.
- One image can create multiple containers.
- Images are built using layers.
- Images can be official or custom.

The next chapter will show how these images become **running containers**.