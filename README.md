# Twitter Internal API Document

Reverse engineering of the web version of Twitter.  
This repository is not complete. Limitations of Static Code Analysis.  
The documentation in the [Develop branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/develop) is automatically updated to the latest version every day at 21:00 UTC.

[Stable branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/master)  /  [Develop branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/develop)  /  [Logged in branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/twitter-login)  /[Twitter Blue branch](https://github.com/fa0311/TwitterInternalAPIDocument/tree/twitter-blue)  

## Document

### GraphQL API

[Twitter Internal GraphQL API Document](./docs/markdown/GraphQL.md)  
[Twitter Internal GraphQL API Json](./docs/json/GraphQL.json)  
[Change Log](./docs/markdown/ChangeLog.md)

### API

[API](./docs/json/API.json)

### Twitter Static Constants

[Twitter Static Constants Document](./docs/markdown/FreezeObject.md)  
[Twitter Static Constants Json](./docs/json/FreezeObject.json)

### Twitter Internationalization

[Twitter Internationalization Json](./docs/json/i18n)

### Twitter Script

[Twitter Script Json](./docs/json/ScriptLoadJson.json)

### Twitter Initial State

[Twitter Initial State Json](./docs/json/InitialState.json)

### Twitter Meta Data

[Twitter Meta Data Json](./docs/json/MetaData.json)

### Reverse Engineering Note

Note written by the developer.  
[Twitter Reverse Engineering Document](./docs/markdown/RE.md)

## Install requirements

```shell
git clone https://github.com/fa0311/TwitterInternalAPIDocument.git
cd TwitterInternalAPIDocument
pip install -r requirements.txt
git clone https://github.com/fa0311/TwitterFrontendFlow.git
```

optional

```shell
python TwitterFrontendFlow/sample2.py

```

## Fast development of modules using this document

```python


```

Can also be used in combination with [TwitterInternalAPIDocument](https://github.com/fa0311/TwitterInternalAPIDocument)

## Reference

- [TechfaneTechnologies/latest-user-agent](https://github.com/TechfaneTechnologies/latest-user-agent)
