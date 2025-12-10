---
title: "AI Trust Index"
linkTitle: "AI Trust Index"
description: >
  This page provides details about the ATX (AI Trust Index) score in Cortex Certifai.
---

## What is the ATX?

The AI Trust Index (ATX) is a mechanism that provides a
unified framework to detect, score and rate automated decisioning
models in terms of business risk as well as benefit.

ATX (AI Trust Index) is used to represent the risk and performance characteristics of an AI Model using a
single number. It is useful in evaluating the change in trust factors for a model over time.

## How is ATX calculated?

The ATX score is a weighted average of 4 scores: one for each of the trust
factors measured in Certifai.

Risk dimensions include:

- Robustness
- Fairness
- Explainability
- Performance Metric (when more than one performance metric is supplied, only one can be applied to the ATX score)

By default, each component gets the same weight. However if a certain factor is not relevant to a particular use-case, it can be given a weight of zero.

## What is the importance of ATX?

ATX captures the risk due to the existence of bias; lack of explainability and transparency; lack of robustness to environmental changes or data attacks; and risks from non-compliance, data quality, or data privacy issues.
