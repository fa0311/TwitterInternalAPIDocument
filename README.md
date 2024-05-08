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

## Install requirements

```shell
git clone https://github.com/fa0311/TwitterInternalAPIDocument.git
cd TwitterInternalAPIDocument
pip install -r requirements.txt
```

Optional

```shell
git clone https://github.com/fa0311/TwitterFrontendFlow.git
python TwitterFrontendFlow/sample2.py
```

## Fast development of modules using this document

[Sample](./sample.py)  
[API](./docs/json/API.json)  

## Reference

- [fa0311/latest-user-agent](https://github.com/fa0311/latest-user-agent)
