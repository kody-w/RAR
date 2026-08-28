---
name: "rar-cowork-cookbook-prepare-for-a-customer-meeting-deep"
description: "Walk into your next customer meeting fully briefed - context pulled, deck built, prep time blocked."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_for_a_customer_meeting_deep", "rar_sha256": "2fac0ea958eb1dccee545cbd891f600a592a9a53532487977bd8963ced45385f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_for_a_customer_meeting_deep_agent.py` and embedded as the fenced Python below (sha256 2fac0ea958eb1dcc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_for_a_customer_meeting_deep_agent.py` first:

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
    "version": '2.0.0',
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
