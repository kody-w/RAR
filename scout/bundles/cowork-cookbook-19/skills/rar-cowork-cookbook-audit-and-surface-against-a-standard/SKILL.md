---
name: "rar-cowork-cookbook-audit-and-surface-against-a-standard"
description: "Audits every file in a specified folder against a named standard and returns a sortable Excel report of violations by severity (Critical/Major/Minor) with impact and recommended fixes; makes no changes to files."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_and_surface_against_a_standard", "rar_sha256": "c57c41ca65305e8cb2417f858aa4b1e445a56e9af710f4892ba5dc1a1a462f9c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "work_management", "advanced", "read_only", "analysis"]}
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
