---
name: "rar-cowork-cookbook-dashboard-create-marketing-material"
description: "Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_marketing_material", "rar_sha256": "dc8d49775c8ed4ea79a25490fd3ad5926690a21d86dee16548dc4b122a166a91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_create_marketing_material_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-create-marketing-material:b64f5900a99c4b99274114716fc0503d72effa39a276a3b515a96a8f4f74ed55", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_create_marketing_material`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_create_marketing_material_agent.py` is
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

Create marketing material Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 dc8d49775c8ed4ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_marketing_material_agent.py` first:

```bash
python3 dashboard_create_marketing_material_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_marketing_material_agent.py   # or on stdin
python3 dashboard_create_marketing_material_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create marketing material Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_marketing_material',
    "version": '2.0.0',
    "display_name": 'Create marketing material Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-marketing-material',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-marketing-material',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c4ddf7ad9d21a31',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-create-marketing-material', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardCreateMarketingMaterial(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateMarketingMaterial'
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
    print(DashboardCreateMarketingMaterial().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
