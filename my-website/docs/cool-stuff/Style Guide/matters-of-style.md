---
title: 'Section 1: Matters of Style'
description: Detailed guidance for document content
sidebar_position: 1
---

# ZMGT Documentation Style Guide

**A note on CSS**: Fonts and colors are generally handled by the Docusaurus CSS so fonts and colors are not included in this style guide apart from as they pertain to screen shots which are created in a separate tool and saved as static images.

## Section 1: Matters of Style

### Audience, Purpose, and Subject

The first considerations of every document are audience, purpose, and subject. For a technical or developer writer these are critical considerations and they should be stated in the first sentence of every document. Let’s define the concepts and explore how to express them in your docs.

- **Audience**: The personas being addressed in the document being authored. It may include the roles or groups of people who have access to the tools (subject) you are writing about. The audience determines the details you choose to include or omit, the vocabulary you use, the choice to use screen shots or diagrams

- **Purpose**: The type of document you are writing. Select a template that provides the sections and content that should be included.

  - Onboarding Guide (OG)
  - User’s Guide (UG)
  - Configuration Guide (CG)
  - Reference (RG)
  - Runbook (RB)
  - Other (O)

- **Subject**: The topic is the product and use case.

**EXAMPLE**: Before you begin writing, jot notes down; then compose your introductory sentence and insert it in the doc just below the title. Every document begins with this simple statement.

**Audience**: Generally \- game teams; specifically \- product deployment team  
**Purpose**: To provide a technical implementation or onboarding guide  
**Subject**: Zynga Connect for Android onboarding or implementation

**Zynga Connect Introductory Statement:** This document is intended to serve as the technical implementation guide for the Zynga Connect ZMGT product users. It provides the information Game Teams require to onboard Zynga Connect for Android.

### Voice and Tense

Use **second** (you, your, yourselves, commands) and **third person voice** (focus on the subject), AND **present tense**.

Do NOT use first person (I, me, myself, us, we, ourselves) AND future (will) or past tense (-ed)

| ❌ NOT this                                                                            | ✅ THIS                                                            |
| :------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| **We** suggest creating a new instance. (first person)                                 | Create a new instance.                                             |
| When the app **was installed**, the option was automatically set to TRUE. (past tense) | The option is automatically set to TRUE when the app is installed. |
| The build **will** automatically kick-off when you merge the PR. (future tense)        | When you merge the PR, the build initiates.                        |

### Style \- Conservation and Specificity

The object of the game is to use the fewest words possible to convey the information needed. Therefore, you want to choose the most specific words to convey your meaning.

| ❌ NOT this                                        | ✅ THIS         |
| :------------------------------------------------- | :-------------- |
| Save the template after the entries are completed. | Click **Save**. |

Titles and Headings  
_What’s in a Name? Would a rose by any other name really smell as sweet?_

It’s important to have a strategy and naming convention for Titles and Headings that is used throughout your documentation library to help your customers stay oriented and keyed into the train of thought of the documentation team’s information architecture and strategy. This small level of mindfulness will not go unnoticed by your customers. Renaming documents and headings is preferred over leaving suboptimal names.

**REMEMBER TO ADJUST LINKS WHEN YOU CHANGE DOC OR HEADING NAMES.**

### Document Titles

Document titles must include the following information in the following order:

- Product-service
- Activity or Purpose: What the document provides to the customer
- Type of document: Guide, Tutorial, Reference, etc
- Version (alternatively, 😣less preferably, date)

**_Examples_**: _Zynga Connect Onboarding Guide v1, JWT Token Passthrough Authentication Alternative to ZIS for PBR V1_

Note that the product or service comes first in this paradigm for easier searching. When the AI tool is implemented, this will mean fewer incorrect responses will be returned.

### Headings

You should have a conscious strategy that you apply to the headings of your document.

Generally avoid the following kinds of headings:

- **Stacked headings**: Avoid placing one heading directly below another.
- **Lone headings**: Each heading should have a corresponding section of text.
- **Overuse of headings**: Use headings sparingly to avoid creating a cluttered or confusing appearance.
- **Articles at the beginning of headings**: Omit articles like "a," "an," and "the" from headings.
- **Headings that exceed 8 words:** Be clear, specific, and concise

Heading strategies may vary by document type. Most documents will have headings like Overview, Introduction, Appendix. These are not part of the general heading strategy.

| Document Type                                | Headings                       | Examples                                           |
| :------------------------------------------- | :----------------------------- | :------------------------------------------------- |
| Informational (Reference)                    | Noun or Adjective Noun         | Headings Parallelism Active Verbs                  |
| Tutorials or How to Documents                | Verb (present tense) \+ Object | Configure Active Directory Groups Create SSL Certs |
| Process Guides (Onboarding or Configuration) | Process components or steps    | Map IDs Set up Payments                            |

In general, good technical documentation is constructed from the general to the specific. So every document will provide a broad overview and then a more specific breakdown before finally providing the deep dive or the meat of the matter. In this way, different audiences can get the level of information they require and drop off or move on.

You should try not to use more than **3 levels of sub-headings** and definitely do NOT use more than **5 levels of sub-headings**.

## Parallelism

Parallelism is a convention whereby any time you have a list, group, or series in a document you mimic the same structure throughout the list . For example in this document all of the headings are expressed either as nouns or as adjective nouns.

Parallelism is a powerful rhetorical tool for keeping your audience oriented and at ease.

| ❌ NOT this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | ✅ THIS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Benefits of using Forge: Alleviate the pain and reduce the costs involved with the complexities when building and deploying games. Free up game team resources for actual game development tasks by automating and delegating tasks to a pipeline. Provides game teams a consistent workflow to build, deploy, and release games across different platforms. Provides game teams with a larger set of standard tools that can be easily incorporated into their build/quality/release flow. Automated processes improve code quality. Company-wide reporting on build/quality/release processes. Builds are more standardized making it easier to roll out new tools to all teams. | Benefits of using Forge: Reduction in the complexity of building and releasing games that results in cost savings Automation of development tasks to pipelines, which frees up team resources Workflow consistency across different platforms for building, deploying and releasing games An expansive standard tool set that can be built into a consistent workflow Improved code quality through automated process control Reporting structures that can be incorporated company-wide Standardized build pipelines that expedite releases |
| Configure GitHub, assign Active Directory roles, and ZID alignment must be done.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Configure GitHub, assign Active Directory roles, and complete ZID alignment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MGT Annual Survey Parameters: Survey Cadence Owners Analysis Communication to MGT Team Leads                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | MGT Annual Survey Parameters: Survey Cadence Owners Analysis Communication                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Notes and Alerts

It’s important to use NOTEs and ALERTs sparingly. These are configured options in Docusaurus styles and are expressed in markdown as follows:

```
:::note

Type your note here.

:::

:::warning

Type your alert here.

:::
```

:::note

Type your note here.

:::

:::warning

Type your alert here.

:::

Other supported callouts: `tip`, `info`, `danger`

For less important notes, you can include the note in parenthesis like this: (**NOTE**: This note is not crazy important.) Use all caps and bold for the label, so it stands out.

```
...parenthesis like this: (**NOTE**: This note is not crazy...
```

## Abbreviations

The first time you use an abbreviation on a page spell it out completely and put the abbreviation in parenthesis beside the spelling. Thereafter, you may use the abbreviation.

**Example**:

Welcome to the Zynga Identity Service (ZIS), a service that simplifies user identification and authentication.  
…  
ZIS is designed with simplicity, consistency and multi platform support in mind. It replaces the Auth, Identities and PlayerId services.

## Lists \- Numbers vs Bullets

All lists whether numbered or bulleted must be preceded by a sentence or two that explain the list that follows. The last clause or phrase before the list may be ended with a colon.

### Numbers

Use numbers ONLY to indicate steps and sequences.

Example:

1. Enter git status.
1. If new content is present enter git add . .
1. Then to commit enter git commit \-m “a message about the content you’re committing”
1. Push the content to the remote repository by entering git push.

### Bullets

Use bullets to indicate:

- Options
- Lists
- Non-sequential items (Use numbers for sequences)

### Bullet and Number Rules

The following are a set of rules to use with lists that use numbers or bullets:

- Lead with a sentence or phrase that describes the purpose of what follows. End the sentence with a colon.
- Add **more than one item** to create a list or sequence.
- Use parallel structure (See “Parallel Structure” in “Section 1: Matters of Style”).
- Begin each item with a capital letter.
- Only end items with periods if they are complete sentences.

| ❌ NOT this                      | ✅ THIS                                      |
| :------------------------------- | :------------------------------------------- |
| Use bullets to indicate options. | Use bullets to indicate: Options Lists Items |

**A Note About Tables:**  
If you have a set of data consisting of only 2 aspects (such as **a term** and **definition**), use bullets rather than putting the data in a table, because the data is easier to maintain and search as text than in a table.

## Third-Party Product References

A general rule of thumb is to avoid documenting 3rd-party products for many reasons:

- The publisher may change the product
- Trademark infringement
- Incorrect information

If for some reason you must provide information about a 3rd-party product, the best practice is to link to the publisher documentation.

Focus all other discussion on the Zynga side of the integration.

DO NOT take screen shots of 3rd-party products or provide detailed walk-throughs of their products.

## Terms to Avoid

- **i.e.** and **e.g**. – Always use **“For example.**” It is clearer and more understandable.

  EXAMPLE: _“A support section must be included that details all of MGT’s support resources (For example: points-of-contact, Slack support channels, and email distribution lists).”_

- **WILL** – As much as possible avoid future tense.

- **WE** – First person plural is awkward

- **WOULD, COULD, SHOULD** – If you use these words to describe an event, you sound like you have little confidence in your product or process.

- **CLICK ON** – instead write CLICK \<button name\>; never “click on” a button) – a differentiator between a professional technical doc writer and an amateur

- **PLEASE** – It’s nice to be polite but not at the risk of brevity.

- **HAS TO/HAVE TO** – Use MUST or MAY instead.

  NOT THIS: The user has to complete process A before beginning process B.  
  THIS: The user must complete process A before beginning process B.

- **Technical Jargon** – Clarity is king. Know your audience and the language they speak.

- **“QR” Code –** QR CodeTM is a trademarked term owned by Denso Wave incorporated. For official publications use a more generic phrase like 'scan a code' instead of saying 'scan the QR code'.
