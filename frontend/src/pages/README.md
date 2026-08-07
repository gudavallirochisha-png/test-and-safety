# Pages Folder (`frontend/src/pages`)

## Purpose & Responsibility
Contains top-level route view components. Pages orchestrate UI components, hooks, and store states for specific URL endpoints.

## Architectural Guidelines
- Each page maps cleanly to a client-side route defined in `routes/`.
- Delegate API logic to custom hooks (`hooks/`) and global state management to Zustand stores (`store/`).
- Phase 1 scope explicitly omits dashboard rendering and business logic execution.
