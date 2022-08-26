# SKEXIE
<img src= "https://i.imgur.com/T0xQ4a3.png">
<img src= "https://i.imgur.com/1pvPGyx.png">

## Skills and Experience Interpreter and Extractor
Endpoint API for Interpreting skills and experiences from external job posts using NLP (Natural Language Processing) to extract them to the Torre platform’s format.



## File Descriptions
**[application.py](application.py)** - Flask module, for storing the skexie api.

**[/api/skexie/skexie.py](/api/skexie/skexie.py)** - Logic script, uses spaCy3 and re libs to run the incoming text through our custom trained model to process it and return the json list.

## Environment

- This project is interpreted/tested on Ubuntu 20.04 LTS using:
 python3 (version 3.9.5)

## Examples of use
- This `API` works through a `POST` request with a `JSON` containing the raw text from the job offer to analyze: 

```
{
    "text": "Minimum 6 years of relative work experience. Strong AppDynamics product knowledge, internals, and product REST API. Extensive industry experience in deploying AppDynamics for mission critical applications. Working experience in monitoring and performance tools. Strong technical skill sets in PowerShell, Java and Linux shell scripting. Exposure to full application lifecycle development including coding; testing; deployment; and post-implementation activities. Ability to develop AppDynamics Monitoring Extensions. Desired Skills: Experience with AppDynamics integrations with PeopleSoft, .Net and Java. Experience as a developer in Java, .Net, or similar coding languages. Exposure to Cloud environments such as Azure. Exposure to authentication and entitlement management with LDAP or SAML. Exposure to Middleware components such as Webserver, AppServer, Messaging, Integration."
}
```

- It returns a list of the gathered relevant skills and their corresponding experiences in years in `JSON` format as well like so:

```
[
    {
        "experience": 6,
        "skill": "AppDynamics product"
    },
    {
        "experience": 0,
        "skill": "product REST API"
    },
    {
        "experience": 0,
        "skill": "deploying AppDynamics"
    },
    {
        "experience": 0,
        "skill": "PowerShell"
    },
    {
        "experience": 0,
        "skill": "Java"
    },
    {
        "experience": 0,
        "skill": "Linux shell scripting"
    },
    {
        "experience": 0,
        "skill": "AppDynamics integrations"
    },
    {
        "experience": 0,
        "skill": "PeopleSoft"
    },
    {
        "experience": 0,
        "skill": ".Net"
    },
    {
        "experience": 0,
        "skill": "Java"
    },
    {
        "experience": 0,
        "skill": "Java"
    },
    {
        "experience": 0,
        "skill": ".Net"
    },
    {
        "experience": 0,
        "skill": "coding languages"
    },
    {
        "experience": 0,
        "skill": "Azure"
    },
    {
        "experience": 0,
        "skill": "LDAP"
    },
    {
        "experience": 0,
        "skill": "SAML"
    },
    {
        "experience": 0,
        "skill": "Webserver"
    },
    {
        "experience": 0,
        "skill": "AppServer"
    }
]
```




