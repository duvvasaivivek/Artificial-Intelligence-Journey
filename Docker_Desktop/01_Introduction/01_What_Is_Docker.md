# What Is Docker?

> "It works on my machine."

If you've ever built an application that worked perfectly on your computer but failed on someone else's, you've already experienced the problem Docker was created to solve.

In this chapter, we'll understand what Docker is, why it exists, and why it has become one of the most important technologies in modern software development.

---

# Motivation

Imagine you've spent weeks building a Python application.

Your project uses:

- Python 3.11
- NumPy
- Pandas
- FastAPI
- PostgreSQL
- Redis

Everything works perfectly on your laptop.

Now you send it to your friend.

They clone the repository and run it.

Instead of seeing your application, they see:

```text
ModuleNotFoundError: No module named 'fastapi'
```

They install FastAPI.

Another error appears.

```text
ModuleNotFoundError: No module named 'numpy'
```

They install NumPy.

Another error appears.

```text
Version conflict detected
```

After fixing several issues, they still can't run your project because their environment is different from yours.

This is one of the biggest challenges in software development.

Developers often say:

> **"It works on my machine."**

---

# The Problem

An application doesn't depend only on its source code.

It also depends on:

- Operating System
- Programming Language Runtime
- Libraries
- Dependency Versions
- Environment Variables
- Configuration Files
- External Services

If any one of these is different, the application may not work correctly.

So the real problem isn't just sharing code—it's sharing the **entire environment** in which the code runs.

---

# What Is Docker?

**Docker is an open-source containerization platform that allows developers to package an application along with all its dependencies, libraries, runtime, and configuration into a standardized unit called a container, ensuring the application runs consistently across different environments.**

Let's break this definition down.

- **Open Source** – Docker's source code is publicly available, allowing anyone to use, inspect, and contribute to it.

- **Containerization Platform** – Docker provides the tools and technology to create, manage, and run containers.

- **Package an Application** – Docker bundles your application together with everything it needs to run.

- **Dependencies** – Third-party libraries and packages required by the application.

- **Runtime** – The software required to execute your application, such as Python, Java, or Node.js.

- **Configuration** – Environment variables, settings, and other configuration files.

- **Standardized Unit** – Every Docker container follows a consistent format, making it portable and predictable.

- **Container** – An isolated environment that contains your application and everything required to execute it.

- **Runs Consistently** – Whether the container runs on your laptop, a teammate's computer, a testing server, or a cloud server, it behaves the same because the environment inside the container is identical.

---

# In Simple Words

Docker lets you **package your application together with everything it needs to run**, so it behaves the same wherever Docker is installed.

Instead of saying,

> "Here is my code. Install Python, install these libraries, configure the database, and hope it works."

you simply say,

> "Here is my Docker container. Run it."

That's the power of Docker.