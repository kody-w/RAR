---
name: "rar-cowork-cookbook-adaptive-card-define-implementation-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_implementation_strategy", "rar_sha256": "e27ca622646d5c3872a376185f798e8883a8e3ac347eabaca3c842278b37005d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_implementation_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_implementation_strategy_agent.py` and in the RCI capsule.

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

Define implementation strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_implementation_strategy_agent.py` and embedded as the fenced Python below (sha256 e27ca622646d5c38…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_implementation_strategy_agent.py` first:

```bash
python3 adaptive_card_define_implementation_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_implementation_strategy_agent.py   # or on stdin
python3 adaptive_card_define_implementation_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define implementation strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_implementation_strategy',
    "version": '2.0.1',
    "display_name": 'Define implementation strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-implementation-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '958e913397b5fe5a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-implementation-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-implementation-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDefineImplementationStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineImplementationStrategy'
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
    print(AdaptiveCardDefineImplementationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZei2Jb2X7GjP2RVmxnMoHlXrdUiyCSioKhU1spiOEwyyShU13/vgxqRlV333u7q9/3Q5hAC++x5P3ufQ/z2Yjd1mJcvn18MYGcTwU6SKATlxM68yTLv8vICf+QXB/6buHlWl5HT1HlZvXx88UDlllFRR3kGl2/L3GtcUE3sSQmaynYSMFl4NnzcgsnSLr2JbGibSZXZRRXm9ST3Jx7wowxMorRIQAqy2h5ZTaq6tGsQ9PCLXTfVxM/LCUgd4HlRFkyibOLZVejkkGP1ET6wowT+hDR7YKfVK9QL3OyRY/Xy+edfPr6M3F8+//biJnYFb7286TSqxN0VkL6TbzzFQ0aJnQVwRdFDD2XwugAlVCaFt6Dmk+fVDxVI/I+Tf/u3S2eXQfXj5y/Z5Pn58jL+0ZtsUodgUud2VQNv4tqF7URJVPevk0XS2X0FHVY3ZTa6DhoPrXx9rPzGKS8mP43PfngIeQ1A/cOXlxyqcNf5y8uPowe+vJTN+P115FL88ONrkneg/OHHb3yqxomBW4/MoNavX5/XT7aQ8Btp5N+l/gS5PgLtgC8vfzBu/Dz0Hu2EK19e4zzKfngwLsq8BZmdueCHH/8RWzcE7iWJqvp/xPfnB+MQ2B606an4jx/vTv5lMn0a9M7zH4stYFj/iiWQ/E3cx8nTUf+I993//4V1AlOsevf432X39xZMf5r8/A9t+2cLPk78Ly8cSGCOl2MVfp789tXY8sufP3jfbn745XfI+r9lY+RN6d45fE3tLPJBVX/9+vOH6n77wy8/f2gKmGuw8L42ZfL3eP49v97lfOfBJ9UP36+F8g/ZJcu7bPKe6ZPf8uJfyt9fJ6adRN63+9XnyR/rZfxMJ6MRb0IfLvhDzVRQ1z/48ceX3yFWZNCaxr0/hlX+r/86USO3zKvcryeGmzf1BAa4jlIwKr8Po2oC/461XQLo1yoaMe9BB/N/jPCoMQS6X//dvUPpJ/cJpYj9RKGvLoShrw8g/Po9EH59A8JfXyd7KCMvoyDK7GSiL7bbL5kdQMJRflGCCpQtRBanr8EniEmfxi8jUv76V8R8vXN8Lfpf7+AfPVBLX0ojYlVNAl5Hq48hyJ42urBfgBtwGygsyV2omR9B2P0IvVHlCUT9evRQdYmSZOJFJXRHXvZ33tCLn0dmv/76qwPB/Ev2gFhi8mgoFQIJ3tWZfPoETfSTKAjrLxlww3zy4bffP0z+Y/LPVt2ZjzK2EPafMYIa3nsQrLlmtB+GDwYcAso9Rr/9/nQ0ZJPBDggjGvkReCyGOXsB3pvXDXHxCafoiQOgt+8NLC/re3eqXyeSP3nXFwodH43IHuZVDTteATIPZG4PudrQnHdPZrAlVjAgld9/nDQVuEv91Sntu4opLH67/nWiLrewj+QJ/G9U804EF+dZBN3/nhOP+5BJ+aGasG8sXiebMUsnhV3aRVjaTxm+/YgL7B9vyyFze5KB7kv2fao83AOJoGfcZ0g/jTGHk0EK8cGr3mTfaeyx2+3vXa/8klXPcrDLMRQubA9QaNBE3tgk/vZMKTgZNIl39x/UdOT0jIL3jMo9B7l/PjcYj7nh++HjS4OjGDn5PzKljFYsBEHnhcWe5yb8Zq+fH94dZ6wxCo+xDA4Jd873Svo2OLzBzhv6fsmSCKZK2f/tQXmPyZPmgWhNCV2oL/Q7f5gQ0Lsj33u+jvlXlmOm21+yN5j/CD10xzRoKyxumPxjzr0JHJ++aRpCQ8frby3/Hl/oSpgRMCcnReMkMF98ADzHdi9Qq3KsuWdEYPKC0c1dGLnhd1ZNIHeYI5D/BCoRwSqCreDuuk0OzYRu9ss8/UYejYNU8QiwN4FDLHidHGHZjKlTwVqF09BIA73w4c5qkgLoY6jiu4er0C4eyoxz71NBe4xFnsJo/zECz4ffEv2uy6g+5Apht4a+7EYQ9sDtEdl3PZ+xgsqmY2neF30f7qetkz/2o799ye46vuM+rPjknr/fnDOBlZZWd4gdAauCoJOCZwLBTLh37ddH43109nddPv9p2P/hr+0H7q308H3kPk/Cui6qzwjyaH9v3e8VwgUCcyQqQPXeCT+NLerTo9g+fV9sn96K7TsZD5d9nvw1Pb9j8UzwzxPsFX1Fx0fryAVjBj8/0C3LT+z5Ezk+/ZLp4Fu8n0kxAm/Sw9b73oXeSGArCkoQjMSPrlSNzayD/fMOwzAiX7L3nHhWDET5LBhbaJX/oZLv7RhG+BHA924BH2U1lO2NQ10Axq1PMqpfgZfPWZMkH18yOwV/bcszNgeYwNAv454JFhMcl+oI3K/eR6fx4vvN373MID54+eex2j5OxjH34+R9Yv04edtD3DdoWQM3UT+P0/IoEpLCH++07ztLB7zA/VvdF6MNj43ROKQ9h+c/KzEWGdQYons16vJWtaPEPzGBX4IAlH9mot2/2MkTOiC6j+07qt8KvoJ6enAYgqDejoUIawtCZgMX/FkMlFOCawP7pDea+81/38zKH7b8fndD/dhd/vbyBiHPGDwnSUgOa/VTNXZKBGYsFAivH7kFn/0/zZhPXhAA4VwDmQGccW0ax2mS9iiXmDG4TTA0NqN8Zj4Ds9mMsGeAsF2CZIANUd0m3BmJ48zMIRgUpTzI75GtX8fRIBr1A6gPiDmGux5B4xRFzjHIdO7ZJGPbHjqbMSjje7BHfFt6gej5NPph5OjR93F3dM7T9t9eHJqElCJZSYvHZ4nMTZsm1s4tPE0H2j/n8SyXDT3XmNMeXR2yKOoYpjI0nVCc3ghca8FX/RlbrKVuJa9VewC7cJbr1CWjsjUT6Uk09YZ4B2Rb6Rrc30JoJtpyE/ALI5ZxqXBn4qWoYl5vdmZJ75XUppRTnplJQcQ7m7Bc97o2ElL2qvU62RJTGkcq084MLRRs17SVY6uSPLmxkCFGkOi01wwEPSamujYTeo45tlOaB1nXnKNiFMPKU6loSECIlsZmt+fEpUXu/bRlrVk+2+r0NrYqZru3ZqDdU9MOpUA7EKSKgwY7S5mi4AMLVnhtGmlZWivYAsx0aczJNbehw3J23SvkWlmsbjk6CLIxJeIpwReuYRGsrl5l7bq+nJQhZ7axGGkdpQulclvOy34JVx0sWdTDxuuV0w4LTsdGV7IikxNlXQr0ocLwjVZiJ03bzUVPv0aNPhs6XRWa6MzboOjVWTndqHLaFTpbDhQr0bvzGtMVKjDlmAARvvdg9nHyer12k/TAs8epePQ6fNeuXFIke2pdHy8ZSRuJotycA3M+FrvY4vAaVM5a25zrVXGlCi4nkU2+PuvVEqft4FaumKFLr1F/aWIh8plrR8xw5kDHdsfHkp9dzeOyls5k1ipKTFPhfN+ZDo1mAoK7Lr24BNGScJqUwSh0d6Vx5iw6cyDoKNk3fdWupkmRBI5BLJVk1WzYiw2mxim9EqZehmQAPPNknJdmuq0I8Vat5HTg8aMGruuDdR4QXBUokkuYMEIvjOBeuCvYdWhldX2fbPO96iPWfHP0y2tUoj5nrQd1zZe7al9bl1BKd+Fc6pmtXEVkrRR7uy62NJ5urzh9xMJy8DLR9lKTlGRqaGhxPpMZYZtocq4sMR/njAOdEkhHIrtK0HEQzR1lvUCzlGCkM27BcF5jdOCn8lQozCg0N3HeD94qrHhPPd+uziUy+f3SIIdLfNqanZznsO7O4EJSq7jcIAF0Oo8Ilw0V2tgeVzC3s2ZsJ8wO+p4yczLwKqvSRWO96/X8tqpu1mGrRClbYFYc3tS1GGveTIolGqlj2gaRi8V5JqnWCttvdGKv7TyVcJYZn8hEoJ7nDoVkl8KzxM6Zuuh0YQfOwZVtHCcGv1t7p7hyEnt/vs2OyQlDbonrXKNhtchJS8HRqCyX59XtpuJxWm0G56gFQkdWtJVN10GhtOXBhWlRyQKF8Uv+ulJ05XKr0JxTl4bJK3GNlGjZ1GhKzOSN6m33q5wEuiK1ty5NTxfJPDT2afC8M4qX00I7r6DrktCR2O7CV4VQT03ygtYGzccXE9EVHWz2XcVe1G5vsjdazG6ban9dN5Yt721usffRATsWJ5Nf4xVdkQfjqmvz09Zg88vBTA8HhfI5E7chQsiRrPddbO/YvY8r6d6y4gJPeVrfzi6JLm/F2O3JJEmUi9xG3uqUo9XtosgGYR8Bl8MC3IpzD0vXRlxn1MU2wpnBYbeyHXxNUs9pvB3WpWprktdvao/S0D1t3wDqXLcB0OZBTSMI7QbInK61NIyldccohlphcysVqxMR8+5UF905LGa+m54uaCn4nL8zz2QwU1EvXy6mEdUYvO+rcdefU0zXzDQJ6Zl/w2wuOpaIJizRmwkzNot4OYgPEh1sjwcB32sttnK2It+dszBZ7BSxWLIralvuMB6fO0O0sPZLEOTcdaMojXywri5XmM4iU8uFdtZ31EZinROwcshUPGbsURNF123Oyk6LzxomLfHkoOH4Idt2jkoeEEEd4pJh2kym3XY43CRZudrobQUV623TWu1npVua1sVfZsEy3s2QGbJdnDjTYJh9hHO3/CCZszmitCTdkqcTMWCWf+sUnepXfdgcPDaozIyqYylcuP1SNFIqd7F9liZsv0xPBpUdjs7BGwgv3DRqPuyZQErDleWvQYD6e4BE1H5Qce9w0mIQ8KLDry6JZtM6bRcklyoHYSh37IGDgb8ertvrKUI7blpjmx2H0NKQTEu1oX0tjXp32iqxNZ3LqHS6qZ15pNSWB1KQkYSl1QamyuUpuaJZGSRe2RCGb4dTUQiX5fkwnyuOpnJZN+wbVqn11KGrraCukorZcDG3Ke0+aedk6qjcjifEnC2ltLfzPDSLOtYNQOFog/OEsVpecrmtWl8+8kvlSkeyhSG8qTreLmvLvtcxgWbd1TFW9WZeFstco4Iw6gtGOST+nlVXBU6eidqIiHAZ7ElZahNR2DjxIhECQ7T3AiHrKoKROzQ9cRDRTe1wtRaXNSkwu0xVBTj1z8j+1PgyXiWcHYWH6iCnpLDPTAtTbkcbSC5xBjtltozshjvpsApM23J2Kx2V40Xvy+hCizAcdYSuBrwhqOCcHkNsaIdL765zcQqaYrObKkZtt2HsoOqCgIMb3JuaQdfYooEpoRQ3Ib7RwwW9wasNHV+vBM3XOiebR2fV0hv+ttVTuSYvudKelzV32Nsr2ldSroWjQJQMglEutzbrw87McuVauu74hiNYrLgYQyDVAmcstlioUf4UtYyddV1Y+WrKBCi+0oTcwWpRYi/TJFhZHfDakkuKs43J3go1hVV3uuT6dLo9MTUTViqq6JhisM2e3tZaIvE6jehZptP0KVoX5ty/ZjumtUhrjVrHYr62vKtvWWmE84YGeyriRF0iRAvUlIRbJ+Es7fU4nxzFWWcq5plNFYuLFJigXpYs/A04J5qyENfiTN5pyfWqiFAl7SJtD1p+5eI+2S9mvmOwUWZGHkkXhLhJeiVmyml/PZ4VBtvuOD1QSadNzZtcxallB3xloepcym4RawyVuTszVGoXe2m6OGsHdmFvc6vg1etg+LdVnBQu1TYcH2ZnHey2FDggVWffLl22sqfUJu+smOvjMPNWlHKElS1RR44aQmOHGlIqG2g2y4wbuiYGlOaba2go8bwYZ9gzI1cCdTauU39mpTqP764+fVC3qMKK1PJGofaZue6ri8Im+FDM+WF1LPSTXijHK3XLsMieoSac/U9esffYdpkXxWkWsahKRqo6czD83GVCKu3VmdXc1opB6LOicHKtpVYyC3FluqyTA3M6x5Qy8ExjcvsazDVyVg2eHohsT17JTIKAyxd6tGX66CKJynGNcdd0mYuSLaHHm2J3iVzkAropF2IgJ75H1dQl9NUrbJfnTXYlaWDGcXTYCDU7z7qm2JnyTuxNbsdudytbxpJ6mrJwu7Zcdhfhqm4zo+Krw5JKdlQBQ4OpV8dtati2NILeL9so2OAnYcrfIsqOJA4xeFzFekrNPFfNPUrGd3QW7bGioiVNTucnhF13u/h42ud4cwwak4k3WjFdrbN9gPF5tFvG5NUcVqYQopy/Fs7qFWucPXseujhmMhTspOuCohFCTZyMvg3NHPBRwoZO0B63Sr30UrJx5euqLGm5nkbLzYnfHTdB6sklxIiQEKm0WJlEv3SKcu64RzXeIJdYne2Z5Q2C39YgDoUbzJe3lCdz0QvWaswJZoSq27AyleVZ0utMSeaF1mDNpuTtsqLyhXjwRXvetbtSi1Mbqbtlakm7deWKpCO0YUebeshRgiWRBy7cFI6abB2F47e0ajhakxQ4whPNkKCtCuT9jYi3y2Bt99A9FktqJ2sRU4VRzGo62F3afOaba2RHrNu6dHHvWPd1N1W35mk3AwlI2iYz3dMcwfCup3ezrVPTtEfuTogrrlzh1OYp3lWcCkPmdweDXcF9AF6waba7lKeLm5NbK66GnGMuB8Fsdz1tn1e0s20aK20UFnblSN4cBiNtZFSH88FMaCNfDRhXtijxlJJTDmAIsTbQbrcZlkg+bntt9nRIasuL9LmSmudqLtREXTEKE8G27mFJSNLqoPV1hUtCrW6HQAXIqjlD7qXkxrf5CkGm2AmRWNQyo4Kw5kgkzzUvblptas3BmYC7ANBni7iW9cVu7cnQZ3YUdMnlVIRHuVxsEiTlT5Eks+kwj1IXk3aG66XLVUiF04UsiNSGDLTFIGezE3s+Tq3T5mrObuhpQTClWoI4n4mcmPY1e0DCg1g1BZGI2nmrFHLgScfjsfPmuzSdqTuGPHdbP8Jal6e9KUc6zLpbzvrjmiZ1sHQsx/NCr8N6pqpimzeQ7U4S/W5Kz6vNejEUZ47307xJRR2/3S6ASa7buWXSa4TGEIZbLU815807vlpgqws3bOebOHDxitEYKpIrpW3rPSFIGRU4wqGvEAGbIXKE0SGeZYC9DP5VVH2NkRGRaSWqDi453DZUdJZ2Z3k6RPhpgS8wzVpNi4vUVJF6ykW39qceqS9aR1X99cVxwyYSVKo5rSPYIi6Lqbpph7DLj4uzqiw3BJi5wtK9MXOlkj0Ky1ZEQKy0Lqn4koxYDdustnMHY7gbzZ+PAXJg4YbfFqaEw5yThXtkWCFdIqxyWXuEnAQkKvA3jj3G/gBCXzw4h1AlkF4i90147Mr+WqNYfSPck6OuGj71s0LeRF5qd0fR4KrsMq9QjeuDfYgBV2euhHyOPVcncIfY7o+x0/KhzmWkkHedg9rdJg67VcixBElW+qU6Lc4Z47mLYUkI7XZ1Bri6oM5rtso1/HQkjx5X5m11rW2vdNo1CeHzhjFXUhVXBLooUbjH36ZivlyqSJGya1Rz0Km6VNgZJ851NZ7nIduBuKb3yrpJwYVpt3qf1HHrSiy5wxuiXOu3mYVlyLI7DVaSEY6neTTSE+wmCLbNMBC2yQ27DQ2OG4AXQVm2JOFU/SZK/Xae42rrYbQjX0FbTzkEURhxutoRrdelWLImkE2w5R3A2+dAaNmD7YkgZpLWB/3mmhC8rUV2CxYluW0U5LjKhSCAHSEtI2o+rxN1hzprClDs3KQGEd+ffDt1j45elO4NkzKLPOXnwhNrLkTl8zZXVzmce8/XYxsNLPSDmx5KBoDTtqDxGQbwhpHmuHYT2MVxmIbTPsHBMec9kWNchaaLJZjua2pGLVhLDU8smhuXbjq48bVVWBDWhkovBoAfjcAHpnNEjNZag94s8aw5aHGpqlm5J9Ke6Lx+Nl8Y9FrrT+cS5zbhPLygxHGGS0fq5qHHzVZi6kzac7kTpCskDZfU5raWHNPvC1YR6dVsfsFj5jTrxNRTG5bsuJoSOB0PaiVe7r2IXXYoA3RyOaMLtY97Ltv4fBaT0rZ1dhSXzbNNfHHxW0eJSCdmQtkU0/6yWCx++unl48t4QP08Zv5fvWweT/v+vx06Ps4H315D3Y+Yge19vsv6/L9T75ePL6UbQeUeB65V0gTPI8n/ctz66a+8yBg59Y/3uuNbtFv9dmJf28H4e0svUeY1kLj/WuVJcz/8/fjiQHDLQFV9fR5yv9yNTYvxxPw74+7XaZRF45vXr3X+9XHyDF7G33AYXxEBL/p2GTwPpT++eD2MZORWXwma+grKYjT++YoE2oy/oq/Yy+//CZc+0uMyJgAA -->
