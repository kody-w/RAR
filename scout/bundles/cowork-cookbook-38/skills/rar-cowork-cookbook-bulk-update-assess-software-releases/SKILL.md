---
name: "rar-cowork-cookbook-bulk-update-assess-software-releases"
description: "Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_software_releases", "rar_sha256": "d95b5341ec0fbf7a4788c43ed014ae72cfa49aaff25364bc10e922ed3b97affc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 d95b5341ec0fbf7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_assess_software_releases_agent.py` first:

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
    "version": '2.0.0',
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
