# AI Safety Agents (`agents/`)

## Subsystem Architecture
This directory houses specialized intelligent evaluation agents:

1. **`risk_agent/`**: XGBoost gradient boosted decision tree model for tabular seller and transaction fraud evaluation.
2. **`review_agent/`**: DistilBERT NLP classification model for toxicity, sentiment, and incentivized fake review detection.
3. **`authenticity_agent/`**: YOLO v8 visual object detection model for brand trademark misalignment and counterfeit inspection.

Each agent operates as an isolated module providing an asynchronous evaluation interface.
