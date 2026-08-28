---
name: "rar-cowork-cookbook-adaptive-card-define-preliminary-budgets"
description: "Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_preliminary_budgets", "rar_sha256": "42a8093e5fbde899904455eb3bf8468973b5a5d4d42aa619f34ff9038daf2d25", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_preliminary_budgets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_preliminary_budgets_agent.py` and in the RCI capsule.

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

Define preliminary budgets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_preliminary_budgets_agent.py` and embedded as the fenced Python below (sha256 42a8093e5fbde899…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_preliminary_budgets_agent.py` first:

```bash
python3 adaptive_card_define_preliminary_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_preliminary_budgets_agent.py   # or on stdin
python3 adaptive_card_define_preliminary_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define preliminary budgets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_preliminary_budgets',
    "version": '2.0.1',
    "display_name": 'Define preliminary budgets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define preliminary budgets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-preliminary-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46f6a44b76d4c226',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/define-preliminary-budgets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-define-preliminary-budgets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefinePreliminaryBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefinePreliminaryBudgets'
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
    print(AdaptiveCardDefinePreliminaryBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZPiyLLlX2HyfejqR1VqRUJ17ZoNAgRaQCChja62Ku37vtPT/31CQGZ1vb795vbYfBhqSSRFuHscdz/uEcrfXsy2CfLq5fOL7JrZbGcmSRi41czMnNk67/MqBj/y2AL/ZnaeNVVotU1e1S8fXxy3tquwaMI8A9NPVe60tlvPzFnltrVpJe5s5ZjgcefO1mblzDhZPM7qzCzqIG9muTdzXC/M3FlRuUmYhplZjTOrdXy3qWd1YzZtPfPyauamlus4YebPwmzmmHVg5UBa/RE8MMME/ARjLq6Z1q/AJncw0yJx65fPv/z68SUE318+//ZiJ2YNbr282TOZs7krP33XTT9UAyGJmflgdDECZDJwXbgVMCQFt4DFs+fVh9pNvI+z//zPuDcrv/7585ds9vx8eZn+SG02awJ31uRm3bjOzDYL0wqTsBlfZ6ukN8caANW0VTZBVgNgM//1MfO7pLyY/XN69uGh5BUY+OHLSw5MMCfYv7z8PK3+y0vVTt9fJynFh59fk7x3qw8/f5dTt1bk2s0kDFj9+vV5/RQLBn4fGnp3rf8EUh8OttwvL39Y3PR52D2tE8x8eY3yMPvwEFxUeedmZma7H37+K7F24NpxEtbNvyX3l4fgwDUdsKan4T9/vIP862z+XNC7zL9WWwC3/p2VgOFv6j7OnkD9lew7/v9FdALCq35H/F+K+1cT5v+c/fKXa/vvJnyceV9eNiCcOxAdIPs+z377Kp+2619+cr7f/OnX34Ho/6MYOW8r+y7ha2pmoefWzdevv/xU32//9OsvP7UFiDWQdF/bKvlXMv8Vrnc9PyD4HPXhx7lAv5LFWd5ns/dIn/2WF/+j+v11pppJ6Hy/X3+e/TFfps98Ni3iTekDgj/kTA1s/QOOP7/8DngiA6tp7ftjkOX/8R+zQ2hXeZ17zUy287aZAQc3YepOxl+CsJ6Bv1NuVy7AtQ4nrnuMA/E/eXiyGBDct/9p3yn0k/2kUMh8MtBXG1DQ1wcBfv0DAX59EuC319kFyM+r0Af3k5m0Op2+ZKbvZs2kG8yo3aoDrGKNjfsJ8NGn6cvEkN/+XRVf79Jei/HbnezDB1tJa3ZiqrpN3NdptVrgZs+12aA+uINrt0BRktvAKi8EVPsRoFDnCWD5ZkKmjsMkmTlhBWDIAaNPsgF6nydh3759swCBf8ke1IrNHgWkhsCAd3Nmnz4Ba70k9IPmS+baQT776bfff5r9r9l/N+sufNJxAlT/9A2w8F5zQK61KRgG3AYcDYjk7pvffn+CDMRkoOIBT4Ze6D4mg1iNXecNcXm/+oQuiJnlAqQBymmRV829IjWvM9abvdsLlE6PJkYP8roBFa5wM8fN7BFINcFy3pHMQAmsQUDW3vhx1tbuXes3qzLvJqYg6c3m2+ywPoH6kSfgv8nM+yAwOc9CAP97PDzuAyHVT/WMfhPxOjtO0TkrzMosgsp86vDMh19A3XibDoSbs8ztv2RTwXQnqO6p8oAHDALI2E+Xfpp8DjqBFPCCU7/pvo8xpyp3uVe76ktWP9PArCZX2KAsAKV+GzpTcfjHM6RAJ9Amzh0/YOkk6ekF5+mVewxu/rpPkB99wo+NxpcWhRF89v9BRzJZv9rtpO1uddluZtvjRTIeqE691IT+o/0CTcFd8j2DvjcKbzTzxrZfsiQEIVKN/3iMvPviOebBYG0FoJNW0l0+CASA6iT3HqdT3FXVFOHml+yN1j8CdO4cBlwFkhoE/RRrbwqnp2+WBmCh0/X3En/3K4ARRAKIxVnRWgmIE891Hcu0Y2BVNeXa0xsgaN0J4j4I7eCHVc2AdAA0kD8DRoQAa0D9d+iOOVgmgNmr8vT78HBqnIqHc50ZaFbd15kG0mUKmRrkKOh+pjEAhZ/uomapCzAGJr4jXAdm8TBm6m+fBpqTL/IURPEfPfB8+D3A77ZM5gOpgGobgGU/Ea/jDg/Pvtv59BUwNp1S8j7pR3c/1zr7Y/35x5fsbuM714NMT+6x+x2cGciwtL5T60RUNSCb1H0GEIiEe5V+fRTaRyV/t+Xzn5r6D3+v77+XTuVHz32eBU1T1J8h6FHu3qrdK6AJCMRIWLj1e+X7NJWlT49E+/SHRPv0TLQf5D/g+jz7ezb+IOIZ3J9nyCv8Ck+PhNB2p+h9fgAk60+08Qmfnn7JJPe7r58BMZFtAphgfK88b0NA+fEr158GPypRPRWwHtTMO/UCb3zJ3uPhmS2A2TN/Kpt1/ocsvpfgiWYe/nqrEOBR1gDdztTA+e60xUkm82v35XPWJsnHl8xM3X9/azMVAxC4AJNpXwSSCLRFTejer95bpOnix83dPb0ALzj55ynLPs6mdvbj7L0z/Th72yvcN2FZCzZLv0xd8aQSDAU/3se+7xwt9wXs0ZqxmOx/bICmZuzZJP/ZiCm5gMWA0evJlrdsnTT+SQj44vtu9Wch4v2LmTwpA7D6VK7D5i3Ra2CnA5ofQObdlIAgpwBVtmDCn9UAPZVbtqAuOtNyv+P3fVn5Yy2/32FoHrvI317eqOPpg2fHCIaDHP1UT5URAtEKFILrR1yBZ//XveRTDiA90MMAQThqLmEKcxee5bhLiqJgHF8sXAuzvCVOLCkSsxbmwsEdMNAkEMrDcM+jYGzpmB7qoAsg7xGlX6c2IJxsc2HPxSgEtR2MQBcLnEJI1KQcEydN04GXSxImPQfUhe9TY8CYzwU/Fjih+d7WTsA81/3bi0XgYOQer9nV47OGKNW0tKV1HIR5lUA0ihFnbFtWR84RVq66LMUab6XRPAr0TR3kthb1VgmECtG5DdlU0u5sESyUC3O4a3dXgeRrlXOjyN9FIdfRvbiAtOvOJNYs7VOM3F7XyDWP7bS5CWAHYwU8QrAwyQvxVdMN2S4FJcEFpy6QMSPJheqhWtnCci4F2S6RdtIiM+INEuFdp0e7y3LJ1eohU8JS705LEzeQK38gd0fpWvHeAYlvCdceq+36eDsxq8K+Qr533C13GBeMx0uBQ6cbRXqdkJLrmHQhPYVY99w5MZuU4ZLZZ5zLqG3CWcmtY5sjxfcBbS+TIKZ6dJmEfLdO6KqWivRwVCQC9wN92xX4NqAVWU2K2BJuMXYSsvggWU7GH9JzJ0cbTStYREpad1wo/UKStVayTJnTbpe1qqMMWi6iALR5un3eZkTnbEqtPS8vvXRIw9CIRa9YH+aVyB04rU+lIRoXfnzzcWE884OvFBV2HXeXC4y79KHvD5jfr+VjYGDuuUflmoG0jZ2olpUEoWkmWzwhrjVLnlnUsy094pyFYTFscsDADgkZFoaE9pVxDGAkiBTwPOASgRjzbDd2VDUqmdxcwqZauafAdcsty2d0VLrLBX+wtA1yGi5dNirGnBx6NpQ3bKZ2BNkpplE5N2Y5tFk+1tZ+OKqV5d5urFXyCKOtMxgp1oGtXOdXJ9hZhnZisMBVL7lU00XEQNeIXYbrTC4rokxk9baf13XK4JuEjMJDTO7sxSbOWFytdge2RqX5ZnEjiY5Jh0uSq9eb6HLYNcI9bRc22XEbrMdtqouecTtu9U1x4y96VRwvhwKR9c46KX6GmgEDi6dipZOHrj97/oqnIF5i1v48WvbDPKvTgUojcoWLAeiMMPgAlkrBGba/8FyiXIvFRRIGSi2Fo8TskWSbCnuTvY63SDkJ65KN19mgc0HrVCv53JeFWBcrfIF48aGrF7eeJWklIUOCPqMw2uEHf+NHJp9fmkNu1F7txBJPr60rKxBr+lzDAl5eGc0WI0MstCW0UFMagQT9diMGVBFFJeR6WTSd7R78w8Ikui1DK8Z8KtjuoIqbZ3BwvmKwjpyvS/a2gi3cvNUR5EO+WJiHwOW4o5wNGk91c6nyKVQ3cHobmJEhKdeEkWMiq7hBpxPWOg+Hilh3uebh7Rrh541020ZIj0uyyvsCymsod90SK5bhOZ8fIH08itA5KzYlIYVGNodOfhc7G8YVY0aG15CaFfsy09Ejy0PVJQp0ROINR93L6bzab6lyFWKumrDCFs+WaSTZxwqv6dVquCC0Q+yz/mjr6Um87rhwEaxiiNg5aqzD9JoqxE5ItmUsd8kF9mWOhdsjf6nUG+GpMVXD4Y45CYfGPeyYTitzdHnbra3DdRlqi1XajU2rXNUbJ6zVxUVQnYQ4nvhrKG8dNEtX5R7w4ACBMB8sx7Y9WbpcicAtcwwj3CLe2ZfTyi74Kyzhm2WBHikdDZVBq7TMG2ChO8uGd+qay9Yj/YOExLW6cTg7Z2scvakGptGUyQXIjTsvFpxiWqAREpKWN3Zjng8at7CW1zalG2Z063I+N/bBluvcUCmajYAsl7IJe6rkjChKZUS8REf47NkrPbhIqyshYjKXQDluKTeDSXq43q+TtewHB0nD3djUCkKZO06C8NhOm2jZwLZhrc6jq0quolV22l3PfbPpaVV3rznnh6RGrPIsihpRZ48co3bZzt5c0fJ0hYQLyJTULvVAbGsC8nSGoNoqvLHMKTfGbVV13rBQ8eQ0OmOjotFSpPE1nyxuKjUXDnR2RJD9EdiHl2cJp/QIAt6HGD2ijvvRFvcRhvrzLUL7JIUuyE4OfLlfZ2ZcsAZ8w4KU3u5SnUdiJdVWba3Mu9SwOcsX21UgC45fUYJkoKqRiBclHC9dvQ7liBPYXYh6KzxIglo5kqtuwfK4ss0VIeh3iFYW8X6uafvoUHFnucT53sWRMka70RYSgpDZfRm2fngI0NVgpRmva/tLYSLCxcW17ng7wwXe7/Eli++u/gE7JDXew+0AZzZ3MqMUYQxNNDjL4Kl5CSkEP5Ci3qTHeocm+XWRU73BVmv1mPOSX9kkHpK81e4D+UxjqOHh1XabkDshOlw0uA6QfXE1l4h6pSE6cxJphSFyyFGpeUaO5/GiXzn0cio2ViJs90p7JSFL1uGopMN1vS54hLKNqySUpkvH+GC0dMlmQ7uOtzd8nmcEJ8dMf4hAxNocuRGIS2eur9aNj3EsCxaBzm9b5nakbf0qqXygWcgcEzMGjleAEojUxk/YybUYUPIxOuZ9sgdlhyogAs8UJuqVriR3fHsw52eMxESEXyXxETqYzeHcopcoxLhIoBqxu0rbMjESH4It7YqyiHiyI8WIDgxmdNJV9EzIJRTRwBgerlMoh88xtTMSLJQDngoE6joavXtZXFZH5VZddgdtS4pbF91JxpFd71lNklhHCaRjdAg0m96UkCDRS17Ukg4/y4qvEKJVdBDG0F15QtHkdtwLtDJWqy1zczdluZk74hVhJCZ2dsplIAmoXWYWNCS+oV0aoIJcLQ6jTtjSfgMXrVRch7XoUBFBXVXeIUWr9dRwsbvIWHUl45uwKdjeOEsQWlaIaqwuzHa1P9CtuNxb43HLEnvq7AiqwTXlngx4ocA9/cr71NowbxJyVCJ1e7slZYshe6Z0WRmUfZVVCn5xoKVbZyXjWSmwvNI584j1ySGoHHnhlE3Jzs/DkvZHZnmEBjOP4EjOnZqX6zOylCgzSNv9Ol3vT/K1TAQBX50X9Ro9R3sZ8jOJLTw4xsJtpmvkpd8uxzXp0pCQhtTOEw+caUvCLRgqa2UK21uaRDrCacotWQHJkOgJMSso49peg65KtoXT2fdOEMGHwdjvtkZA2UHLLc94MyLs6byJDmK+iPkUSaINtQuwRXKUHU07Ehc1DeD9ppb3bWqEJ7hx1XixqbLUOnDWKGtR51BKcGoZgnXl3bgoMXbf3YZOBx2uvbe2tX2MBGY44nQVpSMcF3kBMXHCEUm6dJxbcSlbcZu1MoJXbFcdLvwBWqqS4GsLTymExBj4LQgjX6vGBI7XnEgWG55GS/8I8EdRvjxrYZWSIq30AuNSW+cGB+6hPFonw8lGnLCjKAuV4w5Uu6yX6laOfXrBF+Uq8/kmJsbxPCKNNM7XEG2W9Qk0biycMxEf3Na7QC8lBUEMsl3uK4y4rHPZP6JKOmeGcGGG7GY1LMUaRnpTnueKqAraqkxxOJEtsz2I4ZGk4mbOSRHdxtCeC7yGPAeYpjpZfl46oqApa3rFe2GhHyTFVIhtZdw2ydAQBL7ZubHtLOfRwMxxdudVmt5g2ig0w1UZQRMoYdTx1ldn7BpY6NqMLGIe6rZh9jDCCutenvvwSYp6KGIHBW2JXDrCilp4Zzs6QHEllly9ZZA2ds2bmthBtRVY0cd5ZIUe6X1Nnvd+K9wQYxsG6Wib1tjITEORIqfqNCL5bT4fgiCQqHW+aVOKwncpx0pCfdZwUnT8fu5JoGliuP1CytaGvDvpc/usyW2RqSzndOZAHtHKwVaYRJCGDpgJ8QsRlLyC350l+mbXKokmFyoZaG5YFwHE0Ytz1xRORrdgt9tTsHk64QZruxGF6DmKkFQVQm7qiynk6nSjZpjdzseO9G2yvTnJCkadxtzNx75dl3JKqEh1FBvlLMauoiYZTR2pdeU7qSoS2gKzmHKztwq6jErDqE9rbr6NVL/lFnINt1CK+O6yKGHhGggnrpyjca9TDon0C2O1IwMvntvunIEy5GhtPQOHHJy33bXf9gfQTDhlacGYOfZLZ3fNFghsxbTOcrAzsalDnrQNpUWxC508r4OZExqih7aHocaGhu0yq0lM92yHcgxxMernMaOrKz+uPKk8cvguHtrzeRTmPbslA3rEyPWG2279kaTS1Fbzs2gfs/3hvKBP/YlnMbreSuN+US98m7IsLnHaBbo/DIbgya1aOxuJRNldHbmgURMrdLmgsUCgy4uxI5iAiRkPVrmu0pylq6yAYzBKHs9QCBtZVfNEDGv9wsHW+5EkTbyKhSXmXudJbV6kZFhE1oaKPd1d+eP2ItDOxh721+WFqTxB6sRL4S0KHcegal9K+9EPiYEjVweN21LCKXHsjQxn5qlL2bQHnRuyWpphV2/MMb2mONp1C1ebKxLikGfhZFGSNCB7lNJ3mccy0cqveoV0yK18uzLzYWQuNLrGMdsdmDHWxGEvINl83hBXX96sbrKWkb2AyhiiFkSXnfJ2Q4300jK79BScaw7uchahUHVrpE2oGwdcJhGA8M0/MfygLrmC2Cyhcn7wyt4Q95vloXfoeb6pL3JT3RzXCTV6MGxjB3oV7pijDWEZIrMKWqVX+dsSM+SypNpe8PZwsmS4c2VLVIcSO9Qgu6qJZcy03E2dZZJ0Sw7MiJ4xfhFhgu638RaX9A6H+uo21+bzLUE0XdxUToftEHu936ZIf1h7lHtqTJGuDUOETtHuWtEDcx1Rck42pK2FSzUglX4T+KB1ki91ehxqIsaO3uJowKSMuBiea0FUYGpgikLW0ljYu+vTwfRZ7jaP8k1nO+1RMbbKhtidxvZ6GfJUgt1oM174rkxcmK0PGEyQWxSXNn3UUBGsMkfIQrql1vPCFckQxBHn83mnzHdLee+C8u/IweK8oyKSqQ2X1FVoUR46JQ22+lWgMAxljJZE9CIMFugcw0/Q0q8t/LrxQCRamNJ4txTUxQaXinBlLpnzFXYIYW5S5Z4dS8+WcjRSsVr1VtSokz0pFeZmVch7xIFOt1tn8KxtonPoFsCNnsqYt3aWmjE45RpF8BW8cJRaFfYeDSjNPNon40DnGs72ys1TDpgD7jkHxNNQKyQrt+mOelS1LUfujYjJNbEUydqzF0QSoYd9kOOnOi2qntWJvdh7K7+Ez12C5Ov6FvREoM6VcGGph5u5s8VleN7sx8pqlPhkZ0WHYNw5wRoiY/S+ETDdYneQS8WczWTuuGQoC82HYW3qVXtKTnXfkKTrL5z5kMiusTlsh26Zc/q1ZK+WW8654+4MKR3YxcOehmur5a1I/JO3Ii/b3uIRBj8bspUfWW2dVcOe1gk5vvEnVlwicxQVRsWzEQndOYiNFMNIQFFsQSstGK7JGPPn1erl48t0IP08Vv7bL5OnE77/ZweNjzPBt9dN9yNl13Q+33V9/vum/frxpbJDYNjjcLVOWv95BPlfjlY//bsvKyYp4+N97fSWbGjeTuUb059+B+klzJy2boAxdZ6090Pejy9WW0+/CVF/fR5mv9wXmRbTyfgPi5oObu/vDL42+dfHm+WX6ZcVprc/gKrMxn1e+s9z548vzggcF9r1V4xYfHWrYlrz8w0IWCr6Cr8iL7//bwh2dj31JQAA -->
