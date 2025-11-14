---
title: Integration Guide
description: ZMGT Documentation Template - Integration Guide
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are from 2K documentation samples.

:::

# ZMGT Documentation Template \- Integration Guide

\*[Provide step-by-step instructions on how to connect different systems, software, or components so that they work together seamlessly, enabling data sharing and coordinated processes.]

---

## Title and Version (Product \+ Document Type \+ v1.0 or other number)

:::example

## Integration Guide: Commerce Xbox First-party Reconciliation v1.0

:::

\*[Audience, Purpose, Subject summary statement]

[Assistance with writing this summary statement can be found [here](/contributors/style-guide/matters-of-style#audience-purpose-and-subject)]

:::example

This guide outlines the necessary steps and identifiers that Studio Developers/Engineering/Programmers need to integrate Xbox to allow reconciliation of purchases within a game.

:::

## Introduction

\*[2-5 sentences that describe the service and technology.

- What it is and what it does
- Who it’s for
- How players or developers interact with it
- Why it’s important or useful]

:::example

Digital commerce systems must be integrated with gaming platforms to enable reconciliation operations. In this process, a first-party purchase refers to buying an item directly from a platform’s official store, such as Xbox, using real currency through the platform’s SDKs. To ensure consistency and accuracy across systems, a reconciliation operation is required after such a purchase. This process verifies that the item acquired from the first-party store is also properly reflected in the DNA Commerce system, which manages in-game entitlements and inventory. Essentially, reconciliation involves checking the user’s inventory on the first-party platform and granting the corresponding items within DNA Commerce, based on predefined mappings between the two systems.

:::

## Architectural Diagram (If available)

\*[The audience of this part are the developers, producers, and product managers. They want to see the big picture in a single view including both sides of the integration and what the final connected picture will look like. Remember if multiple types of users are involved in the integration process, you’ll want to include swim lanes.]

## Prerequisites

\*[Provide a detailed description or list of the prerequisites that must be in place prior to process steps. **In an Integration guide**, you may have prerequisites from both sides of the integration. (As with code, it is best to update content in only one instance, so link out to content that is repeated, such as prerequisite steps, rather than writing and updating it in multiple locations.)]

:::example

## Prerequisites

### Xbox Requirements

- To fully utilize the reconciliation feature, ensure you have a product setup on Xbox that can connect to the Xbox live service, specifically, it should be able to retrieve the Xbox xstsToken within a sandbox setup for the game. For details on setting up an application on Xbox Live, please refer to _Identity Implementation Guide_.
- Set Up First-party SSO for Xbox Live v1.0\_ .
- Ensure that, during the development phase, all products under testing are launched within the **same** development sandbox. This guarantees the Xbox services provide accurate ownership and store purchase responses in a cross-title manner.
- Xbox 1 requires the **Legacy product ID** for each game, DLC, or in-game item listed on the Xbox partner center intended for in-game purchase.
- Xbox Series S/X uses the **Store ID** for each game, DLC, or in-game item listed on the Xbox partner center intended for in-game purchase.
- Each title, DLC, or in-game item possesses a unique **Legacy product ID and Store ID**.

### Technodrome Requirements

- Access to **Technodrome → First Party Store**
- Access to **Technodrome → Commerce**

:::

## Components & Settings

\*[List and describe the system components that must be integrated and any settings that must be configured. May be expressed as a table. The name of the headings below are specific to this example.]

:::example

## Components

- Map DNA Product to Xbox
- Map DNA SKU/Offer to Xbox Items
- Map DNA SKU/Offer to First-party Store Entitlement/Item
- (Optional) Set up Cross-title Purchasing

## Platform ID Mapping

This table outlines the IDs needed for first-party purchasing and reconciliation for Xbox.

| Platform | Offer Type | Offer | Entitlement | Title |
| --- | :-: | --- | --- | --- |
| **Xbox One** (XDK) | N/A | Xbox legacy product ID | Xbox legacy product ID | Xbox legacy product ID |
| **Xbox One** (GDK) | N/A | Xbox Store ID | Xbox legacy product ID | Xbox legacy product ID |
| **Xbox Series X** | N/A | Xbox Store ID | Xbox legacy product ID | Xbox legacy product ID |

:::

## Integration Process(es)

\*[When the integration process is complete, describe what users will be able to do.]

\*[Repeat steps, as needed.]

### Step 1: \*[Verb + Noun phrase]

\*[To write useful procedures:

- Break the step into smaller steps
- Use images of user interfaces or code snippets if these are applicable.
- Sanitize any examples, so no secure information is exposed.
- Include who performs the action.
- Include configurations.
- Include the context so the user knows where the action originates
- Include the result of the action or set of actions so the user understands the goal.]

### Step 2: \*[Verb + Noun phrase]

:::example

## Integration Processes

When the integration process is complete, DNA will allow reconciliation of first-party purchases within a game.

### Step 1: Map DNA Product to Xbox

For DNA services to accurately determine which Xbox application requires reconciliation, it is crucial to associate the Xbox application with the DNA product.

1.  Go to **Technodrome → First Party Store → Titles**.
2.  Click **\+New title** or select an existing Title.
3.  Select **Xbox One** or **Xbox Series XS**.
4.  Enter the **Legacy Product ID** for the Xbox One and Xbox Series XS. _Example for Xbox One:_
5.  Click **Save**.

### Step 2: Map DNA SKU/Offer to Xbox Items

1.  Steps

:::

# Verification Process (If applicable)

\*[Add steps to demonstrate how the integration is verified.]

# Next Steps (Optional)

\*[This section, you would point to instructions for doing the activity that you enabled by completing the integration.]

:::example

# Next Steps

## _(Optional)_ Set Up Cross-title Purchasing

The following instructions apply to teams aiming for cross-title purchasing. For example, players can buy titles, DLC, or in-game items for **Game A** while playing **Game B**.

For cross-title, cross-DLC purchases in Xbox applications, ensure titles are interconnected on [Microsoft Partner center](https://partner.microsoft.com/). To establish a relationship between two products:

1.  Access [_Microsoft Partner center_](https://partner.microsoft.com/).
2.  Pick your desired product from the products tab.
3.  Select the **Product Relationship Setup** tab on the navigation menu.
4.  Click **Add a New Relationship** to introduce a new product association to the current title.
5.  Select **can sell** as the relationship type.
6.  Identify the **Microsoft store ID** of the target title you aim to link to your current product.
7.  Enter the **Store ID** for your target product and save to finalize the relationship between the chosen products.

:::

# Appendix

\*[Referential materials that will help users understand the topic: diagrams, tables, glossaries, related articles, etc.]
