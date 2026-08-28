---
name: "rar-cowork-cookbook-scheduled-brief-review-access-policies"
description: "Schedulable morning-brief email summarizing review access policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_review_access_policies", "rar_sha256": "903ac151080bcb6a634e7599d2d4e5d399a2c4fc54fc4ee24ed6a0d1f67dede8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_review_access_policies_agent.py` and embedded as the fenced Python below (sha256 903ac151080bcb6a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_review_access_policies_agent.py` first:

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
    "version": '2.0.0',
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
