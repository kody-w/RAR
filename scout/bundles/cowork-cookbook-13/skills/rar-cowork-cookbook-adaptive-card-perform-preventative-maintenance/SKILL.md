---
name: "rar-cowork-cookbook-adaptive-card-perform-preventative-maintenance"
description: "Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_perform_preventative_maintenance", "rar_sha256": "49a0f3619d6c6be1d3d0f22716f95fbf5535dd047bc0677e4cac1a461b359e8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_perform_preventative_maintenance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_perform_preventative_maintenance_agent.py` and in the RCI capsule.

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

Perform preventative maintenance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 49a0f3619d6c6be1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_perform_preventative_maintenance_agent.py` first:

```bash
python3 adaptive_card_perform_preventative_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_perform_preventative_maintenance_agent.py   # or on stdin
python3 adaptive_card_perform_preventative_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform preventative maintenance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_perform_preventative_maintenance',
    "version": '2.0.0',
    "display_name": 'Perform preventative maintenance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of perform preventative maintenance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-perform-preventative-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'baeddee26c9306ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-preventative-maintenance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-perform-preventative-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardPerformPreventativeMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPerformPreventativeMaintenance'
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
    print(AdaptiveCardPerformPreventativeMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8162ZajyJLtr6ijH7KqyQwhJkGedda6CDQiCcQkoLJWFoMziHkSgur693YkRWRm1zndXX3vw1UOIcDd3Gyb2TZzJ35/sdsmzKuXzy8KsLPJ2k6SKATVxM68CZd3eRXDH3nswH8TN8+aKnLaJq/ql48vHqjdKiqaKM/gdKnKvdYF9cSeVKCtbScBE9az4eMrmHB25U12inic1Jld1GHeTHJ/UoDKz6t0UlTgCrLGvg9N7ShrQGZnLpjU8F5bT+CgCUgd4HlRFkyibOLZdejkUGb9ET6wowT+hGNUYKf1K9QM3Oy0SED98vmXXz++RPD7y+ffX9zEruGtlzetRqWkhwrSdxocvikARSV2FsA5RQ9RyuD1U2d4ywPvFvxUg8T/OPm3f4s7uwrqnz9/ySbPz5eX8Y/cZpMmBJMmt+sGeBPXLmwnSqKmf52wSWf3NQStaatshK+GIGfB62PmN0l5Mfn7+OynxyKvAWh++vKSQxXs0QVfXn4eMfjyUrXj99dRSvHTz69J3oHqp5+/yalb5wLcZhQGtX79+rx+ioUDvw2N/Puqf4dSH852wJeX74wbPw+9RzvhzJfXSx5lPz0EF1V+feD408//TKwbAjdOorr5H8n95SE4BLYHbXoq/vPHO8i/TpCnQe8y//myBXTrX7EEDn9b7uPkCdQ/k33H/z+JTqIMZsYb4v9Q3D+agPx98ss/te2/mvBx4n954UECw7kaM/Hz5PevirTkfvngfbv54dc/oOj/VoySt5V7l/A1tbPIB3Xz9esvH+r77Q+//vKhLWCswdT72lbJP5L5j3C9r/MDgs9RP/04F66vZXGWd9nkPdInv+fFv1R/vE50O4m8b/frz5Pv82X8IJPRiLdFHxB8lzM11PU7HH9++QOyRQatad37Y5jl//qvk0PkVnmd+81EcfO2mUAHN1EKRuXVMKon8O+Y2yOFVHU08t5jHIz/0cOjxpDsfvs/7p1OP7lPOp3aTx766kIi+vqkkq/fk+HX78jwt9eJClfJqyiIMjuZyKwkfcnsAI4dNYDTalBdIbc4fQM+QVGfxi8jW/721xb6epf5WvS/3YtA9GAumduOrFW3CXgdLT+HIHva6cK6AW7AbeFySe5C3fwIku9HiEidJ5DSmxGlOo6SZOJFFYQkr/q7bIjk51HYb7/95kBK/5I9aBafPApLPYUD3tWZfPoEVfaTKAibLxlww3zy4fc/Pkz+ffJfzboLH9eQIPk//QQ1vNcimHdtCodBF0KnQ1K5++n3P55QQzEZrITQq5EfgcdkGLcx8N5wVzbsJ4ykJg6AiEKs0yKvmnuNal4nW3/yri9cdHw0snuY183EAwXIPJC5PZRqQ3PekcxgaayhT2q//zhpa3Bf9Tensu8qppAA7Oa3yYGTYC3JE/jfqOZ9EJycZxGE/z0qHvehkOpDPVm8iXidHMdInRR2ZRdhZT/X8O2HX2ANeZsOhduTDHRfsrGEgvQRLXn2gAcOgsi4T5d+Gn0OO4QUcoRXv619H2OPFU+9V77qS1Y/U8KuRle4sETARYM28sbY+9szpGCH0CbeHT+o6Sjp6QXv6ZV7DEr/Xf+gPPqHH9uQLy2GzojJ/zf9ymgJu17LyzWrLvnJ8qjK5gPhsd8aPfFo0WCzcJd8z6ZvDcQb/byx8JcsiWC4VP3fHiPvfnmOeTBbW0EYZVa+y4faQ4RHufeYHWOwqsZot79kb3T/EWJ05zboNpjgMAHGuHtbcHz6pmkIDR2vv5X+u48hmDAqYFxOitZJYMz4AHiO7cZQq2rMu6dPYACDEegujNzwB6smUDqMEyh/ApWIYCbBknCH7phDMyHMfpWn34ZHY0NVPFzsTWBDC14nZ5g6Y/jUMF9hVzSOgSh8uIuapABiDFV8R7gO7eKhzNgDPxW0R1/kKYzo7z3wfPgt2O+6jOpDqZB8G4hlN1KxB24Pz77r+fQVVHaMo4eXfnT309bJ93Xpb1+yu47v7A+zPrlH8DdwJjDb0vpOsyNp1ZB4UvAMIBgJ9+r9+ijAjwr/rsvnPzX+P/21vcG9pGo/eu7zJGyaov48nT7K4FsVfIWUMYUxEhWgfq+In8ZC9emZbp++T7dP36XbD6s8QPs8+Wua/iDiGeKfJ7NX9BUdH+0jF4wx/PxAYLhPC/MTMT79ksngm8efYTHSb9LDEvxei96GwIIUVCAYBz9qUz2WtA5W0TsZQ598yd6j4pkzkOuzYCykdf5dLt+LMvTxw4XvNQM+yhq4tje2dwEYt0HJqH4NXj5nbZJ8fMnsFPzV7c9YJGAQQ2TGHRRMKOiUJgL3q/c2arz4cTN4TzXIEV7+ecy4j5Ox5f04ee9eP07e9hP37VrWwg3VL2PnPC4Jh8If72Pfd5oOeIG7uaYvRisem6SxYXs20n9WYkw0qDHk+HrU5S1zxxX/JAR+CQJQ/VmIeP9iJ0/6gAw/lvGoeUv6GurpwaYIEvsI4UjrkDZbOOHPy8B1KlC2sF56o7nf8PtmVv6w5Y87DM1jp/n7yxuNPH3w7CrhcJivn+qxYk5hzMIF4fUjuuCz/8t+8ykN0iDscKA4grFRH6dmjEe5lANmHu6hPobNZ5TPkL7jkyROeh5KzB0XpeZzQLi2O7MJaubgJANoB8p7ROzXsUmIRg0x23Zpdz4jPGZuUy7AUQd3wQybeXMcoCSD+zQNCAjW+9QYcujT7IeZI6bvre8Iz9P6318cioAjN0S9ZR8fbsrotmNIzi3cIEPC3GSVOSnx5eTKlZQIBKXJquUpHibt9o66dMKc9QNlRSyJlHW3u0y3OXO6rejuSqnSPJwB7rjrsyWZrXNa0ZyIuRq4b3X0IUh59Fzoew0jl5qdO4kOevTiCY6gigJp7KXVJlrWTCmgpHr2eTtVbirtNpJEXI1Cyyp5FYeynZQCcjzw9gXxr1kjYKvh7EWz0pStqN3x4SzB19toidWnUjXOyPKSG6WjVtiWy7LzYkEF/fTkH9e9iR5lSlJJmr4OBRR1yabnop+CTLr5ygVUO33LS+smFPqqUZJZcz4jM71wYjfkbpfyYk2jis1WHibky3a2TomZcMYoILpCGiaKuzhZM82z4TdjRXWgC9uotCqb5Gh7yxHzvWbtJFluLao8d7PAmLX6Op31mp7G6bWu4tt8I6CYW1LhTpp5ieisMeqoReYytCxKpPe9eCCxbaHviv3uWPXsSRxCQPayZiEbu4mnZ1EKBLfv8dsqXLD6NJyl9DGuugEN8LVReAl6O3KovtUHh6vOZaKEyJpohNnm3MrnW193DarxzEE9KOvOcIpSOtcbs+F6sBNsxjouM+x4a6zSmev2+ZyYfEerJHra8YbZ6/LZzU77EoGdfOvSmFtl2ekQCufSPeOORw3G0mndNj2iyMZZ1W6sn62WydamV1m3lVwau0vvscR2jmBmimJ97e6l9bQ8JOsuDTljul/qFjcXeaGhrPo2u0jTJWqfldaIxO2g1rdbv9mJaqfVbqdgqdT5B7+dU3aE6/rKMJG0P9MHfzPvarm28mBrKME8HuZqkUeEJ+aqzRRStY6vtV9uxM31eHP9HQb8oMPjVgpqPzSRjs5n4mp7rqYduGRLbIpkc2rX9+I+UTPrRu/SsO9W/uqMCaomn/WM1+JYpxqlMgPCzHyrPgZRWa0PJzo28sE8+2sitsn0uhLLxdHBtJ1hbBuXHOhNBPJOtvaipl9iMszw7erSmXlgH3K72M6iWtm1i1Ze5qvjLI96k6M4LXRWyeFsncAxIBpraPWVuTGmxZWXG/yoULtob8hHAgYnPdNcembSU3FNaoQU2cOxZlTHbA5OKaXtkdHqVZP2SeZupvJUo7cOot/qOA38FYkfp3HZ7jeWf9GXtF2rMAq3aYlmHq0pB4IpIyOp98YtzB0QW1JKCdFl3rRb1N+tmcqwy/wQLslOD1cqmqlueVQuyqKZJkToXVGLkm0RzdOjlE172VYFsxq6PDoHBpn0Cl3NmEqJrhSa6K6do3l+DDaXk0LN7Bl5FgpnLfcps71pRoXGQqi15g4LCIafU7G7w1doWy1JnQ8Un9nuvQZPEp7u565HbR209KnVdbkEiabtCMNy8hpBC7Lf9FwlOewR0OJKTPt+bh3cHdonirCP1za+xWniVmW2rnmzY64TGoIO4W7rDHtp4e4cuBWmBy+pFMdLS1E6cthxwcQ4XnrVIXVPJ9bNqWF76QJfcHBGNcnp1rqeBSabuao631L1QZnuzbUrcZ1RZ2S18vqUiy5xSnm4VUR+yjJ2vUNxtC5gNLpqSnhH5pR3aX5IQlDL24Ze8klmIUI17zSR0G+SeqhujLRfpSS/0BupW8vyQbXIhiTC5WrR8gnL04Lqb7MMudzU0zZosm2faFthmS6iNmy6RsQuDr1iu7lwXAXLVPASz25vWiC56Xm3n7k9edpfFNNOhZtxBlZelek6nIXKdSPpoO0ERcRM7dyc8URhrrVz8Ff1EAy0eUMzAx+IdqBnQCPr0yk9zCx+hsyuBJrTwjUTybU93JAVG+02Sk2YyPS4hq0Qjm/2jSNyIWfmMVUx6mVHp76ET1F5GfvChlTRhXXBr2lLFAsWN7ee4C7DQRWts2boWo8YYpkO9qUFc9KHEbfjj93SOClVmZg0kMgYQdI9hbBthB1Puqi6EW8UNdcruXUVUmnJyFnpaVmC7vM1cUpcS/PiwetmPgL5MVWB7jNsVPTzfuM0ZpxXkBV89JBt0E6W/do+lU25js8EttLXhovOHCcwxJw6765maA/n60b3rzndrJFFaeqLeeWIh2RPOLspl2BmTy7M+OYs7GFvWF2AG5hd3xDv5MntUlQ4hHO4A5rKCqhaUZS3ATOnDCLapFyouByOmR6xP/CrhjkvATaN60NJ4BhEakbu3A6wOmpgtemtyzjnTichiFJANUcNPRkKxYJdU7l5k1inHZdI6h72yC62Ek7sBanTqkUiC3HKTLMOFW5IJ1q1Y06+mueO8wPLXRi0tovrmlIb4G5WtxSt413Wrc+Gbs3KLWYe5aLc9d1pJZAXIvBYqd57Vcws5WWYHtmhy25BsKzn7eKY2P02Yc3+JrCXZLh6iqUl6AIRsdnhhPRKc57GlYOawRzX5HUJCxa7PyepF7HKfh6Dy9K6iEBBDOM0JQETrqjlLOzjgpZNRqTcZHvVGk0zUyMQKKsLL/NB4ImscBMrrFJyMciOFcFAbnTltlqJjc8imne2tJrgjmGAJrDfIqjzNFztlMXJ5NqLMU33zjamKNTQULdeqWvrVLX73gGBz1e8WFQm3G71NU83C9wfGobAaNAeo9izM3Ze89v52VMXB1/sebxQPeO2StrplXcKL8vnZs+s1dJRMNy6zhem2d6Wl25NXduoFk6wG9vmvEWsKbbAoyoRpcU05AoFkpuhbl3ZAteBZvIsrPbLmOtK3T96Jy6B/Ravo1cpNoVOLjVBgzsqLifx2eBtS32Ozi5pc54n2tpDeZ2b6610QFiGYjuZQ2w8vbAg3S5jcqMKLtryPM6pR1dMtksRBING+QdicSJrLj1dNrIV4PL2aDDKnOTUfeUXTL6I9ZTgEeO4oxTENa3Ilfe9nqTLwdwk6wBBBHR5TXhOH04bPEzRbJvIwlJB0SCLuuV+aTfaWkOL3a639rpqFvWgrdPUXtxWPSuTWBtsO5jZhALi+U4+Ur6mhadljVn7FvYI50T1Dz2ATevlmC29TChv+DXElLRLkNzKtyGDLikdZxL8kmMBkxC7VigOU+uo72wT2UcqxleIpmh66fr6LFtn1HyZytcgrm5n2XfbS0kPdCWrpTeL5WQjytHyUCwuK1+7HC6G6MR8mUzzNdbHtmC2WL47hQSbnTB3mV5qekrQ8lRQ1h5eLvybzQAZHRbrVdhaoG5XTak0AntWCrs+kkFSehZvSJ2jeiarrAI4EvMETpmfhEznQbxir1pa1H0/u9JSiUcGm8vx8Za29EpO53Z/4LbR4WAKCWwcKH1INx5XFMedlk7Ly4ZVs+lMMaJmIXtoZpLtzj9okeESMxGE/AKFlMEKy1OBwCp5a26NwzqBkBqSpPPy/LI2ssOOnhodv2YRt2Wq9UzxwFxME3YvXCPM5LBBCBXD3+Kqc1U91cH57brbBS7P7QtcZdY8i+DX3SAMeR1P5ezcDDa1HKaF6KI2u1zN2hjovW2TGr4zA28RaM6CtgVp1y1krm2HqONup8ESeYnsCwFDmDi2q4DKOx31Tz3T53SJLnDTObu8yqX5vpZdwhEb4UYgF0U4HJRqiDacqawPG/+8bXcuOtg1154HJ7g4nHPFFhRuisv90CzB8TTTG7oJ+kUuwmohpYmTYddSX5a2acxPU01A/OFqpnjLtEdkc5szYCZtct/BKacE6nHwyLm6VnFgLHh9mDbXRenhyxu+TwaIjomtamfeHuzS4lKv9ZRihWV6nBsxYXobdMAEmeV6YS/gp8zzXB2Go31l0khY9FQS7Qxt4FJs18lz2kewcMksNZoli5UOnIFqSR54eLfk97XlUR5s+enVuT4gBdWR82xDVs0QdqiELtbT2mkt+Yrr+Z4ncQvDM39xPh3pUrq4nB8ZYGgW7fXWCxJq4HOEUxHWkBPsfJ1mc0TIEmYKqBs5NxgmCiqBkThvCwi0jLhNIUgcmq6XXCa79MDKLSnupJSzFXPLGw4mnzUCY1GCcOkbH8vYglRF4hi04mm6it0NYGoUbXF3Ps/MQg3aevCo9NK5gtdVln4gdC5LSEDvbjfDCveHymK7HmGv9oHBL7v1dRHptOsxhwVI/ABZkz3FWzcJ3jOnLInhuG9uaNW9zvdbLFkGl9mCl+gtaOfsrLPqehVJl5MRW5gbHa0NQtoXGtdBOUUan+zsXBly7tptk2BZ1QFQ8c7fnJiahOhaJewaQIux9Sm41AJKHGaND3r6yuR4SS1yA2yoS3YpRTdxfY8uM5GzA5ZnhhbxF6esK6vCXiw3MJL3s/NWdslVfpXB3J46pbU58CHbTQcU7nlbbu2R16yKljJC5LQ53C6XPnfZfC3oR/9oqetd1Z0HfTz7LuoZTfCDUls+Z7vbMPP8HT8FF5mgvXC9z6UZ60WDz+HSLRnAjV+wZxtj9+Yy2DTXINf4tezw2npDIl2me3s3FKUNqtOr4nR1lSk7P1wcjcFn2C50wv11h6lGnpOw8b1RrJcgpJXyXaRz7q5aoT6R9GA/NVhvDtsDJ/X9lmXcUty6+KnbTo/1olqg0gVWMEKgN8dcPPYIBzv7nMUx6XAmmJnXmad9GNYikq/JzOIdwgErJx5UA/gN1qz2scjAjWgrz9x54BHtJrgMRcCuVtNTwxn5DU/TAycsaH5Do+KFKVO58y8DdRKkNgXx+ipBGL3Id7cyccKambOPIqSB8dJ3BtwZXKeJJ/IIWV05Ilz4+0uGzNpNHPjoNHd8bMomM4TCnWkohq5j8R5O0xpMwPl0lrDANxx6M0UM/HTYhldsGh4bco9P49MhdoCmzRZHkStqu5xvfcln+djU/VrPCb2a5+U1EOmKdtqF7VNJICL7DIfsf2NvDa/jW9NtRQ0ZzvN0hkf9OcRaZCnIVoWtwihDXfQgnfiACToxCE5WZJ3pPbwzNN1KVZ1b02G+6vhXR3EV/ygt7Io9L4rlEZVal1Fv84URErRUp828y31io5miwF7drXpz7cX1QLiHbXm9Ca2cabzIH04WGRPLY9MOm+Kkza+ygm48I2aJvuereT0fynnH9DSi6d2Zx3edQQObx1pVYfybWU0Pe5nCtpJ0xdxc3bDY3sQpT8N1uIN23BRspd2J1yXsnKIIRWYnplQr2gPscFqewH5IiJNZqoWanwQRR6+cTwnItuE1oHi3ZqqLUrltyeulPmQNU3dqghmbfEqzoeCFJYuWLMv+/eXjy3hA/Txm/l++dB7P+v6fHTk+TgffXkXdj5iB7X2+r/X5f6vgrx9fKjeC6j2OXOukDZ5Hkv/pwPXTX3udMcrqH+94x7dpt+bt3L6xg/E3mV6izGvrpuq/1nnS3g+AP744bT3+JkX99XnQ/XI3OC3GU/MfDByv3fvZ89cm/+pFdZHX45Lj8lUKvMhu3i6D56n0xxevh86M3PorTpFfQVWMtj/fkozHt+Nrkpc//gN8pZMaQyYAAA== -->
