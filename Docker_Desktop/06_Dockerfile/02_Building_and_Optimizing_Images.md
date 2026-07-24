# Building Images

Once you've written a Dockerfile, the next step is to build it into a Docker Image.

Docker uses the `docker build` command for this.

---

# Build an Image

```bash
docker build -t my-app .
```

### Breakdown

| Part | Meaning |
|------|---------|
| `docker build` | Build an image from a Dockerfile |
| `-t` | Assign a name (tag) to the image |
| `my-app` | Image name |
| `.` | Current directory (Build Context) |

---

# What is Build Context?

The last argument (`.`) is called the **Build Context**.

It tells Docker where to find:

- Dockerfile
- Source Code
- Configuration Files
- Dependencies

Example:

```bash
docker build -t my-app .
```

Docker uses everything inside the current folder while building the image.

---

# Build Process

When you run:

```bash
docker build -t my-app .
```

Docker performs the following steps:

```text
Dockerfile
      │
      ▼
Read Instructions
      │
      ▼
Execute One by One
      │
      ▼
Create Image Layers
      │
      ▼
Build Image
```

---

# Image Layers

Each Dockerfile instruction creates a new **layer**.

Example:

```dockerfile
FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

Produces:

```text
Layer 5 → CMD
Layer 4 → RUN
Layer 3 → COPY
Layer 2 → WORKDIR
Layer 1 → FROM
```

Layers make Docker efficient because they can be reused.

---

# Layer Caching

Docker rebuilds **only the layers that change**.

Example:

```dockerfile
FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
```

If you only modify your Python code:

```text
FROM      ✅ Cached
WORKDIR   ✅ Cached
COPY      ❌ Rebuilt
RUN       ❌ Rebuilt
```

Caching makes repeated builds much faster.

---

# Ignore Unnecessary Files

Sometimes your project contains files that shouldn't be copied into the image.

Examples:

- `.git`
- `node_modules`
- `__pycache__`
- `.venv`

Create a `.dockerignore` file:

```text
.git
.venv
node_modules
__pycache__
```

Docker skips these files during the build, resulting in smaller and faster images.

---

# Verify the Image

After building:

```bash
docker images
```

Example:

```text
REPOSITORY    TAG
------------------------
my-app        latest
```

Run it:

```bash
docker run my-app
```

---

# Summary

- Use `docker build` to create an image from a Dockerfile.
- `-t` assigns a name to the image.
- `.` specifies the build context.
- Docker executes the Dockerfile instruction by instruction.
- Every instruction creates a layer.
- Docker uses layer caching to speed up future builds.
- Use `.dockerignore` to exclude unnecessary files from the build.