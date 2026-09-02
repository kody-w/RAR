---
name: "rar-cowork-cookbook-demo-data-develop-procurement-catalogs"
description: "Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_procurement_catalogs", "rar_sha256": "3f83185db7af5c5b424f034b710593bcc670805703d6673e8de2cf1e4ca4dd10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_procurement_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-procurement-catalogs:eb6585682b75d16d8026a5079f22c2377ecd9880074410214fc5015250b2ef06", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_procurement_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_procurement_catalogs_agent.py` is
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

Develop procurement catalogs Demo Data Generator — Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_procurement_catalogs_agent.py` and embedded as the fenced Python below (sha256 3f83185db7af5c5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_procurement_catalogs_agent.py` first:

```bash
python3 demo_data_develop_procurement_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_procurement_catalogs_agent.py   # or on stdin
python3 demo_data_develop_procurement_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement catalogs Demo Data Generator — Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_procurement_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop procurement catalogs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop procurement catalogs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-procurement-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fb4b9266c32525ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-catalogs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-develop-procurement-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopProcurementCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProcurementCatalogs'
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
    print(DemoDataDevelopProcurementCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
