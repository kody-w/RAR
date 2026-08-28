---
name: "rar-cat-agent-skills-rich-html-presentation"
description: "Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/rich_html_presentation", "rar_sha256": "3d19b945bbfafa005314156f60b03bb2f0361556e9f269fae151015b8e007ec8", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.2.0", "author": "Henry Jammes", "tags": ["presentations", "html", "design", "productivity", "writing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/rich_html_presentation`. The original RAPP
agent is preserved byte-for-byte in `rich_html_presentation_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Rich HTML Presentation — Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#rich-html-presentation
  Upstream author: Henry Jammes
  Upstream version: 1.2.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rich_html_presentation_agent.py` and embedded as the fenced Python below (sha256 3d19b945bbfafa00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rich_html_presentation_agent.py` first:

```bash
python3 rich_html_presentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rich_html_presentation_agent.py   # or on stdin
python3 rich_html_presentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rich HTML Presentation — Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#rich-html-presentation
  Upstream author: Henry Jammes
  Upstream version: 1.2.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/rich_html_presentation',
    "version": '2.2.0',
    "display_name": 'Rich HTML Presentation',
    "description": 'Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.',
    "author": 'Henry Jammes',
    "tags": ['presentations', 'html', 'design', 'productivity', 'writing'],
    "category": 'productivity',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'rich-html-presentation',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#rich-html-presentation',
        "upstream_version": '1.2.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dc40638371835363',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.667, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:presentations', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class RichHtmlPresentation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RichHtmlPresentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(RichHtmlPresentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/81aaZObWJb9K0z2B7uadAoJsWVHRwwIhATaAbGUK2z2fRGbAE/993lIyrSr29U9EzEfRplhs7x337nbufc95bcns6mDvHx6fVq5WdlDgpmmbvX0/OS4lV2GRR3mGXi5KF2zdqEiT8IqcJ1nqHIT75OdZ7UZZq4DreTtBqqS0HEhx7XjCrqGdQDFbp/ltfupqvvEhdqwasykeh4fW7lZOlBmtqFvjks8Q3XggoWfITML09uj27UDlW5TmRaYXpRu5YL1xneQnadFnoHb6gVgdTszLRIA+/XX356fQnD99PrtyU7MCjx6OoV2sKrT5PCDADApMTMfvC16oP94X7ill5cpeOS4HvS4+zjq+Qz99a/x1Sz96pfXzxn0+Hx+Gn9OTTZCh+rcrGpgCNssTCtMwrp/gejkavYV0KBuyqyCTKiqyzDzX+4zv0vKC+jv47uP90VefLf++PkpBxBuWD8//QLlJVivbMbrl1FK8fGXlyS/uuXHX77LqRorcu16FAZQv3x53D/EgoHfh4bebdW/A6l3R1vu56cflBs/d9yjnmDm00uUh9nHu+CizFs3MzPb/fjLn4m1AxAHIFrq/5HcX++CA9d0gE4P4L8834z8GwQ/FHqX+efLFsCt/xtNwPC35UBg3g31Z7Jv9v8H0QkI/+rd4j8V97MJ8N+hX/9Ut3814RnyPj+xbhK2IDpAWrxC375IB27x6wfn+8MPv/0ORP9bMVLelPZNwpcUpJ3nVvWXL79+qG6PP/z264emALHmmumXpkx+JvNndr2t8wcLPkZ9/ONcsL6SxVl+zaD3SIe+5cV/lL+/QGcTUMn359Ur9GO+jB8YGpV4W/Rugh9ypgJYf7DjL0+/A17IgDaNfXsNsvwvf4G2oV3mVe7VkGTnTQ0BB9dh6o7g5SCsIPA75nbpArtW4UhC93Eg/kcPj4hzD/r6n7ZZfzJ9wC2fqjhMkmpSAsr5EgDO+fIja319gWQgLi9DP8zMBDrRh8Pn7DZxXOo2tGwBiVg9IE1AP5/GCyjMoK8/F/jlNvel6L/eqDK8U9FpsR5pqGoS92VURQ3c7AHcNjPI7Vy7AWKT3AYYvDAZWRcIzZMW0Nio9k0JyAlLoGMOasKNhpvsdRT29etXy6yCz9mdN1HoXiWAys13ONCnTwCml4R+UH/OXDvIoQ/ffv8A/Rf0r2bdhI9rHABvPwwPEArSfgeBRGrSke6h0YuAJW6G//b7w6RATOaWEHBT6IXufTIIxNh13uwrrehPMwyHLBfYFdgUlI+yBmQMhfULtPagd7xg0fHVSNdBXtWgnBVu5riZ3QOpJlDn3ZKgtEEV8EPl9c9QU7m3Vb9apXmDmIKMNuuv0HZxAMUhT8A/I8zbIDA5z0Jg/nfv358DIeWHCmLeRLxAuzH0oMIszSIozccannn3CygKb9OBcBPK3OvnbKx+bvoWIXfzgEHAMvbDpZ9Gn48VFCS9U72tfRtjjiVMvpWy8nNWPWLcLEdX2IDzwaJ+Ezoj8//tEVJVkDeJc7MfQDpKenjBeXjlFoNjDb43CT9WYehzM0Omc+j/cXcxgqd5/sTxtMyxELeTT/rdqCO80fj3BgoUfAhE1j2BvjcBbxTyxqSfsyQEEVL2f7uPvLniMebOTk0JFD7RJ+hN/fIm9xamY9iV5Rjg5ufsjbKBItCNnwBwkNMg5sdQe1twfPuGNACJO95/L983twJTAVOAUISKxkpAmHiu61imHQNU5ZhqDy+BmHXHtLsGozN/1AoC0kFoAPkQABGC5AG0fjPdLgdqgizzyjz9PjwcmyKAwmlsgDZwS/cFUkG2jBFTgRQFnc04Bljhw00UlLrAxgDiu4WrwCzuYPIyfgNoPnzxo/0fr75H9w3JCB7INB2zBpa8jhzruN3dr+8oH54CUNMxH2+T/ujsh6bQj5Xlb5+zG8J3WgdpntxC7LtpIJBeaXULwJGlKsA0qfsIHxAHt/r7ci+h9xr9juUVWtAyRN8p7VZroI/pWxW7FTzljz55hYK6LqrXyeR92IsPsqexXsJ88k+F6y9jofk0FppPP2bEHwTfbfAK/bhh+MOARzS+QtOX2QsyvtqEtjuG2+PzCjXZO0t8/OH64a2bN0YeyG70B2JlDMyRGm6Nxcn97k4AJh8zerRyDwrne2V5GwLKi1+6/jj4XmmqsUBdQU28yQYG/5y9u/yRDoC5M3+kiyr/IU1vJRY48O6f9woAXmU1WNsZuy/fHfcjyahu5T69Zk2SPD9lZur++T5kJHcQi8Bm46YFZAXoYerQvd2ZjROOhhuv/7gh298uzGRMnHwslCOT128GvIF2SoBozDQ/HPn8GQJAfcCbox7XMdvGbsACelUVqK3OCLzuixHpfZ8y9kzvDdU/I7glLGAaJ38d8/YZGpvfZ+i9j32G3nYWty1a1oCt1a9jDz3qDIaC/97Hvu83Lffpt5/AeLTUfw7iQSZ3UjetsTCNKv5EJyCtdC8NqITOiOe7gt/Xze+L/X7DWd83hd+e3vji4aVHAwiGg8T8VI21cDJ9QcCC4P4eaeDd/7Q1fEwDtAaaFDAPdaaURc0xy/JMz0QQDJ3Opxju4YiFoJY18xAUn2IY7lLeDKc8051iU2SKWaSLIIRrk0DePUy/jHU+HKE4U5wiKI+gUJRyHQTHplMXsWwMsVEc9aYzEnemc8Qmvk+NQR4+9LvrMxrvvUu9xeddzW9PFj4fjxDm1Zq+fxYT6mzgMyLqAg0ecFffRmQsyCKVoLpsbuqlxtto2m+MzcpE2WOxUjgrloSLvi5iAykNn98GLEZng3BA96m7PFMLo+BMumOXbZixyUA0NnEd6K0/2DiapxpBELhSXmf95VIlorbfTlZDNMCCje/iiyKdCqpszuxaO19UKx78VWRjyjyzjPPCEYXFBa73gpkMdXc5YoZ2yWW1wyTBxJFSPV2wyWmeKY0ccp2LS4i3DbxEbpDzMlVTatKvD723uGxLcWfpmmaAsrycxLxFmCId7Q/thBy8w2Gg5tQEuZLeRGsGi4xIFc8YOl7RIV/ahW1pJ4ITInt+SqpTj4iNo5QHkkayEL9chbNsM3ji8rN4L3docGp2vnwVF2I4L+kZ6mUb5FS7OD9z855LYEXn++05sdY6TVK76qIqnGCL6k7AWemwIXhiENrI3Kiq3Xt1VM41oaSk1O5CxkGjFW8u+OOaLCmziKozf1GP9Rxp1ww9F9zeZUVFgjnHJsiU0VbX1R6LFyRzlI+ChznGwBqXbsCNc9NtvRQWdDM9NSuyWOcBhsyNpZ60TrkGheJSqWKFtL1uXlgqOKViq++qGLi3dAjhGjdyGseqjLaYk1KHodQ3BbcUBW6+jJlob/TLNT8lGCy5+BZGOvy+Ic1wE67mxlSGK2IKpzxqd8YScfa0YOysKloRhxjBsqQgwqVotO45l1CVn+/QxIXViNGIg9htyxnXr+tJ33HqMRiqiRvKh3RyMKQCj88IMdvLKjHIcsxO5AmhJSEIplh1siU+S5ilCp+EWscQLyg3ZC4lh81qi0+OLD2DXWJbUG4t7iYS5hUTbNEujwZ8oFiiWC5QTfHcY9ttV7lysFkxGQp1ucxgo+cvLHvCc5hfm649NHpAHTepK8p91ov0ujhIHmNz1lTLj0ojKdVMNv2p7wXr2W4TF4Ra7CtsZZRTwVyf8T6M9JzNEwUbSqZHVpHRoT0ZU6mK56vdHk/Wm1DM9saETrrsEhKM3se5nanhdUYK2tosjGpZniUrMEPVC3fhYnfsmgjZBte1so5CUjAmh1NALRZ2MzlvieCsChjpwvrBriQBLTdlkx4CCq0lhDpxRoPirrlsYrIEiafPtZlumHunxuR2sjIsV52tFX/hVLtrdpkmy2ZT67WQXKdqpx+3kgcHlYOl1DY+Z4ngrQ20gAet56PzpWolcs4spoM9Y4amlJtW8fKFCZfxpZaE+TGQtGhACefCkBdWXqoi6FNSw9wNx2apbKnwzGP4KsPEWOPxJLFWm6Rj5UnOeEtdw5CAxPoWFWt+PT2siWARLKbBib8OBCU2/QIO09WB3uhbqmETDEX382lBXvMsE66+2uw2laDjjjxoiTKXxWQuKKW69ZbMcIiZ+RKW91sFTPFiQsETrIGt/IxdVKHa0Vl3lacVR5QrOyqEsxB6a/QMClxKFamI1aoKrxHNP6/qyRU10MmVnwSo3XaBQLqGKGqiWSeidUKc9Tk6mzhD+tZQNRfFU7bHS+hNyPk2i+QOm0wOC0AtFDbZS52BBlrXb6eSIGlcNb1YpI17fXLiBL6Z58qsjnpBmSVOMWkCpTFoXifwrLZPjTnfnjXY4Y6XzmyWIUdMtIAWJMzdmrap1LbhGq2iMywaG9NzQK7PgmF4qz2JbFNsvyY3qCRu29msZEQnnG5JfRVcxZrg3bPK23PKOmxxHG2UYiVxtZ90aRYciGhT8CHRqpc1ejyZfXI07NRCL85F28sYPBWsUxEuYYqsInk2rzZxIC5xBHPlvsIcjj75zZ6houWOpOBSYS7LExcjxSTGD3vWXjinfZkHJy9XpGQRR+XpjCW9tosQMTVidLdoZqvTiVuEu1ScIkXC91ghlbozxKtyYIJ2pyYlvjbEtbhjPXw36fQSOTGAEBb+WtvzSrPxtHZZ5DtAz0OBz8R1eFYkisCwRjP2V3jPSSIdHllOZ93FIprRx5RFlD1P0hNUZWYDRbHCgQ09DSQAkxgHwd1Vrq5sGWsdzY/8lJyaQj7f2NY1M/xdvmgjfl8p+XwFI9vY1TvASOdTtSoJuI2xo74XdosQwczlkeslx5zFCpd0FKHLYcC54pkv+N4yYtjgsm4VsBdJEU33qGbqYbWwVccVbV/0llh0kVbr05lVSl4LTKXIxc7YVjPQRFC8d+Ls4dxteC/dNKzI6wWVS3RQbJCYc477rNsUMV+lW9Goom6BxkO53xWFwcNRv86iAUvZupbacH3hos0WLjR20R6lRuYlvUPI8tLp6+OSWa2VahlgWn9hi1xxsZReJEnNEAtlk568WGuIwWCjLVsPjoLFU8FXbVFDB4bqDLEzTXYTZgeNXm1rZnOYpCZiMFvzJAuiwcn7Yk71M359iH2pMS7xwHSJWDeSECzai1KXVdHUVFVi16kFjMpt9WoCKuIQzEmzrHVLatnGRNcr90KjQelo+HFZba+537ELTktWjMohQWYfTz3OcxudWATntRJ5+LL1Ful5oebGSik8310jtRGssyXvH1Mmpk8V3JtczBgG22WMIjtVY9iXXQLnfJEySxRbD+jJZ3lnnQb75dkVJA7Tln5pLCpxM92fuWCw9/vgmE0W+qYK/Ckl+6rC0LQYiIut5jBwrcd6U3OyuTpEfgk3Pq7L2PESuKvQ51YrKYPztdgnoIgc54PaqPFkPkRcVbRiMdQTpQikGjstju2GQ9ZDim0tzpnkgaX3PJVeppfA5CY0g03PhjQLT2So4la0rxuUbiW14axmozBHKYUZTZHbqy9lxsUOyI1Qbsm8Z33/tMESRqKmoqIxM3lFDOGULrqN3UYNE2VJjFBSNDGMDfDjHsMlnFkhs4bsvE1OUihPXmOpVPxyt0tNM1zoQr7bm0md+tysKEvfO20PawkRbSKMB6trJII19YK4Jvien+BB06w5sWDS/KByHmfv6lLf57NqRh5TvRN2flubs3TWzh11UMndFU1IN+I3DuwtwpbwbaLpd4a+32WWFhxCrFgkmkCVDFYhcydAzHO2Q/QhJ4s5JykIJe6EEl24bFtkh45Y2hdcsC773lKvoktF21o+77ax5vCAwPqBRnErH5CzQxYp1V9KyppV0voqTjuvc213XhPh1iYQk5xz3irYemznM6yDOjO0VAJ1viT3eY0jLhxW3WRfkYCyDWoCB/zkuqCKoxbRnjdlQbXuUbld+lS0MefXoC4OQ0Aj7VTnTESWkZrxuWOBnA8Mz1kpEchzNrFln24Tuy/NwL3yidwN1wV8OlYGdWKvGa3GMrzBTSBWndhDpZ7C+XQBk5FtRsx8tqjDfU/YWki2rmLPy+oYp8sq0GUr0IidjbIbvWVChdifHdaE5XausfbgBK2eldRkvedswiLKfEE6zNzG4aRS5aNc4EIIqzrlIEyZsIa9ifU0bwHfIHKkw/uN4mU43kktTk0y5nLa7MPG8MuNz2iGT2bttc6OTo7Deq9fNtqsjU7hZk23VhjtB9LSULLd6Jc13jj5KluismIbJ8pzrsUK5vWY3pDofuoGXNvFVqQH3MY+hrsZl8w4t7M2c4GoS7jqWLrjTVD527wFxLA8DFNbRhJ6aSO2gGXLCo/3zFYqxBSNdOUUmiQ3KyvyROHBVRsKXgXF0uMm8rUUMEodpnNyH5yWnNbQU62sVR1BGaTDLU6ZH/1BvdK8hZ5Iay4s6S5Vr1MmgK0KbEFcb31mO4rxAlW5socSDu3TLuxQW9PDpNFnk6wRdmEUCfamrJnZ+Zqtci7k+j0JxxGLTtZ1RG6n+K6N69JpEdBHnFd8er5uFyyadrug0k04orUrRTFBhc61jKBzv2UYc9dRZcCT4tKfobJTGPUuk/kZQaxLNTMlgoeXVrx1TJxumM6haJFST1eBJHI6UCc58AelqvH05J+Oh9jysOFi7eIurWBa4xpNPy/h+a4nt9UOEeq5vwpWBsFf22VEgNZ6sOs0RR2YWqHEpfaEecJ4B38Tm/v6SCasG60uWtAa+eDWkz2WajN2locVsipW9slZyqs8wj1/MukIB0YM1puitAV2qahHH5mSCNM1U16TrTlgl1JoYdKKzDIK6xW90xztXLFo4UXslT3SMl1IaGePPVq+VkX6iEuDZhvNgpxIJppe0bBXN/PJ3MjRtC2KpRYMkU/jvJP5NLyBl8ySN7VulxIpkzO4dfGShu2J0nPKvRZltSrPunJ3pKuduSF27Q7Dg2CGt0yVgIDlUFxAh6A/LjOfbVbBsd75nU9Gl8O6xFTjuJ3TQz4MwpXf1WBjW4iiQyh2k2+aCbMX2ms1sfpKQkn0VAtLwUvcIZ0nMLzR1WmPy4WxKlwM86q6P1yJul1zyGzZDYv5cAmxXbcurfYQyrTJ4gnSTZEIR0NktcMtnY2uS3OescbMrxeMUDYnPLwiRH2B140y3SUXzED5TadmOWVPKzzaz3OL2GLOAfh9MhyMRqL0iKbpvz89P42ne48zun/zPdt4NvJ/dkRzP015O4q/HY65pvN6W+v13wH57fmptEMA437mVCWN/ziq+ccTp08/P9IdJ/X376nGrwe6+u20sjb98Q8pnn4cPP5ByCjhfk4X+rczvNuRWx22YT3a5VqG4/dpI7DH+S/AMxsPgJ9+/2/hxacWZiIAAA== -->
