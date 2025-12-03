---
title: Onboarding (Implementation) Guide
description: Documentation Template - Onboarding Implementation Guide
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are made up from a fictional example game.

:::

# Documentation Template: Onboarding (Implementation) Guide

\*[Help users integrate with a new system, software, or product. Include step-by-step setup procedures, from initial introduction to the first use case.]

---

## \*Title (Product \+ Document Type)

[**NOTE**: The document title uses Heading 1 (a single hash), not Heading 2 (the double hash) as it is here. It is placed under the front matter inside the document.]

    :::example

    ## MyGame Identity First-party SSO Implementation Guide

    :::

\*Audience, Purpose, Subject summary statement

    :::example

    This guide provides developers with detailed instructions for setting up first-party SSO for ensuring secure and efficient logins in the MyGame platform.

    :::

## Introduction

    \*[Write 2-5 sentences that describe the service or product, including:

    - What it is and what it does
    - Who it’s for
    - How players or developers interact with it
    - Why it’s important or useful]

    :::example

    ## Introduction

    First-party authentication validation is a critical security measure embedded within Single Sign-On (SSO) systems. This validation process verifies the authenticity of a first-party issued authentication token, ensuring that the user is who they claim to be. First-party systems are critical for Digital Rights Management (DRM), Commerce, Multiplayer matchmaking, and more.

    Please be aware that all new apps using first-party authentication must have validation enforced by default.

    **New game applications:** While studios may choose to set up validation later in the development process, it is recommended that validation is set up early to ensure a smoother transition and fewer issues at launch.

    :::

## \*Overview: Architecture Diagram or Flow Description

    \*[The audience of this part is the producers and product managers. They want to see the big picture in a single view from start to finish for evaluation and estimation. Remember to keep the focus on the process. If multiple types of users are involved in the configuration or onboarding, you’ll want to include swim lanes.]

    :::example

    ## Overview: MyGame SSO Identity Validation Flow**

    1. The game client utilizes the SDK to retrieve an authToken.
    2. The client logs into the system account with their MyGame credentials and sends the obtained authToken to the Identity Service.
    3. The Identity Service verifies the authToken by:
        - Checking against the token signing. This involves:
            - Initiating the service without an existing certificate.
            - Requesting and retrieving the certificate from the provided endpoint.
            - Caching the certificate to validate all subsequent authTokens.
            - Identifying and validating any tokens with new signature certificates.
            - Using the Identity Service’s private key to decrypt the authToken.
    4. The token embeds critical SSO data, such as the identiy uid and MyGametag.
    5. A JSON Web Token (JWT) is generated and sent back to the game client, which contains an expiration timeline.
    6. The game client remains authenticated as long as the JWT remains valid.

    :::

## Components

    \*[List and describe the system components that must be configured and the other system's components that are being integrated with.]

    :::example

    ## Components

    - **First-party application setup**: Set up the application for SSO
    - *MyGame first-party application setup**: Request first-party application ID

    :::

## Process Overview Diagram

    \*[If applicable, include a flow diagram of the implementation process steps.]

## Prerequisites

    \*[Provide a detailed description or list of the prerequisites that must be in place prior to working the process steps. (As with code, it is best to update content in only one instance, so link out to content that is repeated, like complicated prerequisite processes, rather than writing and updating it in multiple locations.)]

    :::example

    ## Prerequisites

    - Obtain access to ServiceNow
    - Ensure a completed build

    :::

## Resources

    \*[Provide required and/or helpful information, links to documentation, diagrams, etc.]

    :::example

    ## Resources

    - For Identity setup details, resources, and guides, refer to _MyGame Identity_.

    :::

## Onboarding/Implementation Process

    \*[Describe what users are able to do when the process is complete. Add steps, as needed.]

### Step 1: \*Description [Verb + Noun prase]

    \*[This is a main step of the onboarding process; the sub-steps below this should be numbered if they are performed consecutively.]

    \*[To write useful procedures:

        - Break the step into smaller steps.
        - Use images of user interfaces or code snippets if these are applicable. If you use examples, be sure that you sanitize them so no secure information is exposed.
        - Include who performs the action.
        - Include the context so the user knows where the action originates
        - Include the result of the action or set of actions so the user understands the goal.]

### Step 2: \*Description [Verb + Noun phrase]

:::example

## Publish XBox App with SSO

When the integration process is complete, your Xbox application will be set up to support DNA SSO.

### Step 1: Set up Xbox application for SSO\*\*

Use the following steps in the to set up your application for SSO. You’ll get a _Title ID_ needed for  application setup.

1. Ensure the game setup section is completed.
   - Your System is enabled for your title.
   - Set up a valid sandbox for your title. This is usually done with help from IT.
   - Ensure your title has access to the newly setup sandbox.To test this, look for the newly setup sandbox name in the Primary sandbox dropdown.

   

2. Ensure **MyGame - Single Sign On** section is updated with the website's endpoint.

  

3. Ensure the **title is published to the given sandbox**.

   . . .

### Step 2: Request MyGame first-party application ID

:::

## Configuration (If applicable)

    \*[Frequently, onboarding requires configuration steps following the initial integration steps. Add those here.]

## Build and Publish (If applicable)

    \*[Describe the steps required to generate a build and publish to production if this is part of the onboarding/implementation process]

## Verification Process (If applicable)

    \*[Add steps to demonstrate how the integration is verified.]

## Error Codes or Messages (If available and applicable)

    \*[Make a table that lists any error codes or messages that the user may encounter, what they mean, and what action the user should take if they are displayed. Ideally error messages state actions to take. If this is the case, you can omit this section.]

## Next Steps (Optional)

    \*[Include this section if there is some logical next action that must be taken or link to documentation for that activity.]

    :::example

    ## Next Steps

    - To set up Commerce, refer to _MyGame_ Commerce_.
    - To set up reconciliation for purchases within your game, refer to the _Commerce Integration Guide_.

    :::

## Appendix (Optional)

    \*[Referential materials that will help users understand the topic: diagrams, tables, glossaries, related articles, etc.]
