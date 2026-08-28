---
name: "rar-cowork-cookbook-ar-aging-collection-email"
description: "Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ar_aging_collection_email", "rar_sha256": "506d2305f1393dfdd66d0e2f018115060c46d3b932e57fea0c362c3c3c38486f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ar_aging_collection_email`. The original RAPP
agent is preserved byte-for-byte in `ar_aging_collection_email_agent.py` and in the RCI capsule.

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

AR Aging Collection Email Draft — Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ar_aging_collection_email_agent.py` and embedded as the fenced Python below (sha256 506d2305f1393dfd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ar_aging_collection_email_agent.py` first:

```bash
python3 ar_aging_collection_email_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ar_aging_collection_email_agent.py   # or on stdin
python3 ar_aging_collection_email_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AR Aging Collection Email Draft — Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ar_aging_collection_email',
    "version": '2.0.0',
    "display_name": 'AR Aging Collection Email Draft',
    "description": 'Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ar-aging-collection-email',
        "upstream_url": 'https://coworkcookbook.com/recipes/ar-aging-collection-email',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee17c25e99830559',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ar-aging-collection-email', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ArAgingCollectionEmail(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ArAgingCollectionEmail'
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
    print(ArAgingCollectionEmail().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
