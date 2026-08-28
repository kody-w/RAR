---
name: "rar-cowork-cookbook-dashboard-maintain-and-optimize-background-jobs"
description: "Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs", "rar_sha256": "2d492788f73b5b66139dfb9b319c20eb1b20d66a96cabc470bffa42681256947", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 2d492788f73b5b66…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_and_optimize_background_jobs_agent.py` first:

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
    "version": '2.0.0',
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
