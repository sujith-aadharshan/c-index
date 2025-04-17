# c-index
Compute the C-Index for evaluating prognostic models.

This project demonstrates how to compute the Concordance Index (C-Index) — a key performance metric used to evaluate survival or risk prediction models in healthcare and other time-to-event analysis applications.

Project Description

Survival analysis is widely used in biomedical research to predict the time until an event occurs (e.g., death, relapse). The Concordance Index (C-Index) measures the discriminative ability of a model — how well the model predicts who will experience the event sooner than others.

This Python-based project takes a sample dataset with survival times, censoring status, and predicted risk scores to calculate the C-Index using the lifelines library.

---

Technical Stack
Language: Python
Libraries:
pandas — for handling the dataset
lifelines — for survival analysis and C-Index calculation
