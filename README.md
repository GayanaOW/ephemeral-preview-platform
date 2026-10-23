# Automated Ephemeral Preview Environments Platform

An automated DevOps pipeline that spins up isolated, ephemeral Kubernetes environments for every Pull Request and destroys them upon closure, maintaining a $0 infrastructure cost.

## 🚀 Architecture & Tech Stack
* **Application:** FastAPI (Python), secured with multi-stage non-root container builds.
* **Orchestration:** Kubernetes (Minikube / Kind), Helm charts for parameterization.
* **CI/CD:** GitHub Actions (automated PR lifecycle management).

## 🔄 Workflow Lifecycle
1. **PR Opened / Updated:** GitHub Actions provisions a local cluster, builds the PR-specific container image, and deploys a dedicated Helm release (`pr-<number>`).
2. **Review & Test:** Isolated testing endpoint is verified via automated health probes.
3. **PR Closed:** GitHub Actions intercepts the closure webhook and purges the Helm release, preventing resource leaks.
