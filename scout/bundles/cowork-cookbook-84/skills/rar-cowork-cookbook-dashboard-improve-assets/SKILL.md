---
name: "rar-cowork-cookbook-dashboard-improve-assets"
description: "Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_improve_assets", "rar_sha256": "a6a6bef9a5004f5046db3e1d0d5a86f26303e5a8e6e9d0660d0ee58b1de5eb75", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_improve_assets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_improve_assets_agent.py` and in the RCI capsule.

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

Improve assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-improve-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_improve_assets_agent.py` and embedded as the fenced Python below (sha256 a6a6bef9a5004f50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_improve_assets_agent.py` first:

```bash
python3 dashboard_improve_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_improve_assets_agent.py   # or on stdin
python3 dashboard_improve_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Improve assets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-improve-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_improve_assets',
    "version": '2.0.1',
    "display_name": 'Improve assets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for improve assets - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-improve-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-improve-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cac617b8558a1329',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/improve-assets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-improve-assets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardImproveAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImproveAssets'
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
    print(DashboardImproveAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZPiWLLlX9HE+5BZT5mBdkG2tdkIAWIRktAGorIsS8vVgla0oKWm/vtcARFZ2dXV/dpsPgxpGYHQvb4cdz/uV8RvL3ZTh3n58uVFA3aGCHaSRCEoETvzED5v8zKGv/LYgf8RN8/qMnKaOi+rl08vHqjcMirqKM/gdqXMvcYFFWIjFUj8z+NiO8qAh0RZDUrbraMbQNb6XkQ8uwqd3C49xM9LJEqLMoe37KoCdYV8RvICZBXcBW3oEafM2wqUn5AsRxYkQyO2C5VUSAaAB2U7PVKHALlFoAXlKzQKdHZaJKB6+fLzL59eoOzk5ctvL24CpUMjF2+aNw+l3F0n3JbYWQDvFz0EI4PXBSihbSn8yAM+8rz6ODr2Cfnv/45buwyqn758zZDn6+vL+E9tsrs5dW5XNbTOtQvbiZKo7l8RLmntvkJKUDdldkcJYpkFr4+d3yXlBfL38d7Hh5LXANQfv75ATEp7RPrry08IBO3rS9mM719HKcXHn16THALw8afvcqrGuQC3HoVBq1+/Pa+fYuHC70sj/67171DqI6YO+PryB+fG18Pu0U+48+X1kkfZx4fgO5CZnbng409/JdYNgRsnUVX/j+T+/BAcAtuDPj0N/+nTHeRfEPTp0LvMv1ZbwLD+J57A5W/qPiFPoP5K9h3/fxCdwHyv3hH/p+L+2Qb078jPf+nbv9rwCfG/vixAAiurtJ0EfEF++6YpS/7nD973Dz/88jsU/W/FaHlTuncJ31I7i3xQ1d++/fyhun/84ZefPzQFzDVgp9+aMvlnMv8Zrnc9PyD4XPXxx71Qv5HFWd5myHumI7/lxf8qf39FTDuJvO+fV1+QP9bL+EKR0Yk3pQ8I/lAzFbT1Dzj+9PI7ZIYMetO499uwyv/rv5B95JZ5lfs1orl5UyMwwHWUgtF4PYwgIVX32i4BxLWKILDPdTD/xwiPFuc+8uv/du+sCfnvwZqTd7b79mS6bw+m+/UV0aG8vIyCKLMTROUU5WtmByCrR11FCSDv3e4cV4PPkH8+j29GXvz1r0R+u+9+Lfpf7/wdPdhI5TcjE1VNAl5Hb44hyJ62u5DyQQfcBgpOchda4UeQPD9BL6s8gaRcj55XcZQkiBeV0M287O+yITpfRmG//vqrA635mj2ok0QePaGawAXv5iCfP0N3/CQKwvprBtwwRz789vsH5P8g/2rXXfioQ4HePbGHFm41WUJgLTUpXDb2CUi1tnfH/rffn6BCMRlsYjBSkR+Bx2aYizHw3hDW1txngmYQB0BkwdiE8rKGfIxE9Suy8ZF3e6HS8dbI2GFe1YgHYHvyQOaOnceG7rwjmeU1UsGEq/z+E9JU4K71V6e07yamsKjt+ldkzyuwP+QJ/DGaeV8EN+dZBOF/j//jcyik/FAh8zcRr4g0Zh9S2KVdhKX91OHbj7jAvvC2HQq3YY9sv2ZjCwQjVPdSeMADF0Fk3GdIP48xh809hXXvVW+672vssYvp925Wfs2qZ5rb5RgKF+YdVBo0kTeS/9+eKVWFeZN4d/ygpffm/IiC94zKPQc3Pzb9zT+OCO+NGvnaEBhOIf8/jBej4ZwgqEuB05cLZCnpqvUAdLRmBP4xTMF+f1d9L57vM8Abg7wR6dcsiWB2lP3fHivvYXiueZBTU0IbVE5F3rwtHy6NKTqmXFmOyW1/zd4Y+xOE505PMEqwnmG+j2n2pnC8+2ZpCEEar79373tIIWgwCWAaIkXjJDBFfAiEY7sxtKocy+wZDpivYCy5Nozc8AevECgdpgWUj0AjIgg5ZPU7dFIO3YQV5pd5+n15NM5ExSO6HgJHT/CKHGGljNlSwfKEg824BqLw4S4KSQHEGJr4jnAV2sXDmHFafRpoj7HIU5jAf4zA8+b33L7bMpoPpdqeXUMs25FjPdA9Ivtu5zNW0Nh0rMb7ph/D/fQV+WNr+dvX7G7jO63DIk/GrvwHcBCYv2l1Z9WRoyrIMyl4JhDMhHsDfn300EeTfrfly59G9I//2RR/74rGj5H7goR1XVRfJpNHJ3trZK+QISYwR6ICVN+b2udnfX1+1NcP8h7wfEH+M5t+EPFM5i8I/oq9YuMtMXLBmK3PF4SA/zy3PlPj3a+ZCr7H9pkAI68m/VjKb03mbQnsNEEJgnHxo+lUY69qYXu8syxE/2v2Hv9ndUASz4KxQ1b5H6r23m1hNB/Bem8G8FZWQ93eOIsFYDyfJKP5FXj5kjVJ8ukls1Pwr84lI9PD1IQojMcYeA/ONHUE7lfv88148eNh7F5AsPK9/MtYR5+QcRb9hLyPlZ+Qt0H/fmbKGnjS+XkcaUeVcCn89b72/aTngBd4pKr7YrT4cXoZJ6nnhPtnI8bygRbf+XTsR896HDX+SQh8EwSg/LMQ+f7GTp6kUNX22Iuj+q2UK2inByebTwiMGSwxWDWQDBu44c9qoJ4SXBvY9LzR3e/4fXcrf/jy+x2G+nEE/O3ljRyeMXiOe3A5rMLP1dj2JjA/oUJ4/cgkeO9/PAg+90EagwMJ3GgzNgPHkplNYxjl0xjFeA4JcA/zaHvK+ARDYiSAbwEDZh7GMJiHAUBPHdwDNHBYGsp75OG3sadHoy0A8wE5wwnXIxmCpqkZzhL2zLMp1rY9bDplMdb3INN/3xpDDnw6+HBoRO99Jh2BePr524vDUHDlmqo23OPFT2amzZCi04UndGB8K79M862m5jJ5tPeJkUVRy6Z57F3QlojxJdVzWysOm/lxHoiRYOFplSxoLhu2CimfMu6y1fzC2zldv7BXyulGkPsZuQp63lpr3c4o8E13OR0TzT4BzdytE03TB4ZpSLGcxUNZg45KTzv/lhXnic2YQurxe4zC+q2jh7Jp4kO6Sc2+WaxqKaLN/qhPUj7RQzfAvYsAWDx0r1fsSFt6El1Ilpbk7MK7lCpKbjTXplRHlHguepq4NM96YGcOTbmnDKVueo3qEjFpypo+wSyl6iSOT/EKSHgNjzTl2kkpIa8lo6bao3zGdGWqlsP1kICE2tbqtpG1hL0pIlhp52qnB7u5fC2vS24LsmTal8ekmF2LuWcKczcpxP3eK9sTz6zKyGoHC8tr80D3uNpfPMK0c+ZiapNMCOyIpKBDBZUFhREZOmcNs72a1V63DWUi5PAoS7rFNuNbpwpNsYBtvMHtbdMAJejdviO7czjn2lq9plMpLjsd63GvOtqFpLWdpOErK2POlWjkapVOTjdhmyyAv9wkEqyANWNN5Y1zgLcoym7RHBeZNr6WLZFnQn+bla2WabUeVSUHlBAcr6vNLptfrmBKXfd1uWUyqiTxMy/7bsssyf0CwyN8NhtyqfIahiecU0ahe2fdrcyLA4ZhA1pWqFU14j1b2WKL4HKbnatSd/juUE1LNO+XDmdbxGTfYfZB1mtdrY2hsOnLRDDXTqsrxKFyN8flpCVXm0NA3c6HfkiU3FKUyXk2O7ql3VwxRTmLi6WzZN2bLqlpmEeH0OOHbdGkYiGnUiEz7K5L6KYnNU9PKG5LDiGzvky366OS2Nt8w2MTYo6mvi6yqDMJjmKO3VRQ6/Rpuys8WrvJ8PxlgPS8pTLKTo67lbpad5clI67tzakfLoYoMldFYHpqGw++bGJzmcpp2S04isb8fHOr8MHUBalwBh7TsqvOpjzbikadLA3U0fabzOGdGMTqjtclsClSUQ7opdFJQNzn6yWckCuabKPqUqLtpAiZkFXlaNvqm6ZZVt4tH5Yem0157jIhB1POI4q9bfYT1pQcL9zs2tnaVyZhX1aqI81VXJzV5WJA+wbF6nAmGQ6KtxF3slXThHhRbex07FE4JcU63tZxfvSpho+vaKERXrq9ZGVfnrU00mIzdhhjpeiGQFihsbmJU7avloUs+2zD6SkINkxsR+LeEre4xaOFcfUY1Tpj08usbGyDEMRdlO6nGT87LUsV7FpDhYNl5PcCvqqwLNdXBnowmsCaLVgmELbD6rS/LbexE2jKbD94Fh4Wixkl5oK3lGRzMQ2EM+eezRXfrOm1i2ZDY8RNsSkudbC80avdrafNet7IS0ZV6djsF9IZnGk1O+3hMmfnHMqg8NDisg8mHJEdW0OSUokmJuIxHmzJqHzNzO0Fvr3elpMsJg4HhXNzZthc2gBczyTQawyNK7JYoShVXg8u6ftRtcBP14Bo2ZUrGyRPq2ppno74jbpmdaD4u7AmJvRKxswyUk8XHcOvV8MK0GOydNz5hoqEalAIyF/7kL64uqlerUZPOu92oOYTP8AIP7vmU2KKqSdjvuVTQY6TVRPP1xO1IFvdI1rqfJIAH25bC2xmvJClOOvOBCCKl3bKcV1xFLDETMtANE8Vvz9b1iA5fMUn6u6S2toZ01aQnayT3oVEVrp8fMmJQRJKsy+OV8LMlNTZU8ZE2HtbfOafViPfSrKzXOqrrX2ofY9FpZ3Cl+ipMa/V1A8PC17FLpKynjC5YZONnLP1qpV1cxjombLyqSkKlBuxVyZs3HszNxdD6WBK7uCyZHKItzgvWvF5c8QuQ5aqZ2MJzH533jNX0rmgJ5YeFqF9PaAUv9qqV/KG0ZJS5IyvbzF0ayXSiZb6jSRHrXieY1ixYONLverPuNY7RpLZBWvy15W6WzXUrqTr1VY/TbHT2hCvws0/tCeD5pvM8GLh5IvSXIyYvdanwiaZFN1Emh/IdYnbVMt7MpFpZ5bHmdoGKbdUvBMHhlO1QdEkSQS57uUlGwqOa6cay3X6nHNwk5oAgsZnV5ttQnwISL6+zo8Kxqmat73sPH6nTYmVCIcPi+vbWPONBu14Ze5ElFcAKwvDAohtanp5A2SPFfYr2tpOd4wgXxYYdl0dPBeGOx6IY3ElUp4XZWqywuo+JMy5u7nc8ttKcq06uKQGmpR7R58sBtrZqdrZFbHDLQ71xtod5mYSBkm+NInDSQRbLLOnrjK1yYMVXM+coaFXUBi7izM0wkkgo0MuV+vlYCaNWPeNaZzXrnBIFhnv6vI01SVIrc46WMEkTLfA2rkXHxIHbwVZjOPSTUh3p3JFLBzQJa60EjVbvR51gT+v6OOuF+eJc1NtTktdVjklS2ZdDo0V5Ly/i27EVseYQnMvU51SVdcEXJykXK2ELmXwIGGOAs/tt2iz8Sp5etWZ4ihu8riMl9cFFU24eJ0fPSVNixkpidq632yjw2aTKaxzIobdZBmzS4sWpCy4hufNImH9BS3MhZp3TM9cxdIm1UOWnTE3rRbQUGqNoOs2ihcY2fFyajeXmoplNN5fJ0v5yKKU2SRNU2BnETsfi1o8eylqn89hutQUztxN7P48UwnL2FgLy2pcvC03x1bZtJPjLtecpZzxmK+mMz87D9r0Alk7kB0xPqP9zsQkp1Tw6bwteKE28miOnzV4ElpXkOr0qyqgHsaWqUavVbAiz+ZC8aZD3HJtL0xX5CC0aa6e1bYJ45avDrh7nlphXItRxK1927niC45SD3TFR4cLaS2DtbktlDwj+2XqEINmxNOBd6L5RIyyWaof9xvNVWu8dWSuoTJJMBptszSSZDFV20MmpsJyW+x4d5ds13NpFexAnlnpvsg3mp72RJR2w4G0pvy+vERbLNAHXK7E9tqdID/MCTseipmgrbhSt2JA7zs1Mp2gzUTTpQemWwFevtVi68dFevW19fS8XDcBqRGT227qHluhopNzd+jn1bFZ3uQDtJ/G1v40j/PS2M9OR/fqOdtueqEjLVudVzOrP2+zMhPXtX6rog11jvZqiG/2ehikbnuQl5W+W5vi5LByMTUvImyYi8vtFZxTPEiM+ZBlfiZud6dBCE8iuj5dIzk7W1RurnX1sHDcpNxFqyV/jCLb3Y7jo2XxC19dE91JOFzCDZxKHSHnN2a01Puw0phol3SljbnMTb9h6fIwLO2qlqbiwLUL/7Zp5Uho28Et3daMqy4kg/S8KKX+BoFrL2zKbv3p8cJdmYg6p1iLzbrMpYtBOagu4wp5stQ4A621ykrzoQkc1LosEqLudWohgNj13OmlXejcyjihdFIaE7PR8fIQYZtzfpjgQ18ebo5AbmNMwHFyiU4KLV80C2IeplO6AJdFQJ5Mv0jOWNg7+a7eR5wu+dh1Ei82U80RepXOhKKMT41GzzthrmOLvF0BPVgs53Yqh5W6E5xNV2Q7k75ipDtNzUoxBY0IGGJvrY6sG8gMdy4xac8fL03IO3wxqR1l1dqqGq7mcHIgh4U6LxxmLjtGs/ONg0yQzo6uyeVJ2bnCNCRw3VPxLuI2E4F1St6TUnYvZfursGaCdaZR2Aqv1ijJZyx5ZtlbBI8ViurrJFXXIJycTKslRe3U0a6THW/kjoVQ38KhZmo8nV/OBEENswMa+Lp+M5rNuYBzv0Q2O6Ac4ASlcPo+kPuCnZOKs2qEbm01dj7NlCI+RPNkgxd05C3hjHTD8CK7zP10SeRROYCJeNbYS8M4fpT2opX4BurOsdtUuQKCaWYdWuIetZ/PvdarWIHljEwRcTOkmP0gD2VFbITmsO6I9Q1EROW5Ct7I6mGGTiZKq/sBn+2bwWBrd9Itp1lCk6e1baNkuumxgnC315C5gKtAATd3Rc3S9YWzIs4bHrT5WadDLY547sBMKDORZoe5LLPi/kBzfgCMrtFhU4qV/kyuMFKq0oR0Mn8/We12OJ56NxMD87DEonpuTEJj15xitr1ku5TabkNvcxSOrTdRPXhImpWYncjOKjN8ltFRnnIysRWmvXcqunDKkQTKMFyZOLFSVRfb0Hplv+QmccjMqoUzz7T2uEGlOVCzc992sc8mV2U4m4w4YfBJOc9DEb3s0EN05LSmD3thwlPMui4VbA0PIywoWNbiu6viOkc6g2ejob6JgyUxV3iEpNvJ0vI8rUtO3QyOzi61vXKcwsosPRV43+2bJFhd6tliI28ysF3kx2i2nBH4hL2q3H5RcxYs6+YsgmXWdb58Wm0WdadSLU7I611oSVythTVLrpZWWoQnY2ZpMyYdTkOgSPA8NN2WbXiU8GlGzhhJ0LfE0iKCiTEntoUl4CR1OdXBwVincsyn8zXHStSSb91e3NghnEFv20K/OfE+oJroFtTjOHPbHwmKLbPz1JsaR3Zx7ryYYnZHqwimx0igdelIL2fYap/yuyl6ybjbrnNYSi+vBKoRcA525xptuBbdzAO9oUO67FrpslBJiqHWkiXvexkOYfn2xkan7FL5VsPtN6uAwNestnAd+bLvMkI9zmRsRqqzHZ33uJia++aUX0M/H8Buvlfc1U6MYrE7HQjUPFrYgaOPCjyriVCxEqPrCxYY+lmaGavb+dxy0hW4m5o6CBHp0McAlRhiUt4o4Mg1iopZeyLRQq+cbuPNbuUM360TjsWdvdyZA/BOkyq/0jtm2XnGngSNvYocgkTrdi+ticl8Mknw3uE3zuxGLewhYamoPYV7h6JVo+MksLtitoCi5NxNF7Fj+pWZwwSZjXDD48XMOnI2x1urK2jENUlgeMd1uRKzl1g+JYx/TuDxbk/VdHic3tA0aqZ9Z1TWdCGHF5sKlnuBx2J+IeNbOFm3HnfUlQRlpkLCsnBm38GjyK2drvJqbinChr3dXNpOEmKXLbrWP0s6GR4mrbxpgTH39uF61eXwoBK2bQRHmiu9sINzu00Xyj7jwtmVkNBkrkMCSXKZUTbzLqmEYdYwvegPHo9hRjI9LtZyTyaosyBSXfecwRJJWQx7PEfXXkUfIkjxRnebMkVzOag9QZtT29UCufCVrVSg+KDMh2MGTzvuPI22ATxOiW3QxZk+OVhH71bDFkgL2j6fRvSgD6QVXQBKxxArv2vJyZKu1Y5RJpw4W+745Wl34LiXTy/jo+XnA+J/+43v+OTu/9kDxMezvrcvhu6PhoHtfbnr+vLvTfnl00vpRtCQx0PRKmmC56PEf3gk+vmvvkYYd/WPL03H76u6+u15eW0H45/2vESZ11R12X+r8qS5P4z99OI01fjnBtW350Pnl7sTaXF/gv2mCL633fsz4G91/s2LqiKvwMv49wDjtzDAi+z67TJ4Ph2Gu3sYhsitvpEM/Q2Uxejh85sJ6Bjxir3iL7//XxI+fMRLJQAA -->
