---
name: "rar-cowork-cookbook-dashboard-retire-services"
description: "Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_services", "rar_sha256": "e8920a62d4d1c9faec7d43899c50e036662fd476112f92946a96bca8c15d7fad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_retire_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-retire-services:6699e942008fb576de21f6d936a514067837aa1670345f42c883c956ce7efd81", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_retire_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_retire_services_agent.py` is
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

Retire services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_services_agent.py` and embedded as the fenced Python below (sha256 e8920a62d4d1c9fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_services_agent.py` first:

```bash
python3 dashboard_retire_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_retire_services_agent.py   # or on stdin
python3 dashboard_retire_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_retire_services',
    "version": '2.0.0',
    "display_name": 'Retire services Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for retire services - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-retire-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-retire-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '84ce76aebdb86763',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/retire-services'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-retire-services', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRetireServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRetireServices'
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
    print(DashboardRetireServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
