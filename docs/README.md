# OctoAcme Project Management Overview

This concise overview explains OctoAcme's approach to running cross-functional projects and points to the detailed process documents in this folder. Use this page to orient new teammates and find the deeper guides for initiation, planning, execution, release, risk management, retrospectives, and roles.

OctoAcme follows a lightweight, stage-gated lifecycle—Initiation → Planning → Execution → Release → Close & Retrospective—focused on delivering small, testable increments. Projects begin with a Project One-pager to define the problem, success metrics, stakeholders, and a high-level timeline. Planning breaks approved initiatives into a prioritized backlog with acceptance criteria, estimates, a Definition of Done, and a release/milestone map; risks and cross-team dependencies are captured in a Risk Register and surfaced during weekly syncs.

Roles are explicit to ensure clear ownership: Product Managers own outcomes and prioritize the backlog, Project Managers coordinate delivery and communication, Developers implement and test, QA validates acceptance, and stakeholders provide input and approvals. Work items use a standard backlog item template and a project board workflow (Backlog → Ready → In Progress → In Review → QA → Done). Pull requests are expected to be small, include issue links and acceptance criteria, run automated CI (tests, linting, security scans), and have at least one approval before merging.

Communication is cadence-driven: daily standups focus on progress and blockers, weekly delivery syncs cover progress/risks/dependencies, sprint demos show completed work, and monthly stakeholder updates summarize status. Escalation paths are defined (team → PM → Product Lead → Sponsor) and incident communications follow a structured triage and blameless retrospective. Quality assurance is integrated into the flow: unit and integration tests are expected, end-to-end smoke tests cover critical flows, CI includes security scanning, and manual QA is used when necessary. Pre-release gates require passing CI and security scans, draft release notes, and a rollback/mitigation plan; retrospectives convert learnings into tracked backlog action items to drive continuous improvement.

See also
- octoacme-project-initiation.md
- octoacme-project-planning.md
- octoacme-execution-and-tracking.md
- octoacme-release-and-deployment.md
- octoacme-retrospective-and-continuous-improvement.md
- octoacme-risks-and-communication.md
- octoacme-roles-and-personas.md