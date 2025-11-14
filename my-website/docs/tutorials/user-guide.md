---
title: User Guide
description: ZMGT Documentation Template - User Guide
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are from 2K documentation samples.

:::

# ZMGT Documentation Template: User Guide

\*[Provide users with step-by-step instructions for using all or part of a system, service, or software with a particular goal or outcome. Usually includes diagrams and screenshots of UI to provide clear instructions. The focus is on front end use cases that are not specifically onboarding, integration, or configuration.]

---

## \*Title and Version (Product \+ Document Type \+ v1.0 or other number)

[NOTE: The document title uses Heading 1 (a single hash), not Heading 2 (the double hash) as it is here. It is placed under the front matter inside the document.]

:::example

## User Guide: Create and Manage Campaigns v1.0

:::

\*Audience, Purpose, Subject summary statement

    [Assistance with writing this summary statement can be found [here](/contributors/style-guide/matters-of-style#audience-purpose-and-subject)]

:::example

This page provides an overview of Technodrome → Experience Manager and details how Live Ops and Studio Developers can view, create, and manage Campaigns.

:::

## Introduction

\*[2-5 sentences and/or bullet points that describe the process, service, or technology.

- What it is and what it does
- Who it’s for
- How players or developers interact with it
- Why it’s important or useful]

:::example

## Introduction

The **Experience Manager** is a “content orchestrator” to create personalized promotional and engagement campaigns, linking audiences, content, and start/end dates. The Experience Manager provides:

- Campaign status flow: Draft, Waiting for approval, Scheduled, Active
- Telemetry integration: Events are triggered to describe actions taken by the campaign
- Push integration: A message is sent to the game clients to enable a refresh and show new content to users in real time
- Ingestion and throttling: Allows throttling at output level, includes data validation/operations

:::

## Overview Diagram

\*[The audience of this part is for Studio Developers/Engineering/Programmers and Live Ops. They want to see the big picture in a single view from start to finish, or they want a visual to describe the end product. Remember to keep the focus on the process or end result.]

:::example

## Overview Process Flow and Diagram

Campaigns are created and managed in **Technodrome → Experience Manager**.

1.  Create Draft campaign.
2.  Submit for approval.
3.  Approve the campaign.
4.  Publish the campaign. Published campaigns become visible when the start date/time is reached.

The diagram below illustrates the process flow of creating and publishing a Campaign.



:::

## Definitions

\*[Can include definitions for parts of the UI, end results, and/or product-related terms or components.]

:::example

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

:::example

## Prerequisites

- Access to **Technodrome → Experience Manager**
- Linked **Audience** and **Content**
- _(Optional)_ **Integration with Push**

:::

## Process(es)

\*[**NOTE:** More than one process may be included in a single user guide. For example, a user guide to Create & Manage Sandboxes can include multiple processes, including: Create a Sandbox, Copy (Clone) a Sandbox, Publish the Sandbox, Pin App Groups to an Existing Sandbox, etc.]

### Step (Verb \+ Noun)

\*[Each step in each process must include the following:

- Description of the action(s) the user takes
- The outcome of the action
- Example (description, image, or code snippet)
- Statement of completion]

:::example

## Processes

### View Campaign Details

**Role permissions:** Marketer and Marketing Manager

1. Go to **Technodrome** → **Experience Manager** → **Campaign management**.
2. Click on a **Campaign**. The _Campaign_ page displays, listing any linked audiences and content.

_Example Commerce V2 Test 2 Campaign:_



### Create a New Campaign

**Role permissions:** Marketer and Marketing Manager

1.  Go to **Technodrome** → **Experience Manager** → **Campaign management** → Click **\+New Campaign**.

 

2.  Enter **Campaign details**. For field definitions, refer to _Campaign Fields_ below.
    - **NOTE:** Start time must be at least one hour beyond the time you create the campaign.
3.  _(Optional)_ Link Audiences to the campaign. For field definitions, refer to _Campaign Fields_ below.
    - **NOTE:** Linking audience(s) is _optional_ to **create the campaign**; however, to submit the campaign for approval, at least one audience must be linked.
    - Click **Link Audience**.
    - Select the **Source** of the audience: _CDP, Manual, RAF_
    - Select the **checkbox(es)** next to the audience(s) you want to link.
    - Click **Select audience**.

   

:::

## Next Steps (optional)

\<Include this section if there is some logical next action that the audience would take. Link to the documentation for that activity.\>

:::example

## Next Steps

### Submit a Campaign for Approval

**Role permissions:** Marketer and Marketing Manager

1.  Go to **Technodrome** → **Experience Manager** → **Campaign management**.
2.  Click on a **Campaign**. The _Campaign_ page displays.
3.  Click **Submit for approval**. A confirmation popup opens.
4.  Click **Submit** to confirm.
    - A confirmation message displays.
    - The status is changed to _Waiting for approval_.

### Approve a Campaign

**Role permission:** Marketing Manager

1.  Go to **Technodrome** → **Experience Manager** → **Campaign management**.
2.  Click on a **Campaign**. The _Campaign_ page displays.
3.  Click the **Approval** toggle ON. A confirmation popup opens.
4.  Click **Approve** to confirm.
    - A confirmation message displays.
    - The status is changed to _Ready to publish_.

:::

## Appendix

\<Referential materials that will help users understand the topic: diagrams, tables, glossaries, related articles, etc.\>

:::example

## Appendix

### Campaign Fields

| Campaign                |             Required             | Description                                                                                       | Notes                                                    |
| ----------------------- | :------------------------------: | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Name**                |               Yes                | Unique name of the Campaign                                                                       | 4-256 characters                                         |
| **Type**                |               Yes                | **Select type:**                                                                                  |                                                          |
|                         |                                  | **_Fixed Period_** – Start/End date/time                                                          |                                                          |
|                         |                                  | **_Evergreen_** – No end date                                                                     | **To be implemented**                                    |
| **Start/End date/time** | Required for _Fixed Period_ type | When the campaign starts/ends                                                                     | Start/end times are Pacific Time                         |
| **Description**         |                No                | Description of the Campaign                                                                       | 4-256 characters                                         |
| **Linked Audience**     |                No                | Select source of the audience to be linked to the campaign, then select audience:                 | **Role permissions limit what audiences can be linked.** |
|                         |                                  | **_CDP_** – Audience created in the CDP tool                                                      |                                                          |
|                         |                                  | **_Manual_** – Audience manually created via **Experience Manager → Audience management**         |                                                          |
|                         |                                  | **_RAF_** – Audience created via the Refer a Friend tool                                          |                                                          |
| **Linked Content**      |                No                | Select the Source of the content:                                                                 | **Role permissions limit what content can be linked.**   |
|                         |                                  | **_Commerce V2_** – directly entitling items or VC in legacy titles                               |                                                          |
|                         |                                  | **\*Commerce V3 Direct Entitlements** – directly entitling items, VC, or licenses in new titles\* |                                                          |
|                         |                                  | **_Commerce V3 Offers_** – directly targeting offers in new titles                                |                                                          |
|                         |                                  | **_Promotions_** – directly targeting promotions for all titles                                   |                                                          |

:::
