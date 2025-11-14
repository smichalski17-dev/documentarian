---
title: 'Developer (SDK) Guide'
description: ZMGT Documentation Template - Developer Guide (SDK Guide)
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are from 2K documentation samples.

:::

# ZMGT Documentation Template: Developer Guide (SDK Guide)

\*[This template is for SDK or developer guides. It provides users with step-by-step instructions for accomplishing a software task using SDKs, APIs, or code. Typically, this involves backend tasks that may also include integration or configuration.]

---

## \*Title and Version (Product \+ Document Type \+ v1.0 or other number)

[NOTE: The document title uses Heading 1 (a single hash), not Heading 2 (the double hash) as it is here. It is placed under the front matter inside the document.]

:::example

## SDK Developer Guide: Identity QR Based Account Linking v1.0

:::

\*[Audience, Purpose, Subject summary statement]

[Assistance with writing this summary statement can be found [here](/contributors/style-guide/matters-of-style#audience-purpose-and-subject)]

:::example

This page details how Studio Developers can implement Identity’s QR-based account linking feature supported with DCL, including integration for COPPA compliant login and registration.

:::

## Introduction

\*[2-5 sentences that describe the service and technology.

          - What it is and what it does
          - Who it’s for
          - How players or developers interact with it
          - Why it’s important or useful]

:::example

## Introduction

DNA requires **QR based account linking** for user registration and account management, ensuring secure player verification and COPPA compliance. This method replaces manual email/password linking, with the entire process facilitated through [portal.2k.com](http://portal.2k.com).

      - **Simplified account verification:** Players link accounts by scanning a QR code, simplifying the verification process and making it easy for parents to manage child accounts.
      - **Enhanced security:** QR codes reduce unauthorized access, particularly important for Child accounts needing parental consent.
      - **Efficient parental controls:** Parents can quickly link and manage child accounts, allowing them to monitor and adjust settings as needed.
      - **Seamless integration with age assurance:** Integrates with age verification during account setup to automatically apply correct age-based settings, ensuring compliance with COPPA and local privacy laws.
      - **Improved user experience:** Easy setup and management for players and parents, keeping them focused on game enjoyment while maintaining privacy and safety.
      - **COPPA compliance:** QR based account linking simplifies the age verification process and allows parents to manage parental controls. For details, refer to [_COPPA & Age-based Account Settings_](https://2kgames.atlassian.net/wiki/spaces/TS/pages/1193247418)

:::

## Architectural Diagram (optional)

\*[The audience of this section is developers, producers, and product managers. They want to see the big picture in a single view including both sides of the integration and what the final connected picture will look like. Remember if multiple types of users are involved in the integration process, you’ll want to include swim lanes.]

## Prerequisites

\*[Provide a detailed description or list of the prerequisites that must be in place prior to process steps. (As with code, it is best to update content in only one instance, so link out to content that is repeated like prerequisite steps rather than writing and updating it in multiple locations.)]

:::example

## Prerequisites

Configured DNA application for all supported platforms in your Title.

| Supported Engines  |          Min SDK Version           |
| :----------------: | :--------------------------------: |
| Unreal, C++, Unity | **DCL**: version, **DTL**: version |

:::

## Resources

\*[Required and/or helpful configuration items, links to documentation, diagrams, etc.]

:::example

## Resources

- Refer to _Legal Documents & UX Boot Flows_ for resources and guidelines for legal standards, policies, and compliance requirements, including T2 legal documents, boot flow standards, and recommended UX boot flow diagrams.
- Access to the documents should have been provided during your initial onboarding. If you do not have access, please contact your DNA rep.

:::

## Event Configuration

\*[If you can configure your documentation to split the the screen to put the event description and methods beside the code sample that is preferable, but if you cannot, then stacking is okay as well. Description of the action on top and code example below.]

### \* Config Event Name

:::example

## Event Configuration

### Request to Support: QR Code Related Requests

:::

\*[Table of configurable methods and code samples.]

| Method | Code Sample |
| :-- | :-- |
| \*[Description of the event and what that event controls in the software. List the methods that will be configured and the config options for those methods. Be sure to make note of any edge cases.] | \*[Code Sample be sure to highlight the methods that are configurable] |

[Repeat above for each config event in the SDK guide]

:::example Example 1

| Method | Request |
| :-- | :-- |
| Get User code and verification URL | `Request:  POST https://dev.portal.2k.com/oauth2/device_link Authorization: Bearer {{bearer}} Response: HTTP/1.1 200 OK {   "userCode": "E56CPG",   "verificationUrl": "https://dev.portal.2k.com/device?jti=f4a242a0f7104b3983c0a67f6fa2479e",   "verificationUrlComplete": "https://dev.portal.2k.com/device?jti=f4a242a0f7104b3983c0a67f6fa2479e&amp;user_code=E56CPG",   "expiresIn": 3600 }` |

:::

:::example Example 2

## Event Configuration

### Sample Implementation

Below are integration steps you can find in the SDK DCL Sample Game source code.

1. Game initiates login into the DNA platform via DCL.


    - Login response returns:
      - parentAccountStatus – indicates the account linked is complete or incomplete
      - isParentAccountChild – indicates the account linked is child or not

2. Game accepts legal documents.
3. A confirmation screen displays in game to confirm if the user currently logged in is the user that is trying to link the accounts.


    - This is conditional based on the user already seeing/confirming their console login on a previous game boot. Before the following flow is implemented, the game calls cloud data to confirm if the user has an existing record saved, key: ConsoleLoginConfirmation.

`GET /users/@account/products/@product/records/ConsoleLoginConfirmation`

`Response:`

`record: {`  
 `"properties": {`  
 `"loginConfirmation": true / false`  
 `}`  
 `}`

:::

## Verification Process (If applicable)

\*[Add steps to demonstrate how the configuration is verified or tested.]

:::example

## Verification Process: Player Experience Flow

If a record doesn't exist or the **loginConfirmation** value is false, the following flow is shown to the user:

- If the user clicks **THIS IS ME**, the game proceeds, and the game calls the Cloud data subsystem to store a new record.

- If the user clicks **NOT ME**, the game shows an informational popup with instructions on how to switch accounts on that platform. This set of instructions also links to an FAQ article with additional information.

:::

## Error Codes (Messages)

\*[Make a table that lists any error codes or messages that the user may encounter, what they mean, and what action the user should take.]

# Appendix (If applicable)

\*[Referential materials that will help users understand the topic: diagrams, tables, glossaries, related articles, etc.]
