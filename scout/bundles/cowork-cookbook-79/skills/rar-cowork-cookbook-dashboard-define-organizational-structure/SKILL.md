---
name: "rar-cowork-cookbook-dashboard-define-organizational-structure"
description: "Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_organizational_structure", "rar_sha256": "39675117fb21d45138ab691076c4cb9184228d77eb414a8cad533eb2fbb07f5a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_organizational_structure_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-organizational-structure:c3509cb1b98fd81c700f255fc6b1191a511161b67d5ffd76c18f0b82b211e278", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_organizational_structure`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_organizational_structure_agent.py` is
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

Define organizational structure Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
      "type": "string"
    },
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 39675117fb21d451…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_organizational_structure_agent.py` first:

```bash
python3 dashboard_define_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_organizational_structure_agent.py   # or on stdin
python3 dashboard_define_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define organizational structure Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_organizational_structure',
    "version": '2.0.0',
    "display_name": 'Define organizational structure Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-define-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cc5c9486ebf52de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-organizational-structure'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:define', 'word:structure'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class DashboardDefineOrganizationalStructure(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(DashboardDefineOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
