---
name: "rar-cowork-cookbook-dashboard-implement-cloud-solutions"
description: "Produces a self-contained interactive HTML dashboard for implement cloud solutions - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_cloud_solutions", "rar_sha256": "e4388b2cc9fb31283783a10a895c8ab1c1fbccf7d941b975b394371be00cb86c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_implement_cloud_solutions_agent.py` and embedded as the fenced Python below (sha256 e4388b2cc9fb3128…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_implement_cloud_solutions_agent.py` first:

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
    "version": '2.0.1',
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
