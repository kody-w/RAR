---
name: "rar-cowork-cookbook-teams-update-review-access-policies"
description: "Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_review_access_policies", "rar_sha256": "d80e8e83cdc61c1cd2f6ca5acbad9bdef0a23ef40457d298431310b223476466", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_review_access_policies_agent.py` and embedded as the fenced Python below (sha256 d80e8e83cdc61c1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_review_access_policies_agent.py` first:

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
    "version": '2.0.1',
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
