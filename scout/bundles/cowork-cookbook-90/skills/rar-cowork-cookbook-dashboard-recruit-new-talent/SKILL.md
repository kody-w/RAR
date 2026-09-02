---
name: "rar-cowork-cookbook-dashboard-recruit-new-talent"
description: "Produces a self-contained interactive HTML dashboard for recruit new talent - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_recruit_new_talent", "rar_sha256": "8f89706fbf791136f1e8576dae0d3233bc29eacbe8c42819f235f59ed59eba2f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_recruit_new_talent_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-recruit-new-talent:a2823135f61bea69ac83aa0cea2641c48d7d31c3a30db45c8124a811a6553ffc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_recruit_new_talent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_recruit_new_talent_agent.py` is
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
