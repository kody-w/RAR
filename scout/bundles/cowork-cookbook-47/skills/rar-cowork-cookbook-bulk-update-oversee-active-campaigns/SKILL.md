---
name: "rar-cowork-cookbook-bulk-update-oversee-active-campaigns"
description: "Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_oversee_active_campaigns", "rar_sha256": "0b55d63699f9e6132ffe5886c5887eb72a6872b870b9ec4d47d1763b6564d13c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_oversee_active_campaigns`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_oversee_active_campaigns_agent.py` and in the RCI capsule.

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

Oversee active campaigns Bulk Field Update — Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_oversee_active_campaigns_agent.py` and embedded as the fenced Python below (sha256 0b55d63699f9e613…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_oversee_active_campaigns_agent.py` first:

```bash
python3 bulk_update_oversee_active_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_oversee_active_campaigns_agent.py   # or on stdin
python3 bulk_update_oversee_active_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Oversee active campaigns Bulk Field Update — Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_oversee_active_campaigns',
    "version": '2.0.1',
    "display_name": 'Oversee active campaigns Bulk Field Update',
    "description": 'Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-oversee-active-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '992a2378405713c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-oversee-active-campaigns', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateOverseeActiveCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateOverseeActiveCampaigns'
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
    print(BulkUpdateOverseeActiveCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
