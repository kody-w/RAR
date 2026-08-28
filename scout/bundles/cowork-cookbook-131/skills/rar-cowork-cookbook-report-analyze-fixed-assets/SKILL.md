---
name: "rar-cowork-cookbook-report-analyze-fixed-assets"
description: "Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_fixed_assets", "rar_sha256": "bc75f05c1e3bee49bff1c69115ac7129d68bee13489772b670479ef6b23e5698", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_fixed_assets_agent.py` and in the RCI capsule.

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

Analyze fixed assets Summary Report — Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 bc75f05c1e3bee49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_fixed_assets_agent.py` first:

```bash
python3 report_analyze_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_fixed_assets_agent.py   # or on stdin
python3 report_analyze_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze fixed assets Summary Report — Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Analyze fixed assets Summary Report',
    "description": 'Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-analyze-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0faf53284b08fa6c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-analyze-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:analyze'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportAnalyzeFixedAssets(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ReportAnalyzeFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+7OiyLLuv+JZ54fuOXQvUN69Y0dcRAFBBFReTk/08AZ5vxScM//7KdS1uufs2XP3jrhx7YciVVmZX2Z+mVX424vTd3HZvHx5OQROMeOdLEvioJk5hT9jy2vZpOCtTF3wb+aVRdckbt+VTfvy6cUPWq9Jqi4pCzB92SeZ386cWds1vdf1TeDP2j7PnWacNUFVNt2sDIFYJxtvwSxMBnDfadugA3O8Lrkk3Ti7Jl0868rOydpPs64JCh+8T5q4TeCkfnkt2lewcDA4eZUF7cuXn3/59JKAzy9ffnvxMiAOKLK/L8Y8FuKmdZj7MmBi5hQRGFGNwOQCXFdBE5ZNDr7yg3D2vPrYBln4afZf/5VenSZqf/rytZg9X19fpj/7vph1cQAUddoOWOE5leMmGTDgdcZkV2dsgcEAgOKJRlJEr4+Z3yWV1ezv072Pj0Veo6D7+PWlBCo4E55fX36alQ1Yr+mnz6+TlOrjT69ZeQ2ajz99l9P27jnwukkY0Pr12/P6KRYM/D40Ce+r/h1IfXjODb6+/GDc9HroPdkJZr68nsuk+PgQXDXlJSicwgs+/vTPxHpx4KVZ0nb/ktyfH4LjwPGBTU/Ff/p0B/mXGfQ06F3mP1+2Am79dywBw9+W+zR7AvXPZN/x/1+is6QI2nfE/1Tcn02A/j77+Z/a9lcTPs3Cry+rIEsuIDrcLPgy++3bQV2zP3/wv3/54Zffgej/q5hD2TfeXcK33CmSMGi7b99+/tDev/7wy88f+grEWuDk3/om+zOZf4brfZ0/IPgc9fGPc8H6epEWII1n75E++62s/qP5/XVmOFnif/++/TL7MV+mFzSbjHhb9AHBDznTAl1/wPGnl98BNxQPNppugyz/z/+cyYnXlG0ZdrODV/bdDDi4S/JgUv4YJ+0M/J1yuwkArm0CgH2OA/E/eXjSGNDYr//Hu3PjZ+/JjfCD4r49+e3bnd++Pfjt19fZEYgsmyRKwO3ZnlHVr4UTBUU3LVc1QRs0F0Ak7tgFnwEFfZ4+zJJi9utfSP12F/Bajb/eGTJ5cNKe3Ux81PZZ8DrZZMZB8bTAA/QeDIHXA9lZ6QFFwgSQ6Cdga1tmF8Bnk/1tmmTZzE8aYGwJqHuSDTD6Mgn79ddfXaeNvxYPAkVnD/5vYTDgXZ3Z58/AojBLorj7WgReXM4+/Pb7h9l/z/5q1l34tIYKrHt6AGgoHpTdDGRUn4NhwDnAnYAu7h747fcnrkBMAQoW8FcSJsFjMojINPDfQD4IzOcFTszcAIALgM0nUAErz5LudbYJZ+/6PgvVxNtx2XYzP6hADQoKbwRSHWDOO5JF2c1aEHZtOH6a9W1wX/VXt3HuKuYgtZ3u15nMqqBKlBn4b1LzPghMLosEwP8eAo/vgZDmQztbvol4ne2mGJxVTuNUceM81widh19AdXibDoQ7syK4fi2mUhhMUN0T4gEPGASQ8Z4u/Tz5HBRyUJdBcX1b+z7GmWrZ8V7Tmq9F+wx2p5lc4QHyB4tGfeJPJeBvz5Bq47LP/Dt+QNNJ0tML/tMr9xhk/qzmH56twaNaz772C2SOzf5/NRF3tXh+v+aZ43o1W++Oe/sB19TjTLA+2qJJHoiZR2p8r/NvLPFGll+LLAG+b8a/PUbeQX6O+cGSPbO/ywceBnBNcu8BOAVU00yh63wt3lgZqDy7UxDwAchWEM1TEL0tON190zQGKTldf6/Qd4c1/mQ0CLJZ1bsZCIAwCHzX8VKgVTMl0RNyEI3BBOo1Trz4D1bNgHSAO5A/A0okAGOA3R26XQnMBPkTNmX+fXgy9T1AC7/3gLagiQxeZybIgykWWpB8oHmZxgAUPtxFzfIAYAxUfEe4jZ3qoczUdz4VdN79/YMDnve+B+5dlUl7INTxnQ5AeZ041A+Gh2Pf1Xy6CuiaT6l2n/RHbz9Nnf1YPf72tbir+E7bIIOzqfD+gM0MZE7e3mNtIqAWkEgePOMHBMK9xr4+yuSjDr/r8uUfeu2P/147fi98+h8d92UWd13VfoHhR7F6q1WvIP1BvfKSKmifdevzE+LP95T6/EipP4h8IPRl9u+p9QcRz3D+Mpu/Iq/IdGubeMEUr88XQIH9vLQ/Y9Pdr8U++O5esHyZA1abUB9BoXwvIm9DQCWJmiCaBj+KSjvVoisof3cWBQ74WryHwDM/AEkX0VQB2/KHvL1XU+DQh7/eyR7cKjqwtj91XFEw7UOySf02ePlS9Fn26aVw8uCv9x8Tl4P4BDhMGxaQKqB36ZLgfjXF7LfHmvfLP2yulPsHJ5sSCuTVPZ6CS+Lf0QPuBNwxJcCkVDdWkxaPfcfUA703SP8o9p6dgFb88suUpJ9mUzP7afbel36ave0U7tuuogdbpZ+nnniyBQwFb+9j3zeEbvDyy5+o8WyR/1GJKTnrHlDeRHVTLStasMkBTukenp/Kwdv9PzEQiG6CugfVzZ+U+27tdyXKx8q/35XuHju+317eiOLpimd3B4aDjPzcTvUNBoEKFgTXj5AC9/6dvu85FZAaaD7AXNcj8RDBvXmAukGA0W4Yzj2Cns9xxyPnC9onKPD9HMUomiQXLkEiGEkHIeEu0AAnaArIe8THt6l+J5M6C8fxKDAZ82nSIbwARVzUC+aLuU+iAYLTaEhRAQaQeZ+aAkp82viwaQLwvQWdsHia+tuLS2BgpIC1G+bxYmHacFxLdYdYgG4ZPeyPtHZIY80LRPnQ+d1JzbOiTH0DdZw+wgRFEwXqcNWWkMyM9sDLcLqHbAsXrfmChJfSoRFcxwwT/bCROjJAGwruhThaX4MIS6FiIY6GCTVzKd7uzcxwqGZlu6Z542qv2ul2FYYwzqlSjORZFMeHxVZKiIbpjmY6mMpNGteo7O+G2oQQxTAtpRq3enUcu72y5/JyK3OX/GAk5iHGi+q8vW2cMxLyR5EI1CIe4eCy11ShgYjLfi5xRJfZ8c6o65bbbuo5YUdu0h0TQeoaO862lUdUZojV1/2Q6TtJPAZng6W2B+Gsrh0cqfP6cI7rYiBC2eormfMGMyM4zCzFQTcjbqnbbh7kRptYa24f1O2uSjdna1Asx6rOuWLkLT6npZ4IIEpeenU6z1tbcm2OSStV3t6cqqhNadQPlT2qpS9jInutj8pROm5z3GgEAscgphpiF2bM9Xq16hrmdFRdT9vC7VG6Su0iF8tDSul4kiaJAHYNes3toMvpkEtSs0tqQ7wdjnstpEZ5WLvLrs1L2Rn8kR5Eu6xuXIoshB6zi72rcPy1OOC3lVytNIy1j6bX7EV7DMSgpr2Fdi4u3u60uzFUizVhQBNLV3ADrTM72Oe3YkltRuVG0Tt92wvWPGETQ7Z4L2cz5dyjdo4sxtLbCjxUbzL7msfMBTLl88iNHr9zkUE838QQOy5HyLjJ2lGQuFjtbQAHB3Nodcoc5xpDK9zyacMj1/1I35QTqdg76gRZQ+LetOuytHbZacThqiMQHSGCWu+DbeoXxbbAFIknBOFW3lqjwAwOi0Xj4kvXcqcisKksU6hfzWnA9ucUN4i55rlHZ5zzx64x4j62kW1x8hdGtVtT/djqvL8WttzFFaMz5vv2UHMpxAnnQKQEyqjy07Xc2GukUPXUp+rdbU2P7smxdS7tTokjH1fWqfA4iiGXFaefFrZ+OPYJ0e6lvWAHm4XG9nYi8YfgOM89/qgpYo7R6dBz81Cwbol1XIA2c4ULqEbtoUS8hkNBXLpx2V0QedGIVLHonQpd23PyCjFz02m81kVclQ41rg1JQpKOFwLrpQbN4K1sXwJXtiQqam/uKNbIJkf59Y0LjNgpnRxZC5tmyHEyxkb7QhhqvDoIvFzgFqGLXGUXm0y266Aub4fcNBx5b8Chd7q2yO1I2tcOwztazS1/3Bm4onDZmPLwKa26em+cEOpMkZ20LoAcw2kVd6yNeZnRVh2by9Ktg5H1uRZp2grQgybX0YZekUTOim1X+ebAwhcmhfH9hU8YddBgqC4ZdL8acJu+8ogEj0y7mRO0rZ4L0NOW0fo43lZWspfIzmj48209+nKFnQloObaVjvm30eDWPZcwPSohrCfgg7n2qSLR6pVoHQfYMPY1UmM4lJ6PCPhaVnZ+f26gJc7fYnJT64lELfcEmS8acr9yult+DrenBPdp+iLA3tLZjpZ39Q5q3zFMrGSxBJums+fnZ7TR9wumh0+qvrZiXdjavWTzm7ocTJEYhzW6jU4RpuzXqhW13rVP3RzTzrhfHI2RQxXLrHBrQ+2MnCgOKh+tNP5qE1BJR9EWxdhyd5jndLFBEp3OJE3bczczMgM37Xrd9v3VnEOYvFzwnM0fan9p5Nawvdn1rUOXJcNiHHM+bfXU0sRl5WOuPwwLurC5TbcwKNMTrBwxqwVyUQtXzB3cHpDCQm+0ctxTeKA6zWHgm6qHb0o/SIpOIvN8d249utUAvy0awlNQrornqMW1wrAptRI3PSCAunVh6K4pKC+zCzbQpRrvNFu5XNQdPR7Wy/1m40uWHt9MNbocRG8u9ca57hF0Qxb9yDqH6rhVeiY5rM05qZyVjAYMRMukj2WJjlspuokQYrvapVbtjOYlKjQRq64HatXpIiapLM9qEqcdVMJXD0e+ky1U29TWytNWQZNSUIaaw2WbkHa13690G0UxNEery5nzqu7WNfusQgrfEk+N2ZXnq4OUzNI26UYolHQuxkQ3rHaBfTvFTbw/r5brziR9gTQlQyHoCgO9A59m3WmXaO15hZ0P82V1qPGNqNy6riGChOtsR9w2Vli56tKNMLDnv231ob0s8b1XI/OQJZrc0jtCoSWfW7nQCCXOQXfkRqOwQuibVbZbO3KvuZTlmNJWE1ZLdXkwyF0Wu2vJNXB+NGED3elzmLsebOkozZGjLq6R5QpxF+t4Ll7lS8nKxhFsS+qEDgJh3Hrl7pgqqdlAW6ld5+i64fHg1IvZaheJYkEE1EUNcb9O/c1+bfUb5oZljSKYPXkcMUMUHYnk9aVtC1RztnLNkXh1C/oLxLHj4BI6XEfK1g457nYVfzLYJolS3xQPPLqlzQhhOhknF9aV5uZIRXpa0Kodet0R/npQ91EzZKcw4U2HMvi1FPJXprQhicll1kMlxVmFMg8P4nxdrVMPQ8zeW9X0xhA2R0c1iyvUsFll0et1vOGg/EZ07sVmVJT2L5p7Nm7XjHEiBg9QHdpFvKDlnWEG1W0/pFgAwfRlkG4QJi+01NlYS7eF10Tukcu1f7EroGu3zbish9VzKPpFidsjzR9rl12gp8IFjYU5rM+EtAi6QYE2CsuxPLPgpTnONidJ2ZPtCudtftdpBCXuaXXLlYPs6J4zatLOtHFJ4KjKdDvK24hilq4Sk6q2iKXxTHriPItMI+9GRhhziDhTbrGyEvtBZASQLIhgsmIocJWnXY1jeZaWsQT541gzEEXi+SLr6wHQmLjCZCw9jh4rxv3Nk129Jk7X5XJ0TmaEEwcaxXioXO9BswGXNcYt4yUSRwMxOoppazV0pjYtGRLbuuI2DpZGrtxywwbWdNeqk4twuu0kvHZi3Th4yXpl58qIFSgkHfZ+ItVGZKP4ailbYlk3pi/P42TUBIaIRx3tnVpgziKum7oi55apsDIHXVj7qqkOknkX00t2V3TgrS7cpck2pKKo0Mkq1X1SPuvofs2yreSB0s61HUqJt05CC1dhbR2lDxByPdDdsQEFHibiJhJqgySC0t+U823aGYWyW1QRXRI4nYx5F2irNqdW59OBwflQXmTX+hKlXBPsmVHBt1EQc1gz6OMFSg5RnR5PsBAoK2TRUAgbO9paSwRv3/QxbPfr5QpTb02z2EUknMRMbBv+Uk5PwnZJL4RWHIJND+H1pirGOvPCht2Euro7OUAyPc4lj1OVhVyp67EW6wUacuGGXVmmf7gmKY2xnskqiIgixDLWrih5puwNVjgsX7cRUa604z5rqmQ8H6WNRkXxOt/shsR0kxE/MAmxpFMpvYUH2EeykbTdq7TGuKZYigivLMRlGIiuelaYBZlKObRhTtatsDzuTHK8kg8ErqfxmCPsGV7sluxBP4mg30ypFqFsZXvI9H0kJvmw5MuEglJzLpsSS9ubfaZ69MqWdfOGVTWz27EJLmxDVFgotUNgm15vVRi+Dp2hCuga8budJWb4NWKVpllTLtg+yJDFcwBVfUUQLBsL167bBpAfVKcOd3YuLjYqCM0+Q+dORtOFr12L8GAtb/4KPfTNDka5wVoW5EIs2y1/23U3YS3p2tYFcXkOGwP0mn47Xk1MFbeRXvMQO/hbz9MIluQLT4Hn56i+9mGNtfLpihxICBQ32mAG7ygTfkVoOVLCHRxRgHsJGXStxqlTI1Klr2c9uiiKsqSEeXGxLQgauobuDpeYr10BtD4Lv/D9zuHsSL1FcoALfdkwYVd6ZxQSIKi9qBDoXtNcKmgLhkBrTAQBQuPqxaSQThZI54jSmlLUbYf58yXGZ/votlzit+tmyeMepsPloOwiRGnZ0+HCLs/n7rpaq5qFMVnpI8c9oMpRwOUbhZE8epRI/3bp1USrDCN1CwMJlvGKXJlsPNew0BrTIliDxMyv/lViXVmCy1viyRaNn9qlwUI9gWEEpLdXVfCMudja7RBarBAGfocY446ao/y+2i71DXRp7QD2T+iARoyc8glcaNZ6v4BJvAy3+0Y5VuEJtK0o3Aj1XpAKCUdXC+bUsiIpq9ncWyVI4aiXfJNdqx6aq95JIg6O58rmaRGenQDNB2e+FwzywlBDN58LvB5aqCed4CTfgP21fOyKyNtSToa113rdb0SeZPf9EI/bIUh48gDXo9bKdMdcVRTxk6SrpdU8PFpJ6fW2oio2UIQVGLCVj1buYOp+7MibS3C6Zm4mFtztjGYSblAbyVl5cA1HsIH4vK8s1nYfUeuF3oOyvoaNo3RIFowq4/15pRtqANgv1uQT14IWKsxJ1jCsMueOWF+ES9kbbuHR27j9qVUUcrfYxE0uXnAyOdolNprsSGh+TkV+XEWb0sZ86yKp4zbyjL7fkMSuKWpy34F2KGaLjbJlbB4WqNDBvKWtXX0o2LS3xTaSwC7KQqyrIPMUNW9Jd81itrvqygXk59rCL0n74uW1Q7NQ56YmX3qwuvLUQ85B5x1WYdfmui4VSbdo9RB0nW6vdVD5tiTnCytNXqWUoM75sh8dIsl8+NLli2p+ja2Ycbb+xZNW2K1xoQSa4y2BknFvmWFoNc6N36xgn/KhTqPKVWCrrMuSWEQU8BDNKdeFRd0NzuaZo7f9qmiFJjiHLiXAkIGu5U18WcDxrsO36M3TvDKnNsiw3ClsdT0dTZQlcXeA27NT+QN/dnaWR+OJu0KRhRtHzjHqjtagU9DikG/4na0R5miF+2A9QHkGGuILd6H5gjkN+YWrucQNSU0mVPfYLG+M3LHzZS5WW6JKSdXdg+66IsxbYPkuCjaXlO+TUHATTzWyXemCj6i5Rx8Hkl1dMZ9cHPU55oYYGVAew3TexhpJZHmwYdvf17C09IrdUV7EBX3ZpKDUNwvSEGlUIlrzcqqptlM9rA52cSC5LoOS82K5jVq3t6JLVCLCQjoKaGn1Nxbtdwv2tqXPEkJfZeYokKvr2efTxMjGE8xQHF9X8MhpBWnJpLBYKt1ww4SayVax010Oq/Vht/NZZk2GOsLDySbz9ycOzQtKtQ8rfqTLVSsTKd4eyab3lPhG8whZHPRuJTEM8/LpZToKfh7o/isPYacDtv9n53yPI7m3pzn3I9fA8b/c1/ryL2nzy6eXxkuALo8TzDbro+eh3/86v/z8F+f/08Tx8TRzetQ0dG8H3Z0TTb+9eUkKv2+7ZvzWlll/Pzz99OL27fRrgHb6wYgH3l/upuTVdD78WAt8cLz7ge23rvzmJ21VtsHL9Kx+enwS+InTvV1Gz6PcTy/+CJyReO03lMC/BU01Wfh8njAdg04PFF5+/x8EAIwOzSQAAA== -->
