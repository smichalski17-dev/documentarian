---
title: "Robustness"
linkTitle: "Robustness"
description: >
  This page provides details about robustness trust factor in Cortex Certifai.
---

## What is Robustness?

Robustness is one of the output visualizations provided for scan results in Certifai.
Certifai scans analyze one or more models using the same or comparable datasets.

Robustness is a measure of how well a model retains a specific outcome given small changes in data feature values.  

Changes to data and, therefore, robustness is of particular concern in AI systems because data changes can be introduced in two harmful ways: maliciously, in the form of data breaches or users gaming the system, and unintentionally when prediction inputs diverge from training data.

A robust model will tend to result in the same prediction regardless of small changes in the input values.

## How is robustness measured in Certifai?

To arrive at the values displayed in the robustness graph, Certifai takes a given dataset and generates counterfactuals for the data points.

A counterfactual for a given data point is a similar datapoint that has been changed enough to receive a different prediction or outcome from the model.

Counterfactual data points are created using a proprietary genetic algorithm designed at CognitiveScale.

The robustness value is then a measure of the distance points must move in order to change their predictions.

For instance in the “Banking:Loan Approval” example robustness is a measure of the amount of change required to move the result from granted to denied or denied to granted over all points in the data set.

## How is robustness calculated?

To arrive at the robustness score, counterfactuals are generated for the feature values of the dataset; then the distance from the feature value to the counterfactual is calculated for each record in the dataset.

These distances are averaged and normalized to determine the score that quantifies each model’s robustness.

A higher score indicates a more robust model.

## What is the importance of robustness?

The following actions might be taken by the various Certifai users viewing the reports for the Banking: Loan Approval use case:

- **Data scientists** might select the model with the highest robustness score as a candidate for further development. Conversely, they might choose a model with a lower score to work with in order to make the model more robust.

- **Business decision-makers** might recommend that the model with the highest score be selected for production level use.

- **Compliance officers** might approve models that meet a certain threshold of robustness for use in production use cases.

## How is robustness displayed in Certifai?

Robustness scores for each model are displayed in a bar graph that affords the comparison across the models in the scan definition.
