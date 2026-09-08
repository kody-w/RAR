---
name: "rar-cowork-cookbook-d365-hire-to-retire-manage-performance-and-growth"
description: "Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth", "rar_sha256": "72278fcf35453f51085e2e055ef45cadb7d292299a598ddcc4bc24d71e91a778", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth`. The original RAPP
agent is preserved byte-for-byte in `d365_hire_to_retire_manage_performance_and_growth_agent.py` and in the RCI capsule.

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

D365 Manage performance and growth Expert — Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_manage_performance_and_growth_agent.py` and embedded as the fenced Python below (sha256 72278fcf35453f51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_manage_performance_and_growth_agent.py` first:

```bash
python3 d365_hire_to_retire_manage_performance_and_growth_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_hire_to_retire_manage_performance_and_growth_agent.py   # or on stdin
python3 d365_hire_to_retire_manage_performance_and_growth_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage performance and growth Expert — Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth',
    "version": '3.0.3',
    "display_name": 'D365 Manage performance and growth Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-hire-to-retire-manage-performance-and-growth',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1be97f64b5ce82c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'hire-to-retire/d365-hire-to-retire-manage-performance-and-growth', 'uses_skills': {'custom': ['d365-hire-to-retire-manage-performance-and-growth'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage performance and growth Expert** skill for this conversation. From now on, scope your help to the hire to retire domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.', 'example_request': 'Act as the D365 Manage performance and growth expert and walk me through this process in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'When a user needs D365 F&SCM help on performance management and growth processes within Hire to retire, using the ERP plugin against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365HireToRetireManagePerformanceAndGrowth(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365HireToRetireManagePerformanceAndGrowth'
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
    print(D365HireToRetireManagePerformanceAndGrowth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjxpbmX9G8HTG2m6piB1E3bsQgCRBaEEJswuUos+/7JuT2f59E0lu27/XtHk/Pp1FFhRBkni3PeZ6Tb/LLm913Udm8fX67+HaxEOwsiyO/WdiFt1iXY9mk4KtMHfB/4ZZF18RO35VN+/bhzfNbt4mrLi6LebpbVn676CJ/Hjf4TWvPTxZdudhMhZ3HbrvAKXLB/8/L+rjYxo3/sSs/Nn4Hrj4sjnZhh/6i8pugbHK7cP2HBWFTjl20+B5FFgd8UTWl67et3/7wATxtR7+Ji3Bhh3ZctN0i80M7W/hFF3fTQrsc+cUQ2w97OEVeVFkfxsXfFi5wcAF0LMI+9h56YmBjZHcLu/HtT8At/2bnVea3b59//OnDWwyu3z7/8uZmdgtuvW2AD7Pxaqk8TH8aLv9mN1t4wsNqICqzixDMqSYQ4gL8frkHbnl+8O7s962fBR8W//7v6Wg3YfvD5y/F4vX58jb/U/ri4UZX2m3ne8CFynbiDLj5acFmoz21CxDGvinahb1ouzkon54zf5NUVou/z8++fyr5FPrd91/ewIo1j1X68vbDAsTky1vTz9efZinV9z98ykoQ5O9/+E1O2zuJ73azMGD1p6+v3y+xYOBvQ+Ng8fUic+uXrsZ348oHwn/n3/x5mv4S9wrJ1+fg78vqw+LPJc/+/B3Y+8xBB8j9c7EgBmDm26ekjIvvXzqacvCLeam+/+FfiXUj302zuO3+j+T++BQc+bYHovUKCcjReQl+WkAv377J/NdqK5Awf8UTMPxd3bdA/SvZj5X9B9FZXICSfV/LPxX3ZxOgvy9+/Je+/WcTPiyCL28bP4sBPNhO5n9e/PJIkR+/8367+d1PvwLR/6WYS9k37kPCV1B3ceC33devP37XPm5/99OP3/UVyGLfzr/2TfZnMv8srg89f4jga9T3f5wL9GtFWpRjsfhWQ4tfyup/NL9+Wuh2Fnu/3W8/L35fifMHWsxOvCt9huB31dgCW38Xxx/efgU4BCCu6d3HY4Af//Zvi2PsNmVbBt0CQG/fLcACd3Huz8arUdwu4icYN/6MxTEI7GscyP95hWeLy2Dx8/9yHyj/0X2hPOwBhPsaAWj72pVfn/g8Rxig3NffwfNXAM9fn/D886eFChSVTQwQFkCwwsryl3l80c1GVI3f+s0AgMuZOv8jEPBxvphx9+e/rOvrQ+ynavr5wQ/xExmVtTijYttn/qfZfyPyi5e3LiA1/+a7PdCYlQD9F0EMwP0DiEtbZgNA1TlWbRoDWvCAeheQ2/SQDeL5eRb2888/O3YbfSmeMI4vnqzXwmDAN3MWHz8CP4MsDqPuS+G7Ubn47pdfv1v8x+I/m/UQPuuQAbm8VgtYuLucJEBHYZ+DYWAhwdIDaHms1i+/vqINxBSApsHaxkH84l2QvanvvYf+smU/YiS1cHwQRxDuvCqbbibMuPu0EIPFN3uB0vnRzB5RCYjU8yu/8PzCnR7E+KX4Fsmi7BYzrbfB9GHRt/5D689O8yBgPwcwYHc/L45rGXBVmc3U37y4C0wuixiE/1tiPO8DIc137WL1LuLTQprzdVHZjV1Fjf3SEdjPdQEc9T4dCLcXhT9+KWaK9udQPYrnGR4wCETGfS3px3nNQVuSg3Ty2nfdjzH2zKjqg1mbL0X7KgzQC4CouIAogNL3TuFvr5Rqo7LPvEf8gKWzpNcqeK9VeeTg3Cj8F20NdwMPusWXHkNQYvH/RwM1u84KgsIJrMptFpykKtfnkszd47x0z4Zz1jFLeZTfbx3NO2q9g/eXIotBfjXT354jHwv5GvMExL4BcVdY5SEfOAKWZJb7SPI5aZtmLg/7S/HOEsD1xQMSQWwBIoCKmUP8rnB++m5pBMp+/v1bx/BIisabQwsSeVH1TgaSLPB9z7HdFFjVzIX6WlCQ8f5ctGMUu9EfvJqDDBILyF8AI2JQeoBJPn1D7ufTd9P/MPHZGM1THk1jD+q0eQgAdvjviz7GHYAru3s268DPzw8hwI286mbfHZBZwNPnTb/x6z5u425GxWdc/QpA9Mf5++npfNcHyerOxQJKoOpBdB9FM+dPDtoeYAPADVBDeVyANgAE5RWEh0A795958+pTnxIft18O+Y9Km/nrfeLsyDxnbgkWATAd3Jl+DxTqn6UJkJfPIx56/zHTvmmbZc9g2QLAAxrfnz57h09P+n/2F4t3uZ//aTf0/V/bMD0IXftjAnxeRF1XtZ9h+EnC7xz8CUAV/LS1ffDxx+gP5f7xyZEff1ftH4H+j89q/4OiZww+L/6asX8Q8SqWzwv0E/IJmR8dXsn2+oDYrD+urh+J+emXQvF/Q1agvsxBts0rOYEG4BsNvg8BXBg2AHjA4CcttjObjoDAHzwAluVL8fvsn6sP0EwRztnalr9DhUc/ACrhuYrf6Ao8Kjqg25v7y9Cfd3iPWmn9t89Fn2Uf3gC2+n91ZzfzUz7neztvDkFlzUge+49fD/i4dfPlH7fIp8eFnX1abHwAVVn7+5x8scrMqr8rnafHwNOZHD4sPBCndmZB4PGsfC47uwV5DGycPeumanbluQmc28ZvPeU/W2PMmA2Qzys/z7z14YUP4BvsAz4svrX0QOtrk/XYHRc92L/+OG8n5jA8pswXYA74+jbp258HHP/tp3+yCxj2AB0A3bOs34z8bWj52IbMLgDR3XPX/MsbCLkNYmC/gv7qY8FwUKMf25mdYZCkQDn4/Uwn8Oy/3+G+BLaRDRoqIJHGMHoZuAFOEiQekCiyJH3MR0jSDwjStT2H9jAGwxjGJpml57ku4bgY4dGoz6A2TS+BvGeWfp17kng2kmToAGEYLCBQDPE8PwDjvSW1pFySxhCbcWzSIRnb+W1qGhfey/Onp3NYvzXbc4ReAfjlzaEIMHJLtCL7/KxhBnV8DHamgwmbJBMfws696Pnunl+DQffJ3ks4X1VZKxqumHI96NhqS3JJnPe7EXLYRGAdSgzKHYQU1AnzBXK3jp11wLNdK+CNyeVqdieTG0yOd1DZdEnqQRDEsj/pSp8dI23oHFKt7YhL9tJt7ZgopBuDXIuhflgSGAPzkB/ds3M01cil1KhB52nx2NnV/qATvQZnh5A4nM9KAMMBSanDLbpH5hI9yC5qxgg0+c7FCuTICYLJmEzRr/f8+VYYAtLzFlkIFIcfgQCtVmoRPUZcc+il6bBdwsGgWGZrKJBZYQyPZhfHPyD1OcrSMGlF1dK3MgcdzcSdsoNochksbRuIbHGrvgeyTN+ovU4zy9O23aHM8si59VlvxLq718X2Ggq9hh1S9pZSLVEa/u1kQjp/MURas3bDscqGgql3NZ0okq4e99x+miozVSM6aJ3UPdf6kckJ5mg6XKneZdESyXO4jj3g25Zvz5aY9ZcrNRyVOj4EfpJajdz4Eybt8Ph021fm/WSKGpUgcSvep0FPUzdu9Aui1UIGsTt+vTOsfaXuAsU2BThxpZbcjCmO36SOPTsx10C9RiQtS+KnRNKWHmlF5D1SO47NKDIvkTTJhtXY1nyjo7hAbt18up8kXbna9+uqCQPS171TqN/ZbCuxjN4UVEXEYq+rwn2ZqVZwMAIEW0JigmrtkRqj3QrRjaseydVqosQ0Z4pdLIdKeqn0oRxUQWQ2coKo6b3LNqyZG75eHY3ax+pjeTyczSuX3MR+H5Btq0uHUZjweOInZpLSCT1OjtaNzRnrOA5vdoO+RE/Kpt4hy27tbHSsRtyD6RtR2E/86eTLZW1T3D6gjN43ob026HAkq0cKLJLmLFfeIJpxjO2YtdWe1iie3lYuEvS3KogF1LJaMybXahrZvEcSHuVh4vWgEbEve0sMBslzpT2/pwhGuTt3AnV6uL8uJ5ir6G2tNSuoVVYBVMLM7ZaQeFSb8NkniyMZwBsVFspTcqR1ZbmxdrdS6JgzLSjnxo0Z3ecFzrcw/aalyx0p2KpIR+ExIddiaQS0z/nC0c4rkVJsqEmtE29UUT/dNZEeUngrOkd8KmW+2qe9chWi7qga2vk2CVOin2HWW2nbjtG4sChzh1Pw9X4pds3RctZryDRUq/BScrzmTH6L+JLXnC1+y/i70UmteV0jKXmm2lW5u2/stXLvVgJ7O0qlZRCV0aQqskcSrIYrkl95ljh4q8E/bVpE35xX2cqADrAQ5IlcTTfrTps7NEMGh9Lycd8cltZNyIyxMdEzJaoJUYT5re7r80Es43btxzvKuqxSLcOFC7J1pXshUwivUfI1U+OirON8e2ECTzrkQ50qOn5e28kyn5YdN/H5AVYgizqR9q3KZSpLq7MQ3ndGsD2XR53e7utmezKSog4jzU+NrXG3jXRdpNFG4ch6U+AgIvjabQz3Ei3VRFYHzPOlZSrx8BI1bFoUm8g56QFhmGOfTBujHTY8e4GDY+WvbxBy29rh7Vxwk0uSwq0eR3w8RWM7AGwRYlsg615My/B8JcxL5sDYxVSaI6gqVOrW3Ea9wynv1WhJWZDGH8/QyW8IQiYZ/YQmJy+0Mr3oNtwJ2qM9FRsqumEHofB2Y3A7Gw1+hLfWxZBGefIEN1Dw3X0r7MU7QoXn8biitVtRl3uC5bSEqDz0Liv9yrgianQkT5nNhDx0Txn+wkBcF3GqWHbXcE8P4phq7G21PfFssU9Xm6SKR3zAmVIaxv2G17hyHdyyVXLuD5FgMUvuxFYYS8mOql739sYxUEML4y7kThrrFrzCk9aB3Su7wgkqeoNJXK1h5+3N6LeIgSBks1PpW4MuN5iQ8CGmybitDcttj15r3YxZzcnHVN4UnXA0d/tOaLjlbrNjIFg2cXSE0yZOL+SUqKfY2tx9/bJT4hSmMnXYxOFRELT0gmeXO+zBh4g9OTeEprirc4wTlNQahoZgE8cpBootDYaPabe1Mh7PJPpk61ukx0T2TE87O2abiDxY0lpzYwmFWqLZ7SYZJdxb73J23rTHcWXmspwuLWkgCQjOVZjMc6eto909JlYnYseil2ufo3eeUQdSOHpouuFK/2xTEbLhspwiErGn8HQKo407An7vrIy6cW19CQHFcKp1cmg+Ju/L2HFYmi7bLEquUsG1Z6NsYNJCzjLHauxRyC+b4nzf1FwCavMeqCVzijdcd6vup+KYBgV3z2K+0HcihK7E8KQZq1AJ8nHrNtT2mtMxqyC3DLr4VNKez3pOgKB22go+2C11WnVeQ3Xu1Ol7d4XsFAwR9s3yEmbL9RA2ZuuRmktuhL292xwYrRb9EqryKNhPd4qq1oLYiltEGCK9vspiH9jE7hBfmsY9nHaT1ra71dHfjEc3pt041TXbiRGmF3WBaod4tU/IYT/FhtirQop5GnuK95EgqhJaU9C9aTSCKFvBaq9CdmMFGaSX41GQttowl2YdpS1uXo832VgvefhoM/wZUteNhi8TZ7w2Dnaw7crPxptuo4QUj5fESf2Eu4a9v0cqnkNXhMF6nL+cCiuIVypKqSkjUPmpTDewT9nRHmUhKtgjSqbD2ekCmu78rCEX8ipxXKPlgCXW0ahp+lGVM8kQxNxLo9riZdWLaaacUuiubXZnZ3laQT2f8yv4theOS++8qwxsd+cUx94LCNSTFwUeSOacHk6bjeriALLvoymVOifyrokNHsZbJSLds2ODc/tLuyUh1C94krLoGAvObYoS+Mkre7qmS+4onxxh1eI21cYGvlntKlk6hpcNqtQrebs06mtlYc3KVShl3WpatrpADba2+qWMiX0tEs50m85tSRJSg28ut6zIow2Np8Utpra1Qly1FEFjEiJXq3C5oUXjqpypzQ6vPLGzDj0XNdMtdQtrxIiEFUw02UbH/e7osuUlbevSqjUy2lwhb43stGidbEQxgTZIaey4+369viJnVbmFdnnYN5dRo7bkSjBo4cqtHVUJr7syFExRH4MmH+20KVzMjLo0znY0wbiy23D8tJSU4kjvlmzFX1lqLHAV2/A6K7MyapV3TgfoJ7F6u4Hbdr8+peuxXzP7QB0FQg+Zzp5KygV1rboBEGRamTbWaD+RA7/Pz0slgwmCdu0Lua/ciLml2FLRrBg1pOq0R0cprVbrRNVpfes4JaQ3trKr2ZRs1cGy64F2tsnduWqeeR0dleuvSF9nSLNS05bHBO12JclyzOwNhYu+BthS2FdWyRqx6FjatV42dmFkvkjDpRIL3vZ+Ua8IymJH3uOpRkGvVOAs7/zhgG2V+0Eb0OMZh1hb7w7hmMIKsmfKTudoT0hWd7fbJth0sfkOulfSOla4uNfPkbEiVN/iAcXxeqxZnbq6oiWrMlLKxmh92IqH3Nk7bovdERKqTxLSWRJi4Qp8EThe7Y6SkJoGoXGdD0E7iuonRbBPzjZsp9MqaS8epuDdWps4mh6SZaGrZ18jWb/VRd0RcwBgK1q2runOitQEB9uNChZWQPJ+dz2CdmWHDCsOuTOK3uxJsr6gNzsh6LtHuvx5czmeeM6E+zaIJU6U2GYnF7YetUvnWpyXN+xEEP6uiXcwSkYDj6WqBVpT21Ytu3UxlV1boXfZIxdschWj6l2qvg601K/SfLjepJXHIkPrwOcrMsRhNWUTgMADYyj1YZSmRBGkgRlyZ7PNltvpdL4IVtjvigvaXgutKCVsl5AMQk/rnXJG4RSQX5uHXJ3czxgynla1BOPFgTvjgVtxNa8Yggy6ZSary1EwVZTl6CFU6pNBpNOS4IeBPrvB3qpXVSHA7OCO8VSuD74owhZzjHYWI+QK1vnOsYf3rlvXnSkLbHvpnd2FnoyW74izuj9a1jJhIlGUrLVhpcszRG1ORnYXZIbCrwUVKALpIBVn4Hyzo4rQi1fpRhb6qHJQhsPwe8OrHOQx7rZ1hE2kI668JYgMkpWjfVsiyPbiWRCEGY6x9QkUZTA6FIeeOOzhtpN0ekKR29A0grBRHD1RbEPEiFG5Ul61apc2g/nccWoBAHbyxjO29tlVad3gnJvZHpoQsS2YqblTeJbxZV4Rm0HZVivTWVkY1m4OFbZbVXpsE91OdaJDzeAF0aUQ4J4N25jdsowcokVWUFXd9Y7C0MyLoFytveXdEfjGPNZuYtwOMAEx8DgyWznaV1BQDUv/SLQEuu26NTNwV/ewmoqqjpA6sDU5tv3i3I9Ewe3L8zJ3ZbEgJPNM3cxtcsKjCd3Yt9UGP5rIOs2Ok7KEHKhWZWdz6A7iYFq9GZ+PZu53+TEpSvmE8vUaDoXIqu6GS3hkkkBcLuXRFt9ANKPFt06F5euaCfbGZq0cwi0N4dAw9LBTK8o0ZbQ3CjyJUfddOgT9tdoImggh8BkV/bQhuklDFXJCzMDcKp0QyMr+lJyXhQIXvF3rjClD16tcl6dMu6oX1k4vK2IJe7bD5HpBJl0MyPGMejXbrvb1lssMepdLTY0ZGeGtpUCqeT2iRMglrNzBZcE2D/RaUkYLsrPrMOxN4pxNrXzhexfsfbn4SJ8xkTyBnYTsCz7YRupr9n68ms2tuTD9es9c+0YgG2NTr3e4y1vVVcNW15Bh86E4n5KdPK6cXLkdtsmWdU6hPyFMR6h4s06LAcv84U5Miqwd++tmFTD6fa3fEvVQObJyXecQa7C8qGxwvRzpnMGjK5NiPGS6Xp0SenBRYhKFQm+v5aIgKcjUTd7WjbJezLuteNoq7v1I4xmSmHsybFBWNlPRnZr1rWnvvjMh/G1rWoXrSbZkWsqaM7wJtbrwACGj1CO7moLZiDpd8XaPekwNFUez6xEjaZ2rtILsJdgj77Dx1vBJwrQX+tAYiU0WmRlHk1Dw1xuYe0hqDg9HKTdDNxybAaE6c31SuTaU7wqMFlvKPkfHCjvRhaCdUYFRLzKKXHZluzxKNCvkuE6uCIjdTnQ9rGPMtnwyW+7whso8WDkuobssbyoTP8lOeU+sgiT6tSRLHX2ho3EPJ53AyEbgNmJbDzgJoBuXoX1W4LSqry1lD09aMPA0I9MibUr2GmPGi5nGSc3G60wrRN64ekvdZYB1zaUeiUQZN0ZxGWl3UKI6PUJuBnlUQ7feTd+CUsWKHZzaoQdoNbVSFsnq4/6OHzGCWWtWJjeZxVCCSDT+dk1NrOrqo3ogSMXa9qSrR9yRGGTuxF+HUamklUrSS05YNSC/0ZbOit2O58mUGHIGWosiVMhtn7h4cTOcpgJbBM9JPA4zTtd83/VQEGEqpHs4D7c9uuQsKCzOA9tPnOym57qqRad1lpyED+zxxiSsB0oH88v7JcGYAELvroAhdO5ByGE/IY2HV/RK6g6jW52wisPkK54oyuBkuINEWeIbfWYqfWOTGAyammp7PaF0LlgiPEzYcaRSdFJz0CpJ4VVgCOuY49v65CzhM9g8J0yF7HN6imF7zxKGAiotWUrBashwsFFfroarFLf2GVZHVuo2Y77yGd5nMFUHW29zxdhotPZHtd9uT8F0K5GllweNQaNNWRCMrKwyszscSOZSm/7Kae94ijfMLSxxOE/2TX7Xt6ADEE/ahhK3MrsjxmNxoO+w7wU+M5lVFVDU1dgJ6Jqktpd+Q9Cd05nNwEAM7lW0md3svSgDWkUx+EJDhd7b9NBueLk3zII5cHmjtRYaXZeBmG7MOKZ5tDvrsGt2yMTUB0y+s9YBHzR3aPDWhVR5Raft+VSV27V15AWUHvTA3kgbL1XxE2CSbcWO8RqXxRu745MhZxM3p2p6dV5v6fTmb6sdSvs20xvU1dqOq9FxQV1Q+XopWTiECCxc3pCTgAm70r/ZLo+aHQZJbk01/a6hMZN2W9XxzGrI+FsCE1RHOjgU7ANaQPMQpiTW9AY5dHF5VeLbmzjS/m430NaBcjQuyHFW2uN84tLQngh6OL6oJ6EOxiVEGUe/s2qcxZaF33YYidMhdoD51OD9fUD2QufqCV+GDCApdoRGT78XhFNpQxEHppvBWkBpabXZmGvzzuvWKWSlyxDs7s6KP640M6rjmIURz0N8eBOWLSV5N/Q6HVe3U5iQDut0bCZu45Lwi+oih1yIn0bociLsw6YPJQmzac6mO3xEB6kE3TG8lWRf8js8PpODkLqhn5V30yf4TPAo8xghFwJserU83uf5yEsnVfG33RXdLHt4IHBCAiRArG+nYMnxgcdFxP0sNtKBoNFzXuAsLw9mE0rbFnIngi5UREWMLB8vt9PIsm8f3uYDq9ex0//9KzDzUcD/sxOJ5+HB+zn344THt73PD12f/xs2/vThrXFjYOHzXKbN+vB1aPEPpzIf//I55yxuer538n7i9jzQ6+xwfnvzLS68vu2a6WtbZo9zcDDD6dv5Ha/26+tdiG+HWF8f7wCBn2UX+Q34/qO/b/MrWPP5tu/Fdvf+M3ydW314816vaHydQ+U31ez46+AU+It/Qj7hb7/+b4U4ZwNuKwAA -->
