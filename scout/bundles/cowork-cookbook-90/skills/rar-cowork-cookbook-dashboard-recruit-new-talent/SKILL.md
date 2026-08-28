---
name: "rar-cowork-cookbook-dashboard-recruit-new-talent"
description: "Produces a self-contained interactive HTML dashboard for recruit new talent - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_recruit_new_talent", "rar_sha256": "8f89706fbf791136f1e8576dae0d3233bc29eacbe8c42819f235f59ed59eba2f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_recruit_new_talent`. The original RAPP
agent is preserved byte-for-byte in `dashboard_recruit_new_talent_agent.py` and in the RCI capsule.

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

Recruit new talent Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for recruit new talent - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-recruit-new-talent
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 8f89706fbf791136…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_recruit_new_talent_agent.py` first:

```bash
python3 dashboard_recruit_new_talent_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_recruit_new_talent_agent.py   # or on stdin
python3 dashboard_recruit_new_talent_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recruit new talent Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for recruit new talent - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-recruit-new-talent
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_recruit_new_talent',
    "version": '2.0.0',
    "display_name": 'Recruit new talent Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for recruit new talent - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-recruit-new-talent',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-recruit-new-talent',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '322ca8d5370f2ace',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/recruit-new-talent'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-recruit-new-talent', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRecruitNewTalent(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRecruitNewTalent'
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
    print(DashboardRecruitNewTalent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
