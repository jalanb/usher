# usher
Usher code onto the correct servers


## Context

To flesh out a reason for these apps to exist.

This project sits between an issue tracker, e.g. Jira, and deployment commands. 

It accepts messages from Jira and prepares deployment commands from the messages.

### Messages

A message from the tracker has a payload with

1. `Issue Id`, e.g. XYZ-123, where

	1.1 `XYZ` is a project name

	1.2 `123` is an identifier within that project

2. `Status` - Some values for status are same as server names, e.g. "beta".

### Queue

We maintain a queue of such messages such that
1. The tracker can write to the queue at any time, one message at a time.
2. The tracker may send duplicate messages
3. Deployment scripts can subscribe to a queue and will periodically read the queue and prepare deployment commands per server per project. 


If status of a message is one of "stage"/"test"/"beta" then prepare a command to deploy to the respective server. A server is named for status and project. For example if the issue is "ABC-111" and status id "beta" then the command will be

	`$ deploy beta.abc.example.com ABC-111`

## Development

### Installation

To install the project, you must first have `Docker` installed and running, then

Clone the repository from GitHub, e.g.
```
$ git clone https://github.com/jalanb/usher.git
```

Install the project directory, e.g.
```
$ pip install -e .
```
To enable optional dependencies for stages of development, such as "tests", "lints", "devops" or "develop" then use the following command, e.g.
```
$ pip install -e .[develop]
```

