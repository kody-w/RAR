---
name: "rar-cowork-cookbook-configure-plan-workforce-development"
description: "Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_development", "rar_sha256": "c9120f25a701e6a60c67c89349f783f03ba384f7a2962c321c7a56fa87495135", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_workforce_development`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_workforce_development_agent.py` and in the RCI capsule.

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

Plan workforce development Configuration Bulk Setup — Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 c9120f25a701e6a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_development_agent.py` first:

```bash
python3 configure_plan_workforce_development_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_development_agent.py   # or on stdin
python3 configure_plan_workforce_development_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce development Configuration Bulk Setup — Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_workforce_development',
    "version": '2.0.0',
    "display_name": 'Plan workforce development Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-workforce-development',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-workforce-development',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f2f14dd7f2fb7d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-workforce-development'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-workforce-development', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePlanWorkforceDevelopment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceDevelopment'
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
    print(ConfigurePlanWorkforceDevelopment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bOb1rbmv0Kf94OTh30EYpJ861Y1QgOgAQESU5xymEHM85DO/94bSefYfrl5fdPVVa3EZSE2a/jWWt9ae+PfX8ymDrLy5fOL7JoptDPjOAzcEjJTB2KyLisj8FcWWeAPZGdpXYZWU2dl9fLxxXEruwzzOsxS8Did53HoVpAJWU18X+uFflOa023IDszUd6E6g/IYaJnEellpu5Djtm6c5Ymb1pBXZgnQC4Vp3tTQprfdGPLC2P0IdWEdQK0Zh85D3GRcmcWxZdoRVDV5npX1K7DI7c0kj93q5fMvv358CcH3l8+/v9ixWYGfXpinSe4Z2KC+mbD+ZgGQAO74YGk+AFBScJ27JViVgJ8c14OeVz9Vbux9hP7zP6POLP3q589fUuj5+fIy/Sc1KVQHk79mVbsOZJu5aYVxWA+vEB135lBBpVs3ZTrBVQFMU//18eQ3SVkO/XO699NDyavv1j99ecmACXcMvrz8DGUl0Fc20/fXSUr+08+vcda55U8/f5NTNdbNtetJGLD69evz+ikWLPy2NPTuWv8JpD5ia7lfXr5zbvo87J78BE++vN6yMP3pITgvs9ZNzdR2f/r5r8TagWtHcVjV/5bcXx6CA9d0gE9Pw3/+eAf5Vwh+OvQu86/VTkn3dzwBy9/UfYSeQP2V7Dv+/0V0HKagEt4Q/5fi/tUD8D+hX/7St//ugY+Q9+Vl7cZhC7LDit3P0O9f5fOG+eWD8+3HD7/+AUT/H8XIWQOqYpLwNTHT0HOr+uvXXz5U958//PrLhyYHueaaydemjP+VzH+F613PDwg+V/3047NA/zWN0qxLofdMh37P8v9R/vEKKRMBfPu9+gx9Xy/TB4YmJ96UPiD4rmYqYOt3OP788gcgiRR409j326DK/+M/oGNol1mVeTUk2xkgIhDgOkzcyfhLEFYQ+H+q7RLwRlmFANjnOpD/U4QnizMP+u1/2nf2/GQ/2XP2xojuPSG+vnPg1+848LdX6AJkZ2Xoh6kZQxJ9Pn9JTX+iR6A3L93KLVvAKNZQu5/A45+mL4Axod/+HfFf75Je8+G3O4WGD5aSGG5iqKqJ3dfJSzVw06dPNqBjt3ftBiiJM9t8EHL1EXhfZXELGG5CpIrCOIacsATuZ+XwoOcm/TwJ++233yyzCr6kD0rFoEfPqGZgwbs50KdPwDUvDv2g/pK6dpBBH37/4wP0v6D/7qm78EnHGfD7MybAQl4WThCosWbyGIQLBBgQyD0mv//xBBiISUGTAxEMvalpTQ+DHI1c5w1tmaU/zQkSslyAIkA4mXoM4GkorF8hzoPe7QVKp1sTkwdZVYOOlrup46b2AKSawJ13JNOshiqQiJU3fISayr1r/c0qzbuJCSh2s/4NOjJn0DeyeGqW5bOPgIezNATwv+fC43cgpPxQQas3Ea/QacpKKDdLMw9K86nDMx9xAf3i7XEg3IRSt/uSTl3SnaC6l8gDHrAIIGM/Q/ppijlo6AngA6d6031fY07d7XLvcuWXtHqmv1lOobBBOwBK/QZ0bdAU/vFMqSrImti54wcsnSQ9o+A8o3LPwfNfjwnMD5PFaho2ZEAmOfSlmSMoDv1/H0Qm++ndTtrs6MtmDW1OF0l/4DoNUJOCx8wFxgEIKH/U0LcR4Y1g3nj2SxqHIEnK4R+PlfdoPNc8uAsUvQOoQrrLB6kAcJ3k3jN1yryyvOPxJX0j9I8AnDt7ARdAWYO0nxB5UzjdfbM0ALU7XX9r7vfIls7kOshGKG+sGGSK57rOHYQ6KKdqe8YCpK07VV4XhHbwg1cQkA6yA8iHgBEhqB9A+nfoThlwExTaPQrvy8NpZAJWOI0NrAUTqvsKqaBgpqSpQJWCuWdaA1D4cBcFJS7AGJj4jnAVmPnDmGmofRpoTrHIEpDH30fgefNbit9tmcwHUk0Qe4BlN9Gu4/aPyL7b+YwVMDaZivL+0I/hfvoKfd95/vElvdv4zvSg1uOpaX8HDgRqLKnuKTdRVQXoJnGfCQQy4d6fXx8t9tHD3235/KdJ/qe/N+zfm+b1x8h9hoK6zqvPs9mj0b31uVdAFDOQI2HuVt963qep3D69l9un78rtB9kPqD5Df8++H0Q8E/szhL4ir8h06xDa7pS5zw+Ag/m00j/h090vqeR+i/MzGSaqjQfQZN/7ztsS0Hz80vWnxY8+VE3tqwMd8068IBJf0vdceFbKg3NA06yy7yr43oBBZB+Be+8P4FZaA93ONLb57rSriSfzK/flc9rE8ceX1Ezcf3M3M/UBkLEAkGkfBKoHTEJ16N6v3qei6eLHrdy9rgAhONnnqbw+3rnyI/Q+jH6E3rYH901X2oD90S/TIDypBEvBX+9r3/eJlvsC9mT1kE/GP/Y80/z1nIv/bMRUVcBi2516e/ZeppPGPwkBX3zfLf8sRLh/MeMnV1S1OXXqsH6r8ArY6TQTswPcQOWBYgIc2YAH/qwG6CndogEt0Znc/YbfN7eyhy9/3GGoHxvH31/eOOMZg+eQCJaD4vxUTU1xBlIVKATXj6QC9/6vxsenDMB0YHQBQuwlOke8OWFSCOqSJonYJGUvlhi+9KgF5iGYZWIL3KPM+ZKc29gctSmTID1zQeFLAsUIIO+Rnl+n7h9Ods1N017YFIo7S8okbRdDLMx20TnqUJiLEEvMWyxcHED0/mgEaPLp7MO5Ccn3SXYC5enz7y8WiYOVLF5x9OPDzJaKOZtTlhQcYA2B+36GBw2hZfzJKdeLMr6enN72d+bpsBqVXm46huJjS0Qli7eRrBSOJ4YlV+e57JLWXJnLWSCng7vtTGFNH1MHc1ID9s7nUxhtxNuWSI+Ba2Vl7m63aijt80bZmleT0DS8GLktVhrK4aBKMglbJV+Cki3yQJ7NvH0pMNjhwlS3nAty7pQYCdlHbSyHh+hCWO3uUMT+4SYUC2uX97ObISXKLbtssI1U26UtH8dUyftjtNwqqmQc+FOpG8Vw2Gcky6FCOsIzgV3CcGMtikswW7pWCKPMQpVTOWesvipiTTK1srTXahYTOdfzxhAH6ZLuZ6hxs+O92cTb4XwMUK2qM7gOTvz6sthuiCKywkIJs/bC9HrrmHixLdryehgyDtyYr8JbbY+omMckXZ3t4liIcJxI2u6IlsIOy9BdSyCFufVQR6nU05BchT16LfZmcb3dMGYxWILDcKpcKItZmm0ZOaU4ZjnwerGd73sE2ELc8HVkRs2wki7iSSNqO79Vis6OxLUuYUwfLiCzKX4xZzzJLq7FFi8bpdxoCrGxNotTuCOaNa73eoT6xfxydWvdRvdxrF9cPlei+WWmh2iJWjZ5kzvlxnlpoahMzek4o3gHRDTUET2jaFoMqL0gVkjR6ADGOMawJjiFtXbVxh3u3lAfa2SxrGbueDkanbWzpatZF9YlhI856u2oTYFW5ZYZe+/EBYa6mXPyjNL3N35ttStpxMtQqIyZrcn55lieK13dzZRbaNMZ0Z64ftzuDX1xWxAk2RoJr6CkaqRGF7XrVU8u9pHKL3wOhHrk4vNxVOOeL+bhRat5xfDqgyZf2EF3UoQ/ZEGKJyzOsQMdqUskCwMOu8A6nozk0vMu47jBm5hxHAKbnYx4uYf39XGTxMOysGEGxJXBy9q88JtLywfCVa30PrA2mbs7XCV8fWDwrDC6tbqU9tot2gh1C6/TM7Ms9AtzRZc+iUoMFqwW6+4EVKfDXsq3OJcQrMPdaJ5pN8qNvoiydrCrskiF9aazZYHAgA3rEh7aPCFz7CLIYhggci2Se1dcGEK4PsaDFm/69nK+zuedu2qJywVnoriWhrg0LO80W82TNsbR9bVJ11y9a0tYk/WzpuzOa5FjzHkkJ0PQ6s5lIeKW34lzw+d2vOWfRmzdY4qBkJ4qeSJ7KXyZcT1tpTVH0NNsfcPEu4LNZihhcsudR0qmgOgJP2vHrTbwSuwKxHUoV7OdIoEBVG8vao3cFlgU021RamE2CBKKzAUeI5hcIxpnrxzzM2cJ9XyxVPc5zZ0Iup5JC5guw6q4qKvCmW9FHjtJ515o5hZ3CSXUuWSxeJPhzMPlGG+YrDQPjkWhPXN2DUSccbiutpyYWjV6ZIphnlZHHgmvBF+GvE5W4+EmJXbuq7lJilpRRUg2RtfM6s/HVbSzKOwG50l5zVfNuBgER43ONX+KcY8gzvGVrVj+Ziir+NTSjgXjzcKT95fTtSmHtlotSYZewjOKMwLY5io3vY0VLsbnwQ/jm6VKPWyv8UFaH2ZicCPFbEjpvtHWldGdNFTywwN6Q+OK8+WKEvqT5zHzkdkbyHVve8LQO62YGKc25UfHWKiuZTqcW9KlwQir25Co4UmZZfMCNyM6JHboSuTsKOPkyM3XiCUq7R4r4vyEX312QLIszJmC1qJYsrJ0oR6Ph7BnxGu42yxG6cIXErKcu1t6YS9XAw4IPDVsURfrVOScdD/Hl+FFYNpwM5blcLHbsSI8zSAvMs+UXRLajlf31yjeHZzJTtaNMNqvhBsIJAHD/HF1O2Eoe6gOm0AMtKFzDxIBp4Xh4am3MNxs3cvIXq3GOFaX5dqP/S2zyaMgNc+8YFxFWXFLVpSN4wpPLKrhM4lqCzok18rl0DH+QuOaIgUubPNzakoMHbDrpDDR66HbrugFL4ZzerPUWVTZXo2qR0XzTDkCiW9F5sp6l4Lj7HSjESuYty7dTvW3m/qIkTaH8gIVpZzgNQoNitlR6cWuF60TSrTygjTLUEb3yrh3I2UdEBeSNWlaFo3kuLTJAQ6QGj5u0rBU9QFPdH+89GyfHepRZWsyUyjnNlxlYy2Oa2lc0WHMX+0FAvatM6xz0A3FxdmQyzor1quFl3XM5eYLYS7C4d4Gm22kdHSPs5ks8Y+KxojMWY1g2a9uFipt0iWJORml6IAwAMfPBoa57hbCuKeSzHPzZRcip3SbXFRWyFSyik0m1ys2TPa4xPjp0Ld2er6ZoPWx3EXcqy2q7dZxcN6cBts/zvOkGA345EtwonEK2yvadcYz0SmhbfG6WHN4pWXB8ZQmg93uxVK87k0zGiPBOzRRjHJXfCFcKinuIv/Eh7hWn9E+r5XI2ajIjV45/F7PJEajsDJWj4lpmmGFbB2pOWTjlYQVkV2MS1MPbDvdI/pN1aIR1kCs1bAvaK/BmjhTQkNzblf9xvBYr1a1bSkzSUcIpsQTIyxmOSJHy50cRRKaHGI4mB3xqwArycpOV66ihrbK86h0cHw04fMi0MPwJuKaJDo741rjDN1FSGy5OEk1nnzOMxGhCYSdOZlnca0akXjJZmi1OInbDc01VF8WorGsLtfSTtBo5roh5REDbBu2eePEnKO1cJ1exrJBt7bQIwvi5HY90VaeXJLDwbnc7JQ6ahwZi8QcJtAlzTlnlduM563izKqg4AJ6JfqWtm67lb6Vhir3PTxE5AN9NFeDkFWtRsy9a82h8UoqC9vRvNN6bfCYUYCFtinGJbovIhzOr53Hgrbg56jeunzh9FxvF9nQ7OaFbtr4NtU3dLc78hivLhCG0U7B6SghZJRtHDvybI7ZYnrhB+NYkTyv2nRuJyuHCxICv+4DxOv59qoI83pIwi6VVSfaEsfFNrfgLmjYPBf43S606mJLG47jHPBYQE/G5YioEafAMROkScMuJSbirm7AwjFedAOZXXJ7J6PXfm8dMW0oL8UcLwihTtwNbngZxxjInEksJEcvMa1ySG4Jh6zUC6HY8VKyHHdKcpB5y7O0ciPMpETPlULr1pJLrp3AWFjGeScBPE8JxTfH+Sk20azK+VKdocfNDI6ivBD6eVDminAg58LGwfZplqSeXSyqI+YFK49pzHAPgNr3e1vzpf0641JG5LZWG3HZbrhV1l4viEXs6sNe280r2qWL/nZK/JSUdtqCHPXqTETKraXolGxcrLRGiVFWyhyPNgi2NbPw6vNGsSy71GeoqBvotUochsUuj4R5sV/HlNoWB6TYXIbwLOORsj9pRU+ImsAmaMhypXHlx8TFd/J2Po+yHbs1ojExKUKliQbMNIl+DQ2+muODnoaLJVITpSiv2k0rnG5nQos8kz2LBHnl+EtBrMaLrxTsbauwxpHG9Fw/ZQrWe8HRIKUVigxnUZuJoTDMj3WYUtnYLN2NHByOzBlujK3J4vmhvYEMKOsir2E6Wd3izba08tTU2c1i5fiqtY0aXNkqWKvGpU9FeCQsTpdVUJfOeY/vC0Khwh3P6vra9b1deAOE5eqllNSqr+53Ft8psHMQTc8d5VHqnKu+1ult1hlKmaerueYijc9EW/x6OYb8sj4YIV5zpWju0+PRiQM9Q+o1nhlq2437Kpy7ANs9omrqckmc2gbhqBOraSgqXY4cHc44tN3yascuS0XCspHO/JD1lhJSIdZcxpgZi8+cQliRywI9eFQt9R6a6nI+q9Y+3MCzDLRql/Jn52DIMau1WQarg46VhUgEm5lUbAwn7/Z7B11umzHRD9yM7gh2rC/zc1PMfbjoLVGzSkAf673M3Q6yfpWlM8zmPWgtdNr5Z6wHRp3LEgyrC21m1weVzqhsNbsQKMUsdnC+x+fUJiXn27zX9wJFj8a8xjc5NgvRbYCTFeUNpd9yq1o43yrBEQ9uX/dN1Q9nFtFm1FLyFj4rxeoutVMM5lIwQwrkgiLS+VL0lpHbxKfgrJsJZ6ukHHT2kl2t2EG7SMuqW6gesqmiTmdqe+ZyS8663Iqx25yEM3fe69iq2vQDS1RjR2JxkmwxK7aOsy0NdmBDg2XmedUBaMG+y+iK9VxDqCFlhWO3Vw1W5uPtYm1fcbROhq297njKgw3cn2lVh7G2BG/UI9YeqdUabxu4KokdAWOJkq+3mp8jsw3qDeLSRXbbzDge+cVpvGqX9NZJpT6bH64eRVK9NEPb2XwnbMBIWy6Hk74qDhx7G5eHm+/OwaxHEQlf7VrN7NyjpA+0ZavG3CtNV0tgCxWpkWrpQWrRW3JKqZxiqZYzaj/KuuOsIuOo2xIwXyBXv2dQod+QIYUOTnhOM9auPXiJS7RPHXUtJQ+BjPX7wtbWaD+jKdn32OOeI+z9ep2uLJkPKATMp5dFb8zR/tAIVQfbq65UuTQ4lUeBd1t+vYDXqwxxgt0pOyu0E46qjGG9M7rSekWru2TFHzeaVqd+dl2zrrW+7sBGvUvjYtmIEXUjFEDzItjhz9Ykbak51ZaVbGM7S1hXaSvJ4xE/E+0KvlIXZ+POhlQOVm4zjoynbUasm2mISZys1FNvXrsJpHVK7vSu01DLt9ibb+1263Zc9juzs1c723EX5oLBduVZ0Z35kSb0w6oqhEZTcW25LjPNuFIIJmOuVavG6lZgCtKzW6xesRnlMuvjWaS329mFXGkYhuWIvrmuid2ZuJLnIdtq/OLM5uesGSzSV5ZbV8DrExZs2x2NCCSs2+fVkrDqtrx2JuGBDAhJh0Bn/HVzxKsjjKELEl0PPkWccXeQYbzOl6XutMo+IHibb9pBHmq0OTc2Ziy1ttMowt/4VOyJDbZQcjK5XrgdG7MJx2fd6cwUAgGPB9S0b0yxDHa3XG3nfgFvqHnbB+Q253j/Cmq48doy16LtpoSN9uwTjm0QyY6K0DEcduo8gdeFqI54BfYmiIsIZzH2Yb9z/Uw0fGUHHwAmRD0YclsThA2noAehlElladvPOZRjBhfx5mIzDiidVrjH9qK2rS5Y6LVH9kgfWGZrs4DlLwx7GoRicWtRI+bGbH1kDWO/WhNKbS3366imeNUnXUIiQQ6GrnNzbdZbY+WIrA7tieKdG9bujLV1OOQCSKFuOS48vxlmPFljnHzjLrcEHZNA7pseL3WwX5VX1/P8oJXrPM1bg2bPJGGven9HDEdhVq1kZZcUBMOcbjkqg4mpI/PFEAyX5oxJHOV66Glkz8XVKh1Sz8+lexa9Y+BEB/RY0DT9z5ePL9MJ9vMc+m+9d55OBf+fHU4+zhHf3kvdj6Bd0/l81/X575n168eX0g6BUY+D2Cpu/OeR5X85hv3077zRmCQMj1e602u0vn47uq9Nf/q3SS9h6jRVXQ5fqyxu7ofBH1+sppr+kUT19Xno/XJ3Lsknae9KJ+iz0rXNqv5aZ1+fh+1hOr0acp3QrN3npf88m/744gwgUKFdfcVI4qtb5pOvz1ck03Hu9I7k5Y//DcBT0VEHJgAA -->
