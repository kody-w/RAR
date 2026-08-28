---
name: "rar-cowork-cookbook-demo-data-migrate-to-new-versions-of-software"
description: "Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_migrate_to_new_versions_of_software", "rar_sha256": "ddd8aa83b6053462593854d2e4afcc7ac41efa652cc5cdb5e1846e22f6686b67", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_migrate_to_new_versions_of_software`. The original RAPP
agent is preserved byte-for-byte in `demo_data_migrate_to_new_versions_of_software_agent.py` and in the RCI capsule.

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

Migrate to new versions of software Demo Data Generator — Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 ddd8aa83b6053462…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_migrate_to_new_versions_of_software_agent.py` first:

```bash
python3 demo_data_migrate_to_new_versions_of_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_migrate_to_new_versions_of_software_agent.py   # or on stdin
python3 demo_data_migrate_to_new_versions_of_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Migrate to new versions of software Demo Data Generator — Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_migrate_to_new_versions_of_software',
    "version": '2.0.0',
    "display_name": 'Migrate to new versions of software Demo Data Generator',
    "description": 'Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-migrate-to-new-versions-of-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0c7aa945f00c52af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/migrate-to-new-versions-of-software'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-migrate-to-new-versions-of-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataMigrateToNewVersionsOfSoftware(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMigrateToNewVersionsOfSoftware'
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
    print(DemoDataMigrateToNewVersionsOfSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
