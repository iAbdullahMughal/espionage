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

### Using Pip

- You can install `espionage` by using pip command.

```shell
$ pip install espionage
```

### Console Example

#### Command in terminal 
```shell
python main.py -d "www.hacker.com" --json --extended
# --json this flag allows results on console in json format
# --extended  this flag allows to fetch extended result for domain
```

#### Output Json
```json
{
  "domain_address": "www.hacker.com",
  "domain_availability": false,
  "whois_record": {
    "basic_info": {
      "Domain": "hacker.com",
      "Words in": "hacker",
      "Date creation": "2004-03-31",
      "Web age": "17 years and 8 months"
    },
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
    },
    "other_tld": [
      "hacker.ae",
      "hacker.africa",
      "hacker.ar",
      "hacker.agency",
      "hacker.amsterdam",
      "hacker.ag",
      "hacker.biz",
      "hacker.ca",
      "hacker.at",
      "hacker.be",
      "hacker.boutique",
      "hacker.black",
      "hacker.blue",
      "hacker.bet",
      "hacker.co.il",
      "hacker.co",
      "hacker.ch",
      "hacker.co.kr",
      "hacker.cn",
      "hacker.codes",
      "hacker.club",
      "hacker.college",
      "hacker.casa",
      "hacker.center",
      "hacker.coffee",
      "hacker.coach",
      "hacker.cat",
      "hacker.ceo",
      "hacker.capital",
      "hacker.church",
      "hacker.com.cn",
      "hacker.dp.ua",
      "hacker.dk",
      "hacker.com.eg",
      "hacker.com.au",
      "hacker.eu",
      "hacker.cz",
      "hacker.de",
      "hacker.com.co",
      "hacker.design",
      "hacker.cx",
      "hacker.fund",
      "hacker.dj",
      "hacker.fr",
      "hacker.fyi",
      "hacker.engineering",
      "hacker.com.pl",
      "hacker.earth",
      "hacker.ga",
      "hacker.farm",
      "hacker.foundation",
      "hacker.direct",
      "hacker.company",
      "hacker.fitness",
      "hacker.express",
      "hacker.edu.vn",
      "hacker.equipment",
      "hacker.domains",
      "hacker.digital",
      "hacker.family",
      "hacker.community",
      "hacker.contractors",
      "hacker.net",
      "hacker.info",
      "hacker.org",
      "hacker.rs",
      "hacker.jp",
      "hacker.lk",
      "hacker.lv",
      "hacker.lu",
      "hacker.ind.br",
      "hacker.ru",
      "hacker.it",
      "hacker.pl",
      "hacker.ro",
      "hacker.hu",
      "hacker.se",
      "hacker.in",
      "hacker.nl",
      "hacker.inf.br",
      "hacker.surf",
      "hacker.one",
      "hacker.sg",
      "hacker.no",
      "hacker.style",
      "hacker.systems",
      "hacker.horse",
      "hacker.pro",
      "hacker.house",
      "hacker.im",
      "hacker.ltd",
      "hacker.or.jp",
      "hacker.live",
      "hacker.kaufen",
      "hacker.miami",
      "hacker.hamburg",
      "hacker.pizza",
      "hacker.school",
      "hacker.re.kr",
      "hacker.ps",
      "hacker.haus",
      "hacker.taxi",
      "hacker.plus",
      "hacker.international",
      "hacker.solutions",
      "hacker.guide",
      "hacker.market",
      "hacker.kr",
      "hacker.nyc",
      "hacker.mn",
      "hacker.tel",
      "hacker.shopping",
      "hacker.io",
      "hacker.money",
      "hacker.garden",
      "hacker.how",
      "hacker.holdings",
      "hacker.investments",
      "hacker.supply",
      "hacker.studio",
      "hacker.pub",
      "hacker.stream",
      "hacker.mom",
      "hacker.sexy",
      "hacker.rehab",
      "hacker.reviews",
      "hacker.us",
      "hacker.ua",
      "hacker.tk",
      "hacker.works",
      "hacker.xyz",
      "hacker.today",
      "hacker.za",
      "hacker.world",
      "hacker.zone",
      "hacker.tips",
      "hacker.ventures",
      "hacker.uk",
      "hacker.vip",
      "hacker.trade",
      "hacker.web.tr"
    ],
    "whois_data": [
      "Domain Name: HACKER.COM",
      "Registry Domain ID: 648983_DOMAIN_COM-VRSN",
      "Registrar WHOIS Server: whois.networksolutions.com",
      "Registrar URL: http://networksolutions.com",
      "Updated Date: 2015-01-29T00:01:45Z",
      "Creation Date: 2004-03-31T06:45:45Z",
      "Registrar Registration Expiration Date: 2015-08-21T04:00:00Z",
      "Registrar: NETWORK SOLUTIONS, LLC.",
      "Registrar IANA ID: 2",
      "Registrar Abuse Contact Email: abuse(at)web.com",
      "Registrar Abuse Contact Phone: +1.8003337680",
      "Reseller:",
      "Domain Status:",
      "Registry Registrant ID:",
      "Registrant Name: Pinnatech Inc. d.b.a. Nauticom",
      "Registrant Organization: Pinnatech Inc. d.b.a. Nauticom",
      "Registrant Street: 4008 Gibsonia Road",
      "Registrant City: Gibsonia",
      "Registrant State/Province: PA",
      "Registrant Postal Code: 15044",
      "Registrant Country: US",
      "Registrant Phone: +1.7249339800",
      "Registrant Phone Ext:",
      "Registrant Fax: +1.7249339888",
      "Registrant Fax Ext:",
      "Registrant Email: domreg(at)nauticom.net",
      "Registry Admin ID:",
      "Admin Name: Pinnatech Inc. d.b.a. Nauticom",
      "Admin Organization: Pinnatech Inc. d.b.a. Nauticom",
      "Admin Street: 4008 Gibsonia Road",
      "Admin City: Gibsonia",
      "Admin State/Province: PA",
      "Admin Postal Code: 15044",
      "Admin Country: US",
      "Admin Phone: +1.7249339800",
      "Admin Phone Ext:",
      "Admin Fax: +1.7249339888",
      "Admin Fax Ext:",
      "Admin Email: domreg(at)nauticom.net",
      "Registry Tech ID:",
      "Tech Name: Consolidated Communications",
      "Tech Organization: Consolidated Communications",
      "Tech Street: 121 S. 17th Street",
      "Tech City: Mattoon",
      "Tech State/Province: IL",
      "Tech Postal Code: 61938",
      "Tech Country: US",
      "Tech Phone: +1.8004800080",
      "Tech Phone Ext:",
      "Tech Fax: +1.2172586802",
      "Tech Fax Ext:",
      "Tech Email: domreg(at)consolidated.net",
      "Name Server: ANS01.CONSOLIDATED.NET",
      "Name Server: ANS02.CONSOLIDATED.NET",
      "DNSSEC: Unsigned",
      "URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/",
      "&gt;&gt;&gt; Last update of whois database: Tue, 14 Apr 2015 07:39:01 GMT &lt;&lt;&lt;",
      "",
      "The data in Networksolutions.com's WHOIS database is provided to you by",
      "Networksolutions.com for information purposes only, that is, to assist you in",
      "obtaining information about or related to a domain name registration",
      "record. Networksolutions.com makes this information available \"as is,\" and",
      "does not guarantee its accuracy. By submitting a WHOIS query, you",
      "agree that you will use this data only for lawful purposes and that,",
      "under no circumstances will you use this data to: (1) allow, enable,",
      "or otherwise support the transmission of mass unsolicited, commercial",
      "advertising or solicitations via direct mail, electronic mail, or by",
      "telephone; or (2) enable high volume, automated, electronic processes",
      "that apply to Networksolutions.com  (or its systems). The compilation,",
      "repackaging, dissemination or other use of this data is expressly",
      "prohibited without the prior written consent of Networksolutions.com.",
      "Networksolutions.com reserves the right to modify these terms at any time.",
      "By submitting this query, you agree to abide by these terms."
    ],
    "name_server": {
      "MX": [
        [
          "MX",
          "hacker.com",
          "filter.hacker.com",
          "10",
          "2708",
          "IN"
        ]
      ],
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
  },
  "domain_history": {
    "October 2014": [
      {
        "old server": "NAUTICOM.NET",
        "new server": "CONSOLIDATED.NET",
        "zone date": "2014-11-01",
        "operation": "Transfer"
      }
    ],
    "March 2004": [
      {
        "old server": "EVERYDNS.NET",
        "new server": "NAUTICOM.NET",
        "zone date": "2004-04-01",
        "operation": "Transfer"
      }
    ],
    "January 2004": [
      {
        "old server": "HACKER.COM",
        "new server": "EVERYDNS.NET",
        "zone date": "2004-02-01",
        "operation": "Transfer"
      }
    ],
    "November 2003": [
      {
        "old server": "NAUTICOM.NET",
        "new server": "HACKER.COM",
        "zone date": "2003-12-01",
        "operation": "Transfer"
      }
    ],
    "January 2003": [
      {
        "old server": "INTERLAND.NET",
        "new server": "NAUTICOM.NET",
        "zone date": "2003-02-01",
        "operation": "Transfer"
      }
    ],
    "February 2002": [
      {
        "old server": "NAUTICOM.NET",
        "new server": "INTERLAND.NET",
        "zone date": "2002-03-01",
        "operation": "Transfer"
      }
    ],
    "December 2000": [
      {
        "old server": "NAUTICOM.NET",
        "new server": "N/A",
        "zone date": "",
        "operation": "Epoch"
      }
    ]
  }
}
```

# 🔗 Modules Currently Supported

- [x] 👁️‍🗨️ Domain Availability
    - By using [Mad Checker](https://madchecker.com/)
- [x] 📖 Whois
    - By using [Domain Big Data](https://domainbigdata.com/)
- [x] 📜 Domain History Based on DNS
    - By using [Hoster Stats](http://www.hosterstats.com)
- [ ] 🎁 Dns Services ️
    - By using [Dns-Lg](http://www.dns-lg.com)


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

<table>
<thead>
<tr>
<th>Insight </th>
<th>Badge </th>
</tr>
</thead>
<tbody>
<tr><th>Project Hit</th> <th> <a href=""><img src="http://hits.dwyl.com/iAbdullahMughal/espionage.svg?style=flat-square" /></a> </th></tr>
<tr><th>Code Quality</th> <th> <a href="https://app.codiga.io/public/project/30529/espionage/dashboard"><img src="https://api.codiga.io/project/30529/status/svg" /></a>  </tr>
<tr><th>Test Cases</th> <th> <a href="https://app.circleci.com/pipelines/github/iAbdullahMughal/espionage"><img src="https://circleci.com/gh/iAbdullahMughal/espionage/tree/main.svg?style=svg" /></a> </th></tr>
</tbody>
</table>


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version fury.io](https://badge.fury.io/py/espionage.svg)](https://pypi.python.org/pypi/espionage/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)



 
