---
name: "rar-cowork-cookbook-bulk-update-qualify-and-disqualify-leads"
description: "Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_qualify_and_disqualify_leads", "rar_sha256": "42a0e815a4a7091ed56315f4963a1c658afb535c73ac8b0838b6ea3078a17ff7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_qualify_and_disqualify_leads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_qualify_and_disqualify_leads_agent.py` and in the RCI capsule.

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

Qualify and disqualify leads Bulk Field Update — Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_qualify_and_disqualify_leads_agent.py` and embedded as the fenced Python below (sha256 42a0e815a4a7091e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_qualify_and_disqualify_leads_agent.py` first:

```bash
python3 bulk_update_qualify_and_disqualify_leads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_qualify_and_disqualify_leads_agent.py   # or on stdin
python3 bulk_update_qualify_and_disqualify_leads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Qualify and disqualify leads Bulk Field Update — Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_qualify_and_disqualify_leads',
    "version": '2.0.0',
    "display_name": 'Qualify and disqualify leads Bulk Field Update',
    "description": 'Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-qualify-and-disqualify-leads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ac437cbee3509c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-qualify-and-disqualify-leads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateQualifyAndDisqualifyLeads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateQualifyAndDisqualifyLeads'
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
    print(BulkUpdateQualifyAndDisqualifyLeads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
