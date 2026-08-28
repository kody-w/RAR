---
name: "rar-cowork-cookbook-configure-revalue-inventory"
description: "Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_revalue_inventory", "rar_sha256": "6f2dfa300b534b1f964d453c9c2c45296ef7d29a9d54a620b94887b6d7ecc88e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_revalue_inventory`. The original RAPP
agent is preserved byte-for-byte in `configure_revalue_inventory_agent.py` and in the RCI capsule.

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

Revalue inventory Configuration Bulk Setup — Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_revalue_inventory_agent.py` and embedded as the fenced Python below (sha256 6f2dfa300b534b1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_revalue_inventory_agent.py` first:

```bash
python3 configure_revalue_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_revalue_inventory_agent.py   # or on stdin
python3 configure_revalue_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue inventory Configuration Bulk Setup — Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_revalue_inventory',
    "version": '2.0.1',
    "display_name": 'Revalue inventory Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-revalue-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-revalue-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e68eea6889435eca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/revalue-inventory'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-revalue-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRevalueInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRevalueInventory'
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
    print(ConfigureRevalueInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPiSJbtX2FiPmTWKDNACwhlW5k9ISSQAEloAUFlWZYW177vol799+cCIrJyqrun22zMHplhgST363c957orfn8xm9rPypcvLyow08nGjOPAB+XETJ0Jk3VZGcFfWWTBn4mdpXUZWE2dldXLpxcHVHYZ5HWQpXA6nedxAKqJObGa+D7WDbymNMfHE9s3Uw9M6mxSgtaMGzAJ0hakUNAwccssgcvBO3lTT9jeBvHEDWLwadIFtT+BwwPnIWXUqczi2DLtaFI1eZ6V9StUBPRmksegevnyy6+fXgL4/eXL7y92bFbw1gvz1AQoj6X5t5XhzBiqBYfkA/RBCq9zULpZmcBbDnAnz6uPFYjdT5P/+q+oM0uv+unL13Ty/Hx9Gf8pTTqp/dE8s6qBM7HN3LSCOKiH1wkdd+ZQQbPrpkxH71TQhan3+pj5XVKWT34en318LPLqgfrj15cMqnC3/evLT5OshOuVzfj9dZSSf/zpNc46UH786bucqrFCYNejMKj167fn9VMsHPh9aODeV/0ZSn2E0gJfX/5k3Ph56D3aCWe+vIZZkH58CM7LDPrRTG3w8ad/JNb2gR3FQVX/S3J/eQj2gelAm56K//Tp7uRfJ8jToHeZ/3jZHIb137EEDn9b7tPk6ah/JPvu//8mOg5SmPhvHv+74v7eBOTnyS//0LZ/NuHTxP36sgZx0MLssGLwZfL7N1VmmV8+ON9vfvj1Dyj6fxSjZk1p3yV8S8w0cEFVf/v2y4fqfvvDr798aHKYa8BMvjVl/Pdk/j2/3tf5wYPPUR9/nAvX19Mozbp08p7pk9+z/D/KP14np7Hwv9+vvkz+XC/jB5mMRrwt+nDBn2qmgrr+yY8/vfwBwSGF1jT2/TGs8v/8z8khsMusytx6otoZBCAY4DpIwKi85gfVBP4faxviFiirADr2OQ7m/xjhUePMnfz2f+w7WH62n2A5fQNA8O0Jed/eIe+314kGRWZl4AWpGU8UWpa/pqYHn47L5SWoQNlCILGGGnyGEPR5/AIBcvLbP5H67S7gNR9+uwNl8MAkheFHPKqaGLyONp19kD4tsCHogh7YDZQdZ7b5gN3qE7S1yuIW4tlofxUFcTxxghIaO8L1HYSb9Mso7LfffrPMyv+aPgAUnzwIoZrCAe/qTD5/hha5ceD59dcU2H42+fD7Hx8m/3fyz2bdhY9ryBDFnxGAGgqqJE5gRTUJHAaDA8MJ4eIegd//ePoVikkhg8F4Be7ISONkmJERcN6crG7pz9h8MbEAdC50bDIyCUTlSVC/Tnh38q4vXHR8NOK2n1X1xAE5SB2Q2gOUakJz3j2ZZvWkgmlXucOnSVOB+6q/WaV5VzGBpW3Wv00OjAxZIovvTPhkDTg5SwPo/vcUeNyHQsoP1WT1JuJ1Io45OMnN0sz90nyu4ZqPuEB2eJsOhZuTFHRf05ELweiqe0E83AMHQc/Yz5B+HmMO2TqB1e9Ub2vfx5gjl2l3Tiu/ptUz2c1yDIUNwR8u6jWQmyEF/O2ZUpWfNbFz9x/UdJT0jILzjMo9B5W/9ADMD93CamwgVIgY+eRrg81QYvL/q7kYtaU3G4Xd0Bq7nrCiplweXhx7odHbj/YJUv0EptKjYr7T/xt4vGHo1zQOYEqUw98eI+++f4554BKsbAfigXKXDwMPvTjKveflmGdleXfD1/QNrD9Bn9yRCZoAixgm+eiItwXHp2+a+rBSx+vvxH2PY+mMpsPcm+SNFcO8cAFw7k6o/XKsrWcIYJKCsc46P7D9H6yaQOnQ1VD+BCoRwGqBgH53nZhBM2FZ3aPwPjwY2yGohdPYUFvYbILXyRmWx5giFaxJ2NOMY6AXPtxFTRIAfQxVfPdw5Zv5Q5mxP30qaI6xyBKYtX+OwPPh94S+6zKqD6WaMPbQl92YMQ7oH5F91/MZK6hsMpbgfdKP4X7aOvkzq/zta3rX8R3OYWXHIyH/yTkTWFFJdU+5EZgqCC4JeCYQzIQ7974+6PPBz++6fPlLU/7x3+vb74So/xi5LxO/rvPqy3T6ILE3DnuFsDCFORLkoPrOZ5+fVfb5vcp+EPnw0JfJv6fWDyKe+fxlgr7OXmfjo31ggzFhnx/oBebz6vKZGJ+OePI9vM8cGPE0HiCBvpPL2xDIMF4JvHHwg2yqkaM6SIt3dIUB+Jq+p8CzQB4IA5mxyv5UuHeWhQF9xOudBOCjtIZrO2Mn5oFxgxKP6lfg5UvaxPGnl9RMwP+wMRlBHiYodMS4lYHFApuaOgD3q/cGZ7z4cRN2LyNY/072ZaymT5OxGf00ee8rP03eOv37vilt4Fbnl7GnHZeEQ+Gv97HvOzwLvMBtVT3ko9KP7cvYSj1b3L8qMRYR1NgGI3Fn71U5rvgXIfCL54Hyr0Kk+xczfkJDVZsjDQf1W0FXUE+nGYEcjF4b6Q9CYgMn/HUZuE4JigbynTOa+91/383KHrb8cXdD/dgD/v7yBhHPGDz7PTgc1uLnamS8KUxRuCC8fiQTfPbvdILPqRDPYDsC5y5czHFNfDaz5jhhoS61IBxijtuUjdnEHKMWwCUdjDIpZ06YC2xmUcRySVoLhwS2vVwCKO+Rjd9GRg9GdcDMBTiFYraDL7D5nKBQEoPzTYI0TWcGZ89I14GQ/31qBMHwaePDptGB703p6Iunqb+/WAsCjtwSFU8/PsyUOkHFCEvsLaRcuJ6WTnkrPQkl4hWLme6gy2hjirw3nOdKc9jpScFGaCH7ziHos5t+oJjtwt9i6tQm/Plip5Bcdw5m+rqem9u5tPUb45ZKfc/pmkIU5jw6BYm/HJqThIpNf02FGM9PsSPkEVFvT8YlN4LY4MBOxnHCyGdnxTyfOY6uTHVrJULSXMu50im5Quo5iLFjcCVmsSIZW0SIN9ezlB9CW0WdpFkttBLVExUEtRBhOp/ES+GsnLmd2EcHLYeuN1JkLmsoYrnBVE7L+EZJvdSgvKfbjs8MdlJrZgZEjUntc9woA8s3DmvJS8Fdz3dFV8bKcFiGsyzXYqrYuOqm1PUb46txfypidSlvcYEoDOlkQ1q7NnzeLZhhLtQHMeQNBjk5qnwhZsUprjVZ2+4EVFsxrYKJaFo0+QnX8Nkpv6ySq9AVmBoN11nJbgFH1Icc4/MTn6cUUvMqF88QOzkt+ap3T6aANM6y83k/i/zzjF6R7rqUMldI/cbeo9QcuwHNdgT14iIztVin5/xU8On8og7ublc6QaYJN80QuynD7lm/4rCFue7LFbY/Nm2gRu1ZOwlUaFuLk2YsQnXQQxqkhQMYhzeJQLH3R9fgVkgOmgOFAc9I6UMs3hjKWTYNWB6EyilIBjPxdQeqBB2U2EnJs3ox7E1fsoDTG4u1jXkq7RfoJSFmu+VxLyeL/MDtuqRnWgRjvOE4KzvdRg7N6ebJ+HamBhs9xej92m36XiZ0Ow1y7rbam5elv5wjZJsXQm1IXKpjKaNSh67MhUt41RT+2MQCfsZMY8NfpxtNm6OCUYa3g0bunPOJ3Qi4EC4cWfCW3cHHpZjVE4R191sac1stROjqQIecmXcmbpJ77BQMWBeY8T4fHDQWg+ZUnMzorF2mppgqiuWvmU2lRle3pgk5UBmlZ0kvsheInm55jVqIyw0Fzgu7WoW7rXWVRFutiT3BJ2uTJ27ZjUADOxCq1VbdDYOS+ZyNsqdDEWz2h4U+74hNm/bGhtCVzHWBAA7mHJm5WbDeIvvNeil1Yhwc43S52eBzU54h6F7bzcNzeyW7BR4etdhSimhKLumGs7arvs6XKemfCgq3k3OPJDse3U09ZINW2slS2kpSNgxRMKSKit4FEVxfvE1XvX4LF6gcrKbtWmHDap3PmQ3F3tJY4gv0EuBIg5zqDqeSM+mvcvyCyFLbZv3pfLylRzNil6jdsT5WVourgtTOji32nBZUiJQLMx05EXq0zFATOe3zs3gy5lw+r/BbUOk8M5eJtbDYpug60xxH3VVa2lFKIhcKEDe6z6eE5Kh7STzxK9e+ybSxjSNdII1rebYD05/32iDQnkWLV3W3cZDYxIJL5fSJFB1xXpidhNRozGAWxztPSM4A8uOClDZsR+6Q4TYcHToSr4vpPqhQs3KXUy5I8ZgmE02zU9ROlYDC1tVQDVmX4Jlk4foZdc8766Q27ZCjEJzXDkY65GruIbt9suYuA47r0ZU2pyhXRD61pInBWe1dO0R2sMHZspm0ocwbfT0Vg+SvN6ETrdZc7wQXMFWDjlGd7hLvpHjjyMYMuUypI5pI7QyTtKuTXS70rBqY7aWL0t26lz2ciTgH5ZKDsyZrW/d2R1uJt0aAFfZJdF2ryorLNmM24u7Ax/Si32l7Nt40cr3XOnBkC8E74JomRoJgONSp9WtM3lpMtCtWbruny9WZNpHkemuRlCGGah6qZ9N1ZQ3y2JQscFY8XMwukfHF5STs/fmq0ZIlBnxa7hUeALQ9pC0a0GiCbyurOR5Xm6Btc3PnpicUnU6pSyu3qCqseVblIl3s2v1OJOZrOvNYCd0Xx7zdHkpp53FsG9+K/OCtTWtFcQciWpw9x17v0IQIE2LHXrBYldK+0OYH9hjQq+qaY/GZJv2QlhYXWnTXksqRxqoMSYEuPB10lSaHnqTdbqFacJ2TavZhzTOHTl/WFckW1zOS5sT2OOUAQEyGYQm/bH1SprJoH1px3bWlGuezFBzLDF0DLLeH5e7IM1wKhvgW8otbNeu8c3u4VgF69Ho/6M5u1DSDOFvV/aWxMm2pn3v1HKbbiBOMja1HwQksYZ2hPMknWZBrl82xXllGNmXM9SGhAq+qdCs+gd5Jyht93MG2bLhmq6zfIP263q8HtTJmizNazlGPotiNbW838v68w6twIGO2NuZUvsV5jK7XkWp2S/QcLRgz2wtBBRb1ZmHzLLc8T7kyt7M6czIe4wKDiM6c5W8jUXWjKimT4CYgpZfWB1/fSV5R5MnA8dtKPPpGf9gGDWCy4QwMQar8NfBLfdCFlD8wrSFAvlpcIJMVu1MXdYe+4MRwM6sdp4wo9jwLd1Nmvrt4K9q1qNb2rztpMPVqpghKw19u+rzRj9slWUbomsgF9EInYnsNLdk5zFB1cDx5ZhkWtlP2ebMiDiv/MCdKFSRt6GYsI/niXDEIn6WkQk9pwoh2Qk/49QXVMb/Z9q03xeNr1sa+6hAKeRGu9HyRn7PsUnJYyGvBsItb5qjSIFtYl+3euS0USkwc+uDQ05mJI11x4lNLP5AbmFb20eSZK8Bbg2l7V0+EcykaArGkDoepFiNbpAs2ra/wdMpuN+32WKk84fhlr5uuYSRDTwn1PsLILYrK2KXp0V0m1tQ8773zxT4chQDZD1SzWumiSTO+fGrW+wCvZ/l8Azo5umbsgDKZQMgEemlvB6xY+iXPDoubX++J6ALxdi4eQuSWqmx97YpiHS5ibbV05+pqSE+BQxQ5zpbxUIRYt011AttPMfG49b0DYTXnU58vo7PFLC5hflqpvDnnkUvG7eX+tArb5Ar9cLb5zMZWCq8ki1AT5sW00ADPOJRVSw7dJNWU3g/z+V418HC93Crq8pSb80bNVCVGB6YKdLiS2lwzgT1mliJtgAr7c2Zz9HV6WyhFGe7zq+T3V/KqsfNqOC3Si3XGt5qQV7eupUuR9kKpGS6akkq7Y7a+wlqtuuZW7YrlJYrPJb67gkvLK/HS2VQr0tldg5MZLGRkzxiSDtyNAaS1ucasMCSaK5oZPRctDBuSWVos9XaXcjOZvVr7+cxEb/kG7Jxul5eYbLj0wavx03HdzvyNRQkbXlOjjTITlEE9FQv5DHSRo8vzJeyPVYMwemIXaS+2zJY+YBfKyjkQqUJt3w4iqOVre74Zy71cFhKOd71iglD1N/3CMPmCD87H2swEst900jKiMYa51asuYuqk0Q7b62y6ciDgO/pqoXARpRX1dr9XlzyVeCqBrg9apeStD7dV5yhYubNMTGSMbP3NWr4JncF3uT6oZizCBj0mSMwddC9ikCtja2drwC+3mXQK0yvtxZKYrMItW+gyZ+pi0nMgiLxNargSWPe4v9l6N4Fi0Iy7FfL8RJzRRUQu8UYsGG0Vyuv2nMAGOyb7qY7cDtyRpI6W3TO77XDgkdaRZxd6x2LLFtKAv9PFrVjubI4452wVisXQrMJQXyC7AxYPSc1fMtf39vqaI7Jlym+N3exanjIu8BO4JTD6eGFpJKbqRbMuQtqiaUf0CoddEs0wx7klo3vpKugugWtp2MXfq7vZKcn3q/XFTXhRPlLmYa/pt4XnIUh+NWYgtzkZrRmzVzDUWdv6EBSC6e2mLsSIAb06IqmfVuXUFxGBbC6btIklodkoJCicuLM5J27rJMemOmcMIlqvW7tZtKURCICkSQkZapxs/AWMajg1zoeAzgVz6zYniAO7vJ8ZWHopHS5zu4sdrvp+mpZ5nhlJBqZoUuAC1g12wGvjtmZQZsqwdJebigXQF5V05tbkza1WLoen8hH1Fhts5UaIAwhuaqCCxUwvkXv2a2m/Vsgja/nLhoqZabfxWjx14itwqs2VN3JlCbT0uMYry7bKA1h3h3SKyDN8yq+i68nPuzk1DXJKkjzQrhZXClxQZDAsNfHCStBoae9wCieZwYVICTPPEIQ29/KCw9UdD6SpY2CDO6saEraIlIf4HLvNRTJDfOLYElWYzfG4SWK4RbXsG0vXQX6Tb2UmO7dVYZ3VnXIrbr0+I4dw27DNDlE49eqn1No2cN9Pe+WIeHPSQdfzNSLDzXZD3Arlcjsv0YqVA4Qk1UwvU6upQnWjjj0xzvYyplAtsdnySitecfQ2s1SNpbaEKVJDvZ9Ku+kZ9jTLaR8dz45QI6tDTXNiss4patPjuIW4kXPoOYw0ytrbb3jaYmppfbCMzm5vUyAuGve098IB9tchIiTkfLohXV6oea/sDiS14CqcExAh2Bzj3uulPkLCWlPofksN/ZQ1nN1sT3taVGkU3A/TWF8wKyPsdq6HK568lvisp3e3LbuywF67ZVzPpuR1HqA9im8xzxXp7pRv9oQfrzg2lVFd3qY3DDsfh6WCZOugm0VU3WyXt/gImdgXI+a22s7IA8EmU2WWyM7ad41WiBUHd3NbOAzTgCW0JjO80xQgAcAJMtofYEhUUuhnenWTQ8m6WTGN7fEbBljkyu97DOgKsb7J7ppyV5DrG6e+iM1S5VjJzYrQ9luepLHtVj5vZ9s2bPqFitpK4tZotyfQZH8Gu4HiL6tBP0+vulMBsasWWxeyQYHmWN2QhloN663RFH4g7dML3LdHS1a6oDSrt4trpVL7xVLW2MCThX6ZtQpyYsO57BNL4cpimnvS8dJgw2CGI+xmeVkfrRi5EGBFDrg5vaxXZZyeXFPEyLIlTA+EnI8jSEuqLdCPbSjDJD5ROWkQax+jjgWXOrP1zG07Y6jRSG5M/EoZ7czACeMq7gzqhtt90uagp5h9vsJ9JuFXYYeeSgO/AM7iaRCa/rLflGWynx53iLgQ5A4V6eUm4mkUXQJJprosAKW2yBv5GINr7gQYLuYhZzftAcWnOlbrgbbfyvQNcnZ7WIkrrxaufjTPM8ImnDW4CSeUakxDtNA6b6haRAX8sqxPPNKh/K3Jb7eoUNxLB7Yh3AGZSUtj4AKukJBWu5nqMTNsJVndVb+ecFSoBbiplraCIqzCuT5S1TaH7IhVcyBcSelADEhpUrPzsGrxVmQM5ooP7codTiVa2Um6INeIRh5uAMH5Q9tiTH6QpGJ9wRdXlsxmrFo3mrwx2EwrjKlCJa45T129y9FKoj0nE2buDY3nx0uxzplMpVNr0ay2U4U3dNAvuXy6P8sZWbfXjEgdNcPP8xuRryGi0vZGKl1hzkQ0Tf/888unl/FQ+nm0/K+8Jh4P/P7Xzh0fR4RvL5buh8rAdL7c1/ryL2nz66eX0g6gLo8T1SpuvOch5H87T/38T95EjBOHx/vW8a1XX78dudemN/550EuQOk1Vw3WrLG7uh7mfXiCgjn+vUH17Hlq/3E1J8vEE/H2t8aT2/jLgW519e7wVfhn/nGB8kwOcwKzB89J7ni1/enEGGI3Arr7hi/k3UOajic9XG9Ay7HX2ir788f8A2w0SPYElAAA= -->
