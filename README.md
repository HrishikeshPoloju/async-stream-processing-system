
This project demonstrates a **distributed task processing system** using:

* **Python + Taskiq** for async task execution
* **NATS** as a messaging/broker queue
* **Multiple workers** for load balancing
* **Docker** for containerization
* **Kubernetes** for scaling and deployment

It showcases how **tasks are produced, queued, and consumed** in a **scalable, fault-tolerant environment**.

---

## **1️⃣ Core Components**

### **1. Producer**

* Sends tasks/messages to the **NATS broker**.
* Can be a **long-running service** or a **one-off job**.
* Example tasks: converting strings to uppercase, reversing strings, counting characters, repeating strings, etc.

### **2. NATS**

* Acts as a **message broker**, holding tasks in a queue until a worker consumes them.
* Supports **JetStream** for persistence (optional).
* Ensures **load balancing**: multiple workers can share tasks from the same queue.

### **3. Workers**

* Python processes running `worker.py`.
* Subscribe to the NATS queue.
* Execute tasks asynchronously.
* **Multiple workers** allow:

  * **Parallel processing** – tasks run concurrently.
  * **Load balancing** – tasks distributed across workers automatically.
  * **Fault tolerance** – if a worker crashes, others continue processing.

---

## **2️⃣ Tasks Implemented**

The project currently has **5 demo tasks**:

| Task Name        | Functionality                |
| ---------------- | ---------------------------- |
| `to_uppercase`   | Converts string to uppercase |
| `to_lowercase`   | Converts string to lowercase |
| `reverse_string` | Reverses the string          |
| `count_chars`    | Counts number of characters  |
| `repeat_string`  | Repeats the string twice     |

> Each task is **decorated with `@broker.task`** so Taskiq knows it’s executable by workers.

---

## **3️⃣ Docker Setup**

* **Docker** allows running NATS, workers, and producers as isolated containers.
* **Docker Compose** is used locally for testing.

### **How it works**

* NATS container listens on `4222` (client) and `8222` (monitoring).
* Each worker container subscribes to the NATS queue.
* Producer container sends tasks.
* Multiple worker containers allow **parallel execution** and **automatic load balancing**.

---

## **4️⃣ Kubernetes Deployment**

To run in production or at scale, we deployed everything in **Kubernetes (K8s)**.

### **Key Components in K8s**

1. **NATS Deployment + Service**

   * Runs NATS as a pod.
   * Service exposes NATS internally in the cluster.
2. **Worker Deployment**

   * Each worker is a pod.
   * Multiple replicas = multiple workers.
   * Automatically load balances tasks using NATS queues.
3. **Producer Job**

   * Producer runs as a one-time job or scheduled job.
   * Sends tasks to NATS.

---

### **K8s Benefits**

* **Scalability** – Increase worker replicas as needed.

  ```bash
  kubectl scale deployment taskiq-worker --replicas=5
  ```
* **Fault tolerance** – K8s restarts failed pods automatically.
* **Service discovery** – Workers and producers can find NATS via internal Service.
* **Rolling updates** – Update worker images without downtime.

---

## **5️⃣ How Tasks Flow**

```
Producer -> NATS Broker -> Multiple Worker Pods
```

1. Producer sends tasks/messages.
2. NATS queues the tasks.
3. Multiple workers consume tasks:

   * Tasks are distributed automatically.
   * Each worker executes tasks independently.
4. Workers print the results/log output.

---

## **6️⃣ Running Locally (Docker Compose)**

1. Start NATS:

```bash
docker-compose up -d
```

2. Start multiple workers:

```bash
python worker.py  # Terminal 1
python worker.py  # Terminal 2
```

3. Run producer:

```bash
python producer.py
```

* You’ll see tasks processed by multiple workers concurrently.

---

## **7️⃣ Running in Kubernetes**

1. Build Docker images for producer and worker:

```bash
docker build -f Dockerfile.worker -t hrish/taskiq-worker:latest .
docker build -f Dockerfile.producer -t hrish/taskiq-producer:latest .
```

2. Apply manifests:

```bash
kubectl apply -f k8s/nats-deployment.yaml
kubectl apply -f k8s/worker-deployment.yaml
kubectl apply -f k8s/producer-job.yaml
```

3. Check pods and logs:

```bash
kubectl get pods
kubectl logs <worker-pod-name>
```

* Tasks are automatically load-balanced across **worker replicas**.

---

## **8️⃣ Scaling Workers in K8s**

* To increase throughput, scale workers:

```bash
kubectl scale deployment taskiq-worker --replicas=5
```

* Tasks are automatically distributed across **all worker pods**.

---

## **9️⃣ Summary**

* This project demonstrates a **distributed task processing system**.
* **Multiple workers** handle tasks concurrently and balance load automatically.
* Docker and Kubernetes make it **scalable, resilient, and production-ready**.
* K8s provides **replicas, load balancing, self-healing, and service discovery** without manual intervention.
* You can extend it by adding more tasks, more workers, or even multiple NATS servers for high availability.
