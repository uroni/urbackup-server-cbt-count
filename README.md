## What is this?

A python script to count the number of recently active CBT clients on a UrBackup server

## Usage

Edit `servers.csv`. Input one server per comma separated line. First column is the server URL, second column the login user name and the third the password. E.g.

```
http://192.168.0.132:55414/x,statususer,status
http://127.0.0.1:55414/x,admin,foobar
```

Running the script with `python3 cbt_count.py` will connect to all servers and write the results to `server_cbt_count.csv`.

## Security

You can create a user on each UrBackup server which has only permissions to see the status of the clients. In the user settings "change rights" of a newly created user, such that there is only one domain "status" with value "all".

## Requirements

At least python 3.4. No other dependencies. 