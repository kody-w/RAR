---
name: "rar-cowork-cookbook-report-record-life-events"
description: "Builds a structured summary report of record life events activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_life_events", "rar_sha256": "20879b8262b924d8110c61b36dc54720ff6205cb350a16b604c4ce17c126628b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_life_events`. The original RAPP
agent is preserved byte-for-byte in `report_record_life_events_agent.py` and in the RCI capsule.

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

Record life events Summary Report — Builds a structured summary report of record life events activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-life-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_life_events_agent.py` and embedded as the fenced Python below (sha256 20879b8262b924d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_life_events_agent.py` first:

```bash
python3 report_record_life_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_life_events_agent.py   # or on stdin
python3 report_record_life_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record life events Summary Report — Builds a structured summary report of record life events activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-life-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_life_events',
    "version": '2.0.1',
    "display_name": 'Record life events Summary Report',
    "description": 'Builds a structured summary report of record life events activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-record-life-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-life-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '537b6f7ea42d87f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/record-life-events'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-record-life-events', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRecordLifeEvents(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordLifeEvents'
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
    print(ReportRecordLifeEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aabOi2Jb9K/TtD1nVZl5mkHxREY0oCAIqk0JlRRYzKJMMIlTXf++Dem9m9at6/V5ER5uDDOfsYZ29194H/O3F7dqkrF8+v+ihW0CCm2VpEtaQWwQQV/ZlfQZf5dkD/yC/LNo69bq2rJuXjy9B2Ph1WrVpWYDpiy7NggZyoaatO7/t6jCAmi7P3XqA6rAq6xYqI3Dkl3UAZWkUQuE1LFoww2/Ta9oOUJ+2CdSWrZs1H6G2DosAfE92eHXonoOyL5pXoDa8uXmVhc3L559/+fiSguOXz7+9+JnbgEsv2l2VdlcjAy2ruxIwLXOLGNyvBuBuAc6rsI7KOgeXgjCCnmc/NGEWfYT+4z/OvVvHzY+fvxTQ8/PlZfqjdQXUJiEw021a4KHvVq6XZsD8V4jNendogIvA+eKJRFrEr4+Z3ySVFfTTdO+Hh5LXOGx/+PJSAhPcCcsvLz9CZQ301d10/DpJqX748TUr+7D+4cdvcprOO4V+OwkDVr9+fZ4/xYKB34am0V3rT0DqY9W88MvLd85Nn4fdk59g5svrqUyLHx6Cq7oEKLqFH/7w41+J9ZPQP2dp0/5Tcn9+CE5CNwA+PQ3/8eMd5F+g2dOhd5l/rbYCy/qveAKGv6n7CD2B+ivZd/z/h+gsLcLmHfE/FfdnE2Y/QT//pW//aMJHKPrysgyz9Aqiw8vCz9BvX/Xdivv5Q/Dt4odffgei/1cxetnV/l3C19wtQG407devP39o7pc//PLzh64CsRa6+deuzv5M5p/hetfzBwSfo37441yg3yzOBUhi6D3Sod/K6t/q318hy83S4Nv15jP0fb5Mnxk0OfGm9AHBdznTAFu/w/HHl98BMxQPJppugyz/93+HlNSvy6aMWkj3y66FwAK3aR5OxhtJ2kDg75TbNSCmukkBsM9xIP6nFZ4sBhT263/6d1785D95EX7Q29cHt32duO3rg9t+fYUMILCs0zgt3AzS2N3uS+HG4N6krKrDJqyvgEa8oQ0/AQL6NB1AaQH9+pcyv96nv1bDr3duTB98pHHixEVNl4Wvkz+HJCye1vuA1sNb6HdAclb6wIwoBfT5EfjZlNkVcNnke3NOswwKUqAQ0Ptwlw3w+TwJ+/XXXz23Sb4UD/LEoQfvNzAY8G4O9OkT8CfK0jhpvxShn5TQh99+/wD9F/SPZt2FTzp2gL6f6AMLJX2rQiCbuvxeIqalBFRxR/+335+oAjEFKFRgrdIoDR+TQTSew+ANYn3NfsJICvJCAC2ANZ8gBYwMpe0rJEbQu73PAjVxdlI2LRSEFag+YeEPQKoL3HlHsihbqAEh10TDR6hrwrvWX73avZuYg7R2218hhduBClFm4L/JzPsgMLksUgD/ewA8rgMh9YcGWryJeIXUKf6gyq3dKqndp47IfawLqAxv04FwFyrC/ksxFcFwguqeDA94wCCAjP9c0k/TmoMCDuoxKKtvuu9j3KmOGfd6Vn8pmmegu3V4L9bAlAGKuzSY6P9vz5BqkrLLgjt+wNJJ0nMVgueq3GNQ+/tarz8bgkeVhr50GIIS0P9P6zCZxAqCthJYY7WEVqqh2Q+opr5mgvTRCk3yQLw80uJbfX9jhzeS/FJkKVj3evjbY+Qd4OeY7/zQWO0uH6wugGqSew++KZjqegpb90vxxsbAZOhOPQB/kKkgkqcAelM43X2zNAHpOJ1/q8xv8ACnQYBBVedlYPGjMAw81z8Dq+opgZ6Ag0gMJ0j7JPWTP3gFAekAdSAfAkakAGOA3R06tQRugtyJ6jL/Njyd+h1gRdD5wFrQOIav0AHkwBQHDUg80LRMYwAKH+6ioDwEGAMT3xFuErd6GDP1mk8D3edafI//89a3mL1bMhkPZLqB2wIk+4k8g/D2WNd3K58rBUzNpyy7T/rjYj89hb4vGn/7UtwtfOdrkLzZVG+/gwYCSZM391CbuKcB/JGHz/ABcXAvra+P6vgov++2fP679vqHf60Dv9c784/r9hlK2rZqPsPwo0a9lahXkPmgTPlpFTbPcvXpETCfpnz69MinPwh84PMZ+teM+oOIZyx/htBX5BWZbsmpH07B+vwADLhPC/sTMd2dCOPb4gL1ZQ7obMJ8APXxvXq8DQElJK7DeBr8qCbNVIR6UPfu9Ang/1K8B8AzOQA7F/FU+pryu6S9l1GwnI/Vemd5cKtoge5garPicNp6ZJP5Tfjyueiy7ONL4ebhP9pyTBQOYhOgMO1QQJaAdqVNw/uZ2wXpBMV0/MeN1PZ+4GZTIpVTOZz4+p0r72YHNbBpyrw4nVj7IwRMjQEDTp70U/ZNNd8DnjWARsNgMr0dqsnWx5Zkao/ee6e/t+CewIB5gvLzlMcfoanP/Qi9t6wfobdNxH0/VnRgF/Xz1C5PPoOh4Ot97Ps+0QtffvkTM57d818b8SSXB5273lR+Jhf/xCcgrQ4vHah3wWTPNwe/6S0fyn6/29k+9n+/vbzxx3OVnr0eGA4S9VMzVTwYRDBQCM4fsQbu/fNd4HMiIDrQjICZGDKnGW+OUZjHYEQwR1HEp1APpwKfJGgMiSIKQ0jfw0nERSmPQgif8EOU9lGMorC5B+Q9QvXrVM/TyZgQiUKcQTE/wCmMJAkGpTGXCVyCdt0Amc9phI4CUAu+TT0Dnnx6+PBogu+9Ib1H6MPR3148igAj10Qjso8PBzOWS2G0pyXerKZC2znCopciF+NYOZtty6+DSFrkJ0NUyM70Ym47aGuk2ZuDP+zb+iDEBrkq6MWuaeekQg/iuUIxHsXi2LrKhXQenTmdbZm5s4lTDtE6i+dsK7eIsnRJ85hlt+MFPiL5uBJQ81AlGxi+DnLIe7UsWxyXdc72kl1KVEpgwzhViSlH6kWTHHVznGUXkSLRVpMs0y+UdVlsLsuR98i8EE/O5njx+OBAL5HwdL7ZDe4MzBavSEb2yfB6xMf9cArrShPTeuBUbl27mWmfa7s8bZIDVlar7CQfBANfHm9mjg4WYq1FZii0plQZQ8WFRGEshdLwdPTPHp8yaB0PMmqZ5TGz9554O2yVRSkfFX/gnb2F9pWNH7SUuolyLVCbtm5d2dD84QiaHqIz9qt6WN600yHriYUQoriQr2h+vynRzI/zQOT4bD8LeEDBJjp0QS17W3FgHbR0GnZvIh7bef1Bv3JVfz0SF34TeIEj9WZ04vlDGu196qBwzRHfoGfJnAWHG1fWdX7enk5Mvj9sWlttEXRRH+rcqFSuUCS3ya8RTquXqND7ozHsa69hL2eFMCSLd4aAxTySyin/SDZttO1iu6oFlSCdoCPh4mbTTs+XTFeIjKPITSHQu6Y5j2sfa7OlpVwa2Q+s6qrKG9TjD9esjIOZjKX7jZrs0mI5w9JmXLn+ar3Tsc1wO8GprY7ScXdjs7Y8iPNseQn3HYFtKarsmYQdYLpoL05mW5ZVOYxa9XFjXAdSSa+mOXcXsuP6Xajb3Y5zza22PW6PKDme9uM8ak3qfO19ozEKwt31Z9+emXaRdrIOz3ekMUS7qErmyZln912gezzWOO5RQpNG8whNPXFEvcWwXFtvSFWopPOww04sKju7ZtMzqTkuyQseUobIF1K0yfdw7ZWkbgcJPZYFaxRkkWmc3SVXRT5cbJeQnP7IyppgBtrZ0XTJxld0eVZWanZOSnHjcGLfDH1eK/ODFA8KXjQd2ncnYjML93qoaDRxFCkt1PhBLhKPj6gQXac3eBlXc2xE1XZAbh1guGHBCMjRTX3Rw/dwP5upVUeHG4mJUGalhk3deZodGbzgtdE+XOwc8XKt5K1yUmyy5kYOVWN5Lu0SdYQXt6PlIcMxHtMdvxFulrVwbyGhKQxi5FmNlGh5KciQOMdzQjaW/tCsbg0zC+VRl7Jht4soSUphWRkEo9U8ZFbT18pdWZmQ8c7c5by088dbJSUn9FraWzWTSV5DG7y4VAknaJtNvGKWI5HGUi2cu3p1i9rYganz8RTEBVJG140lrkqUrXGK04RtugwzJNRH2dLwXYFvBHtHMHP5cF5ZM5r3O4Qys6BKlNV2lCRTkwsjd5S9qcUH/sJsxE1kkv32zJPA8i2M4Rvimnkm1Z28ZlRPuHFZygdLmu2C0MTj5VzKx/noOkvjxppjI2N1s2Ly5thuqJDgB5oqdx7sLFiVqFvCX542BqNr2eJSHA+uskDG8SQhbMeMsF0NqevrPuGqtLKI87o5s0eqTfbL+XFBbSqaEWVWIjFUrxZ9htPkXBg3tXsoa5RhpPMh9IQQjOCVGFFW47iopPkBjg1+2xzsoTnK3um80Gapcs4p4ebZTEdRY7I0gW1yVmnJyuGXmmNliyaV5rTbNyu2WsQrlyTz9LSQWiHk0bnN1AOSVCLtHG42AcKmVw08mHc2MpYVoYPGJbruAAOP1sw6LxXUO9XSFTbSWrpsNfWsRfV6n9Gg9G53BzxPZvOG3XYdySTtdsOKs2iUMnh1TIeZBW9vt1nrX3kUJvY7QY4Txw5DS73pq4UqisHmgCXjUWGvurRHxY43ulKxl56nBQulPIsYCw4uZEYsbFc6H63gbCknpO6L+qxTrlMfyg5Zucsmaddmb5Qx2GVIbJyxvLjgIks5rmI4natEfrlJBOnz5pZi9bJmhS6reCpuOe/GpsjiIDVdCthxdtPTi1Cy0fVW84wCCxy6MTKvK2qjyonqcrNo3+q8BSxG6YA0DsegWctLXuNLBb9pbmif3BaJkO5y1hlDaWhHR4DVABeJrEFtTDr0frnXzxdubvGDpM8xvsZvmLRAtBLpWoZJV46PxM4W9gtvexL7rkPJIBPkS5nrJyaNYuJiEqu6nmGz22WrlzwDqBhwWe1OXrcabUTovGo4draNuUpl7bYOVvM4WBbZlTdHa173PoIQZz2LFpkgqIpJLtSsViSOTeZr5rbqtMGodlZGhGzdsoGeoYtMIo7toZIbHRH11vAdgvVs8YSPHql2DGUddCQx95QdK9fUb0AbpHe03VkSV2Z2XuwliaNhJ698M42vJIJUKX8b/PqItk5oiO4MNXT0wO85JmfQQC91yzt7J9Peb7stepLyUIajMlEXtVRcd5S6knbauVrwgZMeYG3Izc0Y0CPbJKQT9y5beee1umpz+dCfqQufcqIKJvML1Mm4MRbJ6FKCTcrSS2mmHM7JuOdOVTaj4wGbrXG/xfPTOb74l3hp9WHgB8uqnDmo5GWYJZwMi6R2LVzIIwob+UmL65TDeVrIdlE/rAiwyzdKlMaFw6xnNldZbFGlvkTNzT9VjnxrA6Yy4sg2lb1IMW5Vk+wxkS2dbVar9RhgneXXkr2eie0q7Zec2a1Xx6KeM9sLKC16r3bomdNEpjMv5mivOWOoTTtXjeiSSUpnIac+biU5UyURUZPhZhY8c9SzkiukrakKPcltelNonENRiRfpou02vgWb1CLztbXKKz0vrVdYddrsyGqZnhNaP1SlQIM0MpB4eWY5ylWWSWGeuVg29MEer0oZ7eQzF5hBZvFrrd6VGResfM8KbK0R+DbcDVunqRcnVOwlMm1IP7TmF39+XPW1eRG2hNk4YePwwiVpMIMwh2DLcEZ4uOrLxZKD92vckoXr/rSMsYuALfiKoP0o8v0mU+hS3eipYzKXcOe3CbetFOGU+WZni6ZkXild29fzQ55vB4E592TExFQUB8V5nc7scjVG6kjYc2uVHBJUl7ntIba8UhvXdWknJ/lkH2RsZXeUfZGQ8ciMpcJzWcDudoyNrI2qoE4lPjP49SyVUoEoNW4FQgpvC9D/8E0NS4GKjvq4xQS/O3ZNu1eXDbrepiHegZ7ltvYOi/Q6XzCMox33gnG8NGfJZg/ldrOQ7GJOYHSKivGK4olOXxrHZOs3sVgOLhfiqhujeWopgpCJRq0mp2hWx/nueF7uLmoBqvGNc7frJuH2/WrX7byyb+K2reARdMIsBV9kAWewxVI3ha3O57PokNLeUbTFJLdGxslFrzu1ZtBKV1ao8KPlCqmGbxeadWxQit3QZaacdH5Xu4a2vlyWKeGcScwtVD8ebHzJN8nScXWVAH2vhaS+nqCwQgcXXKMok4/W4ZLe8ZV0OaczuLd0qbHw+XJfzmysPxyQExOLKk/c2hBNqxIPGlfZ3tacv/cDs+cH1D/6Dl3LJwHlcgVzlAWKaPPKzDhWvnJ4RaCqLVowFlttJy6bajXI/jwkWrvGTijHOMQVoU/IEeHptVtflxa+p3CxnOFJb1o7GKYru2j7XTaQQaCMBzX2BIo8sfyOFeUr2BVFJ4uHy8ulja3eWXfjLtbFxdQkdW2+7IN29Gb2jLu5Nttda3FQQ25mEIHQ3ZT0VgRmwmhSt4Rlfx+ley8+eOOGgo/XTZ/R/PYSz1ASpcvjsNPkK1OcFviAZdEaNoV8WdItvekG8uwiPbxlB5xoGZ7EbWJNEPMuwtGMhG8s7eqZZTC4w8BpxYRt0RWhUoGdIS70sDsU1SmugmqvGKUI87d9BBuKFPlsHLbmDFTgcCEq7payRqHilstT27PnnRIhrBjPwExjYZunmczOty3pVYnVkBi+um2bwiUFElHXKbE4KPUiZ2D5wpDGmAk2Kisnhx3S2eIa6nyXW1W4FBZ01IZ7KjKu/XEZaQHb2PEQ4cOaC4MsOA483OFcVBn82eQ3WySku4amvZ4VrGXojqWXldhVuLlrDHHHwj3OQnSW7xiCILShEju/Z2LBjtMQXiLdbNGDfgC/Yn4eV05bz5Ab364ObWIVTtfW9OxI1tk6uCo2f2ypMrj1uA83c68Kds0KZdkjfbGaGddFyerI9Zx4IG9iYevXYzGKnXsKSRf2qrLj1HhMZseqQ5f+Kl6j/ulwW1qHIVixvYrO17tEt6tedm+bkGFnyhnmvPUh3MyIWc+RJKW3cRKuYLwvSxKuF3MmvPbEcrXD44Cl0GYQZz2S7Rw7xbidkl2WHEfifo4tk70YkQqv2TBOcqpvFTp/nMPiNZY2PFa0c6nDqZ6kG1nRQjz1ghE5Nzd13Noj3C7ALvCKbXheOvOEZygqfKvia9J1JYZ5uEC1AhxWS3297QMrji8hIywbXxCuZa8y22hvy/ycr5i562Aw41C00KG2M/SHpbMPQrKNW2oMB2yo0KrLu97Tm2G5M7tIS7dybXNXDfdXM1tlWetKLcz51R5bo+zFct0r+M2kdljKrxfUdlexZUc5lB5ETJFv6PWB0Jb9qaULRF3W1OjtrgHj3gK0mJ3mHUeRCYYKir6+wrR9MGpzt1ng/HXo4m4mtDXs9uFMQIcjJeN0pR8wvbs51HDGtbadLWGYrxcdv8eLoBeoWVbf9vuFd0uN1QohuBx1tzh/vs64PqBK7HwA60CROb3Srxd4BfafeXxY6OfdhZrt1gA0sAHR+rQIsYHG6F6Su4MwuwJGZBhkRNzgSKnpRvbJPdgCdTjB7hJY6wuuluN8bMcTIpKKGh0w0QnUa4gWMobi+FprGq3cZ6Wnwc6J3q1NLhyTeccH/uGmzCRhDvs92/jisQ82q1bZNbhI1YMAW7l52sYK3mbnco1nIS5U6yYDLY7LVHTG2tTIyXRXJyVNbOFo10s+GTMbX4WxfI/dBvdYhzIh+/B2LfunIaS9YdVTAiElEVnuO8/XNxglz9NeSGZVpARqybRgr0NeDTkOfRYPtRhvz7Je9gjusPtGVXE7ZK/bi7Et5zF98hjUXy93mY8m2Fa7bWDYdgIjoZZw1a0Xl/UQsyz7008vH1+mp8TPZ73/+2vZ6RHb/9mTvsdDubd3PPenrKEbfL7r+vxP2PLLx5faT4Elj+eXTdbFz4d+/+Pp5ae/fCkwTRse7zanl0+39u3pd+vG029wXtIiAE1GPXxtyqy7Pzj9+OJ1zfS7gGb66YgPvl/ubuTV9Dj4oQkcJGkdfm1L4EALjl6mN/bT25QwSN327TR+PsL9+BIMYAlAc/8Vp8ivYV1Nvj1fMExIvyKv6Mvv/w1JqKmBzyQAAA== -->
