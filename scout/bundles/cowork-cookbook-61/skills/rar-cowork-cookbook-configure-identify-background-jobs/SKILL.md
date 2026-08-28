---
name: "rar-cowork-cookbook-configure-identify-background-jobs"
description: "Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_background_jobs", "rar_sha256": "e166b6139f0793fb5662220dd3c954721d5ace5d556e7d4a38c54fe8604de596", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_background_jobs_agent.py` and in the RCI capsule.

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

Identify background jobs Configuration Bulk Setup — Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_background_jobs_agent.py` and embedded as the fenced Python below (sha256 e166b6139f0793fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_background_jobs_agent.py` first:

```bash
python3 configure_identify_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_background_jobs_agent.py   # or on stdin
python3 configure_identify_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify background jobs Configuration Bulk Setup — Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_background_jobs',
    "version": '2.0.0',
    "display_name": 'Identify background jobs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-identify-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ecb3e8a80b33384',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/identify-background-jobs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-identify-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureIdentifyBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyBackgroundJobs'
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
    print(ConfigureIdentifyBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZOj1nb/KqTzh8dhpsWOmFevKloQEiBAYtHicc2w7/sux989F0ndY8fPeXEqVdFMVws49+znd8699C8vZtsEefXy+UV1zQzizCQJA7eCzMyBVnmfVzH4lccW+IHsPGuq0GqbvKpfPr44bm1XYdGEeQaWL4oiCd0aMiGrTe60Xui3lTk9huzAzHwXanIodNysCb0Rskw79qu8BXKi3Kohr8pTIBUKs6JtIHaw3QTywsT9CPVhE0CdmYTOg9mkWpUnycQBqtuiyKvmFejjDmZaJG798vmnnz++hOD7y+dfXuzErMGtl9VTIXf31GD5rgAP5IP1CdAREBYjcEgGrgu38vIqBbcc14OeVx9qN/E+Qv/2b3FvVn794+cvGfT8fHmZ/h3bDGqCyVazblwHss3CtMIkbMZXaJH05lhDldu0VTa5qgb+zPzXx8rvnPIC+vv07MNDyKvvNh++vORAhbsHvrz8COUVkFe10/fXiUvx4cfXJO/d6sOP3/nUrRW5djMxA1q/fn1eP9kCwu+koXeX+nfA9RFXy/3y8hvjps9D78lOsPLlNcrD7MODcVHlnZuZme1++PHP2NqBa8dJWDf/I74/PRgHrukAm56K//jx7uSfIfhp0DvPPxdbgLD+FUsA+Zu4j9DTUX/G++7//8I6CTNQBW8e/4fs/tEC+O/QT39q23+34CPkfXlZu0nYgeywEvcz9MtXVWFXP/3gfL/5w8+/Atb/lI2at5V95/A1NbPQc+vm69effqjvt3/4+acf2gLkmmumX9sq+Uc8/5Ff73J+58En1YffrwXy9SzO8j6D3jMd+iUv/qX69RUypvL/fr/+DP22XqYPDE1GvAl9uOA3NVMDXX/jxx9ffgUQkQFrWvv+GFT5v/4rtA/tKq9zr4FUOwcwBALchKk7Ka8FYQ2B/1NtVy7wax0Cxz7pQP5PEZ40zj3o27/bd+T8ZD+Rc/aGhu7XN/z7+h3/vk749+0V0gDnvAr9MDMT6LhQlC+Z6QPqSWpRubVbdQBPrLFxPwEk+jR9AWgJffvnzL/e+bwW47c7eIYPhDqudhM61W3ivk4WngI3e9pjAyB2B9dugYgkt80HFNcfgeV1nnQA3SZv1HGYJJATVsD0vBofwNxmnydm3759s8w6+JI94BSHHr2ingGCd3WgT5+AYV4S+kHzJXPtIId++OXXH6D/gP67VXfmkwwFIPszHkBDXpUlCNRXmwIyECoQXAAe93j88uvTvYBNBpobiF7oTc1qWgzyM3adN1+r28UnjKQgywU+Bv5Np+4CMBoKm1do50Hv+gKh06MJxYO8biDHLdwM+N8eAVcTmPPuySxvoBokYe2NH6G2du9Sv1mVeVcxBYVuNt+g/UoBPSNPpiZZPXsIWJxnIXD/eyY87gMm1Q81tHxj8QpJU0ZChVmZRVCZTxme+YgL6BVvywFzE8rc/ks29Ud3ctW9PB7uAUTAM/YzpJ+mmINGngIscOo32Xcac+ps2r3DVV+y+pn6ZjWFwgatAAj1W9CvQUP42zOl6iBvE+fuP6DpxOkZBecZlXsO7v5sPFj9bp5YTiOGCmCkgL60GIIS0P/z+DHpvuC4I8stNHYNsZJ2vDx8Og1Nk+8fcxYYAyCQWI/6+T4avAHLG75+yZIQJEg1/u1BeY/Ek+aBWaDcHQASxzt/kAbApxPfe5ZOWVdVd298yd6A/CNwzR21gAmgpEHKT/54Ezg9fdM0AHU7XX9v6veoVs5kOshEqGitBGSJ57rO3QlNUE2V9owESFl3qro+CO3gd1ZBgDvIDMAfAkqEoHYA2N9dJ+XATFBk9yi8k4fTqAS0cFobaAumUvcVOoFimRKmBhUK5p2JBnjhhzsrKHWBj4GK7x6uA7N4KDMNsk8FzSkWeQpy+LcReD78nt53XSb1AVcTxB74sp8A13GHR2Tf9XzGCiibTgV5X/T7cD9thX7bcf72Jbvr+I7xoM6TqVn/xjkQqK+0vqfcBFM1gJrUfSYQyIR7X359tNZH737X5fMfpvcPf23AvzdL/feR+wwFTVPUn2ezR4N762+vACRmIEfCwq2/97pPb8X26XuxfZqK7XecH476DP017X7H4pnWnyH0FXlFpkdiaLtT3j4/wBmrT8vLJ2J6+iU7ut+j/EyFCWQTgArje8d5IwFtx69cfyJ+dKB6alw96JV3yAVx+JK9Z8KzTh54A9plnf+mfu+tF8T1Ebb3zgAeZQ2Q7UzDmu9OO5lkUr92Xz5nbZJ8fMnM1P0f7WAm/AfZCtwx7XxA5YDppwnd+9X7JDRd/H7rdq8pAAZO/nkqrY/QNLV+hN4H0I/Q25bgvs3KWrAn+mkafieRgBT8eqd93xda7gvYhTVjMan+2OdMM9dzFv6jElNFAY1td+rp+XuJThL/wAR88X23+iMT+f7FTJ44UTfm1KHD5q26a6Cn006oDoIHqg4UEsDHFiz4oxggp3LLFrRCZzL3u/++m5U/bPn17obmsVn85eUNL54xeA6GgBwU5qd6aoYzkKhAILh+pBR49r8YGZ8cAMaBgQWwcFGKsigUZzyEZnDPIikKwzDEcXCbIQkaQx3StF3SIUnKpR3CxOc2SXjunEIIxyUZCvB7pObXqeeHk1aYadpzm0YJh6FNynZxxMJtFwWsaNxFSCBlPncJ4KD3pTEAyKepD9MmP75Pr5NLnhb/8mJRBKDcEvVu8fisZoxhznDRGoItnCHMcPQoP+FXOks5TVASdHw8Xx3VwRTRsjTWCvKF56s8sSGChb3jM8NcXZRY9fbxTLM6rV4sVzHtlJ4W6i4vSDcXb2h4tjV5YVdw2k0y0G1Jbi7JXkRdw7wU+27N8ZuTm57kwtDniZkiu7nZ8eJcrwxNTeCZF59tozy1xvWk8tvDoSrWKUUmtSGEUix6w3m4phfsEDjLDeZo4YzDSrva6u213Jko1g3X895xzYt6GguNJ7Qlxll1dDSUYytpBXDlOYNJRUNhzQtnSlYlt9l+kFt0FyVltgpinWKkwm2bE18IKNc0R7UQUze0s5bruPoomW4jjDaSo0iclDCyPiJBuFzuDhKXOcYq10SE8fYArVaoPpxQXBmkvRkJrWBoW3Nkd11iIpm+b40yHPmM7BC2aoMQX9jV4UKijNBSLjzuE7eM2VN5FAxVxwyEPnKuhKStTm90oVVoFGv6UfJXgZrqe7YZOscCKtvwohgr0WNPLLs+w1vDOXBnZe2S54q/tSdMtJvNjlCwRh3F5JRcS55m3HGTGNqJ53J802trk5hd42uYU2vLkg4lWpIJpR4GVD2JfJzNrqFUoY5NVWavJzsvS4/yqlhc6JWhiIh2Qs6pVlaWFAvkHF/nmn1QzrIodimjeayV2m0pITAnbmo7Nsxr22WtPvgYS0R5YhlDxc9IqyQajm+kuqJX49ClYWEgfH6oZkEkzH07tjdnRVPSfb2ZEW1o+GE964+sCaeyfBh2oyvoWimcxgFekxGKWjf7RFVxTSu3hHdPSsnMUbW+pcsjHKjYdX+4crnZp5UZOCe9LysFk5NcjMh9ExFbes7f5l5W423vGhVtlOruzHiwH4pKkQ9wesb4gdnwaNOdTygFskAhgYs19XpClUUc1wbVCNXFJ66Bcj1Z6YbH9teAFOEjBcBDG4mM22V7tu80OaauLJmJRkgKbN+IvClwsZNx7XCqOYE9rl2BGFa+rfZuWNTHsyqM1LF0Nza6MfbpmIk7gqeDQdpuq8AB+LajZk5hXpeNhJB5uJZdUd6uuesFHq4uq6vJyOwSd0MWKXYdMcSOusg3pH7UY3o9K9YzG9/JehQr/I6FbwtvPUvKVtxevYhnT1wWraXqklpwZM91dR/PLyGL1tYOdxOYxZX5dqOhnVpIB5rZWbIkVsdNt3fRUMd5JfbFtlzY+Vp0YLxLGPY4uybN5VjaWNfBmTI3S6G2RRGNBbg4FU2m4nhBnubF3FTVuKuqcwiPsiAh2JInOF+P5mib7DCj1o3zeXvkKl4fd5vNqlOOczio7LrUjpvSaeOQV+Q4I2LD2mNWeKYpf+ATLpa0mV8lPimU9U5C29pTBma3itbWNkpP+GI151C9X1VieRz6TBUObNz1RlXiymbPFWiWbLibGjLHZIPMbTVYuUvHuwWKae+9G4qeIr7BzByx97J+bgYpILKRZsd6tVwnC8zQKZZGQPLq6FKht1JK6hp5xq9Mu8YYckZhjEL2B4kaXe12jvggL3q12Z6plZmR/boaELZhxmV+LaPtXoUv1hIrY2OtcyNp1+6ucYjVJrvC4nHdC1ubHTM+lWeuZyHM5RboYXQ9S2ZW1CFu47594E9LqlcWxrJlR4s57hc77rI2R6eIF8mobgPe5iT62FAnWmwP+2ihI4vGUmtho18LYaYnm2al6HTTl/rOFjK/i08n4dZG+oLBAy/jFE9ueuHIY1x/kk+3RGciHruQV40UbX7lICgpdRlJOQrOoFo4Lsv8ZrRyhxG0r0ZoCUuX85XesgSxuSLUVVooeBPFNt+6hOVox3UMqvJknnnPU0+ztvDsDp/NyhFm8lkg6dcGcYHhaYKs4ENCFeyKk3ZMYgWnRLVQAGQaHzt0Ct9iNKFCvHc3obrWz7d+49QWX5gRX2q8oHSqHQajAksbDqXOrsCs24SR61FZnel2LaRNui/XCTpmzDXlCpHOY0d03GOrN2Fz4C7O0NB8pnPkRWrV/fwUrPNb5hNVhMJNM163GmrqWMQ21woDYWHHGa+5i/RyxmjhLNt05d20cNPbQ3pTDDYSuCAQZtLSGQpejjAivdScGt6ycjvjFnoUwnEuJHXMVI1ka/XRHUdzH0r1gAyH7kbtF/gaD+Lixp4YHbFVyiha5cItjZtHCNpyty6ig8dfToYxlqkGz6x2vm7rs9Iki83CkrfH6HQu1ZCu2B3n2Wy9rja2dsLb/ETVib8q+nob1gLaKDqhShSCwmaiooXR4wf7sie1okC2uxUcmPqNGs12LkgZ1gm+lY3HI7Mx0P3eJzlm2QmCu4zzk9Yb7WkUHBkndydfMtO0sOfrzMBPmqlK8iL2adZk1KvE50TWSPjQeBWCykckEg/S8nYplitTpKvkuE/M3ozqmPeOLl3SyMgYfkXSmpoHTZiYxDw+Zciw2o5p6Bxqs98yDb2j2EN6wS8kt7utnDlKbS8bNEMOknJI57v8UmwZOdSzvNf9Uq4HTUE6OlkFs/Gya8d52SyovepkIUevOxYrUqMUZNbq8wIh6rDw+nix4EkZWy5RvFFUReWurO9Qa69FuqY6VxfHNiLEkt1TuVYWpeb0OJqzDCaE+v4GRlVR0RgcIT2YYjlyvtuvDud6nWm3rsU2Njwgc1Jye5Ksa+9cqaTUFIydWfvzZTSOJO6CUWOxc5RzzxLKhpRmyMFga39R+NLgE/OduBTkI1mvSe66kZpDl7oRLJ3E+U0qsbk5LoKdVGrGngsihEWWaOkR9uWQNKhQxtQo8H23bPe5eqCypNOZFZXorYEQYeCUWy6WF4O/XOjLznHGsZY0Fsww62IuB8oOmQ9M74/nKDjK666ypWV8k1l9b7E5u6Mdp6h9xEP5jr3u2yaN+4O2qxpiW7em1m8QYtBYIjzHndguUeag0wxzKXzDRXT+UCPcXDy3QZq5JuGi7OkQ+Au11M0q2xZBGwwFfdUum3z0D5Us53RIxzDi5J5vpLnPn8+WUHYavhH05bmpVPxgCLFZtimvGCUiplooj4nh0VrHOvtEHoha3CpH9bpmBJJctSJaLUh0f3U4zaVDczbUxc4yZmgd08PR1PEzgd2qdiNHHD6y2kzAd5XYtZx8ao8MsTsnZ+m02ZNETCTbod81B0M+EKthHzM5JSxXNSOEwb6dBfqudQ7E1grExdbbLwckUUxxcWqtFEyOWaNVZUIvb/hVsbYHs5PWx3F3BUM5FQqrRcJWp8pxCdHO3OsO262IZokfVg3XavvsiFC8nywoRw/G40bGbF+7Ep6lLm07AH1GQLCtrPeV6voFYQQ3Lq3wtC78NncRoUy4zLT40vaXlDfTB1eINzzug/mGjOfYlW2XsbR3E3cVn2opoDaHXBYMXUqHtb5Kfa4CA+x2dbn10WpW+LB/OawVfGeHsHCAIxk3Yk2Ik8MOHukkixmWYgi3ObaMZMjdQcfqix8g1UKkx57mFkt4yZfWxkaMzQXFt+qt3w8aP/jhofdiE9fG4ibo5SEuQh/mVv1lxe/8LjsorVDfTuJhTa7lmpRAX0CwGZ6zPrrPnP1KX6woWzZooRkcg66tnC2WrioGEc90Z00cLsdThKMCuaSVdb/M6S1/7E0/U8rViqaCjDPGnMDL/WmcEQ4VdWVZ1l1qsPpSM9swnplw4KQ6g+4uxmJ1vd0qGQ19tz+RZ+K2pclNp4hlpTazGkydvZAOpIab5yUsw7MoGi+ZM+ydkdwzc8uSx2btOYMD3KWK9S3CsnN5iQA0yH1oKrzin/bROSxwLSqLuNMujC01sauRWsr3YT3uR7vLgrU/eDOLXCPH3fl0m/diat2IGru4Jj0ulgXMTvsXfj4nwnoPF2Xf0NmawrSgJyjFXEQd0u9leXmmuiDXNrSMzekAGxZedphj+OZG4i19y/L5vAPDHcrAgz9fGATloN2MbGdRsbRAp4k9J2G8PDv1XbvI9udQ9HINocKob9rC3ZFMhvSaYc0WCXNc5lK8LvDIDzpOxnf7K7ycLfw6mqdz/XyY7/D2dAR7b2ymqfT11qVHMLaVsdDcclORbryR1sl+iHTcbkQ8kGX7BiA7ue5S7oxsBi3kEGu7IaS4s3xppq8xFAsIOtoJ6S24iRgdwOKtaUL4sJ3RdnECewJ7la7n5w1RrDH8wLZrJ8n3R7gM576rBGoTeRf0CHtVnmxnYJohzPkQq2Ay2mGgEljf07YEqF0GJeGANkuwnzu16GKeh9J+RRF1UFsu1nRScC7Lvch36/mxwit5XzkwHWhKvR9YLSNSp2aiwQr3ODdEO5XoQYdTlSNTYu7ASdgw0885N9/6iwV+Q2j7ZuvybuzA4EHMmn6JkFmzZcEOfTNUzc5yxRueGwM7o81bmoVV29X8nFgvT/W1U9csYcTMTORIB4ZFEQMkXrNw1PVxvdVoRePOy4F1LtxVzNlg0Wj12lqbh4u2QTZXc7ZFV0HrI8fQdGchC7Iwjvq2XwFQwa90vKsHFi+Z6w071MPxmDcbfMwskYgwhIWNvkIx+6LN8NQcaIqKzlfcpuXeYghWvF7HqOy55Wy+W5lze309IBIstcvbaR3to6rCI8Vf2ea8MXxcvCx75LS2dMcum6GhcE9uRx4t2zhzq+BCrr1zahSjLGYXuzOQOSFfgoWudwApRbg1mfbGzn0Z7BMBLBBlkNhZP3dj2KeFrhTOiEWQHCLDLDfz12e6Iv1+fsabFoNrbdk1IAPgc5V13XLlBxER4C3c4Xru6kdP8DZnVbu5WIYlAWUXqBi0pmxt8UEmR+eytrINRh9pJhnh821nzbtcubormFFXfOxXYZQt+K7fSJGh2dacgo2topazy+3Yg1THV00Ao9XcShfmYnUhSxMWM5yijGF9LC+nYqC2A5kmsGh5p3JujNwciw5c1S/8RqNbebHNr5i7WEhH3+avVUry9c3umYWs7QyKmy+TUvQYSjhHgA4WNyzAxN0Bv8CbCFW2Ne9uox4eTaxbwTPfOfrkboX2gbIZ8tX8FvR9WM5Yk+Scw57YD8us1PwDptOlcvCLW3Mc5xzdLZRIFKSubZM0mUU0GCriZK7TshXgnWytcVlbOdbtouGy6GDtAfYchDykclCnQ7vq85Y+uAJG7uGLLfhy6TE8LzHMTV6CBD/3xHzZhrscOWVi7w9IdNjl9lEWb/TynB35s60O0lDO+ExEujCT5mrPOtvucBgcc6CU2WI/Y0sX5QVQXS8fX6YT6+e58194vzydA/6fHUc+Tg7f3kHdj5xd0/l8l/X5ryj188eXyg6BSo9j1zpp/ecR5X85dP30z99dTOvHx2vb6XXZ0Lwd0jemP/3l0UuYOW3dVOPXOk/a+8Hvxxerrac/gqi/Pg+4X+6GpcV0Wv4uEnw3nTTMwuml6tcm//o4cZ7uh9n0Hsh1wu+X/vMw+uOLM4I4hXb9FafIr25VTOY+34hMJ7jTK5GXX/8TPrQuMOglAAA= -->
