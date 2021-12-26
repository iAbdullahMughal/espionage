<p align="center">
<img src="https://lh3.googleusercontent.com/NfYrnpBuMyqZGwGqBZ9HR7j0NmuZWaEIOdWq-ZBxoylsWHhVaTXKD_8VJPhZk_-QFyUoJZFRxAYeYM5iphN2A0UeyqD_Hd8w-rpRhzlYQWv01o9GK9Q9mWnTPulNkedLjlZMdkz9" />
</p>

---
<center>
<h3>𝙴𝚜𝚙𝚒𝚘𝚗𝚊𝚐𝚎 - 𝙳𝚘𝚖𝚊𝚒𝚗 𝚁𝚎𝚌𝚘𝚗𝚗𝚊𝚒𝚜𝚜𝚊𝚗𝚌𝚎 𝚃𝚘𝚘𝚕</h3>
</center>

---


# <p> <img width="25" height="25" src="https://cdn-icons-png.flaticon.com/512/1716/1716764.png">  Work in progress ... </p>

## ⚙️Install espionage on system

### Cloning Repo

- Download & install `python 3.6` or above
- Download or clone the repo.
- Create a virtual environment execute followings

```shell
$ git clone https://github.com/iAbdullahMughal/espionage.git
$ cd espionage
$ pip install -r requirements.txt
$ python setup.py build
$ python setup.py install
```

<p align="center">
<img src="https://lh3.googleusercontent.com/q7y3lieNJ4wTPXHr2nzmsgW_Qj4beP4d1ECDxMreOBFLTcGcl5g6q1E6PEw8RhFTmIiuVYKdFTohfd5YNdb9I3HIU6WQ091Qe_bco3LzDZ2ruA6JEhdJdt0Uyrtu4ycu6frhAYck" />
</p>

### Using Pip

- You can install `espionage` by using pip command.

```shell
$ pip install espionage
```

# 🔗 Modules Currently Supported

- [x] 👁️‍🗨️ Domain Availability
    - By using [Mad Checker](https://madchecker.com/)
- [x] 📖 Whois
    - By using [Domain Big Data](https://domainbigdata.com/)
- [ ] 📜 Domain History Based on DNS
    - By using [Hoster Stats](http://www.hosterstats.com)
- [ ] 🎁 Dns Services ️
    - By using [Dns-Lg](http://www.dns-lg.com)


### Status 
[![CircleCI](https://circleci.com/gh/iAbdullahMughal/espionage/tree/main.svg?style=svg)](https://circleci.com/gh/iAbdullahMughal/espionage/tree/main) [![Build Status](https://app.travis-ci.com/iAbdullahMughal/espionage.svg?branch=main)](https://app.travis-ci.com/iAbdullahMughal/espionage) 
### 👁️‍🗨️ Domain Availability Check

- This module check if a domain is available or taken already.

*A domain name locates an organization or other entity on the Internet.*

### 📖 Whois Check

Current module support following in code

#### *Domain Basic Information*

```json
 {
  "basic_info": {
    "Domain": "hacker.com",
    "Words in": "hacker",
    "Date creation": "2004-03-31",
    "Web age": "17 years and 8 months"
  }
}
```

#### *Domain Registrant Info*

```json
 {
  "registrant_info": {
    "Name": "Pinnatech Inc. D.b.a. Nauticom",
    "Organization": "Pinnatech Inc. D.b.a. Nauticom",
    "Email": "domreg@nauticom.net",
    "Address": "4008 Gibsonia Road",
    "City": "Gibsonia",
    "State": "PA",
    "Country": "United States",
    "Phone": "+1.7249339800",
    "Fax": "+1.7249339888",
    "Private": "no"
  }
}
```

#### *Name server records*

```json
 {
  "name_server": {
    "MX": [
      [
        "MX",
        "hacker.com",
        "filter.hacker.com",
        "10",
        "3600",
        "IN"
      ]
    ]
  }
}
```

#### *History Records*

```json
{
  "History": [
    [
      "Date",
      "Status",
      "Name Server"
    ],
    [
      "2014-10-09",
      "Transferred to",
      "consolidated.net"
    ]
  ]
}


```

<p align="center">
<img src="https://lh5.googleusercontent.com/k4aYijBl_3uZByKt019ALda93wNcnLSPuKUt1I8I8A4wahMrAHtekyUzu8gvi3qSoB_4Y6e78El9JGOLy4aLdC23vm-dDuqRjhBfliEKMorA2kokG0ED5drQnC25HdHXkN825t1a" />
</p>


<pre> ⚠️This is an educational project. Don't abuse services.</pre>



 
