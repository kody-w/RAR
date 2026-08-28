---
name: "rar-cowork-cookbook-configure-track-project-fees"
description: "Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_project_fees", "rar_sha256": "35002e46690c146cc4dcc5462f1341449fc12cacb164853f7c90507fffd18d72", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_track_project_fees`. The original RAPP
agent is preserved byte-for-byte in `configure_track_project_fees_agent.py` and in the RCI capsule.

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

Track project fees Configuration Bulk Setup — Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 35002e46690c146c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_project_fees_agent.py` first:

```bash
python3 configure_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_project_fees_agent.py   # or on stdin
python3 configure_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Configuration Bulk Setup — Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_project_fees',
    "version": '2.0.1',
    "display_name": 'Track project fees Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to track project fees from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94e234b33eb0c408',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureTrackProjectFees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackProjectFees'
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
    print(ConfigureTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8Vae5OiWJb/KmzuH1W9VqW8kZqYiEUEFVFQEJCujmre7zcI2NvffS9qZnVtz8zORGzEmpWRAuee9/mdcy/124vVtWFRv3x5UTwrh9ZWmkahV0NW7kJs0Rd1Av4UiQ1+IafI2zqyu7aom5dPL67XOHVUtlGRg+VMWaaR10AWZHfpndaPgq62pseQE1p54EFtAbW15SRQWRex57SQ74EVfl1kQB4U5WXXQtzgeCnkR6n3CeqjNoSuVhq5DzaTUnWRpvbEo+nKsqjbV6CJN1hZmXrNy5eff/n0EoHvL19+e3FSqwG3XtinKp46yZYfonkgGaxMgV6ApByBE3JwXXq1X9QZuOV6PvS8+th4qf8J+o//SHqrDpqfvnzNoefn68v0c+pyqA0n+6ym9VzIsUrLjtKoHV8hJu2tsYFqr+3qfHJPA3yYB6+Pld85FSX01+nZx4eQ18BrP359KYAKd9u/vvwEFTWQV3fT99eJS/nxp9e06L3640/f+TSdfXctYAa0fv32vH6yBYTfSSP/LvWvgOsjlrb39eUPxk2fh96TnWDly2tcRPnHB2MQw6uXW7njffzp77F1Qs9J0qhp/ym+Pz8Yh57lApueiv/06e7kX6DZ06B3nn9fbAnC+q9YAsjfxH2Cno76e7zv/v8frNMoB3n85vG/ye5vLZj9Ffr579r2jxZ8gvyvLysvja4gO+zU+wL99k2ROfbnD+73mx9++R2w/l/ZKEVXO3cO3zIrj3yvab99+/lDc7/94ZefP3QlyDXPyr51dfq3eP4tv97l/ODBJ9XHH9cC+ec8yYs+h94zHfqtKP+t/v0V0qbC/36/+QL9sV6mzwyajHgT+nDBH2qmAbr+wY8/vfwOwCEH1nTO/TGo8n//d2gfOXXRFH4LKU4BAAgEuI0yb1JeDaMGAv+m2q494NcmAo590j0xbNK48KFf/9O5o+Vn54mW8zcE9L7dMe/bk/7bhHm/vkIq4FnUURDlVgqdGFn+mluBl7eTvLL2Gq++AiSxx9b7DDDo8/QFICT06z9i++3O4bUcf71DZfRApRO7nRCp6VLvdbJKD738aYMDYNcbPKcDzNPCsR7A23wC1jZFegWINnmgSaI0hdyoBnKKenzAcJd/mZj9+uuvttWEX/MHhGLQoyc0c0Dwrg70+TMwyU+jIGy/5p4TFtCH337/AP0X9I9W3ZlPMmSA488YAA0FRTpAoKa6DJCB8ICAAsC4x+C335+OBWxy0MRAxCJ/akrTYpCTiee+eVnZMJ9RgoRsD3gXeDabegnAZShqX6GtD73rC4ROjybkDoumhVyv9HLXy50RcLWAOe+ezIsWakDiNf74Ceoa7y71V7u27ipmoLit9ldoz8qgTxTp1AzrZ98Ai4s8Au5/z4HHfcCk/tBAyzcWr9BhykKotGqrDGvrKcO3HnEB/eFtOWBuQbnXf82nbuhNrrqXxMM9gAh4xnmG9PMUc9CwM1D/bvMm+05jTd1MvXe1+mvePNPdqqdQOAD+gdCgA90ZNIG/PFOqCYsude/+A5pOnJ5RcJ9Rueeg+ucxgP1hYlhOQ4QCQKOEvnYojODQ/9uAMenLrNcnbs2o3AriDurp8vDjNBBN/n7MUKDdQyCZHjXzfQR4A5A3HP2apxFIinr8y4Py7v0nzQObQHG7ABJOd/4g9MCPE997Zk6ZVtd3P3zN3wD7E3DKHZ2ACaCMQZpPnngTOD190zQEtTpdf2/e90jW7mQ6yD6o7OwUZAbwm3t3QhvWU3U9YwDS1JsqrQ8jJ/zBKghwB9kA+ENAiQjUCwD1u+sOBTATFNY9Cu/k0TQSAS3czgHagonTe4V0UCBTkjSgKsFcM9EAL3y4s4IyD/gYqPju4Sa0yocy05D6VNCaYlFkIG//GIHnw+8pfddlUh9wtUDsgS/7CV5db3hE9l3PZ6yAstlUhPdFP4b7aSv0x87yl6/5Xcd3RAe1nU5N+Q/OgUBNZc095SZoagC8ZN4zgUAm3Pvv66OFPnr0uy5f/jSZf/zXhvd7Uzz/GLkvUNi2ZfNlPn80src+9gqAYQ5yJCq95ntP+3wvs8/PMvs8ldkPPB8u+gL9a3r9wOKZ0F8g5BV+hadHYuR4U8Y+P8AN7Ofl5TM+Pf2an7zv8X0mwQSp6Qia6Ht/eSMBTSaovWAifvSbZmpTPeiMd4AFEfiav+fAs0IeGAOaY1P8oXLvjRZE9BGw9z4AHuUtkO1O41jgTbuUdFK/8V6+5F2afnrJrcz7X3YnE86DDAWOmPYzwNlgsmkj7371PuVMFz9uxe51BADALb5M5fQJmibST9D7cPkJehv375unvAP7nZ+nwXYSCUjBn3fa932e7b2AvVU7lpPSjz3MNE8959w/KzFVEdDY8abeXbyX5STxT0zAlyDw6j8zke5frPSJDU1rTZ04at8qugF6ut2E5CBsoNJA8QBM7MCCP4sBcmqv6kDLcydzv/vvu1nFw5bf725oHxvB317eMOIZg+fQB8hBMX5upqY3BykKBILrRzKBZ//SOPhcCxANjCRgMUbAMOrhJEnDDoKTjoO7jkPgJOojGI7gOO07COpYjo2Q+ILAfMqhYQKmfN93kYVLoYDfIx2/TV09mvTxYN/DaLDKxUiUIHAaoVCLdi2csiwXXiwosNwFoP99aQLg8Gnkw6jJg++T6eSMp62/vdgkDig3eLNlHh92TmuWbcj2EG5mt5QeTipxVJJ427iIpCCeu9vWjReZqCyItsrZYcH4gcLjHB4yzlbINYu9zLf1or+SqkyFiMfy4qiQvhqdPWF3uHlYS87kug04RolbUtvXyemUlfT5XGT8ObWcLB/DFDuXOxQZF4buGpdE1Fydn0moYSw04awfrRMvcq2wbGDlUmfKTKu2Y+G2SafUe30fOqQ4K3e5iIgae9GldK86llSndqRnZ9xdE1lexCeTD/eyPnj8zmr7w6okFp64oPaGgFKH63DI63bmzENJbJWS41KAIluvrcxz6dqOyqY7wbKURtGd8GLOj3sfOQd10NrpuepORAb8lHZ5nLJctQ+Z89rVNnp5zvmZ01BN6RDaqA8If6kM/hQZgtKGrWARRhTaqsUeLUSzuHhxG08aeuyvBwfcHcVMcRNtfrz5xq50iSIBWqVS5krwKW/doQwPQJcaqxE7SESxc4h9fTnZkVnpKuKa9HIVGevZtt1u2W4hNVm4KL013V+NW+22CwW3rLT30yJPNlKqhPqOQryRy3RXH9b17dAfVxY+NxMzqq2V7R6OFVIRCa4cB+Kki0KSz80IrhHXIWul19Ktn1cniS2ZC8VqsggfUTiv/Cq3D8mOWGCr4uQc54YkHq4ZrfqcnTlddYBna4pvAHBZZtfm2WUIUQ6Pi1RM0VqYm2o1bzIhRZqaYsfhSsbCCRaKIz8fB15X1pnE1nlY3nhvP3cMNsT3xdXZKut5GcfJ9rg3uuICZoB2a8SzC93qe2pdVY0oxQWuYGWM+zofIYnfszxceLTCpUQ5HjmEPnJwWchFkxtmhndSQuZyf4sb1cAtuU/cy0y75FF5U+f4fqdWrj+/LemoMU6dVzVkh3aKC9ucPuNUkDeabBXbS544aVYJJ35jL3ubD6/4XjCH3TqdIXztnXBR3GIXNpkfQY4RqzA/oUGO3TBeZS9RdnU2StXruDDrta1F7gsr2d6iRhm6JXYSjju7lpZqf+65Uhl3u0t7C5fNhqM8b6QMlrwGtUkcyguhStySs7fX3TraB8cLNTcrYoXK+EW5oqNX0oWeuQO38iVZEZOWnekw2eZzjBD6LT6/HQYxxW9jh2pzoXSMbrxt2CtutweCQ/QzlseRG20Ojr52XQvOdywG6mNDu/zJpK3zPN7YW3/HyTy7xw1pB2qh6vjbzaXFcsDIPY0xXFwNsLmfz1VeMdW155GJArP0obN4ivYt+HylHQUu67N11rABPXUVcZPXyVa5arf63KZbQvPhuZHVfrIL1dEQbowlH2ez7dWhosrQoksn9MJhJrQk7CrceT4X+C1cIH21IXm452HC5FkvQ1mikvO142h4oNzQ/mAEUVwrguE2a5EjTTXkTuPSNRUTJ3JDaprSGs00r5Z910QgAaW+brdOSh2XseVdR6Q+eLm+2aDJmfSKWg8sit4ijcr3eYyeXTM54UdZaKhZCZ/ppMHq8iQm82JGuTOZusnRyaRQw1WGyHH9lltbmk9iqiIccJpcnFbi/DhjSaVoYqbM9JtzZg9hFfOXvJa3omItNWL0ooqec6uIu9yCYedfdxXhXo+4uVSVPHNiGPFsy+ydhkmDm7Nx2MRg9/C8QEb4cELNaF/z8wwXVkkoi4dBdjudEM29RKxOBaMEiXnRSsVauYJ+uSSHYohSpxOOjBhpziFZ3MzzfkfNrG5/GHGTCtLscBzWiz4yR4Qe4wKYIhZnczRn27jzrmo70tINGdx8WArFqEWHDsVnsXIdKulIJcQVWRUOvUp0Q87qoicWDdya7o1a2cqFWxAsLSPePldn4BdRF7tNTpL7uXf2x6zg0PEqH9xBIZc5c6TP1yWbdc7Y4KVSIHjj8kIO0OSGqaOlaKo6dFykrM5q3fNCY++63U2oTsJOvipOJClyduDXyM7wdukKzIVSqxxGA6tWStZk+2qZYIy2tqtkni1OYBi43BYmJZzjiLosU7LaN/tVZnEL59ZmDrGiT8mM2jQwf1p4V63slgF5LuU1lfE1b84sZbXr4YQR2dvZ3NFw2vKp3TiCuJb1y4jrl2DQhs2wqZtbNytgRUTnm6Tkut2g7OKUOZxBcKKsUVi/62/dIrsULm9YAN3MSHBDYSYxDkNgWnI+VFHr1LXCu9X8mOzrXX3ZHzl027HyrJSSRhask6+WvnHN0RWCyuXQu5dFY4geqvLY7uTqHJr5TtKzuOaoOpV12C7IFqwa1Hl3VbR2zy28tRURdO0tF2l7TJULIon4UNDbYdmoRS5WZVaP14godMXYafPTWeOQpdJc0FPLVAVrMIbNK8RGkBJaz8NZBJPLIx8XK7YmCzI92o6rBPV4GBJlmS5D2RflOqMzM93HJasnJp6H+5hjxNSw9/YOSYZreUzX0WHUMDq3yosyrmd5rFdbwxbH/W6j8aREaUS5vVlbBd4s6mqQTueD71qrIwsP+dV1V+fDMaBNVoWzis1nQuHlLqsmZwFkjYaHxwt6RsMhH7pkTknjifG5XOjDLkBvh3zam64jhZFuJ3e91NyEXQbimIkKQtRsXBo0x4VbXg9isrWvF77K47qC3di83TTmInCjfZU6YVnM2rPSsRauDiYpd/OcuiHnPpV8NlVYN24tx6Wxvs7Rdb0RKFSSaCIgEdcQWmRv49QlKtdq5SskpufCUivHGRMdca/tfHZdWBzD7ZfX/cqOVy1cEJuslxMTVBLC5j3CwwvPblKxujZKv9wTHYcW/W69h9VZfiLml2E8RCy/6yJSSs/9dXltt7sTiaXXvF1T6TE7w1sydKrNpvV7imNwY+lr/qgH+56L9P2qpKXTcT0XOlw167AvN8sRXnuZWuZLVhcCQ2EunbkfPasmEqzaZBtlUM09n6QZsdJVeXnR5862DJ1QHE5psSaOK3ptg5FrIcipJp1vB15g+fnlmFA3Y+UVJ4U5MEdE2RtmGrPERo+bsI3TVWnZ+ZBunLbJUXC54EKMDVmcMjWD9PCaZZZhC9KEHXhLQxY3gczO3Z50TqhT1f7xigf74VwztXbgwkRO4jyp5nt9ccjOyw4zDuN8aErtwOe71mpnbUGWUisi0qEhqVahDjHFCvPU5twUwxhVvHGzJhFvYtSwyQI+OkqM45xXWRvGWeLdUar0KKhrSSnKUPSDlBVjTVrOcIVZZrej3W7jMer5MiMufirUF4rcbKzOy3dUP2O1MLrk5UGyufR82l7WhWYhlEqwVNL3whqJ9DY4rLZupe3UkNTrSIQrTo0AEuKZtjsY1YAfEW+DIgEly+ZZuCUSTioZbaqwsIr2jH3lnTnvMgSiwpG2T/LKNeFT0Uk3Y5HUghILs9my2RL7zeEg8pelpGKlFhBcvboowbnaxLy2MZuVeiyLQ6GtMKpf7+dbUBqXa7Dpj500oNs8EvJTTlW9kCpKwfmmO1r9bjie5cCtDte2Kt0Fk/Exz61zO8wtk2IWK3m/km7lfh0U16wJem0msaK5ZpDEEYk1aLGiQxqjEOlDb6yWQ8EO26DNA1nfNTddPK6IldQQ+2t9glEaK7hY2+cux56ZpWVLui3Qg5vSjV1w5dJTxCwW6NZYicPlpIeNtjMHMl/1y4LaLE83K8u885lHEVsyFTbztBoZdvKFOErDUkNcujmObLHeBOTVS2rjduh2mc0z485YxKuuRtNO83YzVMP9HZ3gNE+nfopWKI6dKVIn0RPlqeyVhBeKSDkGsZBcHZXI3rE9NGd8E1b4rXiyGcJE82ORrxT4kN30C8WLTL+NTmODGnZ9PcsbqzXyBtbNRhVufXhQ5RFjsqUhj3PVDVTYOtVuGjKzubER/CgD8/Kl32WYMj9SeDxeZhuHcG0tCGkpR4oLvaSxFrbXPlWdF73eIPLqlNkz1yUIBhmZhdSP8MalSIyyxg2YPwV/fkX4ec+Ya+Ni+ah/xTvfiEOqwrrEN/SVD2q0LwuGWmrjhq+iYLFSi2wveKvwsEHG1QA2bNKoLhkBubV43IctJ23k/ZFg3MA7x9nqIq4SaTA3y6Gz3b3YYhJ6QbcJKtZ7zCuLxYapVRI9q2v+6I6Lq3de4Le6STK+CcGea2kg/MIekpPR4wotjx153ChXkDjO4C4bPLvRfi/FzdymrgU7c3LJN+v1OUgWXtR3xLyDqZ7oLSdYL+j0aJxPqM8O1nqGVHFDGZ6Fzdq5OSB9mB49GWbQYF1zga9ucGMD6oqYhZRViU6ro4jsFNFyz5J4EzYgwq18oLWqOtSqtCJiozYcU7VpbJ37Wz5mcrE/Uy7Ygd14fiaM3DEcoqEbEi9IK90ZNjR6m58xdYeLy01YZ+WMZp1zU4BhSuPwed4vYSIPN1xgOPxQh1vbE0Ws0AYOo2IiPg0YpqHczPOC+rzFwtVusRsln+x92agXEjOsaHxTHXe9ick2dWFxedvGq9vSZOJimdO9eZEE0Mnzo5bWC//MIcga3Z5UbGHm7BEOPcaY7UiBcvPuDPQHspFcPrE3UOILLPd3boPJcYeX8C0w2gbv69k282YkiYY2WGTPFiaNc1uTmC3Jo7TyT9mqdXZsUxy5+eYQ7A8RycIzSmTUEcnEs06OF45j8Yu9uhZod0CPJB1joUWcYRi7uld9W3khVo07mN6kaSVhEXZ1rlzK9GpKG7jgZbmDhYF7lLeX+dqEwTTfSyvYv7LmydVsNNFG2DtSjWp3nOxIWBefku5aH9oZ2qwbzLTnuKEH886iht02MGY4QbV2SGw3tEhusUEelPWV8m7B4mjxmXtGbnKOC8TONG9U1KK2SS14erYdj87i2khmJ9G0BMtbXeY2AHk8RvLWVUd6ZjwXm9Cr6fqwZhHH6SWaqa3rIC3WZcAHSSmT3TUmiFvDcypi7Wf55UBvF6NOJUNeIfqadD0fzKMatupDhZJ27KY4Abu28ul42fb7m8dlBpjpinVZtjiKi7uynWNF6UlShuGNFsgMHLHkBtv7JU6EYr/wqcwwkAJE3e3kjcDoHSfg3YHRMxndcJpKHMXERJhbcONJr5SWtGm3J1IjJJrc6VfDJRhp3wTZjIx0y5jJbaxGijG77B1s6d3MRnaIvYCAGjk4cwlsX+OFR9XjkvFXhBD6BIiNXiy0lrTxY58y9HlODskNw/b4WrJcfxX3a3IbrTzLubKrjXJgduHAUb5+2dGksCXjUbgeZMobFhs6IfJVw+QpXYQxjyibYr5g4nCtCl1fMgzz15dPL9Pp9POM+Z96Zzyd/P2fHUA+zgrf3jHdj5c9y/1yl/Xln1Pnl08vtRMBZR6Hq03aBc/jyP9xtPr5H72VmFaOj9ev0yuwoX07fm+tYPr/Qi9R7nZNW4/fmiLt7ge7n15ssPvOvab59jzAfrkbk5XTafi7sMfNu+JtMVH60fQ8yqf3Op4bWa33vAyeB82fXtwRRCRymm8YSXzz6nIy8vmeA9iGvsKvyMvv/w2lXdnulCUAAA== -->
