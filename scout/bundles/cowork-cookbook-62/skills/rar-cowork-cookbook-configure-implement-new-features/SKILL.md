---
name: "rar-cowork-cookbook-configure-implement-new-features"
description: "Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_new_features", "rar_sha256": "7bd79a6fd58f08698e5f5cb6eab62f943f82a5cfef5c14f9d41fabce621f8ed1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_implement_new_features_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-implement-new-features:6394b95dd87410bc09b80144289b61f975fbf0724e2a3c94fbc6fac0ffa73008", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_implement_new_features`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_implement_new_features_agent.py` is
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

Implement new features Configuration Bulk Setup — Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-new-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 7bd79a6fd58f0869…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_implement_new_features_agent.py` first:

```bash
python3 configure_implement_new_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_implement_new_features_agent.py   # or on stdin
python3 configure_implement_new_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement new features Configuration Bulk Setup — Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-new-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_implement_new_features',
    "version": '2.0.0',
    "display_name": 'Implement new features Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to implement new features from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-implement-new-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-implement-new-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21434cd3e49b1e5a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/implement-new-features'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-implement-new-features', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureImplementNewFeatures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureImplementNewFeatures'
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
    print(ConfigureImplementNewFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
