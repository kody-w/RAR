---
name: "rar-cowork-cookbook-dashboard-define-organizational-structure"
description: "Produces a self-contained interactive HTML dashboard for define organizational structure - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_organizational_structure", "rar_sha256": "39675117fb21d45138ab691076c4cb9184228d77eb414a8cad533eb2fbb07f5a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_organizational_structure_agent.py` and in the RCI capsule.

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
