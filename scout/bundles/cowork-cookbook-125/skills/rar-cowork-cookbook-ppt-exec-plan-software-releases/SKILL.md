---
name: "rar-cowork-cookbook-ppt-exec-plan-software-releases"
description: "Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_software_releases", "rar_sha256": "963bec39f48ae64906fc9d830220e402b45f1d5a22255c09fef5b9b1708d6d84", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_plan_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-plan-software-releases:cebb61a39626354e789ca8a94d4cd799fec3bc613ebe603335751c728cc906c0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_plan_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_plan_software_releases_agent.py` is
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

Plan software releases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 963bec39f48ae649…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_software_releases_agent.py` first:

```bash
python3 ppt_exec_plan_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_software_releases_agent.py   # or on stdin
python3 ppt_exec_plan_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan software releases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_software_releases',
    "version": '2.0.0',
    "display_name": 'Plan software releases Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ffa5523311f4c1b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/plan-software-releases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-plan-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPlanSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanSoftwareReleases'
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
    print(PptExecPlanSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
