---
name: "rar-cowork-cookbook-d365-record-to-report"
description: "Scopes the conversation to Dynamics 365 Finance & Supply Chain Management record-to-report guidance (6 L2 areas, 49 L3 processes), answering against USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report", "rar_sha256": "4cca93e21260feb46032d1d69d7b1f08841223a31f9bb8d5ee74b43ae15206c5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
