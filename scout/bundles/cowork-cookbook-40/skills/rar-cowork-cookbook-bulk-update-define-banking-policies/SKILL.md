---
name: "rar-cowork-cookbook-bulk-update-define-banking-policies"
description: "Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_banking_policies", "rar_sha256": "3f1bc8653db6a5adf72dd86b7478d3d6f5d5fd8e916cd900bcc51d27393403e3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_banking_policies`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_banking_policies_agent.py` and in the RCI capsule.

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

Define banking policies Bulk Field Update — Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 3f1bc8653db6a5ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_banking_policies_agent.py` first:

```bash
python3 bulk_update_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_banking_policies_agent.py   # or on stdin
python3 bulk_update_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Bulk Field Update — Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_banking_policies',
    "version": '2.0.1',
    "display_name": 'Define banking policies Bulk Field Update',
    "description": 'Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6848bd3db14b5448',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineBankingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBankingPolicies'
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
    print(BulkUpdateDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOj1rLmv8LU+6HtR3UJIbH1jRsx7BIgkARCArejzb4vYhFCHv/vc5BU1fbz9ZvriYkY9VICzsmT+WXml3kO9euL03dx1bx8edEDp4REJ8+TOGggp/QhthqqJgM/qswF/yCvKrsmcfuuatqX1xc/aL0mqbukKsF0uq7zJGghB3L7PIPCJMh9qK99pwsgx2uqtoX8IEzKAHKdMkvKCKqrPPGmKU3gVY3fQmFTFWBhKCnrvoPypO1eoSHpYshvxs9NX0J1E1ySYIDcIKyaAOhTFEn3BlQJrk5R50H78uWnn19fEvD95cuvL17utODWCwMUOtw14e4aMA8Fts/1wfzcKSMwsB4BFiW4roMGrFCAW0Bn6Hn1Qxvk4Sv0n/+ZDU4TtT9++VpCz8/Xl+nPHqjYxQHUVU7bBT7kObXjJnnSjW8QnQ/OOJna9U05odQCKMvo7THzu6Sqhv45PfvhschbFHQ/fH2pgArOBPTXlx+hqgHrATjA97dJSv3Dj295NQTNDz9+l9P2bhp43SQMaP327Xn9FAsGfh+ahPdV/wmkPlzqBl9ffmfc9HnoPdkJZr68pVVS/vAQXDfVJSid0gt++PGvxHpx4GWTP/8tuT89BMeB4wObnor/+HoH+WcIfhr0IfOvl62BW/+OJWD4+3Kv0BOov5J9x/+/iM5BbLUfiP9Lcf9qAvxP6Ke/tO2/m/AKhV9fuCBPLiA63Dz4Av36Td/y7E+f/O83P/38GxD9fxSjV33j3SV8K5wyCYO2+/btp0/t/fann3/61Ncg1gKn+NY3+b+S+a9wva/zBwSfo37441yw/qHMymoooY9Ih36t6v/R/PYGmU6e+N/vt1+g3+fL9IGhyYj3RR8Q/C5nWqDr73D88eU3QBElsKb37o9Blv/Hf0CbZCKpKuwg3asA/QAHd0kRTMobcdJC4O+U24CBgqZNALDPcSD+Jw9PGlch9Mv/9O6k+dl7kuZsYsNvDx789iDAb08C/PZOgL+8QQYQXTVJlJRODu3p7fZr6URB2U3LAtZrg+YCCMUdu+AzoKLP0xdAk9Av/4b0b3dBb/X4y53UkwdH7dn1xE9tnwdvk43HOCifFnmAgoNr4PVgjbzygEJhArj1FdjeVvkF8NuER5sleQ75CSBvUA/Gu2yA2ZdJ2C+//OI6bfy1fBDqAnoUinYGBnyoA33+DCwL8ySKu69l4MUV9OnX3z5B/wv672bdhU9rbAG3Pz0CNJR0TYVAhvUFGAacBdwL6OPukV9/e+ILxJSgsgH/JeFUdqbJIEKzwH8HW1/Rn1EMf68voI5UTTeVKlBloHUIfegLFp0eTTweV20HKlsdlH5QeiOQ6gBzPpAsqw5qQRi24fgK9W1wX/UXt3HuKhYg1Z3uF2jDbkHVqHLw36TmfRCYXJUJgP8jFB73gZDmUwsx7yLeIHWKSah2GqeOG+e5Rug8/AKqxft0INyBymD4Wk4VMpiguifIAx4wCCDjPV36efL5vcICx7bva9/HOFNtM+41rvlats/gd5rgXsiBKiMU9Yk/lYR/PEOqjasetAMTfkDTSdLTC/7TK/cY5P6iP5jqNyTcG4pHGYe+9igyX0L//3qOSV1aFPe8SBs8B/GqsbceME5N0gT3o68CtR8C8x4p870feGeTd1L9WuYJiIlm/Mdj5B3855gHUfUNwGpP7+/ygecBjJPce2BOgdY0dyC+lu/s/QpQuVMV8A3IYhDlU3C9Lzg9fdc0Bqk6XX+v5E90ppwGwQfVvQtQg8Ig8F3Hy4BWzZRcTyeAKA2mRBvixIv/YBUEpINgAPIhoEQC0gUw/B06tQJmAnfc0f8YnkxuAVr4vQe0BV1o8AYdQX5MMdICB4AmZxoDUPh0FwUVAcAYqPiBcBs79UOZqXF9KuhMvqiKKSh+54Hnw+8RfddlUh9IdUAIASyHiWT94Prw7IeeT18BZYspB++T/ujup63Q78vMP76Wdx0/eB2kdj5V6N+BA4GUKto7l07M1AJ2KYJnAIFIuBfjt0c9fRTsD12+/Klb/+HvNfT3Cnn4o+e+QHHX1e2X2exR1d6L2hvIghmIkaQO2nuB+/xIus+PbPv8zLbP79n2B9EPpL5Af0+9P4h4xvUXaP6GvCHTIyXxgilwnx+ABvuZsT4vp6dfy33w3c3PWJiINR9BRf2oMu9DQKmJmiCaBj+qTjsVqwHUxzvNAkd8LT9C4ZkogMXLaCqRbfW7BL6XW+DYh98+qgF4VHZgbX9q0aJg2r/kk/pt8PKl7PP89aV0iuDf2rdMnA/CFcAx7XdA6oCep5segauP/me6+ONe7Z5UgA386suUW6/Q1Ku+Qh9t5yv0vhG4b67KHuyEfppa3mlJMBT8+Bj7sRF0gxew9+rGelL9sbuZOq1nB/xnJaaUAhp7wVTHq48cnVb8kxDwJYqC5s9CtPsXJ38SRds5U1VOuvf0boGePuhxXiHgPJB2IJMAQfZgwp+XAes0wbkH5c+fzP2O33ezqoctv91h6B5bxF9f3gnj6YNnOwiGg8z83E4FcAYCFSwIrh8hBZ793zSKTxGA5UCXAmQswrnrkTi28F3cwRw/JFDfJ3GXWBKkv/DxEPOx0CcDao57PoUgrudhcx8lFtRiiSyCBZD3iM1vj7IGRAZIGCyoOer5CxzFsCU1J1CH8p0l4Tg+QpIEQoQ+KATfpwIN/aetD9smID961gmTp8m/vrj4EoxcLds1/fiwM8p0cJRw97ELN3hg2afZ2i1NCW12rqx1wsoLJaZI9YEvFrIwMtq4XyHd7hDDx53Z6GJkYHxJMNu2I7ENMa6zGkUS8phE5kUppexmk0SuUaQtRwk7GNockTI988beV6xDf8jnjXQwDfyC6OntJGcL3l9kiT6aMAybJ89uStmay7y/WkYg6NSRSIc8arK05YWkQvdHRahSplkbWtwSw3nv1J22X7snB+MPxW21t4/SReBOx2LO14xTHNg1ihOHXlpuGdxqTwLsXYwO9rfXbdlQlD/j6D0xt5BSOpzl5bEda5D8SmYe2ZOcu1aSN8XG55stKQTSaJr9iCgSpXPmQRcVYr9ZeI5gmIcZE7NVf0bW+bJXkKg1lVL2o9ZnuAs7xD2bWmylzW/bPYvsxawXHGGuW8bZKi6tUiG3k4Uc+x7LSlsI4UDoTce+iUqu7DRXojdkM64tgx0PerK2Twhf6nxqwVLBnLw56woWfupRb48wY6ufbDpqKr4hUfFwQ9GeIT1acS9S0Y770trieYIruR7b5zUxD0ZBYeHYz40W5zFti+8Yq5hHBWrsjqrVYzKGkLuDiY+OtO1d1TKZK1whbb4bVvWyNKJSF/t1ts4sTW0YPD+ni1utqWG3xA6rtYrc+gWhNKfyyjal20X+pcsGpZEks7AvNlxsKik9Lvv1IQYRtXTFVVeYgt7fzBQLlqvcEFyRnVv75Xgl3f3RTW5bZn9bjlhyYUNtdW74zfrSro/izIyTcKiwi0rvb4JiWWRKup1/2hD8eaRugKo0SyBteLEzrtvM5HHhZssAJ1Q+nVDtZKJaaPYbvGmKfVlL5TL06rkURlZZFatsCAzmmmL7NpCtzphF40m7ZtRM5GbsUmPYziPmROdnlIOuu1YRYw9TNBwt45WMKaquS1XYrm8XqRvinBNVw2vZiN2xIb8VZDvr8v2M2UjIrNa0/RYb8aXmdRtZH8U2llzp2iR5yaT0inZjUfSrI18ZraFG9HKPrhIBoetincRg/07ZpZ5rq/XNC1j3xJ63XIPNm2tjXlAGjkkkrGaMgIdLfb5d2kHceFkSZl5XXq0tAiM3U8O4oKW2cT0Th5Vc+JYym5Gxd0Z3ya3RsTAUTi4K53yvzG2fs3hRYNVEnJ93Znkkl3yrVW3OBWjM0kKwWWy97co3cRzxrJiSPeJgJg5PMyVb48mGrPH8GM3iGRasExkAuVMMOLXinCKp47FKymFJoY1QKCRytS1tnpfGeTu/SbsyG/J1s02vdu01Qy1hu7NENic9cs/96NxS/7KSQOALmLg9c+Xge4fYV9fHGCXmdErO+Rlf4LZsbPRZSGcSv0RbGWT0adxQSTPSfnPJb6cLyjreKWsPyhHZHNuiKDHG7LhCW5H7xOZNiulUvc6uuSlGvMDxiHw50LYflXy/C/PTQcY2YjqK5CwU7IPTHdU+PEeGjSd+zTT9De9u1dWjGNQ+7g+VQSxXOnFWnO1ZUM/jsYOHmNy6KTxQF5iLdrOe36y2cSL3mKoPhdEogp6SlnDNziLDDCGZOTQ7kCBERZ4Sx+Qcxww22NUipA9Xr7SK8gLoky5KXxz0tL6eFIpSC1YxbbtWYD/O8JMjFrS2p3PbyiQ7SQ8GpqI1fwp9O2UHn9fYnSDJa+RW7VxT64ur0rN8qq43zEHMRf4wOJVgd6QOcwXBLr1dxsjRjtOy3LBZ3SRC0126VHpdXCX2XKWUHQmxvqQihNj4FwRP5/ze0PoLUmB+ieGzsEwv69FamJp2QVMky0XHJN2bfFvU6rCWiQpRVXzW70r2yhKEEaPCuK52DZipxdd8Ne73NBnuTRIOLobFLOtQ4HRrHC9hfh30HeDfzFzbaDqezuaBz1fnK7ISTbpnChhPHL02LK1nWIc7GA0inDau3OuldAYJvA3B7KEWmaKw5jQ3iPSalCJmQfOUs4oNMV+ZUuetI1RpF9Z61pObJXIeNyACMGrcVJia2ye/kS5Bbs1vJuLt9kfBpyuHOHBCa2OGW0pa0RxilemD8aSuQKQvQ2aX7WyRRwL8ZOQbDN0sb7FEbEDrz+9316hYJlp4WVImfr7ui5kx2gmIT0LFrNDaFeOu2o2nkzxXsDCaeWmrB+yGwo/r9ERyS8kjI6svk3V/xEWhEHZHG/NH3rRjGClv2zmTHOohIQ7UXHUOfLXTQkZAzgqXa7zTantl5uFHWdmteJZjDJMoql1BikmWIFczmnuzg7a9tmyaG9ixyp1aL4e1F/eDYLGryHEFlhLkc9ueyhxLVjrH10YjcMbNNbMcreLaOI7ANiQ5D1fxkpQ3I9gXtqk4u2Q9ay3xdFWOPmB81+RtOW9vvrSKTI3qw8KudLuYpWi6y5ScwOjuZiWgRMnI3Lg560O7gtPzXNvDm1tncSyNMMXFP962m5DWsCuDGz5fl52cHhbVeKCT7sLoF4RNCva8yDx4v/Py5cHhBCsrVb5HueOS4dhjpcdM3MrDqDVIdPBiqYKdkiN6aa7M0FSORYeuKO0y83iR5GcOVfKDtxEMsaK3JxVDywYVkbo8mPXynC0DeEaGtUbNqM2yyvBtFBMZ5+KzjmM2vobeLmdfcfdC1s8uqSL5zWi3sc/V823supcTHJ2RSxXtPZk4EcaRWdOsyMbcESdhLCNsWduXLYeJlrjpabFWGXjrqvC+mKuIakcbzqwEfYFJenPTWk+XlqlyFNVDbyInCak0FfMrnc21jleWGUxd8rHKV80VOR+cObUqLZocxI20kBxyfmZS1ReSY8JcrwbwjrLi4jpR1huDnJvemjXOhTRK4sYXRdbnIyScK5fM3vQdXnAShppHhINPAoezqGeBPDi7531j82x5gGsuJ/eCXoCO2RJTdk7mUjTqhZLu9goh7SKySIkZKWMHNDeVk77x0h5D9eV6lPbU4mil2z4R9ze9jmE2tKiq1zTUTuFaxmdop9SxVbTyGQMl+aQYsqtJjbI/chebQnPVkuCmv5SRnPs5V2KgeU2OfWr3NhERKcCMVeSdM/colzlRtSbraesvcdwwJPPgS+5obK+mCmO2a0gl3o8r2p/zugraiIRHajbz2IXRscxYJhSoaeSBU61RE3g71OhYwywucntei+yWcvBbdeyk27xIVXy/KVB9g4oGoot+316W2370rvJiqysmsjoIx1Nu4JKiM6DvK2o6pL1ZKrC0BppoZTBFmt40WSnwannYYTtdEN2aPypX7RxUbafM6KNTK/mBuW6vYoEKt7PtHNcrYk+i1gLQR40ebj1L8/vsZMimY47ZVeoIInevelRxoYSORnMamnU+D+ZleY6GrlduJpuoMsfmNV978dESW7bOF1d31wbLa4nNgVM2V9rhtxfhVLgn3LjegiVaGRtxQ25jue5N/qId3Rx14mbJnbegC0jwIWGJHlQtmZOD1YWba7eab7H9KUjTpB5SpJ5lqXoWezFJkWUgBLZsG+am9dRhUM9Mpq+3Nc6pSSx6psNa631fSnnnaP0cvkRFkuiZGjFFVJlHWPNWNuJdLorEILtByRIlkmuhXW04Yr9Ld718OR1aiTrvyEBdA56D4wwAQ+13e84vLZhYrZozqvGuMeBbtGqaEY12jHKwTCpfGQe0JRauQzTXk5D4pLFwBmcVyL7i09wNjhYLZjDhI4w6YLtimO560SMaNRJy0AWYuei5liDkRQBCq1I0dEv51nhio7z28SValPy5We0bR02F4RjPmHpUQ7b0bx6mstSVm8+t+RHblqJp7QWrsA97fZvQRjobUC9FdioWj6R8vhwvwwx2rkTk0GvOm7ci1elYN95aHRhztfFsO68wrrgiAcmJs3zZLd3+dgWA2Av7uGgs5nhc4UgoZBJ59QkNEfHZCoSkG4YXRNiOTCybtjODg3B5Doy5SjRllYeuz2zRAzbypEjRHR7bRiXPhCui0quQoTar+ZK7SrPd0fOZlKC8sdlF1lLZpdJiZPGDtwtAlHKWkrJhdtvemuDoWCe3N9sbeaBRvFkvtCSiFvSqMW1ZKsHuDAtPF3njWTe6xjJ7XRxOg3o1EhF1N/kNHcpudtwelJHC2RkxypVwE8YbSu5h5dZ25353QY7YSK0tuWVOBsVxK0KGUZJjMnpRtASOOWojJceY7EQSQ3OqzMMmhFsPuEu69W0ER8UhSvobg6AwtySIbrEdtWKXEH4zRwch5ZkuPpZSoTYEesJmneiH6llYxFhEYtfF5uaTROxv2w1K707LwmwpFnaTzULE2LW+HKzS0kN9RKre4mDMmp3dXtJX0cCMxxoly2VlWbkdNHuMcHdGBWwt+WxHCljT0+pFHDyU9WKBwrTDxfPtKwWg37WMy4jo2jt1hpRSR47BqNm2zjcLOjjTmFBUHdjwERmZaCy9kXpub8nnhZ1HGbbUyAVetVvCj+Vzc8TgPbwtTsMx33RXg1x3yLzfL8KTdcb6dUGVgaolTWEPp1vAeU1x8toAHvMkVr0+nbEXsEUmlkZjdV6p3po6zolot4yvPjW6y2IBb1ZhsJmfwuh61dxFKwme6sC15rupWaZtaIm0VwmXo7lyw4unaDEyV9pzh9u1O/PRxouGuVIqVprgC7pE7AtDF6pHC8JtR13dqjmZhJXtaCzYZhKu3SrEXZPhCmzRitHFzydKaLgNWiyGYZHQzsq/nC/sEAZHwiX68nZS+h7eEfn8dCGH0yWMh9ssOFHpYYuryOaCAeLDZz5Bbgdu186boscZeAcm4Sg+FAtN6WBuRiguam/giwz28d1SOSHKjozWwSGwoiKlD6hqBvNZccHU60ZuUN7RYgcmWGUZXvSZWFbHLCoYPbskGAz3ebA76KXZUfhKacYtjyy8oqeO+rhATgOl0/NA8ZQMvo3RgPP+CmE5xJRZ/VihVykjVup5f3abYN7rY9OEPiGDyOhrWBHWFNi73fqYvJW4r1l0sEoHWHbQho3hnW9HOM04y12ZLBEmcAc725vbXLpI6YHSSnUnxeXyoBa9cap3SI22WMDYRM8vE5ixA2pm0+VswcdGtGmoU3Tp2bk8bg0d8+OZShXSJXQR8bggRLNccAeGDFs5URFHl44LKSWV4bCeG1R+rrdoby/mG9l3uXRYOay3Iik7OIhyhOsyH0korNL7GaILc6FyAycc1QTfbBf+2jPgM++mFu45+Xy7jbZ22jbdKatpmv7ny+vLdCT9PFj+O2+Np4O+/2fnjY+jwffXTPdD5cDxv9zX+vK3tPr59aXxEqDT42S1zfvoeQj5X85VP/8b7ycmAePjdez0TuzavR/Ed040/U7RS1KC5qZrxm9tlff3w91XAGI7/XpD++15iP1yN62ou/uzD1OmM9v7S4JvXfXt8dr4Zfr9g+lNT+AnjxHTZfQ8bX598Ufgp8Rrvy1w7FvQ1JOxz1cewEb0DXmbv/z2vwHQlEzwuiUAAA== -->
