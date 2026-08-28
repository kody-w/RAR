---
name: "rar-cowork-cookbook-configure-assess-software-releases"
description: "Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_assess_software_releases", "rar_sha256": "de78582c5155affb6a29752e8e8e42ea0cb64c500d3f9ef48cf3bccb988fa7df", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 de78582c5155affb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_assess_software_releases_agent.py` first:

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
    "version": '2.0.1',
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
