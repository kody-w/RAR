---
name: "rar-cowork-cookbook-bulk-update-reserve-budgets"
description: "Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reserve_budgets", "rar_sha256": "9c16124a42edcf23e728fbb5c1b3833089a2836ec9e779aaff2958b2ed5765fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_reserve_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-reserve-budgets:4443583b39e026c8e6c762409fa9937f018b8ae73d5db70db11c361344b1f7f9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_reserve_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_reserve_budgets_agent.py` is
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

Reserve budgets Bulk Field Update — Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reserve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 9c16124a42edcf23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reserve_budgets_agent.py` first:

```bash
python3 bulk_update_reserve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reserve_budgets_agent.py   # or on stdin
python3 bulk_update_reserve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reserve budgets Bulk Field Update — Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reserve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reserve_budgets',
    "version": '2.0.0',
    "display_name": 'Reserve budgets Bulk Field Update',
    "description": 'Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-reserve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reserve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b06ea583b0e06b5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/reserve-budgets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-reserve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateReserveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReserveBudgets'
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
    print(BulkUpdateReserveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjyLLlX2Hyfajup6xk3/LaNRstCAESCARo6WrLYgeJfRX06/8+gaTMqrq9zL1mY6OyyhQQ4e5x3P24R5C/PVlNHWbl0+vTzrNSiLfiOAq9ErJSF5pnXVZewK/sYoP/kJOldRnZTZ2V1dPzk+tVThnldZSlYPo0z+PIqyALspv4AvmRF7tQk7tW7UGWU2ZVBZVe5ZWtBwa4gVeP105WuhXkl1kCFEJRmjc1FEdV/Qx1UR1Cbtl/LpsUykuvjbwOsj0/Kz1gR5JE9QswwbtaSR571dPrL78+P0Xg+9Prb09ObFXg1tMMGGLcLNDummd3xWBibKUBGJH3YPEpuM69EohOwC3X86HH1U+VF/vP0H//96WzyqD6+fVLCj0+X57GfxqwrQ49qM6sqvZcyLFyy47iqO5foGncWf24xrop0xGWCmCXBi/3md8kZTn0z/HZT3clL8DAn748ZcAEa0T2y9PPUFYCfQAH8P1llJL/9PNLnHVe+dPP3+RUjX32nHoUBqx+eXtcP8SCgd+GRv5N6z+B1LsPbe/L03eLGz93u8d1gplPL+csSn+6C87LrPVSK3W8n37+K7FO6DmX0ZH/ltxf7oJDz3LBmh6G//x8A/lXaPJY0IfMv1abA7f+JysBw9/VPUMPoP5K9g3/fxEdRymI+HfE/1Tcn02Y/BP65S/X9ncTniH/y9PCi6MWRIcde6/Qb2+7LTf/5ZP77eanX38Hov+vYnZZUzo3CW+JlUa+V9Vvb798qm63P/36y6cmB7HmWclbU8Z/JvPPcL3p+QHBx6iffpwL9BvpJc26FPqIdOi3LP9f5e8vkGnFkfvtfvUKfZ8v42cCjYt4V3qH4LucqYCt3+H489PvgBtSsJrGuT0GWf5f/wVtopGVMr+Gdk4GeAc4uI4SbzReD6MK0h9J/XUnCev1S+J+hcDdMd0BRVhNXEN8aUUxIKds9Pi4gsyHvv5v58aan50Ha8IjHb7difDtwYBvDwb8+gLpIdCYlVEQpVYMadPtFrICL61HXbeoqJrkczuqA6ZEd7rR5sJINVUTe/+Avv6N/LebqJe8H03/kgJfWMBBLlR7SZ6VVhnFPWTdKLuvvc+ATAF/lFkc25ZzgcYfTf4y4rEPvfSBkgN42rt6TgNoPc4cYLMfAQJ+Hsk9iwG51yN21SWKY8iNAMODYtHfqgnA93UU9vXrV9uqwi/pnXxx6F5FKhgM+DAY+vwZkL4fR0FYf0k9J8ygT7/9/gn6H+jvZt2Ejzq2oADcoAIBHEPiTpEhkI1NAoZV0BgKgGpu3vrt97sPRutSUPZADkX+WMbq0S/fuX5cwd0x714Bax5N9MqHph9xg7oQ4AJFNUAL5HX1/CUdRWRgaNlFlfcO4n3yHfp3N9/1jD6pHhgCP92K5Dj2FnWjM8fi+QIJPvSBFFgu8Gs9ejTMqhoEau6lrpc6PZhp1d9cmGY1VIFcqfz+GWoqsNRR8lcbiB7BSQAhWfVXaDPfgtqWxeDHCNBNPZidpdHo+Eec3m8DIeUnEGOzdxEvkOwBNKHcKq08LK3Ku43zrXtEgJr2Ph8It6AUlPexfnujj25ZfIs87V9ahrGkQ8tbb3Gv7NCXBkNQAvr/336M5k15XuP4qc4tIE7WteM9lsY+aVzavbUC3QAE5t0T41uH8E4m7zT7JY0jgH/Z/+M+0r+Fz33MnbqaEsSGNtVu8sdELm9ygSmQMHq1LG8AfEnf+fwZoAFcUI3UBHL1MmZ+9qFwfPpuaQgScrz+Vtsf6IxxDyIXyhs7jhzI9zz3FuR1WI4p9AAfRIQ3phOIeSf8YVUQkA68DeRDwIgIoA44/wadDFIB9EN39D+GR6NbgBVu4wBrQa54L9B+DF3ghwo4ALQ94xiAwqebKCjxAMbAxA+Eq9DK78aMvevDQGv0RZaMwfCdBx4PQRiOhQPo+8gxINUCoQOw7IATQApd7579sPPhK2BsMsb7bdKP7n6sFfq+8PxjzDNg4zeGB+32WLO/AweQc5lUN74B1fRSgUxOvEcAgUi4leeXe4W9l/APW17/0LD/9J/19LeaafzouVcorOu8eoXhe117L2svIAtgECNR7lW3Evf5nmyfH1n2+ZFlP4i8I/QK/Wdm/SDiEc+vEPqCvCDjo3XkeGPAPj4Ahfnn2fEzMT4dCeSbex8xMJIXIFS7/6gh70NAIQlKLxgH32tKNZaiDlS/G5XdasJHCDwSBDBlGowFsMq+S9xxTaND7/76oFzwKB3J3B2btcAbtzDxaH7lPb2mTRw/P6VW4v391mUkVBCfAIdxrwNyBbQ9deTdrj5aoPHix/3ZLYtA+rvZ65hMoHiBdvUZ+ug8n6H3vcBtY5U2YDP0y9j1jirBUPDrY+zH5s/2nsC+q+7z0eb7Bmdsth5N8B+NGHMIWOx4Y3nOPpJy1PgHIeBLEHjlH4Uoty9W/GCGqrbGkgcq7SOfK2CnC3qjZwh4DeQZSB3AiA2Y8Ec1QE/pFQ0osu643G/4fVtWdl/L7zcY6vsu8bend4YYv98r/j1iwIR/pyEb0XwvpG+jTGuceWubbuDeGsw3sLBoLJjfPQrG6v92j72nV8As3vPTCGEZga55uO2En+6GgBV8a02BBMARn6uxAYBB6gBJoCzno/UXwG/fKRhvR+5t/Pjl9U/72b9I9leCIHCSwW2c9RCMchiPcmgKIxDWt1gWp30EZWzG8mjcJV2bRlwbRR2cQnGCsFGf9lmgf/ReYj30w+iIO7D8A9z/pL1+uk8FFQEjKTCXdVAKxQiLwDzX8THcozHGt23SQW2cwXGEYS2MwSnPYT2aZi3L9zGWZGwwmqQp0ndGeY8u727P23tH/e6Je7q/3TsEoBGzLIdxaJRwWdqiHA9HbNzxUAx1adxDSBb3GcYjwPyPqQ9vjM66L3kM0fyxMHf01wMJEHYUAUauiEqY3j9zmDUt+kjbcmizNOUHxZlhEDbvsYRah7YyULxK9eopQ6KZWPdREl5ysd5gyloqIlkg8Q039QGkR5GNhzV12fYkKWKM0SDzWW1vV/2l7HySJNeKGs2RfR2bh+SsLftUQs0TY+lKWZl6aYuGv1QuVbyOUJKFOc9dXvZxHB5V55o7zKGsr8lJ5/cxpyxFo9jszeJqCwjfL4fMV6Lyskts3dD2KFZrZtnkyd6NKNGQ0bzWrH6fx2q0OTVyWa01ajucKtY7DAztH1IiX8eTie+jriRTjaVHrbkkxL3plsYkL8Rhtjb5utZ2wpr3mk3aLO2Zx1PVcp+TvGVQdmSQHnXl0KHQF0bESZFeRKQpxZTfYjZqNF5xWh+OIR566mF5Ypp4xZNpmVvCebfiz7uiltdnST/wMnZyy9ha6ycSLS35gLS7VDk7+SXt44qXL/HKW9KrxKA5o7ggcXVB2UCVJa1iZfqyO0UJZpFYxTLEOVunzmVPzRb78Ihh1yFR+rjzgRhbJiVqEHkzgEttWzkUKi2PeYvSwq5aU0tMVwZRuzg+00tXzp7VTZLJ1tXtmXV9FfVDuzBF9uzYTgpvqfOuN85TLy3chqO1shAVYblIra7JyaImSJ22aYahZ+LZ6drDdt2mLTvXV3aj1klNsKt24ZFC1AwsLW+u6aw6XZdacRDPvTs7CvQEOyYI1lfOesvDxSbmuySctRNeoS92QmxWgzHHlOYId6leE1m4nQ5raRlu2SOxnPOreCj4vZHT8xz36W1drOuTabpn0hbt7rrRt/Prqt0gO26d71zjIMoHM5d9nQT/aVTWy/OwObQYqvkBAbsN+OnP1ElXhQcl5owEJrbr1fTq+2uXlZjjjNMQvTUbFNPrFHi5A4S6jjLaQtSoMQvTuhzmnN/yYWUowvEarrmCX9F7hSUSteT3EyM9zs+w3l8IcuGnWhOk7YAv9fkxitpqtSuyPbFkO2NamZwhny4nzRM3uEBnnLCU0SDKj3NqboT2Ml47Q0cki0hrt6RxCt1tv3SYBGHUlBYO4iRad77QTFbVCS7Xxlnf9pwtV6xuH+sNXYg8i7fX+oRl6TxhkZaBifPRdtzl0oNDlnEPm3KiS8fWNvl17HWsQvdiUeWpIouY4KBXu7MShFO5slsP+OKKoFrjrvbMVjfTXVQs1lc1EcWly5Gn0gTe8M7AN6uUtRx6vyRSuS0RhmEiU7PPocvup21iSgcXqWTKcUGfhZ7EKeAahKgU3fQyR78WM6NFDYsNGKO9yOke1pSCVNW1wQR2m3n+dKm5VRXHx3QdGPM1XMw82dwH5oIhuJqL+ZzzYWPhCx0iCdWuYav2wFLDeUjky0zzMNWiLguTFi0clBWj1CVfCBTVKoqDkm4oAg2Cy5HXLCo6SCVXGcN5WeHRXpkTG+wMrxjbTMqd7ifkXHGVy7YWHZgwJFoMjRWyEvmqJzpuRSwkuND5bb6SqfAge90UPjMkDeMSPD0lW6uhZx0DSgo/D8/rxV7JKkRa1Zd0pWXkFtEmlJcVq2mm7AdnN9246CmYhbjtMAHMXTf7pbeV3G4uOV0Wi4opeltg1qYx8z6iDmSRihWLOBv1FM34vhPmq3iWpVcbm8EG457O1tUhGkVdCpLQ93ZnL+sJRq6rOXdYzDdTZh/vuV13zOJTGGnMsMTMitCE+Z4LeDsnk17YmTgojoTtDgPW5RKVn9mTujxJBHusiIr1GToaNuqgNG1VTJxD3MP+YVEI0nEwFaVtzhggu5PJnHBpUNxZJ4p0hqxlftsO2rTUGy+j3bBTFcrwfAlOT/hAySsqXqWM54s6qcLSLriakTex6OgynUbdkTKa+iwbZHzSnHkWI42Lzi5T+0AJWR5z1L6bryupIRshpuYuL6fmUs/QjMQ2fnQE3CR2SaGdurxbOJLKN1Ncn7NFgMzaeFY70xBbq71BwJeIJI7msT8b7Wy/CLR6AzhsWPfL4soLiRTNQFWbLISOjvb5wRFEBLVsGb2Ie+uaUfstPKsFZz5ntkeLRON6C9uOKvrJBjtGxOZIwNPratL2B0vo3cmat5cefmQuTHxBBAQ5TeHrLs49wdKWNYttcpzD+aA7gyqZiRG7IOT5JDgqJJMeptV5jvqHuDDXjdVbyLafTvQ809X9pFqvVvt8KcXJzuDkXVLLBqLqHUm0qF46mRs4U0BColGWIb/tTEpDdW6/MHFZvcI18Efir9EFbK4MfLa4uNg8UFVmMT9mYA+zQdOkZ9tMHdRTnLvTk6RIdnGhUM5W+HIzcEmnqhxyZYSJYbcT3Dqtd5w2JaOpNRGpwbiiBaGdxX2VCK7ozE2sPjODrK03V8mSLSN0q/a0rG3jcKG4Q3LR5SqUOp+uDzVyiKSVd0bUUCKH4bDRz6s0rRi1CWTNMgk1gxXKiQXB3km78jp1SCevV+x24S36Khq0VTlNSCJsunJYJrFaa5qWb8QuU0qu2DPirJAVfZnXWwVNKbUXwt1x5iPDZBX0gEtxo8ax8yUonH46i4hWqfYzBAs2VFJvPSRe4Dg9wAreJnKac2ctN7buxbRNFleFc4nuXXddas3GzVPyartr113U5zVyanRqj9MGT0v1vBEu9jRDSay0keCyMfYZP6gGvsUt0uyVOvCFsyHmBd+E1jYbrHY9x3L5WgqctG+nBZ+cJdM7FcMlaDnN6sLClJqIUGKza9ctBvgczUL3krb50JjqiXUm5m7YN7EBzzh+2oUKa+HJWZVICbhupRe7QEUpje2C4qCH2mzRpht0fikVyeczbtojESDAaGXCXMKqCEXhktUksFXhUx20jOvdYTgvqkVYO7vadTpJSpfcttlJE0OPF73WM3s4lLiFKKjpPI/MuR46c69YRfl5m7FKeD3Rp8EgL12dZEdjh/Nbga2Grp2WjHIRVwdbyls9XQrG7OKeNey4F+eudrqw+/LA24pQrt0St6gVmw3qAQuT1JpTaOQq8Nz0vPpIVQqhetxkjVrNqgp3djzU1erAZEhWKCF1Ll1ZQZFcPm9nEhyrF/Zs4NGwHurhMqVpIWIa0Bse692CI7hJQnAL0AnQenNBsqV0RSzpGFFHUd2Rh0VgN5wSSBVDU0PhVWS2xSKAqpRgw6bf68iOd1vZ72DZpHut8Zxdnh0rvmolDJ0Z8dwXj7XKgRqSpfxu6tjiPAkII4BJI1dE1uqyMAINk7SWyyVDagWerlcc3S+xWCWX1T5UNsxWjRzc9vogc+RIXzFleznsFK3rBFBUROmCu4blRLI7EayJKchnnHLLRKrZdCd6pn4C+wthbUsEombNLnDCky7YAjoRQSq7LqMT65XHHSesl6LiPtgU27YXpIl9Eim63p2MnJ/x3qqrqz4zbPis5CKeUSRLhbRtCkUrdBEdIrCW7VpQ6Zm+oma5jOyxROhKx3XFg3M5LYR4QBAnPSNxX7ZTLnfDQMEWQWc2erjYaMfNgR6WUZj0G+vUm95eT5ujTUl8MWys6ZydRlTOTAh+yIbWT/pFPgRbgTts5H51VA5pH2n7UDaVo0joC/OaEaer2mGDvikQm/KC0KKwaw23/pZzHEkv6wVFhRdO1bf+0tfEfVfYFlk0iEYaHTlv64zeUzFZ07UfMwfE5gm4Kdgd7uF7ptHEMjZoLOzAFYyWNdWynWN2YDSKJrPIxjrifF3uBPVQ463JKQi1jHmaWCwq8PgqdWtcuGxKd6ivmLFAsdKUaHmbWIGmXS9iRl49jNvN4QnerQltoXeDxxdMWg6Tbg4XfqMsz1PDZWZwJSKrOcOHeUFgYMtCZfQh6jkR17ChopnTrm3ZYq1fkVMCJwfNU2VH2+qVwk5W1rW+Tqq8326RA8ySe5+Zeam0kbdUiU+klkYrNqbxYVtTEUyLbClZcwVBuSlRI5c0OLmr2WzVp7sr63TM3ke46tId5zXORJV42U0RhHKYcBGJ6IzcNYQc1IoKLxMnVUgZQSrcwengWM3Kg3dq3IVGNFNXt3pTV+Sd208mTD3E/MEtjjy1kteCAmew7m0uyoSvFgNR0PncFeHZRkZjhBsie0k5R39KYjEOqziZkCt6LWAh1w7IYoHTGw80bFq3wfagTpPF+rqhFU1pzirTapNz0aI+vN9OiGO2G7JNm3FxxhVV4K3xbp+qbEVOTtRpDji3PdjcfqnDmGk5iYW17ck5hMgJdUAH1K5JjR5CxWkZxs7324q7TqcHOjxVk0Xoh8JhjiyEPXkV0uOuNReIFFpnj7JgK81X0iKIOrhEDruwiQyZbA9lhGk9Mp0opy05EAY/5+dYoK9gRzmL247q4zQCMeB0kaN15X6ThsvVRilBezbxWz27IPB8s1L9YkpzSRHXbQ8nTDSfC0xeTV1CcNJTG2T7xXbX85mzpuneNQwW482Nvj50h3TuohKzqRuU1TF/5cTLRsCYw0nxojQRhe0yCycG7Te7KZvrYhC1vkaHB2xTLSoZrfmJjtEoSQxgrY5KNtpFmMg1cxYR5bwwEYJnUjlTxH4yjzxypdTX84AmW/esctiy65P0oNfOuQlRZNXa9GXQD55dY+wyLFYerh0WiAt2GWtvoTESM7UWgexjWCATndu7/Gw5nYRnxkpPE2R3IbfahBVjTta3lgt29+S8uZoNpzIC7ZEs15GTDY/Dsd8zqXuCV7AetIq9bK5nLsTribLaEwyx8Gp4Ri9LOsJaWJ7Xk8yQGio7VLCfpZFdOp6DKgMN+0ELD6i2OBvscHCu6TaPr+L8WgV0F2rclCSsgi7pjT+hI0vW3GNwXJvosMS7pb+cAI+i8pThL8LWRBlns110WbQv9SRttsel55J1btAUg0bNYZVQyKKgZ5mZn8+XqY4otB9M+axXuGx3wjQxpdNlplGW5dWN2lO2x5bKIT7X5aRcHhdquO4m0WTAMU/JDHa1INiioOq5B+su2ZHTmUWoaUQhM+tIEJVm+ok8wU67DTUdNHy/C44Tk3asizYc3B4tlLQxZudys2mba6Ms2oBGWXoad/sFlndbTLIW9ErMvZpw1HCICKfutzldt8JcRORukNhBzR3sWO1rySd3Qbxgd9iRok+0PVFnw6Q5TB1ipijLEGErIdHyvFGn5yOlOhNm5rhG42qkiPMtmRGN73rkWas2ZewSzhCjSpptcXt9PnO8pE6nT89PtzevT68oQiLY89N4nv84lf83T3aDIcrfHkJwGmGen/7fHUHejwPf39Ldjug9y329aX/9t+z79fmpdCJgy/0YuIqb4HHg+C9Hq5//5qR3nNjf3xSPrxCv9fv7i9oKbmfQUeo2VV32b1UWN7cTaIBrU41/H1K9PV4BPN2WkuT17dmH6eMx6+18+63O3u5vtJ/GP+AYX4x5bnQfMV4Gj7P65ye3Bx6KnOoNp8g3r8zHRT7eFI2nsOOroqff/w9HKESn7CYAAA== -->
