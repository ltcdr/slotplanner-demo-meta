# Slotplanner Demo Meta Repository

This repository serves as the meta layer for coordinating releases, manifests, and version alignment across the Slotplanner-Demo-System. It provides a central place to manage release definitions, audit trails, deployment order, and references to all related service repositories.

## Purpose

The goal of this meta repository is to ensure reproducible, traceable, and well‑structured releases across multiple components of the Slotplanner demo environment. It acts as the single source of truth for:

- Release manifests
- Version mapping across services
- Deployment sequencing
- Rollback strategy definitions
- Audit and compliance documentation

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


## Submodules
The services/ directory contains Git submodules pointing to the individual service repositories.
Clone this repository with:

```
git clone --recurse-submodules <repo-url>
```

This ensures all service versions referenced in the manifest are checked out correctly.


## Service Repositories

This meta repository coordinates two service components of the Slotplanner demo system:

### slotplanner-demo
GitHub: https://github.com/ltcdr/slotplanner-demo  
The main web application providing the demo frontend and backend logic.

### slotplanner-demo-functions
GitHub: https://github.com/ltcdr/slotplanner-demo-functions  
Azure Functions backend providing API endpoints, background processing, and integration logic.

Both repositories are included as Git submodules under `services/` and are versioned independently.  
Release manifests in this meta repository define which versions of each service belong to a coordinated system release.


## Documentation
Additional documentation is located in the docs/ directory:

release-process.md — describes the release workflow

rollback-strategy.md — defines rollback procedures

audit-trail.md — outlines compliance and traceability requirements

## Branching Strategy
Development for each release is performed on dedicated branches following the pattern:

```
dev_r000.XXX_<task>
```

Example: 

```
dev_r000.005_create_readme
```
