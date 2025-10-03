# FastAPI EKS Application

A FastAPI application designed to run in Amazon EKS with automated Docker image builds and deployments to Amazon ECR.

## Features

- FastAPI web framework with automatic API documentation
- Health check endpoints
- Docker containerization
- GitHub Actions CI/CD pipeline
- Public Amazon ECR integration

## Running Locally with Docker

### Prerequisites

- Docker installed on your machine
- Docker daemon running

### Build the Docker Image

```bash
cd app
docker build -t fastapi-eks-app .
```

### Run the Container

```bash
docker run -d -p 8000:8000 --name fastapi-app fastapi-eks-app
```

### Access the Application

Once the container is running, you can access:

- **API Root**: http://localhost:8000
- **Swagger UI (Interactive API Docs)**: http://localhost:8000/docs
- **ReDoc (Alternative API Docs)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **API Info**: http://localhost:8000/api/info

### Stop and Remove the Container

```bash
docker stop fastapi-app
docker rm fastapi-app
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint with welcome message |
| `/health` | GET | Health check endpoint |
| `/api/info` | GET | Application information |
| `/docs` | GET | Swagger UI documentation |
| `/redoc` | GET | ReDoc documentation |

## GitHub Actions CI/CD

The project includes a GitHub Actions workflow that automatically:

1. Builds the Docker image
2. Pushes to Amazon ECR Public
3. Tags with git commit SHA and `latest`

### Required GitHub Secrets

Configure these secrets in your GitHub repository settings:

- `AWS_ROLE_ARN` - IAM role ARN for GitHub OIDC authentication
- `ECR_REGISTRY_ALIAS` - Your public ECR registry alias

### Workflow Triggers

- Push to `main` branch (when app/ files change)
- Pull requests to `main`
- Manual workflow dispatch

## AWS Setup

### Create ECR Public Repository

```bash
aws ecr-public create-repository \
    --repository-name fastapi-eks-app \
    --region us-east-1
```

### Configure GitHub OIDC with AWS

1. Create an OIDC identity provider in AWS IAM
2. Create an IAM role with trust policy for GitHub Actions
3. Attach ECR permissions policy to the role
4. Add the role ARN to GitHub secrets

## Local Development

### Install Dependencies

```bash
cd app
pip install -r requirements.txt
```

### Run Development Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── build-and-push.yml    # CI/CD pipeline
├── app/
│   ├── main.py                    # FastAPI application
│   ├── requirements.txt           # Python dependencies
│   └── Dockerfile                 # Container definition
└── README.md                      # This file
```

## License

MIT
