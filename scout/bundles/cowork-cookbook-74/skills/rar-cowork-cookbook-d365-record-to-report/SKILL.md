---
name: "rar-cowork-cookbook-d365-record-to-report"
description: "Scopes the conversation to Dynamics 365 Finance & Supply Chain Management record-to-report guidance (6 L2 areas, 49 L3 processes), answering against USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report", "rar_sha256": "4cca93e21260feb46032d1d69d7b1f08841223a31f9bb8d5ee74b43ae15206c5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_record_to_report`. The original RAPP
agent is preserved byte-for-byte in `d365_record_to_report_agent.py` and in the RCI capsule.

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

D365 Record to report Expert — Scopes the conversation to Dynamics 365 Finance & Supply Chain Management record-to-report guidance (6 L2 areas, 49 L3 processes), answering against USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_record_to_report_agent.py` and embedded as the fenced Python below (sha256 4cca93e21260feb4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_record_to_report_agent.py` first:

```bash
python3 d365_record_to_report_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_record_to_report_agent.py   # or on stdin
python3 d365_record_to_report_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Record to report Expert — Scopes the conversation to Dynamics 365 Finance & Supply Chain Management record-to-report guidance (6 L2 areas, 49 L3 processes), answering against USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_record_to_report',
    "version": '3.0.3',
    "display_name": 'D365 Record to report Expert',
    "description": 'Scopes the conversation to Dynamics 365 Finance & Supply Chain Management record-to-report guidance (6 L2 areas, 49 L3 processes), answering against USMF legal entity conventions via the D365 ERP plugin.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-record-to-report',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-record-to-report',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd4d6b9cdb91c4897',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report'], 'recipe_category': 'report', 'recipe_type': 'prompt+skill', 'upstream_path': 'record-to-report/d365-record-to-report', 'uses_skills': {'custom': ['d365-record-to-report'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Record to report Expert** skill for this conversation. From now on, scope your help to the record to report domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 Finance & Supply Chain Management record-to-report guidance (6 L2 areas, 49 L3 processes), answering against USMF legal entity conventions via the D365 ERP plugin.', 'example_request': 'Act as the D365 record to report expert and walk me through period-end close in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants D365 F&SCM help confined to the record-to-report end-to-end process, using USMF tenant conventions and the ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365RecordToReport(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecordToReport'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(D365RecordToReport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
