---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-reporting-and-analytics"
description: "Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics", "rar_sha256": "e0724f507bde903b718d4a787e4723ed37113a7c0e24eddbed55460418f7b3f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_manage_reporting_and_analytics_agent.py` and in the RCI capsule.

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

Configure and manage reporting and analytics Demo Data Generator — Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 e0724f507bde903b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_reporting_and_analytics_agent.py` first:

```bash
python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py   # or on stdin
python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage reporting and analytics Demo Data Generator — Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics',
    "version": '2.0.0',
    "display_name": 'Configure and manage reporting and analytics Demo Data Generator',
    "description": 'Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-configure-and-manage-reporting-and-analytics',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8be9fae2c476db92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-reporting-and-analytics'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-manage-reporting-and-analytics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConfigureAndManageReportingAndAnalytics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndManageReportingAndAnalytics'
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
    print(DemoDataConfigureAndManageReportingAndAnalytics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSJLtX9GL+ZBZrcxALAKUffqcQUgsEhJiESAq62Sy7zsIUE399+dIisiqqe55r3vmwyhPRghwNze7ZnbN3IlfX6yuDYv65cuL4ln5jLXSNAq9embl7owu+qJOwK8iscH/mVPkbR3ZXVvUzcunF9drnDoq26jIwXTWy73aar3mPtWpvft38CuNmjZyZq6XFeDSKWq3mflFPUnzo6CrvfuEzMqtwAMDyqJuozy43wT30hFMbmZRPrNmDbhnF8Os9XIrb+9C2tqK8rfhZZQW7axxwOM6KppXoKM3WFmZes3Ll59/+fQSge8vX359cVKrAbdeNkCnjdVa9JsqVO4e7orIb3qAO9SbFkBeauUBmFiOALQcXJdeDdTIwC3X82fPq4+Nl/qfZn/5S9JbddD89OVrPnt+vr5M/+Qun7WhN2sLq2k9gJZVWnaURu34OqPS3hon4NquzpvJaoB5Hrw+Zv6QVJSzv03PPj4WeQ289uPXl6KcnAA88vXlpxnA5+tL3U3fXycp5cefXtOi9+qPP/2Q03R27DntJAxo/frtef0UCwb+GBr591X/BqQ+fG97X19+Z9z0eeg92QlmvrzGRZR/fAgu6+I6Oc7xPv70j8Q6oeckU8D8f8n9+SE49CwX2PRU/KdPd5B/mc2fBr3L/MfLlsCt/4wlYPjbcp9mT6D+kew7/v9JdBrlIDfeEP+74v7ehPnfZj//Q9v+qwmfZv5XEOxpdAXRYafel9mv35TTlv75g/vj5odffgOi/59ilKKrnbuEbyBnI99r2m/ffv7Q3G9/+OXnD10JYs2zsm9dnf49mX8P1/s6f0DwOerjH+eC9c95khd9PnuP9NmvRfl/6t9eZxqgGvfH/ebL7Pf5Mn3ms8mIt0UfEPwuZxqg6+9w/OnlN0AZObCmc+6PQZb/27/NDpFTF03htzPFKbp2BhzcRpk3Ka+GEaCq5p7btQdwbSIA7HMciP/Jw5PGhT/7/u/OnV0/O092hSaC/OYCNvr2zozfAKt9ezDjt3dmvN98Z8bvrzMVrFbUURCBezOZOp2+ThMAQQJNytprvPoKOMYeW+8zYKfP05eJT7//awt+u8t+Lcfvd86NHkwm0/zEYk2Xeq8TEnro5U+7HVBWvMFzOrBsWjhARz8CjPwJINQU6RWw4IRak0RpOnMjUCFAeRnvsgGyXyZh379/t60m/Jo/aBedPepOA4EB7+rMPn8GxvppFITt19xzwmL24dffPsz+Y/ZfzboLn9Y4gYrw9BvQcKeIxxnIwy4Dw6bqA2jacu9++/W3J+RADKh4M+DlyI+8x2QQx4nnvuGvcNRnZInPbA/gDjDP3mpb1L7OeH/2ru+z7E1sHxZNC2pl6eWulzsjkGoBc96RzKcCB4K18cdPs67x7qt+t6cqCFTMACFY7ffZgT6B2lKk4Mek5n0QmFzkEYD/PToe94GQ+kMzW7+JeJ0dp8idlVZtlWFtPdfwrYdfQE15mw6EW7Pc67/mU131JqjuafSAJ5j6ganu3136efI5KPkZCC63eVs7ePYM7ky9V8L6a948U8SqvXu3AFQZZ0EXuVPh+OszpJqw6FL3jh/QdJL09IL79Mo9Bul/psGYWoHZ1AvMno3MVDw7ZAFjs/+Fnc1kHsWy8pal1O1mtj2q8uUB+9SjTe55tHWgo3gIm1LsR5fxxlFvVP01TyMQQ/X418fIu7OeYx70B4xxAbfId/lAMQD7JPceyFNg1vWUAtbX/K0mfAJW3QkQ+BJkPciKKRjfFpyevmkagtSern/0B08wJ8tBsM7Kzk4BzL7nubblJECrekrGp3dAVHtTYvZh5IR/sGoGpIPgAfJnQIkIpBeoG3fojgUwE0Dr10X2Y3g0ORVo4XYO0BY0wd7rTAf5NMVUA5IYtE7TGIDCh7uoWeYBjIGK7wg3oVU+lJn65qeC1uSLIgNB83sPPB/+yIC7LpP6QKo1sfLXvJ942vWGh2ff9Xz6CiibTTl7n/RHdz9tnf2+eP31a37X8b00ACpIp7r/O3BA/NXZI8wnJmsAG2XeM4BAJNxL/OujSj/agHddvvxps/Dxn9tP3Ovu+Y+e+zIL27ZsvkDQo1a+lcpXwCMQiJGo9Jp72fw84fX5Pe0+g8U+P9Lu83va3W++p90fVnuA92X2z2n8BxHPUP8yg18Xr4vpkRCBbAUIPT8AIPrz+vIZm55+zWXvh+ef4TFxczqCOv1eqN6GgGoV1F4wDX4Urmaqdz0osXemBr75mr9HxzN3QCHIg6nKNsXvcvpesYGvH658LyjgUd6Ctd2pFwy8aeOUTuo33suXvEvTTy+5lXn/0oZpKiMgogE808YLZBdottrIu1+9N17TxR93k/e8A4ThFl+m9Ps0m5rkT7P3fvfT7G0Hct/l5R3Ygv089drTkmAo+PU+9n2ransvYBPYjuVkymNbNbV4z9b7z0pMWQc0drypNSje03ha8U9CwJcg8Oo/CxHvX6z0ySVNa02FPmrfGKABerqgbfo0A84EmQmSDYRuByb8eRmwTu1VHaio7mTuD/x+mFU8bPntDkP72Jv++vLGKU8fPPtQMBwk7+dmqqkQCFywILh+hBh49j/UoT6lAm4EvRAQ6y0IBPOXC8J2vdUCtQmYdDGLIAkPIxDUc1EChlGLcBYegnmua3vuconhCwwmfcJGfRjIe4Tvt6mdiCZNEctySIeAMXdFWLjjoQsbdTwYgV0C9RbLFeqTpAeE/ZiaAGJ9mv8wd8L2vVmeYHqi8OuLjWNgJIc1PPX40NBKswhDsI+hvapxn2riVdIOe82sr25tC17lHTDE6ReWY+/syo+tNJxL610VZdRuURA6tkzm8m7eq4SQGwGVyE5aJiQh2ptjt5M5anCMlXhyHWW7leLDctFoSl2WfCTE+yG6tNjufE4VGNWqNB6k201oCW0fG0F0hAsy8trLaScytbiztPneyFECyXE1nOtJOldhz8n0/swqi7rcl3XMx4Dsztdm3lUhPRy4SMcFL0oTzYHpMamznTYXs3TMz63K16GSJWqcWPltuXTzDUn4xgnYMUI+dxpsJfZq2mg3axaOdi1eK61m40gBJkax02BnNVn1uGMly6sCb2LGLIFNfFUTyoEAxDfilhtI5UkXt0kmJNhV34yLJNQFzTgDznUkg9H38eZEK66mZHlFb2FUGKPQjZgx1+DQxdELwV41vM7EW9ms0tKCSnyfLsJKVmOIJhVjd/HoNE0btWQMhQ75cXXuQpquF+cj0ml17ov8SC+RctdQknaOTc+mIpOojO2c5WQTPy9Q3dzWjQHp5XF9E5TGjDJIdxSkKmMqSuxsXqgJBpUBE12QrW0fZQuObnHS1ZGFd7qgX4g9idI7cQ7rabI882WzqCQ4pAyzj/CFhDRGpo61ryXVcnXblKrTn1RdsK+dq/hbq2u67Lgg2Zrp6M1wyWzEX6JbekAvumSvNXa4qp1SdTET17GhDhTY55RJkda0vbVQwt7HvGEuq5NX2bB2EaDhyNSs7EesbUrNeiVwWywMYacKwPJOP5rQqoZhbWxwoliQq6RZXvRSH0CTHx838h6EQpiniCkfjvpCtflqVcb2uswQmnQOSO9Xtm5fj4N/LZGlH/R50Z2ChR9SZE+WGn1ueJwI5wfnZq4gEV0c+lEUMjW3B0eOwnFgnEQftbFs4svtNOp7DW/3dQYesNjtYqeMyx4u2XJ3kjP40K2HHYyyQ5JdaBPSlBRbboT64oWiJwQ1tZEW+rFWD4yjtNgxoOZxJfA7ZHGO5OMg4rvNmjZdflXRnRRVHT3m9QE77Hosc+uRPw77GBvnbYvbnuGNUcT051bB98V2lRiyAgvdnqsvV1at+psA0ksRbfh2O6ZjfPPkHJAVdq1qbShzb4NAG2jrWfNyow0KeYVpGJ9fsaWxxptm2O7N9ZZdxAUkspsY9yKOU1iexg8yExwO5/rknGxVy9VuZeUrmhOP7UanNlWkJx5u8ic5oAtezZTMK1cGiFXbZBpsg1g8dL0tjXFnpp7ILMYbA+30rs0VBC1LnRzmdnakblVpJGR/kI4Jst6hS3pnrBqN1o47vq3Fbh+5OlZSlstEbbm9YYfr3jRzRR/OVnhoHOYAbSvIIkNxD0i7jeI9g+4rSIb5cLSqMcgtwnVPTB8dxXOlOFvCWguimqgR0oqRSm3aQ0lG3SrowstSM7NFFZA8uhH3td5IS4/ND4yEVlYaXyR9529I1TV4RXWz5cKpGsy2FAcdoLrvcuMCwNocyqYssbjpuxrikdEZPVuMXJlkUcplINBeX/GVxR3HRbjo/FVO73ZzfQuRtrVQTlBgsEph2lVydMYtRW8pO10SrLNpvPOFjyDsQMOuFClufsk5tC+bS8LszWHwhSUO0WYWeqZNqey+itCekBGFHpAsoTeh2p63OCT58Hg8iBG8h2Wpd5KANxb2UDUufQtNc62fiJiWRv4cXSs5YxNKOZ2X5kW62SWt09E6pcrQyJTljgElQ8vDRc6dSqXhLXmHlBKn1/LtfHOWiLGBBadED/h+vNVL3M/tFemfsWi0UhazbvZmedwfuhqrFWJhJhAdaHQskRAJnSiOwiMCv6UIswgK6YrrIz3XG2O8+FfbuBGnJMKc7nwco4LScuOaIcuSouKGFdPTRlpmmcMu0r4qTSFVL8sLR89jAl7GnNBRI05r+WnYZr3JL7tsV7mWyHkyvR+4PKos2BEWzIZa7cwISS/0Xkrl0jCbgTHZjt4O9cnXmMuRtRXIyKAqu6GpeBucNusSZZAvloUYTYpju5WabPW5WoxEdzp26+7ajlquMb6BXKUOQ8ujhLkwpFFOL13YNDaNfQPtmNqPmQOhZTfO2G9Y9igfkAVATRNt3WuxU0r4ccYlZI7ZJSMcZFgIrUIWLDpHIHiO6e4yDPhxk3phYYoCNpwAIaTE+QTzcwyRaKJqGObYmRIHG1zBt0Ex35dV0q9UmXHTiFshh7BSllRP2RsML52FRV1ul7jr2x1z03t/cBdHKTm3hgRzG4Y/4+tdYm93GRWSjDYYojwsELkuF+QgmKxlC1ucM1xzWwmZ55AgM/G1R223K4fpKgI2K/iGRDtWzvjNDkvrU85VddEeL4ziyIo0iOuBGEvERGR0cYSPVzbcG3UKh3aHMrlYMUWV4rp0vVxXhlYlAblEsAWbcEUO8sXelHN0foikbFHEjRx7ubxXFxfF0TgdC874Ah4jF0UqyiRy7XJmw0gzZVQSlhE6mhxfFkE0bJgdZLLKPOSPEj467Tlcoc488VUpLddxQXlt4ts0Ny/F1pDHg30Szix62KSG1RA4S7fKGVbTOHe3S5q7XvMcl1sUdWgpUdiaF5dUPl9Y50Dl1JJc4bahjLIpXImbghgmfkAOVxlsGsY2ReqVA3qgs8zP15FAtAR9ZiV6OAc2R4X9HiESV9hfuDmv7t1LWPcnecXV2tzN4c14xPp6e4vE47UXAZ3oc3PgBo5NdtZKGUvxUPXbriTMxfFcFcb1DK+x0fTGcrSgVZWxqS+Wc0qAuXPihLC/h6lFFmQ5j9uyFNGd4lfbtUK0GiUtl52Hj1pM7Y1dcB55E79cWNykSj/yfT5yW7sVNcpLGkISxuVSUAw43pCcrJDKBVH547pBT5WT+ttTVtaVEFDu4HU7Xjk41BjKh3ondWsFZYgE3nEK5oRVOSrIZS+EOmI2stPTnlef6IN47Q9J7h6DMlvt3fNSslp2J5iDgx/sPW4mKVtLmwNoBocKn49NO08P8+0C7plOccLV4oDTNjwu4sqYLzhzD2/JrA5VVrPHoWfn1pLyTDiXSDlt6twjtj5/69VueT6KcG0ndYwyMEPZY51V0SU+y40Sb7Gtv7eowNldrmdxQF2HPIb82dnDzWG3FUJfX18v0v4A3SRAKPEYDWmdzS8+uqs5G1n7g7OCFCQbt9VRg8lkC1/3qaYq0bo25au3RdZoFoh9L8mlKAd8k6JVUov57tIUnFKlJ5pv88w9Y6ZpG92mWSg2W5jBcdCzgRkjxo4OjKBQyGVe2iSmG/ts09FmMqrtMVvM1W2IxlcGYjWGUkchzu2bqBKpG2fFYbVjFmXvVAvpsJP2mtAr+7jLKNlRDyJigS1Tzx4gPhhxMy9oORBAihLCpZwTDhHrYRJIt76GanG/2pBgg+IcK6Zu612LhIuNsecF9qaKZCPuCprIDzc4yghyxyCkntaUr5SrHetiY7aO4zPuaadyz4S4grBbrOBcAEK+Ec/RYApyxihhNh6spZBarFp3vmHt1xV6sCiqpc5j6+IYeyuWkK9La5Vu9rtwvYVQuOgdPdEKBZE774j0pGTpA34+CCpmwopk+3oyjizOIuU13eICQZ3Vrr+ecGiTwIKIFzhhdSFvrfmtYeFXvNwjXNvy6vUaib5GKRKBr0U46r1ex43ljSPw/Opxss/YkFv53FyqINcieOIkRBQOk5bRYaJQXGoXJy7roCUu5BGOd5hC6y1Sx5DlKNXobgAFSQo9+thhTZ3GyrbQE+G4Mb9qzyutU01uzfNdMfoK2CQPdLiOIZtkVnw8Lhx0IxRtRho3rs8Pa2Vd2GUdxU3ln0S+3l4rq7G9JT9vecxBxLgLeNRFtSu7Qro2vPgisUdIvN+Pva/EGErlBIuCHLdr0omHFbyaQ0EK8ay01MIaJSVogBftuEQNbqxW3YLpTKPmVcRe0Fy1W4lB7RichAZKubfzA41gt0GEJNNS1wHZugMarqWeTTktj3j87Eje+dZtLkKcnAaTC9GrwByFDt3Pl8iecrSD5ubSwhOijZE1ponSxcn01evecS43qTQTl890o3cHtdIR+5T2h95Y3ZZ+xBHybeO4Q47Jl1sT3ZrtKZoT+HhNiHTTNTeF3ecbY3tT4xAfrkeCAk2EwPhs0GW5OfJp4RNaJ65Sl+GhOQrVHEeLoiLU3emyzng+v/Yr4Rp4bECIxCrfNfvOsEj3sLaGtX3RTMSurbmfDvZSJtTblYrcK7zpxNxOCa6+CrtVkBUUBTX4Ne/PO5KPcCOQaVRcb4nIxkpX4fUC7fQrtFvtJMnJDqcRZhaFXaSDaKcVVgd+SZ3iTF84nbYOTsFQbJcQsilGldy5NRwKKKc7vkiR55o1+iiMdlvUGA3/FPSOyF3k2DrCErdttG13JG8Omki9xIRloArrnU4cSY4OJFy4WFEPXZEt2WrtyGwc6HANjvuzTUOYjt4s8uSu3KjQMdVE3AWM7xEzX1/a7Wm82kS2WSDa/szX8MLDbCzTvZHDkdjY1Q6Bk+YKS/a8g0qrTNx0kMogp81GX/AslLvBgYnwTTPHDCq/bQ46uYLbRSYJadCIY2Hhhr220c5L/fQWq67qzjsGNLfe1bU2W88QMc7bhBjv9Cuql4yVxe/n3Hwlgq104FMDtNgXmFWcHQ5bzXcah6i+7lxbub8d687hW0xiQxRF/BDjroKbr+oDOzdW9ursdQ4OEYf14RKc5mB7gGubWyDgJqavkvmprFekg/nHlo49hCUCdYkPJkFCOq/ja/faexCJOCGmbTwYpewa1/2ADzDJxeQyoiySkWzERdxOnm85fqx8Ry5ws1pB9DWcwzV50QOLpi9MZXUCh85JbdjInZ/ayflk5Li/VO0evkUjiyDjfF8p7A27SksVO+EcU4Ckli6ccuYBB28MLuMKDzEPtaEvyM630dYcV607F4jmLIlTqXGPpCYk87ZfYyI3kGd4ZW2N5RHNNgnF1CEtCrXElPEGVB9tfoHxA56Yi122OTQ56B8r5DhP14rvjWlxzD3J53TJPHXt9bS5xoSG81RKnomdG/omiXAIq6qufbuERM50I8qTeQdQEsWwW1+Mtb4VMnQbpa0LVQld+CWa77vGQ4iMIm9l2p84gOSut/Y3Zild9nZx4XU6z0d/baAyr50V2RlqaN+dCl9fDXEi+piIsrubrcWJD60djjCYLbIPKOrl08t0iv08i/5vvr6ezgL/x44kH6eHb++v7kfRnuV+ua/15b+r6C+fXmonAmo+jmibtAueR5f/6YD287/2LmSSOT7eHk+v5Ib27dC/tYLpD6deotztmrYevzVF2t0Pjj+92F0z/c1G8+15QP5yByArH6ftT4PBd8vNojya3u1+a4tvjxNr72X6u4rpXZPnRj8ug+dhNhAwAh9PGKD48ptXlxMEzzcs02nv9Irl5bf/C5A2HgC7JgAA -->
