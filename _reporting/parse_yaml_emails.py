# Generates the mentoring email lists and the COA table locally.
#
# These used to be rendered by hidden.md, a page with no front-matter marker
# keeping it out of the build, so it was published at https://jthaler.net/hidden
# with ~79 addresses on it and no robots.txt or noindex. Nothing linked to it,
# but unlinked is not private. The page has been removed; this script produces
# the same output without any of it reaching the built site.
#
# Run from inside _reporting/, matching parse_yaml_reporting.py:
#
#   cd _reporting && python3 parse_yaml_emails.py
#
# Writes email_lists.txt, which is gitignored -- it contains the addresses, so
# it must never be committed. Note that _data/mentoring.yml itself is still
# tracked in the public repo, addresses included; see CLAUDE_REVIEW.md.

import datetime
import yaml

mentoring = yaml.safe_load(open("../_data/mentoring.yml", "r"))
output = open("email_lists.txt", "w")

current_year = datetime.date.today().year


def person_blocks():
    """Every top-level key holding a list of people.

    hidden.md looped over all of site.data.mentoring and relied on Liquid
    quietly skipping entries with no email. Being explicit here instead.
    """
    for key, value in mentoring.items():
        if isinstance(value, list) and any(
            isinstance(entry, dict) and "name" in entry for entry in value
        ):
            yield key, value


def everyone():
    for _key, people in person_blocks():
        for person in people:
            if isinstance(person, dict):
                yield person


def alumni_blocks():
    """The blocks listed under alumni_categories, in that order."""
    for category in mentoring.get("alumni_categories", []):
        block = category.get("block")
        if block:
            yield block, mentoring.get(block, [])


def section(title, body):
    output.write("## %s\n\n%s\n\n" % (title, body))


def joined(addresses):
    return ", ".join(addresses) + ("," if addresses else "")


output.write("Generated %s\n\n" % datetime.date.today().strftime("%B %d, %Y"))

# Everyone currently in the group.
section(
    "Current Email List",
    joined([p["email"] for p in everyone() if p.get("email") and p.get("current")]),
)

# Not yet contacted this year: everyone with an address whose `updated` year is
# not the current one, excluding the deceased.
section(
    "Email List for Remaining %d" % current_year,
    joined(
        [
            p["email"]
            for p in everyone()
            if p.get("email") and p.get("updated") != current_year and not p.get("deceased")
        ]
    ),
)

# Already contacted this year.
section(
    "Email List Done for %d" % current_year,
    joined([p["email"] for p in everyone() if p.get("email") and p.get("updated") == current_year]),
)

# Alumni with no address recorded, so it is obvious who is missing.
missing = [p["name"] for _b, people in alumni_blocks() for p in people if not p.get("email")]
section("Missing Email List", "\n".join(missing))

# Every alumni address.
section(
    "Full Email List",
    joined([p["email"] for _b, people in alumni_blocks() for p in people if p.get("email")]),
)

# Conflict-of-interest table for proposals. Names are written surname-first,
# split across cells, matching the format hidden.md produced.
coa = ["| Arkani-Hamed | Nima | | IAS | advisor | %d |" % current_year]
for block in ("phd_students", "postdocs"):
    for person in mentoring.get(block, []):
        name = "|".join(reversed(person["name"].split(" ")))
        after = person.get("after")
        org = after[-1].get("org") if after else "MIT"
        coa.append("| %s | | %s | advisee | %d |" % (name, org, current_year))
section("COA", "\n".join(coa))

output.close()
print("Wrote email_lists.txt for %d" % current_year)
