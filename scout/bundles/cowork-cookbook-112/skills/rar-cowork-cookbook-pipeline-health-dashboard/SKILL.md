---
name: "rar-cowork-cookbook-pipeline-health-dashboard"
description: "Produces a self-contained interactive HTML dashboard of pipeline by stage, value, age, and owner that opens in any browser without Dynamics 365 access."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_health_dashboard", "rar_sha256": "1943f07bfb66bd571a7aba3f79916c25ebe0a18ed8eca7df48d68658f4136582", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pipeline_health_dashboard`. The original RAPP
agent is preserved byte-for-byte in `pipeline_health_dashboard_agent.py` and in the RCI capsule.

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

Pipeline Health HTML Dashboard — Produces a self-contained interactive HTML dashboard of pipeline by stage, value, age, and owner that opens in any browser without Dynamics 365 access.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-health-dashboard
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pipeline_health_dashboard_agent.py` and embedded as the fenced Python below (sha256 1943f07bfb66bd57…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pipeline_health_dashboard_agent.py` first:

```bash
python3 pipeline_health_dashboard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pipeline_health_dashboard_agent.py   # or on stdin
python3 pipeline_health_dashboard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pipeline Health HTML Dashboard — Produces a self-contained interactive HTML dashboard of pipeline by stage, value, age, and owner that opens in any browser without Dynamics 365 access.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-health-dashboard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pipeline_health_dashboard',
    "version": '2.0.0',
    "display_name": 'Pipeline Health HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard of pipeline by stage, value, age, and owner that opens in any browser without Dynamics 365 access.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'pipeline-health-dashboard',
        "upstream_url": 'https://coworkcookbook.com/recipes/pipeline-health-dashboard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16f2dc5614c14da0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/pipeline-health-dashboard', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:pipeline'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PipelineHealthDashboard(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PipelineHealthDashboard'
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
    print(PipelineHealthDashboard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
