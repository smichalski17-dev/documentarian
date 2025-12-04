---
title: User Guide
description: Documentation Template - User Guide
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are made up from a fictional example game.

:::

# Documentation Template: User Guide

\*[Provide users with step-by-step instructions for using all or part of a system, service, or software with a particular goal or outcome. Usually includes diagrams and screenshots of UI to provide clear instructions. The focus is on front end use cases that are not specifically onboarding, integration, or configuration.]

---

## \*Title and Version (Product \+ Document Type \+ v1.0 or other number)

[NOTE: The document title uses Heading 1 (a single hash), not Heading 2 (the double hash) as it is here. It is placed under the front matter inside the document.]

:::note

## User Guide: Create and Manage Campaigns v1.0

:::

\*Audience, Purpose, Subject summary statement

:::note

This page provides an overview of Experience Manager and details how developers can view, create, and manage campaigns.

:::

## Introduction

\*[2-5 sentences and/or bullet points that describe the process, service, or technology.

- What it is and what it does
- Who it’s for
- How players or developers interact with it
- Why it’s important or useful]

:::note

## Introduction

The **Experience Manager** is a “content orchestrator” to create personalized promotional and engagement campaigns, linking audiences, content, and start/end dates. The Experience Manager provides:

- Campaign flow statuses : Draft, Waiting for approval, Scheduled, Active
- Telemetry integration: Events are triggered to describe actions taken by the campaign
- Push integration: A message is sent to the game clients to enable a refresh and show new content to users in real time
- Ingestion and throttling: Allows throttling at output level, includes data validation/operations

:::

## Overview Diagram

\*[The audience of this part is for Studio Developers/Engineering/Programmers and Live Ops. They want to see the big picture in a single view from start to finish, or they want a visual to describe the end product. Remember to keep the focus on the process or end result.]

:::note

## Overview Process Flow and Diagram

Campaigns are created and managed in **The Experience Manager**.

1.  Create Draft campaign.
2.  Submit for approval.
3.  Approve the campaign.
4.  Publish the campaign. Published campaigns become visible when the start date/time is reached.

:::

## Definitions

\*[Can include definitions for parts of the UI, end results, and/or product-related terms or components.]

:::note

## Definitions: Campaign Status & Actions

The table below defines available actions for a campaign in a specific status.

| Campaign Status          | Available Actions                                  |
| ------------------------ | -------------------------------------------------- |
| **Draft**                | Edit, copy, view campaign history, delete          |
| **Waiting for approval** | Edit, copy, view campaign history, delete          |
| **Ready to publish**     | Publish, edit, copy, view campaign history, delete |
| **Scheduled**            | Edit, copy, view campaign history, delete          |
| **Active**               | Edit, copy, view campaign history, suspend, cancel |
| **Suspended / Frozen**   | Resume, edit, copy, view campaign history, cancel  |
| **Cancelled**            | Copy, view campaign history                        |
| **Expired**              | Copy, view campaign history                        |

:::

## Prerequisites

\*[Provide a detailed description or list of the prerequisites that must be in place prior to process steps. (As with code, it is best to update content in only one instance, so link out to content that is repeated like prerequisite steps rather than writing and updating it in multiple locations.)]

:::note

## Prerequisites

- Access to **The Experience Manager**
- Links to **Audience** and **Content**
- _(Optional)_ **Integration with Push Notifications**

:::

## Process(es)

\*[**NOTE:** More than one process may be included in a single user guide. For example, a user guide to Create & Manage Sandboxes can include multiple processes, including: Create a Sandbox, Copy (Clone) a Sandbox, Publish the Sandbox, Pin App Groups to an Existing Sandbox, etc.]

### Step (Verb \+ Noun)

\*[Each step in each process must include the following:

- Description of the action(s) the user takes
- The outcome of the action
- Example (description, image, or code snippet)
- Statement of completion]

:::note

## Processes

### View Campaign Details

**Role permissions:** Marketer and Marketing Manager

1. Go to **The Experience Manager** → **Campaign management**.
2. Click on a **Campaign**. The _Campaign_ page is displayed, listing any linked audiences and content.

_Example Test 2 Campaign:_

### Create a New Campaign

**Role permissions:** Marketer and Marketing Manager

1.  Go to **The Experience Manager** → **Campaign management** → Click **\+New Campaign**.
2.  Enter **Campaign details**. For field definitions, refer to _Campaign Fields_ below.
    - **NOTE:** Start time must be at least one hour beyond the time you create the campaign.
3.  _(Optional)_ Link Audiences to the campaign. For field definitions, refer to _Campaign Fields_ below.
    - **NOTE:** Linking audience(s) is _optional_ to **create the campaign**; however, to submit the campaign for approval, at least one audience must be linked.
    - Click **Link Audience**.
    - Select the **Source** of the audience
    - Select the **checkbox(es)** next to the audience(s) you want to link to.
    - Click **Select audience**.

:::

## Next Steps (optional)

\<Include this section if there is some logical next action that the audience would take. Link to the documentation for that activity.\>

:::note

## Next Steps

### Submit a Campaign for Approval

**Role permissions:** Marketer and Marketing Manager

1.  Go to **The Experience Manager** → **Campaign management**.
2.  Click on a **Campaign**. The _Campaign_ page is displayed.
3.  Click **Submit for approval**. A confirmation popup opens.
4.  Click **Submit** to confirm.
    - A confirmation message is displayed.
    - The status is changed to _Waiting for approval_.

### Approve a Campaign

**Role permission:** Marketing Manager

1.  Go to **The Experience Manager** → **Campaign management**.
2.  Click on a **Campaign**. The _Campaign_ page is displayed.
3.  Click the **Approval** toggle ON. A confirmation popup opens.
4.  Click **Approve** to confirm.
    - A confirmation message is displayed.
    - The status is changed to _Ready to publish_.

:::

## Appendix

\<Referential materials that will help users understand the topic: diagrams, tables, glossaries, related articles, etc.\>


