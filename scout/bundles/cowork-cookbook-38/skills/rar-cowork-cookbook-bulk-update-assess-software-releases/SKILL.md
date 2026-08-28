---
name: "rar-cowork-cookbook-bulk-update-assess-software-releases"
description: "Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_software_releases", "rar_sha256": "e7b9eb1cd9dede5f3354441f874361281ae977ffbb9198fa4b27b57a1e72e22d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_assess_software_releases`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_assess_software_releases_agent.py` and in the RCI capsule.

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

Assess software releases Bulk Field Update — Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 e7b9eb1cd9dede5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_assess_software_releases_agent.py` first:

```bash
python3 bulk_update_assess_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_assess_software_releases_agent.py   # or on stdin
python3 bulk_update_assess_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess software releases Bulk Field Update — Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_assess_software_releases',
    "version": '2.0.1',
    "display_name": 'Assess software releases Bulk Field Update',
    "description": 'Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-assess-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-assess-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6a5f400dc7043408',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/assess-software-releases'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-assess-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAssessSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAssessSoftwareReleases'
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
    print(BulkUpdateAssessSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
