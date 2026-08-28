---
name: "rar-cowork-cookbook-demo-data-write-off-bad-debt"
description: "Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_write_off_bad_debt", "rar_sha256": "5d777441f43691709326096a69c0535d722de38a3f02b5edef0cf2bef590634b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_write_off_bad_debt`. The original RAPP
agent is preserved byte-for-byte in `demo_data_write_off_bad_debt_agent.py` and in the RCI capsule.

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

Write off bad debt Demo Data Generator — Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_write_off_bad_debt_agent.py` and embedded as the fenced Python below (sha256 5d777441f4369170…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_write_off_bad_debt_agent.py` first:

```bash
python3 demo_data_write_off_bad_debt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_write_off_bad_debt_agent.py   # or on stdin
python3 demo_data_write_off_bad_debt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Write off bad debt Demo Data Generator — Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_write_off_bad_debt',
    "version": '2.0.1',
    "display_name": 'Write off bad debt Demo Data Generator',
    "description": 'Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-write-off-bad-debt',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '132ad93d46ccbb0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/write-off-bad-debt'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-write-off-bad-debt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataWriteOffBadDebt(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataWriteOffBadDebt'
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
    print(DemoDataWriteOffBadDebt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
