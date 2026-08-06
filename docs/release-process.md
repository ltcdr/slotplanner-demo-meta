# Slotplanner Demo – Release Process

This document defines the standardized release workflow for the Slotplanner-Demo-System.  
It focuses on the operational steps required to prepare, coordinate, and finalize a release across
multiple service repositories.

Structural details (repository layout, branching strategy, and component overview) are documented in
the main `README.md` and must be considered authoritative.

---

## 1. Overview

The Slotplanner Demo system consists of multiple coordinated service repositories.  
Releases are managed centrally through this meta repository, which provides:

- Release manifests
- Deployment sequencing
- Rollback coordination
- Audit documentation

The goal is to ensure reproducible, traceable, and controlled releases.

---

## 2. Release Identification

Each release is assigned a unique identifier:

R_000.XXX


Example:

R_000.005


This identifier is used consistently across:

- service repository tags  
- manifest filenames  
- development branches  
- audit entries  

---

## 3. Development Workflow

All development work for a release is performed on dedicated branches.

The naming pattern and rules are defined in `README.md` under **Branching Strategy**.

General workflow:

1. Create a new development branch for a specific task  
2. Implement the change  
3. Commit and push  
4. Open a Pull Request  
5. Ensure all checks pass  
6. Merge into `main`  

No direct commits to `main` are allowed.

---

## 4. Preparing a Release

Before creating a release manifest:

1. Ensure the repository structure matches the layout defined in `README.md`  
2. Ensure all service repositories have tagged versions for the release  
3. Ensure all development branches for the release have been merged  
4. Ensure documentation in `docs/` is up to date  

---

## 5. Version Alignment

Each service repository must provide a release tag matching the release identifier.

Example:

- `slotplanner-demo` → tag `R_000.005`
- `slotplanner-demo-functions` → tag `R_000.005`

These tags are referenced in the manifest.

---

## 6. Creating the Release Manifest

A release manifest is created under:

manifest/R_000.XXX.yaml


The manifest contains:

- Release identifier  
- Service versions  
- Deployment order  
- Rollback strategy reference  
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


## 7. Pull Request Requirements
All release-related changes must be merged through a Pull Request.

Requirements:

- PRs must reference the release identifier
- PRs must contain only the intended task
- All automated checks must pass
- Reviews are optional unless required by repository rules
- main must remain protected

---

## 8. Deployment Workflow
Deployment must follow the order defined in the manifest.

General rule:

- Deploy backend (slotplanner-demo-functions)
- Deploy frontend (slotplanner-demo)

This ensures backend availability before frontend rollout.

Deployment steps:

- Validate release manifest
- Deploy services in order
- Verify system health
- Update audit trail

---

## 9. Rollback Procedure
Rollback strategy is documented in docs/rollback-strategy.md.

The release manifest may include additional rollback metadata, but the detailed rollback steps
are maintained exclusively in the rollback strategy document to avoid duplication.

---

## 10. Audit Requirements
Audit documentation is maintained in docs/audit-trail.md.

Each release must include:

- Release identifier
- Manifest file
- Author
- Date
- PR references
- Deployment confirmation

---

## 11. Finalization
A release is considered complete when:

- Manifest is finalized
- All tasks are merged
- Deployment is executed
- Audit trail is updated
- Release tag is created in the meta repository

---
