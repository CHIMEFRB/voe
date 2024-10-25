|   **`Status`**   | **`Coverage`**  |   **`Docs`**    |  **`Site Release`**  |   **`Style`**    |
|-----------------|-----------------|-----------------|-----------------| -----------------|
[![Continous Integration](https://github.com/CHIMEFRB/voe/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/CHIMEFRB/voe/actions/workflows/ci.yml) | [![Coverage Status](https://coveralls.io/repos/github/CHIMEFRB/voe/badge.svg?branch=main)](https://coveralls.io/github/CHIMEFRB/voe?branch=main) | `TBA` | `2024.05.xx` | [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/) |
---

# frb-voe : An FRB Virtual Observatory Event Service

`frb-voe` is a telescope-agnostic server for publishing, broadcasting, and recording Virtual Observatory Events (VOEvents) for detections of Fast Radio Bursts (FRBs). Telescopes and observatories that are actively detecting or following up FRBs can establish a subscription-based FRB VOEvent service using `frb-voe`. The core functionality of the code base is the following tasks:

- Publish VOEvents that follow an extension to the FRB VOEvent Standard originally prescribed in [Petroff et al. 2017](https://arxiv.org/abs/1710.08155) using a [Comet broker](https://www.sciencedirect.com/science/article/pii/S2213133714000407) and/or an SMTP email server.
- Maintain and interact with a [Mongo Database](https://www.mongodb.com/) of VOEvent metadata and subscribers information.
- Submit FRBs to the [Transient Name Server](https://www.wis-tns.org) (TNS).

![frb-voe-workflow](/frb-voe-workflow.png?raw=true "The frb-voe Workflow")


# Installation
## Dependencies Installation

The following are instructions for installing the frb-voe package and running the TNS service.

First, `cd` into your preferred path `/my/path` and clone the repository.

```
git clone git@github.com:CHIMEFRB/voe.git
```

Now, move into the repo:

```
cd voe
```

And build the docker container and initialize the servers and database. If you do not have docker installed on your system, instructions can be found here: https://docs.docker.com/get-docker/.

```
docker compose build
```
Note: MongoDB is set to run at port 27017 by default. Ensure nothing is running at this port, or, choose another port by changing the SANIC_MONGODB_PORT variable in the docker-compose.yaml file (and the corresponding ports in the mongo configuration). 


# Getting Started

## Configuring Your Observatory
The `frb-voe` software operates using HTTP requests, in order to initiate the publication of a VOEvent from your observatory, a correctly formatted HTTP request must be sent to your `frb-voe` server. This request is required to contain the burst metadata (for "detection" and "subsequent" type VOEvents, or an update message or internal ID for "update" and "retraction" type VOEvents, respectively). This can be accomplished manually, or from an automated request being sent from the host observatory to the `frb-voe` server upon detection of a new event. An example script demonstrating this is provided in the `examples` directory.

## Environment Variables

Certain aspects of the service (such as SMTP servers and interactions with the TNS) require sensitive information such as passwords and API keys. To use these services, it is recommended that you pass these secrets as environment variables. These must be added to your bash profile with the following naming convention.

- FRB_VOE_EMAIL_ADDRESS
- FRB_VOE_EMAIL_PASSWORD
- FRB_VOE_TNS_API_KEY
- FRB_VOE_TNS_BOT_NAME
- FRB_VOE_TNS_BOT_ID

To obtain a TNS API key, bot name, and bot ID, proceed to the next section.

## Registering on the TNS

The TNS is the official IAU-recognized distributor and maintainer of the naming scheme for FRBs. All programmatic requests to the TNS require authentication. This in turn requires registration on the TNS web portal. To complete the registration process and obtain required authorization, follow these steps:

1. Request a User Account [here](https://www.wis-tns.org/user/register). If you had additional team members who will manage your TNS data, they should also create a User Account.
2. Log in [here](https://www.wis-tns.org/user).
3. Edit your TNS Group members [here](https://www.wis-tns.org/groups).
4. Add a TNS bot [here](https://www.wis-tns.org/bots). This is required in order to obtain the credentials that are needed for making programmatic requests to the TNS via the API that is embedded in `frb-voe`.
5. Once your TNS bot has been created, it will appear in the table on [this](https://www.wis-tns.org/bots) page. In the rightmost column you can click *edit* to view or change its properties. In particular, the *Edit Bot* page allows one to create a new API key for the bot at any time.
6. From the *Edit Bot* page, one can obtain values for the environment variables that are required to use the TNS functionality of `frb-voe`.
    - `FRB_VOE_TNS_API_KEY` from the API alphanumeric key value.
    - `FRB_VOE_TNS_BOT_ID` from the `"tns_id"` key in the `User-Agent` specification.
    - `FRB_VOE_TNS_BOT_NAME` from the `"name"` key in the `User-Agent` specification.

# frb-voe Client User Interface (CLI) Usage

**Once the frb-voe backend is started**, a dedicated CLI can be used for all interactions software.

## Interacting with the frb-voe Server

```
poetry run frbvoe voe [COMMAND] [OPTIONS]
```
### Send a VOEvent

```
poetry run frbvoe voe send --help
```

## Interact with the Subscriber Database

```
poetry run frbvoe subscriber [COMMAND] [OPTIONS]
```
### Adding a subscriber

```
poetry run frbvoe subscriber add --help
```

## Interact with the TNS

```
poetry run frbvoe tns [COMMAND] [OPTIONS]
```

### Submit an FRB

When you have the event number of a FRB Candidate that needs to be submitted to the TNS, use the following command to acquire the TNS name.

```
poetry run frbvoe tns submit --help
```

The help dialogue will explain what options are required and what data is needed from the user. These include:

- event number
- proprietary period length (in years)

Optionally, one can practice the submission by setting the `--sandbox` flag in the call signature.


### Contributing

All motivated community members are welcomed and encouraged to contribute to the frb-voe Service. Contributions should be initiated with an issue and corresponding development branch. We encourage users to write tests for their contributed code, which can be run locally using: 

```poetry run pytest --cov-report=html --cov .```

The repository is formatted according to pre-commit, to run pre-commit locally, use: 

```pre-commit run --all-files```