# Slotplanner Demo – Rollback Strategy

This document defines the rollback strategy for coordinated releases of the Slotplanner-Demo-System.
It describes the minimal required steps to revert a release safely and consistently across all
service repositories.

---

## 1. Purpose

Rollback ensures the system can be returned to a previously stable release if deployment issues
occur. Rollback must always be coordinated across all services.

---

## 2. Prerequisites

- Previous release tags must exist in all service repositories  
- The release manifest for the previous version must be available  
- Deployment order must be known (see manifest)  

---

## 3. Rollback Order

Rollback follows the **reverse deployment order**:

1. Roll back `slotplanner-demo`  
2. Roll back `slotplanner-demo-functions`  

This ensures the frontend does not reference newer backend functionality.

---

## 4. Rollback Steps

1. Identify the previous release identifier  
2. Check out the corresponding tags in both service repositories  
3. Redeploy services in rollback order  
4. Verify system health  
5. Update the audit trail with rollback details  

---

## 5. Manifest Reference

The release manifest may include rollback metadata (e.g., coordinated: true), but the detailed
rollback procedure is defined exclusively in this document.

---
