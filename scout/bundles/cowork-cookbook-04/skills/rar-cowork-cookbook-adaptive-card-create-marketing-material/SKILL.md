---
name: "rar-cowork-cookbook-adaptive-card-create-marketing-material"
description: "Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_marketing_material", "rar_sha256": "e32199e231c02cecae17031321249b03eaae7badbadb006cb1775ff9a9dd7b28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_create_marketing_material`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_create_marketing_material_agent.py` and in the RCI capsule.

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

Create marketing material Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 e32199e231c02cec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_marketing_material_agent.py` first:

```bash
python3 adaptive_card_create_marketing_material_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_marketing_material_agent.py   # or on stdin
python3 adaptive_card_create_marketing_material_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create marketing material Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_marketing_material',
    "version": '2.0.0',
    "display_name": 'Create marketing material Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of create marketing material status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-create-marketing-material',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '83092695e8192eea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-create-marketing-material', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardCreateMarketingMaterial(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateMarketingMaterial'
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
    print(AdaptiveCardCreateMarketingMaterial().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6e7OiyLbnV3H2/aOqL1VbeQhYJ07EACqKCggKQldHNY/k/ZKHPHr6u0+i7l1dt0/fOT0xEWO5SyEz13v91srE316spg7y8uXLiwqsbMJbSRIGoJxYmTvh8jYvY/iRxzb8mzh5Vpeh3dR5Wb18enFB5ZRhUYd5BpfLZe42Dqgm1qQETWXZCZgwrgWHb2DCWaU7EVRJnFSZVVRBXk9yb+KUwKrBJLXKGNRh5sNvNShDK5lUtVU31cTLywlIbeC642iYTVyrCuwcEqs+wQErTOAnnHMCVlq9QpFAZ6VFAqqXLz//8uklhN9fvvz24iRWBW+9vIkzSsPdeR/eWB+enCGNxMp8OLnooV0yeF2AEsqRwlsu8CbPq48VSLxPk//8z7i1Sr/66cvXbPJ8fX0Z/ylNNqkDMKlzq6qBO3GswrLDJKz71wmTtFZfQTPVTZmNBqugWTP/9bHyO6W8mPxzHPv4YPLqg/rj15ccimCNRv/68tOo/NeXshm/v45Uio8/vSZ5C8qPP32nUzV2BJx6JAalfv32vH6ShRO/Tw29O9d/QqoP99rg68sflBtfD7lHPeHKl9coD7OPD8JFmd9AZmUO+PjTX5F1AuDESVjV/xbdnx+EA2C5UKen4D99uhv5lwnyVOid5l+zLaBb/44mcPobu0+Tp6H+ivbd/v+FdBJmMBfeLP4vyf2rBcg/Jz//pW7/3YJPE+/ryxIkMLzLMfe+TH77psor7ucP7vebH375HZL+P5JR86Z07hS+pVYWeqCqv337+UN1v/3hl58/NAWMNZhz35oy+Vc0/5Vd73x+sOBz1scf10L+5yzO8jabvEf65Le8+B/l768TzUpC9/v96svkj/kyvpDJqMQb04cJ/pAzFZT1D3b86eV3CBMZ1KZx7sMwy//jPyaH0CnzKvfqierkTT2BDq7DFIzCn4KwmsD3mNslgHatwhHpHvNg/I8eHiWG8Pbr/3TuAPrZeQLo1HoC0DcHItC3B/x9e4e/b2/w9+vr5ATJ52XohxlEQ4WR5a+Z5YOsHlkXJahAeYOgYvc1+Azh6PP4ZcTHX/9NDt/uxF6L/tc70IcPrFK47YhTVZOA11FXPQDZUzMH1gbQAaeBfJLcgUJ5IcTZT9AGVZ5AhK9Hu1RxmCQTNyyhEfKyv9OGtvsyEvv1119tiN5fswew4pNH8aimcMK7OJPPn6F2XhL6Qf01A06QTz789vuHyf+a/Her7sRHHjLE+adnoIT3egMzrUnhNOg06GYII3fP/Pb708aQTAarHfRj6IXgsRhGagzcN4OrG+YzNicnNoCGhkZOi7y8F6uwfp1svcm7vJDpODTieZBX9cQFBchckDk9pGpBdd4tmcHyV8FwrLz+06SpwJ3rr3Zp3UVMYcpb9a+TAyfD6pEn8L9RzPskuDjPQmj+93B43IdEyg/VhH0j8ToRx9icFFZpFUFpPXl41sMvsGq8LYfErUkG2q/ZWC3BaKp7ojzMAydByzhPl34efQ67gBSiglu98b7PscYad7rXuvJrVj2TwCpHVziwKECmfhO6Y2n4xzOkYBfQJO7dflDSkdLTC+7TK/cY5P6yR1AfPcKPPcbXBpuhxOT/fzMyys7wvLLimdNqOVmJJ8V42HTsokbbPxov2BDcKd/z53uT8AYxb0j7NUtCGCBl/4/HzLsnnnMe6NWU0HAKo9zpwzCANh3p3qN0jLqyHOPb+pq9QfonaJw7fkFHwZSGIT9G2hvDcfRN0gAqOl5/L+93r0IrwjiAkTgpGjuBUeIB4NqWE0OpyjHTns6AIQtGC7dB6AQ/aDWB1GFkQPoTKEQIcwfC/t10Yg7VhGb2yjz9Pj0cm6bi4Vt3AttU8DrRYbKMAVPBDIWdzzgHWuHDndQkBdDGUMR3C1eBVTyEGTvbp4DW6It89PcfPfAc/B7ed1lG8SFViLM1tGU7oq4Luodn3+V8+goKm44JeV/0o7ufuk7+WHv+8TW7y/gO9DDPk3vofjfOBMZkWt2BdYSpCkJNCp4BBCPhXqFfH0X2UcXfZfnyp3b+49/r+O9l8/yj575Mgrouqi/T6aPUvVW6VwgSUxgjYQGq96r3eaxJnx959vk9zz6/5dkP5B/W+jL5eyL+QOIZ218m6OvsdTYO7UMHjMH7fEGLcJ9Z4zMxjn7NFPDd1c94GJE26WGZfS87b1Ng7fFL4I+TH2WoGqtXCwvmHXehM75m7+HwTBYI65k/1swq/0MS3+svdO7Dd+/lAQ5lNeTtjr2bD8bNTTKKX4GXL1mTJJ9eMisF//amZiwEMGyhScYNEUwh2BDVIbhfvTdH48WPm7p7ckFUcPMvY459moyN7KfJe0/6afK2S7jvvrIGbpN+HvvhkSWcCj/e577vGG3wAjdndV+M4j+2PmMb9myP/yzEmFpQYgjn1SjLW66OHP9EBH7xfVD+mYh0/2IlT8CAmD6W6rB+S/MKyunCxgdC+W1MP5hRECgbuODPbCCfElwbWBPdUd3v9vuuVv7Q5fe7GerH/vG3lzfgePrg2SvC6TBDP1djVZzCYIUM4fUjrODY/20X+SQDEQ+2L5AOwDF0sQAYjjozzAGOBVBqhqPwLkYs7BkOLAtQtuWO79mMdGyUouaet7AWrkvZGA3pPWL029gBhKNomGU5tEOhhLugLNIB+MzGHYBiqEvhYDZf4B5NAwJa6X1pDOHyqe9Dv9GY7w3taJen2r+92CQBZ26Iass8Xtx0oVkkvre74IIMpGdso8VWUJVcms3S3Kql9UrDcCN2I+SIxeiKIBnBiIOG1Vl/r/IGmlbJcs5kgyDj0iVjosKF72XZ7Vh+jZ9QapH0CD2frf2eMTLT4jRCqMElTnZFeqOtWC3A0WzIgND0GotvuzCuAZd52960p8iUqamLdZ2dciXNBD1Eo0Hq+KWO9wgCaG02+M3irGin3dx2GqLBGrI7984RW6fJLh+EbOcCW1/xRpbumL7tpwcARGJduVFsZMMc8bJhNgUXGVueamoBbDqYcwvsGOrXfasCRyMuOnreWY0baxCQeUPY4351wK/8rS8OpV+7Rwuvd4LY9c7NPQ91J1xWjtieT+RVvapzvqfn4rCdU/uLoPDlruMW1x1H7HdnczsoSeP2wuWIBjrfKFaa9EmaxmFTlYk6bAyUlE8OIciom0iFNV92Msv11m4dHudIvB2QiojbxObMDS/vU+5UsH5mcuVFYBN7MHrMO0ltz81xYV2xvhYHGo1L5wFTmzV9kMirJtbYIZ5bYSWQIn+2z8b16NnTYK3eysteNEzpys+bJWH00tY+alVKEFaL5OKebNNr2fbXjO9v/VZ2SVTaYhVLIOu5VZz9UuWlghrCvKsN+TxdS8hNUKJptuFCYXsIax3uMFzVW1lN1aTr2XSjZC4iXCt733umako6UbWsxOoxyXcKTibY2awDo7qANaWZquCLjtEMB5ePj2dKA1ZezAq380L5pBKrYZEMNrcO5F7spO3ZuVS5YYYZutJPSI4gJevWZ81aXWg8Cdeh2VzMMKeUVtkem2C+6BOMaZWEnldKhVmRUM4jqdjVhGlVzOJUcTe283hOPhJeYNAtfUUP7EEvkNYtswOJTNMNZra9NMSX0mAdLg77qTHlJdJSz4p1yby4XKFIrZZ80ptyH7fYbuMcjFYMz1kk5L6zShV7EyJrn+HK03WuQuDM0OuldbX5sl4q/CEvbQHnTOkMt149414POZ3ElgJ6AzeofLVdS6If3owDz8WBtx52/tAR6fKq4DKimb4r95rrTA8I6XXq+YiEVifnlZHFnidgh6RDQ0U50SGYZvHVNTfdBZxw5MQe7etxa2ES3k5pryjRUPQ7oWjpvbJHECJtRNR0I2alirEYrPX0jGaXA20CiUArNi5Vyee3ZEkqMWLnzU6+nWmFQdqjutvtrtez0x0XyTIN/LOfDM1tegnFHa7YxbIgldAgkKnXD6pwWgMpnqkDOy2d3M0sbCjqDW07M2G6E3ZcJiJzWcKG22Z16qM1hl71Y+yEN9KI9kHtrX0hTzkn33tHGtnmodPNh70i2fuct5FgoxmoszjejJuGXkONE07XjA4Uk+lNbc01OGU6swxFd0dnVfkCNtvqnuiXga7b6CIIxFjChLVzPAECOzSiZYZJYKHlTlN0slju55yk1XGdbK3NFgwL5FybIWbgJiKsxfK6JsPI8zLRztQlySwPSNXnRCwf+Q6PbVcu9iJ5giVzhTtyf4vq8kQf8eO0meW81nWocTAPfZvW9R7oClIxRG8ysB3ybzs1n21WmLSRb+Zx7XdBFQw5ji/NjikL0qvIjjbEaGNmVnRWxOV+jS24I7mm+RNIvKvd23uXoZg1WAtbptjZzjbdIJFXBsBYKW3f7LmTHweqHaJHENtVMT8j2/rorQ7MrE9Xl3N00HbL6pqEyjRIbIeudD7iSjuCpaQ9OuUmLeVl0EjyUjRO58rjXba41hszEk94g8Ae0gwbd4beUnw/o+RLgjnx2W/31jkZypLyNEFQqot31bp60R+dkJuRC3GQl/hUZfYSFaUydV6tFMg1i6g5Td/SS0bEt002nStM1DDVueaCkhDVm6epRuyv1XZLnmf1JuMP/Wx7kLSrYB5IZsHUi3qFEn04lRsmtPaaX87Y7GDv6h0uXBWhwDtW2yrn7MSHKmCMJAsOR51iMjxHd4WaI8UpCg8ZetkVCsM0c3QzB6e2XqbS+cb1Ke4LeGc6EDgWt4HOEtpC16tG2bdRtL1wB2zItDJaCrPOKoTisL+kOM/hJlNNPZ6dRadqxyFxkvAd1boQEiwsn4uuvo5g5mMFsugYfVbPJZQGp1saxLGd0gdzBYptGApaqhc8i0fG/uKeFjmzVY9XZLjM910gqF1kSqtEvGxn9XKQerXsc28IEDPzV+erL7AYKJaUtlwfj3v24MaDDgroaYbfe8lUJ+peoZmO9QZiF0QXUkrUbRS0cWDs9XbaOTOJif3koqKbvcCdV6wU2yuhZJZbia0CpyJwHdhCS5tblgvVImavAnp29ULjh6ZxEOeiqkyhL69plF08cV5pK9N2pGMtZpx6kmZZUbdYPqxDXwtAdAiSrpnCOnHSV014MxfETOAos2H2Lnao2+scqMW10Dp9OVUSUG5vvNss1jm7W+2rhcVcMbnenCluvjePpqMjRexkC/4Y48nKr+aenxcJbJqKA6Pv5T4Q6tBcxxt31ejLE5Fscy3st0IdKOtVj/VrpV+l0aKm5T7PzreptSq2B3pZkq6HGOvDNqobzBnUvtUOhc8KDp5ZlT+zz2lyuijmWmlmNEBu85uATZ3S2LBJeWxY5+haguteiMwn95f9bDbfbCSkXexg6wDmqYjLUedEV21Z2lR5OSy52WD4qkOtNermMNt0t+ICBidBLbFWz1dL6SAn13zVt4xPqCEJNiimhriSCo4PWDL2uPp2Xcqd7DeuOQv2+u6gsgp6KfydVKPOTd0l0kI05pHeICtYtWhBE0VN9DJirbU8s8VbbJpc2avIipIy67NyxTrxVC1Wdtifu02cCkghRWfYwzBLrN0LKuvU6tY9p/E03Fz26jwy0elVHSrmts36eudhhmiQ1imMXIcf8kNToApF5WmUCOZxunI2AjnHgpWVHk6rRFX6U2BwBLnjhGF/PSBJa+7Pp1VR2VKztQ29W08ZcU5W9LYlp+xguTNMiLviVGW77rTtCEoaErVSLkkt8Ol5a87NcMryFyxJZPI45Bci8Piao3IRW2fdHI98zF8khwqTrX4dGWHF7t3NLo0kn5zGcbyG9TjfYdopcW05tg+nZn4WpRk1I279IM5yxh72oR/aEJ0rNeK3txtvMb4jGLezdL2M4Z1Hir0qCvWcplAFrGIAk2n0TMfP6pru8262CFCkjIq5Lu12R/XadMR5VuxmOWvukrzN4l25InvspuI129OsGNcaz/eFxR937LnP7TYoNDLWRE2XKJnJ7IUQrA4dbF5PHke3Tq2t2CSf2ryxdfRLA6utRM8owV12Apli7upc9YCaxhqxVa77OraXewUXhDbFDwiL4nm7g6S98xmBNjXCfGh8c2kMy6Sre4RY8iB2XIfO2iXtb/vbotzDDuvKUbdLsiqOhk6wYtSXx8wM7HRnBRZJhhc3d5YXZYlGRpFJ1sbvCJcExvWkuSiTkvupjq9O28Gbbwd5pbfVGfZbsxoVLlv56JiBtGNxgxu2bZfmVbTM7bXqp9zKNvvCs4ay9iKr46+UZDGstqGxymFmwpATyK10mCJVVxy1ZhG+y1pHSs6Gkiq6KrE+cbL0bn7Cer9bIhGT9mWhu40iDpXmrvenVvGkADbUanPdzUV2tQmUOhPkdF5k1yEJQmkqsdj5Jm7cjIW4WrQBzk2XhHw5OhFClkMJFliD3fCunM+mVEvIVgX3QjimLJxl4mF21fLcUEctfubXR03KL7cLT8+I9RkhT9qJR531zGstJyr7gpJwyT7eZGNRq6JWn1g2apWNGlvxRpE5PQynNJ4v0WRTCuJq29B4BrcEcm3ZZMr4Lq1TsncGypJe9Dq60Fl51iD1snWwJqp9Awd4UpRURdvcEXMxrSZRRksipDnm1FYnIxtFKpYUN9x0ujCBRx+lMNH5xM2myPZCkCHAaKqOMPSIkgJ0mcPtOo1mYGnWT+0BXaPdfntbLmsV4+y9fBCm54O6ZCNSdBZXmDOEre/WwdxHfMePnJQ+braXeMCEHl1XqYbbiVFN14yIkYOE55bMtQHq2xCHCVSg9pY7V4aU6Xa6uVGFRKNZ5zxf35ZhSG/yPUbTOMogtes3En2lt9XBD6e3lRykmIZethewdAokOWgqF3dkZJ4WsWc3bKCu3D3rLp0FPyMwWUf4yHNKdTrwt+421WX5bG85qjxkFdOvVhfsIMo3/yoFFBjoqIi3zbQAEsZUhn/htdAYeJSm9v0Uj/QyA4pDAEuWHDAcpllW7YuFnxKwTIlqc/GVPbyiLox+wIGwWvhnoXHCnb6lGt2jrAVRHR2ek2LVu8Hc2g+HEmosb2iVcXl+YXSOuvYbfuEvbazZiH52UGmulHSoO4HQ7DznudqvvZUswBa2m5YKgQCIHMvZhvSlgN0f8ZC62Uyx7Ftiu2ovhiD5tuyk+jI6Gqf4sLbEqQh7UFdp+lXkTQ9RIJCczd14Feo2bNy5W/U6cTIREMeYgJkl67i51AMX6TtiuWOljTbvNo3oBL2MdhvPvDmL2hIbWl2veLeXzci3b7POjY4tWnMsNVvAPXF9afWMYuqpc+FaK6J0nF0zDc/1ds2hfUUuT6LnanaMw9Z0iZZ64F83omeCZV4FXj4Ajj3IDrMWhpPblbl9MSkjPjJzXSbi+X5esOveXZ7I6HwyxcV5D66XANufXEKxO19kGxz1AmJz2yMJvYZ9w75pkOMmGbLLdDccL4Mxn9b7YJ5vFmuKv23pDkXLBUVfYblSrsYe9siYC+rat0sLpCjIYBr6txt1VpaNtmApYNbeUVw6ZjRn0YC7btnT/KxTJmYgFMVDbS2F6PmyTva34w4pF74XXC3WWO+OTVkStONSrLJx03K6kDZqDcy9SwsoZtZ8mp3Miy+eYqDwV0xy2M1xXiNHBu6XDTUQUnLrUA7hcvpJTkiSThPYtbvU7lJH2Wy6zivW8PgDVXnO3Io17LAJckIO06Js9elWOrQe41/jYxQSMxbYrRkrGp6ItyOW865k+aflvs3tfX26FMdZiVVzwJqbhiGuCGcvEmtgParRVI8xvdRn5Vtydc7HFOvJqPCoA1QB2wq8V7m6XQkxt6Xm2pnKZ/GxatDLOpvlx2s27U87u3aomWGsSHyz9KXZipCSK7bID8p2Bss/c6oX6TFC8ljeydurM6N7fB/aNweth7V8je3IoOomQUU5l5GKxFHSKBiG+efLp5fxWPp5uPx3HyePB33/z84bH0eDb4+c7gfLwHK/3Hl9+duS/fLppXRCKNfjhLVKGv95EPlfzlc//5vPK0Yi/eN57ficrKvfDuZryx9/gPQSZm5T1WX/rcqT5n7Q++nFbqrxdxDVt+eB9stdxbQYT8d/UGk8Oc+h2kX9rc6fir2Mv1UYHwABN4RCPC/95+Hzpxe3h24LneobTs6/gbIYdX4+BRkPa8fHIC+//284JqeO8iUAAA== -->
