# ASG5: Containerized CI/CD with Docker and Amazon ECR

This folder contains a small Flask app and a CodeBuild buildspec that builds a Docker image and pushes it to a private Amazon ECR repository.

## Image

- Dockerfile: `Dockerfile`
- App port: `8080`
- Health endpoint: `/health`
- Image tags: the abbreviated source commit SHA and `latest`

## AWS setup

Create a private ECR repository named `asg5-container-demo`. Configure CodeBuild to use this repository's `main` branch, set its buildspec path to `asg5/buildspec.yml`, use an Amazon Linux standard image with privileged mode enabled, and grant its service role permission to authenticate and push images to that ECR repository.

Every successful build builds `asg5/Dockerfile` and pushes both tags. ECS deployment is intentionally not included; it is optional in the assignment and requires running compute resources.
