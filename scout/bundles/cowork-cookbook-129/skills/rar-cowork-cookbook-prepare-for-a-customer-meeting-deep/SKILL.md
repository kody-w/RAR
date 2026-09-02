---
name: "rar-cowork-cookbook-prepare-for-a-customer-meeting-deep"
description: "Walk into your next customer meeting fully briefed - context pulled, deck built, prep time blocked."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_for_a_customer_meeting_deep", "rar_sha256": "2fac0ea958eb1dccee545cbd891f600a592a9a53532487977bd8963ced45385f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prepare_for_a_customer_meeting_deep_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/prepare-for-a-customer-meeting-deep:08ab83b3ab10f873a06dfb5401a584af84660ebb87e61a2ab745601ce66d178e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/prepare_for_a_customer_meeting_deep`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prepare_for_a_customer_meeting_deep_agent.py` is
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
