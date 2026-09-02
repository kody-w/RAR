---
name: "rar-cowork-cookbook-dashboard-implement-cloud-solutions"
description: "Produces a self-contained interactive HTML dashboard for implement cloud solutions - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_cloud_solutions", "rar_sha256": "4eb109a4dc1d66444b7135beccfd9afb1d70e08a8fe56b410ab79d09bd3e239c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_implement_cloud_solutions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-implement-cloud-solutions:9b15fa811d5b3f77e0885853193e45138c94ce2a2ee03a62f713b5a1f89a5726", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_implement_cloud_solutions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_implement_cloud_solutions_agent.py` is
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

Implement cloud solutions Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for implement cloud solutions - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-cloud-solutions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_implement_cloud_solutions_agent.py` and embedded as the fenced Python below (sha256 4eb109a4dc1d6644…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_implement_cloud_solutions_agent.py` first:

```bash
python3 dashboard_implement_cloud_solutions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_implement_cloud_solutions_agent.py   # or on stdin
python3 dashboard_implement_cloud_solutions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement cloud solutions Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for implement cloud solutions - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-cloud-solutions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_implement_cloud_solutions',
    "version": '2.0.0',
    "display_name": 'Implement cloud solutions Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for implement cloud solutions - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-implement-cloud-solutions',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-implement-cloud-solutions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddf3d094536d6547',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-cloud-solutions'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-implement-cloud-solutions', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardImplementCloudSolutions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImplementCloudSolutions'
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
    print(DashboardImplementCloudSolutions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
