---
name: "rar-cowork-cookbook-bulk-update-update-asset-register"
description: "Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_update_asset_register", "rar_sha256": "01ffeb1ebe988c29053d103f11546927f8bf673a6e88b8004b790b2d5a194693", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_update_asset_register`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_update_asset_register_agent.py` and in the RCI capsule.

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

Update asset register Bulk Field Update — Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_update_asset_register_agent.py` and embedded as the fenced Python below (sha256 01ffeb1ebe988c29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_update_asset_register_agent.py` first:

```bash
python3 bulk_update_update_asset_register_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_update_asset_register_agent.py   # or on stdin
python3 bulk_update_update_asset_register_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update asset register Bulk Field Update — Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_update_asset_register',
    "version": '2.0.1',
    "display_name": 'Update asset register Bulk Field Update',
    "description": 'Applies a bulk field update across update asset register records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-update-asset-register',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-update-asset-register',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31a68c652a5292d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-asset-register'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-update-asset-register', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateUpdateAssetRegister(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateUpdateAssetRegister'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(BulkUpdateUpdateAssetRegister().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaebOq1pb/KvTpP5I05x4BGe+rV9WA4IAMIiiSm7phBhllUkjnu/dGPecmnbx+L1Vd1d5BkbXXvH5r7Y2/vDhdG5f1y+eXfeAU0NLJsiQOasgpfIgvr2WdgrcydcE/yCuLtk7cri3r5uX1xQ8ar06qNikLsJytqiwJGsiB3C5LoTAJMh/qKt9pA8jx6rJpPq6aJmihOoiSpgWS6sAra7+BwrrMgVgoKaquhTJw8xW6Jm0M+fXwqe4KqKqDPgmukBuEZR0AbfI8ad+AIsHNyassaF4+//jT60sCPr98/uXFy4AgoBgH1DHvkh//s5N4/SkdrM6cIgJk1QD8UIDrKqgB/xx85Qch9Lz6vgmy8BX6j/9Ir04dNT98/lJAz9eXl+mPDhRs4wBqSwfw9SHPqRw3yZJ2eIPY7OoMDTC07epi8lAD3FhEb4+V3ziVFfT36d73DyFvUdB+/+WlBCo4k5O/vPwAlTWQB5wBPr9NXKrvf3jLymtQf//DNz5N554Dr52YAa3fvj6vn2wB4TfSJLxL/Tvg+ginG3x5+Y1x0+uh92QnWPnydi6T4vsH46ou+6BwCi/4/od/xNaLAy+dovkv8f3xwTgOHB/Y9FT8h9e7k3+C4KdBHzz/sdgKhPWvWALI38W9Qk9H/SPed///D9ZZUoDkf/f4n7L7swXw36Ef/6Ft/9uCVyj88rIIsqQH2eFmwWfol697TeB//M7/9uV3P/0KWP9TNvuyq707h6+5UyRh0LRfv/74XXP/+ruffvyuq0CuBU7+tauzP+P5Z369y/mdB59U3/9+LZBvFmlRXgvoI9OhX8rq3+pf36CDkyX+t++bz9Bv62V6wdBkxLvQhwt+UzMN0PU3fvzh5VcAEAWwpvPut0GV//u/Q3IyAVQZttDeKwH4gAC3SR5Myhtx0kDg71TbAH+CukmAY590IP+nCE8alyH08396d8D85D0BczYh4dcH6r2/3cHv6zv4/fwGGYBxWSdRUjgZpLOa9qVwoqBoJ6EA8Zqg7gGcuEMbfAJA9Gn6ACAS+vmf8v56Z/NWDT/fwTx54JPOrydsaroseJvsO8ZB8bTGA+Ab3AKvAxKy0gPqhAlA1Vdgd1NmPcC2yRdNmmQZ5CcAtkEfGO68gb8+T8x+/vln12niL8UDTOfQo0E0M0DwoQ706ROwK8ySKG6/FIEXl9B3v/z6HfRf0P+26s58kqEBK5/RABpu9qoCgerqckAGAgVCC6DjHo1ffn16F7ApQJ8BsUvCqUNNi0F2poH/7ur9iv2EEeR7ZwEdpKxbgNAQ6C/QOoQ+9AVCp1sThsdl00J+UAWFHxTeALg6wJwPTxZlCzUgBZtweIW6JrhL/dmtnbuKOShzp/0ZknkNdIwyA/9Nat6JwOKySID7PxLh8T1gUn/XQNw7izdImfIRqpzaqeLaecoInUdcQKd4Xw6YO1ARXL8UU28MJlfdi+PhHkAEPOM9Q/ppivm9t4LANu+y7zTO1NeMe3+rvxTNM/GdOri3cKDKAEVd4k/t4G/PlGrisgNjwOQ/oOnE6RkF/xmVew6afzoXTH0bEu9jxJPgS4chKA79f00ak6rscqkLS9YQFpCgGPrp4cJpMJpc/ZilQM+HwLpHuXybA95R5B1MvxRZAvKhHv72oLw7/knzAKiuBn7SWf3OH0QdmDDxvSfllGR1fXfDl+IdtV+BT+4QBeICKhhk+JRY7wKnu++axqBMp+tvHfzpnameQeJBVedmICnCIPBdx0uBVvVUWM8QgAwNpiK7xokX/84qCHAHiQD4Q0CJBJQKQPa765QSmAlq6u79D/JkmouAFn7nAW3B5Bm8QUdQG1N+NCAAYLiZaIAXvruzgvIA+Bio+OHhJnaqhzLTsPpU0JliUeZTEvwmAs+b37L5rsukPuDqgJQBvrxO8OoHt0dkP/R8xgoom0/1d1/0+3A/bYV+217+9qW46/iB6KCss6kz/8Y5EEjNvLnj6IRKDUCWPHgmEMiEexN+e/TRR6P+0OXzHyb07//aEH/vjObvI/cZitu2aj7PZo9u9t7M3kAVzECOJFXQ3Bvbp0eRvb/da+3Te639jvHDT5+hv6bc71g8s/ozhL4hb8h0a5t4wZS2zxfwBf+JO33Cp7tfCjDffwT5mQkTpGYD6KQf/eWdBDSZCCg+ET/6TTO1qSvojHeABWH4UnwkwrNMAH4X0dQcm/I35XtvtCCsj6h99AFwq2iBbH8azKJg2rNkk/pN8PK56LLs9aVw8uBf2KtMWA9SFThj2uGAsgFzTpsE96uPmWe6+P3e7F5QAAn88vNUV6/QNJ++Qh+j5iv0Pvzft1NFB3Y/P05j7iQSkIK3D9qPjZ8bvIDdVjtUk+KPHc00XT2n3j8qMZUT0NgLpv5dftTnJPEPTMCHKAIW/4GJev/gZE+QaFpn6sZJ+17aDdDTB7PNKwRCB0oOVBEAxw4s+KMYIKcOLh1oe/5k7jf/fTOrfNjy690N7WNb+MvLO1g8Y/AcAQE5qMpPzdT4ZiBNgUBw/UgocO+vD4dPBgDfwGwCOCBoGAYuGrgBQ9MexiDE3EeReYiiBE4yGBXSbkhSc4cMaNqlEQR3KQZxMZ9wUAYQzAG/R15+fTQ0wDJAwmDOoJjnz0mMIHAGpTCH8R2cchwfoWkKoUIftIBvS1MAjk9LH5ZNbvyYUyePPA3+5cUlcUC5wps1+3jxM+bgkBju3m4WPJLByS2I3b5INsXeLkn3sq7lpIv86GZLPldyC6A7Equ+ONiUOkpEeeDUXUyXOpEWVDGqw6FVh1Ral6c2sbpxcyW8gQphD2+igT2FdlM0mc4fL61kOgnaXszLbSNfet3WWrM08H1Iw73c48momSTWpLyU0PpRO6AEa3FxnSMM452OkmGLp2Zfy4cmlkl+6PeVmHj8BuvaYV0psZYMpRE4Ytcql81eQuXS1Js2a/0xdc4NFmrbBA4KFyNgofL61W2EQ1TulWLnic6l5vaDdA5yRD0Ep41ZKsxFOqqnAUlS5kp6+5Tsvaw87jF0eSmR9RFG/A5PL8WlInn+cPAO5UG6qZa9OXWWWmrwhrPJRPUyjvNEDOORzM4Cybjw4iK4NEqVrs/WTTk4VtXmqp43jMJsOnKlBDnXHYb97Tg/S9e9seXpoZJ8cL1PjvpZgmNh2KWuVsu2cDllftz627EqTJ/1aqHAdmuJ5NYzP85kpt1GoVI4mDvY54185PumOOyujEJWO3m28vVmYx2Odsy0RuOwpKphNne6tBGGGeZSsTtbxRHZM9HL4G5mub11O+ZUmO6Rb9wFTe+q3aFaFMJeGBRBPTT0nvFtomlXmnr1JTcXSYJw4GCGbBr/QvCYMz8jTpOjg5H5BeXsy7O6ddBEYD03Qexl0aYoajej6BLBelUYB0vgs5OBn60ZliSDoAbL87zqxtVRCOFt2prrtUbLx2VvnxNPrgiN4/WR255MOqaZDq5vdmISDmF5YyHvYXnmljZeYGqi8ERTKFLjZNtqVq5s5oiMl0tnLYMkDuP2UpgZzMZBwgajgQXhqdPr1b6TTI1e+eck1PoMhnNPPifEgUTrPhQQbI635Ra7eeR2QOh5JUmKX5PCYOxmzq4IDhS3kJbNPrdDZo/PSX/Rb1b2sU03M2W7Mc+lGvgywSOUKmeylJDL5qY4m7iO0IKLWDS146PqF8t1vcILW4ivcdMLYsTtGl1cbLWKHNUV76mbHKdTtBORcGmN55WBnbXm7PNEGVLcPIprFx8YbsmshH69y4rbTkNgZDyoxAJufC3m5jlsSbl/3M4KOvYc4Kcx3BNbX7S2GJwtuy168M8ngRXnMLNwGEkyzkGQrETz6PFdu1+yUmNrQWmH7byo9Li1EAHsLOJOcLLEkUWhuu1YBtWLrEMuSIEcQxSPlz2iDvENgKKsaX0f0QfBhK2iBgV+C3Nso+lw1zi6MbvYa8HFlpWowyElbrJA3GiSomvZnjQXhwO2G3xPiShZDNkugQUsiAl6rwv4mTQOjdltr8KM2W9vF7JR5JncWOdxoQ/r82DNWNS8aGseOwMzx6DFaby12dJqo2NTcZv+uLFaLd+uHNuwhQO98MV9hRD5YZkKosKOUriTOD/KFrDnZ6twQ7BSPBwROkQV02kltQvz2KiGOIhSVKtulk2forCk5Hp9MTctvihbVGwtlM9Ruz72fmAvMBLuMTc8c8OKsEJ2Ry5xlUyz7eKkdr0prW5psdTLkyzo1gCmzznbqUfGG682eTmLglVvg4XZcuFmCJMhDHls5Hkdc2NJy2+hPJcHe+lbq5w94+jRrcK1QrAFzppits8wfrOZlXPHFH1KTJQtd5Xxzdo8n+qdumsbk3Tsq8pUOn11rylyMkt7x9mNmc9v6sw7nKxFTEeVubjaaX6h1td9b+B1vwi7YEkra1DLVi2zzdZa1bOMGMl+lBaWXsg4OZvVBOxZW/TmpUI/bo5rbKQKODxsNvpQe7nMNAveDJIkwpkaDrWw3gE+nXqa9dcdtxqwnUbcDrNkOxIzacHMYCVYDUcPNrUhKQXRs/ocIzYsqzZLNZPdHXHJ5Hov7VCpO5wvjYlvT7iu6GZZG0dW9/kLfsB5W5LSI3pIM2WBFGOzvgnsuRsNgBrcfChYH6kjEub9dIE3Z75oc/6yuM0OleOc0DqhKYHM+X6pBXMN9uBEoDSCFPfzU66bzOk6I/HFdXb2U4cYx8zGzrVpL/FuuCLKyl+lLMmyUTLItsOgeStt3Ma7zZYqdhrw4BQNC3017hIquIFEVJxMCeYnPJMxFpPoq1+ey1RaIBk6xHvYorZzZC5Eu1hz0WidtBa14a/xCR6TtWo7y8MF76k13RF83USUdSbOVXTdH06c7gbksJH25nqlRbEkcvGA5fJypZozx5dEq+HjqIgqh2jM00FdbPa7YX25OZ14WWlUxy+4PRF0Z3k8pgM9dldR4FeRTYkyI0qXppkXMZGs+EVTabW4NQYfeBkrY8I4hjlemMCUNO8ja9wGSndCt84uWffNaWndtKN3XFLuLrWlrBmtjRKZKgMq7FDu7BxA9XmXblsKL9v+lMDFnkdQY3RKs1nB5wuq6qo8+s4CfM2CStNHTQ5wdbxxZE50iSjMSkRPmeU+Fw4ZKYlYtDVxa0k7KReLuMkdSinrdh6yJ06KlhiXjbneXZGluD4Vh4tZq2yMhso2Yo4plc2oXcYVCssHxQoPFgufnblVLyJeJBpYyqoFR2CYp2KpDzpNSwTpNYA7PLQxhq7p2Sl1+FlMRWfDoXouFrx+b8+RLjuXI3YMi6xNexRRMK+PU7K4tj1WKsLBWe30NczZW9DwWXPF8jczchVe8Rimyaz1gHF0IhvLY+m7it6t6sMtLFCZlO3dan8oFZCanFGfJctjODxy94JiXg7IXETLjsN9bMlnaiVs4Qj2Q3uoDttLL3SWk11nBb5Gr0t2PccxGnG4UOEUVUeuxTr1vXS22/DoQFx28TAKjJK5PCtjpe8lu7N1oqOVvlV6Mp8PQm5hzL5PaUra7rlZnZyZ2JBlY/AOPrMebrujaFyK3uLklWRjsc3awba4tfkCeL/bSAIs5Dwu6qYpjhdhWK3Jzk/9RCZN17+BpkmVm9RDTqcwwmDNWS2MNjdn1TVRBtYKxgslc2KsId0QVPMNKmaC0leXzayBi11x8dDjfAnvYEcN2QPmKCcyM/Crs4Rpcd1ZZcRTGdp6yhE50Zdtl+Hnra2qGbpGjRWvzjIDcfW+k3Lz4tIrtoisjS4MIl6csuXmum75ej3nd2uB6pe2qaLCCTPj+Ibvr9fU68QGFyhOrZGyPnb4SNU3h/VLJDCdS29SWizYy2Q+i6VgOzaF5zdnI0J9o+IPPm6CYSXf3chyA7PFThNwDj/y65YbZU7Le0OmCHTDrUVO9k3M0cWGBu7Na20/u4p5tScOkTnSuu3HLJkfs4S7IqGSK5KlbRkQoyhiU/tA27fWQfd4mtPMtSXqncH16czaZCGxSPdkLQ0jynrWXCQuMcdmHHEcE/ai195C54SBwt3moMmnkb5kWk0yrI0sisPVJ6x9OF47BC33a1Gmt+clkR/l2dKh0NyJXQq+uH7pDNiQJGMjnInN+eII/dDKo112OGf40XhJriJShXu9QHmD13XY1/habr3qki6lFX7iUXZQxFVKcFlsnRWyZWUAOUaKYW1hONf51RAPg49EHM4eqhNxaPYFN/cDDOYqsdHXQigo+4Wvzs+3RHcS67CsNri7OHANZce7G6YY2kUwqCCqBnJJEHONKW7stdcMgXbABntLipyg6LwlHkNFO177Bq26mcjt7fFW+Gc9ahGA6vNE2xJWN1uVlmFRbRbq5LVD9V5KtXHAxaANsGyOckS4yFxk23grfmzj6+qoZtdYbCiwg1k6wX7fB4u4RVyDJYqrslpn/tbHmQErFyh2PuxHxcr9tW7qqR2JesgLJD+DXZKj13kZETR3OLoW4/pcKF+5lcAlJnbbXEuZZDaBuDOzJlskBjO/VGBvqFLr0cVaLNrMiR0qxjjZUNpQR/M13yqakQfMehXc0OvsiBBiQVIzmD5rcFSQ2XFZMLdxJswRQgpIhloUJANmuUwlMwXVTs5x7efk3rh6zGrLrcbZnoJxtGxnO9TTuasWhIlmJDnLGef2ds0DUOOSXsFGsF4kfmrMxpTRArlGB+nmrbaRuzukVq6nwC8j1oA9hX2VVp0lUuO5kOSe3J+Wg5gdmlVorvU+37fh4sSRwcGfc3QRRvASvpBccJMSphe0CMAVVadbeN7pftbYO9ZxyaUyp+Sgoxb6VcaOPLHcXLbVGYW3XBmuDheVaX27Csn5rFitcjn36guwksvX66K/Mts+8pcRpVDMedNIXd8G6nLdnVilk2RKu7VhONAtX7oZ1bJABXSRqzmTzs5MnwnY1TDXfNgxx+2JT2HhENS7dewW68TXeTrrT+eM5OZbizn4G3bn5Z42MAoqzznJpQswemkyuWfDpUzIOO2swH473G1iAlmUg0HLTWvj2XwVeDt1TZu1aF2TNlmKMwuP4dowbjRcyGhOxcGFJcQ8bfs23aZ0ovJredMtdicJgI7G2ZEM/KTsTiFGgb2y1Q5CSIdqH9XqiUpCPHaz2h07uLtttp7eUiod+OJKHiP4OCwJQ8kJc0FlmsBLNHyesb22cVa4UV8weA9yj/I2e1JQeW8eXQu4jplzdVXOC32O4x7YWa/YQ7H1enyWwidGxOstQkUgpU5KtsHGaM6PF8YXZxl6Ntr+QIVJdAOA1DTxRa2tCzuPkJDvWSfCNxJcIIu+YhpjfV2XK8ybLSvMV4SNaiAhaNX6whyxQrzlgU41vhsLGq/OsVHfqWHNNzO0miH7se7PKumjcwbLcBlvZEZDryS6GKJ2XNFieeq7WR0G8JISj5XTzneLQWJO88XcWmNEDxe4NmvAkCMPS7omOWwetaHf8gMbEzqR8I7MGSf0QJmwMwvmAnKJcL0kxZq6lH0MM1v6FMTOnj+J0h7eFhRNmyKnb5jjfB55HXyl93N/cCnU3m7DXQh6LHVA2mu3X2nSYlHqSLhba2BY3thO4Qq50XhYtay6ljoSW6lrmXlTBUiAztBTxTpCdbQRDdvBBjFnFxEZrmLLQtfGfDB6dcWyW4sXaOsYSaO2UhKpokuFkJ3IRkDXkOWevzUZ5jJSkvqUdCyxgIhhtYkuM6ej8SO8bayS5S3CRfZzLojFVGm8LiWtmOLn2gbmqS19vszpeCPH6tK1lo64FahVgnb6TEr5cpZkRuEaGnWUWNVHB3yRseqYndre4YVEUdCBBYO7ga61ZLu45KOs6SoOM1ah3Ga7uUxeGJXAAue2J0cDsWg2PA54eWgqlmX//vL6Mh0/Pw+R//Unw9Ox3v/Z6eLjIPD9cdL9ADlw/M93WZ//gk4/vb7UXgI0epyhNlkXPQ8c/8cJ6qd/+hRiWj48HrdOz71u7ftxe+tE06+FXpLC75q2Hr42ZdbdD3Ffgfua6acLzdfnYfXL3ay8au/3PsyYeAd1n3jB17b8+vzRxcv064LpeU7gJw+a6TJ6niu/vvgDiFHiNV/nJPE1qKvJ2OejDWAj9oa8oS+//jdTT9v0lCUAAA== -->
