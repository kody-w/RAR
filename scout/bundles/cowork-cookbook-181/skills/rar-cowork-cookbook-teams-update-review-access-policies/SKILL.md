---
name: "rar-cowork-cookbook-teams-update-review-access-policies"
description: "Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_review_access_policies", "rar_sha256": "f4f63fdb98a978d32fba2d92a7d9175a8f6bcf1de5fc270af805582391e950f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_review_access_policies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_review_access_policies_agent.py` and in the RCI capsule.

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

Review access policies Teams Channel Update — Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-review-access-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_review_access_policies_agent.py` and embedded as the fenced Python below (sha256 f4f63fdb98a978d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_review_access_policies_agent.py` first:

```bash
python3 teams_update_review_access_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_review_access_policies_agent.py   # or on stdin
python3 teams_update_review_access_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review access policies Teams Channel Update — Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-review-access-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_review_access_policies',
    "version": '2.0.0',
    "display_name": 'Review access policies Teams Channel Update',
    "description": 'Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-review-access-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-review-access-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9c27cb19f6b7cd2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-access-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-review-access-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateReviewAccessPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReviewAccessPolicies'
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
    print(TeamsUpdateReviewAccessPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
