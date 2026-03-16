# CLAUDE.md

This file defines how Claude Code should work inside the AIryss
repository.

Claude must follow the architecture and rules described here.

------------------------------------------------------------------------

# Project Overview

AIryss is a browser-based AI collaborative IDE platform.

The goal is to allow a human developer to collaborate with AI agents to
implement code safely and incrementally.

The system is **human-governed**, meaning the human is always the final
authority.

------------------------------------------------------------------------

# Core Roles

AIryss separates AI responsibilities into two agents.

## Human

Human is the final authority.

Responsibilities:

-   define requirements
-   approve changes
-   review diffs
-   approve commits
-   manage releases

AI must never bypass human approval.

------------------------------------------------------------------------

## Iryss (Implementation Agent)

Iryss is responsible for **code implementation tasks**.

Responsibilities:

-   reading repository code
-   generating patches
-   modifying files
-   refactoring
-   suggesting tests
-   generating commit drafts
-   generating pull request drafts

Iryss **must not directly merge code**.

------------------------------------------------------------------------

## Aryss (Architecture Review Agent)

Aryss is responsible for **design reasoning and review**.

Responsibilities:

-   requirement clarification
-   architecture review
-   implementation strategy comparison
-   risk analysis
-   reviewing Iryss patches

Aryss should not directly modify code.

------------------------------------------------------------------------

## AIryss

AIryss is the orchestration platform that connects Human, Iryss and
Aryss.

Responsibilities:

-   browser IDE
-   session management
-   workspace lifecycle
-   git integration
-   audit logging

------------------------------------------------------------------------

# Repository Structure

    apps/
    web/ frontend (Next.js planned)
    api/ backend (FastAPI planned)

    workers/
    workspace-runner/

    infra/
    nginx/
    postgres/
    redis/
    workspace-images/

    prompts/
    iryss/
    aryss/

    docs/
    architecture/
    api/
    infra/

Claude must follow this structure.

Do not introduce unrelated directories.

------------------------------------------------------------------------

# Code Modification Rules

Claude must follow these rules when editing code.

## 1 File Replacement Forbidden

Claude must **never rewrite entire files** when modifying code.

Only patches should be generated.

------------------------------------------------------------------------

## 2 Patch Format

All code modifications must be produced using **Unified Diff format**.

Example:

    --- a/file.py
    +++ b/file.py
    @@
    old line
    +new line

Patches are applied using:

    git apply

------------------------------------------------------------------------

## 3 Human Approval Required

Every patch must be:

1.  generated
2.  shown as diff
3.  reviewed by human
4.  approved
5.  applied

Claude must not skip this process.

------------------------------------------------------------------------

# Workspace Model

Development runs inside Docker containers.

Workspace container format:

    workspace_<project_id>

Filesystem layout:

    /workspace
    /project
    /tmp

Example command:

    docker exec workspace_001 php artisan test

------------------------------------------------------------------------

# Verify Mode

After patch application, verification commands must run.

Allowed commands for Laravel MVP:

    php artisan test
    php artisan route:list
    composer pint --test

Claude must not execute arbitrary commands.

------------------------------------------------------------------------

# Git Workflow

Standard workflow:

    create branch
    generate patch
    show diff
    human approval
    apply patch
    verify
    commit

Claude should assist with:

-   commit message generation
-   PR draft generation

Claude must **not perform merge automatically**.

------------------------------------------------------------------------

# Development Guidelines

Claude should prefer:

-   minimal changes
-   readable code
-   incremental improvements
-   preserving existing architecture

Avoid:

-   large refactors
-   speculative features
-   dependency explosions

------------------------------------------------------------------------

# Important Principle

AIryss is **human-governed AI development**.

Claude is an assistant, not an autonomous developer.