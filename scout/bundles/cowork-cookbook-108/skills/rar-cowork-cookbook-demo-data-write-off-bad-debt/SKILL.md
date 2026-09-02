---
name: "rar-cowork-cookbook-demo-data-write-off-bad-debt"
description: "Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_write_off_bad_debt", "rar_sha256": "d246bc66a729aa0fd8d868bc7a3702a922b2e94fcb2861a06ffdc1b2db1cb082", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_write_off_bad_debt_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-write-off-bad-debt:a91b62fbaf7ecfa2d1c4fce6e14155d24c22a756686a9dfd8b65a870ca053bfc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_write_off_bad_debt`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_write_off_bad_debt_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_write_off_bad_debt_agent.py` and embedded as the fenced Python below (sha256 d246bc66a729aa0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_write_off_bad_debt_agent.py` first:

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
    "version": '2.0.0',
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
