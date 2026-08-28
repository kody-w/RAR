---
name: "rar-cowork-cookbook-scheduled-brief-review-access-policies"
description: "Schedulable morning-brief email summarizing review access policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_review_access_policies", "rar_sha256": "3a4ff872afc8993bf83451306db8a2549bf7e18499d0439835963cfe96503ffb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_review_access_policies`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_review_access_policies_agent.py` and in the RCI capsule.

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

Review access policies Scheduled Email Brief — Schedulable morning-brief email summarizing review access policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-review-access-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_review_access_policies_agent.py` and embedded as the fenced Python below (sha256 3a4ff872afc8993b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_review_access_policies_agent.py` first:

```bash
python3 scheduled_brief_review_access_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_review_access_policies_agent.py   # or on stdin
python3 scheduled_brief_review_access_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review access policies Scheduled Email Brief — Schedulable morning-brief email summarizing review access policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-review-access-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_review_access_policies',
    "version": '2.0.1',
    "display_name": 'Review access policies Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing review access policies for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-review-access-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-review-access-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '350e16fc688ad9c2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-access-policies'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-review-access-policies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefReviewAccessPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReviewAccessPolicies'
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
    print(ScheduledBriefReviewAccessPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
