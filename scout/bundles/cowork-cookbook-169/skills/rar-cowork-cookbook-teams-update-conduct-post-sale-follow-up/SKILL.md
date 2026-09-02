---
name: "rar-cowork-cookbook-teams-update-conduct-post-sale-follow-up"
description: "Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_post_sale_follow_up", "rar_sha256": "a0273dd361aaf2edcec3e669f2b9cc3795c8a15f77e6272f7aa546d293e47948", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_conduct_post_sale_follow_up_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-conduct-post-sale-follow-up:a89557c264bddcf93ad0a6e2aad2aad61b5ad6d23c7d600836a413831f131b8c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_conduct_post_sale_follow_up`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_conduct_post_sale_follow_up_agent.py` is
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

Conduct post-sale follow-up Teams Channel Update — Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 a0273dd361aaf2ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_post_sale_follow_up_agent.py` first:

```bash
python3 teams_update_conduct_post_sale_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_post_sale_follow_up_agent.py   # or on stdin
python3 teams_update_conduct_post_sale_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct post-sale follow-up Teams Channel Update — Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_post_sale_follow_up',
    "version": '2.0.0',
    "display_name": 'Conduct post-sale follow-up Teams Channel Update',
    "description": 'Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-post-sale-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ad8948a4c383e7a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-conduct-post-sale-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConductPostSaleFollowUp(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductPostSaleFollowUp'
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
    print(TeamsUpdateConductPostSaleFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPixrbnV9HU+6PtR3Uhob1u3IiRQIAWEBJoQW5HtfZ9QQtI+Pm7Twqo6u5n3zv2i4kYOgq0ZJ79/M7JzP7tye7aqKyfXp/2vl1AKzvL4sivIbvwoHl5KesU/JSpA/4gtyzaOna6tqybp+cnz2/cOq7auCzA9EVtB20D2dDBt/MGciO7KPwMqsqmhcpinOt1bnu7/9zYmQ8FZZaVl89dBTWt3XYNdInbCPCF4qL1a9tt47MPMZ5d3S7mdu2BKTV06mI3hYAcdui/ACn83s6rzG+eXn/59fkpBtdPr789uZndgEdPN2G0yrNbf36XYAcE2AP+yxt7rQIkMrsIwdhqAJYowH3l14BTDh55fgA97n5q/Cx4hv7zP9OLXYfNz69fCujx+fI0/lO7AmojH2pLu2l9D3LtynbiLG6HF4jJLvbQQLXfdnUxGqkBChThy33mN0plBf1zfPfTnclL6Lc/fXkqgQj2aOYvTz9DwARfnupuvH4ZqVQ//fwCFPHrn37+RqfpnMQH1gbEgNQvb4/7B1kw8NvQOLhx/Segeneo4395+k658XOXe9QTzHx6Scq4+OlOuKrLs1/Yhev/9PO/IutGvptmcdP+Jbq/3AlHvu0BnR6C//x8M/Kv0OSh0AfNf822Am79O5qA4e/snqGHof4V7Zv9/xvpLC785sPif0ruzyZM/gn98i91+3cTnqHgy9PCz0B21LaT+a/Qb2/7HTf/5ZP37eGnX38HpP+vZPZlV7s3Cm+5XcSB37Rvb798am6PP/36y6euArEGcumtq7M/o/lndr3x+cGCj1E//TgX8NeKtCgvBfQR6dBvZfW/6t9fIN3OYu/b8+YV+j5fxs8EGpV4Z3o3wXc50wBZv7Pjz0+/A5QogDYAC8bXIMv/4z+gTezWZVMGLbR3y66FgIPbOPdH4Q9R3ECHR1J/3Yu8JL3k3lcIPB3THUCE3WUttKrtGMBdXY4eHzUoA+jr/3ZvEPrZfUDotB3x6K27AdLbAxPfRkx8GzHx7Y6J4P3XF+gQAfZlHYdxYWeQyux2EIC8oh0Z30Kk6fLP55E3kCu+Y48650fcabrM/wf09a8ye7vRfamGUakvBfCSDVznQa2fV2Vt13E2QPaIWs7Q+p8B4AJkqcFkxwZIPH511ctoKSPyi4f9XIDjfu+7XetDWekCBYIYgPQzCIGmzACet6NVmzTOMsiLa2Cysh5uRQdY/nUk9vXrV8duoi/FHZZR6F5smikY8CEw9PlzVftBFodR+6Xw3aiEPv32+yfov6B/N+tGfOSxA0XiZjcQ2hkk7OUtBPK0y8GwBhqDBIDQzY+//X53yChdAaojyK44iP3bZEDtW1CMGty99O4ioPMool8/OP1oN+gSAbtAcQusBTK+ef5SjCRKMLS+xI3/bsT75Lvp331+5zP6pHnYEPgpqMv8NvYWj6Mz3bL2XiA+gD4sBdQFfr0V62gsz55f+YXnF+4AZtrtNxcWZQs1IIuaYHiGugaoOlL+6gDSo3FyAFV2+xXazHeg6pUZ+BoNdGMPZpdFPDr+EbT3x4BI/QnEGPtO4gXa+sCaUGXXdhXVduPfxgX2PSJAtXufD4jbUOFfoLHG+6OPbvl9i7z5v+ku7v3I/NGP3HsB6Es3gxEM+v/StIwCM6uVyq2YA7eAuO1BPd6ja2ywRmXvPRnoHG6Tb6nyrZt4B553SP5SZDHwSD384z4yuAXUfcwd5roaRIvKqDf6Y2rXN7pxC8Ji9HNdj6Fsfynesf8ZWAQ4pRlhDGRvOmJB+cFwfPsuaQRSdLz/1gdA94gbMwHEMlR1Tha7UOD73i3s26gek+phfxAj/phgIAvc6AetIEAd+B/QHx0RAyeB+nAz3RYkB+id7pH+MTweuysgBfAXkBZkj/8CGWMwg4BsIMcHXhvHACt8upGCch/YGIj4YeEmsqu7MGPT+xDQHn1R5mPIfOeBx0sQmGORAfw+sg5QtUGAAVtegBNAUvV3z37I+fAVEDYfM+A26Ud3P3SFvi9S/xgzD8j4rQCAPn2s798ZB8B1DWJ4hA9QedMG5HbuPwIIRMKtlL/cq/G93H/I8vqHTv+nv7cYuNVX7UfPvUJR21bN63R6r4HvJfDFLfMpiJG48pt7Ofx8r1CfH9n2+SPbPn9k2w/07+Z6hf6ejD+QeAT3K4S8wC/w+EqKXX+M3scHmGT+mT1+xsa3XwrV/+brR0CM2Abw1hk+Ssz7EFBnwtoPx8H3ktOMleoCiuMN6W4l4yMeHtkyIk841sem/C6LR51G796d94HI4FUxYr03dnn3VVA2it/4T69Fl2XPT4Wd+3919TMiLwhbYJFx4QRSCHRObezf7j66qPHmx/XeLbkAKnjl65hjoMqBjvcZ+mhen6H35cRtlVZ0YD31y9g4jyzBUPDzMfZjMen4T2AR1w7VKP19jTT2a48++o9CjKkFJHb9sY6XH7k6cvwDEXARhn79RyLy7cLOHoABgH2sjaAkP9K8AXJ6oKN6hoD/QPqBjAJA2YEJf2QD+NQ+QHuAuKO63+z3Ta3yrsvvNzO094Xmb0/vwDFe31uDe+yACX+7jRtN+15+30YG9kjm1mzdLH1rWN+AlvFYZr97FY49w9s9JJ9eAfr4z0+jPUHdyuLrbY39dJcKqPOt1QUUAI58bsa2YQoyClACxbwaVUkBBn7HYHwce7fx48Xrn/fHfwEQXm2KxnHSnRGY43luQKO2B9uEP7Ntb/wjEAcH394MdUmPgGEKJWwMQSkUCRAUcSgXCDP6NbcfwkyR0SNAjQ+z/49796c7HVBPZjgBCNnwjEQ9DyUQ2w5mvuf6LuoTBB3MHNp1UZLGXcpG8IAkfWJGzgLStnEMiE6jPkbSGDXSe3SNd+He3jv0dx/d8QHIlOfxKDqwgEu5JIJ5NGkTro/CDur6yAzxSNSHcRoNKMrHwPyPqQ8/jW686z9GMmgYQbt2Hvn89vD7GJ0EBkausYZn7p/5lNZtApWcPjInVyI48glVCvtDaQqn3NvOBL7pOmsmrflrsbVYRe7CuYFzx3DZHOdplm+tM6/4Lk/tHfrqFVy037QzuULknSRsj+7E3wXBtVCMBc/GXp4MbQqXWp9ZB/G6AeDvSNfNDJYapRYOnlGIeFac2k2wnKRNJsUtQk+WR1rq7KFJBSym1AOn4JEr7IJLKxiNHbedJ2nGJnKJGlGqFK4CEV3th5KfFpty6C1rfxZxxI2Nk9Z0+jz1k5Twdldq4hf1hfCHq2yC3+mV02raFg+nVjPDzNJn7YHIa8kgOiTK50MqrWWCzSYnmHWX5PHEB0oJo1w1TJCFSiYatxUPIbOYI4Qu9kEhyI5sypmbNbSuiwKuH5eDYTTcvMTQDa1Llh0KtSme93YXB7mviN1wPqxTv06svra9APaRFQgjU9otV7HO5+yQCDsVjfwez+R+KVZbwU6nUelqtUU6BZ9dl5Jbr40BbZfrcC3jgkemDIMWudC4Amg+yuVkwjXnvbOoYntZngqGOisugYiZVgZZIu0rFXFSo8HmXRwGVWLFymxeW1uVQCJSL41DJBzMelmmXX/eRkq0s8+HIa1Zfx37crzk7Xp+mM+PeFeudQrZ066FN3iwk0OLcfItgVueT5vprvE6Yj7z0QXndiuDX+mzoLWEfIO1tcwrkhIdV8uyEJaB4XCz1cRMWAtDPStTSibrLyrtKL4TI9L8VFGW2wdhncSYdjm7VdLOL2t046bVYrHv0YUkajTbTM8eCiPLSXcSu57api12nEhodCysK8uoXcbO9Gw15w2qpO3jpCas1kxR5yyfrh5u2/Flcmg2U5adCm7AlpM5S4e43nkiU2nTS5DLAjKhJjt4PgzyNTOLo0ot8nSYLoOlMRMPmmroxUJLU51o9/UxxI5pYDXbMC7q1UahUqm8HsVgaSmenlYytiT9JhOJij0U7jQkrhc0c9jjEDduYYtytlRgpt1jmqogtlotsWqFrS1uH2qoEYt0KIGMXTaG1lsZi80WMVLIuKaHXjBBKZBeLi5c9rLtcWicqvJeiyv4IIt6GPiw4xebQ725CiV1veptk6TbvJQnLWujO0G9NtdJsqMlz8BT112uj0V/nCxMUiTzYbaGcTWblZySOINwaoTWXHHXlWxj7d5ZzTisMsMAPa0SvIvLlKbP01A3hgSrEkkl6BMWEdeDetJtr56cOaGeRGtFciYJp1b0dOJ7fObqGKbokiJRA25ZGjFBKtakvf1Q4Zqt6SeMatBWwYtE4aqjxO5zLcn0ySEqz4aP6fOFezlsWZVYF/0WO8RS5RnCgK+ZFMVSsz7SfH+YUiGc7RNzX05LkwoFXIuOWbVtWy8hDutC9HmjoZoLgvE2MlvlC0s4bOWcI1S+SXWD6zzZwvvakbVLHLa0w4vB3uo5AFQZknbctuL66da0bDhHrVOSoIfTQjIOpr+luxibep0EFpK6Z6UqdpitW2dWNxydN2a7mtDEbMbiOTWZXHaSX66TSaqnME32x72wiesD0uYn0WPWSJmvza5aFGmh5v7y5HYGVrpY5VKLodjoZ1cZYjxQNZCKyWW+ctEyE+Sj7e/QRt8U6mmW+OhELIRmArvw0Y2POLNiFruMjYurQ+63bEhdVkiOlyGTAYRTGw3hZ7W9bQnUY6zNylAWbCsOZVSltraBNQMWmOs5metKexHVtehbZbVCJHtL1nOAFD6HeKHWBM2Ob4f2LOnO2iYwurcKIcPUupbPBTLzz06Mlf2RyTnrRKxr+uz1+LHMUTxxnd0RWzNhpxW1AfPu1MD31w7HEw9rlqobm5szeqoRmhIcmt+dpyd3qpmEsls6l9qeNA2JIorLnSK9mW+yra3ifCLXp9XhhOt84R2t/ZaenGs848zZZQ5ySnOn3HzDHuucLEHOHFP/SHuhAXJ76xhYnJ0oSz019rnSd3ECV4mYnDJ1u9QnRpVXp6korSMUSQHybOiI5WZzjwflmqewqUw2Z0ENGkM5ZSc55TF4na3Wboo4TojIGaEL53VkX40gT0Nk2pksOb9uxDkNZ9nKaAmZmyYbZ+O4ZqMct2VlTfSdmQhiboEEPSQdes33W2xPn3ucj7aHhkVLUIEzCa6PpbOWM/iMTzuh4/1lVXFBNaNjyp2bm2PnClc31TbFgYOVCivOCRphjCCeQq6c0S3r6lzOKAa7pbS92azkeblWDxe5tTO9OwnsTiuJY98nxkqmFlIhnpa6uTP58/Kq9FqukQRd1kg1RMylSXxGZrgzg+WiNYgHzyKa3WGSRtzaFAtlFa9BQbLT2bG1w9LKsf1yXoRlHhDni+bXm9lKhaPUDbHLehvL3JzvrFY8DppFboyhZ9RF6rOIUMaGssZIR+sXpCAiJJ23ZzVqd57H2ZWthzvEMawZz/LrTj1t1HyD4xLiOQmNkxvOLA/GWtwX/SKByXLQYnqvq2rs+8ftQl4awV5QXJgW4W4jUFdBtiVns6Ik/XQy+LKEmaWirfVcl3wuvPCsYEzmOxmpCWVQIk1ZBDA6JeMZUvjbw7YgZHWOk2LJ1SzuoaVcRXyhZa2pKtY1QNNSnU7cQBLNnr40IPC1cu2FTmEt8JBPqhkOoBKsSTZtW+C05UktvXJWZjm4B9FASY9spAVD8vCRgREcpi/DXEx0jpF2bLiZJN3SFCmDncZbJZ3xTr7iiTjGvaK6KnZiaMJ1G2i1YecV0meiHJ0ItdhzrV3q3PpEZAcW9KEywAo9pjGiQrU6G07J0cGHk3vc0pcsZMNhRS1Ryb6gsFqpFznniaVixnkd7XJ5vU/3Eq9YE0vOtZVAxezhuEyRNZHDQS+ctaXctUMuXuZ7w0m3+IbKKoe+RPly4M7LlZE6vCIz1tVhaiae6Rv8sGH8bukMxyiDU0VKzMgDQ3g2QhTBVM9cIaaeLscrVJ6IihWvV9qKqOy1scaW/oKIhL3XxDldRMkm5OxZJTWXRjezrSkPfmVK12XGtWfh1E+bSW6nu6V4svQmotMNppt4jiYNEm4rfOoL9iZQZV3QS3XbW04PSugeXxLmCvY8sk7sXOQOU8HmvAyU2IV4XVJtacbmcs9hSyzFspVw4ZMFyqNzhefILhXK9Sx2HfF4wjvrGOKikznyXFNWcuDRFnJcpQgJ09eK4SykXQUXeqsfUAFdy9Ie3mgrIzByhNUyNhCMVuEmSqDLm0ptFC6xF108D5Z+ju36StvbdgRjZQrHijUUSOcbxhaNpVbMenFVLVxLOkda1c2yhA2AgKvF1gx4I3P7iFIaW9sD0CLKgVkKU9oEHYpimH41850c7ad8BhvbrKjCS9bViTqPKpGdZd4mcQODWXPzKrtez8rFx/oCh8XgcBwYF9uhmRlh6HBoUQuelaK72lA71rZAzyqdY7DuR8sJjhDhUBy5eM5G+mxeTQp2uVuYiZVZsDrzS9DPBzOEVYYrvW/wUuFladvylNTM9KHq4p4hFmEJL46w5l/Leb70PNDlLuMoH9zc7LO9d6anLI+YAqoyBcMIGZlZvVMm+XJqXbYb0Y72/fJ6bQi4Fq5EzzeXq3iWGVeI7CPmc8cY666H7Wmw8SmVzHZdLw06HJ5D9XhmWDvYLB3qnCQn43Q95zCnbIXeFfEJfPDmiDeUp6uiTAl+E5lE6ZFbka7b63mQgVeuoX+2EQedkDDVWXada9OZDvumWCP1FOu83jUvOEwis3iRODMEOxBdGlaVbXqdsq0Q+2TBwyw5wu4yLS58p9KWRoIuso3P5vHqXVvNP0zJHKwFrf2G8I5FtLj0Dt1y1oSvSvU6FzsKBb0gbNDEGdusTJ4gsZoqrjW6PQr0AemnM3mH+kGxDkupWWzPjukMWdA4mrFOTtd2KndzKrRxLlhjGpF2dOIsAPSmblCdpygxRzHmvJCadkeaO0rdScSERq4oca5rdrHSyYk2C+mw0hez3V7z2WrjapwMQKhgChfeGMGGo9KLMu9NqmuqtmSqHsbxeA2Wtosh314cduNGE2eDyS1pVZXX4eh11+8B8lk5iXjrENNI1og763JaytJA44dr3PXz/dEYllHWrAOYx8+rvR4s0nqGnQhrTotTltpeM3h1jf0zioUEe6XP3SSUcBG3UUOtJOGwOPGXKwL63vOiYLOBsaWJx7rqzilTI6LbFYXL2bRogzqYNH7Fuac5WXe7I5tf+KK5THQENIN7r5xMrNiozbp15RUIOMbrxA25Q9ogGI7tpExOeB/6LkqcikRcB4hre1SYb+bzMwsyqfGljVJgBW/N15yUeJFA886hQeINWku0ddhMw4ZjV51dkLDQ78lEpGjtkEwXzPpg+BvXUBcXfXXeRy3Wyv6lnXMmzuF7st8WATr3bTaSjrIZLRrqBLtTRKH8YGdZK97pmKnBGoudS7rTFcrinMszFmpS6nHd1mGpLVaqs9BWa3xyKXRPciNxt4YzaikoiXuY7hxv4RxpFJmJkRNtz8LsYJYlPuTznmC8bAJX+eIy1+euUC/hANsOhjQ1GY/06tTLg6BjaPck866pUPx01bA1C++ShQ5ju2aRU+uVZS7ss1cUOdbjBLnukHAxZ4/bVqUBDK/I8uCtSL7wc8IgYe+E8pYdoQFlZsSaL+DtecnM1v5SXISFRDbKaoLLGKwy1n6HufQKh902newS+NDsLY/WrpPYiy7BgSxVp2e28w4FK1HXRNsOmaizhe903dRyKtSc7gbzco0vVzRArydtJzLmdnqdR6cJ7tU0dyHd01bCO0ImdihlYyuCWIM2v5kkKCaRU5lTSDxQfJTSSYIobWUTiLIdnmJGm2x1DwZmoeKeWpWzE3WU9P6aoRewdJ0Iu0u/Yah5yu90mvLlHd2XcVSbOdntlK3vCV4so0h1XlLJYqtjPIxdteYgrXYMWh5nHccu2NATmLCH+2VO5suSJWw7aDtmIJyArmUzKc4aWCb2q3BusO2aznYN5Sk96QUJxkvdTCAHCZ2t01CSmLUrLSLHYdcLYlNuKnJoZqEVssXizKdMT59mGCIsUIEQZyV+2jT0auVaOxnvZOc8R8kpoa6XFro5s4Hdnnanfitl6DqewkNLJkHYDFNraHfuQmmSc6YfWiNL9Ki3sXKaKaw2xffWoT4XYC1YygEywxZLRu0vjVy0bCys8q5nTuROyfhpLGVbFV+u84JS3WsCiNfdEXPWIrHzO3UgyAQ2KWZRy0xfbyqGYf759Px0O/l9ekVggsSfn8YDg8e2//9kwzi8xtXbgyJKYujz0/+7/cv7XuL7AeHtGMC3vdcb99e/L+yvz0+1GwPB7lvNTdaFj63L/7Zj+/mv7iaPVIb7gfZ4rtm37+coYPFw2/SOwdSmrYe3psy625Y3MH/XjP/BpXl7HEA83ZTMq/E043ul7s+bygd6teXbqStvz24HxrnvxfbHbfg4K3h+8gbgytht3lACf/PratT5cWY1bu+Oh1ZPv/8fzXqk5LwnAAA= -->
