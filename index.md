<p align="center">
<img src="https://lh3.googleusercontent.com/NfYrnpBuMyqZGwGqBZ9HR7j0NmuZWaEIOdWq-ZBxoylsWHhVaTXKD_8VJPhZk_-QFyUoJZFRxAYeYM5iphN2A0UeyqD_Hd8w-rpRhzlYQWv01o9GK9Q9mWnTPulNkedLjlZMdkz9" />
</p>

---

<p align="center"> 
<img src="https://lh5.googleusercontent.com/dqRwPKHuPqS5RzTz5ceBEbL7MkPbtLsBbAgCIE3vNCmhsKZWYtGFzFSVnixsKvNooEFuAWIuzTKQOeyzXAxnlTmJJR9L0fQxicsSHzg8TDJCrb9zOqzSRGWQ-t_NIno0MsOOsMBt" />
</p>

---
<p align="center"><a href="https://replit.com/@iAbdullahMughal/espionage#.replit"><img src="https://img.shields.io/badge/Try_Online_At_Repl.it-Click Here-blue?style=for-the-badge&logo=repl.it" alt="Espionage on Repl.it" /></a></p>

<p align="center">
<a href="https://pypi.python.org/pypi/espionage/"> <img src="https://badge.fury.io/py/espionage.svg"/></a> <a href="https://pypi.python.org/pypi/ansicolortags/"><img src="https://img.shields.io/pypi/l/ansicolortags.svg"/></a> <a href="https://app.codiga.io/public/project/30529/espionage/dashboard"><img  src="https://api.codiga.io/project/30529/status/svg"/> </a> <a href="https://www.codacy.com/gh/iAbdullahMughal/espionage/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=iAbdullahMughal/espionage&amp;utm_campaign=Badge_Grade"> <img src="https://app.codacy.com/project/badge/Grade/4a00d6efafea4a50a9159c43dc349bfe"/></a> <a href="https://app.circleci.com/pipelines/github/iAbdullahMughal/espionage"><img src="https://circleci.com/gh/iAbdullahMughal/espionage/tree/main.svg?style=svg"/></a> 
</p>

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

# 🔗 Modules Currently Supported

- [x] 👁️‍🗨️ Domain Availability
- [x] 📖 Whois
- [x] 📜 Domain History Based on DNS
- [ ] 🎁 Dns Services ️ (In progress)

[//]: # (    - By using [Mad Checker]&#40;https://madchecker.com/&#41;)
[//]: # (    - By using [Domain Big Data]&#40;https://domainbigdata.com/&#41;)
[//]: # (    - By using [Hoster Stats]&#40;http://www.hosterstats.com&#41;)
[//]: # (    - By using [Dns-Lg]&#40;http://www.dns-lg.com&#41;)

### 👁️‍🗨️ Domain Availability Check

- *This module check if a domain is available or taken already.*

### 📖 Whois Check

- *Domain Basic Information*
- *Domain Registrant Information*
- *Old whois record information*
- *Name server records*
- *History Records*

### 📜 DNS Based Domain History

- *Tool is searching historical records based on DNS.*

### ✍️Console Example

---
#### Example Json Report
```shell
python main.py -d "www.hacker.com" --json --extended
# --json this flag allows results on console in json format
# --extended  this flag allows to fetch extended result for domain
```

<details>
  <summary><b style="color:skyblue">Click to view Json output</b></summary>

#### *Output Json*

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
      //      Report truncated  
      "hacker.trade",
      "hacker.web.tr"
    ],
    "whois_data": [
      "Domain Name: HACKER.COM",
      "Registry Domain ID: 648983_DOMAIN_COM-VRSN",
      "Registrar WHOIS Server: whois.networksolutions.com"
      //      Report truncated  
      //      ....
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
    //      Report truncated  
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
</details>

---
#### Example Table Data Report
```shell
python main.py -d "www.hacker.com" --extended
# --extended  this flag allows to fetch extended result for domain
```

<details>
  <summary><b style="color:skyblue">Click to view Tabler output</b></summary>

#### *Output Json*

```shell

███████╗███████╗██████╗ ██╗ ██████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗
██╔════╝██╔════╝██╔══██╗██║██╔═══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝
█████╗  ███████╗██████╔╝██║██║   ██║██╔██╗ ██║███████║██║  ███╗█████╗
██╔══╝  ╚════██║██╔═══╝ ██║██║   ██║██║╚██╗██║██╔══██║██║   ██║██╔══╝
███████╗███████║██║     ██║╚██████╔╝██║ ╚████║██║  ██║╚██████╔╝███████╗
╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

Espionage v 0.0.4 - Domain reconnaissance tool


╭─────── Domain Availability Check ────────╮
│ Domain www.hacker.com is not available . │
╰──────────────────────────────────────────╯
╭────────────────────────────────────── Domain Whois Information ───────────────────────────────────────╮
│ ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │                                      Basic Info Information                                       │ │
│ │ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │ │
│ │ ┃ Domain                               ┃ hacker.com                                             ┃ │ │
│ │ │ Words in                             │ hacker                                                 │ │ │
│ │ │ Date creation                        │ 2004-03-31                                             │ │ │
│ │ │ Web age                              │ 17 years and 8 months                                  │ │ │
│ │ └──────────────────────────────────────┴────────────────────────────────────────────────────────┘ │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │                                    Registrant Info Information                                    │ │
│ │ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │ │
│ │ ┃ Name                        ┃ Pinnatech Inc. D.b.a. Nauticom                                  ┃ │ │
│ │ │ Organization                │ Pinnatech Inc. D.b.a. Nauticom                                  │ │ │
│ │ │ Email                       │ domreg@nauticom.net                                             │ │ │
│ │ │ Address                     │ 4008 Gibsonia Road                                              │ │ │
│ │ │ City                        │ Gibsonia                                                        │ │ │
│ │ │ State                       │ PA                                                              │ │ │
│ │ │ Country                     │ United States                                                   │ │ │
│ │ │ Phone                       │ +1.7249339800                                                   │ │ │
│ │ │ Fax                         │ +1.7249339888                                                   │ │ │
│ │ │ Private                     │ no                                                              │ │ │
│ │ └─────────────────────────────┴─────────────────────────────────────────────────────────────────┘ │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │                                       Raw Whois Information                                       │ │
│ │ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │ │
│ │ ┃ [                                                                                             ┃ │ │
│ │ ┃     'Domain Name: HACKER.COM',                                                                ┃ │ │
│ │ ┃     'Registry Domain ID: 648983_DOMAIN_COM-VRSN',                                             ┃ │ │
│ │ ┃     'Registrar WHOIS Server: whois.networksolutions.com',                                     ┃ │ │
│ │ ┃     'Registrar URL: http://networksolutions.com',                                             ┃ │ │
│ │ ┃     'Updated Date: 2015-01-29T00:01:45Z',                                                     ┃ │ │
│ │ ┃     'Creation Date: 2004-03-31T06:45:45Z',                                                    ┃ │ │
│ │ ┃     'Registrar Registration Expiration Date: 2015-08-21T04:00:00Z',                           ┃ │ │
│ │ ┃     'Registrar: NETWORK SOLUTIONS, LLC.',                                                     ┃ │ │
│ │ ┃     'Registrar IANA ID: 2',                                                                   ┃ │ │
│ │ ┃     'Registrar Abuse Contact Email: abuse(at)web.com',                                        ┃ │ │
│ │ ┃     'Registrar Abuse Contact Phone: +1.8003337680',                                           ┃ │ │
│ │ ┃     'Reseller:',                                                                              ┃ │ │
│ │ ┃     'Domain Status:',                                                                         ┃ │ │
│ │ ┃     'Registry Registrant ID:',                                                                ┃ │ │
│ │ ┃     'Registrant Name: Pinnatech Inc. d.b.a. Nauticom',                                        ┃ │ │
│ │ ┃     'Registrant Organization: Pinnatech Inc. d.b.a. Nauticom',                                ┃ │ │
│ │ ┃     'Registrant Street: 4008 Gibsonia Road',                                                  ┃ │ │
│ │ ┃     'Registrant City: Gibsonia',                                                              ┃ │ │
│ │ ┃     'Registrant State/Province: PA',                                                          ┃ │ │
│ │ ┃     'Registrant Postal Code: 15044',                                                          ┃ │ │
│ │ ┃     'Registrant Country: US',                                                                 ┃ │ │
│ │ ┃     'Registrant Phone: +1.7249339800',                                                        ┃ │ │
│ │ ┃     'Registrant Phone Ext:',                                                                  ┃ │ │
│ │ ┃     'Registrant Fax: +1.7249339888',                                                          ┃ │ │
│ │ ┃     'Registrant Fax Ext:',                                                                    ┃ │ │
│ │ ┃     'Registrant Email: domreg(at)nauticom.net',                                               ┃ │ │
│ │ ┃     'Registry Admin ID:',                                                                     ┃ │ │
│ │ ┃     'Admin Name: Pinnatech Inc. d.b.a. Nauticom',                                             ┃ │ │
│ │ ┃     'Admin Organization: Pinnatech Inc. d.b.a. Nauticom',                                     ┃ │ │
│ │ ┃     'Admin Street: 4008 Gibsonia Road',                                                       ┃ │ │
│ │ ┃     'Admin City: Gibsonia',                                                                   ┃ │ │
│ │ ┃     'Admin State/Province: PA',                                                               ┃ │ │
│ │ ┃     'Admin Postal Code: 15044',                                                               ┃ │ │
│ │ ┃     'Admin Country: US',                                                                      ┃ │ │
│ │ ┃     'Admin Phone: +1.7249339800',                                                             ┃ │ │
│ │ ┃     'Admin Phone Ext:',                                                                       ┃ │ │
│ │ ┃     'Admin Fax: +1.7249339888',                                                               ┃ │ │
│ │ ┃     'Admin Fax Ext:',                                                                         ┃ │ │
│ │ ┃     'Admin Email: domreg(at)nauticom.net',                                                    ┃ │ │
│ │ ┃     'Registry Tech ID:',                                                                      ┃ │ │
│ │ ┃     'Tech Name: Consolidated Communications',                                                 ┃ │ │
│ │ ┃     'Tech Organization: Consolidated Communications',                                         ┃ │ │
│ │ ┃     'Tech Street: 121 S. 17th Street',                                                        ┃ │ │
│ │ ┃     'Tech City: Mattoon',                                                                     ┃ │ │
│ │ ┃     'Tech State/Province: IL',                                                                ┃ │ │
│ │ ┃     'Tech Postal Code: 61938',                                                                ┃ │ │
│ │ ┃     'Tech Country: US',                                                                       ┃ │ │
│ │ ┃     'Tech Phone: +1.8004800080',                                                              ┃ │ │
│ │ ┃     'Tech Phone Ext:',                                                                        ┃ │ │
│ │ ┃     'Tech Fax: +1.2172586802',                                                                ┃ │ │
│ │ ┃     'Tech Fax Ext:',                                                                          ┃ │ │
│ │ ┃     'Tech Email: domreg(at)consolidated.net',                                                 ┃ │ │
│ │ ┃     'Name Server: ANS01.CONSOLIDATED.NET',                                                    ┃ │ │
│ │ ┃     'Name Server: ANS02.CONSOLIDATED.NET',                                                    ┃ │ │
│ │ ┃     'DNSSEC: Unsigned',                                                                       ┃ │ │
│ │ ┃     'URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/',       ┃ │ │
│ │ ┃     '&gt;&gt;&gt; Last update of whois database: Tue, 14 Apr 2015 07:39:01 GMT &lt;&lt;&lt;', ┃ │ │
│ │ ┃     '',                                                                                       ┃ │ │
│ │ ┃     "The data in Networksolutions.com's WHOIS database is provided to you by",                ┃ │ │
│ │ ┃     'Networksolutions.com for information purposes only, that is, to assist you in',          ┃ │ │
│ │ ┃     'obtaining information about or related to a domain name registration',                   ┃ │ │
│ │ ┃     'record. Networksolutions.com makes this information available "as is," and',             ┃ │ │
│ │ ┃     'does not guarantee its accuracy. By submitting a WHOIS query, you',                      ┃ │ │
│ │ ┃     'agree that you will use this data only for lawful purposes and that,',                   ┃ │ │
│ │ ┃     'under no circumstances will you use this data to: (1) allow, enable,',                   ┃ │ │
│ │ ┃     'or otherwise support the transmission of mass unsolicited, commercial',                  ┃ │ │
│ │ ┃     'advertising or solicitations via direct mail, electronic mail, or by',                   ┃ │ │
│ │ ┃     'telephone; or (2) enable high volume, automated, electronic processes',                  ┃ │ │
│ │ ┃     'that apply to Networksolutions.com  (or its systems). The compilation,',                 ┃ │ │
│ │ ┃     'repackaging, dissemination or other use of this data is expressly',                      ┃ │ │
│ │ ┃     'prohibited without the prior written consent of Networksolutions.com.',                  ┃ │ │
│ │ ┃     'Networksolutions.com reserves the right to modify these terms at any time.',             ┃ │ │
│ │ ┃     'By submitting this query, you agree to abide by these terms.'                            ┃ │ │
│ │ ┃ ]                                                                                             ┃ │ │
│ │ └───────────────────────────────────────────────────────────────────────────────────────────────┘ │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │                                            Other TLDs                                             │ │
│ │ ┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓ │ │
│ │ ┃ hacker.ae         ┃ hacker.africa   ┃ hacker.ag           ┃ hacker.agency  ┃ hacker.amsterdam ┃ │ │
│ │ │ hacker.ar         │ hacker.at       │ hacker.be           │ hacker.bet     │ hacker.biz       │ │ │
│ │ │ hacker.black      │ hacker.blue     │ hacker.boutique     │ hacker.ca      │ hacker.capital   │ │ │
│ │ │ hacker.casa       │ hacker.cat      │ hacker.center       │ hacker.ceo     │ hacker.ch        │ │ │
│ │ │ hacker.church     │ hacker.club     │ hacker.cn           │ hacker.co      │ hacker.co.il     │ │ │
│ │ │ hacker.co.kr      │ hacker.coach    │ hacker.codes        │ hacker.coffee  │ hacker.college   │ │ │
│ │ │ hacker.com.au     │ hacker.com.cn   │ hacker.com.co       │ hacker.com.eg  │ hacker.com.pl    │ │ │
│ │ │ hacker.community  │ hacker.company  │ hacker.contractors  │ hacker.cx      │ hacker.cz        │ │ │
│ │ │ hacker.de         │ hacker.design   │ hacker.digital      │ hacker.direct  │ hacker.dj        │ │ │
│ │ │ hacker.dk         │ hacker.domains  │ hacker.dp.ua        │ hacker.earth   │ hacker.edu.vn    │ │ │
│ │ └───────────────────┴─────────────────┴─────────────────────┴────────────────┴──────────────────┘ │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │                                             MX Record                                             │ │
│ │ ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┓ │ │
│ │ ┃ Type     ┃ Hostname          ┃ Preference                  ┃ TTL    ┃ Class     ┃ Address     ┃ │ │
│ │ ┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━┩ │ │
│ │ │ MX       │ hacker.com        │ filter.hacker.com           │ 10     │ 2787      │ IN          │ │ │
│ │ └──────────┴───────────────────┴─────────────────────────────┴────────┴───────────┴─────────────┘ │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │                                          History Record                                           │ │
│ │ ┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │ │
│ │ ┃ Date                    ┃ Status                         ┃ Name Server                        ┃ │ │
│ │ ┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩ │ │
│ │ │ 2014-10-09              │ Transferred to                 │ consolidated.net                   │ │ │
│ │ └─────────────────────────┴────────────────────────────────┴────────────────────────────────────┘ │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯ │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯


DNS Record History
├── December 2000
│   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
│       ┃ First time DNS NAUTICOM.NET record was added.  ┃
│       └────────────────────────────────────────────────┘
├── February 2002
│   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
│       ┃ DNS transferred from NAUTICOM.NET to INTERLAND.NET on date 2002-03-01 ┃
│       └───────────────────────────────────────────────────────────────────────┘
├── January 2003
│   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
│       ┃ DNS transferred from INTERLAND.NET to NAUTICOM.NET on date 2003-02-01 ┃
│       └───────────────────────────────────────────────────────────────────────┘
├── November 2003
│   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
│       ┃ DNS transferred from NAUTICOM.NET to HACKER.COM on date 2003-12-01 ┃
│       └────────────────────────────────────────────────────────────────────┘
├── January 2004
│   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
│       ┃ DNS transferred from HACKER.COM to EVERYDNS.NET on date 2004-02-01 ┃
│       └────────────────────────────────────────────────────────────────────┘
├── March 2004
│   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
│       ┃ DNS transferred from EVERYDNS.NET to NAUTICOM.NET on date 2004-04-01 ┃
│       └──────────────────────────────────────────────────────────────────────┘
└── October 2014
    └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ DNS transferred from NAUTICOM.NET to CONSOLIDATED.NET on date 2014-11-01 ┃
        └──────────────────────────────────────────────────────────────────────────┘


```

</details>



<pre> ⚠️This is an educational project. Don't abuse services.</pre>

<p align="center"><a href="https://www.python.org/" title="Made with Python"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" /></a> <img src="http://hits.dwyl.com/iAbdullahMughal/espionage.svg?style=flat-square"/></p>



 
