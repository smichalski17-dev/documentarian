---
title: Reference Guide
description: ZMGT Documentation Template - Reference Guide
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are from 2K documentation samples.

:::

# ZMGT Documentation Template: Reference Guide

\*[**NOTE**: Reference guides provide detailed information that helps users understand policies, functions, methods, properties, parameters, etc. Examples include a Glossary, Data Dictionary, Policy Document, etc. **This page includes an _example_ of a reference guide.** While reference guides may be structured differently, they all should include: **Document Title and Version, subject statement to define audience/purpose,** and **Introduction**, as noted below.]

---

## \* Title and Version (Product \+ Document Type \+ v1.0 or other number)

:::example

## Reference Guide: Commerce Smart Pricing: Repurchase Policy v1.0

:::

\*Audience, Purpose, Subject summary statement

    :::example

    This page explains **Smart Pricing** and **Repurchase Policy** for Studio Developers and Live Ops users setting up a pricing strategy for in-game inventory items and offers.

    :::

## Introduction

    \*[2-5 sentences and/or bullet points that describe the reference material. May include:

    - What it is and what it does
    - Who it’s for
    - How players or developers interact with it
    - Why it’s important or useful]

    :::example

    # Introduction

    **Smart Pricing/Repurchase Policy** is a dynamic pricing strategy used by DNA Commerce Marketplace to adjust the price of an **in-game bundled offer** based on the user's existing ownership of **durable, unique items** (a player can only own one) within that offer.

    This mechanism automatically reduces the cost of a bundle or offer by excluding the price of items the user already owns, ensuring users do not pay for items they already have, while still providing a discounted price for the remaining items. This method enhances perceived value and encourages additional purchases without redundant costs.

    For example, if a user already owns one unique item in a three-item offer, the price of the offer is adjusted to reflect only the cost of the two remaining items, applying the offer discount proportionally.

    :::

## \*Content (as needed)

\*[Include reference information that explains the topic, such as definitions, diagrams, use cases, examples, related articles, etc.]

:::example

## Terms and Definitions

The following terms apply to Use Cases below.

| Smart Pricing Terms | Definition |
| --- | --- |
| **Offer** | An Offer refers to a unit that can be purchased by the user. That unit can contain one or more items and/or currencies. |
| **Intrinsic Value** | An abstract number value set on an item which determines the worth of the item/currency is in the context of a game. This is the worth of 1 of the item or currency. |
| **Discount** | An Offer is sold at a discount if the user would pay less than the items in it are worth. |
| **Premium** | An Offer is sold at a premium if the user would pay more than the items in it are worth. |
| **Base Price** | The price of the Offer before any amounts are deducted for owned items or sales. The base price could entail an implicit discount if the price is lower than the Offer content is worth, or an implicit premium if it's higher than the Offer content is worth. Note that DNA Commerce does not know about these implicit discounts/premiums. |
| **Sale** | A flat percentage discount applied on the price after the value of owned items has been deducted from the base price. |
| **Offer Price** | The price of the Offer after the price of owned items has been deducted from the base price and the sale discount has been applied. This is what the user would pay to purchase the Offer. |

:::
