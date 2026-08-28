---
name: "rar-cowork-cookbook-configure-assess-software-releases"
description: "Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_assess_software_releases", "rar_sha256": "dd39638bf65b3e3ef81af376dc14cedf6b102d1734ca1e4d0e6806c6b8fc7cdf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_assess_software_releases`. The original RAPP
agent is preserved byte-for-byte in `configure_assess_software_releases_agent.py` and in the RCI capsule.

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

Assess software releases Configuration Bulk Setup — Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-assess-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 dd39638bf65b3e3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_assess_software_releases_agent.py` first:

```bash
python3 configure_assess_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_assess_software_releases_agent.py   # or on stdin
python3 configure_assess_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess software releases Configuration Bulk Setup — Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-assess-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_assess_software_releases',
    "version": '2.0.0',
    "display_name": 'Assess software releases Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-assess-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-assess-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d6dff430f4c9ee3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/assess-software-releases'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-assess-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAssessSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAssessSoftwareReleases'
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
    print(ConfigureAssessSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
