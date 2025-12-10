---
title: "Explainability and Explanations"
linkTitle: "Explainability and Explanations"
description: >
  This page provides details about explainability trust factor in Cortex Certifai, and the optional explanations which illuminate the details of the explainability score.
---

## What are Explainability and Explanations?

Explainability measures the average simplicity of the counterfactual explanations provided for each model.

The Explanations report provides a record-by-record view of the actual input data values side-by-side with the counterfactual values, so viewers can observe the amount of change required to move from one outcome to another. The fewer feature values that must be changed to change the outcome of each record, the more explainable the model is.

The explanations report is run on an alternate dataset that is specified in the scan definition.  This report must generate counterfactuals for every row in the explanations dataset, so it may take some time to run for larger datasets.  

## How is explainability calculated?

The explainability score is the score assigned to capture the simplicity of counterfactual explanations for dataset observations. A single feature change is assigned a score of 100, and scores decrease as more feature values must be changed to alter the outcome.

## What is the importance of explainability and explanations?

The different types of viewers of the Certifai evaluations may use the Explanation report in different ways:

- **Data scientists** may use this report to spot check the records to make sure that the outcomes assigned make sense. For instance in the Banking:Loan Approval use case you would not expect that a larger counterfactual loan amount would move the result from Loan Denied to Loan Granted. If anomalies like this are present, then the model may have to be altered to be more accurate.

- **Business decision-makers** may use this report to get a closer look at why specific models perform the way they do. By knowing which features change the outcomes most often or how much certain features must change, business users can identify the model that best expresses their business’s goals and values. For instance in the Banking:Loan Approval example if changing from have no savings account to having one with just a hundred dollars often moves the result from Loan Denied to Loan Granted, they can help enable loan requesters by encouraging them to open savings accounts.

- **Compliance officers** may be interested in using Explainability to define thresholds for acceptability by observing the amount of change for specific features in the best and worst models.

## How is explainability displayed in Certifai?

The top of the report displays:

- The purpose of the prediction
- The target result for the counterfactual derived for the observation

The explainability histogram shows the distribution over the number of features that must be changed to alter the outcome. The number of changed features is  on the x-axis. The changed features for an explanation are the features that had counterfactual values assigned that altered the outcome.

A distribution skewed to the left with a higher score indicates fewer features must change to alter the outcome. Lower scores that are skewed to the right indicate more features’ values must change to alter the outcome.



## How are explanations displayed in Certifai?

In the first section, at the top of the report, the viewer makes selections that determine what information is displayed in the sections below.

- Select a model from the models defined in the scan definition.
- Select the observation one of two ways
    - move directly to a specific observation number by entering it in the search field
    - manually move through the dataset records one at a time by clicking the forward and back arrows

The second section of the report shows a table of the changed feature actions of the observed data point and the actual and counterfactual values. Changed features are features that may be altered in order to change the predicted outcome for the selected observation.
Table columns are as follows:

- The name of the dataset feature
- The original value for that feature as expressed in the dataset
- The counterfactual values for the feature that resulted in a change to the outcome

When you read this table you should look closely at features the algorithm changed and the delta or difference between the original and the counterfactual values. By analyzing this table, the viewer can gain insight into what features must change in order to change the prediction.

The third section of the Explanations report is a table of the remaining features of the dataset. The original data point values and because the counterfactual values are always the same they are designated "No change required".
