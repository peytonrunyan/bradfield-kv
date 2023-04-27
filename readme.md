# Simple distributed key value store*

### Installation
`pip install .`

### Usage
Start the REPL using `kv`. When you shutdown either by calling `exit` or sending a keyboard interrupt, it will persist the data for next use.

Use commands `get`, `set`, and `exit`
```
$ kv
Welcome to KV Store. Use commands get, set, and exit
Example: get 'mykey'
Example: set 'mykey' 'myvalue'
>>> set dog manny
Key dog set to manny
>>> get dog
Value: manny
```

*Not yet distributed

