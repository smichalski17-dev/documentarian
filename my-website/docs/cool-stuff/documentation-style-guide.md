---
title: Documentaiton Style Guide
description: Comprehensive style guide for writing docs as code
---


# Documentation Style Guide

**A note on CSS**: Fonts and colors are generally handled by the Docusaurus CSS so fonts and colors are not included in this style guide apart from as they pertain to screen shots which are created in a separate tool and saved as static images.

## Section 1: Matters of Style

### Audience, Purpose, and Subject

The first considerations of every document are audience, purpose, and subject. For a technical or developer writer these are critical considerations and they should be stated in the first sentence of every document.  Let’s define the concepts and explore how to express them in your docs.

* **Audience**: The personas being addressed in the document being authored. It may include the roles or groups of people who have access to the tools (subject) you are writing about. The audience determines the details you choose to include or omit, the vocabulary you use, the choice to use screen shots or diagrams

* **Purpose**: The type of document you are writing. Select a template that provides the sections and content that should be included.

  * Onboarding Guide (OG)  
  * User’s Guide (UG)  
  * Configuration Guide (CG)  
  * Reference (RG)  
  * Runbook (RB)  
  * Other (O)

* **Subject**: The topic is the product and use case.  

**EXAMPLE**: Before you begin writing, jot notes down; then compose your introductory sentence and insert it in the doc just below the title. Every document begins with this simple statement.

**Audience**: Generally \- game teams; specifically \- product deployment team  
**Purpose**: To provide a technical implementation or onboarding guide  
**Subject**: Zynga Connect for Android onboarding or implementation

   
**Example:** This document is intended to serve as the technical implementation guide for the MyGame product users. It provides the information Game Teams require to onboard MyGame for Android devices. 

## Voice and Tense

Use **second** (you, your, yourselves, commands) and **third person voice** (focus on the subject), AND **present tense**.

Do NOT use first person (I, me, myself, us, we, ourselves) AND future (will)  or past tense (-ed)

| NOT this | THIS |
| :---- | :---- |
| **We** suggest creating a new instance. (first person) | Create a new instance. |
| When the app **was installed**, the option was automatically set to TRUE. (past tense) | The option is automatically set to TRUE when the app is installed. |
| The build **will** automatically kick-off when you merge the PR. (future tense) | When you merge the PR, the build initiates. |

## Style \- Conservation and Specificity

The object of the game is to use the fewest words possible to convey the information needed. Therefore, you want to choose the most specific words to convey your meaning. 

| NOT this | THIS |
| :---- | :---- |
| Save the template after the entries are completed. | Click **Save**. |

Titles and Headings  
*What’s in a Name? Would a rose by any other name really smell as sweet?*

It’s important to have a strategy and naming convention for Titles and Headings that is used throughout your documentation library to help your customers stay oriented and keyed into the train of thought of the documentation team’s information architecture and strategy. This small level of mindfulness will not go unnoticed by your customers. Renaming documents and headings is preferred over leaving suboptimal names. 

**REMEMBER TO ADJUST LINKS WHEN YOU CHANGE DOC OR HEADING NAMES.**

## Document Titles

Document titles must include the following information in the following order:

* Product-service  
* Activity or Purpose: What the document provides to the customer   
* Type of document: Guide, Tutorial, Reference, etc  
* Version (alternatively, 😣less preferably, date)

***Example***: *MyGame Onboarding Guide v1*

## Headings

You should have a conscious strategy that you apply to the headings of your document.

Generally avoid the following kinds of headings:

* **Stacked headings**: Avoid placing one heading directly below another.   
* **Lone headings**: Each heading should have a corresponding section of text.   
* **Overuse of headings**: Use headings sparingly to avoid creating a cluttered or confusing appearance.   
* **Articles at the beginning of headings**: Omit articles like "a," "an," and "the" from headings.   
* **Headings that exceed 8 words:** Be clear, specific, and concise

Heading strategies may vary by document type. Most documents will have headings like Overview, Introduction, Appendix. These are not part of the general heading strategy.

| Document Type | Headings | Examples |
| :---- | :---- | :---- |
|  Informational (Reference) | Noun or Adjective Noun | Headings Parallelism Active Verbs  |
| Tutorials or How to Documents | Verb (present tense) \+ Object  | Configure Active Directory Groups Create SSL Certs |
| Process Guides (Onboarding or Configuration) | Process components or steps  | Map IDs Set up Payments |

   
In general, good technical documentation is constructed from the general to the specific. So every document will provide a broad overview and then a more specific breakdown before finally providing the deep dive or the meat of the matter. In this way, different audiences can get the level of information they require and drop off or move on. 

You should try not to use more than **3 levels of sub-headings** and definitely do NOT use more than **5 levels of sub-headings**.

## Parallelism

Parallelism is a convention whereby any time you have a list, group, or series in a document you mimic the same structure throughout the list . For example in this document all of the headings are expressed either as nouns or as adjective nouns. 

Parallelism is a powerful rhetorical tool for keeping your audience oriented and at ease.

| NOT this | THIS |
| :---- | :---- |
| Benefits of using Forge: Alleviate the pain and reduce the costs involved with the complexities when building and deploying games. Free up game team resources for actual game development tasks by automating and delegating tasks to a pipeline. Provides game teams a consistent workflow to build, deploy, and release games across different platforms. Provides game teams with a larger set of standard tools that can be easily incorporated into their build/quality/release flow. Automated processes improve code quality. Company-wide reporting on build/quality/release processes. Builds are more standardized making it easier to roll out new tools to all teams.  | Benefits of using Forge: Reduction in the complexity of building and releasing games that results in cost savings Automation of development tasks to pipelines, which frees up team resources Workflow consistency across different platforms for building, deploying and releasing games An expansive standard tool set that can be built into a consistent workflow Improved code quality through automated process control Reporting structures that can be incorporated company-wide Standardized build pipelines that expedite releases |
| Configure GitHub, assign Active Directory roles, and ZID alignment must be done. | Configure GitHub, assign Active Directory roles, and complete ZID alignment. |
| MGT Annual Survey Parameters: Survey Cadence Owners Analysis Communication to MGT Team Leads | MGT Annual Survey Parameters: Survey Cadence Owners Analysis Communication |

## Notes and Alerts

It’s important to use NOTEs and ALERTs sparingly. These are configured options in Docusaurus styles and are expressed in markdown as follows:

:::note (or alert)

Type your note or alert here.

:::

For less important notes, you can include the note in parenthesis like this: (**NOTE**: This note is not crazy important.) Use all caps and bold for the label, so it stands out.

*Markdown*: \*\*NOTE\*\*:

## Abbreviations

The first time you use an abbreviation on a page spell it out completely and put the abbreviation in parenthesis beside the spelling. Thereafter, you may use the abbreviation.

**Example**:

Welcome to the Zeus Identity Service (ZIS), a service that simplifies user identification and authentication.  
…  
ZIS is designed with simplicity, consistency and multi platform support in mind. It replaces the Auth, Identities and PlayerId services.

## Lists \- Numbers vs Bullets

All lists whether numbered or bulleted must be preceded by a sentence or two that explain the list that follows. The last clause or phrase before the list may be ended with a colon.

### Numbers

Use numbers ONLY to indicate steps and sequences. 

Example:

1. Enter git status.  
2. If new content is present enter git add . .  
3. Then to commit enter git commit \-m “a message about the content you’re committing”  
4. Push the content to the remote repository by entering git push.

### Bullets

Use bullets to indicate:

* Options  
* Lists  
* Non-sequential items (Use numbers for sequences)

### Bullet and Number Rules

The following are a set of rules to use with lists that use numbers or bullets:

* Lead with a sentence or phrase that describes the purpose of what follows. End the sentence with a colon.  
* Add **more than one item** to create a list or sequence.  
* Use parallel structure (See “Parallel Structure” in “Section 1: Matters of Style”).  
* Begin each item with a capital letter.  
* Only end items with periods if they are complete sentences.

| NOT this | THIS |
| :---- | :---- |
| Use bullets to indicate options.  | Use bullets to indicate: Options Lists Items	 |

**A Note About Tables:**   
If you have a set of data consisting of only 2 aspects (such as **a term** and **definition**), use bullets rather than putting the data in a table, because the data is easier to maintain and search as text than in a table. 

## Third-Party Product References

A general rule of thumb is to avoid documenting 3rd-party products for many reasons:

* The publisher may change the product  
* Trademark infringement  
* Incorrect information

If for some reason you must provide information about a 3rd-party product, the best practice is to link to the publisher documentation. 

Focus all other discussion on the Zynga side of the integration. 

DO NOT take screen shots of 3rd-party products or provide detailed walk-throughs of their products. 

## Terms to Avoid

- **i.e.** and **e.g**. – Always use **“For example.**” It is clearer and more understandable.  

  EXAMPLE: *“A support section must be included that details all of MGT’s support resources (For example: points-of-contact, Slack support channels, and email distribution lists).”*

- **WILL** – As much as possible avoid future tense.

- **WE** –  First person plural is awkward

- **WOULD, COULD, SHOULD** – If you use these words to describe an event, you sound like you have little confidence in your product or process.

- **CLICK ON**  –  instead write CLICK \<button name\>; never “click on” a button) – a differentiator between a professional technical doc writer and an amateur

- **PLEASE** – It’s nice to be polite but not at the risk of brevity.

- **HAS TO/HAVE TO** – Use MUST or MAY instead. 

  NOT THIS: The user has to complete process A before beginning process B.   
  THIS: The user must complete process A before beginning process B.

- **Technical Jargon** – Clarity is king. Know your audience and the language they speak.

- **“QR” Code –** QR CodeTM is a trademarked term owned by Denso Wave incorporated. For official publications use a more generic phrase like 'scan a code' instead of saying 'scan the QR code'.


# Section 2: Capitalization and Punctuation

## Capitalization Rules

Capitalize:

* Product Names  
* Company Names  
* Field Names  
* Occasionally for EMPHASIS


Use Title Case for: (Title Case Capitalizes All Words Except Prepositions and Articles \- First and Last Word Are Capitalized Regardless)

* All Headings in the Docs  
* Image Labels  
* Bullet Lists of Key Components (For bullet lists of activities or descriptions or other longer descriptions use sentence case.)   
   

DO NOT capitalize words that are commonly used product names; only capitalize names if they are trademarked or unique to Zynga or another company.

| NOT this | THIS |
| :---- | :---- |
| **Know product names:**Add Mercury Messaging Service to your Zynga mobile account in Apple. | Add Mercury messaging service to your Zynga Mobile account in Apple.  |
| **Title Case in Headings**Taking a Message and Passing It Through to the End | Taking a Message and Passing It through to the End  |

## Punctuation Rules

### Periods

Use periods only after complete sentences. Do not use periods after phrases, for example, in the case of lists.

| Periods are NOT used here | Periods are used HERE |
| :---- | :---- |
| Zynga Connect Components include the following: Landing page where you download the apps/games Separate game pages for pilot games Tutorial for installation of APKs Google Analytics | This document assumes the following:  The game team has made all product decisions. The game is ready for release.   Information about player interaction with the product is provided purely to assist with contextualizing the use cases and performance of the product. |

### Commas

The general rule of the thumb with commas is, *when in doubt, leave it out*. The following rules, however, are immutable.

* **Series (Oxford) comma**: When a comma comes before the conjunction in a list of items 

  ***Example***: *The people on my team write code, keep track of emerging use cases, interface with new users, and remediate bugs.*

* **Before a conjunction separating 2 independent clauses**: When two complete sentences (independent clauses) are separated by a conjunction creating a single sentence, a comma comes before the conjunction.

  ***Example***: *The documentation portal assists current users by providing practical tutorials,  and its complete product catalog is designed to attract additional users by showcasing the complete range of  ZMGT’s products and services.*


* **After an introductory dependent clause followed by an independent clause.** (The dependent clause always starts with an “ing” verb or a subordinating conjunction)

  ***Example***: *After the game is first launched, the player must accept the terms of service (ToS).*

* **After an adverb or adverbial phrase when they come at the beginning of a sentence.**

  ***Example**: Optionally, you may change the package name, BundleID, used, but this is not necessary.*

* **Around an appositive phrase, a descriptive word or phrase that comes before it.**

  ***Example:** Optionally, you may change the package name, BundleID, used, but this is not necessary.*

* **Around non-essential descriptors or interruptors.**

  ***Example**: Android Playstore’s fees, which we are trying to avoid by using zConnect, have increased every year for the last five years, taking more and more of the profits from game makers.*

* **Within dates and addresses**

  ***Examples:***  
  * *May 15, 2025*  
  * *15 Clearview Drive, Phelps, New York USA*

* Commas not much used in technical writing:  
  * **Direct address**: Fritz, please calm down.  
  * **Dialog**: On the seventh day, the developer looked up from his code and proclaimed, “It is good; it is very good.” And it was.

### Colons

Colons are used to: 

* Set off  lists either when they are bulleted or numbered  
* Set off a list within a sentence or paragraph  
* Separate a term from its definition or description in technical writing

| Colons are used HERE | and HERE |
| :---- | :---- |
| Games published under these accounts have the Apple publishing configuration baked in, and no additional steps must be taken for: Zynga, Inc.; Zynga Mobile; Zynga Game Network, Inc.; Town’s End Studio, LLC; and Rollic Games. | This document assumes the following:  The game team has made all product decisions. The game is ready for release.   Information about player interaction with the product is provided purely to assist with contextualizing the use cases and performance of the product. |

### Semi-Colons

Semi colons are used in only 2 cases:

* **To replace a comma between a conjunction separating clauses**: When two complete sentences (clauses) are separated by a conjunction creating a single sentence, a semicolon may replace the comma that comes before the conjunction. This is usually done when the topic is closely related.


  ***Example***: *Only users with Admin permissions are able to run the GET userlist API call; the userlist returns PII that must be kept secure.* 


* **To replace the first level of commas in a complex series**: When the sentence contains a series and one or more of those series also contains a series 

  ***Example***: *Three teams contributed to the project: the Core team built out the APIs, setup the database, and wrote the Kubernetes jobs; the UI team developed the forms, wrote the wizard, and created the messaging tool; and the QA team ran the API calls, wrote automated tests for the UI, and documented the test plan.*

* **When too many commas complicate a sentence***.* The requirement of the commas in the game company names plus the series commas would make this sentence confusing, so we replace the series commas with semi-colons.

  ***Example:** Games published under these accounts have the Apple publishing configuration baked in, and no additional steps must be taken for: Zynga, Inc.; Zynga Mobile; Zynga Game Network, Inc.; Town’s End Studio, LLC; and Rollic Games.*

### Dashes

There are 2 kinds of dashes that are used for specific purposes in technical writing. 

**En Dashes (**do not require spaces on either side):

* **Ranges**: Used to indicate a range between numbers, dates, or periods. 

  ***Example**: "The reaction time was between 1–3 seconds."* 

  * **Compound Modifiers:** Join compound modifiers, especially when they are already hyphenated or consist of two-word nouns. 

    ***Example**: "The condensed matter–biology interface is complex."* 

  * **Between Dates/Years:** Used to separate dates or years within a range. 

    ***Example**: "The project spanned from 2020–2022."* 

    

**Em Dashes (**require spaces on either side):

* **Parenthetical Information**: Used to set off parenthetical information within a sentence, similar to parentheses but with more emphasis. 

  ***Example**: "The device — designed for portability — is easy to use."* 

  * **Marking a Break**: Can be used to mark a break in a sentence, often to indicate a sudden change in thought or tone. 

    ***Example**: "The results were surprising — we didn't expect such a high failure rate."* 

  * **Emphasis**: Can be used to highlight information that is being emphasized. 

    ***Example**: "The key to success — consistent effort — is often overlooked."* 

# Section 3: Active Verbs 

## Handy List of Active Verbs for Technical Writers

Accelerate Add Adopt Aggregate Analyze Apply Assemble Authenticate Automate Back-up Balance Block Boost Branch Bridge Build Bundle Calculate Calibrate Certify Change Check Classify Clean Cleanse Clear Code Collocate Compute Computerize Configure Consolidate Construct Corrected Debug Decipher Decode Dedicate Defend Deliver Deploy Digitize Discover Dispatch Distribute Duplicate Enable Engineer Enhance Equip Eradicate Evaluate Extend Extract Extrapolate Fabricate Finalize Fine-Tune Format Group Host Identify Implement Initialize Install Integrate Isolate Launch License Link Load Maintain Manufacture Map Mechanize Merge Migrate Mined Mirror Mobilize Model Modified Move Network Neutralize Operate Optimize Overhaul Package Patch Penetrate Pinpoint Prevente Prioritize Process Program Protect Prototype Qualify Rank Realign Reboot Rebuild Reconcile Reconstruct Recover Rectify Refresh Reinforce Release Remodel Replicate Restore Retool Retrieve Retrofit Revamp Revise Roll-out Rotate Route Safeguard Salvage Scan Scope Scrub Secure Select Sequence Solve Stabilize Standardize Straddle Systematize Test Toggle Trace Transition Update Upgrade Validate Verify Virtualize Web-enable 


# Section 4: Markdown Guidance

## Markdown Guidance

I only included a few basics here. For more markdown guidance go [here](https://www.markdownguide.org/basic-syntax/).

### How to Format Links

#### Add links to other pages in our site

Use standard markdown link syntax with a path relative to the docs root with a leading slash.

Examples:  

* \[Link text\](/about.md) \--\> goes to the `about.md` page in the root directory.   
* \[Link text\](/about.md\#how-does-MDS-work) \--\> goes to an anchor on the Overview page.   
* \[Link text\](/MDS/notifications.md) \--\> goes to the notifications.md page in the MDS directory.

#### Add links to external pages

Use standard markdown syntax: \[Link text\](https://google.com)

### How to Format Images

(See “How to Annotate Screenshots” below)

#### Markdown format in file: 

\!\[Image alt tag value\](/zynga/img/filename.png)

#### Image Storage

Images are saved as .png files in the website/static/img folder.

File naming convention: tool-section-function-step.png (If any part of the naming convention in not applicable, simply omit it)

### How to Format Videos

Videos should adhere to the following conventions:

* No more than 3 minutes long.  
* Always include narration that explains the visual content. Keep it simple and clear.  
* Orient the user as to where they are in the UI \- page, tab, window  
* Visual content should move slowly and smoothly, avoiding jumping and quick mouse moves. 

The way to achieve the best result is to:

* Write out the script   
* Practice the video before you produce  
* Use a tool like Camtasia so content can be easily edited. 


### How To Format Front Matter

The sidebar is automatically created from the front matter.

At the top of each page you must add the following, which provides the sidebar content and heading.

\---  
title: "This is the Title"  
linkTitle: "This is the Title"  
description: \>  
 This is a short description of the contents of the page.  
\---

### How to Format Tables 

To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column. For compatibility, you should also add a pipe on either end of the row.

#### Tables with uniform column widths

`| Syntax      | Description |`  
`| ----------- | ----------- |`  
`| Header      | Title       |`  
`| Paragraph   | Text        |`

#### Tables with different column widths

`| Syntax | Description |`  
`| --- | ----------- |`  
`| Header | Title |`  
`| Paragraph | Text |`

#### Tables with Alignment Left, Center, and Right

`| Syntax      | Description | Test Text     |`  
`| :---        |    :----:   |          ---: |`  
`| Header      | Title       | Here's this   |`  
`| Paragraph   | Text        | And more      |`

### How to Format Code and Code Blocks

To generate a code block:

````   
`{`  
  `"firstName": "John",`  
  `"lastName": "Smith",`  
  `"age": 25`  
`}`  
```` 

You may also add the type of code after the first set of tics to further define the formatting.

 ```json
    {
        "scaling_schedules": [
            {
                "name": "my_schedule",
                "game": "awesome_game",
                ]
                },
                "default_scale_config": {
                    "upper_threshold": 0.7,
                    "lower_threshold": 0.3,
                    "scale_factor": 2,
                    "min_replicas": 1,
                    "block_scale_to_zero_seconds": "600"
                },
```                

To add code to a line of text, put tickmarks around the code you want formatted, like  \``"firstName": "John"`\`, and it will be displayed correctly.



# Section 5: Formatting and Annotations

## How to Annotate Screenshots

**NOTE:** Annotations were done in SnagIt.

Screen shot  formatting rules:

* Crop out the menus (when possible), so that the image is easier to maintain.  
* Annotations  
  * Color: Primary Blue \- \#0078E5; rgb(0, 120, 229\)  
  * Alt Color: Zynga Brand Red \- \#DC0606; rgb(220, 6, 6\)  
  * Font: Helvetica Nue | 16pt | 400 weight |   
  * Numbering Style: ![][image1](point toward the item)  
    **NOTE**: It is not necessary to use numbering on screenshots, but if you choose to do so, use it consistently.  
* Sizing (to ensure consistent proportions): width between 1000 and 1200 pixels  
* Highlighter: yellow 75% opacity  
* Arrows: 3pt   
* Boxes: 3pt, rectangular with rounded corners  
* Callouts: 3pt, rectangular with rounded corners  
* Blur: Information that is not sensitive (blurred info can be decoded), intensity \= 2-4  
* Remove sensitive data: keys, PID, etc  
* Borders:   
  * All sides  
  * Color=black  
  * 1pt  
  * No shadows

![Annotated screenshot](/styleguide.jpg)

