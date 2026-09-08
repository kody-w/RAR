---
name: "rar-cowork-cookbook-audit-and-surface-against-a-standard"
description: "Audits every file in a specified folder against a named standard and returns a sortable Excel report of violations by severity (Critical/Major/Minor) with impact and recommended fixes; makes no changes to files."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_and_surface_against_a_standard", "rar_sha256": "c57c41ca65305e8cb2417f858aa4b1e445a56e9af710f4892ba5dc1a1a462f9c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "work_management", "advanced", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_and_surface_against_a_standard`. The original RAPP
agent is preserved byte-for-byte in `audit_and_surface_against_a_standard_agent.py` and in the RCI capsule.

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

Audit and surface against a standard — Audits every file in a specified folder against a named standard and returns a sortable Excel report of violations by severity (Critical/Major/Minor) with impact and recommended fixes; makes no changes to files.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-and-surface-against-a-standard
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "folder": {
      "description": "The folder or location containing the items to audit.",
      "type": "string"
    },
    "item_type": {
      "description": "The kind of item to review, e.g. file, image, asset, or document.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "standard": {
      "description": "The standard to audit against: brand guidelines, compliance policy, naming convention, or internal quality standard.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_and_surface_against_a_standard_agent.py` and embedded as the fenced Python below (sha256 c57c41ca65305e8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_and_surface_against_a_standard_agent.py` first:

```bash
python3 audit_and_surface_against_a_standard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_and_surface_against_a_standard_agent.py   # or on stdin
python3 audit_and_surface_against_a_standard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit and surface against a standard — Audits every file in a specified folder against a named standard and returns a sortable Excel report of violations by severity (Critical/Major/Minor) with impact and recommended fixes; makes no changes to files.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-and-surface-against-a-standard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_and_surface_against_a_standard',
    "version": '3.0.2',
    "display_name": 'Audit and surface against a standard',
    "description": 'Audits every file in a specified folder against a named standard and returns a sortable Excel report of violations by severity (Critical/Major/Minor) with impact and recommended fixes; makes no changes to files.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'work_management', 'advanced', 'read_only', 'analysis'],
    "category": 'analysis',
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
        "upstream_slug": 'audit-and-surface-against-a-standard',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-and-surface-against-a-standard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '755d198aabc53809',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/review-against-standards/audit-content-against-a-standard'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'work-management/audit-and-surface-against-a-standard', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A sortable audit report showing every violation, its severity, and a recommended fix - so you can prioritize manual cleanup confidently.'], 'confidence': 1.0, 'deliverable': 'A sortable audit report showing every violation, its severity, and a recommended fix - so you can prioritize manual cleanup confidently.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'folder': 'The folder or location containing the items to audit.', 'item_type': 'The kind of item to review, e.g. file, image, asset, or document.', 'standard': 'The standard to audit against: brand guidelines, compliance policy, naming convention, or internal quality standard.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Apply a brand guide, naming convention, compliance policy, or quality standard across dozens of files - without manually reviewing each one and without risking accidental changes. A sortable audit report showing every violation, its severity, and a recommended fix - so you can prioritize manual cleanup confidently.', 'expected_output': 'A sortable audit report showing every violation, its severity, and a recommended fix - so you can prioritize manual cleanup confidently.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "Audit every [file / image / asset / document] in [folder] against [our standard / brand guidelines / compliance policy / naming convention]. Read each one in full.\n\nCategorize violations by severity:\n\nCritical\n\nMajor\n\nMinor\n\nFor each violation, describe the issue, the impact, and a specific recommended fix.\n\nProduce a sortable Excel report showing total items reviewed, violations by category, the most common issues, and the recommended order to address them.\n\nDon't change any files - give me the action list.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A sortable audit report showing every violation, its severity, and a recommended fix - so you can prioritize manual cleanup confidently.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits every file in a specified folder against a named standard and returns a sortable Excel report of violations by severity (Critical/Major/Minor) with impact and recommended fixes; makes no changes to files.', 'example_request': 'Audit every document in our Q4 Marketing folder against our brand guidelines and give me an Excel action list.', 'inputs': [{'description': 'The kind of item to review, e.g. file, image, asset, or document.', 'name': 'item_type'}, {'description': 'The folder or location containing the items to audit.', 'name': 'folder'}, {'description': 'The standard to audit against: brand guidelines, compliance policy, naming convention, or internal quality standard.', 'name': 'standard'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants dozens of files checked against a brand guide, naming convention, compliance policy, or quality standard without editing them.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAndSurfaceAgainstAStandard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAndSurfaceAgainstAStandard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'folder': {'description': 'The folder or location containing the items to audit.', 'type': 'string'}, 'item_type': {'description': 'The kind of item to review, e.g. file, image, asset, or document.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'standard': {'description': 'The standard to audit against: brand guidelines, compliance policy, naming convention, or internal quality standard.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(AuditAndSurfaceAgainstAStandard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
