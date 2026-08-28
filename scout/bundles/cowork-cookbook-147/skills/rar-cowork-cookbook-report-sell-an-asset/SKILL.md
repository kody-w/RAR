---
name: "rar-cowork-cookbook-report-sell-an-asset"
description: "Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_an_asset", "rar_sha256": "c09f5666233c20a28769f62f68c0fd539dfccc6869a8de18add1d17a26602bb5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_sell_an_asset`. The original RAPP
agent is preserved byte-for-byte in `report_sell_an_asset_agent.py` and in the RCI capsule.

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

Sell an asset Summary Report — Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_sell_an_asset_agent.py` and embedded as the fenced Python below (sha256 c09f5666233c20a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_sell_an_asset_agent.py` first:

```bash
python3 report_sell_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_sell_an_asset_agent.py   # or on stdin
python3 report_sell_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell an asset Summary Report — Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_sell_an_asset',
    "version": '2.0.1',
    "display_name": 'Sell an asset Summary Report',
    "description": 'Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-sell-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-sell-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0009834f5e59b884',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/sell-an-asset'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-sell-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportSellAnAsset(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSellAnAsset'
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
    print(ReportSellAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7Va+ZfayHb+V5TOD/YEu5GEFuR33jmRBJLQCgIkYDzH1r4vaBeT+d9TAty2k5mXvHMS3G0Qqrr13e27t0r9+4vVNmFRvXx62XtWDvFWmkahV0FW7kJs0RdVAt6KxAa/kFPkTRXZbVNU9cuHF9ernSoqm6jIwXSmjVK3hiyobqrWadrKc6G6zTKrGqHKK4uqgQofqr00BbIhq669BrKcJuqiZoT6qAmhpmistP4ANZWXu+B9gmBXnpW4RZ/Xr2BFb7CyMvXql0+//vbhJQKfXz79/uKkQBpAoN9X2YMV6Jye5IMZqZUH4FY5AiVzcF16lV9UGfjK9XzoefUeoPI/QP/2b0lvVUH9y6fPOfR8fX6Z/ultDjWhBxBadQP0cqzSsqMUIH+F6LS3xhqoCFTOn/pHefD6mPldUlFCf5/uvX8s8hp4zfvPLwWAYE0W/PzyC1RUYL2qnT6/TlLK97+8pkXvVe9/+S6nbu3Yc5pJGED9+uV5/RQLBn4fGvn3Vf8OpD58ZXufX35Qbno9cE96gpkvr3ER5e8fgsuq6Lzcyh3v/S9/JdYJPSdJo7r5X8n99SE49CwX6PQE/suHu5F/g2ZPhd5k/vWyJXDrP6MJGP5tuQ/Q01B/Jftu//8iOo1yr36z+J+K+7MJs79Dv/6lbv9owgfI//yy8tKoA9Fhp94n6Pcv++2a/fWd+/3Ld7/9AUT/j2L2RVs5dwlfMiuPfK9uvnz59V19//rdb7++a0sQa56VfWmr9M9k/pld7+v8ZMHnqPc/zwXrH/MkB/kLvUU69HtR/kv1xytkWGnkfv++/gT9mC/TawZNSnxb9GGCH3KmBlh/sOMvL38AUsgf/DPdBln+r/8KKZFTFXXhN9DeKdoGAg5uosybwB/CqIbAz5TblQfsWkfAsM9xIP4nD0+IAXF9/XfnzoYfnScbzh+k9mVitC9W/uXOaF9foQOQVVRREOVWCun0dvs5twIvb6Z1ysqrvaoDDGKPjfcRcM/H6QMU5dDXPxP35T7ztRy/3skwerCQzm4mBqrb1HudtDBDL39idgC1eoPntEBoWjgAgR8BvvwAtKuLtAMMNmlcJxFgYTeqgHoFoOdJNrDKp0nY169fbasOP+cPylxAD46v52DAGxzo40egip9GQdh8zj0nLKB3v//xDvoP6B/Nuguf1tgC5Z42BwjFvaZCIIfaDAwD7gAOBARxt/nvfzwNCsTkoCgBD0V+5D0mgxhMPPebdfcC/RHFCcj2gFWBRbPJmoCHoah5hTY+9Ib3WYwmpg6LuoFcrwTlxsudEUi1gDpvlsyLBqpBoNX++AFqa+++6le7su4QM5DMVvMVUtgtqAtFCv6bYN4HgclFHgHzv/n+8T0QUr2rIeabiFdInaIOKq3KKsPKeq7hWw+/gHrwbToQbkG513/Op6rnTaa6p8DDPGAQsIzzdOnHyeegWIPaC+rot7XvY6ypeh3uVaz6nNfP8LaqyRUOoHuwaNBG7kT6f3uGVB0Wbere7QeQTpKeXnCfXrnH4P6nur5/1v1HRYY+tyiMYND/e4cwAaF5Xl/z9GG9gtbqQT8/DDR1LpMhH83OJA9EySMZvtfyb0zwjRA/52kEvF2Nf3uMvJv1OeYHFXRav8sHPgUGmuTeQ24KoaqagtX6nH9jXgAZutMMsDrITxC/U9h8W3C6+w1pCJJwuv5ehe8uqtxJaRBWUNnaKXC573mubTkJQFVNafO0NYg/b7JmH0ZO+JNWEJAODA7kQwBEBBIB2O5uOrUAaoKM8asi+z48mnobgMJtHYAWtIbeK2SCyJ+8X4N0Aw3KNAZY4d1dFJR5wMYA4puF69AqH2CmbvIJ0Hr64kf7P299j9Q7kgk8kGm5VgMs2U9s6XrDw69vKJ+eAlCzKbfuk3529lNT6McC8bfP+R3hG0GDlE2n2vqDaSCQKll9D7WJcWrAGpn3DB8QB/cy+vqohI9S+4bl039roN//cz32vbYdf/bbJyhsmrL+NJ8/6tG3cvQK8h2UJCcqvfpZmj5OqfTRyj/eU+knWQ/TfIL+OTw/iXiG8ScIeYVf4emWHDneFKfPF1Cf/cicP2LT3c+57n33K1i+yAB/TeYeQS18KxffhoCaEVReMA1+lI96qjo9KHR3vgSW/5y/+f6ZF4CO82CqdXXxQ77e6ybw5MNRb7QObuUNWNuduqnAmzYX6QS/9l4+5W2afnjJrcz7i03FRNcgIoEBpu0HyA3QkDSRd7+yWjearDB9/nmDpN0/WOmUPsVU+iZufiPHO2K3AnCmfAuiiaE/QABlAHhvUqKfcm6q77Y3cSOolu6EuhnLCeZj0zE1QG/d0X9HcE9bwDdu8WnK3g/Q1Ml+gN6a0g/Qt23CfbOVt2Cf9OvUEE86g6Hg7W3s2/7P9l5++xMYz/74r0E8KeVB4pY9lZpJxT/RCUirvGsLaps74fmu4Pd1i8dif9xxNo8d3u8v31jj6aVnNweGg/T8WE/VbQ6CFywIrh9hBu79r/q85xzAbKDnAJMcmPJxgiDQxcJBYQtdkgTlE6hPLB3Yd/EF5fqO4xBLgrKWrocsLddFXIS0UIKAUdvGgbxHgH6ZynY04fBg31tQCOq4CwLFcYxCSNSiXAsjLcuFl0sSJn0XkP/3qQkgxqdyD2Umy721nPfgfOj4+4tNYGCkgNUb+vFi55RhkSfZVkObqgifdvL5xo4W0uFSald0QImq1NRYbbKKv6GzDOMjfL0LxWuU0Ru4sk0MT2a6OOsPpJyfCtZPSgR159eYt72R9VYRlhOONxLFhg55bizV0BnXDWcZ2FW2bH4/cJ5zVeFj6XcLnJtzRumCZj9Ka9PQB1M/XtfuZStRPVwPe1SEbb60SRM3bIcQNs0+3UoIQ4h1ylyCZHYRTVGXhMzIxE4Jr1t9tJoTjnrdoSFcf7/QFlVPzsf1kaQu0sCeK2N3CQ07QZljameJdLRQhJMFDYfZhOqRZSqmDo5w6qjAFVIUzPVGLdblETe2lhnP57monduTlipcRBmpxBGnNdcfzZaHC2yhUJx8WbdXyUKMs32Q9KwLpCvcHey1FzcXvLJcH3YR4mzhJ1HmrP6AjlJIY8u+U6+JV55l0ZC4WJoFCbFLZFZVcAV0/rJq1n61yJO1qGx3CYsGAUsOzmXLXPilciu9ZpA3fbY4j4fgeuJYqzy3EW4UR2nw3co8X6PxOpyv6sGBmd7xlyM7rG2mqbNCsQZ3pIbyXBSVkSDEbOE2h5o6sVfrINqXkDuGOStqoqydCia2t+v8VM3VsMAReMUdnL4TVGlB5jOfi5ucNmN05sRIMrajYtez295gyQhpzk5h2PwgcF55uxK1KbbqslmzHd5eI8aoxXrHzamiUEItDwOKsOqbQXczMehbbiMQnHzY18MgCcdl7IYGfiz3eb0xD7N6NiszIzpdTDyH0VxhUW0uFzf1UpQYLGfjEXcWa/hqRU6f5SvdPTrYVZkLZKOl0pJdk2t8th7Aj16Rem1JO2pL9ZS6FY0bpWzrU0BwI7KoD+YlUuWDaXtRbZioHO88M8upi76pUoszGyGJRCTqh1Hs6nOvRqYcD9ftbB5tkZtoS+Z+pl5QuNS0HY0jc0x1aoUwe14pJVtEiojrGLvndlaoc+5R5JNTEJLJBY6UFW8t9b3CqMzGV5d9WyqOJwfjBsmdq9JrHbmfmWAvtVTIDbsR9JUkozQXd8vIjpszFfjr2fWyzNHWKhdrC4EVb1cjWZxvs2W3Wjr7WUOdACL5RG1Z9VTtyWw0BRjXQ/x0FM62eVFNd3MbEj3opKALmtWZRZQDVvI+5l60E8V1obxf8UqO+8RR5MpzvvGU89W7Frd96hnWRt/NfUdKPJMTkfpsKg7IyOpSw4ExO8Wtey4GHzUl+YJea8LWZyc4ZS9odIzqmeaPRYoUKXWKQpOp7as3Wrf40vniYZUmgUavltSKJJKzWLSlag7RfEUf5mjlqU3gjfGMPK/9C6z26ZziDXYrReRIOx0a4dttoJmOeG4wGYVps7VF+7opUM4WVpfNho6JZWC21XE0hh3LCKh4CF3eL5YYs2eXEdad6AC2zlVOYqUk2EZs50RimcFy3CwGsuoJLPD0GnUzw9rBS329IVniSurbS8NVepujWCv4TDh38RVfLaJ2TLammrmIKGF85q7M6rxYKR6y5xfWfL1u9HUrMp5KUBmt3Ux+FFSz8dZ6tJEPx7lgrHrJdhSZF1vhPNvaSIuz5R5B6NYJtYN4aS9YcA02JeNtVIVjmqTPZ7R8MrhLzI8un2k7RN5tdLk6yqq6MVHpOiq8a8JCgIbr9W68sOlBxLkm2ijkrm+P85LZbeD9IHJnXrcUTAoxmFylDbOXjUBHEhpRqhie72F8GZeb2JSlC4LM6kUFk8qCQx2kSyO1Rsm5SiRJge8XYqzZwi4l6SLRttYiD2/UpVB1aiA5ai3RG+2AzeatfCvxZZsTaX4a+9l8PhyEMZwdXRqQ6mwpH5IkWPP9ZjxWIA3FkPPWoXDFEYE30qYbbMZBj1hqmbTrMBJanEJ4PjOHcc7fRpzJVZTbpdrBi9aLwxpPAvTmqtVVhGlAGOtmRwqsK8V9Ge/ja7L2mL2f8pd9MY+WCs5Jw257Kzv8dgZMu/RGOMfcmxv53AHZx7NFbFZ7Zlartyxn0yYx871a+mlW2CgpY3PKFsw+itH91SmlE7aI2/W2HtLbXmfiXOgY/JaRsXG6ximoeluxlcXMqDsjQILonBNskHIDtlc6YXUa5iKD6cUx66hZJlyUPhwMb5Gtm+CiCUUUkAeuWpBtttOZndtJR15QFxffRjgJZsde23J7jrScgQ7qgTj5BlGd12Hh0Mb2WlRmAbMs0/LmcWnY6mmbs7ceDXWpXBLHbQnrh3TN691u1bNCYAtrguKka12f8gZn+XYVlXLFaYeuuPZ72wFxEYUHR1+vLGwTL4YcP7R4ZhuytYs2l/rMnwbJtFo+ttE9epQ3aSube2Zb0EuyppTuuFbmHpqoASpGlDfLwbBzQMKVZZWXNJFaaaUjVrohNX2mMiVDbG4nJROJUzOCYBa7TMUp/UxphJJuNjY5HvNRtiPEIDTXA1Az0+DpmawkOBaivdUz+XHX6PqhPGwURRjZZbqgd/tO12lKEkjjRuiIymaBkB2YGRn0KAGohWxVYcMcqTJY6b3n1vSqK4gLItr4KZW6g4oT22aey7ebfIhjnZau7IIjvWTul9Ea80BlP1o+c+LHgVLqKkH7XEW26LnVYakaGvdW7oIddlR2G4my7AbZmaFs7Ol6zR9uNNoYTiWehdlmUPRzGGxO8VWSG9TLEWGvXHbrmVFoOkZFx2p92wt0PA7H41X1wXZJPLcGHPdJI8q4LO3OEolnpQZSK7V2hrZ3MLsO92sDw7bnUb3tT0f1Es12uE1UKp0MnLPe3Yhj4eytSApaycdLeg+nhM62hXkoUmZVBkzNryRCZIbVORsRRV8Sh5uAuVp+IPLrVdwRMl5y5a0PzWvX8E2dhEZPxHa2wmxtODd7ntV2ZZbNU9/KJIs4G1WyZRyp3XTmJj1Y+JVOZrxEVAp2IRW+1LKAYVrWjmSziwi6V1tBYORiczr5Xe+qoDEpd/V2t8wceGvX5g5fwfxpP2r8Xiow2nAz6RDICJ8NVqIuQJ+V5yukBvuLzW2/uvlFTV+2Gbms9cs65ENkr0SaFRh2AWrkiTFWvMBVl+1Riqo0LtJK84Us7mHWWNDoEpEdT+NPEX87EQq8ZkSusKJQkYDteI93DiIGOsI2Iy0ySsD2V7s4pWsQqS2I16275lqHcqJIQ4E0GwO17xbVgZJ1PGCwgrXo+iie6GVmLlz3orDhLuaI0bxQhR2kjEEfd/aAA+JujlaVacl15XJlU90Gd2FgLi0SYrrrsNBgWdTJxQ3PoAIFS+ZOX6xJsrolrOOHaWijFIM2LJuV67HbNDtK9ZOlshutcNlEV7OOEcuhdILOqN4sTSQMbXHlX45q5c7lipG12GRVmfd0QUvYqPDy0jvkl6IeYFbXToQKr217lNvkKvZtcohhLSeFKjwR7fJAu6S/EUoqgzuJC1bKAc5sVR0X8BVwqcPkzeZ2ZiPDVWy1PVumuCDVYJXoQw6v1obCuc1Cg7mFOToX1l+nPWnNWk3eh/R6ESzgpRSUK4Lsd5aWkcNwjES6czrbrGCCIhrrujxjBEZxq4vXtgZ1uGY4xaMpN/cE9gSTiNu2/fZWOJV3c4gAM93aWxNhBHO4zFNqBV9KomQ5JOMFPXBIh6BnPXsp7TYlNoK/sKPbclhyYX66OIipLy2CWQowgWyiS8ak7nag9Lm2na9s2o/0yjTtG6DYRSf1OsnxBTODOUQIDv1WlztqETOLcZP63PbI86uCrElpdrskEtzPNXogC28W1cNcC0d1a53mFG76y0DSEs01ltTM87GrdyBUrMyvobewVm4tomtxji9K+3IMAozdDt5aWCDjre7nzhYW5719FXbOysnrBsYqmk4w0lHE1WE1o8e1dhUSrufFzXyJbVeLWKJctsm1EWs5uhTw5CIEmEMxXH27bJub58DkGK/5BBXbUNQvTD6XYzmMd3mC01qH+0c0TMil0C/Q085GN8mpmcV9nF981w39Ue0TzRxSltl1G9b3sBlB1qoAXHYGLJIVbdaBnpoP541ZkCiCZOk8jectr62Vq1uhvXpmrvJGiG/UNg4ctCZVEo/EQjp1zWHBbyqZbVpZsYVb0x1uvmpdbYPs6HFokLhVM6qex26XnNF+d8Qkt6X24znC5hx+2OywAMvPka9Lt2N3jnHivM3ttjHZYIXcTJGYrZZHFz5inTFsheMqlZlev42LE6B64SJZjOqrG1xZkyyJZo6oYyDp8Z6M0nKc0U2ywzqwk9oivjAkoxvycumzEnzK8rRvMDQZkM3aww4XgdaBaxVhPfYOsaL9MKiqBYwWbRcoYF/o+0PmDOphvVw2HtIbqC84Jd5uWiq3NG3Ms0tg37yDU2Q3R9awsYgYzvMtO5Tnt7ydrQmi6ZKqctuFBJy0CgQEU8S8HSJSYIJKWq/8W4eA7b7DXP3miurtLPPUgSp4fllwAXoUbHtuyVoE1wJqmJQGpwhFSbeN4lo4wW+w1sMEb6Vh4nK40kGuEg1MdGZTHzb9phCWmh8rmMZHvBASylZUru3VAD2PTeUISgjacrfaVQ0FhqzI8VZ1+N5TnZaQEdo7Gd480K3VbMuehLiRQ7wQKJFgF/C8j43VXBu6JZ57h2LWRtZNbONmSGFBbUO/nK3m5JbsZ+vdIvd7E12mFVbtmEOfxWsOPrM5IgYIAuezrFfJArSdin4l8JZcOV0044SllQUWuz8KV2ImCsIMPuqC3kXCHh1JzO4vW1jPiEbFmvlwRBcX6gAje1Hp6nqlhTdruRP6OX7eh1KGbwCjYC6rHdQT0kTWybUXzSWiGoqQW5S5XHdceNU7N8a77ZH1bsFS4zzniKgzkV3OnZ6pFdroG40r61W9AL4ds/kxg3M1UMg6PSb8IvVQC9+2qb8LLCol08TBbrGMtRUS2Bt+7s3qjSMmc6nmqNh00IG1TlW7xeX6pgqkE4yz+XlMlhi/EWO3POptvNOlGa7MS4cNtdJXGkOcUTeNKeODvPM8mtwfgkVayWMwwPkO39WMtljsmW4W7bSijsjbYebXAkMmJ/VsRLnDbonw2GY9xc1psJdwb6tS7Gn65cPLdBb8PNH9hw9ap9O0/7NDvcf527fnN/ezVM9yP93X+vSPYfz24aVyIgDicUBZp23wPNr7L8eTH//srH+aMT6eUU6Pk4bm26F2YwXTH8+8RLnb1k01fqmLtL0fin54sdt6eqpfT3/44YD3lzv4rLwfdt4XAR8s534Q+6UpvrhRXRa19zI9c5+ekXhuZDXfLoPnEe2HF3cEdo+c+suCwL94VTmp9nx2ADRCX+FX5OWP/wQ97l8qhyQAAA== -->
