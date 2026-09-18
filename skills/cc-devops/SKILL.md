---
name: cc-devops
description: "DevOps configuration standards and generator guidelines for Dockerfile, Kubernetes, Helm, Ansible, Jenkinsfile, and Terraform."
---

# CC DevOps Skill

## Standards
1. **Multi-Stage Dockerfiles**: Use minimal base images (e.g. `python:3.12-slim`, `node:22-alpine`), run as non-root user (`USER appuser`), and clear cache layers.
2. **Kubernetes Manifests**: Specify explicit resource `requests` and `limits`, liveness/readiness probes, and security contexts (`readOnlyRootFilesystem: true`, `allowPrivilegeEscalation: false`).
3. **Helm Charts**: Maintain clean `values.yaml` defaults and explicit template validation.
4. **Terraform**: Follow modular structure (`main.tf`, `variables.tf`, `outputs.tf`), lock provider versions, and write native `.tftest.hcl` unit tests.
5. **CI/CD Pipelines**: Write declarative, reproducible Jenkinsfiles and GitHub Actions workflows with secret mask enforcement.
