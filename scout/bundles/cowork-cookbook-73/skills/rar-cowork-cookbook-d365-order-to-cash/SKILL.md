---
name: "rar-cowork-cookbook-d365-order-to-cash"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Order to cash end-to-end process - covers 5 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash", "rar_sha256": "fc702e5d63639e5c85fb87234bb7e0d1c46773b49b39d083ec543a1543f29bf9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_order_to_cash_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-order-to-cash:66b60a16c71cf93de2dae6f8dd0b0c68301d304ddd3e89208a1bd7c992044d63", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_order_to_cash`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_order_to_cash_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
