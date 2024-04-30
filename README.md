[![Coverage Status](https://coveralls.io/repos/github/CHIMEFRB/voe/badge.svg?branch=main)](https://coveralls.io/github/CHIMEFRB/voe?branch=main)
---
# Overview : A Telescope-Agnostic FRB Virtual Observatory Event (VOEvent) Service

`frb-voe` is a telescope-agnostic server for publishing, broadcasting, and recording Virtual Observatory Events (VOEvents) for detections of Fast Radio Bursts (FRBs). Telescopes and observatories that are actively detecting or following up FRBs in the radio regime can establish a subscription-based FRB VOEvent service using `frb-voe`. The core functionality of the code base is the following tasks:

- Start and stop a [Comet](https://comet.transientskp.org/en/stable/) VOEvent broker.
- Publish VOEvents that follow an extension to the FRB VOEvent Standard originally prescribed in [Petroff et al. 2017](https://arxiv.org/abs/1710.08155) and broadcast them using the Comet broker.
- Maintain a database of subscribers that can receive the VOEvent broadcast from the Comet broker.
- Submit FRBs to the [Transient Name Server](https://www.wis-tns.org) (TNS).


# Installation
## Dependencies Installation

The following are instructions for installing the frb-voe package and running the TNS service.

First, `cd` into your preferred path `/my/path` and clone the repository.

```
git clone git@github.com:CHIMEFRB/voe.git
```

Now, install `poetry` with

```
pip install poetry
```

Then install the requirements using `poetry` by running the following in the top-level folder where the `poetry.lock` file is found.

```
poetry install
```

# Getting Started

## Registering on the TNS

The TNS is the official IAU-recognized distributor and maintainer of the naming scheme for FRBs, as previously announced in the FRB 2020 virtual conference (watch the first presentation in Session 11 from the conference [here](https://www.youtube.com/watch?v=mgqXDtYDPJE&list=PLPIVxyomLL89sdsz770tYRWJL048H5CtE&index=11&t=394s&ab_channel=FRB2020)).

All programmatic requests to the TNS require authentication. This in turn requires registration on the TNS web portal. To complete the registration process and obtain required authorization, follow these steps:

1. Request a User Account [here](https://www.wis-tns.org/user/register). If you had additional team members who will manage your TNS data, they should also create a User Account.
2. Log in [here](https://www.wis-tns.org/user).
3. Edit your TNS Group members [here](https://www.wis-tns.org/groups).
4. Add a TNS bot [here](https://www.wis-tns.org/bots). This is required in order to obtain the credentials that are needed for making programmatic requests to the TNS via the API that is embedded in `frb-voe`.
5. Once your TNS bot has been created, it will appear in the table on [this](https://www.wis-tns.org/bots) page. In the rightmost column you can click *edit* to view or change its properties. In particular, the *Edit Bot* page allows one to create a new API key for the bot at any time.
6. From the *Edit Bot* page, one can obtain values for the environment variables that are required to use the TNS functionality of `frb-voe`.
    - `TNS_API_KEY` from the API alphanumeric key value.
    - `TNS_API_ID` from the `"tns_id"` key in the `User-Agent` specification.
    - `TNS_API_BOT_NAME` from the `"name"` key in the `User-Agent` specification.
7. set the following environment variables using the values that were provided to you or your organization when registering for usage of the TNS.
```
export TNS_API_KEY=""       # Alphanumeric API key for your TNS bot
export TNS_API_TNS_ID=""    # ID number for your TNS bot
export TNS_API_BOT_NAME=""  # Name of your TNS bot
```

## MongoDB Setup

Docker is a reliable way to set up a containerized MongoDB server. Follow directions to install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on your machine. A MongoDB server is required to host the databases used by `frb-voe` and this can be set up to run in a docker container on a standard port.

## Interact with the TNS

**Once the frb-voe backend is started**, a dedicated CLI can be used for all interactions with the [Transient Name Server](https://www.wis-tns.org/). The command signature is the following:

```
poetry run frb-voe tns [COMMAND] [OPTIONS]
```
Be sure that:
1. The environment variables are properly set
2. You're in the `frb-voe` conda environment
3. Run `poetry run maestro start` to start the server

### Submit an FRB

When you have the event number of a FRB Candidate that needs to be submitted to the TNS, use the following command to acquire the TNS name.

```
poetry run frb-voe tns chimefrb-submit --help
```

The help dialogue will explain what options are required and what data is needed from the user. These include:

- event number
- proprietary period length (in years)

Optionally, one can practice the submission by setting the `--sandbox` flag in the call signature.

# NOTES: 

Layout:
- observatory (L4) will send an HTML request contiaining all the information needed to create a VOEvent to voe.
- voe will validate the dictionary using Pydantic, publish it to comet and save it to a MongoDB
- voe will periodically check the MongoDB for new subscribers and for newly retracted FRBs
- voe will also be able to submit FRBs from the MongoDB to the TNS through a CLI

Desired Features:
- easy installation through docker to compose the voe service, MongoDB, and comet service in one swoop

Environment variables: To use the service, you must have the following environment variables defined in your bash profile. TNS Bots can be registered here: https://www.wis-tns.org/bots.
- FRB_VOE_TNS_API_KEY
- FRB_VOE_TNS_BOT_NAME
- FRB_VOE_TNS_BOT_ID
- FRB_VOE_EMAIL_ADDRESS
- FRB_VOE_EMAIL_PASSWORD
