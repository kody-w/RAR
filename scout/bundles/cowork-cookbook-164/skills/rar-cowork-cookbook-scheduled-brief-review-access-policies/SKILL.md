---
name: "rar-cowork-cookbook-scheduled-brief-review-access-policies"
description: "Schedulable morning-brief email summarizing review access policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_review_access_policies", "rar_sha256": "903ac151080bcb6a634e7599d2d4e5d399a2c4fc54fc4ee24ed6a0d1f67dede8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_review_access_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-review-access-policies:ec7bdc3e75349570de559461f5099cc7871c45afc13dfefb7d68f5465718c01b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_review_access_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_review_access_policies_agent.py` is
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
