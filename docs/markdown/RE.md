# Twitter Reverse Engineering Document<br>

## Requests

### graphQL()

```args
metadata, operationName, operationType, query
```

### graphQLFullResponse()

```args
metadata, operationName, operationType, query, queryId
```

### getURT()

```
path: /2/{0}{3}
method: GET
params: {1}
headers: {2}
timeout: {3}
```

### getUnversioned()

```
path: {0}
method: GET
params: {1}
headers: {2}
host: {3}
```

### delete()

```
path: /1.1/{0}{3}
method: DELETE
params: {1}
headers: {2}
```

### deleteURT()

```
path: /2/{0}{3}
method: DELETE
params: {1}
headers: {2}
```

### post()

```
path: /1.1/{0}{4}
method: POST
params: {2}
data: {1}
headers: {3}
host: {5}
```

### postI()

```
path: /i/{0}{3}
method: POST
data: {1}
headers: {2}
```

### postUnversioned()

```
path: {0}
method: POST
data: {1}
headers: {2}
host: {3}
```

### postURT()

```
path: /2/{0}{4}
method: POST
data: {1}
headers: {2}
host: {3}
```

### postURT()

```
path: /1.1/{0}{3}
method: PUT
data: {1}
headers: {2}
```
