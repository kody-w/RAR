"""Primary navigation and its no-JavaScript counterpart stay in sync."""

import re
from html.parser import HTMLParser
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index", "distros", "skills", "install", "front", "store",
         "discover", "metrics", "submit")
DESTINATIONS = [
    ("Browse", "index.html"),
    ("Distros", "distros.html"),
    ("Skills", "skills.html"),
    ("Install", "install.html"),
    ("Front page", "front.html"),
    ("Advanced", "store.html"),
    ("For AIs", "llms.txt"),
]


class NavigationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.placeholders = 0
        self.stylesheets = 0
        self.scripts = 0
        self.in_noscript = False
        self.links = []
        self.link = None
        self.brands = 0
        self.dropdowns = 0
        self.in_primary = False
        self.in_legacy_header = False
        self.primary_targets = set()
        self.legacy_targets = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "noscript":
            self.in_noscript = True
        if tag == "a" and attrs.get("class") == "rar-brand":
            assert attrs.get("href") == "index.html"
            self.brands += 1
        if tag == "details" and attrs.get("class") == "rar-more":
            self.dropdowns += 1
        if tag == "nav" and attrs.get("id") == "rar-nav":
            self.in_primary = True
            assert attrs.get("aria-label") == "Primary"
            self.placeholders += 1
        if tag == "header" and attrs.get("class") == "rar-page-header":
            self.in_legacy_header = True
        if tag == "a" and "href" in attrs:
            if self.in_primary:
                self.primary_targets.add(attrs["href"])
            if self.in_legacy_header:
                self.legacy_targets.add(attrs["href"])
        if tag == "link" and attrs.get("href") == "nav.css":
            assert attrs.get("rel") == "stylesheet"
            self.stylesheets += 1
        if tag == "script" and attrs.get("src") == "nav.js":
            assert "defer" in attrs
            self.scripts += 1
        if tag == "a" and self.in_noscript:
            self.link = ["", attrs["href"]]

    def handle_data(self, data):
        if self.link is not None:
            self.link[0] += data

    def handle_endtag(self, tag):
        if tag == "nav":
            self.in_primary = False
        if tag == "header":
            self.in_legacy_header = False
        if tag == "a" and self.link is not None:
            self.links.append(tuple(self.link))
            self.link = None
        if tag == "noscript":
            self.in_noscript = False


@pytest.mark.parametrize("page", PAGES)
def test_shared_navigation_and_plain_fallback(page):
    parser = NavigationParser()
    parser.feed((ROOT / f"{page}.html").read_text(encoding="utf-8"))
    assert parser.placeholders == parser.stylesheets == parser.scripts == 1
    assert parser.brands == parser.dropdowns == 1
    assert parser.links == DESTINATIONS
    assert parser.legacy_targets <= parser.primary_targets


def test_shared_script_destinations_match_fallback():
    source = (ROOT / "nav.js").read_text(encoding="utf-8")
    assert re.findall(r"\['([^']+)', '([^']+)'\]", source) == DESTINATIONS
    assert all((ROOT / target).is_file() for _, target in DESTINATIONS)
