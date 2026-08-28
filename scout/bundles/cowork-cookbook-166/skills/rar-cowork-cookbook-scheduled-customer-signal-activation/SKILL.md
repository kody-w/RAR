---
name: "rar-cowork-cookbook-scheduled-customer-signal-activation"
description: "Run a weekly customer-signal sweep that feeds next week's messaging, content, and campaign moves - correlated against live campaign performance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_customer_signal_activation", "rar_sha256": "0c34251fa981b6f9b2f0cfc8c75b2582a40d15f0305fda704e6ec938687250ee", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_customer_signal_activation_agent.py` and embedded as the fenced Python below (sha256 0c34251fa981b6f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_customer_signal_activation_agent.py` first:

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
    "version": '2.0.1',
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
