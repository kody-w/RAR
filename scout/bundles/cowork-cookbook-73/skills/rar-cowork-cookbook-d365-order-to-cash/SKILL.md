---
name: "rar-cowork-cookbook-d365-order-to-cash"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Order to cash end-to-end process - covers 5 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash", "rar_sha256": "b3d89e1665aa8050a419ab04e0a708bdd19aa6551035d2e4b6237f7b6a270c43", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_order_to_cash`. The original RAPP
agent is preserved byte-for-byte in `d365_order_to_cash_agent.py` and in the RCI capsule.

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

D365 Order to cash Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Order to cash end-to-end process - covers 5 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_order_to_cash_agent.py` and embedded as the fenced Python below (sha256 b3d89e1665aa8050…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_order_to_cash_agent.py` first:

```bash
python3 d365_order_to_cash_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_order_to_cash_agent.py   # or on stdin
python3 d365_order_to_cash_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Order to cash Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Order to cash end-to-end process - covers 5 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_order_to_cash',
    "version": '2.0.1',
    "display_name": 'D365 Order to cash Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Order to cash end-to-end process - covers 5 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-order-to-cash',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-order-to-cash',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '89b6091838ba5b4c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'order-to-cash/d365-order-to-cash', 'uses_skills': {'custom': ['d365-order-to-cash'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365OrderToCash(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365OrderToCash'
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
    print(D365OrderToCash().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
