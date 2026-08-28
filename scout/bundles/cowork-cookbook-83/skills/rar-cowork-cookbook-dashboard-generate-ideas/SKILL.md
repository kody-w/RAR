---
name: "rar-cowork-cookbook-dashboard-generate-ideas"
description: "Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_generate_ideas", "rar_sha256": "b22c1eb2de066f554b54a475d65f4603c1838384088cfec0a3a806bc9cbaac2e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_generate_ideas`. The original RAPP
agent is preserved byte-for-byte in `dashboard_generate_ideas_agent.py` and in the RCI capsule.

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

Generate ideas Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-generate-ideas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 b22c1eb2de066f55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_generate_ideas_agent.py` first:

```bash
python3 dashboard_generate_ideas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_generate_ideas_agent.py   # or on stdin
python3 dashboard_generate_ideas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate ideas Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-generate-ideas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_generate_ideas',
    "version": '2.0.0',
    "display_name": 'Generate ideas Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-generate-ideas',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-generate-ideas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e21d3c1aaaa3f321',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/generate-ideas'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-generate-ideas', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardGenerateIdeas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardGenerateIdeas'
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
    print(DashboardGenerateIdeas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
