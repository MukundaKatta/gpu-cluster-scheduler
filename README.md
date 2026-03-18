# Gpu Cluster Scheduler

Intelligent GPU workload scheduler with fair-share

## Features

- Api
Cost - Tracker
Monitoring - Utilization
Resources - Gpu Manager
Resources - Spot Manager
Scheduler - Fair Share
Scheduler - Preemption
Scheduler - Priority Queue

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/gpu-cluster-scheduler.git
cd gpu-cluster-scheduler
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
gpu-cluster-scheduler/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
