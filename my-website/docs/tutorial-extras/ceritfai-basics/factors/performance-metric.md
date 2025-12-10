---
title: "Performance Metric"
linkTitle: "Performance Metric"
description: >
  This page provides details about the Performance Metric trust factor in Cortex Certifai.
---

## What is a performance metric?

Performance Metrics are a measure of the model's predictive power, or the quality of the model's predictions. Performance metrics are user determined and defined trust factors that may be added in Certifai to track specific use case concerns.

In order for Certifai to calculate values for identified performance metrics the dataset used must contain an "outcome value" feature.

In addition to the main Certifai reports, you can optionally identify one or more additional performance metrics.

For the Banking:Loan Approval use case the optional performance metric configured is Accuracy.

If you have identified more than one performance metric you must identify which one to use in the ATX (AI Trust Index) calculation.

## Supported Performance Metric

Certifai can calculate the following metrics as part of the Performance Evaluation:
* Accuracy
* Recall
* Precision
* F1
* R-Squared

:::note

Certifai supports `micro`, `macro`, and `binary` variants of Recall, Precision, and F1. The default variant for each of
these metrics is `binary`.  To specify a variant of the listed metrics, you should place the variant within parenthesis.
For example, `Recall(micro)` specifies the micro variant of Recall, while `Recall` alone is equivalent to the the binary
variant of Recall.

:::

Other performance metrics can be included as part of the Performance Evaluation, but each model in the evaluation
must specify the corresponding metric value in the scan definition.
