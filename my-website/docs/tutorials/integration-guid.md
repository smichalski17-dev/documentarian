---
title: Integration Guide
description: Documentation Template - Integration Guide
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are made up from a fictional example game.
:::

# Documentation Template \- Integration Guide

\*[Provide step-by-step instructions on how to connect different systems, software, or components so that they work together seamlessly, enabling data sharing and coordinated processes.]

---

## Title and Version (Product \+ Document Type \+ v1.0 or other number)

:::example

## Integration Guide: MyGame First-party Reconciliation v1.0

:::

\*[Audience, Purpose, Subject summary statement]

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

Digital commerce systems must be integrated with gaming platforms to enable reconciliation operations. In this process, a first-party purchase refers to buying an item directly from a platform’s official store, using real currency through the platform’s SDKs. To ensure consistency and accuracy across systems, a reconciliation operation is required after such a purchase. This process verifies that the item acquired from the first-party store is also properly reflected in the system, which manages in-game entitlements and inventory. Essentially, reconciliation involves checking the user’s inventory on the first-party platform and granting the corresponding items within digital commerce, based on predefined mappings between the two systems.

:::

## Architectural Diagram (If available)

\*[The audience of this part are the developers, producers, and product managers. They want to see the big picture in a single view including both sides of the integration and what the final connected picture will look like. Remember if multiple types of users are involved in the integration process, you’ll want to include swim lanes.]

## Prerequisites

\*[Provide a detailed description or list of the prerequisites that must be in place prior to process steps. **In an Integration guide**, you may have prerequisites from both sides of the integration. (As with code, it is best to update content in only one instance, so link out to content that is repeated, such as prerequisite steps, rather than writing and updating it in multiple locations.)]

:::example

## Prerequisites

### Requirements

- To fully utilize the reconciliation feature, ensure you have a product setup on your game platform that can connect to the service, specifically, it should be able to retrieve tokens within a sandbox setup for the game. 
- Set Up First-party SSO for Game Platform.
- Ensure that, during the development phase, all products under testing are launched within the **same** development sandbox. This guarantees the services provide accurate ownership and store purchase responses in a cross-title manner.
- Each title or in-game item possesses a unique **Legacy product ID and Store ID**.
- Access to **GameCloud → Store**

:::

## Components & Settings

\*[List and describe the system components that must be integrated and any settings that must be configured. May be expressed as a table. The name of the headings below are specific to this example.]

:::example

## Components

- Map MyGame Product to Game Platform
- Map MyGame SKU/Offer to Platform Items
- Map MyGame SKU/Offer to First-party Store Entitlement/Item
- (Optional) Set up Cross-title Purchasing

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

When the integration process is complete, the Platform will allow reconciliation of first-party purchases within a game.

### Step 1: Map Products to the Platform

For game services to accurately determine which platform applications requires reconciliation, it is crucial to associate the platform application with the game product.

1.  Go to **GameCloud → Store → Titles**.
2.  Click **\+New title** or select an existing Title.
3.  Select **Platform**.
4.  Enter the **ID** for the Platform. (Example:*PLT-A1*)
5.  Click **Save**.

:::

# Verification Process (If applicable)

\*[Add steps to demonstrate how the integration is verified.]

# Next Steps (Optional)

\*[This section, you would point to instructions for doing the activity that you enabled by completing the integration.]

:::example

# Next Steps

## _(Optional)_ Set Up Cross-title Purchasing

The following instructions apply to teams aiming for cross-title purchasing. For example, players can buy titles, or in-game items for **Game A** while playing **Game B**.

1.  Access partner center
2.  Pick your desired product from the products tab.
3.  Select the **Product Relationship Setup** tab on the navigation menu.
4.  Click **Add a New Relationship** to introduce a new product association to the current title.
5.  Select **can sell** as the relationship type.
6.  Identify the **Partner store ID** of the target title you aim to link to your current product.
7.  Enter the **Store ID** for your target product and save to finalize the relationship between the chosen products.

:::

# Appendix

\*[Referential materials that will help users understand the topic: diagrams, tables, glossaries, related articles, etc.]
