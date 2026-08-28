---
name: "rar-cowork-cookbook-dashboard-generate-ideas"
description: "Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_generate_ideas", "rar_sha256": "d5a94a9b67c9c0465f110a9b10d12cc8a0886fd4e7e168db4bf3c3b46b4313a6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 d5a94a9b67c9c046…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_generate_ideas_agent.py` first:

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
    "version": '2.0.1',
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
