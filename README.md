# Twitter Internal API Document

Reverse engineering of the web version of Twitter.  
This repository is not complete. Limitations of Static Code Analysis.  
The documentation in the [Develop branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/develop) is automatically updated to the latest version every day at 21:00 UTC.

[Stable branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/master)  /  [Develop branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/develop)  /  [Logged in branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/twitter-login)  /[Twitter Blue branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/twitter-blue)  

## What is this?
This is incomplete documentation of Twitter's internal API.
This is the limit of static analysis, and it is very difficult to improve the system any further.
This document is dedicated to automated analysis at the expense of accuracy.

### How does it work?
Be the first to know about changes to Twitter's internal API.
You can find out information about APIs under development that cannot be called from the UI.
It also serves as a reverse engineering assistant.

### Do you have accurate documentation?
yes.

<https://github.com/fa0311/twitter-openapi>

## About the X-Client-Transaction-Id header?
Unobfuscate `ondemand.s` every day at 22:00 UTC.

<https://github.com/fa0311/twitter-tid-deobf-fork>

## Document

### GraphQL API

[Internal GraphQL API Document](./docs/markdown/GraphQL.md)  
[Twitter Internal GraphQL API Json](./docs/json/GraphQL.json)  
[Change Log](./docs/markdown/ChangeLog.md)

### v1.1 API

[Internal v1.1 Document](./docs/markdown/v1.1.md)  
[Internal v1.1 Json](./docs/json/v1.1.json)  

### Static Constants

[Static Constants Document](./docs/markdown/FreezeObject.md)  
[Static Constants Json](./docs/json/FreezeObject.json)  

### Internationalization

[Internationalization Json](./docs/json/i18n)  

### Script List

[Script List Json](./docs/json/ScriptLoadJson.json)  

### Initial State

[Initial State Json](./docs/json/InitialState.json)  

### Meta Data

[Meta Data Json](./docs/json/MetaData.json)  

### Reverse Engineering Note

Note written by the developer.  
[Reverse Engineering Document](./docs/markdown/RE.md)  

## Run the generator

```shell
uv run python generator.py
```

Put an X cookie export (browser extension JSON or `{name: value}`) at `cookie.json` to scan as a logged-in user.
The logged-out x.com shell no longer ships the responsive-web bundle, so a cookie is required.
`PROXY_LIST` (`host:port:user:pass` per line) is honored; CI gets it from [fa0311/twitter-secrets](https://github.com/fa0311/twitter-secrets).

## Reference

- [fa0311/latest-user-agent](https://github.com/fa0311/latest-user-agent)
