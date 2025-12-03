---
title: Configuration Guide
description: Documentation Template - Configuration Guide
---

:::note

To use the template: Replace any content with an \* beside it with content that is similar to the example. Delete this note, all notes in square braces, and examples.

All examples are made up from a fictional example game.

:::

# Documentation Template: Configuration Guide

\*[Provide detailed instructions and information on how to set up, manage, and maintain a system, application, or environment. Typically related to settings.]



## \*Title (Product \+ Document Type)

    [NOTE: The document title uses Heading 1 (a single hash), not Heading 2 (the double hash) as it is here. It is placed under the front matter inside the document.]

    :::example

    ## Game Autoscaling: Multiplayer Configuration Guide

    :::

\*Audience, Purpose, Subject summary statement

    :::example

    This page details how developers can configure the game autoscaling management feature.

    :::

## Introduction

\*[2-5 sentences and/or bullet points that describe the service and technology.

    - What it is and what it does
    - Who it’s for
    - How players or developers interact with it
    - Why it’s important or useful]

    :::example

    ## Introduction

    The autoscaling management feature provides greater flexibility in creating autoscaling configurations and defining rules. To use the feature, developers prepare a JSON configuration and upload it to Cloud Data. The multiplayer service periodically reads and applies this configuration.

    :::

## Prerequisites

\*[Provide a detailed description or list of the prerequisites that must be in place prior to process steps. (As with code, it is best to update content in only one instance, so link out to content that is repeated, such as prerequisite steps, rather than writing and updating it in multiple locations.)]

    :::example

    ## Prerequisites

    - Obtain authorized access to CLI tools
    - Obtain access to Cloud Data

    :::

## Configuration Items

\*[Each configuration item in this section should include:

    - Title/subheadings written as verb \+ noun (per item)
    - Explanation of the configuration item
    - Table of options
    - Description of how configuration changes the behavior of the item
    - Configuration instructions
    - Examples]

    :::example Example 1: Config Items List

    ## Configuration Items

    The autoscaling configuration is a JSON object that contains two list attributes:

    - **scaling_schedules:** Attributes define weekly schedules
    - **override_scaling_events:** Attributes define event date(s) and time(s) when the override configuration takes precedence over other configurations.

    :::


    :::example Example 2: Config Items Table

    | Attributes | Description | Format |
    | --- | --- | --- |
    | **name** | Identifies the **schedule_name** or **event_name** | String |
    | **game** | Identifies **game_name** of the game configured | String |
    |  | **regions** | String |
    |  | **game_types** | String |
    |  | **revision_ids** | String |
    | **default_scale_config** or **scale_config** (override) | Array of attributes that define the default scale configuration or the override scale configuration: |  |

    :::


    :::example Example 3: Config File

    The code sample below represents a full example of an autoscaling configuration that contains both a **schedule** and an **override** event.

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
                "scale_schedule": {
                    "daily_schedule": {
                        "Friday": [
                            {
                                "start": {
                                    "hours": 17,
                                    "minutes": 0
                                },
                                "end": {
                                    "hours": 23,
                                    "minutes": 59
                                },
                                "scale_config": {
                                    "upper_threshold": 0.7,
                                    "lower_threshold": 0.3,
                                    "scale_factor": 2,
                                    "min_replicas": 5,
                                    "block_scale_to_zero_seconds": "600"
                                }
                            }
                        ]
                    },
                    "utc_offset": "-0300"
                }
            }
        ],
        "override_scaling_events": [
            {
                "name": "launch_weekend",
                "game": "awesome_game",
                ]
                },
                "scale_config": {
                    "upper_threshold": 0.7,
                    "lower_threshold": 0.3,
                    "scale_factor": 5,
                    "min_replicas": 10,
                    "block_scale_to_zero_seconds": "600"
                },
                "scale_trigger": {
                    "date_time_trigger": {
                        "start": "2023-09-23T06:00:00.217316Z",
                        "end": "2023-09-24T23:00:00.217316Z",
                        "utc_offset": "-0300"
                    }
                }
            }
        ]
    }

    :::

## Build and Publish (If applicable)

\* Describe the steps required to generate a build and publish to production if this is part of the configuration process.

    :::example

    ## Build and Publish

    Once the JSON configuration with the rules for autoscaling is created, upload it to a specific record in cloud data, where the multiplayer service automatically detects and applies it. Follow these steps:

    1. Go to **Cloud Data**.
    2. Click **\+New Record** to create a new configuration.
    3. Enter the **New Config**.
        

## Verification Process (If applicable)

\* Add steps to demonstrate how the configuration is verified

## Next Steps (Optional)

\* Include this section if there is some logical next action that must be taken or link to documentation for that activity

## Appendix

\* Referential materials that will help users understand the topic: diagrams, tables, glossaries, related articles, etc.
