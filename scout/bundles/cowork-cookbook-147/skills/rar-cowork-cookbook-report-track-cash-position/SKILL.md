---
name: "rar-cowork-cookbook-report-track-cash-position"
description: "Builds a structured summary report of track cash position activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_cash_position", "rar_sha256": "6f021e5b21a47cca8e5b0f9c957142e101c22aea511f6990667b7a774438e2bb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_cash_position`. The original RAPP
agent is preserved byte-for-byte in `report_track_cash_position_agent.py` and in the RCI capsule.

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

Track cash position Summary Report — Builds a structured summary report of track cash position activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-cash-position
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_cash_position_agent.py` and embedded as the fenced Python below (sha256 6f021e5b21a47cca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_cash_position_agent.py` first:

```bash
python3 report_track_cash_position_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_cash_position_agent.py   # or on stdin
python3 report_track_cash_position_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track cash position Summary Report — Builds a structured summary report of track cash position activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-cash-position
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_cash_position',
    "version": '2.0.1',
    "display_name": 'Track cash position Summary Report',
    "description": 'Builds a structured summary report of track cash position activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-track-cash-position',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-cash-position',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b1fcdda37f6b7311',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/track-cash-position'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-track-cash-position', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportTrackCashPosition(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackCashPosition'
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
    print(ReportTrackCashPosition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+bOiyLbuv8Lb94eqPlRtZZY6cSKuoijIIAKidnVUMySDIDMy9O3//SXq3lV9b/d550S8uNYgQ+bKb03fWgn+9mI3dZiVL19edGCnyNpOkigEJWKnHsJlbVbG8CuLHfgPcbO0LiOnqbOyevn04oHKLaO8jrIUTl80UeJViI1Uddm4dVMCD6ma69Uue6QEeVbWSOYjdWm7UJBdhUieVdE4F7HdOrpFdY+0UR0idVbbSfUJjgSpB79HIE4J7NjL2rR6heuCzr7mCahevvz8y6eXCB6/fPntxU3sCl562d/XMsZ1OLjM7rkKnJfYaQAH5D1UeDzPQeln5RVe8oCPPM8+ViDxPyF/+1vc2mVQ/fTla4o8P19fxj/7JkXqEECcdlVDHV07t50ogfhfkXnS2n0F1YXqp09bRGnw+pj5XVKWI/8Y7318LPIagPrj15cMQrBHrF9ffkKyEq5XNuPx6ygl//jTa5K1oPz403c5VeNcgFuPwiDq12/P86dYOPD70Mi/r/oPKPXhNwd8fflBufHzwD3qCWe+vF6yKP34EJyX2Q2kduqCjz/9lVg3BG6cRFX9L8n9+SE4BLYHdXoC/+nT3ci/IOhToXeZf71sDt3672gCh78t9wl5GuqvZN/t/99EJ1EKqneL/6m4P5uA/gP5+S91+2cTPiH+15clSKIbjA4nAV+Q377puxX38wfv+8UPv/wORf8/xehZU7p3Cd+udhr5oKq/ffv5Q3W//OGXnz80OYw1YF+/NWXyZzL/zK73df5gweeoj3+cC9c30ziFWYy8RzryW5b/n/L3V+RgJ5H3/Xr1BfkxX8YPioxKvC36MMEPOVNBrD/Y8aeX3yE1pA8uGm/DLP+P/0DkyC2zKvNrRHezpkagg+voCkbwRhhVCPw75nYJoF2rCBr2OQ7G/+jhETEksV//070z42f3yYyTB8F9u7Pbt5Hdvr2x26+viAElZmUURKmdIPv5bvc1tQOQ1uNqeQkqUN4gjzh9DT5DBvo8HiBRivz610K/3ee/5v2vd3qMHoy054SRjaomAa+jRlYI0id+F1I76IDbQNFJ5kIcfgQZ9BPUtMqSG2SzUfsqjpIE8aISqppB2h5lQwt9GYX9+uuvDoTwNX3QJ4E8uL+awAHvcJDPn6FCfhIFYf01BW6YIR9++/0D8l/IP5t1Fz6usYMM/rQ/RCjqqoLAfGqucBh0DXQmJIu7/X/7/WlWKCaFxQp6K/Ij8JgM4zEG3puN9c38M07RiAOgbaFdr6NNIScjUf2KCD7yjvdZpEbWDrOqRjyQwwIEUreHUm2ozrsl06xGKhh0ld9/QpoK3Ff91SntO8QrTGy7/hWRuR2sEVkC/xth3gfByVkaQfO/R8DjOhRSfqiQxZuIV0QZIxDJ7dLOw9J+ruHbD7/A2vA2HQq3kRS0X9OxDoLRVPd0eJgHDoKWcZ8u/Tz6HBZxWJNhZX1b+z7GHiuZca9o5de0eoa6XY6ucCH1w0WDJvLGAvD3Z0hVYdYk3t1+EOko6ekF7+mVewwaf1Lv9WdX8KjUyNcGn2Ik8r/UP4yg5uv1frWeG6slslKM/elhrLG7GY36aIhGeTBiHonxvca/McQbUX5Nkwh6vuz//hh5N/FzzA+K7Of7u3zoX2isUe49/MZwKssxcO2v6RsjQ8jInX6gajBXYSyPIfS24Hj3DWkIzTCef6/Od3eV3qg0DDEkb5wEut8HwHNGu9VhOabQ0+IwFsFo0zaM3PAPWiFQOjQ7lI9AEBFMCmi7u+mUDKoJs8cvs+v34dHY80AUXuNCtLB9BK+IBbNgjIQKph5sXMYx0Aof7qKQK4A2hhDfLVyFdv4AM3acT4D20xc/2v9563vU3pGM4KFM27NraMl25E8PdA+/vqN8egpCvY55dp/0R2c/NUV+LBx//5reEb5TNkzfZKy5P5gGgWlzre6hNrJPBRnkCp7hA+PgXl5fHxXyUYLfsXz5H032x3+vD7/XPPOPfvuChHWdV18mk0edeitTrzD3YalyoxxUz5L1+Z5Qn8eE+vyWUH+Q+DDQF+TfQ/UHEc9g/oJgr9PX6XhLilwwRuvzA43AfV6cPpPj3a/pHnz3Llw+u0JGG43ewxr5XkDehsAqEpQgGAc/Cko11qEWlr47g0L7f03fI+CZHZCg02CsflX2Q9beKyn058Nd70QPb6U1XNsbe60AjBuQZIRfgZcvaZMkn15S+wr+6cZjpHEYndAM40YF5glsWuoI3M/sxotGW4zHf9xQqfcDOxlTKRtL4sjZ73R5x+2VENSYe0E0MvcnBGINIAeOqrRj/o1134GqVZBJgTdir/t8BPvYmIxN0nsH9T8R3FMYco+XfRkz+RMydrufkPfG9RPytpW4b8vSBu6lfh6b5lFnOBR+vY993y864OWXP4Hx7KH/GsSTXh6EbjtjCRpV/BOdoLQSFA2sed6I57uC39fNHov9fsdZP3aBv728McjTS8+ODw6Hqfq5GqveBIYwXBCeP4IN3vs3esHnTMh1sCOBU2l/imOAcnDMJhnXtWfweOqzLksxGIkDbIq5OG4Dm8Iwn2bZKU0zDmMzDEkSM4A7DpT3CNZvY1GPRjRg6gOCxXDXI2icokgWY3Cb9aB82/amsxkzZXwPloPvU2NIlU8VHyqN9ntvS+8h+tD0txeHJuHIDVkJ88eHm7AHm8aZixI6KEP7gZ3OSNtSKKmurNm6tQZbP+PaxqZ17kzYorA8W7otNoq0zlfbU0xwCrehFztc909MyBp8lSu5x654L5/jlzgAm5yRPIZaqlrETf1aFxM3io+nhLsqWG5OG6kpMSs/Oa5Nbk3MiTCKnax0tkztg6Wv12UV00WT6Hm1oWzats+hfcE5URFzm8Xq/YpokkLsE62vpuBU+IJ5wy0QlaE5izJMYWJlT6sGRk92A0b7t+WE0fOe9Y8T1NcvoKT2gsHT+W2x7cvEvorrWDLJvMh1DN/ieiUTxfrW5zLcEWYF2NOJeiVDQbgRss4PiTbkR7CdUcrARyxWxplV0LV228ZBw/VYmycbm0rL0BEO2OJ4LMr9tJTb+ICF3vV4YtZXYnqUVyt24+2v1+bQD92+4sWozzV1J0uDWlFTITxvc2N9Lvl8oVWFNcR404snYkvhVV2RF2GRXsNru1gcdf44uJSxcyxyM1Bm1G0rlLyS9L411qmuZmuwxazC3PREnJsZzfZba328ho0ToGvZEpXTto6xTWltaj08qytMAZVV6jjD3lyiQA9LziuluVJM57RGhfJZP2wUZkGlRe5QM89S0ZldSNGaPGNGnRPlQPqHIYnbJp12p4qI4+sg36pZv3bVOjWwVe4WGOVctt6GSjq3qJLTzEIVwjzbYiD3qwZdq2W/6t31hckKgz/KPmksOm9LNQJW11y7iSvXiHgiGYpmi+1sbXaZdYydnq/i4XCyPMN2RWk6zJrLvKP7NNL2/tZICNxYhpiYa3TcnzE02HqO5UQsmpoJOl96vQ3CeMKJ3YWyIrCd17tJ0PKq2KOTdNLyAa0MmB+bFtVg5VI7g34XXZyFWJxuWyOv8vjQNjpjxf1+zXTZiZ+mOH+yuq0Xoph/887xtotviSH4eE33ZroRDJeWZmsGWGRxMtbmgQ1obM8R4c7lSOWURXkxvUA0kkqtPeEyF6N6dVjODU2/SqdKKozNJiLlSKGIbS0vS3SaJvG0vKyano+UqRGHRdi1bHBjNTvGXDZoC1+ZYYYj5KpTLDasa+7rQ5+nejTBfFLvBkA2+fpyITrPHPx8K0WYdYQBRAwHk4gN6yxZw3Vx2dSaFVhhtQhCaZZffbLhyAJNYJax85TLokxONoShArPjygO3Ta9Mb0bDqVaVgcOM6zCd7HY7ITEtkkmPW3kzy/WY8LYOuCbOZcmY8SBkRelf3Nk2BLZo4iR9pE211nHzkmCE3gPQpPP8vKqKuTvd7QK9LRpb72sjGVYLginSmcXwN345s+XbAlsXKzAcLmTY7zfYOeEXTYMZ1G1zWVgn2Z3JkhWvLJURwa2Ka4VZcmdB5YwtGVlqKvenNrtolWbmdM2lcO9tJktAnWIpWJ7rmd+xlt1cnGpQLoOmXDRAyTXtYTMDFdYMPmwH6cKd0Hk2sPsTxgr57aBjJSHzZXP0nY4wSLUlKp6dcfOZo022uhLULgmWttGsT6g9UxoMVrWCOwK9mTmKs+LCdbyLVf3mygG26tRrDnZXtuVst8kSUTVpFPgyet5IRsIHTdupxpmqzkLQBqduWWSLW7JO0k7CF4rJKOfLtnPbRtV4gRP6yKkcvi7wiVQWcD81cVedlaxW+va0vhoSH16ircx4rT6f56IrYMag8BVn2NVMrEmKcZJwoXdo23B0aINCt9MrTbldnoo5o1u259+GmAVE3WHRXJnMQxOV0TjOui2Rl265cWNmHqfqTZ9e9xP0vFih7EBsnEDm9uZl5kFSLo4D2gFpQIVbalBNQYYuLzlO39fNVmtFcrGsdTLeOofZgt7bUca3jYfxV2ztsrhg6EYhKkq7OmpRUZ5iHPgGRc2UNMXXLnbCOpNSaMFgZc3Sl4My7W6nVFvgYqszy3olEtudfpULtdgHpCDW5rmROl+hnX10uDB9T0oa0NxGVFj0GBCiue1WjJntOlIpgovChzVX0XpZ69Pt4SbYzdFa7s6otLM6ohIyNs5T2JCjypQJlowMXCLWTlTLUKHqEfqpcEmvljZnSqEc2WITWl5Xq8mK3R+5rNEKIydbG911212kcDFG+tVpkK6xKpRHV0pkSWy9Fb6htTLwDyoabaF2By0Y1g1TTppM5ILTWqTI3KwdYy+skuvO2eD5wQkC5ZLNc0NbSzaz14SNSZ2d7iBj/na2UZZbcZUf2/M+vOx5VTPOa4zTAsFfTGaaE7sxbWBnsKkkO5MyUw3k7ra9FIdF1TneZXvg27gVy6DfeeqtBox1vsp1zllXXmrE4+YM48Vmj3QXh8d9iUUWvTAEcsLI2HIaTxVWXdeq1qyNxMbrUsLPSwKPbDu0D8G8to9nfNvxRrOn5X0oU6Skq1dq1rJqtJlemxToRD7VYnbN3fjDQRUcdqOetcon+mBODLNMNzRecjMm46vOnq7Sgxbr++FiCbOMP+CaoGpljNrxhq7EWprgIbTmbl406ZG5chJTeV46uHYDuHwpztdSw9rdapNS066gaUkopOq6JAiCpXbELU7SfBUufJ1vDMIv1kO86rAzAep9qQFZSVKKOnuSQq2d7THrXaOwCMakd9uauwjxeZ6zFE44bVAL5na1PGcZkya1mVFr0O7ic7bqsWXQJvx0BpgqWRR6pQ+LYZ/P3WvvwNovXkllcatLWAbOTepJOqVl4jFZ0JG5tVZRj1sbXneNg7e1wq1b0drN4OJT2mo2lpyaDM9g2zejcJy9VLy5WLnTFbM045NOS1yK2hqZC2B6KOxFQ561FSXMz/N5c73MYWdAzTNuOq2uMjOImwGdLJPD5nzYH6b2QItaut+ssaO1dmpRk/KBJ5RNix+y1l5lq9n+2DQ3jj0AF5+2N7NYq6RZHUCVc4mpoTYF20qqHfBz3TvKnNu4m3Rx5PVq012WAR6siQWfw+7c991aTmQm0+WzIW8tYpc2ZrvYmNfLvm1g7yiYonmj9b1WzqzrVe3Xi3hK+bAuT4JUFXb8bGjFFJUuXUcWIqdsilice54W4dplrR71w3K9WRvnnalHZXLJEkYFV9Mswn1DihbKuvPcZNF+ep7lUbTcTxPONVchp7gacx0CbNiZBUGkS9ElXCcKj0wsSgSQNH+rSW7eMOqKr8443rawGUkPh9W55rKuzXPOnkNSMuYzS0fdvadzoRbx65l1VjInSBRrLpjnTtw561qzy/32Wgz7Vc6mbVfPcNJbSbSYaFa3vq34jFT7lbiUDTTDq0uELnA8nfCr02Up4WXFGMRpxYuagG0tp1/afl65YRyuKUfBmvPSm3oF3EMoZMCqtH3Rp/qabnO6YDeEvjh6MGpsPWd13RawgzbzuVmqDub5Eq/7euhsUsOt+AJEc5d4QrrKPH9QCbuegiZZlDSz9x1SERUzPhIoVxhKdGVDmueHFJ33eOxVi8X2dlVCXPZ2a6aOukUvUEOxuGyvXIOXF2cpMTd1fqhB452nU/4YHrucO0lzlZTBpoSslJsTWjngWSbTK188DCxZYEVtT04ZbPm4fAaicJXaxAFw9poWLare4DOVw3NiJnlOzKoLtCGksl7rQ3XRiKN80vJMXMKN6ATua7LWU/kEF9PFFJBys5Bay0mdqJ8Gt8WN8G70JZBWeWBTnHyzMVeidmF7Ys1BvfRodumD4+zWHimB5ec7oT4Ch0B98xBepoIHlmg2ZEpwi/1osidvqNIkyRqFHZosEx7mAA/lHYHIF6QfHoItSSutSs3Ufc6AyeQmDH61OFaZVNwmt2GCbtMEZcD2TE+PNR6wDsfWnNuArYkfBFKdX2ZHajFj3RnvaeqC5n1ytc7J1ZwWGclRbWGuqCqx5LRpOwnkcFlE+4W7iPQd2SxbGktAw1tDenZh7TJjr1cuwWlXE7Aw+Mt6QE2M6dMNWPXbZs/r53AzUww/ulRpQmkcSU1cJTWZCR8MxFEzFCF2OtSYRqnoe2x37Ou22ll7SL2ncisfS+B7Z2I9REFV8TPYmB0No0L5At95EbZB0WZ2SNHKZ9tOS1LNA+QCbm325zlsn8KZu7wSKXXz5b3C9Yxjsl0kRW3pRMO6YxlnOiMGq7iygGzlymFPzOV8pf0OJfqtcxK38mJHgPwsL4AfVTUvyJpnVHs1C732WO1nrLzsvSnhLDSeocr5zN+jW5XeBseCvN6K1TaBLQZ1c8pWcDkZO8yvxMVWh4XaNuyQciZQK7JxVTK3T7dgs19pElqS4aQUY9zftZfFdNNG9WmGu43CwmZKzoMLwTnzVX9TlmLQxtYy1U/LqcqzYJYeeGUWJgM/MDPZCMWC3qWHSq0EwNAMv1G6hAgYkZma7qAuUaf1E3XqhB0GDtxJKHH8Sh5mq2HjLz1nX8dMU3tARmt9s1KdABi75YrH1c0cl5WNf3EKuP8gdYFkDuRs1h7n5e5wwvBu2Vhcy2yX5dGr+Bss4BZ6VBUF43HpdFifzjQ2kPKe8pzAI1UmSIdFxnEukRkGzcZNJ1/mUeC3FCoPAWsLJ7DJyFncF3RO1AvshvonJ3OZbq5wDVFfAnJ3k5QaDQ2sTCYHvzB6ukwTQ9KcjtTZuZefVEWbZKlmTQp06WQAu4Hd3CFTa7HM+maQwr0bepBKghq/nZkZz6J4P3f7W2U5jYqx8pTLsuXxwl2FxaVPxAJnrZvky2zgHJxGmHoC5g2e1e7AAZXQ0Na5E7/VUSmFXaRJLfZzdKOvAcNIlbeTk4aSz3Q1uRwJQjf2BeYLM8Fshj7o6JW3aZcTpg8XVzF2yKpllw0hQH/e1oR0xqCObC3i3ZTY8EW1OFnxidBQasDktBL8ZUjc+No4hqeJhMutP58nrmB0vj0vlYlMC8UN42/ixVyqpXIUw4Q8skljSPlxmqnVGbDnTbMiI5QrmXLbzScMutSN+dmns8UOJCkba1espy8NYOSlNyEEobrhbrlD+YATGOpgMtk0tqtmuePTaaYV6WRrbH3PHSrntKInm02gTldTlcpxNpP3wrQzxblRs0LroFm8K3ZCMZtOQmbRurujl8H6M43qrnIbSqM3u6kjrkSZjuJsPp//4+XTy/hM+Plk9194ETs+T/v/9ljv8QTu7Z3O/ZkqsL0v97W+/Ctgfvn0UroRhPJ4XFklTfB8xPffHlZ+/uu3AOO8/vE+c3zd1NVvj7trOxh/evMSpV5T1WX/rcqS5jnDaarx1wDV+IMRF36/3BW55uPj38dS94PxKfy3Ovv2filKxzcowIvsGjxPg+dD208vXg/9ELnVN4KmvoEyH9V7vlOAWuGv01fs5ff/C1mlG2HJJAAA -->
