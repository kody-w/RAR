---
name: "rar-cowork-cookbook-bulk-update-oversee-active-campaigns"
description: "Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_oversee_active_campaigns", "rar_sha256": "7034ec9aed4277ca28fa607f48752fdc0e694a2d26760e9c2792994136917618", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_oversee_active_campaigns_agent.py` and embedded as the fenced Python below (sha256 7034ec9aed4277ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_oversee_active_campaigns_agent.py` first:

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
    "version": '2.0.0',
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
