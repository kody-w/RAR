---
name: "rar-cowork-cookbook-report-identify-business-continuity-risks"
description: "Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_business_continuity_risks", "rar_sha256": "6bb546bb534cf29fe2b90300a38937c095f5bf747ad161fb17c64207888bc20c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_business_continuity_risks`. The original RAPP
agent is preserved byte-for-byte in `report_identify_business_continuity_risks_agent.py` and in the RCI capsule.

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

Identify business continuity risks Summary Report — Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-business-continuity-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_business_continuity_risks_agent.py` and embedded as the fenced Python below (sha256 6bb546bb534cf29f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_business_continuity_risks_agent.py` first:

```bash
python3 report_identify_business_continuity_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_business_continuity_risks_agent.py   # or on stdin
python3 report_identify_business_continuity_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify business continuity risks Summary Report — Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-business-continuity-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_business_continuity_risks',
    "version": '2.0.1',
    "display_name": 'Identify business continuity risks Summary Report',
    "description": 'Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-identify-business-continuity-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-business-continuity-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55173d5db73adba5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-business-continuity-risks'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-identify-business-continuity-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportIdentifyBusinessContinuityRisks(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyBusinessContinuityRisks'
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
    print(ReportIdentifyBusinessContinuityRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZObWJfmX9Fkf7CrZSeSECD8xhsxYhdCaAG0UK5wsVz2fYea+u9zkZRpV3dV91sdEzGynSnE5SzPOec55175txejrry0ePnyogAjmfBGFPkeKCZGYk/otE2LEP5KQxP+m1hpUhW+WVdpUb58erFBaRV+VvlpAh+naj+yy4kxKauitqq6APakrOPYKPpJAbK0qCapM/FtkFS+00/MuvQTUJZ3oX5S+xVc5pchlGBVfjNetn7lTaq0MqLy06QqQGLD36NdZgGM0E7bpHyFZoDOiLMIlC9ffv7l04sP3798+e3FiowSfvRyuqvePNVST630u9LTqBNKiYzEhcuzHqKRwOsMFE5axPAjGziT59XHEkTOp8m//3vYGoVb/vTlazJ5vr6+jH9OdTKpPACtNsoKAmAZmWH6EdTzOllHrdGXEAuITfIEyk/c18eT3yWl2eSf472PDyWvLqg+fn1JoQnGCPXXl58maQH1FfX4/nWUkn386TVKW1B8/Om7nLI2A2BVozBo9eu35/VTLFz4fanv3LX+E0p9BNUEX19+cG58Pewe/YRPvrwGqZ98fAjOirQBiZFY4ONPfyXW8oAVRn5Z/Utyf34I9oBhQ5+ehv/06Q7yL5Pp06F3mX+tNoNh/TuewOVv6j5NnkD9lew7/v9BdDRm1zvifyruzx6Y/nPy81/69l898GnifH1hQOQ3MDvMCHyZ/PZNObD0zx/s7x9++OV3KPq/FaOkdWHdJXyLjcR3QFl9+/bzh/L+8Ydffv5QZzDXgBF/q4voz2T+Ga53PX9A8Lnq4x+fhfq1JExgTU/eM33yW5r9r+L318nZiHz7++fll8mP9TK+ppPRiTelDwh+qJkS2voDjj+9/A6JInkQ1XgbVvm//dtk51tFWqZONVGstK4mMMCVH4PReNXzywn8O9Z2ASCupQ+Bfa6D+T9GeLQYMtyv/9u60+Zn60mbyIP9vr1R37c36vv2nfq+3anv19eJChWkhe/6iRFNTuvD4WtiuPC5UXlWgBIUDaQVs6/AZ0hIn8c3Ez+Z/Pov6/h2F/ea9b/eqdR/8NWJ3oxcVdYReB39vXggeXpnwa4AOmDVUFOUWtAsx4ds+wniUKZRA7luxKYM/Sia2H4BgUgh44+yIX5fRmG//vqraZTe1+RBrujk0TZKBC54N2fy+TP0z4l816u+JsDy0smH337/MPk/k//qqbvwUccBsv0zOtBCUdnLE1htdQyXwcDBUEMquUfnt9+fKEMxCexzMJa+44PHwzBbQ2C/Qa4I688LDJ+YAEINYY5HiCFjT/zqdbJxJu/2PvvbyOleWlYTG2SwWYHE6qFUA7rzjmSSVpMSpmTp9J8mdQnuWn81C+NuYgzL3qh+nezoA+wgaQR/jGbeF8GH08SH8L8nxONzKKT4UE6oNxGvE3nMz0lmFEbmFcZTh2M84gI7x9vjULgxSUD7NRl7JhihuhfLAx64CCJjPUP6eYw5bNWwncMu/Kb7vsYY+5x673fF16R8FoJRjKGwYGOASt3at8f28I9nSpVeWkf2HT9o6SjpGQX7GZV7Dm7++1FBec4XjyY/+VovZvPl5P/PJDKavOb5E8uvVZaZsLJ6uj2gHOWOkD8mrVEezKdH2XyfD97Y5Y1kvyaRD/Oi6P/xWHkPwHPND36d1qe7fBh9COUo956cY7IVxZjWxtfkjc2hyZM7dcH4wEqGmT4m2JvC8e6bpR4s1/H6e2e/B7OwR6dhAk6y2oxgcjgA2KZhhdCqYiywZwBgpoIR4tbzLe8PXk2gdBgFKH8CjfBhyUDs7tDJKXQT1pZTpPH35f44L0Er7NqC1sK5FLxOLrBGxjwpYWHCoWdcA1H4cBc1iQHEGJr4jnDpGdnDmHGUfRpoPGPxI/7PW99z+m7JaDyUadhGBZFsR7K1QfeI67uVz0hBU+OxCu8P/THYT08nPzadf3xN7ha+8zss7mjs1z9AM4FFFZf3VBu5qYT8EoNn+sA8uLfm10d3fbTvd1u+/Kfp/ePfG/Dv/VL7Y9y+TLyqysovCPLocW8t7hUyA2xzlp+B8tnuPr/V1+e3+vr8vb4+3+vrDwoeeH2Z/D0j/yDimdtfJvPX2etsvCX5FhiT9/mCmNCfqdvn5Xj3a3IC34MN1acxpL8xBpAS+vdu87YEthy3AO64+NF9yrFptbBP3ukWhuNr8p4Qz2KBbJ64Y6ss0x+K+N52YXgf0XvvCvBWUkHd9ji2uWDc2USj+SV4+ZLUUfTpJTFi8Dd2NGMHgKkLQRn3Q7CI4DRU+eB+ZdS2PyIzvv/jNm5/f2NEY52lYzcd6f6dWu9e2AU0cSxM1x9J/9MEWu5Cghwda8fiHEcGEzpaQtYF9uhJ1Wej6Y8dzzh9vY9m/9mCe31DYrLTL2OZf5qMY/SnyftE/Gnytke57/6SGm7Sfh6n8dFnuBT+el/7vks1wcsvf2LGczj/ayOe3PNge8Mcu9fo4p/4BKUVIK9hu7RHe747+F1v+lD2+93O6rG9/O3ljV6eUXqOknA5rOPP5dgwEZjQUCG8fqQevPc/HzKfgiAvwtkGSsJNE1uOP9Cl5SxIByxMcobOZga6IlHCmpGYg5kOsSQMe47PHXNOWPhyMSNWq5VpLWYWlPfI5G/jeOCPxoGZA1ByvrBsFF9g2JKcEwuDtA0ow7BnqxUxIxwbto7vj4aQVp8ePzwc4Xyfd+8Z+3D8txcTX8KVwrLcrB8vGiHPBr4gzJNnTgsc3PQruTF9LTdU3TxyYYMX3l4OaZNK9IW/2pwXFIuFuRErvMFX29mcORy9aXoiwwbdx4DjInGQpLTgqBirrIu5T5j4SqBdktPrDZWvlEg/4/XpIvV1trsojS+sp72S2ebNVMiy3vqLuA8Xt2w4AyXmJASZZtXyWoezUttsL1iaS34dsLFAyvt9jGm1d+g7s8sv0yxdoXXUSzufjODc5st0Jq24KvbP7k00pgpCG8PyQrWrRoqmdiKFhJ2gS3+YL5CD0w7cgjj7ue2J/TazsKURStdd0BdX3iu2RxpDlR3a5jszzFNpr8QzPudaEz8kOzUasjOpq/vUwg5DFK+8A853IO25LbmlGZ3fdp1birx+9TPzGM274ja6ZioHiaDxQGyq/HC6lNN5xTf4VQxWl1jr/e6y42orTo+7w0rqjIxJLwp+Ubxb36TULhT5YSntVlrs6HEBDvMhCVlxd8BDeuG6NNHhvcH0ZyLZc9MFG9aqSRbink5W+mEb+rkANyjh2feQS+kpcZ93t5xRkFQNl0i25vzbgjZ1mbrNfSJKr6rI2NdCLGZkjRiJiDcc2ybKYmC2GbNn6Zt6sQqKufRABMVlagqnoSj5bYy5YA+0K3Dw1YKfW52xM7OVfGH22MarB4KUNalmLnMP98+8HuwNTEkUYTpvIn568SkUOWy7dbpgp1saWbRafEvUZE3icW1faaRNTp691etNVFV0K4RNqfYcyhOLtK+G22YVrDocT/RYtKP0YquG1UnLgawDZi/PD6zb41piZmFcKbq8DQfDFuNZehxypXHiSxofQpQr3KPTDYduL7TaoZQ21ZBduK0zFaZdt0+S6XKqHniqt3LS5BZM4cBgq4QuoJcFF6TLRlHrMgvPfRVwxQnbuKRu7eiFifA75hbJbW/sDpTIGmRURdv1GqtQK7vsj3Nsrqb7oezbxrPOx3MsFSf2YNHlcrcWtsx2mw/ypmBL0zVnNEvz+Op023E7ir1dupt6joHEtrYv6+g22DHFahFEqZY0G9Bf8uYkna9pZBQztYwM/ort52Jb4OzphFyHTq78+alO0TxRZ2ZwyqjeawxoLdLWZ5PvTki2uoSny3bVYFbmk0A7LjjGo+Rmg8URp3f1vjPXnVyviy4mcS9YoSctQvjL6rLTVfEUO8am3ge7FOndcn+gkhO/3a4V1IlXbU5fk8XgMSfUxHeRk4TmltvtsXPf8Ah3rqtEaYcs44krOIsyLSk5ulztgkDVr56iolQugLNcZvy2qOPVamZi3aUVkY1E3S6AmpPqgV1eZ3VxE7XEzdBljAbH+aY7ItPlRhFPBaY5+K5jaT/eieuanPvY/JDximXMypu0mK0vtSmba3ZhDrbn7UJ+33HWUbpec51eppXrqSy+v+rAU31zd+yLRrNi4agzOWiGy5kv7MAMln1PRblILPgpcsiRvccNS16PtChbJrVbmXVahWQ4W2QcPiwNsyW3U4eJk+VQUIiTteuQsQVbUUKvSsxzHjDLVg2kmeYhvXqTcoYH6m7pzE2eLvhQCvegcXZUwvbTOAMHPGhpw0ITHljUiSQhkfZ7JZNqzsJ8G4tiLPEZxNVSjF2Ls47vVblpqYOs2O7OFGfphmIgbL5eQzvZWWauciLtb/O6pQVDO56MvXbuuQyYm5DZg1LyOuN485jdRd/krk+cEuoMBMFY1Zvt0SgFUC7pIdLAgIN4b+NAkjlyhxuDas4hGxeL6X7bnHo+t2yndhRF0zNzkEu0H8Qpt7Zl3suQ62pFWdJRapq9cLtKvkcnAUYi8kXF+Lif7nORku0V7h44qU0NZH85V/1FoOT11s6VmRfcGm290lxDB1JytrIjTSxUgs68LVe1+JLmCrnjy+Pl1pV5trX4TIiFK8vNIkGt1oYszpiANvjuiJY0UgYhuMTCmfaMQpxqU0Plp0mUSNVF83B7z7bX8rx2VHat4TGKsWlJ6Gh3crXzLPMKuT46WwYzTffMZ8U5O8BkHq6ycLp1M2TN7PxZuc3JWRxtO2JpdgkVNl7Uz08cw/MENQ98Ijhfc4a7mMhBrLdidCyRxItaP1YUyYg2qWk45JQhF4fuWrGGLBVXJ/X4q7zhzfzom8nu5BmwRGNgAqUv6AOxWyzt5faoyAIWMMiZzY5HlZJZTSKUDlNO/F5KwZJbRIN4a/V1C5tg46ehGFALXGc17CZfDxGrrlCPXmSrXDtn2lw1Q/rYHHmMvro3mVNWbB6XZRJUmMLqVqSUx9xxs86OIuBZKl8CmdKuu9M65w/1fkiAK0/LVabMQs1zTcBGO+rm1lWHZscyVoCM0XxzbDAeQ/Q6y26114jEOVO4fkU2F7w8OUOxX81Ua3HNbgzJzxe2H54QwgXM+qbuAY0GxdaphVvqkxsdw64ybrPigXIL6qyr/h5V9FzbOFN/Iyyype6SOCuqkVCtq5g5Hz1B07TN0VnPZ/Yl02BmUycXZRlCU+srUvFayBtrVN43iMXHotejKLDd5WabDBvuYAmJWR9MXLvYyqU7c0owQwDwhQabrsizJTAMK+4ZkxWArzvXWlzKQRbD/XuX+F1nb5sCEcM9EeulZwUZduiqCi0SmGf66rjZykVBphjFsjpDHYNCdhzL5+ooWQ8Lbxb0/K46cqVM2QchJkQVT3N2thTK+RGms4olW1FmPHE+XWacNAhHKcp25Zkt+pCktpxMSVrNeYOWsPLVr1IlkfahzLYZL7YsVekXKQ22l/p02Nvz6hyv0dbfG7Q+943dJVJZDRkUIRKZhR+djhVKbRm2oJoNy2kzQ2D4bBPRV0/XYORPxylwtqyRnbe5GoeXq7plcUle5HjHHPeSgZ5DR9UvAZfartrJ4VUF0Sqzdl3UXU80f5ldS05pMkssCYrZWrm6EUAgFqqY0sciSJYHvVpq5YWBjJXTC4qLCGIJcUKtWJPirFdqg61i52B5Ph1kMs9kQOOP+7z0Lja1T+cL6ejWOKueIfFWUbFax+AIJIJ0VXmFHrxAurnTGciPN2oWBbssZP25ZWi7mwVbKXCvHMpwJ4MHU6zivJQtPCoi0ks7tXaNIG+E+U6jLuIAJ3CP3Si5L4CFdRIHt+9IylpbbEjCGthGUhVrhLWUKSRzqyEukt1xsQjV4rB2HN46a8b6dr119MUVU0ZJlXgr7KoaN9QNv/b20jkMO+KIMls6pxQXx/p8eTLS+XUnioDHmZOJNgGxD1p8rc5Uw3d8TttIem+F7k24ObA2PMsgrCpD2o7ftP2qIPYz8iLLN5bOlMgn6bg0gLDRN6f6MkTnZEvGgayBUmx2XHa2b8bFP6I15+gol+MtTWTzdaB0QpEPOpvngreUQ3JhFBtr3euwEfZeYBqaPYtO+/MMbuq9ObLB7C2iHJQjAc0RCUfMxLx0p057VfRycT06StoUXsuDWSC70vw864UF5mW3xEnz9a4TeOe4OWnteYFalRaRAyJZGh6oXsjb7JI1KvUqcljq0lJX4Ht+uT3FNc9KUlY51fm2OBLYaj8vTnsGNJdiygm56loHTgVEYmyv6EKcg7ZFPbRGNWourdLabp0E0TXiPMNJT190SJDzcnthy6C5UtZseT5N8XDV6DOLWzqtaTG8W6EXVGTCADBqSSBz3r3otnAeZjrX1ekBPzGB0YmH/FCQqhDRDuFwG7rL97zTGXW5SDqjVX1XWzclgxfDRl47oeAh7bqZyn7j8XjDr4U5as9NUPWceXOKdCt3ItUBu55yK/nAaCTiOE6pHWq2M1jGbgVk1ThBIRIY6tMAPTN2qixg5S/T6GqEdWR46rK+uLvZRruiNMsWKeI1M+a0xCnBzcno4vHrlg8DcRhYkuJYIeLP9G0bhIdODzbYIqrj6DIkpkVwpy1D63yHzoQadxdZ7qE6IhkkdgoK3uCEXZDt2n7K1xd/KOMks0hNRJz5/EhMz80RRS19vilvS+CgvkABuyLPvUxeD/wpY6hQS/jdrF2Ckhj09shfmKnRNVKWLRy6NeAOxBwSJ8RTZB4MFb9d1/jBI6idR3FkzWTkijuhqF47pb2j6AVxDSpXojdzk272w868omUzOMYeB6YmNVJHYYNXYzWGoTTm3MR6vW4GrdCXnIXwXM21/LEavNO+DUF8TU9WKzB9h2iEHbIC5TJlo5I4v9ygRY5dCn+TZy5+o1yznPMHT7l1R8no9oe9e2UVp76G0kE4Wo5BrWaUeGn1xhe7pWZZyPm2Ao4TRfzGrJmZVHgXY4ryMxQ3Wa09cl7lUqdrXSzb41ECQ7Gb4gI9TSw195dTB5hwJl7x4sDOp0jbL9CLJNik7Rfx0icW9nKGb2s9oRx5Kff1Te46TNoFAm1gdjalrMMKmbcCGAzYpxPUpCTz6HWnCpC0vtRu0z7V8X66HqZg2hxh+zioZKRh15bY8el0Hqi+RqOFdIrnzqIf0krKie14Rqwgop2jm52sYGy8WdZVK5K82R7F4LqmFGuGWgK+nXdgIbLr/TmYsnVdztkA23vpasOxC9U5b9GcWlIxupiy+9WNOZrV6rgEFNGjulOXU0O356hck/aZIHccAfccohWAWUPErjPjUtVxGkaeAQzVGjcic31tz8yrYXdsrdWBTrY94aTklJ4iQgdp5zo7VAhnTP0lq1lU0Xkndo1hypq0rT0SNSev3+UJyhp736gHq1geKgWRkaNMUTs6Eh1uQBBnu3LTXGYySbaZamYl+RG2q5q8OC0BpCxKZ0bLZex1OvRui7O20DKI2UdUvL+hnRgSgpyfcrMA8xrOe4VjE9trFdT13jQ43NueY5sho0M4tdv1ci90M21OKiyzComBatf0vPUO3Dyly8Ebbn7ubFWg8hmccg1XZeCkbYp2jChutrb1fsUPzcYJpI3cLNJmwzU+UWG7dYREhGj6zdZC8cVeVWw1cDwiwaY9Crfr9WLlybxzZXZFINJRr/vdeQ6QXbzWDnM1C7IsISudQfc4ZlGDK+j9jkcqStH42Md2NJyPlKFpuW6u6HMhTCzTsTqPRDdXuEPxE9s82KVWt+mKR9Z6cNxKmrA9rtcvn17GA+XnsfDf/wZ4PH77f3YK+Diwe/u66H4iCwz7y13Xl/+Bbb98eiksH1r2OPsso9p9HhD+h5PPz//y9w2jmP7xNev4PVdXvR2sV4Y7/u+hFwh1XVZF/61Mo/p+CPvp5d1U6JwFf7/c3Yyz8Wj5oRm+MezYT+6H4d+q9Nvj6Be8jP/HYPz+Btj+90v3eSr86cXuYeR8q/yG4tg3UGSjy8+vMKCni9fZ6/zl9/8LH6KW9KAlAAA= -->
