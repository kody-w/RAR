---
name: "rar-cowork-cookbook-dashboard-implement-cloud-solutions"
description: "Produces a self-contained interactive HTML dashboard for implement cloud solutions - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_cloud_solutions", "rar_sha256": "4eb109a4dc1d66444b7135beccfd9afb1d70e08a8fe56b410ab79d09bd3e239c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_implement_cloud_solutions`. The original RAPP
agent is preserved byte-for-byte in `dashboard_implement_cloud_solutions_agent.py` and in the RCI capsule.

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
