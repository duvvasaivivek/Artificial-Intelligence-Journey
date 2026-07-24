# Container Communication

In the previous chapter, we learned how Docker networks connect containers.

Now let's see how containers communicate with each other.

---

# How Do Containers Communicate?

Containers can communicate **only if they are connected to the same Docker network**.

Example:

```text
Frontend
    │
    ▼
Backend
    │
    ▼
Database
```

If all three containers are on the same network, they can exchange data directly.

---

# Using Container Names

Docker automatically provides **DNS-based service discovery**.

Instead of using IP addresses, containers can communicate using their **container names**.

Example:

```bash
docker run -d --name backend --network my-network my-backend

docker run -d --name frontend --network my-network my-frontend
```

The frontend container can reach the backend using:

```text
http://backend:8000
```

No IP address is required.

---

# Why Not Use IP Addresses?

Container IP addresses can change whenever a container is recreated.

Container names remain consistent, making them the recommended way to communicate.

---

# Example Workflow

```text
User
  │
  ▼
Frontend
  │
  ▼
Backend
  │
  ▼
Database
```

- The user sends a request to the Frontend.
- The Frontend communicates with the Backend.
- The Backend reads or writes data to the Database.

Each service communicates through the Docker network.

---

# Inspect a Network

To see which containers are connected to a network:

```bash
docker network inspect my-network
```

Docker displays:

- Connected Containers
- Network Configuration
- IP Addresses
- Subnet Information

---

# Best Practices

- Use **custom networks** for multi-container applications.
- Communicate using **container names**, not IP addresses.
- Keep related services on the same network.
- Expose only the ports that need external access.

---

# Summary

- Containers communicate through Docker networks.
- Containers must be on the **same network** to communicate.
- Docker provides automatic DNS resolution using **container names**.
- Avoid using container IP addresses, as they can change.
- Custom networks make multi-container applications easier to manage and more reliable.