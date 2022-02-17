# TARANTULAS INFO
This app serves infos about every tarantula at world.
Datas for create database are scrapped from [The Tarantupedia](https://www.tarantupedia.com/)

## Link
### [TARANTULAS](https://tarantulas.herokuapp.com/tarantulas)

## What info can i get from this API?

At first I have created the API to collect all species names of every Tarantula worldwide. But then i decided to add info about country where it lives in nature. 

## Endpoints
---
    https://tarantulas.herokuapp.com/tarantulas/families

Returns lits of all families and number of species in each

---

    https://tarantulas.herokuapp.com/tarantulas/family/<name of family>'

Returns lits of all genus in the family and number of species in each

---
    https://tarantulas.herokuapp.com/tarantulas/genus/<name of genus>'
Returns lits of all species in the genus and laction where each lives

---
    https://tarantulas.herokuapp.com/tarantulas/location/<name of location>'
Returns list of all species that live in the location

## Reponse

Standard response looks like:\
`curl -i https://tarantulas.herokuapp.com/tarantulas/genus/caribena `:
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
