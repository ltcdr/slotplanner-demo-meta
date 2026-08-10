# Slotplanner Demo Meta Repository

This repository serves as the meta layer for coordinating releases, manifests, and version alignment across the Slotplanner-Demo-System. It provides a central place to manage release definitions, audit trails, deployment order, and references to all related service repositories.

---

## Purpose

The goal of this meta repository is to ensure reproducible, traceable, and well‑structured releases across multiple components of the Slotplanner demo environment. It acts as the single source of truth for:

- Release manifests
- Version mapping across services
- Deployment sequencing
- Rollback strategy definitions
- Audit and compliance documentation

---

## System Components & Related Repositories
Slotplanner is structured as a multi‑repository system to reflect real‑world release and delivery workflows.
This meta repository (slotplanner-demo-meta) coordinates all components and defines how they are released together:

[slotplanner-demo](https://github.com/ltcdr/slotplanner-demo)  
FastAPI backend and demo frontend providing the activity and booking workflow.
Versioned independently and included as a Git submodule.

[slotplanner-demo-functions](https://github.com/ltcdr/slotplanner-demo-functions)  
Azure Functions automation layer generating weekly demo activities and performing cleanup tasks.
Also versioned independently and included as a Git submodule.

These repositories form a distributed system with independent deployment units.
The meta repository provides unified versioning, deployment sequencing, and release documentation to ensure coordinated, reproducible releases across all services.

---

## Repository Structure

```
slotplanner-demo-meta/
│
├── services/
│   ├── slotplanner-demo/              # Git submodule
│   └── slotplanner-demo-functions/    # Git submodule
│
├── manifest/
│   └── R_000.XXX.yaml                 # Release definitions
│
└── docs/
    ├── release-process.md
    ├── rollback-strategy.md
    └── audit-trail.md
```

---

## Release Manifests

Each release is defined in a dedicated YAML file under `manifest/`.  
A manifest describes:

- Release identifier  
- Service versions included  
- Deployment order  
- Rollback strategy  
- Audit metadata  

Example:

```yaml
release: R_000.006
services:
  slotplanner-demo: R_000.006
  slotplanner-demo-functions: R_000.006
deployment-order:
  - slotplanner-demo-functions
  - slotplanner-demo
rollback:
  coordinated: true
audit:
  created_by: ltcdr
  date: 2026-08-06
```

---

## Environment Strategy

The Slotplanner demo system uses a staged release approach:

- **Development** – feature branches and early integration
- **Staging** – validation of coordinated service versions
- **Production** – finalized demo releases defined by manifest files

Environment configuration (backend URLs, Function App settings, identity
configuration) is managed per environment and aligned through the meta
repository to ensure consistent deployments across all services.

---

## Submodules
The services/ directory contains Git submodules pointing to the individual service repositories.
Clone this repository with:

```
git clone --recurse-submodules <repo-url>
```

This ensures all service versions referenced in the manifest are checked out correctly.

---

## CI/CD Integration

Releases defined in this meta repository are executed through GitHub Actions
pipelines using OIDC authentication. Each service repository contains its own
deployment workflow, while the meta repository provides:

- Version pinning for each coordinated release
- Deployment order definitions
- Release notes and audit metadata
- A single source of truth for cross‑service CI/CD execution

This structure ensures reproducible and traceable deployments across all
components of the Slotplanner demo system.

---

## Documentation
Additional documentation is located in the docs/ directory:

release-process.md — describes the release workflow

rollback-strategy.md — defines rollback procedures

audit-trail.md — outlines compliance and traceability requirements

---

## Release Lifecycle Overview

A typical release follows these steps:

1. Development work on feature branches  
2. Creation of a release branch (dev_r000.XXX_<task>)  
3. Version updates in service repositories  
4. Manifest creation in the meta repository  
5. Staging deployment for validation  
6. Production deployment following the defined deployment order  
7. Audit trail update and release documentation

This lifecycle ensures predictable, controlled, and well‑documented releases.

---

## Branching Strategy
Development for each release is performed on dedicated branches following the pattern:

```
dev_r000.XXX_<task>
```

Example: 

```
dev_r000.005_create_readme
```

---
