---
name: "rar-cowork-cookbook-prepare-for-a-customer-meeting-deep"
description: "Walk into your next customer meeting fully briefed - context pulled, deck built, prep time blocked."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_for_a_customer_meeting_deep", "rar_sha256": "10767937c8e690630f7bf08cf858c96ddcaeda6bbcd43100fd6509c8fd33b017", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prepare_for_a_customer_meeting_deep`. The original RAPP
agent is preserved byte-for-byte in `prepare_for_a_customer_meeting_deep_agent.py` and in the RCI capsule.

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

Prepare for a customer meeting — Walk into your next customer meeting fully briefed - context pulled, deck built, prep time blocked.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-for-a-customer-meeting-deep
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_for_a_customer_meeting_deep_agent.py` and embedded as the fenced Python below (sha256 10767937c8e69063…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_for_a_customer_meeting_deep_agent.py` first:

```bash
python3 prepare_for_a_customer_meeting_deep_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_for_a_customer_meeting_deep_agent.py   # or on stdin
python3 prepare_for_a_customer_meeting_deep_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare for a customer meeting — Walk into your next customer meeting fully briefed - context pulled, deck built, prep time blocked.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-for-a-customer-meeting-deep
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prepare_for_a_customer_meeting_deep',
    "version": '2.0.1',
    "display_name": 'Prepare for a customer meeting',
    "description": 'Walk into your next customer meeting fully briefed - context pulled, deck built, prep time blocked.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prepare-for-a-customer-meeting-deep',
        "upstream_url": 'https://coworkcookbook.com/recipes/prepare-for-a-customer-meeting-deep',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '255f96c5f64a2da1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prepare-for-a-customer-meeting-deep', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email', 'Calendar Management', 'Scheduling'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PrepareForACustomerMeetingDeep(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareForACustomerMeetingDeep'
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
    print(PrepareForACustomerMeetingDeep().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
