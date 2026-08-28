---
name: "rar-cowork-cookbook-bulk-update-define-business-continuity-objectives"
description: "Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_business_continuity_objectives", "rar_sha256": "37d350d552bcac20a45b4ca69a5b89111bf540641d47fd6e6944136a89f38a04", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_business_continuity_objectives`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_business_continuity_objectives_agent.py` and in the RCI capsule.

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

Define business continuity objectives Bulk Field Update — Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 37d350d552bcac20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_business_continuity_objectives_agent.py` first:

```bash
python3 bulk_update_define_business_continuity_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_business_continuity_objectives_agent.py   # or on stdin
python3 bulk_update_define_business_continuity_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business continuity objectives Bulk Field Update — Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_business_continuity_objectives',
    "version": '2.0.1',
    "display_name": 'Define business continuity objectives Bulk Field Update',
    "description": 'Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-business-continuity-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c3aa56f9b3e5c04',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-business-continuity-objectives'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-business-continuity-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineBusinessContinuityObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBusinessContinuityObjectives'
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
    print(BulkUpdateDefineBusinessContinuityObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166Zei2Jbvv0JHf6isNjJkFMy77loPERVUUEBEKmtlMRzmedbq+t/7oEZkVde93V2v34dnZmQInLPnvX97H/LXF6ttgrx6+fKiAitD1laShAGoECtzES7v8yqGv/LYhj+Ik2dNFdptk1f1y+uLC2qnCosmzDO4nS2KJAQ1YiF2m8SIF4LERdrCtRqAWE6V1zXiAi/MAHxew1/weqQXZm3YXJHcjoDThB0kUAEnr9wa8ao8hWIgYVa0DZKEdfOK9GETIG51/Vy1GVJUoAtBj9jAyysAqaVp2LxBwcBgpUUC6pcvP/38+hLC7y9ffn1xEquGt14WULzTXa7lXZ7FUxzuQxr5QxhILLEyH+4qrtBMGbwuQAXZpfAWVAd5Xn2qQeK9Iv/2b3FvVX7945evGfL8fH0Z/yhQ3iYASJNbdQNcxLEKyw4TyOwNYZPeuo56N22VjQasoZUz/+2x8zulvED+Pj779GDy5oPm09eXHIpgjT74+vIjkleQH7QN/P42Uik+/fiW5D2oPv34nU7d3vUbiUGp3749r59k4cLvS0PvzvXvkOrD2zb4+vI75cbPQ+5RT7jz5S3Kw+zTg3BR5R3IrMwBn378Z2SdADjx6Nz/Ed2fHoQDYLlQp6fgP77ejfwzMnkq9EHzn7MtoFv/iiZw+Tu7V+RpqH9G+27//0Q6GUPsw+L/kNw/2jD5O/LTP9Xtv9rwinhfX5YggUFcWXYCviC/flMPPPfTD+73mz/8/Bsk/d+SUfO2cu4UvqVWFnqgbr59++mH+n77h59/+qEtYKwBK/3WVsk/ovmP7Hrn8wcLPld9+uNeyP+UxVneZ8hHpCO/5sW/VL+9IbqVhO73+/UX5Pf5Mn4myKjEO9OHCX6XMzWU9Xd2/PHlN1gvMqhN69wfwyz/139F9uFYv3KvQVQnh7UIOrgJUzAKrwVhjcC/Y27DcgSqOoSGfa6D8X8vJFDi3EN++T/OvZ5+dp71dDoWym+PEvntURu/vdfGb99r47fvtfGXN0SDjPIq9MPMShCFPRy+ZpYPsmYUAhbEGlQdLC/2tQGfYWH6PH6BFRT55S/z+nYn+1Zcf7ljQfioXwonjLWrbhPwNup/DkD21NaBtRoMwGkhxyR3oHheCIvwK7RLnScdrH2jreo4TBLEDWGVhzByvdOG9vwyEvvll19sqw6+Zo9iSyAPfKmncMGHOMjnz1BPLwn9oPmaASfIkR9+/e0H5N+R/2rXnfjI4wBB4OktKKGoyhICs69N4TLoSOh6WFru3vr1t6e1IZkMAiL0beiNADduhtEbA/fd9OqG/YxTs3cggoCTV9CgPgLhCBE85ENeyHR8NNb4IK8bCIgFyFyQOVdI1YLqfFgyyxukhiFae9dXpK3BnesvdmXdRUxhGbCaX5A9d4CIkifwn1HM+yK4Oc9CaP6PwHjch0SqH2pk8U7iDZHGeEUKq7KKoLKePDzr4ReIJO/bIXELyUD/NRuhFIymuifPwzxwEbSM83Tp59HndyiGjq3fed/XWCPuaXf8q75m9TMxrArcER+KckX8NnRHuPjbM6TqIG9hFzHaD0o6Unp6wX165R6Dy/9RWzHCPrK6dyUP9Ee+tjiKkcj/L43LqAq7Xiv8mtX4JcJLmnJ5mHhkN7ri0aqNXOG+Rzp97yPeq9B7Mf6aJSGMl+r6t8fKu2Oeax4Frq2gHRVWudOHUQFNPNK9B+0YhFV1N8vX7L3qv0Ib3Usc9BvMcJgBY+C9MxyfvksawDQer793AE/rjPkOAxMpWjuBQeMB4NqWE0OpqjHxni6BEQzGJOyD0An+oBUCqcNAgfQRKEQIUwkiw910Ug7VhDl3t/7H8nB0C5TCbR0oLWxswRtyhrkzxk8NHQCbo3ENtMIPd1JICqCNoYgfFq4Dq3gIM/bCTwGt0Rd5OobI7zzwfPg92u+yjOJDqhYMKGjLfizHLhgenv2Q8+krKGw65ud90x/d/dQV+T08/e1rdpfxAwFg2icjsv/OOAhMt7S+19mxatWw8qTgGUAwEu4g/vbA4QfQf8jy5U8DwKe/NiPckfX0R899QYKmKeov0+kDDd/B8A1mwRTGSFiA+g6Mnx8p+PmRe5/fc+/z99z7/D33/sDoYbcvyF8T9g8knlH+BcHe0Dd0fLQLHTCG8fMDbcN9Xlw+k+PTr5kCvjv9GRljCU6uEIk/8Oh9CQQlvwL+uPiBT/UIaz1E0ntBhm75mn0ExjNtYL3P/BFM6/x36XwHZujmhxc/cAM+yhrI2x0bPR+MI1Eyil+Dly9ZmySvL5mVgr8+Co1QASMZ2macp2BWwTaqCcH96qOlGi/+OBne8w0WCjf/MqbdKzK2v6/IRyf7irzPFvfhLWvhcPXT2EWPLOFS+Otj7cfYaYMXONs112LU4zEwjc3bs6n+sxBjtkGJnbF8j4D2TN+R45+IwC++D6o/E5HvX6zkWUPqxhrBPGzeM7+GcrqwNXpFoCdhRsIkg7WzhRv+zAbyqUDZQtR0R3W/2++7Wo/4HiWCZmgeU+evL++15OmDZ4cJl8Ok/VyPuDmFUQsZwutHfMFn//ve80kQlkPY6kCKBO0SFOpSFG47loOjFknZpGPN5hZlM3MMw2yPItEZibkk7bkzMJuTJEbMLGbuEYyFkpDeI2y/PfAPkgSoB4g5hjsuMcMpipxjNG7NXYukLctFGYZGISWIGN+3xrCWPjV/aDqa9aMNHi30NMCvL/aMhCs3ZC2wjw83neuWfZ7aSrCbVMlkGIjZkTgVp0khAu0We7MokHcxpy0yc6YAfksLhaPqjWaI5u7c8Oaiy6OJ39HqZGbi4Lzb7nXJiSJ/XYXYTcTdzCQMk7xs/XTZKxyGFrXK1F2QVJdA0tuyRlv9nB6ywzaksciGBcbUQThzreKSkbt4HpeO1nVTMtW6PYPpoY4LNLaw5oadEOvguKYpkbisrjmunHerPFpUgiYHNd2XilU0siLYhkXxp/S2Ucyz2K1Y4pwSvMFh+9xZNJ1rJvIidA5ZgzseXc8PBsUTmwnTGavlbEV2usik+2IrWM3VPOYznm741t0ejxPzWiXSLKjmW34FqN2xTjBSOt36xrQXDNXnuqyfUM4P87ZEhYRsd6jfJDtj2/hNsVgeuOmi5YKLSMrY7aBwqHKO29V6hakXrbykXW3X6M1Yo+e6peLMXHkTsGr1tXlb7xLpKLsiu2eqiVVEtc6V52NL4p2wYEkxvQo3dCea4R7bDrPWnfRBv6ts/oyyrAF2hpgftkZQOTusnmWax6f5FUq7L4Oir3QrOHq7iVpclvjOVUHqEwp5KJZmqJ25qpAWORbSpyrVAlEzdlIed0qHtcfTxiK0ayIugBECmVsJVsVpDKSK88vqbO2AzNc4k2XRce9jujzd12kDPPRQu63F4S0esU6dJjMlabKZdY3iPY4XfLItLmdMQG912FZ6aDZQMBYWtTL39YazedGY1wsx3e4ZyThohxTk9HSQ1onv19N+4K1JKsueIlzBdpOd+CaImM2thbmoOedyt9nT2WkIiSCiPXXDeMftAd2lV74vqfrY4vWlvToKlpA3ezuk+Ml15sO2aLfzQcauzIqerxRmHZHCBl8m6wGtmCSaLomcWt+mk4vXr1a+Y5TRGXN7U5KacDvR7UsrLShLdTBVVY0rKjQhHJjDedwTzHaoL8PyqlyXQ4AxYH+sUhXXN85KzqwwmVELLPNW/pzrb4W9uFzj3MlObDEo4nppsusFtjoNeH0KFWmQZ4vdYmmC3l1z5dHfpsCNVing1r0TNRQtNs6uZNZNVm5WzdY2ZWrbazJo+MY4h1hUKBaFB9QkwtS4n/r4ZVqZTIa3VkHwNhYqk0szNPi1zNzN1JjGdVIx5jCNYVZSsw02TYR2Z5je0lwtt120lSohrUCI9xR/kQqTzfNuSCk6IG95R5yLSO4KTUxb92hQurI9i9qenKh+PcspNeAbggJksvLQ8BpYCWpvD4eO6C+lKni3aqj3IDSKJlJpraDXTTItVSW5bqNTGOlsWcbXwzYWuU7fFccmESjDRTk9i07YLTBVc7DZ+HCcTMQSuLetoUNfx70oTcQViYnq5XSYZjP+erKOujZZHPZRmpeMv1Hpxl3b82G1EfDdbo+1yxUpdgVGnm1Y6IIDf/EVxfNp41SCPVXdFGbJxuTWO3KSe1utSacMNt5AEddAPbrktCpzbBu4zlRVtOIauqnYt/zcWKDTQ3Ckjnqsb4ODF5Nglp6jiaJZdUIbXUdtrkd8YHaMs1mR8oLK3NvybGO7ZCXOGpSi3bMwrXmSkaTdhtXrZCuj/SFIiPNqHwlwEDmv6P6g5P7iwFDyIB+8gSWD9X4i+QmNXbqsQg9rIzPmJtn3UpLOMkfwfJc7atzteNqt1vwBtSnrsl7th3USUhop7uKqWwZ4nDR+v7dsGa49YhIr8JZeaMJSEi37IDRHNcgWYKVyO//kyGStmidpq2xOLnnCggGrdvU6Tqu9vjN2DloC8uqmcqJ6N2zfZ67kiRIzPdySOcgCaXdcKpEEZrOpxrXDVj7Z6JBiWe0sM980jEJFSWd6vqpkS1KBO99vgBMYDHDVQzdcGYjE1KQIpjK7o6/B5DRnY9OlqSJVjePB4jZhthccTEv1YqXqx24Vle0pVKczg15r6rl0AdbzlmqFhcf2emDq15MpqTsxmJNaDPZKZpZ52h4ZJRPAiRDx1YXbHvXj5TTPg9WFweeX+W4/o7TpbFiqhJHSlqoBVFAG7Wp3qza/NVFIrUXF0Np1e0tSfLU94VQflSWWaUaU1clNQdOVebhyK38HVnGLY1oiqf0E7aGbJVAHK/V4Da7LpKJgNaxW26yVcl6n3eUVcM7tyN8Uzb8eT3HVerayAzMClzCB3m16X2hNi/MCTxlScrlCp4F0W17ImthaV21FCIqe0pOT5wT7RSw6yy0e0GWF5uKOTXOuUnR8Izj9zXWl6WpXXPJGNI8KmojuHjh6Gqv+iREXQ1kWJUWQuM6Fqnnu2llAp76wiuR+zXCebx4XJqNf47quYOcONtclm5t0IvsG212vlaLEQ1ksj0py26i6trwS1qYzI6eK54LCd+s9e+uzwY/5Vupat6Tiq7s4smU41B7ulhocRJZhq58ONVmcOirHJ2shnaO8Uq7KMzsNGjO7hHwEyLXfry9alnY+ycjTjdeH82VFLNQE8NeD1mbicb/GmGTLHPfA2nYqqvWYShOJku+aQKvJI30xi5j2fIrbbnk2Yae8ey6O9YU7BD4maxRJWedpsBLVhZIvJ5ExTUVN4GnrkF16Z09p6xBiwG5ofKN1K10uKq1Xxb6ZT5mphhHkvj/GWXnMV67vzez5JO+jBJ+0c6VgzsCmN9gMbzV7D2xOrwcnEnSjcumDHbDLnvRYg6Jxh6wW8GHILtLuxC+aqXLeOmBJq7zK43vbSo9kyFFeZs4V83Y+LZyFn1leiR+Xq20q8QmsU7xpH5UyubYlJa/YG/RDLJQXmsgL2c8vklOK6potTzvJmtEayeP5kiNpFE5ye3aWZ6q5U1YCqIf5wPZGFCjysqtOOhvf5O25FXmnR9vjmjQX+bTUgMCZri3tc/+snG3/YDroJthRQ5iKA0/wkbE+rq1ifuR2fUonPKXs/QNY0TM/EPv4aEfHhayIx37KVQM9SU5loJZJUIBWIeKZ6DgmW4BZ7ighATtXStTV6UIUPNQwNhU/TE8Ub/ei0BAK7aYY7AkN+QqKTMTkhJcCsRqm9aRUM9MZiEDJL3tOTpxJoZsXrChZOsbI1rzRcVvsZM3Sj3PbMdbBjFhPXHcozolJc+Y0tlE9Jghhs8X204LfzXZxyTk1aThqQJGnMF8TghsIoSbPtNC/7EQVDkAGj+74zW7hLIs+QSEW0DYchoJCBigGOlXwU1yB/ZsXLrRmnkzZeWpkYkuRYAv1PyYF0A95XAt8bPVWMjBBxjhFHIW9eEY3RcyvT5ydhevKF5lSjMIUV4Uq4/TzfDAvBGBRrDd2QoRKQ9rilJZeLALlq9DZXzTRYTbS3lwu2ZBycrJqTF31w92NIIOKOvuDzCybPDlv6kBYUS6Wbaps7IuXCgiZLcdJpauaXOvL/UavYMvoMy6pRDbGehd+zQKpXwtd3TZ9VpU3JVHTnDcvHmdo+0A1DgelkLp8W0oz/2JbwrbZ9tw0jmXFV72CM9NQlxbDSbIU7ERuZsY0VCJsueSAMnW91exiUYZuXXIp8LvzAvbDdcZu0y1K+vReoJZyTM6VWEVbgrgwxMnZnLYqyq4tltKrmdm7GFbbzQKt/VV6Psi6unRbX4vYK8blM0mNBpvONRPF15F8tcyJEhuWjmmsormqU8j5MJBQXf3IuPV6q8wwyvUMjGMFq5i1N2FisUlyiJoS7zAnOlK0sbFufnap3Mq1l7AvweVNYGv21C29CKO3DGXtYEladBc4Ju50ut3VU1rO3MSxcSmr7MlhP0u4EhqbPZU3LTwbShHLvQ8i71iSrLot3IMc4TcrWWL4EoK0dKh5cTWdqSmXUXMy8vce7YmHUimlPdPSxrbsDHp1uViC5rO9mtI7ZUGTzWDvDxeq0fQ4mssbrDguF3PURXdrjwhPTH6uUWLppibMhhnF6ldhIvcD7rn0jJjNbhuWnKbedNro057NSuNiebjnkaWn5QpdEu3eq7BFgZ/o+EQf50Np8nvidAKLAgU1f9iU6RIO3SQ6zeV26weTpjNXhZLksIEIbjdeVjaXTbKnfJwjqWWdKoxL4zeNo91bm7phIa/Lq3Qr84Pbi8S5SfjBP22cbkckG3lPy6IY2MKZP/fuXMlTxlSxKYZ2UV21JIgzhp8ae+No46IzreplTh/wyWzGdgl1k2o0sk6cerjwhIcGtF0vjUV57c83Sx8A7CGuwhDbdNpJt0V3njaXCa2EwW1dON5Rk3zFK3ym6vx2y9DKfK7wk3NrWLV7WtjBQrroCm5GFj5NcJtSNzrWsPW8g7ONnM+v8+jWQTV6LRZkr3UJ7cJdJrwOdkchsAkhlBR5rh0unUlyhG3MdVcMfCdfryaTkDw1pIodVsycKf0DIW6i9dlxgO76onA7iRHdGAufID231wIIvgw1IaPhWC/sxZYRwqwxxGh+Xi6o+XyVW8EEXWCXLWmymUNbHHkQooi9yTab9IvB7vG+5rxlJTNwTmOIXK5KDI48WUeWsoAVXr3pJglB4/TGTcxQxOdRJYMZDyfBvVnJ7elmdu7B8k+LzbIzzCHYTJV90xAYs261lCLmPk73wul6a1ZSxHDTI7O0nNPc9I7yRKaXha33vDkhCG4Tgf0ZrbGaPAur2xEn7JPU2FIQz7pOba4lVeB0BSrlRC0zNTaKmVzBjrZb+RMSmDjr+93M8s9zNZ13S3biA3aYSlFOW4XvbPrpRFgtcd07O0axIM8yJrfCadrvDFvCt+REmuHEmYk1EQpuuNp8Mqs6nPdBRwdZO+/oUw3QVQ082Hz39NKtJreeFnQLj3SJO2R6ZLbLA9il5txre2NKUea6v03mdioQBBq4K4iLER2GWb/oemwV6VqzYzD0AkdBfTKkkZ8G9YqqFvOtR6J7FmVj6nbCmPPhMCercB3ZsywT8vMmt+xSOU86/VJlC6rmA9eoMY46dCTJykFmkiyLrbk+47B1L+wJp29YSXNtvOnPumvTnaLCxhw7EBfjcGJVksi9emCyZbnOtIHxxIV7Gg6TUJoHlMCh/cLgevKc9ot+Em2XW5mppHx72Zg9fRXZk7dtWkz151cQNqVshAa4LWUhi1Qt3tmDxLjRdUvdZDohd/RSAkQmBqDt58kkLTq3QjcpMV/r4i0qRcar5fJQo1lYt0uDMvqcLbOpqHNe49y6hjKHVvbYS86dZLPEJ8JegWio8nzUwGk+w/O4K3dCyaBeQG9OXifZDLVsu9yG6OEYK/xw8A+xjIMwPpUsy/795fVlPMF+nkP/37+cHo8C/5+dSD4OD9/fWN0PoYHlfrnz+vK/kPHn15fKCaGEj3PZOmn956HlfzqV/fyXX3yM5K6PN8Ljq7eheT/hbyx//P9PL2HmtnVTXb/VedLeD4pfXz7kfh6Iv9zVTovm/uxDTXhluWkII6IB1bcm//Y4ox7vw9oGqhS44fdL/3l8/friXqFbQ6f+Rsyob6AqRv2fL1Sg2vgb+oa9/PYfUIfAFXkmAAA= -->
