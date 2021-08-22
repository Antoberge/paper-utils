FIGSIZE_md = (9, 6)
FIGSIZE_lg = (6, 12)

COUNTRY_TIMESPAN = {
    "DD": (1950, 1992),
    "DE": (1877, 2010),
    "FR": (1905, 2010),
    "GB": (1893, 2010),
    "US": (1836, 2010),
}

COUNTRY_PATEE_TIMESPAN = {
    "DD": {"ASG": (1950, 1992), "INV": (1950, 1992)},
    "DE": {"ASG": (1877, 2010), "INV": (1950, 2010)},
    "FR": {"ASG": (1905, 2010), "INV": (1980, 2010)},
    "GB": {"ASG": (1950, 2010), "INV": (1893, 2010)},
    "US": {"ASG": (1930, 2010), "INV": (1836, 2010)},
}

TECHNOLOGY_TIMESPAN = {
    "additivemanufacturing": (1986, 2019),
    "blockchain": (1998, 2019),
    "computervision": (1969, 2019),
    "genomeediting": (1983, 2019),
    "hydrogenstorage": (1994, 2019),
    "naturallanguageprocessing": (1967, 2019),
    "selfdrivingvehicle": (1970, 2019),
}

STYLE = (["-"] * 5 + ["--"] * 5 + [".-"] * 5 + [":"] * 5) * 10
COLOR = [
    "#00004d",
    "#2f326d",
    "#53648d",
    "#7999ad",
    "#a8cfcb",
    "#ffb9ab",
    "#e7797a",
    "#ba424e",
    "#801428",
    "#3f0000",
] * 10
# https://gka.github.io/palettes

OFFICES = [
    "US",
    "CN",
    "EP",
    "JP",
    "GB",
    "FR",
    "DE",
    "IT",
    "CA",
    "KR",
    "BR",
    "RU",
    "IN",
    "ZA",
]

TECHNOLOGIES = [
    "additivemanufacturing",
    "blockchain",
    "computervision",
    "genomeediting",
    "hydrogenstorage",
    "naturallanguageprocessing",
    "selfdrivingvehicle",
]

CLAUSE_FIRST_PUB = """
    NOT(country_code="US" AND kind_code not in ("A", "A1", "B1"))
    AND NOT(country_code="CN" AND kind_code not in ("A"))
    AND NOT(country_code="EP" AND kind_code not in ("A1", "A2"))
    AND NOT(country_code="JP" AND kind_code not in ("A"))
    AND NOT(country_code="GB" and kind_code not in ("A"))
    AND NOT(country_code="FR" and kind_code not in ("A", "A1"))
    AND NOT(country_code="DE" and kind_code not in ("A", "A1", "B3", "C1"))
    AND NOT(country_code="IT" AND kind_code not in ("A1", "B") )
    AND NOT(country_code="CA" AND kind_code not in ("A", "A1"))
    AND NOT(country_code="KR" AND kind_code not in ("A", "B2"))
    AND NOT(country_code="BR" AND kind_code not in ("A", "A2", "A3"))
    AND NOT(country_code="RU" AND kind_code not in ("A"))
    # all IN
    AND NOT(country_code="ZA" AND kind_code not in ("B"))"""
