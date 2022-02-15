# TARANTULAS INFO
This app serves infos about every tarantula at world.
Datas for create database are scrapped from [The Tarantupedia](https://www.tarantupedia.com/)

## What info can i get from this API?

At first I have created the API to collect all species names of every Tarantula worldwide. But then i decided to add info about country where it lives in nature. 

## Endpoints
---
    [hostname]/tarantulas/families

Returns lits of all families and number of species in each

---

    [hostname]/tarantulas/family/<name of family>'

Returns lits of all genus in the family and number of species in each

---
    [hostname]/tarantulas/genus/<name of genus>'
Returns lits of all species in the genus and laction where each lives

---
    [hostname]/tarantulas/location/<name of location>'
Returns list of all species that live in the location

## Reponse

Standard response looks like:\
`curl -i http://localhost:8000/tarantulas/genus/caribena `:
```json
{
  "Caribena": [
    {
      "family": "Aviculariinae", 
      "location": [
        "Puerto Rico", 
        "Brazil"
      ], 
      "species": "Caribena laeta"
    }, 
    {
      "family": "Aviculariinae", 
      "location": [
        "Martinique"
      ], 
      "species": "Caribena versicolor"
    }
  ]
}
```

## How to run the API

1. Download all files
2. Create file `database.ini`
3. The file should looks like:

```
[postgresql]
host=YOURHOSTNAME
database=YOURDATABASENAME
user=YOURUSERNAME
password=YOURPASSWORD
```
4. run program with:\
`python main.py`
5. Where can you get data? Some day I will setup a database and paste the link here. For now - it;s just a portfolio project ;)