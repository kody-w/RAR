---
name: "rar-cowork-cookbook-scheduled-brief-forecast-marketing-campaign-targets"
description: "Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets", "rar_sha256": "9aa6cc11e8af5a4a50e28fa6b8cca4bbec7266e46522e8e5641fcea7ac1cb0ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_forecast_marketing_campaign_targets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-forecast-marketing-campaign-targets:54faaac6b981c2c21bce22bde8ac6e1d8b2e5853fea58b235864b9f86b519675", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_forecast_marketing_campaign_targets_agent.py` is
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

Forecast marketing campaign targets Scheduled Email Brief — Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 9aa6cc11e8af5a4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_marketing_campaign_targets_agent.py` first:

```bash
python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py   # or on stdin
python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast marketing campaign targets Scheduled Email Brief — Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets',
    "version": '2.0.0',
    "display_name": 'Forecast marketing campaign targets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-marketing-campaign-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '99c0c0116db6c114',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/forecast-marketing-campaign-targets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-forecast-marketing-campaign-targets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefForecastMarketingCampaignTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastMarketingCampaignTargets'
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
    print(ScheduledBriefForecastMarketingCampaignTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjSJbuX+HGPGRVExmIHaKtza7QLhAIJCGkyrJIFmcR+y6oqf8+jqSIzJzqmtvLPFzSMoLF/eznO8fd47cns678tHh6fdoBM0EWZhQFPigQM3GQSdqmRQh/paEF/yN2mlRFYNVVWpRPz08OKO0iyKogTYbptg+cOjKtCCBxWiRB4n22igC4CIjNIELKOo7NIujhe8RNC2CbZYXANyGohle2GWdm4CVIZRYeqMphDFL5AClAmaVJGQx00zYBxV8RyBiOBA5SpUhRJ4gD6XcIHN8CEEbdC5QNXCG9CJRPr7/8+vwUwPun19+e7Mgsy2+yAkcYBJw/pNm8CzN5yLK/iwLJRWbiwXlZB22VwOcMFFC+GL5yoIKPp59KELnPyF/+ErZwYvnz65cEeVxfnoZ/GpR1UKlKITcovm1mphVEQdW9IOOoNbsSalvVRVIiJlJCUyfey33mN0pphvxt+PbTnckLFPCnL08pFMEcHPHl6efBEF+eoF3g/ctAJfvp55cobUHx08/f6JS1dQF2NRCDUr+8PZ4fZOHAb0MD98b1b5Dq3eUW+PL0nXLDdZd70BPOfHq5pEHy051wVqQNSMzEBj/9/GdkoTvsMArK6h+i+8udsA9MB+r0EPzn55uRf0XQh0IfNP+cbQbd+s9oAoe/s3tGHob6M9o3+/830lGQgPLD4n+X3N+bgP4N+eVPdfufJjwj7penKYiCBkYHzJ9X5Le33XY2+eWT8+3lp19/h6T/n2R2aV3YNwpvsZkELiirt7dfPpW3159+/eVTncFYA2b8VhfR36P59+x64/ODBR+jfvpxLuR/SMIEpj/yEenIb2n2f4rfXxDdjALn2/vyFfk+X4YLRQYl3pneTfBdzpRQ1u/s+PPT7xAxEqhNbd8+wyz/j/9ANoFdpGXqVsjOTutqAJ4qiMEg/N4PSmT/SOqvO3ElSS+x8xWBb4d0hxBh1lGFLIoBB2E+DB4fNEhd5Ov/tW8g+9l+gCxWvmPT2w09396x8u0DK9/esfLtgZVfX5C9DyVJi8ALEjNCtPF2i5geSKpBhlu0QPj93AxiQBGDOwxpk9UAQSVk9lfk67/A9+3G4iXrBlW/JNB3ZnCDZRBnaQHBHqKyOWCZ1VXgM4RkiDdFGkWWaYfI8KPOXgb7HX2QPKxqwxoErsCuK4BEqQ11cQMI489DGUijBmLnYOsyDKIIcQIoIaxF3a1YQX+8DsS+fv1qmaX/JbmDNYnci1SJwQEfAiOfP2cFcKPA86svCbD9FPn02++fkP9E/qdZN+IDjy0sI4/iBCVc7xQZgRapYzisRIbQgdB08+5vv999M0gHSxcCcy5wA3CbDKl9C5VBg7vD3r0FdR5EBMWD0492Q1of2gUJKmgtiAPl85dkIJHCoUUblODdiPfJd9O/u//OZ/BJ+bAh9JNbpPFt7C1KB2faaeG8ICsX+bAUVBf6tRo86qewejsgA4kDEruDM83qmwuTtEJKmFul2z0jdQlVHSh/tSDpwTgxBDCz+opsJltYC9PovY4Pg+DsNAkGxz/i9/4aEik+wRgT3km8IDKA1kQyszAzvzBLcBvnmveIgDXwfT4kbiIJaJGhCwCDj25Zf4u8+T/QiHw0C8js1sjcegbkS02McAr5/6jrGfQZLxbabDHez6bITN5rp3vwDX3bYIt7qwfbjQebARs+WpB3tHrH8S9JFECHFd1f7yPdW7zdx9yxsS6gMNpYu9EfMr+40Q0qGDVDGBTFEOnml+S9YDxDR0CflQP2weQO77q8Mxy+vkvqwwwenr81D8g9IIdEgaGOZLUVBTbiAuDcsqLyiyHnHl6BIQSG/INJYvs/aIVA6jA8IH0EChFAi0Pr3kwnw9y5eWlIhI/hwdCSQSmc2obSwuQCL8hxiHXogRKxAOyrhjHQCp9upJAYQBtDET8sXPpmdhdm6KUfApqDL9LYrMD3Hnh8hHE7VCbI7yMpIVXTMStoyxY6Aebc9e7ZDzkfvoLCxkOC3Cb96O6Hrsj3le2vQ2JCGb+VCtj+32L5m3EgmhdxeQMoWK7DEqZ+DD7i9F7/X+4l/N4jfMjy+ocFxE//3BrjVpQPP3ruFfGrKitfMexeON/r5oudxhiMkSAD5bcaes/Fz++Z9/kj8z6/Z97nR+b9wOpuuVfknxP3BxKPOH9F8JfRy2j4JAU2GAL5cUHrTD4Lp8/U8PVLooFvbn/ExoCCMMOt7qMYvQ+BFckrgDcMvhencqhpLSyjN0y8FZeP0HgkDoTcxBsqaZl+l9CDToOj7378wG74KRmqgjN0iR4YVlTRIH4Jnl6TOoqenxIzBv/KSmrAaxjN0DrDggxmFuzCqgDcnj46suHhx9XlLecgWDjp65B6sDbC7vkZ+WiEn5H3pclt9ZfUcG32y9CEDyzhUPjrY+zH0tUCT3BxWHXZoMl9vTX0fo+e/I9CDBkHJbbBUP3TjxQeOP6BCLzxPFD8kYhyuzGjB46UMP6GpqF6z/732H1GoC9hVsJEg/hZwwl/ZAP5FCCvYQ13BnW/2e+bWuldl99vZqjui9bfnt7xZLi/NxT3OBpo/xt94GDl9/o9TITWGSgO3drN6Lc++A0qHAx1+rtP3tB0vN0j9ekV4hN4fhpMWwSwue9vy/inu4BQs28dNKQAkeZzOfQdGEw0SAl2A9mgVQhR8jsGw+vAuY0fbl7/vO3+xyHjlaZc0zRtxuI53CZsArdsQBCWAzj4EuAOZxGA5mjSBSYN70maYyiLdznGonGeYWko18A2Nh9yYfjgJ6jRhzP+N1YHT3eSsA4RNANp8qbJ2DaOQyld2qRMegQIzjUZi7Ntk7IsYLMEwwCKoQkCcIBmKNy1gcmaNm5bI9sc6D2a0bucb++N/7vn7mDyBhE5DgYtCGgkzmZxyuFZyBuQI4u0AU7gDkuCEc2TLscBCs7/mPrw3uDcuymGUId9KOwCm4HPb49oGMKXoeDIJVWuxvdrgvG6iVGsdfWXqDFCr2eXVY1dpjlVugjmrVHrvZKflub02JEaGIv9em3vzvWlnu4Mfh7Sy/VkyQhbYucWMjuh1wd3FTnRxJPPPXXJOic5j1yS7PqDr83DDsR6Fo8uzmWNRileV91qr1B5vgeRudjxh9NIl1il6qpqQoN1viYPfpPn+DGtMAzbNdzMjH1txR5o57QNMbo4rtcEyng6xq9g/GOnibsKFmahiXh5PuTFzkRpUTf4nbIXVX9FyDPrYO2ijpE5qZO51NHJkuKSkMqqxoiuvI0tcyaurrzb6wHKB5ya55toQ+RxN7PWdZUbx56nqzRAR0UM8klSz0gC+tOab4r6XB6UHI8aAwsF2TadxNMmknYe8WZLb4z5BD818u4aVla+vjqbRRCXVKumNGFHu4LWq3MoihWTE0S2CzZyjCsj93SpqIXCujurTsj8cm70XSJdpE6L96lRlrDRlZnYt9nZMQ+5yAlxayUuElHWYl+qj2ltFTZDCKitjeZ9s7PAeKzlwI9cv6ztBc1sT/jCMiaoEla2hIJzI/Q5keu7HoXGk1GHEHXBiP1Ya7FJWMwu5ZxEzX1fzAmxq5LAjBtir62xC8wAM/BxNJG1cg7dRrErzs/ztUJbyj4UIqqxMUPRLLHvW3upBdJ654Nji02ZGSHik6trWz4vE1OTXu34nh/XRi3hS03c5slOX54orCPSvCLMsBZNPGNGvWCORI4WOFalrWDUCJpEEfS+WbjKss7OkxhttZOJxYp8us5EIOL7WjwSND+lK04+SfaRMHc5a0zazsgutGPMY8erQl9kDobjq7HJ5nS+XNARIfcHRe4NQp4aTrePanHay0S+WSb8fMVdBGw2xaax1Gf7SNqi0/7aKy6W11jScIbUqY0h8HXsiWrGhoCZ98fMkY2TpgkiTTharnKr9ZXrF7jGZBfHPUXjVcdo0mQ+CogI6AtCCwPZ9C3FY+c4ddiedrw0agNJJ47TwtjIjlbPZHVl7rNVqC86GDRu4ITiMthcZAWGmabvpTzLe0WtbWWd0zxj2KLVOW4dTWQVvTK1sreX3W62RsNgxO2obEuhs47f1/z50JRndH/ievZYTYpo22aUOwUTR611m+1ddklJo5M4lw69VXvXFV4ssPAaSzjTJeNsZoisIMMSflK2a2JtOplJSQCfaOOmZbHRdIrVeXpGF+FRXcYLaT/X5ZHvuVqSpztupUTHMrS2Pu/1PRGjGnudVYncJA5N8it9jss6zxDT7co6oFjmrDZ4AvDmGEZqvNfMUnVUzKqJ63rjHcSSLE7nfoYf0eyg1HUhHCeVfz7H/oyf9kyYrMkQYsQGd9RQc3lt2Vv8OTu5CmcdzusCn0v99pSuNF03ZLNlrbWIsgJ9PZjSrJFWjiPOFtNrlpC6jTrZZUs5+3KRp5ot2r1lHLXZVUoqnSLLHccWkXdiuUKlD+JyklzQPGb1YokltKA4ysh2IkUaHSf0YTQJ5vswIJzDYsK3086eL9s9IUpOuC22nhjt0YIFexnVdI6qwWbsC5SiroL5JFwzTN+eNlt2BnjRx7Hs0CylEdipY8HwzGy1lE0v1yXMC5e7ajKNcBDkKDrjgxnTU71ydI8lA5pTcA48tW1P58AqK68Jz4pn9gEj7I+50wXhsp0Rnk60iyqkKshePB61azfXrIMtKrnkmTPWE4EwTUzYSO1h07FGMz7dTSSPnbQnL9rNGmsToIeLGm7aKNR6NPQSv0xNXVHS1lCsfb+RdtSWKq6rCb2pGbGTmr7jm2WBcml28HLunJPLI2Y72VojZHfhiCWENnsibRl5Iq0EDDuN551DbcfLcLU6255hEOq29OztkmRARvPJ9IqhZABE46rh7aYtyP5oz8Jx20U5xO8rvfLqYjK74CAn+sobj6WU1ypmChb+qvZ0XeK0LlwseMI6yMLevnSelYprM1sXs22qaAKz9y4V4Qm4L6qE4OmTpa1dMLa9Npk6pqWRLZ+L/SmFPa54aHFzPLZ1doI1ZBBd90kQy5vd+Ti7XGa8lp0ziTdKkWEuTSbjmk6uz5fKCXx54fpaqUrK/IQSuOSlDAZGI7XrZass5N2s92t657RVN6UnvDPlKi7DS5mCeOsE+bkg5c1MbGfYzlnaRE1NeDFjPcwiD72djsR9dkTFhFeuXmZmXScn56OobWFdY/S8julpnWBCOA6lYzu3WUAUKZcy4lWTnZY+nO1qJ0PbmDrg1seFOc74MT+6mkAgZtVk35XHIkWDgiOFaTDnLqPTVhf27WGiNepMDxoPr0WcEr3iHFXJkRkp84W0I3a+7TU71JIrZyGN18UxHZ/HsAGONe6MnXy27A9zazfXcP4yNglJUYWOW5LRHgqwnYtxudFoiDxeP0MT6SShjsADtY77YkE2iUSco77frePkcKG2mKLHdsCZO7Y7qpPsUIEOnRY0NROi65zR6ZiZ6ZiWthWziZaNKDXzzWhzvhyWZKDOZgZ/wAWfPdJjSZNwn0DXxyk7MddCWYnhRSmCy2EiiFTLYFO0WYNo26m7sFVjoSkSdGEYosCSLYrDXkRMNqbX+lLnBiP3UiRKZpkQMmflPKjGGJb0167i5c3WCi2T8NhSU9kmJMNa9sQ1J9M1PbowumtkFbdl+bMtqPszvq1coxzFK8U79WrdKkfA0/bJS8fWOpyema05psmuiOStwGkTurPGm0BYb8PMdY2I3JXToy6r43Q1B9RmMRX3Rq+poNQ7XwLmXJtf+SOt1lNHUHnRzCZ8PHHTdSjW+mFGCqdRIQMG21PC1BYuO6drXDMac2G4V2V7FMxd0aw2/Ily8vWqDH2D9ohzezDy1dzxj2LIXLuDCtv/NQaLMYjyGKWMbmFFc0gDx/doe4kXVzuZLYj4rKVKPCK9WOY0f1Hb6fEksROet07peT0RKTw0im4meGf5oOmjsSb5ndIY5ynsLCJxIS2uc3e2xxchtbp22NgE7ui4TNhZhu2j2Tlcb/hEJ064WDDSsQ42h9GxD5SuxG2WdN3zfiu4+X66O2x9L1Fl92iYggTGxDJbU7OQ0Jk26KJLY+yJzsLySeen7NJU6tGIV092qpFcbgelhXXKpJRcgptzImWtEnXoMI24TUbniQo/7c9LfdurYzlad4fM4T3Tq/owGWP2ypkmEYuTS8M1pZV9WdLEeKk0odFNd70tdNWVlOtE09WI4XNDn2qnBaPrxKSnpgBW4pWQKyF9HHf50onEnHEvyS4AINiIabgB52yf4E0DTktyN7fNjF0Rc9+NDmZ+yMpSn66Xp8skGrWYc6nT/fSMapv4aMB1N7HSsSXo0R0+8/Z9c+lYolatBYjzzXwX7TtzVjvz1WKXLsyIy8jrbkQt1UlR9d1ehaucazIfrd09jo6pdIsVaZ8qV6saAY5IRXshB1vhOA9HpdGI1Z51Vb5v8GmudJp21HycEGgsWc8agYxPxnk0PvrDzqvWXqlRrruiFgiyBIsPrSSVFR3P6jia+p6yGIsnMc3asSFWCxE7C5v0zCVzv0uJaHRljYjwNCZdA2/seNL8jPqb5dkxCGosUgdfULNTzzqFMVnU5VrcyEzaFtu5fYzkpSaLC72fbIhiXSQ8oY8gLl/VOqWpeZNcMgasCo2SFDSxCkB4B+2wKEy07osA+inkxrORhR4O6Aa14VJjYwNH8X2HptFYSvadWzOogguXljM8GT+W3NZI+5qldsaF4RQjx5aix0FgsCWhxmaMFqJzuzgs8c51AJF3zprPlPEiIKzZ7OAtdVy6WClfgmvu1LJSE1lx9cKZodCL81rZUxc17TEHHaOzFoawBaMIUGghhLN9PU7HnDyCflR6KSZ32rVgmmYRmuaW3W0SuUhZ6ihjDu32mN4nlDFrha5p0FQrVwZNLH0+bOyabwmVT8gLitU8LOg7bLVQ53pUYAyGzcnRQkYZn9UTGvaIOe7haVImpSxv9pQjnOnjoSXDHVUsk00gU/11T3t9GV9mtIyJaXC0VXmqJNvViYodFRxY/2JKfaysz8M6VZLloiLX9HyxhnW5NtgaD/nteNxIZ5H2glShAekuxvaqV890xagb0KQX4rKvuA4YFOq5y4NBpwa35+cUSR4O88uiLlBGRaW+tOJAbaiIThj3mntn0j21Z4zek6R6Uvy4Gx1T1tGO4hauzWutBCDFcJwwC8xKentzXJ9HR4Ne7NupDtTtvBgoAtTGVlP5OieWB6vyJWUlspOmnorscVumBcU4TK1NJlKHdmBM7Rup3S4YgyREKxAkbpTjQAua6xGbM0s1ugZX+Roq/kU3+UA2ki0XY1NjHM7XhHZKWEa67sirZPJGDy+PPHvbpSJvaE7sVyfBApJPbcbUxOBOdN9fm3pjj1Gw9ouj0gQHlIoOPBa7LLWZJwmnX9kl420zIc/K5TQ+J5ZH+YoobXRlYq7IZSlJAnsuhTyZVCUmiReVtE+zq11jl4Dq6mLpXbDeaaf1ijzW11kBzjy5IcTpLFmY+LFl9uW25OhVKON+ozK0sERPtKXbVqZME7wDrFArgVr7Uz+xRvYEqzbTZlq6yrG02zmvWLOThPPzCCMP0Jjzk+MvC+sqe8ZUM53K3I4qYtIaGm8upSZumJjlJ9J0pkxBRyxS3l4GDsNv18t4fILNPKbKEyzlmj133aTTfOOyArMVywO5RrdNfFYvEYHrW8bcqHuTdaeSC2HYwbFlak6X3YjFFtKkjEoCm/c5mRi+2Z6DSMBq1F3uSnDQXIudJmjT8o7ry6RLVamxIHzSmbjiUq7ZmLnOturKuV5INnJGF1hfGGwVd1xUUM0q3ol1IEPOlpdbi7zpm568UnSsG8tgQCvDpfVuSVzcAEuPoRevd2ET8ChaR5rK7b15Tc/2EY4ZPnRPjPLHrt0SxlXfbWVwWCzy05VqKXmiTInpmJlEgrH2LKpsp9OaXOlKQHp6t3AvdWkM5yvny/JwOQTSaqlh1nbkgPQwTaYUJu6YInC5RGL3/XjRtgI5GVHHuj334CJeRIndWTubWPVZf9ipFIpb5nQ34nMQ8IVixEfQXxSlyZkGI0vP4Km1mrVHhyhag9DNPlmsI1CP+MO1F8ma76ZwSXYRYfcjt9aCk7zIqdNWrxiL2av4hDecM8wCzMrsSy/ExJjjBFDPU9wtJS1sR+SpVEt5a8Sw21RytQ45dXmxMN12TcHpL4ltXhqrwpZFJSlrjBPgSjqh55t8PB7/7en56XbA/PSKjziSfn4aThseZwb/5g6z1wfZ24M4ydKQ9v/e1uZ9m/H9zPF2hABM5/XG/fXfkvvX56fCDqCM923qMqq9xwbnf9vi/fwv7EQPBLv7wfpwgHqt3k9pKtO77Z0HiVOXVdG9lWlU33bOoX/qcvjzm/LtcaTxdFM9zqrHtvR3qg77+ik0SFa9VelD3afhj2SGs0HgBGYFHo/e4wDi+cnpoLsDu3wjGfoNFNlggceh2LAlPJyKPf3+X3Jn4Zp/KAAA -->
