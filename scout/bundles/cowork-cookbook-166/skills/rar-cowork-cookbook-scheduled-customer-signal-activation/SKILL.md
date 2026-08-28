---
name: "rar-cowork-cookbook-scheduled-customer-signal-activation"
description: "Run a weekly customer-signal sweep that feeds next week's messaging, content, and campaign moves - correlated against live campaign performance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_customer_signal_activation", "rar_sha256": "75398db71ae59b881207b842c5d6979a6de707f3f70789ddeba7e78f353c4242", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_customer_signal_activation`. The original RAPP
agent is preserved byte-for-byte in `scheduled_customer_signal_activation_agent.py` and in the RCI capsule.

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
