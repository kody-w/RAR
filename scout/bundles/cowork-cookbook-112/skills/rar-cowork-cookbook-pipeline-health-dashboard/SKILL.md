---
name: "rar-cowork-cookbook-pipeline-health-dashboard"
description: "Produces a self-contained interactive HTML dashboard of pipeline by stage, value, age, and owner that opens in any browser without Dynamics 365 access."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_health_dashboard", "rar_sha256": "48531a665fd2d83c6167ab98782474e9715c011f90bcdb29f75a8213eb82b13b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pipeline_health_dashboard_agent.py` and embedded as the fenced Python below (sha256 48531a665fd2d83c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pipeline_health_dashboard_agent.py` first:

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
    "version": '2.0.1',
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
