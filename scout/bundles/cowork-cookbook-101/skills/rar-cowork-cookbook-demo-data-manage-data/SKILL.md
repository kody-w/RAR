---
name: "rar-cowork-cookbook-demo-data-manage-data"
description: "Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_data", "rar_sha256": "18b640aff93f1838fa91017497ed3cca3535782236795cc5b7a82dd299961a0f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-data:eaa6424cb692c4cd378fc2b862b578e88191a59588a52232e721fd9fdac1ac0b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_data_agent.py` is
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

Manage data Demo Data Generator — Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_data_agent.py` and embedded as the fenced Python below (sha256 18b640aff93f1838…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_data_agent.py` first:

```bash
python3 demo_data_manage_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_data_agent.py   # or on stdin
python3 demo_data_manage_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data Demo Data Generator — Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_data',
    "version": '2.0.0',
    "display_name": 'Manage data Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage data in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7eb5736491f16430',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageData'
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
    print(DemoDataManageData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
