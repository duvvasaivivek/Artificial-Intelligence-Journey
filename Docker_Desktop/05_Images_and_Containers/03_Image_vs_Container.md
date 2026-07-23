# Image vs Container

Images and Containers are closely related, but they are **not the same**.

A Docker Image is used to create a Docker Container.

Think of it like this:

```text
Blueprint  ─────────►  House
   │                     │
Image              Container
```

You can build many houses from one blueprint.

Similarly, you can create multiple containers from one image.

---

# Comparison

| Docker Image | Docker Container |
|--------------|------------------|
| Blueprint | Running instance |
| Read-only | Read & Write |
| Static | Dynamic |
| Used to create containers | Created from images |
| Doesn't execute | Executes the application |
| Stored locally or in a registry | Runs on the host machine |

---

# Relationship

```text
        Docker Image
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
Container1 Container2 Container3
```

One image can create any number of containers.

Each container runs independently.

---

# Example

Image:

```text
python:3.12
```

Create two containers:

```bash
docker run python:3.12
docker run python:3.12
```

Result:

```text
python:3.12 Image
        │
   ┌────┴────┐
   ▼         ▼
Container A  Container B
```

Both containers use the same image but have separate lifecycles.

---

# Quick Rule

- **Image = Template**
- **Container = Running Application**

You **build** an image.

You **run** a container.

---

# Summary

- Images and containers are different concepts.
- An image is a read-only template.
- A container is a running instance of an image.
- One image can create multiple independent containers.
- Images are built once and reused many times.

This distinction is fundamental to Docker and will become even more important when you start building your own images using **Dockerfiles**.