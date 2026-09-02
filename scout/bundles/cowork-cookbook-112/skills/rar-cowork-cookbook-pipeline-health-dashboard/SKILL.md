---
name: "rar-cowork-cookbook-pipeline-health-dashboard"
description: "Produces a self-contained interactive HTML dashboard of pipeline by stage, value, age, and owner that opens in any browser without Dynamics 365 access."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_health_dashboard", "rar_sha256": "1943f07bfb66bd571a7aba3f79916c25ebe0a18ed8eca7df48d68658f4136582", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pipeline_health_dashboard_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/pipeline-health-dashboard:2982dceb46c895745a703b55a0fcff770224d83012f3d3364945cefe6a0174f7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/pipeline_health_dashboard`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pipeline_health_dashboard_agent.py` is
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
