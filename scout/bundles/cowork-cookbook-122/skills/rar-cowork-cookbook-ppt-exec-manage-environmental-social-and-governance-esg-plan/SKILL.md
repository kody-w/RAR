---
name: "rar-cowork-cookbook-ppt-exec-manage-environmental-social-and-governance-esg-plan"
description: "Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "c0f15ed6368786168f195e8f0ae518311845b248f5a0a7cf3a7f3fcf3057eaae", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-environmental-social-and-governance-esg-plan:7b38769853dd7c74550d8fbd774fd8b1d0ece3213c217c486278b819d792de5b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` is
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

Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` and embedded as the fenced Python below (sha256 c0f15ed636878616…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` first:

```bash
python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py   # or on stdin
python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan',
    "version": '2.0.0',
    "display_name": 'Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-environmental-social-and-governance-esg-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '901e05fbed772744',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/manage-environmental-social-and-governance-esg-plan'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-manage-environmental-social-and-governance-esg-plan', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecManageEnvironmentalSocialAndGovernanceEsgPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageEnvironmentalSocialAndGovernanceEsgPlan'
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
    print(PptExecManageEnvironmentalSocialAndGovernanceEsgPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a5eiyJruX2FyPnT1mFVyFai99lpHUQRERBRQu3plcQkucpU79PR/n0Azs6qme885e09/OOaqTIGIN97r8z5B1G9PVl0FWfH0+ekArBRZW3EcBqBArNRFuKzNigj+ySIb/kOcLK2K0K6rrCifnp9cUDpFmFdhlsLpa5CCwqpACacioANOXYUN+FgAy+0RNWtBoWZhWiEucCIkS5HESi0fICBtwiJLE5BWVvyMlJkTjn/H5f2sAUVqpQ5APqwO65+RPIaiy8qq6vIZKpPkMagA0oZVgDiBVVTlfRqUE4Wp/zG/L5dmUKVPUFvQWeOE8unzL78+P4Xw+9Pn356c2CrhrSc1r1ZQ5+1dqdX3Oh3uGs1Td/2uzqr0VagKFAp/+3B23kMfjtc5KLysSOAtF3jI69WHEsTeM/If/xG1VuGXP3/+kiKvny9P449Wp0gVAKTKrLICLuJYuWWHcVj1n5B53Fp9iRSgqosUGgjtL6B1nx4zv0nKcuTv47MPj0U++aD68OUpy8eYwAB9efoZyQq4XlGP3z+NUvIPP3+Kx8B8+PmbnLK2r8CpRmFQ608vr9evYuHAb0ND777q36HURyrY4MvTd8aNn4feo51w5tOnK4zJh4fgvID+vLvzw8//SKwTwGSJw7L6f5L7y0NwADMO2vSq+M/Pdyf/ikxeDXqX+Y+XHfPsn7EEDn9b7hl5ddQ/kn33/38THYcpLJs3j/+puD+bMPk78ss/tO1/mvCMeF+eliCG9VlYdgw+I7+9HNQV98tP7rebP/36OxT9fxVzyOrCuUt4gRUdeqCsXl5++am83/7p119+qnOYa8BKXuoi/jOZf+bX+zo/ePB11Icf58L19TRKszZF3jMd+S3L/634/RNiWHHofrtffka+r5fxM0FGI94Wfbjgu5opoa7f+fHnp98hbqTQmtq5P4ZV/u//jmxDp8jKzKuQg5PVFQIDXIUJGJU/BmGJHF+L+uthI8ryp8T9isC7Y7lDiLDquELWhRXGCKyHMeKjBZmHfP0/zh18Pzqv4DvN8+plhNWXB3C+/ACcLw/cfIH49/INNl9A6d/T6esn5BhAlbIi9MPUihFtrqoIlAIBEipzT5uyTj42oz5Q1/CBRxonjlhU1jH4G/L1f6PAy32tT3k/Gv8lhdG0YIghVoMkzwqrCOMesUZ0s/sKfIRQDRGoyOLYtmCzGH/V+afRo2YA0lc/O+9tBiBx5kCjvBDC+zNMlTKLG4imo/fLKIxjxA0L6Nqs6O8NAkbo8yjs69evtlUGX9IHfBPIo52VUzjgXWHk48e8AF4c+kH1JQVOkCE//fb7T8h/Iv/TrLvwcQ0Vtpe7L2EJxIh02CkIrOd6dFqJjMkEweoe799+fwRp1A42UgS6MPRCcJ8MpX1LntGCR+TewgZtHlUExetKP/oNaQPoFySsoLcgMpTPX9JRRAaHFm1YgjcnPiY/XP+WB491xpiUrz6EcfKKLLmPveftGEwnK9xPiOgh756C5sK4jg0ZCbJybPo5SF2QOj2caVXfQgjbM1LCaiu9/hmpS2jqKPmrDUWPzkkgpFnVV2TLqbA7ZjH8NTrovjycnaXhGPjXRH7chkKKn2COLd5EfEIUAL2J5FZh5UFhleA+zrMeGQG74tt8KNxCUtAiIzsA98Qe6/Geedt/ka6s3pjQ9xxoOXKgLzWOYiTy/zVvGi2fr9faaj0/rpbISjlq50eajlxw9NqDPkKqgkCq86i5b/TlDeneesCXNA5haIv+b4+R3j0zH2MeuFoXMO20uXaXP2JEcZcbVjC/xoQpirEmrC/pW7OBJo+1Uo64CWEgGkEle19wfPqmaQBrfbz+RjyQR+qO1sOiQPLajkMH8QBw7/VTBWMQ3uIEkw2MlQrLyQl+sArGooKJBOWP8QmhO2FDurtOgVUGXfoomffh4UjnoBZu7UBtYRmCT4g5VgXM7BKxAeRk4xjohZ/uopAEQB9DFd89XAZW/lBm5OevClpjLLIEptL3EXh96L9mmfutfKFUy7Uq6MsWBgFWZ/eI7Luer7GCyiZjKd0n/RjuV1uR77vi38YShjp+6y5wSzESiu+cA3G/SB5ZB1t9VEKQSMBrAsFMuHOHT4/2/+AX77p8/sOm5MM/t2+5N3T9x8h9RoKqysvP0+mj6b713E+wVqYwR8IclGP//TiW58dHAX78oQA/PurvI1z947fy+wjb38c7mfx+zYcLPyP/nN4/iHhN+M8I9gn9hI6P5NABY0a/fqCbuI+L80dyfPol1cC3+L8myQicEMzt/r1/vQ2BTcwvgD8OfvSzcmyDLey8dxi996P3HHmtIAgjqT823zL7rrJHm8aIPwL6DvfwUTo2Enekmj4YN2fxqH4Jnj6ndRw/P6VWAv71TdkI9DC5oY/GHR4sNEjoqhDcr97J3Xjx4wb2XoIQO9zs81iJz3fYfEbeOfUz8rbLuW8n0xpu834Z+fy45GPl97Hvu2MbPMHdZtXnoz2PrdtII1/p/R+VGAsQauyAkTZk7xU9rvgHIfCL74Pij0J29y9W/AorEPlHjIcM4BUMSqinC0ndMwIjCosU1h1M6hpO+OMycJ0C3GrY/N3R3G/++2ZW9rDl97sbqsf+97enN3gZvz+YyCObxu3yX8EkR3e/MYCXcVFrFH3ne3fv37n1C7Q8HDv9d4/8kba8PBL36TPELfD8NPq4gKuGw/0FwdNDU2jiN1YOJUAE+liOzGUK6w5KgnwiH82DbdP9boHxdujex49fPv8Zlf+XoeQzbRMMPWMZinBd2qFJikJdxrNdmiY9l7ExFwUOIHCMcHCMdkhmhtOMzWCsS7O4CygbKjjGP7FeFZxiY+Sgae/h+Uu3Hk8P2bBj4dQMCndQD6OAOyNmDM3MsBnjYSwFGA+1AIUxBIYxJGXjJONRFmrRjkdYtEd48C9K0cCywCjvleA+FH5520y8xfKBNi8Qu5NwNAe3LIdxaIx0WdqaQd+gNuEADMdcmgAoxRIewwASzn+f+hrPMdwPn4xVALktZJbNuM5vr/kxZvaMhCMFshTnjw83ZQ2LNmlbC2y2mIHz5TQV7VC/9fbFLmQJYILp2OI8WYKh5DO9KFdKL60wxdGuu61Im1uFE2YLFT94tjM5zPNDKtjVvCkXPlk6uF0TcuRRFEkbC43POsBQXLPQ1NjEboUTKnJ7LjdoHx5ZKjntjPpW3VYVuGSimxrMZIdfjFav8GlERdcL3yxOdWxHR/ZQpoeSc8IaP0+nU/8I+stGP22vCrdvV9ZlZzHCYJ/YxdGv9P549m6ijhNLbdZeN9htnwcLudYuJd4r1kSpytKnsJt5w+O46kvDEHMhY5V06OldSuETNZ1yQzyZNI2PX27T0zySNj6FXmymszBXKnFDNoZNH1+CpAFcJoPMmi65MxEfz+SQXPRePiasZ3UJHerBPjhuN4J05HdyyuPOKb52p61YG7cW3Z6qWpTDWrrE+WKhirk7X3e4Tt7yc3uYrXtr1uK3Ct9p2Q5YM/rECq7RDvZOkU+iIRHHXndJ4nbgByU4hMshLmXlEk3xykNzg7tZJr0+w6Z52gEwX+o4KylNzLfZcMuzo3QKb06B9d3FQnHCPDjVwj6rONPP5MiszteLgle1qeB6cjNDfemgC8bxTJQvRXxpe8reMm4sRR01rdqX7rG5nNatphKTDC0baREfy/iwrkVyiAhP2C9vFKDAzmFwWHnpfhsrA8c6TF2DKSqV7o3icPt0RV1TQfdRse7ZU7dnAnNLh8P8OstQudQ3JkbdKky3SSAKqWEo6Ty+XGlFmtgL81IOSnwlbgnM2810MmR6yO1TfCVzXnUJnW1OqQsrvy7k4swEDDWhm/w2VMe1kZZskhj4eXLSuzLZrEOJM1B5d4MabrpNLFcg3t0izM0jvJvYmlxt0v1h0UfmiZUvNEpNcMxi+xNJSrMhmK6Xkzm/bvLNJdstsSnOheUkOREoOe3AMttDhsMSq6DXMDtOZpchyS/rIyrr3WZiVkaoXbbH2dC6BtasdqLVbU5xgq2s9dBBkm1Hh6TgkphZoIKwQZleZU6tSCXby96yF9gy7AtjumgW87kr6bFIHLRAmnS4JgLRlS/rYWUMfGUyt9vFTLV4J6wgumwjYn5TrzI1qHnJ59QmXAmSTmq9Tl+jm5N1YpYIh92h5rJg0WJsuWFDPZ2Ig9QDiZKvZmpL62ESkMq0pvi2afjNdDU5+TNuCPHuwNIe78ZBM1nlV9bVz3tl7/fFpTWq9Z5zzkclIm2IL6edz1uXJlCG6aLTu5Tuj7Wr+spK2561o36h8mEjSnKr1ee91rJMYSp7eaC99rbtUAZmkCdZYh1kTbMiL9SN1RvLOLKuhe4KNt9t+eJ8O7QS6QVKhEsSznOyS6IQ6a02n+8q3HdP89S3L0kAFGGYzcsNg6WbyukcOjIms8iD4FB758ZiZYyS5JzHqbSJ1tNNUyR5VmHV2TufJ1WTyLZ65JR8zi8njI7T2ZIDbZseZKxMapEqpHZbKWv+GvFGTMv5OWaDqoiCRqzPGLqt5hxHzaaFFvWz7dGZRnY0YCvavDZeGmitHWxni0SHbXOr0Xu5n24UP0V1c8hSc7pgI5VrqNjzZmKWSu2so1oVtIuYwnRdSvfDzQr2i/YsdXG/2bPUdu7a+1W47xk3UBJhvubEhpZ4y87MbHetrieClksx5v3VECvVBagC48KVThvRjAVDMfiqpLJgvw/Uo+FLl5nPHmcKk5skF5jLpbNTiIXIJdKKvRV8F80rsyiCnpf8Hb4wisOVU1xzrt7y22E2bHfnPbUX1/o65D0qM3iFtQB/hk2w62k/nyfVnjagvcaCHi74mV5e8CRAg8R1PdtgaHWIKS+VFpvyiCcQlMnpkSukrdq7m8pIjsxm4W+U5cDIzGTuKLjcFLvT+WRwATdtCj87XVv8KBoTADx1WjAoyrKZGvD6vtHcWqfP6JZLVrYYTg6CErFUtjcWN6ytL+5Z97dHSvXJU6BsA3IhZYrpNHsLhRgSbXdHPRhOTbgJD1W+jqpLNFnghsrZvLO/Lc9RZUjr6ywxg7XYKk4eD5ZIXA/FrjWSQRAPqa7oqCGh+TKq4/OyoaNV55qieww4M8jEjm6Xah2UOF5WqW7YZ7w6VDV2PaA57FbzTiizNZ94B1z2s67bMbRv2voFx2W+KxaRlRA6uu8sVyXrFakPl2YpYgA/m1OqafY7QrICZbe/eaVmHo6pNZ1PmIRekFpUaIw+7Q/XuRldeWx1sS+mRNI6rkTYCXpmsphejr673srLTAvYG+m3wqHVpUvExsuzkob8RfBZEs0q8tCtenFOxJ11Vna83BPS4qqda+omC1TNCfk8Z1twEycH3QecwsHiv5bbsOxBSYrExbZxJlnkgS2d+r3sTFwRrQ0NotdVh3olc3mRkXG1JwbZK3hjYRKLaCfvlAWa9J64yTzF5XJSPObmNi9Yvo48lU2siO9n3BSiwDGSg5I+VxOrn8oYT4nJ7WYGpTApLGqnAWnvzlSNW8mpe8P5s8uarODvIqraYOcLezizu5kTi6Ls31ps5ssHcrWuQcolC+YEdxzJrI0oMqhbu+PLuC3NiyRu5Xm0czehuZUW5GJ95JtErekUvc7slTKHek8JS8A7uYvSkyyyazkNt/uA5igD91Qz9FI9xnRM50/GBt6mqW4SFx7rBudD0Fg+3y2onCFa9LoTLGu6SporOiFMteAr5wa5an1hTTl0NzfW9hzLO1/WwrDi0gb0dacFix2/nzviuuoEnIjmMmlqZ49eOBcjXN+CRI3K6kThnl6SGLV0xTPKVc6e52ozpHNdPTvWPi7WvKA5pl6TQkCc9YOrwRZ41NNrErL8/uio3c20CkdT2yPrb8VjkxQTIxMYdIVSwnEHyn3cH13FC2QF0xfLNOFnhVScl0dUafastjyIFw+PiFBIhQN19Bwjl5WWY0IPVsOU8rtrTu02CtbZoY9uTthiaA4ifqb6AIjJxFejfoXV5257iKWtpPJptocMP9Zh1+EUNejXt1SSYVFDSjCrrhs34Rj1sN02reyl7CLIWUuf5n2p3+Y5xEdan0Uma5QFZFLG+pRNiDorUjDQLmdnBaplLhOwKMTxoi9tLPL5YX22N0rd5KVkLHh6uFplXEfxdCUlAYklqOvK+T6kV6FCSCl5SzwTkqSYJsHAzZWpCUTxjK+KVd4BbpUdyasjzf1jPTmHPtjclsYhqoreTHahre3cpdsGuiqnU2CpLKcPdbWSJ8oJZYUjtzqbm3Vi9qSOVktLn0PmhpLHdmEkDj9f5Nsot5btgaMDa3yfokWrmcFd8j2RK8ch3RSWk5SnibojwtM80xIFN2uS126p1a/mdOigkBzauBvh5nY3WR23YCiUCF0cAfQM7WOkqN3UKrKXqnaqlTYmtsGCILJ2E6217WatBmYRb29bu1zG61VPVZW7BGKXUsu1p66mcyta0jFRXdaYhNGNBbVPuDUQVOXAbgeOrgxjTaO8QzB7Silnl2KFXc85pMNC25Fep1i3heHK7W1GnXS0VS2G5RxKxOYrHqtQptBMbCZuV+u9G/jb9WJmcSrfz415LQ/xmQ+DpHcsYRNb9pFOnKM1Wd58/7Jn3ZXPsZMZuet7Ikbn+iBzgbsPPZnHyJ1w3Kx4W2wLdUkCSREsRoItbpVT2vwEe1psxDPFlggjdNk+DXPTFHP8NCl2pkARBQYZ4ASTjPNpANfN/NafDolXrU77+ORw8WnObzfhsrSJaoeFMcBM6kQJgjCTUaAeJpMUp3WWWC7NDQ1rmQDC8oTRk7hRMsiBuhMdD2Cp2XiXwS3gmtzkGxpAbM27WcKgkBuU5Wp/9C6pyPV7uDt0Ny6Gz5cUThsJrTimGBje6jijE37HHEG7Jc8HvDxi/tzVmiRLWryZodvF0vZ7UeRnG9KhN/FgEylkQppxXWKSgOWLZdKhLrNcT6NzU9EuXpxNYaj7qtmVXFkKaDZRSGl6cekdup5NBXE7BZ43zTR1tggXBtypTbxppzMNShMnVZtMm4g/5afychyOxLoMxa6OMiZVNQw99HCfsVzRET4IFBdQPD9v6WkcOEoGrXPrw6qjgslCEgRKIbNdRkspe9IYh+zr076giLJehC3hgnitwaDuOg7nr72wZ3Gq2Z1Z6tBZkG7WgaRdtJRd9vYMa9T4Nt/Vcs3Oc0qYqEFT1hm9FM/NEC4zvolZAuO9DbEFk0ERL7dSOR9d1RKKHYM7Sw4qbjAWN7PcVIZMYFqZJI3HuH6dFs3EcYAIdOM0W4F2uTpoKhjQGjJza1kSDe4k7Y1yiw5t+Wa1tvraTiy8aS7OaYJeMIYU5UbuNHoIaqqmKIKbeWepFufNsC0ulMBN4RWWr68KEWrKRWJF2QyxcEsUKmMAPxPBci5wlUqUpzIuwlPcl2nqG9zuugRMRl6F9mau96qFb1Xgn1aHyWCrJpDYjo2Ewd/ycJfMinCjrEFVsKEjmV2gCVuvnrPmwuDzDbGbmBD4fHTPB7Uve4tNTNukzM871Gwxrps0znETHwhRJzpmNglRcqg3dS8rindj047oNLtUGgUf0iynkss6RHXIn2tCFWr9tiX3p6Jk2oJlTNALM/x6kgqHnjEXlow2ojPV8O12Pd07yzPjLM771puARBxg29wORdZIVUhfT2lRAhLMnZz3cUM4aaor11cMs8ubO7NzugnwwgyCmwCuFyBkVujtcWa1PGvkfCPffBov9pB91J3oz/vSIxf9Sc4wW2Q8IeM7KSawozrzIA6wbh3AveEchYWJ1mt/wlT4FN+0dOdiKSu5YDJjliivZL7KEt10ZiyHUKE7XHBotpYKdqjmbD7jzbgNmQnNX+1mAElvZwY+1ejpgPfXTlfokyNV7oFlmPOx44lgnYiLojXWqUZcCoqerZzrJme79TVPCphZk6k4xdls7fvJwkqasGOnDeS5qD3jJxS/5KlJ2u0Jz0oY09aqGqCxeDKYfWblrFAtr6hIqtlWyCAmOui6FoSrLl64QsfReb2nIbD3bOV28qw09ltuVfmuMjHUaOK2C1h0HaNjrLU6URKRLKM5n/Q8IxwC+cgJSr+7MWGDVTct2a+dXR/ul0Jf2K21FyQbP1Vay/QD6ly6iJ0Bkt1Nls2JPHOnhU0c0oXH5aVaOkk8I8JuSezkSY9llOeW1MFxls66azhSOrk38WKD2yTeKvtGb05lyIAZnc6ZIY9bVZ3bhYRam4Gn9ueDnbmiyaU0qi5OhCaaB0tyqYItSk9bsEQqbJ2gZxv3iPUT4TydzLHjvvWnysafz5+en+6H20+fMZSl6Oen8dji9fDhr3pJ7Q9h/vK6CkEzs+env+5d6OO95Ntx5v04Alju5/vqn/8aA359fiqcECr7eOUNeZT/+mr0v70l/vi/eas9Su4f5/3jaW1XvZ0EVZZ/fyEfpm4NKVIP9Y7r++t4GLq6HP+fUPnyemDydHdGko+nL2/Gw69eVgDHKquXKnt7Ix2m4wEkcEOrAq+X/uuxxvOT28MMCJ3yhZhRL6DIRxe8HriNb5PHE7en3/8L+OGB6zgpAAA= -->
