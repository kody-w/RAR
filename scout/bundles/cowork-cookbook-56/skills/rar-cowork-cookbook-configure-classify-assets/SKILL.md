---
name: "rar-cowork-cookbook-configure-classify-assets"
description: "Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_classify_assets", "rar_sha256": "62c20996af6f25a3cfcf6cf82fe56dbfd709f2cfabf9354747a4dd2befe4f8d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_classify_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-classify-assets:619aef5b0823a526b153c7a7bf7c57ed5d03e882afca8ea5813925797dba9594", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_classify_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_classify_assets_agent.py` is
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

Classify assets Configuration Bulk Setup — Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-classify-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_classify_assets_agent.py` and embedded as the fenced Python below (sha256 62c20996af6f25a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_classify_assets_agent.py` first:

```bash
python3 configure_classify_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_classify_assets_agent.py   # or on stdin
python3 configure_classify_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Classify assets Configuration Bulk Setup — Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-classify-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_classify_assets',
    "version": '2.0.0',
    "display_name": 'Classify assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-classify-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-classify-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f58aba90b73692aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/classify-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-classify-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureClassifyAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureClassifyAssets'
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
    print(ConfigureClassifyAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
