# Dockerfile Best Practices

Writing a Dockerfile that works is good.

Writing one that is **small, fast, secure, and maintainable** is even better.

These practices are commonly followed in real-world projects.

---

# 1. Use Official Base Images

Start with trusted base images whenever possible.

```dockerfile
FROM python:3.12
```

Instead of:

```dockerfile
FROM random-user/python
```

Official images are maintained, tested, and regularly updated.

---

# 2. Use Specific Image Tags

Avoid:

```dockerfile
FROM python:latest
```

Prefer:

```dockerfile
FROM python:3.12
```

Specific versions make builds predictable and reproducible.

---

# 3. Keep Images Small

Smaller images:

- Build faster
- Download faster
- Use less storage
- Have a smaller attack surface

Whenever possible, use lightweight images like:

```dockerfile
FROM python:3.12-slim
```

---

# 4. Order Instructions Properly

Place instructions that change less frequently at the top.

Example:

```dockerfile
FROM python:3.12

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
```

This improves Docker's layer caching and speeds up rebuilds.

---

# 5. Use `.dockerignore`

Exclude unnecessary files from the build.

Example:

```text
.git
.venv
node_modules
__pycache__
```

This reduces build time and image size.

---

# 6. Don't Store Secrets

Never include sensitive information inside a Dockerfile.

Avoid:

```dockerfile
ENV PASSWORD=my_password
```

Use environment variables or secret management instead.

---

# 7. One Container, One Main Process

Each container should have a single primary responsibility.

For example:

- One container for the backend
- One for the database
- One for Redis

This makes applications easier to manage and scale.

---

# 8. Clean Up Unnecessary Files

Remove temporary files created during the build whenever possible.

This helps keep the final image smaller.

---

# Summary

Follow these simple rules:

- Use official images.
- Use specific image versions.
- Keep images lightweight.
- Order instructions for better caching.
- Use `.dockerignore`.
- Never store secrets.
- Keep one main process per container.
- Remove unnecessary files.

Following these practices results in Docker images that are faster, smaller, more secure, and easier to maintain.