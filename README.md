# Python-app-project
Project working on deploying a python application from EKS cluster using git actions. 


Sprint 1: Project Setup and Local Testing

Tasks:
Create new Git repository.
Create project structure.

Tasks:
Write code for the python application
Write a Dockerfile for the Python application.
Test the Docker image locally with sample data.
Document the local testing process.

Tasks:
Create a "test" branch in the repository.
Establish a workflow for merging features into the test branch.

Sprint 2: GitHub Actions for Build and Local Testing Automation

Tasks:
Create a GitHub Actions YAML file for building the Docker image.
Test the GitHub Actions workflow locally.
Ensure successful builds in the test branch.

Tasks:
Integrate testing steps in the GitHub Actions workflow.
Include linting, unit tests, and other relevant checks.
Ensure successful local testing in the test branch.

Tasks:
Identify key components of the architecture (EKS, Docker registry, etc.).
Use a tool like draw.io or Lucidchart to create a visual diagram.
Include communication pathways and data flow.

Sprint 3: EKS Deployment Preparation

Tasks:
Create Kubernetes Deployment
Configure environment-specific settings
Test the deployment locally using kubectl

Tasks:
Extend the GitHub Actions YAML file for EKS deployment.
Configure GitHub Secrets for EKS credentials.
Test the EKS deployment workflow.

Sprint 4: Integration Testing and Finalizing Deployment

Tasks:
Create integration test cases.
Integrate integration tests into the GitHub Actions workflow.
Ensure successful integration testing in the test branch.

Tasks:
Implement health checks in the GitHub Actions workflow.
Add rollback steps in case of deployment failures.
Validate successful deployments in the test branch.

Sprint 5: Documentation and Continuous Improvement

Tasks:
Document the project structure, Docker setup, GitHub Actions workflows, and EKS deployment.
Include troubleshooting and FAQs.

Tasks:
Review and optimize GitHub Actions YAML files.
Ensure resource-efficient deployment.
Implement feedback received during testing.

Tasks:
Review the existing cloud architecture diagram.
Update the diagram to reflect the final state of the project.