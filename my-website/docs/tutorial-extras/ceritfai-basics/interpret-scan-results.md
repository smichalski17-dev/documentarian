---
title: "Interpret Scan Results"
linkTitle: "Interpret Scan Results"
description: >
  This page provides illustrative examples of how to interpret scan results displayed in the Certifai Console.
---

This page provides illustrative examples of how to interpret scan results displayed in the Certifai Console.

Certifai scan results can offer significant information to model developers and business owners who have wider insights into the model. These insights can be used to steer subsequent model enhancements based on Certifai scores and explanations.

## Prerequisites

The discussion below assumes a working knowledge of the what trust factors are and how they are derived by counterfactuals. Read the pages related to trust factors before proceeding.
- [Performance Metrics](/certifai-basics/factors/performance-metric.md)
- [Robustness](/certifai-basics/factors/robustness.md)
- [Fairness](/certifai-basics/factors/fairness.md)
- [Explainability and Explanations](/certifai-basics/factors/explainability.md)
- [ATX](/certifai-basics/factors/atx.md)


## Assumptions

- Interpretation is being done by someone with understanding of the domain and models
- Explanation dataset has been taken as a representative sample
- The models used for the examples that follow have not been optimized
- The datasets used in the examples that follow are considerably smaller than many "real world" samples (under 1K rows).

## HealthCare Use Case: Diabetes Prediction

### The Scan

- **Use Case**: Predicting a diagnosis of type 2 diabetes
- **Models**: Support Vector Classifier (SVC), Multi-layer Perceptron Classifier (MLPC), Logistic Regression (LR), and Decision Tree (DT)
- **Trust Factors**: Performance metric, robustness, and explainability, ATX (AI Trust Index).
- **Dataset**: Pima Indian women

  **NOTE**: Fairness was not included in this evaluation because the dataset used was for a homogeneous demographic

### Evaluation Overview

The image below shows the Evaluation overview results as shown in the Certifai Console.

The Evaluation view for each of the identified trust factors is displayed.

Scores are calculated as a percent (out of 100%) for each trust factor and model.

The higher the score, the better the model performed for the given trust factor.

![Healthcare: Diabetes Evaluation Overview](/img/interp-healthcare-eval-overview.png)

### Interpret Robustness

**Observations**

- Greater variation in the robustness scores (heights of the bars)
- Lower scores for robustness - All of the models have under 50% robustness.
- The multi-layer perceptron (MLPC) and decision tree (DT) models have much lower robustness scores.

**Conclusions**:

- A low value of robustness arises because the majority of the data points and their counterfactuals are close to the decision boundary. This often occurs when there is a complex decision boundary, which is common when a model is overfitted.
- This dataset does not provide a clear separation of those who have  diabetes and those who don't.  
- The MLPC and DT models may be overfitted.

**Actions**:

- Based on the robustness results and the early-development state of the models, it would make sense to revisit the tuning of the models.
- Check MLPC and DT models' accuracy scores against the training dataset versus the test dataset to confirm that the models are overfitted.

### Interpret Explainability

The following view from the Console displays the explainability histogram for each model, which shows the percentage of explanations that require a given number of changed features. In general, the fewer features in the counterfactual explanation, the simpler it is for a human to understand the explanation.

![Healthcare: Diabetes Evaluation Explainability](/img/interp-healthcare-expl-by-model.png)

**Observations**:

- The explainability figures are high for all of the models
- Most of the models' predictions can be explained by a change in only one or two features

**Conclusion**:

- All models have simple counterfactual explanations.

### Interpret Explanations

In addition to displaying the model's overall explainability score, the Console provides a set of sample explanations that you can click through one at a time to explore the details. This can offer insights into the model.

#### Decision Tree model explanations

The explanation detail (#8) below displays the observations for the  decision tree (DT) model.

![Healthcare: Diabetes Counterfactual Explanation 8 for Decision Tree model](/img/interp-healthcare-expl-obs8-DT.png)

**Observation**:

- The model predicts that a subject with a glucose level of 155 does not have diabetes, and one with exactly the same other feature values and a glucose level of 154 does have diabetes.

**Conclusion**:

- The model behavior seems questionable because typically, with a higher level of glucose a subject is more likely to have diabetes.
- The oddity is almost certainly related to overfitting.

#### Logistic Regression model explanations

The explanation detail (#8) below shows the same observation for the logistic regression (LR) model.

![Healthcare: Diabetes Counterfactual Explanation 8 for Logistic Regression model](/img/interp-healthcare-expl-obs8-LR.png)

**Observation**:

- The LR model behavior predicts that the subject with a glucose level of 155 has diabetes, whereas a subject with the same features except for a lower glucose and slightly lower BMI index does not.

**Conclusion**:

- The LR model is explanation is not problematic, which makes it a better choice.

### Possible Use Case Conclusions

- If the MLPC and DT models could not be improved, the combination of their lack of robustness and weaker performance would discount them from selection.
- Because the LR model scores better for performance, explainability, and robustness, it is the preferred model.

## Banking Use Case: Loan Decision

### The Scan

- **Use Case**: Banking use case determining loan approval/denial
- **Models**: Support Vector Classifier (SVC), Multi-layer Perceptron Classifier (MLPC), Logistic Regression (LR), and Decision Tree (DT)
- **Trust Factors**: Performance metric, robustness, explainability, AI Trust Index (ATX), and fairness
  - Fairness sensitive features defined:
    - Age: < 25 years old and >= 25 years old
    - Status: a combination of marital status and gender (e.g. male and single).

### Evaluation Overview

The image below shows the Evaluation overview results as shown in the Certifai Console.

The Evaluation view for each of the identified trust factors is displayed.

Scores are calculated as a percent (out of 100%) for each trust factor and model, plus the ATX (AI Trust Index).

The higher the score, the better the model performed for the given trust factor.

![Banking:Loan Approval Evaluation Overview](/img/interp-banking-eval-overview.png)


### Interpret Robustness

**Observations**:

- The DT model has significantly lower robustness.
- The LR model where regularization has been used to counter overfitting shows a higher robustness score.

**Conclusion**:

- The DT model may suffer from overfitting.
- The best selection would be the LR model.
- A second choice might be improve the decision tree model  (e.g. by using regularization techniques) to discourage overfitting.

### Interpret Fairness

The Fairness details display provides a view into potential bias of the models.  

The upper chart compares the fairness scores for age and status, the two defined sensitive features for fairness in this use case.

The lower chart shows the burden associated with the groups within the status feature.

#### Support Vector Classifier model fairness

The following charts are for the SVC model:

![Banking:Loan Approval Fairness Support Vector Classifier](/img/interp-banking-fairness-SVC.png)

**Observations**:

- The SVC model is the most biased model with a fairness score of 70%.
- (Upper chart) The score for status is lower (i.e. less fair) than that for age.
- (Lower chart) The lowest burden is on married males.
- Three times more burden is on divorced males.
- The difference in burdens (change needed to obtain a favorable outcome) is greater across the status groups than the age groups

**Conclusion**:

- According to the SVC model, divorced males would need to make larger changes in order to have a loan approved.

**Actions**:

- If a model has a low fairness score, you might check to see
if the data is imbalanced, and if it is, gather additional data.

#### Multi-layer Perceptron Classifier model fairness

The following charts are for the MLPC model:

![Banking:Loan Approval Fairness MLPC](/img/interp-banking-fairness-MLPC.png)

**Observations**:

- The MLPC model has similar fairness for both age and status.
- The burdens across groups are significantly more equal (than those for the SVC model)

**Conclusion**:

- The MLPC model is more fair than the SVC model.

### Interpret Explainability

The following view from the Console shows the explainability histogram for each model.

The histograms in this view show the percentage of explanations that require a given number of changed features.

The fewer features in the counterfactual explanation, the simpler it is for a human to understand the explanation.

![Banking:Loan Approval Evaluation Explainability](/img/interp-banking-expl-by-model.png)

**Observation**:

- The MLPC model has reasonably high explainability with most predictions explained by a change in only one or two features.
- The SVC model has lower explainability as it often requires three or four changed features to explain a prediction.

**Conclusion**:

- MLPC is the better model to choose from point of view of explainability, if its other trust factor scores are acceptable. (In this case the robustness score is also high)
- The higher-performing SVC model may be harder for a human to understand, which is unfavorable.

**Actions**

- Try another model implementation, specifically one
with lower complexity (e.g. in a classification setting, try logistic
regression).
- Try adding or increasing the amount of regularization in
your model.

### Interpret Explanations

The interpretation of explanations depends on how the explanation dataset has been sampled. For example, you could:

- Explore the model behavior by deliberately choosing inputs that are potential outliers
- Choose a random sample to facilitate discussion with domain experts to build confidence in an algorithm and look for unexpected results
- Choose a larger representative sample (e.g. 1000 rows) to perform additional analysis (e.g. This notebook (link to notebook has been removed) is designed understand how frequently various features occur in explanations.)

The explanations for this use case have been selected because they are noteworthy and unexpected.

#### Support Vector Classifier model explanations

The explanation detail (#29) below shows a counterfactual explanation for a prediction made by the SVC model.

![Banking:Loan Approval Counterfactual Explanation 29 for Support Vector Classifier model](/img/interp-banking-expl-obs29-SVC.png)

**Observation**:

- The SVC model requires four changed features to alter the prediction (checking status, duration of loan, history of paying back loans, and employment period).

#### Multi-layer Perceptron Classifier model explanations

The explanation detail (#29) below shows a counterfactual explanation for a prediction made by the MLPC model.   

![Banking:Loan Approval Counterfactual Explanation 29 for Multi-Layer Perceptron Classifier model](img/interp-banking-expl-obs29-MLPC.png)

**Observation**:

- The MLPC model requires two changed features to alter the prediction (reduced residence time and increased number of existing cards would cause loan to be denied).

**Conclusion**:

- The MLPC model's counterfactual is simpler to understand because it requires fewer changed features to alter the result.

### Possible Use Case Conclusions

If the comparison scan is run with the purpose of choosing between existing models that cannot be retrained or modified:

- The lower performance and lower robustness of the DT model would make it the weakest candidate, despite its higher fairness and explainability scores.
- If the selection of a model is based only on the performance metric, the SVC model is the best candidate, even though it has the lowest fairness score.
- If the selection of a model is based only on the ATX score, the MLPC model is the best candidate (when the scores are all weighted equally).
- If the selection of a model is based only on the ATX score that weighs explainability lower and performance higher, the LR model is the best candidate.

## General Interpretation Conclusions

### Fairness

- The fairness score won't tell you if there are underrepresented groups.
- However, if Certifai has a low fairness score, then you could check to see if the data is imbalanced, and if it is, gather more data

### Explainability

If the number of counterfactuals required to change the outcome is high and the model is therefore less explainable:

- Try another model implementation, specifically one
with lower complexity (e.g. in a classification setting, try logistic
regression).
- Try adding or increasing the amount of regularization in
your model.
