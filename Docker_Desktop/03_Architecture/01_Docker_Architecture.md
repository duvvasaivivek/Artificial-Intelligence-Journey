# Docker Architecture

Docker isn't a single program.

It's a collection of components that work together to build, run, and manage containers.

This overall design is called the **Docker Architecture**.

---

# High-Level Architecture

```text
                User
                  │
                  ▼
      Docker CLI / Docker Desktop
                  │
                  ▼
            Docker Engine
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Images      Containers    Networks
     │            │
     └──────Volumes────────┘
                  │
                  ▼
           Docker Registry
```

Every Docker operation flows through this architecture.

---

# Client-Server Model

Docker follows a **Client-Server Architecture**.

- **Client** → Accepts your commands.
- **Server (Docker Engine)** → Executes them.

Example:

```bash
docker run nginx
```

Flow:

```text
You
 │
 ▼
Docker CLI
 │
 ▼
Docker Engine
 │
 ▼
Container Runs
```

The CLI only sends the request.

The Docker Engine does the actual work.

---

# Core Components

Docker mainly consists of:

- Docker Client
- Docker Engine
- Images
- Containers
- Volumes
- Networks
- Docker Registry

We'll study each component in the next chapter.

---

# Why This Architecture?

Each component has a single responsibility.

For example:

- CLI → Takes commands
- Engine → Executes commands
- Images → Templates
- Containers → Run applications
- Volumes → Store data
- Networks → Connect containers
- Registry → Stores images

Separating responsibilities makes Docker modular, scalable, and easier to maintain.

---

# Summary

Docker Architecture defines how all Docker components work together.

Almost every Docker command follows this flow:

```text
User
   ↓
Docker CLI/Desktop
   ↓
Docker Engine
   ↓
Docker Resources
```

Understanding this architecture makes the rest of Docker much easier to learn because every command you run interacts with these components.