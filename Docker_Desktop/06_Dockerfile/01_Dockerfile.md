# Dockerfile

So far, we've used existing Docker images like:

```bash
docker run nginx
docker run python:3.12
```

But what if you want to Dockerize **your own application**?

That's where a **Dockerfile** comes in.

---

# What is a Dockerfile?

A **Dockerfile** is a text file that contains a set of instructions used by Docker to build an image.

Instead of manually installing dependencies and copying files, you describe everything in a Dockerfile.

Docker reads the file line by line and creates an image automatically.

---

# Why Do We Need a Dockerfile?

Without a Dockerfile, every developer would have to manually:

- Install dependencies
- Copy application files
- Configure the environment
- Start the application

A Dockerfile automates this entire process.

Once written, anyone can build the same image with a single command.

---

# Dockerfile Workflow

```text
Dockerfile
      │
      ▼
docker build
      │
      ▼
Docker Image
      │
      ▼
Docker Container
```

You write the Dockerfile once.

Docker builds an image from it.

Containers are then created from that image.

---

# Basic Dockerfile

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

Every line is called an **instruction**.

Docker executes these instructions from top to bottom.

---

# Common Dockerfile Instructions

## FROM

Specifies the base image.

```dockerfile
FROM python:3.12
```

Every Dockerfile starts with a `FROM` instruction.

---

## WORKDIR

Sets the working directory inside the container.

```dockerfile
WORKDIR /app
```

Equivalent to changing directories using `cd`.

---

## COPY

Copies files from your computer into the image.

```dockerfile
COPY . .
```

Syntax:

```dockerfile
COPY <source> <destination>
```

---

## RUN

Executes commands while building the image.

```dockerfile
RUN pip install -r requirements.txt
```

Used for:

- Installing packages
- Updating software
- Creating directories

---

## CMD

Specifies the default command that runs when the container starts.

```dockerfile
CMD ["python", "app.py"]
```

A Dockerfile can have only one effective `CMD`.

---

# How Docker Builds an Image

Docker processes each instruction one by one.

```text
FROM
  │
WORKDIR
  │
COPY
  │
RUN
  │
CMD
  │
Image Created
```

Each instruction contributes to the final image.

---

# Summary

- A Dockerfile is a blueprint for building Docker images.
- It contains a sequence of instructions executed by Docker.
- The most common instructions are:
  - `FROM`
  - `WORKDIR`
  - `COPY`
  - `RUN`
  - `CMD`
- A Dockerfile automates application packaging, making builds consistent and repeatable.

In the next chapter, we'll use `docker build` to create our own images and learn how Docker builds them efficiently using layers and caching.