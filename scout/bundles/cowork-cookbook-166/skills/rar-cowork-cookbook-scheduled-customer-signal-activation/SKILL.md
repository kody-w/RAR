---
name: "rar-cowork-cookbook-scheduled-customer-signal-activation"
description: "Run a weekly customer-signal sweep that feeds next week's messaging, content, and campaign moves - correlated against live campaign performance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_customer_signal_activation", "rar_sha256": "75398db71ae59b881207b842c5d6979a6de707f3f70789ddeba7e78f353c4242", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_customer_signal_activation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-customer-signal-activation:ceb482b29f53d101e24dfe25cf1dd7ee36d4978c04e00938a36be16caeb402f6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_customer_signal_activation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_customer_signal_activation_agent.py` is
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

Scheduled customer signal activation — Run a weekly customer-signal sweep that feeds next week's messaging, content, and campaign moves - correlated against live campaign performance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-customer-signal-activation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_customer_signal_activation_agent.py` and embedded as the fenced Python below (sha256 75398db71ae59b88…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_customer_signal_activation_agent.py` first:

```bash
python3 scheduled_customer_signal_activation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_customer_signal_activation_agent.py   # or on stdin
python3 scheduled_customer_signal_activation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scheduled customer signal activation — Run a weekly customer-signal sweep that feeds next week's messaging, content, and campaign moves - correlated against live campaign performance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-customer-signal-activation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_customer_signal_activation',
    "version": '2.0.0',
    "display_name": 'Scheduled customer signal activation',
    "description": "Run a weekly customer-signal sweep that feeds next week's messaging, content, and campaign moves - correlated against live campaign performance.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'scheduled-customer-signal-activation',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-customer-signal-activation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16c7007a4d089f11',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/analyze-marketing-trends'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-customer-signal-activation', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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


class ScheduledCustomerSignalActivation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledCustomerSignalActivation'
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
    print(ScheduledCustomerSignalActivation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
