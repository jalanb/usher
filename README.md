# Usher

An `usher` is antonymical to a `tracker`.

It helps code to find the right `server`, in response to changes on an `issue`.

## TLDR

### Run

"How do I run this thing?" is [below](Fred).

### Walk

My current workflow uses 3 Gippities

1. OpenAI in MacApp (see what we thought about `usher` [here](https://chatgpt.com/share/675e5c32-b6a4-800f-9264-7a7eed8c6ba7)).
2. OpenAI in Browser (`usher` is [here](https://chatgpt.com/share/675e4fe1-7dac-800f-bfd5-c494694fe666)).
3. Claude, within [Windsurf](https://codeium.com/windsurf). 

1: I use the OpenAI Gippity in the MacApp for a higher level view, discourage coding, play dumb, imagine alternatives, tell Claude what to do.

2: I always have OpenAI open in a few browsers as well, for details, follow ups, and gossip.

3: I use Anthropic's Claude Gippity for direct coding, inside the [Windsurf](https://codeium.com/windsurf) IDE.

Claude needs less correction for coding **my way**, which speeds things up.

## Context

To flesh out a reason for these apps to exist, make it easier to find edge cases.

### WWTS (2015 - 2024)

This project sits between our `issue` `tracker`, Jira, and our `deploy`ment commands. 

Jira can send us `message`s when an `issue` changes `status`.

We need an app on the build server to catch 'em. 

On the build server, so must be fully, whassname[^1], ..., `Docker` compatible. Y'know yourself.

### Asynchrony

We get a lot of users who come from meetings, start doing testing, updating Jira, triggering deployments. We have seen the same issue moved 1 time to `Test` and 4 times to `Beta` in 7 minutes, after one of their big Tuesday afternoon meetings!

A full deployment, even to a test server, can take 20 minutes. 

We need to minimise deployments in "hot times", proceed in an orderly manner.

Hence we need to disconnect the timing of Jira actions from the deployment actions, and some kinda `queue`, aka `Q`, would do that for us.

 'Specially if we did it `async`, use that new `FastAPI` we all wanna try, eh?

 😎 

#### Apps

`server` app holds the `Q`

`trackers` app should accept Jira `message`s, whenever, and add them to `Q`

`deploys` app should often prepare `deploy` commands from the messages in `Q`.

`successes` app should clean the `Q` after deploys are "Pass" (`v1.1` ?)


## Design

WIP (not a surprise).

### Message

A `message` from Jira has a payload with

1. `Issue Id`, e.g. XYZ-123, where

	1.1 "XYZ" is a project name

	1.2 "123" is an identifier within that project

2. `Status` 

    We ignore most statuses, only noticing `issue`s going to `stage`, `test`, or `beta`.

#### Messages

**YAGNI**!!!

Yes, yes, calm down, we need an excuse to show the good way forward.

We will implement 2 kinds of `message`s

* front end
* back end

Do something with the `front` end one, make it look different, use `pydantic` to check `project` exists, or something. No pressure, just, like, this _is_ an extended interview! 

What fourth wall?

### Queue

We need a `queue` of `message`s at `v0.9` such that

1. The tracker can write to the queue at any time, one message at a time.

   1.1. The tracker can send duplicate messages (`v1.0`/Needed ?)

2. Deployment scripts can find servers, and their project's issues, in the queue.
3. Deployment scripts can remove messages on success (`v1.1` ?)

### Serve Status 

If the new `status` of a `message` is not `stage`, `test`, `beta`, ignore it.

The `status` and `project` determine the `server`, for example: 

    "beta" and "abc" deploys to server `beta.abc.wwts.com` (internal).

So a full command might be

         $ python -m wwts.devops.deploy beta.abc.wwts.com ABC-111 ABC-113

And that allows the normal abbreviations

         $ python -m wwts.devops.deploy abc beta 111 113

# Run

## Users

To just run it do this

```python
import usher
```

## Developers

### Installation

To install the project, you must first have `Docker` installed and running, then

Clone the repository from GitHub, e.g.
```
$ git clone https://github.com/jalanb/usher.git
$ cd usher
```

Install the project directory, e.g.
```
$ pip install -e .
```
To enable optional dependencies for stages of development, such as "tests", "lints", "devops" or "develop" then use the following command, e.g.
```
$ pip install -e .[develop]
```

[^1]: “Bugrit! Millennium hand and shrimp!”
