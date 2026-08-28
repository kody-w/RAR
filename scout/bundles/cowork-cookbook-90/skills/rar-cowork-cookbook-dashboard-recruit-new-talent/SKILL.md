---
name: "rar-cowork-cookbook-dashboard-recruit-new-talent"
description: "Produces a self-contained interactive HTML dashboard for recruit new talent - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_recruit_new_talent", "rar_sha256": "44c72cf595145414d421cfc24342964db27914625fb2b635e98ca2577dceed1e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 44c72cf595145414…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_recruit_new_talent_agent.py` first:

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
    "version": '2.0.1',
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
