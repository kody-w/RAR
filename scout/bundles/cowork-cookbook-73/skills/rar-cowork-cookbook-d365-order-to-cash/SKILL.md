---
name: "rar-cowork-cookbook-d365-order-to-cash"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Order to cash end-to-end process - covers 5 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash", "rar_sha256": "fc702e5d63639e5c85fb87234bb7e0d1c46773b49b39d083ec543a1543f29bf9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_order_to_cash_agent.py` and embedded as the fenced Python below (sha256 fc702e5d63639e5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_order_to_cash_agent.py` first:

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
    "version": '2.0.0',
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
