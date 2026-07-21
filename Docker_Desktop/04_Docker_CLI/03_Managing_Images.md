# Image Commands

Docker Images are the foundation of containers.

A container cannot exist without an image.

This chapter covers the commands used to download, view, manage, and remove Docker images.

---

# 1. Download an Image

```bash
docker pull <image-name>
```

Example:

```bash
docker pull nginx
```

Docker downloads the latest version of the image from Docker Hub.

You can also specify a version (tag):

```bash
docker pull python:3.12
```

---

# 2. List Images

```bash
docker images
```

Example:

```text
REPOSITORY   TAG      IMAGE ID       SIZE
---------------------------------------------
nginx        latest   a8758716...    192MB
python       3.12     b75c3a...      1.02GB
ubuntu       latest   c34ab2...      78MB
```

This shows all images stored on your local machine.

---

# 3. Remove an Image

```bash
docker rmi <image-name>
```

Example:

```bash
docker rmi nginx
```

You can also remove using the Image ID.

```bash
docker rmi a8758716
```

> **Note:** You cannot remove an image if it's being used by a container.

---

# 4. Tag an Image

Tags help identify different versions of the same image.

```bash
docker tag <source-image> <new-image>
```

Example:

```bash
docker tag my-app:latest my-app:v1
```

Now both tags point to the same image.

---

# 5. Push an Image

Upload an image to Docker Hub or another registry.

```bash
docker push <image-name>
```

Example:

```bash
docker push username/my-app:v1
```

The image must be tagged correctly before pushing.

---

# 6. Image History

View how an image was built.

```bash
docker history <image-name>
```

Example:

```bash
docker history nginx
```

This displays the image layers created during the build process.

---

# 7. Inspect an Image

Get detailed information about an image.

```bash
docker image inspect <image-name>
```

Example:

```bash
docker image inspect nginx
```

Information includes:

- Image ID
- Creation Date
- Architecture
- Environment Variables
- Layers

The output is in JSON format.

---

# Image Workflow

```text
Docker Hub
     │
     ▼
docker pull
     │
     ▼
 Local Image
     │
     ├─────────────┐
     ▼             ▼
docker tag    docker run
     │             │
     ▼             ▼
docker push   Container
     │
     ▼
Docker Hub
```

---

# Commands Covered

| Command | Purpose |
|----------|---------|
| `docker pull` | Download an image |
| `docker images` | List local images |
| `docker rmi` | Remove an image |
| `docker tag` | Create a new tag |
| `docker push` | Upload an image |
| `docker history` | View image layers |
| `docker image inspect` | View image details |

---

# Summary

Images are reusable templates from which containers are created.

A typical image workflow is:

```text
Pull
 ↓
View
 ↓
Tag
 ↓
Run
 ↓
Push (Optional)
 ↓
Remove (If No Longer Needed)
```

Understanding image commands is essential before learning how to build your own images using **Dockerfiles**, which is the next major step in your Docker journey.