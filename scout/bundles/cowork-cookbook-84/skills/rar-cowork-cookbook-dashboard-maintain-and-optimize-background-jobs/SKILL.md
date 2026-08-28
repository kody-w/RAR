---
name: "rar-cowork-cookbook-dashboard-maintain-and-optimize-background-jobs"
description: "Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs", "rar_sha256": "27cf23c2bbf76e2b6e8a8a35db49357d388a0cfba834aa47bb6b9ad25df12bfe", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_and_optimize_background_jobs_agent.py` and in the RCI capsule.

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

Maintain and optimize background jobs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 27cf23c2bbf76e2b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_and_optimize_background_jobs_agent.py` first:

```bash
python3 dashboard_maintain_and_optimize_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_and_optimize_background_jobs_agent.py   # or on stdin
python3 dashboard_maintain_and_optimize_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and optimize background jobs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs',
    "version": '2.0.1',
    "display_name": 'Maintain and optimize background jobs Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-maintain-and-optimize-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '19ac1a455aa9b38e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/maintain-and-optimize-background-jobs'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-maintain-and-optimize-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMaintainAndOptimizeBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainAndOptimizeBackgroundJobs'
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
    print(DashboardMaintainAndOptimizeBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
