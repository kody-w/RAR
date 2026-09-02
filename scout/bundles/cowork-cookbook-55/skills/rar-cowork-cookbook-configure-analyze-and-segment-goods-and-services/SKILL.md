---
name: "rar-cowork-cookbook-configure-analyze-and-segment-goods-and-services"
description: "Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_and_segment_goods_and_services", "rar_sha256": "52b85d1af95a4fff44fe2b7276691645a139fc9a1123dff49a26016cb17af88b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_and_segment_goods_and_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-and-segment-goods-and-services:fcf6f2df4884039b6b2aa42b9887c9d5522cb73447d1e82d802a740afd33ea70", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_and_segment_goods_and_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_and_segment_goods_and_services_agent.py` is
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

Analyze and segment goods and services Configuration Bulk Setup — Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 52b85d1af95a4fff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_and_segment_goods_and_services_agent.py` first:

```bash
python3 configure_analyze_and_segment_goods_and_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_and_segment_goods_and_services_agent.py   # or on stdin
python3 configure_analyze_and_segment_goods_and_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment goods and services Configuration Bulk Setup — Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_and_segment_goods_and_services',
    "version": '2.0.0',
    "display_name": 'Analyze and segment goods and services Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-and-segment-goods-and-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e433b724985b2148',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-goods-and-services'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-analyze-and-segment-goods-and-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeAndSegmentGoodsAndServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeAndSegmentGoodsAndServices'
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
    print(ConfigureAnalyzeAndSegmentGoodsAndServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZebyJrmX2GyP7iqlU6xL3lPnTMI0A5CArGoXCfNDmLfharrv08gKdN2162eW93zYeRjS0DEG+/6vE8Q/v3Japswr55enxTPyqCFlSRR6FWQlbkQl/d5FYOvPLbBX8jJs6aK7LbJq/rp+cn1aqeKiibKMzCdLYok8mrIguw2uY31o6CtrPEx5IRWFnhQkwO5VjJcvZv82gtSL2ugIM/d+nGn6iIHSPGrPAV3oCgr2gYSLo6XQH6UeM9QHzUh1FlJ5N5Fj9OqPElsy4mhui2KvGpegHbexUqLxKufXn/97fkpAr+fXn9/chKrBreeuId6HnvXh81c5a7NYlTmdnlXBYhKgPJgTjEAT2XguvAqP69ScMv1fOhx9VPtJf4z9O//HvdWFdQ/v37JoMfny9P459BmUBOOTrDqxnMhxyosO0qiZniB2KS3hhqqvKatstGHNXB0FrzcZ36TlBfQL+Ozn+6LvARe89OXpxyocHPGl6efobwC61Xt+PtllFL89PNLkvde9dPP3+TUrX32nGYUBrR+eXtcP8SCgd+GRv5t1V+A1HvAbe/L03fGjZ+73qOdYObTyzmPsp/ugosq77zMyhzvp5//SqwTek6cRHXzL8n99S449CwX2PRQ/Ofnm5N/gyYPgz5k/vWyBQjr37EEDH9f7hl6OOqvZN/8/59EJ1EGEvvd4/9U3D+bMPkF+vUvbfuvJjxD/pcn3kuiDmSHnXiv0O9viixwv35yv9389NsfQPT/VYySt5Vzk/CWWlnke3Xz9vbrp/p2+9Nvv35qC5BrnpW+tVXyz2T+M7/e1vnBg49RP/04F6x/zOIs7zPoI9Oh3/Pif1V/vEDaiATf7tev0Pf1Mn4m0GjE+6J3F3xXMzXQ9Ts//vz0B0CLDFjTOrfHoMr/7d8gMXKqvM79BlKcHCASCHATpd6ovBpGNaQ+ivqrslltty+p+xUCd8dyBxBhtUkDLSorSiBQD2PERwtyH/r6v50bxH52HhA7fYdN7+0BlODbfXsA5dsNKB937uj09QVSQ6BGXkVBBGZAB1aWISsYYRUocEuVuk0/d6MOQL/ojkEHbjXiT90m3j+gr3930beb/JdiGI38koGoWSCULtR4KUBfq4qSAbJunWBovM8AiAHSfED0+E9bvIye00Mve/jTAVjvXTynbTwoyR3rjvb1M0iJOk86gJqjl+s4ShLIjSrgwrwa7tjfZq+jsK9fv9pWHX7J7jCNQffmVE/BgA+Foc+fi8rzkygImy+Z54Q59On3Pz5B/wH9V7Nuwsc1ZNA8bv4DqZ5Aa2UnQaBu29FNNTQmDQClW1x//+MemFG7DHRTUG2RP3bHZgzWd0kyWnCP1nuogM2jil71WOlHv0F9CPwCRQ3wFkCA+vlLNorIwdCqj2rv3Yn3yXfXv8f+vs4Yk/rhQxCnW6Mdx97ycwymk1fuC7TyoQ9PAXPHrjpGNMzrBqR04WWulzkDmGk130KY5Q1Ug6qq/eEZamtg6ij5qw1Ej85JAXRZzVdI5GTQBfNk5APVoyuC2XkWjYF/JO/9NhBSfQI5NnsX8QJJHvAmVFiVVYSVVXu3cb51zwjQ/d7nj2QDyrweGnu/N8boVu+3zGP/NRbC/UBiZiOvUQBEFdCXFoURHPr/ivPc7FosDsKCVQUeEiT1YN6TcORt45p3qgcIBwQIy72ivpGQd7x6R/IvWRKBwFXDP+4j/Vve3cfc0REAhgvw5nCTPyJAdZMbNSB7xnSoqptvvmTvLeMZOArErh5NAEUej5CRfyw4Pn3XNASVPF5/ow/QPTFH00HKQ0VrJ5ED+Z7n3pzQhNVYe4+4gFTyxjoExeKEP1gFAekgTYB8CCgRgZwGbeXmOgnUEKBc9yh8DI9GUga0cFsHaAuKzHuB9DHnQd7WkO0BZjWOAV74dBMFpR7wMVDxw8N1aBV3ZUYu/VDQGmORp1bjfR+Bx0OQv2NvAut9FCeQaoHYA1/2IAig9i73yH7o+YgVUDYdC+U26cdwP2yFvu9t/xgLFOj4rV8A+j/Sgu+cA1C9Su+ZChp2XAMISL1HAoFMuDGAl3sTv7OED11e/7SB+Onv7TFubfn4Y+ReobBpivp1Or23zvfO+eLk6RTkSFR49bcu+vlReuDb/fwovc+30nvcuZfeD+vc3fYK/T1dfxDxSPJXCHmBX+Dx0RYsM2bx4wNcw32emZ/x8emX7OB9i/kjMUYoBPBsDx8d6X0IaEtB5QXj4HuHqsfG1oNeegPGW4f5yItH1dyxCLSWOv+umkebxijfg/gB4OBRNrYGdySJgTduppJR/dp7es3aJHl+yqzU+7ubqBGwQRoDz4z7MFBSgIA1kXe7+iBj48WP28pbsQGUcPPXseZAcwTE+Rn64MDP0Puu5Lbpy1qwLft15N/jkmAo+PoY+7Fntb0nsCdshmK04r7VGmnfg47/WYmx1IDGwJD6hueP2h1X/JMQ8CMIvOrPQna3H1byAJC6scaWCjr5o+xroKfbjnAP4gjKEVQYAM4WTPjzMmCdyitb0MTd0dxv/vtmVn635Y+bG5r7fvX3p3cgGX/fGcU9h8CE/zYLHF383r3fxoWsUdyNq908fuO/b8DaaOzS3z0KRsrxdk/Rp1eASt7z0+jXKgKt7nrbuj/dtQNmfWPOQALAl8/1yDqmoMKAJMAFitGkGGDjdwuMtyP3Nn788frXdPtfBIpX3/FJH3V9nKZxGGNs0kYtC0dthqYph3EJAkUdm8JwnHIRj0ZdGkYtCoct38Uwz6JGXcc4p9ZDqSkyRgiY8xGG//GW4OkuD/QdlCCBQAK1acJFLJ8hLNz3fRz3PdSmUIokGYTECQvBGN9hLARBMRc8ZiyUhBHSsRHK8mnaHuU9uMZdybd3wv8eszt+vAEETqPRBOASh3YoBHcZyiIdD4NtzPEQFHEpzIMJBgNiPRzM/5j6iNsY1rsfxgwH/HO0aVzn90cejFlL4mDkEq9X7P3DTRnNsvWpfQi3kyqZXC4YuceOxTEuT5jsaXS5E8l2P5MWTURs+sIw5XSIARi13GA0m5U16/LzJOgoZUKeUA3d5IVq4PmswiVzcLET6iakv1DyVVDPC8HzbINUVhHcm612Xuehua1U+Zwle2xTaItsl0RVeJLmrruZT9aXGJlsFSTGCv/MIMxUsLQs5WLloiyCELPmUoItLvFmq5ty6B1ouOqclZqb5VA6BkEiamqWxLA7rCtNmc7V01Bdt5vUPhk7ejjsKlwrhmRtuGpgZjzBeNlywsiqNnH9aCrqVTRheFrPC8UqLTUfbK+MK02fCsbci4woP8NVJAqEoYrTixZQQaFq2NrjjZWmbeeIZx3Wyv4is/EqrQ7tpkjXESNuT+Gk2ie2qDVg8za3eEfTL2ZgVe18drW8/JAs9+cNLEfEtWQuKZFfQmZZItTupA86s3RP5KE5XYRjeVA01dA1mNovPAlO2+N5YYitTCFw0w9S4IUKGcPL3cUoC7g1RJ91KC3Mgi23mZXTeW4cpXh79muNIzsqCQOsUtTdlciPTkQk66N8wdRNe3CPx0O0HxC0jXpfX16FqF4vFZvXqnmaao4eJ7DroNHFOkw7s6hQ90hWSh8nKz9LDzpXsBa12Fi7GdrknXOOLbRba2ciW7IREbRloxu2RKLkCnNPznHbENKCP+GBVqQW6hOYwPUojqzS4lRZF5soS1xKQYYwW4Ibhi4dSg1e5/tkOlzmurLZ7RZVliZM5rFTx9gXuFPIjqlw0yI8Z/heNMpYsMpMFI3zxGNc/UgtapJZi2tid5TIU2sQ5xLZ7738WBTrMxUTUjBfGERmXtzY7PGBofcL3XfMkloUE362bi+Ds4en86k/8zyWrrAJKzrJGePRnFhcpxO/6/cRLm5bW4fpXpuvm2h14iRRL9NBCiVZqPXtQTkah9lw6Y8X0255Qxet8LRCZmQPt7t0mIjKziwPO9idwUNVHV17jh/b0FwosC7lV3HuBp0pCbPNUlAOPOPkAtgiuzFncMJAhmt6frzMj46W7vRTv7bDQaSW+aEaDnqIMKcdjjK5bS+i0+VC8+02WwqRlBOUmcNXlx1cPc8yFtnUPoEXx4l9WXer5bQWjli10bSuawd5UhU7Imm2xAbPULOZVoxr9z26hJEDXxQ479nDLqJzY7dcXefiIhdFOx6EjPVCXsX4C6KdYNLXz/J+6eRz0byGq0oRzYAClKnZLK4z1UH8CVOz5VmmRInfnBQBwybIQEf6yeDTg1jOfITTLi2ppa68maqyerycxLLUiE19pueuFCiel69XU4kslXWxnfMu0iJJCSdCZB/2OQV3crCZbh3lsLITt+i58FqsJ+tER08cbe2qvbZIBSFDzhR7rOaoNrdUuzLplpwRF4XbssutqHmcwLlokTYmQmU8662ISrEobqfpBLHOsY0IV5xuGSnAUJTkQ29l99K+rQX7SLE04mor2LelY+2XTl9akbMPpw0s5weyy3ZsXSbDKrtsty3R0l25ViW8rrjAT0pWFrMW42eMzfe4h9DxlLl2RIgnoDL4BVlTGRPI1UWQJUSZb0/KuRV59OS2URGf5ARUVjeZ5c18tcWyNbq+MPR2KW7CrC1F36uIGnHCfJjI7CxIzkv9AJp0f0hZONzEs2VZ6Nxm7h+XAl0sWNTRYXXGEetrkMtMRJR6pO7zYLe11R5n92Gpa8ICpsOyVHBsttnUgqlKy91M6W19u107acGrAdUXZ/7cLYzVbB1T7IHXtnaf6ujgprtYcddVIa4xwxiu9u5KXzyDoPfKSoDt0G5aOccr2jqfEaral1d4NyMGcXvGLsxuLs9asL1IZRPzDrNltPL9jiDoylny0+mEOPjrYFrLHabs8LM5txUqzSymcoMs3tZlzy3XK3pQd2drfyzb0zVRTeLYMLDMTNNkNWF6WN9bYK/Essn55BrHk6Ss1jOaVOFDeUD7Mk8Llb6AAcehQJXTpAzmh8LQmjDZX30R9xGsEnfGVF9Z8sYpZiUeyXuNcC8bqyY85TBQ3p7pMXmhRRYWZQOyEAgKuKtBiFYx0dBupZLdthKpHBtqlRF4G8wMFtctizAydze1zX1uk42+H3Da3KfxGqDntgOwp019jVJn6UYkyxCOI2TtiBerSzexP3QMTLrD7nIhV4VIb7ZX4XDi3InPEvEZjiJdUCjnsCn1EmcCc6FK2+AKC8FyL83oJDST7iQoPlZpWNggPDmBCxw3Vr0Y2z1z0OQNwxyXFKce5NqYSbZDBn612LEGOqvo40FzVvUx1tULSk+kireO0/i0yiuSXPeopdd8ESQbJ9Ykm5gurkWlmAruHI4bUQvVo5mqxx6M2e4lKkqd87mII+McTiN9I8NJlC/X20mdwpdC9Oe9Ha3a46Aa5k4hdddlKsIhi0GKeoI/OPpa3F8wrgkb+TTvr9EKrtwFFVcttUNENImlidjp5cqwC7jfyNqclucAHleM3evwkq7Ki35wpKtr8iwLD1nXaGfDjWq34oxjVHG1Jwyy2mbrPbfChySnD4DCKVM1UK/7zcVItPyAnNXG3KM9pkp1kzoRGSmsMD80i0Psx84s2OgLW9NII9wq08lqze03DC/DFja5bHUnQymCErf87og2MUeENEptsV22qI7xtsL43T60KQqZxJV0tcPlOg47k3cDI51Z5DVc8t01SObZej2ra1mvLAJpLm291q+LQUy0XYPVV5Za6KRUXE0RNtBpusnlFSc4XC0x50AwlQPcrQMPD8WCiRZRiO/yGrRV1D9yAXXmal4jkGA6THg0kLl6u19mnNDkOWEmhuYmQm5h9eAJmuhSKb7VVXUwdnv4YoVNeZ5tPHbWzEyD90/GcGaFxVqIraWKOtzMVIgzcQ6x9ZYbjgufHE7nWemtAk1fm7sDqh68Ex5PB0nfKpezJclxmFqqt5c95zitV2VYJ+vLUqsXOwAiTlScEHoPl2WTtyuuM5NeUvlYEidIuM53cMMxtFCX6HWTTYu8PSA5tbbNeTDkU1acHTDWX1AHNJywGnkOAYOth9KVnWOxtwS04d3wSOars5DlFzM3NPPsKC2gRRjoN0pqJtoGwzaHicK5qk2ilS4mhMbaErZ01pyvaJWCR4mHToo4nRzTVNJQuSax5BqgA30RJoOLboYtlajnbocdA2mw25IzTpZKKyGxEs8rfbpyDmygteQ+Ck4bWakLJQzmGsfHx1RCTI6eyfy2kSwejth1lbU1MsBM2bh7o17KbuzWHmCOR0k0w8zCK03QAfNY602LM/uW2DnDoc7nlMVXytxaeySxC4tAnW9COC/OcbQ5XTKNlNOFdA2ZZjW/DAsXcN+q3h3LUIeZWYSDxrWzDXkbqjN3z6wSY2G5ZZ0WQ78kpoy8JfWg2NAcjaNilgDmX5sMvywMNllU4dEJ480sSlzu5Dhwv4a5MsGGOVvKtNnX5GpbWCh7abjztVPOaK62yAlH87WwkGqwE7i2zd6Q10LZYHlZIDSvXyJB2MXmofN0w+xZadhLrrNNk8tmEc1sfcelW1Wwe1hckGgDA9RXEGrbb8xYCoOGZAdL2a5Bnp44p9JigQ4zxbHIbWgtbSr2DGvBl9nMYtmGgxXGTXGPLIEYVttXG6FPsunyco7xeFv2QZOKvVu28BJp+ChfHdQIYxYzN9HV6xSNU0J0kyJOLrYpR5ozYIylLVt4ayutF5xmOJ9ZwZkoFVLwrQW6FGykXMirnNa5hmrU1E5gr6smeU8vbKvzwR0D29MZmkrL1gFZhs4Q2mjh9trllEta885E3cbHJ9ciVky9QMNz1ewKTU+reSllgPuVHssN3MY6d2rbwClFzpsF056HA403ztoQz3CCXfADL9pTlNhPhDMZ1nDNTzf0pGIP+HrBzdjIz2wlM4WJ1xT6woepk0UtlyS6Ky74hqPYa4EKtC4WuNWEXbegdgONAoXY6eaMY/wSJ7GOUquKdjiQaMx0cjlOA9A83bDCCGIaFRfZv7b5LkImHawtTmrRq5ctspjHqurO9rje7WHWmfKkKTW9H6htXsPkbo5RkXPAzrwV60cv6PrVdjVdd8K8BzSBGUiwf9WR0gadl4EHcS5djqEGu8yMatcbMjnzoolI1FZx8cP5LF45QGCVdUjQ7ORIIN3iOveYOU9SNIJwTD0J/AlO0+saz+hpi8sRTYF6i9e10h0zVd+UrC5MBcQb9kwLz6QAPZm83ZR4t1JjQrBIibm6S6JMz4AUmhMmLEJDWq2mfWSxSqfMCNmfOS6DaRl5LvLcnSAWZYKocbu+OgeDjtTUhp6iiV4VHRs7HbzMdsVpYK4UmohMrwrszk9PmIrvThPh4lz3YmhnwlkKNwyBHetTLmL2clq0cNzvBJ6fSgd3s8DXp2s6sdr9fkkF58tVXuyWm7bnArM8Yg6F9KY0EYxwbqo2Ve38dkUft3zaHztuZVLasJ9KnVHLYPsSWjyzXx6DY88wbUFfkz0Qma5jBZ2tWCqHZ/PuFKey5oae0c0KpbMzpMfbqAua3ZEIVXq5V20iO9XuoKX4+YR4MU6tdLMImLQmCbXRSZNZzZXE2TDucjf3pvUVxQy9LwnZzgyM32ZceF5KMDxIvX21ere5qFozYameqb2wy3o3Qyc9TCNEhM6bbidwMweWGrRZoAHao26WFQaxQUrwiDEUZFi0hVhfA9fwYNyrGrwXEYYN8pbkap9ZEVMPlXBW1M6TtaRftOWWkEOcXhEsqvmaiBUNDnOI7An6NOANrCKTnjawpkVA8W4tu20n4rKr5G6qzZjllZ82tI82Pp3znuwL1PpCkJRBatHCqRERV4Kt0yWgnsiLgMlVg/JTKkiQipMrpgOR8RSECQRjwbWbncOmU/aIYrGbbtOuJgZ406EibG6RyXVV4WpjTRdZoGctYrZVRDCTNgHbZVsldCcKc88tuhzHLmU2d5ayxMLbklH7reFR54AlF00WsLxj6kKuEEYopVQ6yznyRHe+EcCNb9udqjiKN1nCTcxTM/wguzzubY9ie41xb8dTUmnRHDEJCYGHg7XBsY6BBuvrhOe4TUsXEr6zlkVPDGvx6G/C2iOOHiEfFshy22/T6WwnywE5wUSH6PAWl/brtX/Sr5lJESdpQmXrsG36ppimp3RqrGS5I8X8sJR11cTm7nF5KmQN0Ntu1c33vOZPwu2u6bJTU213LjLgPA92DJFp+8f5am9tTtHmiO7iSqtYw9BW2tFTxEtDIzu/BJsr5EIudpTsy8KhyS74dmrIM5MmuZxl2V9+eXp+uh1GP70iMEPjz0/jocTjaOF/8jI6uEbF20MyRjHY89P/u3eh9/eS74eSt6MGz3Jfb6u//veV/u35qXIioOD9dXadtMHjdeh/ehv8+e++sR6lDfez9/Fs9dK8n+E0VnB7wR5lbls31fBW50l7e70OwtLW4//Nqd8ehx5PN6PTYjxB+VAA/PbzynOsunlr8rfHYUuUjeeFnhtZjfe4DB5nE89P7gDCGzn1G0YSb15VjHY/zsrG18bjYdnTH/8Hn8kz3JMoAAA= -->
