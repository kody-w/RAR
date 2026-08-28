---
name: "rar-cowork-cookbook-bulk-update-define-sales-quotations"
description: "Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_quotations", "rar_sha256": "5e0f072c20eba3763d675a113f1bfd38036dd69bed5ae43c0632a1635045afe0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_sales_quotations`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_sales_quotations_agent.py` and in the RCI capsule.

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

Define sales quotations Bulk Field Update — Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 5e0f072c20eba376…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_sales_quotations_agent.py` first:

```bash
python3 bulk_update_define_sales_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_sales_quotations_agent.py   # or on stdin
python3 bulk_update_define_sales_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales quotations Bulk Field Update — Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_sales_quotations',
    "version": '2.0.1',
    "display_name": 'Define sales quotations Bulk Field Update',
    "description": 'Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-sales-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c937ab11d2770c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-define-sales-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineSalesQuotations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineSalesQuotations'
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
    print(BulkUpdateDefineSalesQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjRrrmX2HO/WD7qqrEJhDV0REDEgKEALFISHJ1lFmSRaxiFXj83yeRVKfs6+477YmJGNVyBGS++a7P82Zyfn1z2iYqqrfPbyZwckRw0jSOQIU4uY+sir6oEvijSFz4D/GKvKlit22Kqn778OaD2qvisomLHE5nyzKNQY04iNumCRLEIPWRtvSdBiCOVxV1jfggiHOA1E4Kx93aonGmuTVSAa+o/BoJqiKDCyNxXrYNksZ18wHp4yZC/Gr4WLU5Ulagi0GPuCAoKgD1ybK4+QRVAXcnK6HUt88//+PDWwy/v33+9c1LnRreeuOgQoeHJuuHBuakgP6+PpyfOnkIB5YD9EUOr0tQwRUyeAvqjLyufqxBGnxA/vM/k96pwvqnz19y5PX58jb9MaCKTQSQpnDqBviI55SOG6dxM3xC2LR3hsnUpq3yyUs1dGUefnrO/C6pKJG/T89+fC7yKQTNj1/eCqjCQ9kvbz8hRQXXg+6A3z9NUsoff/qUFj2ofvzpu5y6da/AayZhUOtPX1/XL7Fw4PehcfBY9e9Q6jOkLvjy9jvjps9T78lOOPPt07WI8x+fgsuq6EDu5B748ad/JdaLgJdM8fy35P78FBwBx4c2vRT/6cPDyf9AZi+D3mX+62VLGNa/Ygkc/m25D8jLUf9K9sP//0V0CnOrfvf4PxX3zybM/o78/C9t++8mfECCL29rkMYdzA43BZ+RX7+ae3718w/+95s//OM3KPr/KMYs2sp7SPiaOXkcgLr5+vXnH+rH7R/+8fMPbQlzDTjZ17ZK/5nMf+bXxzp/8OBr1I9/nAvXP+RJXvQ58p7pyK9F+T+q3z4hRyeN/e/368/I7+tl+syQyYhviz5d8LuaqaGuv/PjT2+/QYjIoTWt96z/z2//8R+IEk8gVQQNYnoFhB8Y4CbOwKS8FcU1Av9OtQ0RCFR1DB37Ggfzf4rwpHERIL/8T+8Bmh+9F2jOJzT8+sTBr08A/PoAwK/fAfCXT4gFRRdVHMa5kyIGu99/yZ0Q5M20LES9GlQdBBR3aMBHCEUfpy8QJpFf/g3pXx+CPpXDLw9Qj58YZaykCZ/qNgWfJhvtCOQvizwIweAOvBaukRYeVCiIocgP0Pa6SDuIb5M/6iROU8SPIXhDPhgesqHPPk/CfvnlF9epoy/5E1AJ5EkU9RwOeFcH+fgRWhakcRg1X3LgRQXyw6+//YD8L+S/m/UQPq2xh9j+igjUcGtqKgIrrM3gMBgsGF4IH4+I/Prby79QTA6ZDcYvDiammibDDE2A/83Zpsh+xBfUN36BPFJUDURpBLIMIgXIu75w0enRhONRUTeQ2UqQ+yD3BijVgea8ezIvGkh4TVwHwwekrcFj1V/cynmomMFSd5pfEGW1h6xRpPC/Sc3HIDi5yGPo/vdUeN6HQqofaoT7JuITok45iZRO5ZRR5bzWCJxnXCBbfJsOhTtIDvov+cSQYHLVI0We7oGDoGe8V0g/TjF/MCwMbP1t7ccYZ+I268Fx1Ze8fiW/U4EHkUNVBiRsY3+ihL+9UqqOiha2A5P/oKaTpFcU/FdUHjm4/hf9wcTfyObRUDxpHPnS4ihGIv//eo5JXVYQDF5gLX6N8KplnJ9unJqkyd3PvgpyPwLnPUvmez/wDU2+geqXPI1hTlTD354jH85/jXkCVVtBXxms8ZAPIw/dOMl9JOaUaFX1cMSX/Bt6f4BeeUAVjA2sYpjlU3J9W3B6+k3TCJbqdP2dyV/emWoaJh9Stm4KEyMAwHcdL4FaVVNxvYIAsxRMhdZHsRf9wSoESofJAOUjUIkYlgtE+Ifr1AKaCevq4f334fEUFqiF33pQW9iFgk+IDetjypEaBgA2OdMY6IUfHqKQDEAfQxXfPVxHTvlUZmpcXwo6UyyKbEqK30Xg9fB7Rj90mdSHUh2YQtCX/QSyPrg/I/uu5ytWUNlsqsHHpD+G+2Ur8nua+duX/KHjO67D0k4nhv6dcxBYUln9wNIJmWqILhl4JRDMhAcZf3ry6ZOw33X5/Kdu/ce/1tA/GPLwx8h9RqKmKevP8/mT1b6R2idYBXOYI3EJ6gfBfXwW3cdntX18VNvH79X2B9FPT31G/pp6fxDxyuvPCPYJ/YROj3axB6bEfX2gN1YfufNHcnr6JTfA9zC/cmEC1nSAjPrOMt+GQKoJKxBOg5+sU09k1UN+fMAsDMSX/D0VXoUCUTwPJ4qsi98V8INuYWCfcXtnA/gob+Da/tSihWDav6ST+jV4+5y3afrhLXcy8G/tWybMh+kK3THtd2DpwJ6nicHj6r3/mS7+uFd7FBVEA7/4PNXWB2TqVT8g723nB+TbRuCxucpbuBP6eWp5pyXhUPjjfez7RtAFb3Dv1QzlpPpzdzN1Wq8O+M9KTCUFNfbAxOPFe41OK/5JCPwShqD6sxDt8cVJX0BRN87EynHzrbxrqKcPe5wPCAweLDtYSRAgWzjhz8vAdSpwayH9+ZO53/333aziactvDzc0zy3ir2/fAOMVg1c7CIfDyvxYTwQ4h4kKF4TXz5SCz/5vGsWXCIhysEuBMhYADVAa93AUuA5BU4RP0QsHw4gAcwOfWKIE5fsU4wJ/4QCS8FCKwB2MIhYouXACMKn0zM2vT1qDIqFEQDAY7vkEhS8WJIPRuMP4Dkk7jo8ulzRKBz4kgu9TEwiRL1uftk2OfO9ZJ5+8TP71zaVIOFIka4l9flZz5uhQxM5VI3dWUQFbX5mkoYuEOrmW3La+VlDWeBisS4uh2h079f1xa/JbldfvHN5sqL2qiRS3x83gTHMzbpNqQ0L4+cXxnOaiS6S2jk800YtHjuVD3L8VlpJW/HDcgOXtsCzNbDnIJXak5MuiSk03bsfBKA15Pu+GnabQ41HQ4g0nqDsiXnqtMuyKAZOqdH2WN/FhMOwdexs3V8nS6rY63Cy4VVHvldceTalSWzkcEiO4mbem4p1sI19MaTzdmmGZht5+jO9+XsYzjSiXc54CLXEZGeWu1se1DdIhKaIbsU1XKdZyG2fr3ewmFg6ttCBMZX4/nnP5iNNb3btikn+0pHO3563jWBzVo6XIgjxQpR5bIb3P9ne+9Up7NaL8itmtVqTc1NtwZ2nMQdR52VkczqeNmVwqkr81OxS/iwVtAxlPT4zog2zVHgfzbhNXuTetHbscStk3e9uMbeO6mkX8oCfuflR6eZFJzuKkpYsmP/isV/ERrksyxcnz6qqd6d2Jm7lyWhPJaF+UsRYZ8+5zY6kXGO/PussqDQO9HcuZ4yzaNanfzwkW3nBLd9QzwORFQloHbBiccle7zPnARXiFLiOzP0Vkfg1TU2ilhAzPmhsLmKvy3QkAd2+NYyGYzuIKWvvkdgHF2xrhGbqIX5QVNZjHS+biQXmVV2es3cUb6eigrXCP6EtpHKoaO89OLbc43O172Ni8poH9FYbQs3fkbRUIJ94lrfvgyaTVr/AhOlszG98yq3XMoNxOOTARO3RMh2OHoR6uMlHPEnRR2PfT6HMdvzR4qzz5SblVc7dUT5eFCpylUPkL7HKqr2vd6lB8UYV60I/7u7ffhsuQvRKz6Hw4j1RAr/khuJbrmTI/E1xfphWkJ7+qu1IwuCYi0V1eXgj7gMqLE3e5mRd1zZSCv+BaXimcu2ylIcqarEVG5NbV0jpWybLUchiSoSSUE7G9p2Wk2zqWbStDUb1DSyr6ilx7cj82bL/hg/iSrMSVMCz1LNwod/6g1HOxUsjDtl8I7nWwHPJkkH6gqWDvqLNhj+6Tq78nJdxgIoqcRemMb0xbAv3lvKdmYNvkyU3FBeaOBld3UFnNVykyWM4NmTx66UZsuwFv5e6UEtuyDsp4tRoKnhVcdHtDpcgWpVFQ5LBLKx3l7PVmho7q8qSBVMBRjwz9umqlYcfidMTNb1d1C7bHGx4My51tz3RXY2XR7/olzSx5p4jFJcWcrmI2FURxUTHsalAdVSfF8X52ajvf0upBuNAHvq+wqpE2RaKmR8JiAdhzJ1bE6yiaFbOAw+6mgKKRI7qdt9qPB2tpumVyV+47ZrnWE+vq6sW8P+bSOJM7icPx+Ult5+ft4g6Gu964+t01HafLNjZqnsngLsiJcUJlFJMzSzgeHF4/6JZ+Y3QOwwXP2nKzo29UCelwkjcySzs1btgZX8xunJrfZLwWWlq7LbTrZlzQl/SyMaN91/s7yDDFrDjg1RbSyEpa++2cXuNzUlipM1rvvbkgtXSCSasLZOujsr/nuWAWOi+B+WAUrLXugcWeLZQuiIEb1nu7W/F1vBUsfi6iHLlRNdm/JsQ66cRq4deSd3No66R04japCWWpexlnsX0hYxuhToaKMbZatRrxbUJdWDaiTN3YjnZowx6jIQ6e4rNOWHC3RpakGzuEMnGGeR1rNd32Cc+XHAT+1cD1JjjQ++OFdJnoTkDsk5OYKetNFKNMxGP7puup61GyLJDVKM6AvBxm++syTRzOvGc3zw/2dLmVlUNFEtkx70w1tGCMC8fC5stS2cQqhou7WuUNPTotL0EQLM5GuAy2xRLsCVIPZof13VzKQrNOU8Ds1mESbrS7dNPvTV53Bzncyt3xWrR8wXk71T/yaOpkve+tBDQr8hMp12cbZr5mHZLx7M34UDwOPKfW94IVQ4299xa7rsMtrexXmSppN+t6QNdkO/oRN6P78YpX0jxLrYznLcVAr5TaX1NybbX09j4mVCqzVcVf115UlJFG7b3FtkfdQ3pTrvFp4RV75mhRMj+wW7at8EPrl7mJZzivGIscS1btVlCkgTfmCwam+yEDKn47n1R0v62212ZFtyK+MjjRvC3OW1Fj6C70YwM3xCvo0a3eWmRy1smLfvd05bIsm3XkXk4pLhl+KsKttrKvRdmsuF1zwU+4apkpSyn8WS9q2SbvV26RXZctWhwFVJb40yrb5aoRAVLZbgUppje3RViA4EZuteMujQdbhhstKRo4eu2S5nK9JksxLA9pmi69aqdToYvJnFcOK2eB20dnpWWqa1/iTjnPOE0JNl2GL69VekjLFZnwd/0C+MgnyApr7HtS2taWTnDOpoX7/JKVu2w3Ux1G01vxmsoEd91RF60aDVU9N2a/p9QqWWykq0mES57VM7DEOp65L3m65PeFb1Py4TqkxjJALzKr23lSnm6bo8XZzgA8wRZLZyOEg73djsauCbGQNfr0xhf62V/VyvrGSBtRMuN9dmNn9Mo350wxFEYWyierYgiO64Q9Hl4GRVxzh/stXGMjYEqKSRv5gm0csNtqYtfN6eWxC+ajJm+160KyF3tyVtMGa4nHVqGpzsRR/bLraBId7Mtybx+6KKHyvmnwcp4cHZE0pIHzK6bdsQkvwZXCSgWRNzBNepIGnFvGiiXYBYhUrhUXGaNYTr4S6nC1vmFC6dZFeVzkZ+3CLo1jtRJuJ5lyQ+pwWsGYG5yZ2/GGMYM2xxcH2CCR1HGnmlQCO5zgvF7xNFoC58Teszbrdxy/IMtbcsWuYZ9gm0RQZ87txnPG3RIW/FUAucxpme7sqYSIlfxkL6w1uqRkGrDzXRYyXKAp68E/7ga7Kg9cjlIlj6GmYGZ+YetCEi+W6SXsTWEX69Ge3oY1k4nj4m5rN9e8pZCONYM409uavyjkjKq9Y0Zw++2i1Pu5sUMBaomiq9znh3Tj1uyo5gZ1NuUqjlv7sj8MCZWNsd2jWELjwbGwcA3c6Csthf5a6525IjS+SSxdZr0HYuLM9nXJVccRqzcBzsuJJZ7pO4a2mXMrSJOosyC+XZgBxTNrTzS8tqJlKXPb45UvI3MjkeJMdIT1RtxQFhWRxXoYEk+WHBxw8bHvc5bwpONqvFAYJuqYM+aVL1h4fNm0yaIs94Z0wanlPJzR25GvPEZqTnqkHy8zt9K3zmGrpJBBrOUqr71S5+5JcnHWJctyqZIsinsxi09yfF4WDdpuUz09djXgN0SyVet22JFkQo75ZbUdVZWW1/Med5Vr0s5SX7qIazYmlwVZNZejWZpbhiDT3eIQkntvi+N6RZCNlC58LO+qMGya3dVYxYy8Wm1SvqyjU5EVXHkkxiCsfdK40tgqOCtX1lWCClp3OlAjcwfSUFrKSll25bbUDDEP9oG52+vHww4TU7w1jrYRpfPttr566ZzFYqe8oDsnKPzGMDh7YVIHZjAS9HraW8bg7Fcn+VZHcYoL7OKsjZy50PhDt0nuYaXIm7WakIyRmGibwz0bJDzxKOs4Kzir69El6d7PjVFYNoloiGxrSi17S4Te6/fNZuWvSNgMmH2Ol+s7icZc2VGCcSxP2IbjVby50jXQYh+fSTNB5Ch044MTarKScxXaupg5WXoN6MpqYCtaW12cucLcoCOrdAseBMlqToJVO+T4ePSDKqYvApNFEOn9E1YRSsvAfd7eP7kpbjLGBb93VSWslke+2baEjaIkZpwpn9ZrqV2jEKs1rlscqluVX2q7lQAkmRu+rZdjtZJu/FW7yhxprDx3LoxhEBuVop2i4/GGzYX5eNora4Nj3awJx/omqp3tx0eIX7J4yOYNsatxEOFXkmDuED9SHKhR0Gm0PCxdXRv6zlz3y9TOdt0Z72m7J8Wc3s1ny6s605WtWe2s2TjOeWsAZed7DE/PlsaVSbVlqnJ7zwQSsCkowmNESHD91eIYj106AbrpeP08Y07LDJWyFYv2lLdks0xE14nkJsSKJfOFMl+SIldlR4pMXcXf9Gp9G7ZjQe5BP+CoHWeXXhbb04Yer7ms9I55FoZNuoEVfThHXbbeBIzCUUHaESslD8KOmsUUB+5KyHToKVzSO7dKdjOhPbQmrhXsZsno4Ww+zsuW7f21Wl73s9aJnYMvFp1oVO2xCBZwA5zPK5EASuyN5bar2bTgizr0YXOIajP6Mi7HJpPa0WGaApzvvHveNPfL1ZkxKQXoO4Qcp/FJ7aBqtX9X6GBPEu5irdb8RmNztzvUmdTt78oh5jVJ2OJSjoJG3uHSrBX2i4y+nSKJZTwsBl2JSwK+PZxuJAA2KVIeR14iRdxH5pnud85d2WvhiZ/AP92J4sk7OZyHzjk7NLpY3JCHgzc/hrD/Egs0O4weRxXrxHZifIZbrTVIZ2nZt20S3/JLHiYYpdUjXXg7yr9rtypbMEa7y0+9JSo+Bju3BsVmBh6IXrRopYzJHU0b8uwSuiOwvCJbeI02G/KY2wB8HFddr11o0q3Oap2pWFdFKRHrRTR6qu2S8nymnNyzgrlBaDB7Vyx2m+VmO1vcgDses6sXOEKvF5u5aYuu1Xi0FqLYprsxcMtbET5On+MeW+e7oosoQarQbcft7Q1gMa43GgZ2a4FNnxODvZj7ZDFTxpB0pDMQw36ZDDeqPDVbeu3NEkIniZgFvN+1wyoMAtt1mT6f2zutnRm7kjgFKHWaW3E/EsHJr057eXVS5nczus2WTbU0+tGrsV3cUgalE3RM4hSZE9q2no0EuaNnrgLy3ex+aUn6hO71PpJmun/WbzF7mKlHgDFZwNj3hirwxFaiG7VY0Uuvi+cbkXSy0ObMZH+jZlqWa/3ByI8lQ9FiN3QK2V3OLrXE4vZMZBC1bkuhMLbNPGUNVKODkBWKweaTu+mhuNd6WiReshuFY+qubSh8iQG8pQq69mLMVGrV2dNKoC6o0MC9fdRXdJxt87tE5HTGbq7hqhVLPVVDJmOEo3a4MvbFRCllBLhthgE40v4tAcPJH44VnrcHcK0UKa9ORG4SvT8wHGvSIxhsskIhoDTXBM0PJEHai1mAQk5PfHuebDkC68cVOeqll51rWx0C5hBu1syBOlPOZe7aOjO27Yn1SA73rlxH64eUK4tWD69nym7WS87zD5kfUVtCONEJOVPZZgRCYrVRVgzaCTZXkCTZJFnMOzAkLMv+/e9vH96mY+nX4fJfeXM8Hfb9PztzfB4PfnvV9DhYBo7/+bHW57+k1T8+vFVeDHV6nq7WaRu+DiL/y9nqx3/jHcUkYHi+kp3ei92bb4fxjRNOv1f0Fud+WzfV8LUu0vZxwPsBOrGefsWh/vo6yH57mJaVzePZuynP23UJvOZrUzxsme7F+fS6B/ix834Zvo6cP7z5AwxU7NVfCWrxFVTlZO3rvQc0Ev+EfsLefvvfiGkkn78lAAA= -->
