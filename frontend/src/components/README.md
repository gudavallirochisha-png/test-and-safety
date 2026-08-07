# Components Folder (`frontend/src/components`)

## Purpose & Responsibility
Contains presentational and UI design system components adhering to the **Single Responsibility Principle (SRP)**.

## Architectural Structure
Organize components by atomic responsibility:
- `common/`: Reusable atomic UI elements (Buttons, Badges, Modals, Loaders, Risk Indicators).
- `risk/`: Components specific to tabular seller risk evaluation.
- `review/`: Components specific to NLP review toxicity analysis.
- `authenticity/`: Components specific to visual product authenticity assessment.

## Rules
- Components must be purely functional, controlled via explicitly typed TypeScript props (`types/`).
- Business logic or direct HTTP fetching should NOT take place inside primitive UI components (delegate to hooks/services).
