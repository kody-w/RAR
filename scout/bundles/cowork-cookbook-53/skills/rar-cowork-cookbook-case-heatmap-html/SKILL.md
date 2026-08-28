---
name: "rar-cowork-cookbook-case-heatmap-html"
description: "Builds an interactive HTML heatmap of customer service cases by product category \u00d7 priority \u00d7 age bucket, with drill-through tooltips."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/case_heatmap_html", "rar_sha256": "02589177681d025837a579a4ca089a1a8e7c1737472aabab38a5c94fc6433558", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/case_heatmap_html`. The original RAPP
agent is preserved byte-for-byte in `case_heatmap_html_agent.py` and in the RCI capsule.

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

Customer Service Case Heatmap (HTML) — Builds an interactive HTML heatmap of customer service cases by product category × priority × age bucket, with drill-through tooltips.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/case-heatmap-html
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `case_heatmap_html_agent.py` and embedded as the fenced Python below (sha256 02589177681d0258…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `case_heatmap_html_agent.py` first:

```bash
python3 case_heatmap_html_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 case_heatmap_html_agent.py   # or on stdin
python3 case_heatmap_html_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Service Case Heatmap (HTML) — Builds an interactive HTML heatmap of customer service cases by product category × priority × age bucket, with drill-through tooltips.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/case-heatmap-html
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/case_heatmap_html',
    "version": '2.0.1',
    "display_name": 'Customer Service Case Heatmap (HTML)',
    "description": 'Builds an interactive HTML heatmap of customer service cases by product category × priority × age bucket, with drill-through tooltips.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'case-heatmap-html',
        "upstream_url": 'https://coworkcookbook.com/recipes/case-heatmap-html',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2e6ac1bee32eafe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/case-heatmap-html', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class CaseHeatmapHtml(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CaseHeatmapHtml'
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
    print(CaseHeatmapHtml().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166bOi2Lbnv0Kf9yGzHplHZjRv3IhGVEBUZhUqKzKZB5lkkKFe/e+9Uc/JqldV9/WN6A9tDkdg7TWv31p7c359sdsmKqqXLy+ab+cQZ6dpHPkVZOcexBZdUV3Aj+LigH+QW+RNFTttU1T1y6cXz6/dKi6buMjB8mUbp14N1kFx3viV7TbxzYd4fb+DIt9uMruEigBy27opMsC/9qtb7PqQa9d+DTkDVFaF17oNuNH4YVEN0NcWQTwa3I+LKm7er+3Qh5zWvfjNJ6iLmwjyqjhNPzdRVbRhBDVFkTZxWb8CBf3ezsrUr1++/PzLp5cYfH/58uuLm9o1uPXCAsn8QzO+yVJAn9p5CB6UA/BIDq5LvwqKKgO3PD+Anlcfaz8NPkH/+Z+Xzq7C+qcvX3Po+fn6Mv1R2xxqIh9oYteN7wGDStuJU2DCK8SknT3UUOU3bZUDZ0E1cGgevj5W/uBUlNA/p2cfH0JeQ7/5+PWlACrYk7u/vvwEFRWQV7XT99eJS/nxp9e06Pzq408/+NStk/jAqYAZ0Pr12/P6yRYQ/iCNg7vUfwKuj8A6/teX3xk3fR56T3aClS+vSRHnHx+MQfRufm7nrv/xp79j60a+e0njuvm/4vvzgzHIHQ/Y9FT8p093J/8CwU+D3nn+vdgShPXfsQSQv4n7BD0d9Xe87/7/b6zTOAcZ/ebxv2T3Vwvgf0I//61t/2rBJyj4+rLyU1Bule2k/hfo12+avGZ//uD9uPnhl98A6/+RjVa0lXvn8C2z8zjw6+bbt58/1PfbH375+UNbglzz7exbW6V/xfOv/HqX8wcPPqk+/nEtkG/kl7zocug906Ffi/J/Vb+9Qkc7jb0f9+sv0O/rZfrA0GTEm9CHC35XMzXQ9Xd+/OnlNwAJObAGgM70GFT5f/wHtI/dqqiLoIE0t2gbCAS4iTN/Ul6P4hoCf6farnzg1zoGjn3SgfyfIjxpDFDu+/9279D52X1C52yCuW9PHPwWAbj5/grpgBGAtjDO7RRSGVn+mgNwy5tJSFn5E0IC+HCGxv8MgOfz9AVgK/T9T7y+3Ze9lsP3O2zHD/xRWWHCnrpN/ddJ/1Pk509tXYDSfu+7LeCYFi4QH8QAJz8Bu+oiBbDdTLbWFwCskBdXwLAJkCfewB9fJmbfv3937Dr6mj/AEoceraCeAYJ3daDPn4EdQRqHUfM1992ogD78+tsH6L+gf7XqznySIQOcfnobaLjVpAMEqqfNABkIBAgdgIa7t3/97elNwCYHvQXEJg5i/7EYZN/F995cq/HMZ4ykIMcHLgXuzMqiagACQ3HzCgkB9K4vEDo9mjA6KuoG8vzSzz0/dwfA1QbmvHsyLxqoBilWB8MnqK39u9TvTmXfVcxAGdvNd2jPyvfeBP6b1LwTgcVFHgP3vwf+cR8wqT7U0PKNxSt0mPINKu3KLqPKfsoI7EdcQCd4Ww6Y21Dud1/zqdv5k6vuyf9wDyACnnGfIf08xRz09AxUule/yb7T2FPf0u/9q/qa18/EtqspFC4AeiA0bGNvgvt/PFOqjoo29e7+A5pOnJ5R8J5Ruecg+9b+tWf7n5ow9OzC0MdpWvgJNHoMQQno/7eBYtKf4Th1zTH6egWtD7pqPvw6zUWT/x+j1MQaJNejhn40/zfoeEPQr3kagySphn88KO/ReNI8UKmtgPNURr3zB6kAjJz43jN1Mquqphy3v+ZvUP0JBP+OSyBYoKxB2k/Z9iZwevqmaQRqd7r+0bbvka28qchBNkJl66QgUwLf9xzbvQCtqqnanqEBaetPzu+i2I3+YBUEuANXA/4QUCIG9QPg/O66QwHMBIUWVEX2gzyehqFHpIC2YPD0X6ETKJgpaUAUfTDRTDTACx/urKDMBz4GKr57uI7s8qHMNKs+FbSnWBQZiPzvI/B8+CPF77pM6gOutmc3wJfdhLGe3z8i+67nM1ZA2WwqyvuiP4b7aSv0+57yj6/5Xcd3WAe1nk7t+HfOgUBuZ/UdXCeoqgHcZP4zgUAm3Dvv66N5Prrzuy5f/jSgf/z3Zvh7OzT+GLkvUNQ0Zf1lNnu0sLcO9gqAYgZyJC79+t7NPj+L8PPUgf7A6OGXL9C/p8wfWDyz+AuEviKvyPRoB2p7StPnB9jOfl6an4np6ddc9X8E9Rn5CVfTYQKCtybzRgI6TVj54UT8aDr11Ks60B7vKAvc/jV/D/yzLACI5+HUIevid+V677YgjI8ovTcD8ChvgGxvmr5Cf9qKpJP6tf/yJW/T9NNLbmf+X25BJogHyQjMn7YqoDDA+NLE/v3qfZSZLv64+bqXDKh1r/gyVc4naBo7P0HvE+Qn6G2mv++L8hZsan6eptdJJCAFP95p33d2jv8Ctk3NUE6qPjYq09D0HGb/rMRUMEBj15/advFegZPEPzEBX8LQr/7MRLp/sdMnDNSNPTXhuHkr3hro6YGR5hMEggWKCtQJgL8WLPizGCCn8q8t6HbeZO4P//0wq3jY8tvdDc1jt/fryxscPGPwnOwAOai7z/XU72YgMYFAcP1IIfDsf575ngsAYoERBKxAMHK+QGmamqPe9B2nbZJe2IRrI/OFjdpzn3ZRGqcJGrNtx3bwuU26CyJwKQLHSXIO+D0y79vUxeNJCR8JfHyBYq6HUxhJEoA9Zi88m6Bt20PmcxqhAw+A+o+lFwB3T8selkxuex8/Jw88Dfz1xaEIQMkTtcA8PuxscbQpjHbUyIEryjfJgFLwdWlcMppW0MuNqhJpeUq0bk+2hhOy0qDySKMYEcwpXqqvlCUcdytauV2ywNrNx82CuEgYcmbhjnNidBzLjkRh2N2jirIUZf2UelcRKTHBLatMibChOoa77nRrqj68kMHtnC8WPU8vYDXAqq1lXaNcztyuMgLxcmncsF9VjsRdUbNI87LH6KXUITHu1+LmaG97wz9yYjNEOI2Os14XS+3YmuO5q0/oPDteRadWU9NJS3MYMOdYpjrq1/tr6WzFTVK4iUH6t1U483F+oNuu8m5OhgcpLpxbvDPWotkaRwI/obXRn6+ZflSzwj0FS9O6KfsANcIqbLzU3N5UMttrKN3macWm7rDedutlL6K7i7MbL7i8yuvazaKNczLP9cZPtTTaXecedyJxIT1wek5vrsbpenUtBUyLW3YumeTpZnVOlQTIAe6H3Vn0O9ROtY1mdbVesvtZJW3321OXqX0ykOFlDC/L8kyyxdmSBicxOkw+I6a0lxBij4ShOHbUYPODRxTU1r9hdmlgpGlmpcPC4XFwLkqp3JwmAjuKipcJndOvURaHsybszLReYpSd9NWS6rq6irXrLeFilxZhbM7zZ6rShk3C+PnVO7Fbwab5RBRHigq983jkhy7Pxos7p5aXTWvi1TWlUSoXzpbjzfkabnNhECwiLE+HBS3te3xZ2z3HMQdS24kuIdAzzREk0wvW7Ei1lM5odd/EG9gLhTpj8+EaUddGPSbyzCTXQiigdMgyOc2Z5GqdbwnxJJmlp/KEnOO36/zkbA7H6EjvSSK3sl20MG0RcxFtvRM03+idw3lbHQ6NgVEzsd+mWYcPnpgS0g5jjjS/IkQe41ObUlrV1ukljcrWHIazGbKJqcOIOJUmHVstOfsGqReldeTLVvO3MF96cWKo6txMpLjH2E1XEygzLKiob7rbzNrLY+MtdVjk9NRWJH9yFkIfXNToE/s075p12YmR22GX5Z5DDFUngoIIvXpRq6LKF5ZwYNjIrEU+VUehI1wsdHUJpcbKZa/w/lZphwyPZA4uuTG46Ceerr0xoxBKudSLRTjTKaPdV9RO3gcBU+0O52zTUHICV3O23cznHIfkGDzfHWhqRpwyGSfVcLui+N3ZVo/HUsKI4eL0tMH1WeEpfre+wRdLzqhdnFBpuO/NuS6mMgFKMzodi/oGxvFLZYQpOvMW1VLcOnrudbHRI4vD5ZwjfrzbW7staeKrIT9hniTMHDqLOFXdmkeVL6mzOKTaDaXEBX1ai1teqJBsYfnyQQlX1jxU07Ak+DO6q8eT1FonQRdy9hJg1i1DCqWOFm5mRlp8HIrgwmgCm4o+Q5So4M2z0ZL1oxCp6jDuzmEU4WVanbpxMwR7q455krnWrdvVIxmzyZnRFIe9KqWLbdt9eFsjCdcdD8dWJltaOCG4c0AuvpbW9uq4rG7IaJBICPsMqaKZykcMvrJwX2/WcFafo0aNooi6yFUSLYbdoASkp63YkGvPIisZ6NGiE2rOo/E+cOQW09PNktD7YWwinemDDceOcmL1h1vHz3KSGqzFvOc5cTgcuTI2q3O1oDZlfe4tzzaIMhfrBcLOTZXTWK5DzppxgnVGR5aLM+0eOJS2eMHXNhwlKOri0sYZrisZtjL1G3NYlgexE3xUOeSb3SZJiqONHbNLv3C1UM3Bloa9CCHa1luHICgczZZaP7d2XBsjXssgMoySrkrmYknp1U26nUnMvzkXQiCdItpqJ4Q/4z0daglRzoxdbtP5mlivT5fFYdSjcXElDgevp/nFQnQFzYKFHZ4M0tKJ68FnK0LZbXZuaUsrg5Z7JbMYBq5ZKRVthUxyuWGZfSq2R1261liBnGGCtVxVPfA4o5bizl60yXZDH/h8DvvB2jQwuohJxL4opteEuqZHzbCimS6UBklptKXkL6mjlh4pXY5uyNXT6o6Ed2O7PrJBW1i3Med8Op+Dbe/yFJ83m4JJzAPT18RF8RABZXEA7ADNfXPHZZVGSsPSnmNmNzcnMCBXHVY0KgeHZXoZNJj3mlheWcdQwCKX6ww/uB1dqo0OCz2lrdhJm7N4kteCsIXjMNUypGSZ1eKGOnXhm+xme70FVo+HdeeejvVcN27rZHUbTyWS2qSEwsl1teBtVFKH4BQhthzbe1khHR5sifTjbr2eY4ZDBxou8ibPbDar+IqqromTrEl6epG1fS0bojy661WZdo1CoWq67UKSgxVnr2bcGQml7jjgsbftb/xqwdXGWhAze03exOR6ZAtsgePbfINcwm0UUqGZH+DEczYqp+Kri8CQXb7umzKlUD7oYxh0onobn7nlTsARMueiThvERY4n+nrXZATTVOYwUxbVcFKv6XlDCFvuGNdxox3wYrEW9KWXVd1GREcP90MzawjjKs7sPV/iyoXkiYsQx+Z1ptIngyUW5Lh0wrmI1PtlYeueodGmtwHpUJ52QnnZNetap3XhmDOKfRORzreTtHTgtZEKGymuKS+AzVC+9jAmHPrKIsSLwTBm61DBqvOWuW5XVVFHRcOachDcBnKLOQiDzMttInY+zdhSmUmMyjuj5nlXR/YFvzmjVOmtfDpT65ua2hnSpJgz9im3nqsCHFt4pSUyKymREoWHMo5GR6sih5knq4V5jba1giI7dcFvMPqgAxjmbmtlRea8kMyxrLFP8CjuAu4oKOg1Wit+JR73q35RFivRO23x5Jp7JkZdDtz8fEiNPX0eJL1Yc8wYtTB/Xl8Rw3B3ZSxlxkZXxlC+GftNbxmhQlKrw7EknCV73oangbGoo7CirKU4R9K5sqZtXDTLDFNOXiiTLnIuacqVhdhVHTrEaK2yCXPI+vGMcqSBbvYz1Uz2/IzaLLWIbbers2yxG0RHtbm6tnU+TvljUkdNlZa7oCviq7zn93uHP/HE4Vzlonah95SF+NWWLSzevPjkvtcVijNIu0o3YbU+EgIFI7clrGUeC695chBkbykV7Uzm5m4239RWZPYhStZX1FlqNIWShnyem/P4aoSLkLZPEooksBr22zFrYqlz9gM+jAfcZ3azXVwWN464ECm37YZk2Qs4qwgbp71IBT9c170RaY6WZizC9B4aWifW0mP17EtCnm8T3kF5nmqkfGuTRcSqqitYwLZxezWYOtIQUx83m9izmGWx4K/I+cTXIXEwTEcEo4WnipnK+saBvRnXshZRzCpk/YZka2Vc23V5mO/G5YAaCqcme9cqK2douu2gjllu7Up/uzOw8Zrote/OrDJgDTukS7EfDHXU55tmvF1cTwQwgJoaY4iRPgdCEjGxcdVZiY6bybUs781xXka7/DpTcorpzzCaVsbsGOlopcWGYBXK7DAOlZJbEX0R7cSmqFiZm8rq7HHuij2UuL7gVkw7a2ldxMGmZVRwW2+W+3Gu8bC2x4ezyUm7g7DYedpxWCE8Zx5XijQyJ1Ja7x173lFcvy62YcRh7vWM3TQvgZ0Tg54tWmOuxSIy6CRiqjIZW7IheLVijoOwcre51NX+rkDi1ZKIXRL391uea26n7crSCQvVGMc5XU59iWvBXrt51KWyqHbLWEtiF1higjZU2Ta4oJyDVPDTXaLgG8Xb7VkvbOqmaaWlLMlqcDzjTerrM/d46rCbfe5p95gbt3Gg6Xh+i8aG9NDTMrEwjBgp1lP2uxKvjmyNkJuLT5cpv4n2BywPV5K6Ik+LI+gO5tmre5LObFmsGbCdkY/GLm6E8uCsiKCTOQO2I4zR8kG6NXR3uJ3nhybWfdCEdkSehHJ4K+Cyd/LFmCwMr5u5h5XHqC0tUbiBb2p0ExFUTctjFeIC12p6QTNnNHEwuN5QB363WFzh2UzogsOGsQD64uRsttEHf5t7nrfBUTREU8EjRStr9hWxzLncyEN7xR1M3ryNm1DDJH4b7LcuGNdW4621rdFYMlaH1W6/uqxnzLxIQFtUeSHIxmw5ok2dHXEnN92RZxqWHNuxsGVpiNaI428YCvWTfCvNBSthz0uaKbZ1V8HxZUvbdOUN3drcwYt5QM7gnRr7YEs43xbyfhjr9Q1gLdqfBfy8cy3sUqd+iCYjx/JgIySD3Lww1CmmODKWRiJbGTBWuW6uzcbTrcdnJ/nI8ukynYf6ibHrYUlxM5YguKaSkDzYq4fkuFgUSxPl0AMNwM7LCSxPyfa0MDTY8wg5Pkgt2MRWBLwoVdk1eoY5k1dvgNlt0Bpnm2D7jIou57V2U3pkt7UTn7Zni/M+5JZDuA/Gy9mN2uvpMATS2Vic6HBVdDju7taRuSutbtPQ/IY3T1F8TraWthjyMSE7Po7MK8w0nqpJaMDjC/vA6yS1Nk/hzFhiQnlKL+0otaIyr6X9cr+BQ4BBlQcmxkgRnHS/0fazA7aeN8cGE9YEXN/Crbh2ljcpxkKq4L2FV8cnWrcG74JQ4sktw9bvOCuQfJOaOaIqrY80cK84D9LbLZLayiF3Nu4s+ubMRP22cVdM7o4JfUpCh+PAYNMkLhoSQ0E4R5jN+nar+lLv3a68u9+EGKV4gVUf8lNG7PBtld2srMoWGwaRPH8IVyrpLxRufloRGrmkVmG+I86KBG9PBKIyliYT5kIkS4kbPF6lWGlbZ/D1ONPt7nyWFoXq9MyBbXFUXu5BHd+OQTnAtuMhuBTO2jk1kzGNgWlZXlSGvGXwEjcbysqk9jq7eYdRQoSVbTltvR93iF7r3lHfz3cImEbm0WIxZ4VgfivAOLChwcZKTvaBKO2ZsxqKnhjP7HbA8Zw4LQ1aO3AIRVsDXbC368ycIZgDkMxsdxUxaB69VDk9c2ZHiVc939p58y3oA80m01fW2R91xVftKybNV1KCIbTiduZOaRQrLjn4akkjhji2Nb8F50NpwzjuDylB0At5ae8UV44lurq5pJ+n2ZqPiLlUZ821qwOC9wmXYdpMqSKs0C5d1MHJsTXwIcPs7LKmXZLJuSBSsMDMZDcp8SudFiwhL1ZxRYg3rKmEzawljtt6mcIaw8Pd6dKrrOPsrlI6q7sGH82wsGY9akvmSlj3s+66xdVSKB3v2m7lrXq9BrPlvmzR8aZGoQ5qs11S4VahTpWDhP060XrFXUo4eljOiHh7MnzVJUuyqaULvG7GDV+s6SgKuF6nTgni0Ptixa40kWGYl08v08Hy83j471/0Tsd3/89OER8Hfm8vgu4Hw77tfbnL+vIvdPjl00vlxkCDx1lonbbh8yDxv52Efv7T+4KJfHi8HZ3eSPXN28F4Y4fTr+u8xLnX1k01fKuLtL0fvn56Adk8/SZB/e15yPxyVzsr7yfWdh05hV1NB5t3lZvi2/1l9tvi+zvEzPdiu/Gfl+HzNBisHoDHY7f+hlPkN78qJ9OeryCARdgr8oq+/PZ/ACgGQugrJQAA -->
