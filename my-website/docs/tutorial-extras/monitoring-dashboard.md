---
title: "Monitoring Dashboard"
linkTitle: "Monitoring Dashboard"
description: >
  This is a guide to understanding how to navigate through and understand the Certifai Monitoring Dashboard.
---

This is a guide to understanding how to navigate through and understand the Certifai Monitoring Dashboard.

Production models need to keep pace with new data collection and consumer preferences to prevent degradation of prediction and incorrect inference. To aid in your monitoring pipeline, we introduce Certifai’s new Monitoring Console and specifically the Monitoring Dashboard, where data and prediction trends can be easily viewed.

The Certifai Monitoring Dashboard is a tool you use to analyze data statistics and drift of new datasets as compared to the training data.

Certifai’s Monitoring Console enables users to keep track of data trends, explore data characteristics, and detect the presence of both feature drift and prediction label drift in data uploads. The information displayed in the Monitoring Dashboard allows you to evaluate model performance and detect drift, so that corrective actions may be taken.

## Prerequisites (Initial Release)

In the initial release your Cognitive Scale representative will assist you with the setup process for your Projects.

Access to public notebooks (link was here) that includes insights and instructions are also available in this initial release.

## Monitoring Console Navigation (Initial Release)

To open the Monitoring Console:

1. Log in to the Certifai launch page
2. Click the Account icon at the top right.
3. Select **RAI Center** from the menu.
4. Click the Account icon again.
3. Select **Monitoring Console** from the menu.

  ![Open the Monitoring Console](\img\open-monitoring-console.png)

4. The Monitoring Dashboard is displayed. Select a project from the dropdown menu at the top right.

  ![Select a Project](/img/monitoring-dashboard-select-project.png)

  In the Monitoring Dashboard the **Project** is the parent organizational object. Each Project has one or more **Models** (the **Model Version** is also displayed if one is provided in the model registration). To calculate monitored analytics, each Model must have a **Training or Reference Dataset** AND an **Evaluation or Monitored Dataset**. For other evaluations only the Monitored Dataset is required. To calculate the data statistics, the model's behavior using the Monitored Dataset is compared to its behavior using the Reference Dataset. The behaviors compared pertain to the following:

  - **(Compliance) Status**
  - **Data Drift**
  - **Data Quality**
  - **Performance**
  - **Fairness**

5. Click anywhere in the row of the Model to display the monitoring details.

The Data Drift thumbnail depicts the prediction drift, while the Data Quality thumbnails depicts the missing elements in the data. This is a generalized summary of the monitoring details and more details on these categories will be explained later on this page.

6. Set the date range for the graphical displays by selecting start and stop dates from the calendar widget to the right under the tabs. (Defaults to showing all available data)

  ![Select date range](/img/monitoring-dashboard-date-range.png)

7. View details and values on the graphs by hovering over the x-y intercepts.

  Two types of hover views are displayed:

    - When a single evaluation has been run for a given date this is the view:

      ![Hover to view values-single run](/img/md-hover-one-run.png)

    - When multiple evaluation runs have occurred on a given day, the Categorical Feature Distribution displays the top five values, determined by highest count in the range of dates provided, are expressed as "Worst Case". Depending on the graph being displayed, the Worst Case can vary. In the numeric quartile graphs, the Worst Case will be the scan where the IQR is the largest.

      ![Hover to view values-multiple runs](/img/md-hover-multi-runs.png)
fai
## Reading the Graphs - Visualization Types

Additional detail about the calculations described in this section are provided in the monitoring example notebook (link was here).

The different visualizations that are presented in the dashboard are described in this section.

### Drift visualizations

Depending on the type of learning task, regression or classification, the drift statistic will either be the univariate Kolmogorov-Smirnov test or the Chi-squared test, respectively.

The blue line represents the value of the statistic.
The red line represents the statistical threshold.
The red region depicts the drift region, which is determined by a statistical threshold with default confidence probability of 95% (alpha = 0.05).

If a prediction demonstrates drift, the value of the statistic (blue line) crosses the statistical threshold (red line).

Drift may cause a degradation in the model performance.

### Distribution Visualizations

Distribution visualizations are used for classification task types and categorical data features.

Two display options are provided for distribution visualizations: counts or percentages.

The distribution graphs are a pictorial representation of the proportions of the groups of the data for a particular feature/label. Substantial changes in value distribution in the data distribution suggests that the distribution of the features is getting larger, which could signal a potential degradation in the model performance.

When the distribution appears to vary widely, drift may be occurring, and action to revise your model or evaluate data is recommended.

### Quartile Visualizations

Quartile visualizations are used for regression task types and numeric data features.

The interquartile range (IQR), the region between 75% to 25% percentile, provides a depiction of the statistical dispersion of the data without the influence of outliers. This enables you to gauge the variability of the data.

## Compliance Status

One of the metrics displayed in the Project Models list is the Compliance Status. This value provides a rough evaluation of the Trust Factors' performance.  Users interacting with the models list can use this status to quickly evaluate which models they need to investigate and ultimately take action to correct.

Compliance statuses indicate the following:

- **NONE**: There is no policy configured for the model version. (usually because there is no dataset or policy to measure compliance against)
- **PASS**: All of the compliance checks passed; no further action is required.
- **FAIL**: One or more compliance checks failed; further action may be required.
- **FAIL-SEVERITY**: The FAIL status along with the severity set by the user during policy definition. Includes:
  - **FAIL-VERY LOW**
  - **FAIL-LOW**
  - **FAIL-MEDIUM**
  - **FAIL-HIGH**
  - **FAIL-VERY HIGH**

## Data Drift/Predictions

The **Predictions** tab of the Monitoring Dashboard displays the distribution and drift statistics of the model predictions.


### Total Predictions

The Total Prediction pane tracks the total number of predictions across all the monitored datasets. This allows the user to visualize the activity of the ML model and verify that the production models are making predictions as expected.

![Total predictions graph](/img/md-total-predictions.png)


### Prediction Drift

The Prediction Drift pane displays the drift statistic for the prediction outcome. Depending on the type of learning task, regression or classification, the drift statistic will either be the univariate Kolmogorov-Smirnov test (range from 0 to 1, inclusive) or the Chi-squared test (range from 0 to N, inclusive), respectively.

![Predictions drift graph](/img/md-prediction-drift.png)


### Prediction Label Distribution

At the top right of the Prediction Label Distribution pane, select a display option: Count or Percentage.

Depending on your learning task type, one of two graphs is displayed.

For regression tasks, you will see the quartile distribution for the prediction values. The quartiles allow you to evaluate the descriptive statistics of the prediction label.

![Predictions label distribution: regression](/img/md-prediction-value-distribution-regression.png)

For classification tasks, the count or percentage distribution of the classes is displayed. The breakdown of the number of predictions that belongs to each class for each monitored dataset allows users to analyze changes in class distribution.

![Predictions label distribution graph: classification](/img/md-prediction-label-distribution-classification.png)


## Data Quality/Input Features

The **Input Features** tab of the Monitoring Dashboard details page provides visualizations that help users evaluate the feature quality of the monitored datasets by tracking the following distribution statistics for each feature:

- **Quartiles (min, 25%, 50%, 75%, and max) for numeric data features**:
- **Count/Percentage data for categorical data features**:

  The data distribution, displayed as either Percent or Count, is illustrated for each feature. Note that Certifai only returns count values if a categorical feature has less than 15 distinct groups. As a result, categorical features with high cardinality cannot be displayed.

In this section you may select to view an overall analysis of the features or you may select a specific feature to visualize.

For categorical graphs only, categorical features are listed in the dropdown; while numeric features are selectable on the numeric graphs.

### Feature Data Quality

1. Select the type of data quality analysis you wish to run by making a selection from the top right menu.  Options include:

  - **Average Missing Cells**: The average number of cells that are missing values either for the overall Monitored Dataset or for a selected feature.
  - **Average Unexpected Cells**: The average of the cells containing values that do not exist in the Reference Dataset either for the overall Monitored Dataset or for a selected Feature.
  - **Percent Rows with Missing Values**: The percent of rows with missing values in the overall Monitored Dataset or for a selected feature.
  - **Percent Rows with Unexpected Values**:The percent of rows containing values that do not exist in the Reference Dataset either for the overall Monitored Dataset or for a selected Feature.

2. Select to view an Overall analysis of the data features or select a specific feature from the dropdown list on the right.

![Feature data quality graph](/img/md-feature-data-quality.png)


### Categorical Feature Drift (Chi-squared)

Similar to the prediction drift, feature drift is calculated for each feature. For categorical drift Chi-squared test which will very from 0 to N inclusive, is applied.

![Categorical Feature drift graph](/cortex-certifai/img/md-categorical-feature-drift.png)


### Numeric feature Drift (Kolmogorov-Smirnov)

For numeric drift the  Kolmogorov-Smirnov test with range from 0 to 1 inclusive, is applied.

![Numeric feature drift graph](/img/md-numeric-feature-distribution.png)


### Categorical Feature Distribution

 The data distribution, displayed as either Percent or Count, is illustrated for each feature. For categorical features,  the top five values in each categorical feature (determined by highest count in the range of dates provided) are displayed, and all the other values are grouped together into the `other_categories` group.

 Certifai only returns count values if a categorical feature has less than 15 values to avoid listing high cardinality features. As a result, categorical features with high cardinality cannot be displayed in this way.

 ![Categorical Feature Distribution graph](/img/md-categorical-feature-distribution.png)


### Numeric Feature Distribution

The numeric features are characterized using the quantile method which is used to evaluate descriptive statistics of the spread of the feature distributions.

![Numeric Feature Distribution](/img/md-numeric-feature-distribution.png)


## Performance

The **Performance** tab of the Monitoring Dashboard Details displays the metrics used to evaluate the performance metric (link was here). These include accuracy, precision, and other specified metrics (e.g. R2 in regression) calculated by Certifai.

The threshold presented is a user-defined value from the provided compliance requirements and reports.

![Performance graphs](/img/md-performance.png)

## Fairness

The **Fairness** tab of the Monitoring Dashboard Details page displays the metrics used to evaluate the fairness metrics (link was here) of the model. These include the overall fairness score and the fairness scores from each fairness feature as calculated by Certifai.

The Fairness metric may be toggled to display different metrics if they were included in the evaluation. This can include: Burden, Demographic Parity, equal odds, or equal opportunity.

The threshold presented is a user-defined value from the provided compliance requirements and reports.

![Fairness graphs](/img/md-fairness.png)
