---
name: "rar-cowork-cookbook-teams-update-develop-product-portfolio"
description: "Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_portfolio", "rar_sha256": "df7ab03785e875c83eb62d629df360cd1d4f44340dbde06a8976d26ae8cab3a7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_product_portfolio_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-product-portfolio:7bbed09a49f870dcff2608e85b7e3f593ecab53f8f6adebeb2733e24cb6d21c6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_product_portfolio`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_product_portfolio_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Develop product portfolio Teams Channel Update — Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 df7ab03785e875c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_portfolio_agent.py` first:

```bash
python3 teams_update_develop_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_portfolio_agent.py   # or on stdin
python3 teams_update_develop_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product portfolio Teams Channel Update — Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_portfolio',
    "version": '2.0.0',
    "display_name": 'Develop product portfolio Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop product portfolio status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8addd5522920dd9a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-portfolio'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-develop-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDevelopProductPortfolio(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductPortfolio'
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
    print(TeamsUpdateDevelopProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6d3PjxpbvV8Fq/xh7oRFy0q1b9UgQJJgAkggMHpcGoRGInEgAXn/3bZCUZmZt716/elUPU5IQuk8+v3O6e357spo6yMqn1ycNWCkys+I4DECJWKmLiNk1KyP4J4ts+IM4WVqXod3UWVk9PT+5oHLKMK/DLIXTJ6Xl1RViITqwkgpxAitNQYzkWVUjWYq44ALiLEfyMnMbp4bvy9rL4jBDqtqqmwq5hnUAuSJhWoPScurwApCRa+W3G9EqXcTLSqRoQidCoBSWD16gDKC1kjwG1dPrL78+P4Xw/un1tycntir46ukmipG7Vg0md/6bO/vNO3dIIrZSH47NO2iHFD7noIScEvjKBR7yePqpArH3jPzHf0RXq/Srn1+/pMjj+vI0/Ns1KVIHAKkzq6qBizhWbtlhHNbdCzKKr1ZXISWomzIdTFRBBVL/5T7zGyVonn8O3366M3nxQf3Tl6cMimANRv7y9DMCTfDlqWyG+5eBSv7Tzy9xdgXlTz9/o1M19hlAG0NiUOqXt8fzgywc+G1o6N24/hNSvbvTBl+evlNuuO5yD3rCmU8v5yxMf7oThs68gNRKHfDTz39F1gmAE8VhVf9LdH+5Ew6A5UKdHoL//Hwz8q8I+lDog+Zfs82hW/+OJnD4O7tn5GGov6J9s/9/Ix2HKag+LP6n5P5sAvpP5Je/1O1/mvCMeF+eJiCG2VFadgxekd/etI0k/vLJ/fby06+/Q9L/Kxkta0rnRuEtsdLQA1X99vbLp+r2+tOvv3xqchhrMJfemjL+M5p/Ztcbnx8s+Bj1049zIX8jjdLsmiIfkY78luX/Vv7+gphWHLrf3levyPf5MlwoMijxzvRugu9ypoKyfmfHn59+hyiRQm0gCAyfYZb/+78j69ApsyrzakRzsqZGoIPrMAGD8HoQVoj+SOqv2nK+Wr0k7lcEvh3SHUKE1cQ1MiutMB7AbfD4oEHmIV//j3MD0M/OA0CxesCjt+YGSG8PRHx7IOLbByJ+fUH0ADLPytAPUytGdqPNBoGAl9YD21uAVE3y+TJwhlKFd+TZifMBdaomBv9Avv5rrN5uVF/yblDoSwo9ZEG3uUgNEjjGKsO4Q6wBseyuBp8h2EJUKbM4ti2IwsOvJn8ZrLQPQPqwnQMxHLTAaWqAxJkDxfdCCNDP0P1VFkMsrweLVlEYx4gbltBcWdndyg20+utA7OvXr7ZVBV/SOyRTyL3MVBgc8CEw8vlzXgIvDv2g/pICJ8iQT7/9/gn5T+R/mnUjPvDYwAJxsxoM6xhZaKqCwBxtEjisQoYAgQB08+Fvv9/dMUiXwroIMyv0QnCbDKl9C4hBg7uP3h0EdR5EBOWD0492Q64BtAsS1tBaMNur5y/pQCKDQ8trWIF3I94n303/7vE7n8En1cOG0E9emSW3sbdYHJzpZKX7gsw95MNSUN3B94NHg6EwuyAHqQtSp4MzrfqbC9OsRiqYQZXXPSNNBVUdKH+1IenBOAmEKav+iqzFDax4WQx/DQa6sYezszQcHP8I2ftrSKT8BGNs/E7iBVFgWJZIbpVWHpRWBW7jPOseEbDSvc+HxC0kBVdkqO9g8NEtt2+RN/nLvuLeh4iPPuTeBSBfGhInaOT/Q7MyCDuazXbSbKRLE0RS9N3xHllDWzUoeu/EYMdwm3xLk29dxDvgvEPxlzQOoTfK7h/3kd4tmO5j7vDWlDBSdqPdjf6Q1uWNbljDkBh8XJZDGFtf0nfMf4b2gA6pBviCmRsNOJB9MBy+vksawPQcnr/Vf+QebUMWwDhG8saOQwfxAHBvIV8H5ZBQD+vD+ABDcsEMcIIftEIgdeh7SH9wQwhdBOvCzXQKTAzYM92j/GN4OHRVdy9BaWHmgBdkPwQyDMYKsaETr8MYaIVPN1JIAqCNoYgfFq4CK78LM7S6DwGtwRdZMgTMdx54fIRBORQXyO8j4yBVC4YXtOUVOgEmVHv37IecD19BYZMh+m+TfnT3Q1fk++L0jyHroIzfoB9250Nd/844EKpLGMEDdMCKG1UwrxPwCCAYCbcS/nKvwvcy/yHL6x/6+5/+3hLgVleNHz33igR1nVevGHavfe+l78XJEgzGSJiD6l4GP99r0+dHrn1+5Nrnj1z7gfrdWK/I35PwBxKP0H5FiBf8BR8+rUIHDLH7uKBBxM/j42d6+Pol3YFvnn6Ew4BqEGnt7qO4vA+BFcYvgT8MvhebaqhRV1gWbxh3KxYf0fDIlQF1/KEyVtl3OTzoNPj27roPLIaf0gHl3aG3u6994kH8Cjy9pk0cPz+lVgL+1TXPgLkwaKFFhuUSND3sl+oQ3J4+eqfh4cc13i21ICa42euQYbC+wT73GfloWZ+R90XEbW2WNnAV9cvQLg8s4VD452PsxwLSBk9w6VZ3+SD9fWU0dGmP7vmPQgyJBSV2wFDBs49MHTj+gQi88X1Q/pGIerux4gdcQFgfqiIsxo8kr6CcLuyknhFoQ5h8MJ8gTDZwwh/ZQD4lgFgP8XZQ95v9vqmV3XX5/WaG+r68/O3pHTaG+3tTcI8dOOFvtm+DYd/L7ttA3hqI3Jqsm51vTeob1DEcyut3n/yhV3i7B+TTK0Qe8Pw0WBPWrDjsb+vqp7tMUJlv7S2kADHkczW0CxjMJ0gJFvF8UCSC+Pcdg+F16N7GDzevf94T/69g8MrZNnBxwaIFj+dw1/E8ksV5wDM2ByiPESjgWDZDebzHwqWjDWySoyhA0o7NuiThsFCUwaeJ9RAFIwZvQCU+TP5/2a0/3anAOkIy7LBp4HGWjVMczwCeYxyeAjZLuiwpuB7F4o5LuLRH0xSNu7YLcNbiBQ5KyFqAhwpQFjfQe3SKd9He3rvyd//ckeENImoSDoKTluXwDkfQrsBZrAMo3KYcQJCEy1EAh6bxeB7QcP7H1IePBhfetR9iGDaJsEW7DHx+e/h8iEuWhiNlupqP7peICaZl7zF7F6zQMkbblmK3lJEbSQmnV2VsKG7r+DNLkSfa8pofjgsv0urCos8LB884da2MPNzEjgdqtelFxtutYxWvNgEujmtbXpBuegJpGie5NprvIsyInXw9P5ZaLpta6CwNwl1EZOZTWsJW6hQSmYITumTmJ+sg2RzGL3PWcOL4NLcJiQ6N5RGuB5xcBoU73VdFUTeKbe6rwGFXrZYb18KD8zQtW2HN1IiL+JjES748mN3SyrWOMZY7VtVPPKb2DOteJjE3rxhwOafYfLe7EFEWjc9lp1Uhu89rzSRqsC9wol8sp2fZnPXY2B6DGVtNjUWEg9M5qk92wDNX66Ca4locnQIn7jKT6by0nHLFYbGvzBgEYMqMHTMuAk/dKOfVQSP3pXho29woSscr14uFezycYlKlSptcJXs3IrFr7x6WuctkkZZL2frc9VeXPkTuqc92GnvQ9sqqJQRxW9VuH0GbxM2CLU8bok8jSVm4Nh5RDXENlcbhgip3ZgxfH45xYukaWEeMvWy3J7KM9/n2Igv72ApLeV0eM71Jkt0Vm0ilFFRTirXORDklV9s6DbXoQuq7BXZ27C5DAYGmilZNGbCg2TkfFMVCmS/0hA1qrzdXRB/t+5rnZ+No19BUZsYK16PB9Fxf/T1F4s659klmFAq9sFLWrR9UTDsb25LKXmv5OOdQ/JjgZNc4q3mCFetiKknonMAE31rDIhxkAmtVbXzeYBK+b6aCTM5Wus63bSHPA/1qVO5VI5NN5qkcZZ6V1i4K8dx4/W4Bkk1AHPdzck1q0irXXNPcwazKVjZalFYDf+p8b5oowwuK4y1awdvi6Bl4IY+Nx+hofLnUs0V21gkPFdc4mh42eI/5OTg7wmFKkGC0qNzLzr6aShgThgvjtl0tCCs3lu1SVaUruVrZ81PZz/JAmxinanIJj/O9aS/1QHQORao5WhitkuXcXbC2Fod8B7uHdLuYatlyPVJ9MiyWibZU5pvxkZr3uXRcrIkqbI4hKxo7fRo75JF29HHLUSpjHHwOq/LpSSikljYiJ5wtPMkPZWaZTZz0WGCyupDwTXeiFJ7Q7Xm+sQslTehepAlr6YQYrmJX17DDtrUMd+ZN+1ABVdnYi6OnSzO53s39PRHppq1fnaO+PjKleA3J+NI59FRgg4CndoaBCZoiXvg17O1NOT7GSxMkWorNdkpYmofshB46KcW2dj7N5G14pFBMcS7z2NjT9J5a0jLf5TtbjeOLvr9QJJFpeARdlLbsVEWT/jKLJM03salRzNiUD32WtiTlsJTGXlqIG3yz8SECTPZaV+tx246nHC5hs8Le7QN0nVKRdjaL+aVYtFtJLLYVtDlFogov6lQ4ilQGzAybleYC52lCVdQhNxHd7GxpGhvu1XTN0kSeLoG7LU6uyUrNvLhis4ZZdMAd79UFiy33FcG6NIMaYdrHEnfSDyAm6+WRGaHjTi/X4WYMMBG/sOdWJ7UeRIdy47fRhM1pjKe9AN3KChoHneoIk9ksOK8mJ/XME4Xc+xuQbjUKz5ZhYq2dxfq4u1J4NNaVo710egvNNW4eK4rOe8ZmlNfXk+YkjNcyvNcq3azLWffsEJaT9NypP425a2uNpOsUW06cMqZQ35xsTV+xoS7z8cRI5uGeqfF6RqV22TB0N1eS7Ti3TGPnLSKLW1+NfTcX+stBHG33eCydz5s1aUysNEq4dRioChCn7taoHEf1q2hPRX7CUE0gH/enzgK4GadUf8U2hwuDZq3hx9tTQcl7DmB6l4wSikkde3PEZcmv1YtWRVsBqzOxIwnGd+mZuG52l3VE6SuOodHNZBVcMU2QLrnEGxcxLjPmdLgsI3pBj3VeGxmKxXDLXixEjYPtRKGrI3nTe/teWUzzOqJGu3JRrGJSbMBKzWHdK3YLmyLGRraTiHC1ZTa+o+jXRJKFuc4Y+3h9cjxj3vYjvat6YSti7DzeLfooU3b1XnaYJbtiXcokVZGmC5gGhjtftaOJPEuNkFjZQdXUtkGko6DoDc+ZnY0AnYvuNKb7mCtWy01PHa/6eF1Xbd3q7fishl56zFl6sjBIT2pUd5qwbtUWm4PQrReukio+E4TueGOctTIsK0sGZ3SkEGo7wQtlkfJK2nhnf4+fp9RMXVXnFg+OSRQokRB6/HI0YnyNkhZrbD1STKnebvrpnCesfZ37SYfrMlpzRlFft4F0He/wK3WeZWunm+3U9Uw2qY05xVY4DMrE4Ng0s075ckSXlbIPlOsSG6u82UdOxOrCCchkOc6mhqn668AzKXPpns1yNh2tMYkdGaOpBIsuekx7kOAdGS1Dv5yNCX7r+JugVWh5pp2XQkjuF9bR6K4n9GRNIxFFYYXZkrkmWKhhe+gxs4ltrmZ78yhiiVC72lHjuMg9G6et2gBislJBgQE6dEd2F1GtouNspjlnQWN2O80Ec3ndB3baF1v5mOZGHATynhmtdqtTSGmLfZEf/XDiHo2d4e5PRiWJKwLDwxXnaO7Kw/1oMUquwMtTjDzYUsBQFXrKmMUyXWejNFhdbePq6Tml5uURLmnbxJtfdGGDYwBdVmKQJ/gqOBjyKdxhurhglPAUaUBY62dwbOJD3NmuXgipvD7MSXPHUiindNtFv07nEqW2scs6vrhcBKN8qwRpBBqW0HTfk7fsNrnqC7w9jIzLgSHcqJjg03A/lzPFmhx6VTAKvkflLHEyjQrPhm9AgHOW/sGjVlqYHy72XrVJyimiblZfS5MsHeuEigd+HGgKSlyUpW+L2iIT1dQgJL/EUy4YG02qhZq8WZ4KU9k787lFjrfZrszdrZ5ESSrAdBT1sjzllAjs2KxHvNlqqA76SZbooetp6xCfcQ6THWN8t2ehcORWXYUCP7tGp0U4owlJ1zpj4x/OrXOa7Fy8kedWByIlcUM86zBynSlGg59ozzfVTSFNznVsYnl/9LeTiZtq5HG/KLXish+rhLiImDN/3h8aAqdIpxeOU1HR1stgi+1VTzTB7nKczLjeaZdJK4SUTiShdJieq8OBr/CsUAP2XLqKKhCxcr6MVSzewvQiN9lk1RO4P+K4ecg2x0461dokoqUmqLTx9RByIzYH1piqcjVMJnUpGtNmX9EyNGDGehu1oem4BLYgHRl1O2cIvgFzV9n31IyUL5Mdfjam4KIxxM7YjxtoRD9CR1QUzbrRicrVg79aBtRpWzQpcwJZmmaBWCwmcgKMXLDtNBkLeGDPMtApwTZFTbZglrYy3XZTct4vHKicqRfytfMifRFFgmWroSS3VIhF+W4u8RzNk0IZke0qL0ox13JhLcpqDAcbE0VDj0nG1/6Jk6hJnCRCwI/Pm+XcQtMFO6KyCWzcvaIRU9C4dbmN8IUdaRLRL8vtZWbZpG4FNucVB+foafhOSs/H6SG05PA69rj9MdkdXKJLWOViHqa6xuAFb5znR7yZdeeIB3Fj7pgRnjnrcXcV92K1XMNlxmoXXmZHfTnz5i2TLkzmpDaE4GWRla2pbCxno9bE4qDVZ0y6Na+5JkbhOO0rlpxIhHCUtsdTfEhCVezqaq+I66Oy4unWqprG81ab8yqT+diVyoASL7Mip4mVeaR6MJnPfLwxj6h1anwL5aVlRR03TTiZm2ggg167WJzD8eezwEDH15RZ7gUSpHEvuqBI0Q6V4y4UNIxdpSdvlR1Lt+PUsV9zHG2XM9Ewu3rVHOQG59jkhOdkSBsjOaLwRTBuTYOL7ZSp1LJyG3JWUPnF7xNxThlnNT0s6C3vHLB9K3rhyBbVo2keEh6dXDSbatBs5CjtGGM4pu7tyeZIuB4RQLS6cDtHVspMoGcKxjB2dzHLkt5LV9DVl4bWqvmBwWWViZqqEaj9VpDTBGB1c7mgo0s4BbPYtTE082iSrUuZOmwuIXpZG5vTIcX1wsYlNpmuVb/gV0vruFWd6blXxzOupBf8Vdf0sc9Nna64Rra02p7zvpPQ8dSQY4X20RGdy/5+B9fUHaZr5am/BLtwu2cAA/rK2ijXcbnaa8vtqugbo+baVNakbtbobtRPVrQqlO3E3kThdRqtSNZutImw6yeO20Z42IbYlHPn3pQhyd6bUyzlMPuEX1bTnUyq2QbdCTU9m8x3VcVECgUrzrlllwpuc6kloy6B5tisFajzdLR317EwXgujqZdM2j06oVn5ksr9Rj/u3IaQOFrsw7F6LcvqShJnbgm71FQtowT2s14hO86Cizm59FYnwU+y0RZzrUt6NRb8Ai5l/d2IUseSHOqcIojZPuub/YUsk13n0/P1hhVmeGZnwQHYBEsHEahHm3Nirh3U3PmEX2cSg1GTrNP5kRv2gQK7MsdTRzxezg7XMA1lEzvQLVaOfdrZXPsxviFGXjg56JTHVL1KjMcjYJDbhSNlet3789W4P1ZBkYrCxVkVTdxsiVXIaKgY0btmcQl19+wdhWRBzXd2uLhMUT3NYibUJq219GKVStdyJRVStz2UFX9Neb6qgw0hQJeRDFweUFw7N7YMGhRzdYRNeJGj6Vkf+DLvzOb9fuWv9bLe8F6UHAVmVq4qwpfl8VGJd0q/pEQq14Ult0j3DTvjCHfVz9cCYC+zOd24wVLwDpHf76qRWHF5CNvt5HCijsl2ROw3dCXIjGFdIlQ+42m0OrmC2aPlZBKRCXW9Ut3ISl3vyE59lK9JDEevq9YlLsKVdRkCtn3CMR953CVF8UKORwcivDKYwU8OBy5wE3RqTdvaUSiPatt+0gRNtZv0BedsMbRjhSaQFIHqFtVlAfv+cBpB4DnrkkTSsDQVZQVXDJilLgITpc+wQJhUZzq+kB/oqzDCJaldGjV/2GAEXnawCZhdmo3PuA7DRAS1KC9mVU0EhV8Yfn8oNuJ0U/HZGgTyDhv5ynTnn0c9wWsn0PZWZCUJ1dvDiSmFgSLmdjTFE2E1zrT4eNhiTMmoqTMHk4D3TMUjg42Xq/zVGY0uzlxvXWt8WdMOOS/SzqeMthinegIDsOOXM5Kyz3Cxc+T2zmVcCTAJT/Y4Qtl9dd2gWG2k15nZllebmlglIy1qpznSB7QXqUZBJ+UKS5edcFVGuoxN5qk7i3qz7o50xMeissdOS1vnysSd9GJKXWl+jIaSjx/SVeu3eLo9bKuxeuhi8aKGWzXjQ7nXUaWyd2OhN2VYfXXb5TYH23T1np0ILAYi0V5uR6On56fbye7TK4GzDPH8NBwLPDb3//62sN+H+duDHsWRwvPT/7udyvuu4fsR4G2rH1ju6437698V9dfnp9IJoVj37eQqbvzHFuV/25f9/K/tGA80uvtR9XBq2dbv5yS15d+2tcPUbaq67N6qLG5um9rQ8E01/LeV6u1xwPB0UzDJh9OK7xW6H16EfvpWZ8P+bFgOr26nwQlww/uI4dF/HAXA8R30YehUbxTLvIEyHxR+HEkNe7jDmdTT7/8FDVvSJI8nAAA= -->
