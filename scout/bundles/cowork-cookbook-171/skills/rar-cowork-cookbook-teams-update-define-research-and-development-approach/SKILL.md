---
name: "rar-cowork-cookbook-teams-update-define-research-and-development-approach"
description: "Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_research_and_development_approach", "rar_sha256": "501188a747a77adfadc933cb1b2e30e043786866a0a43a1020e771a361991ec3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_research_and_development_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-research-and-development-approach:fefad8f4027a0730d10187c77d3f387764c4455da828551035537ab64a2a6844", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_research_and_development_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_research_and_development_approach_agent.py` is
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

Define research and development approach Teams Channel Update — Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_research_and_development_approach_agent.py` and embedded as the fenced Python below (sha256 501188a747a77adf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_research_and_development_approach_agent.py` first:

```bash
python3 teams_update_define_research_and_development_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_research_and_development_approach_agent.py   # or on stdin
python3 teams_update_define_research_and_development_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define research and development approach Teams Channel Update — Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_research_and_development_approach',
    "version": '2.0.0',
    "display_name": 'Define research and development approach Teams Channel Update',
    "description": 'Drafts a Teams channel post on define research and development approach status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-research-and-development-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94e153f3b2d0769b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/define-research-and-development-approach'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-define-research-and-development-approach', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineResearchAndDevelopmentApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineResearchAndDevelopmentApproach'
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
    print(TeamsUpdateDefineResearchAndDevelopmentApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOjSJLuv8Lm/tDdq6zkkjhybMweAl1IAsQlRNdYNkdwiFMcEtCv//cXSJlZ1ds9uzsza/aUVpkCIjzcP3f/3IOoX5+ctomK6un1SQNOjqycNI0jUCFO7iN8cSuqBP4pEhf+Q7wib6rYbZuiqp+en3xQe1VcNnGRw+lC5QRNjTiIDpysRrzIyXOQImVRN0iRIz4I4hwgFaiBU3nRXb4PriAtygzkDeKUZVU48EHdOE1bI7e4GQchcd6AyvGa+AoQznfK+xfeqXwkKCrk0sZegkClnBC8QJVA52RlCuqn15//9vwUw+9Pr78+ealTw1tPd82M0ncaINzVUd+14XJf+KYL964KlJc6eQgnlj3EKIfXJajgshm8Be1B3q9+rEEaPCP/8R/JzanC+qfXrzny/vn6NP6obY40EUCawqkb4COeUzpunMZN/4Jw6c3pa4hL01b5CF8NrcnDl8fMb5KKEvnr+OzHxyIvIWh+/PpUQBWc0QFfn35CIB5fn6p2/P4ySil//OklLW6g+vGnb3Lq1j0DrxmFQa1f3t6v38XCgd+GxsF91b9CqQ9Xu+Dr03fGjZ+H3qOdcObTy7mI8x8fgiGGV5A7uQd+/OnvifUi4CVpXDf/I7k/PwRHwPGhTe+K//R8B/lvyOTdoE+Zf3/ZErr1H7EEDv9Y7hl5B+rvyb7j/59EpzDU6k/E/1Tcn02Y/BX5+e/a9l9NeEaCr08CSGGqVI6bglfk1zdNWfA//+B/u/nD336Dov9bMVrRVt5dwlvm5HEA6ubt7ecf6vvtH/728w9tCWMNJtZbW6V/JvPPcL2v8zsE30f9+Pu5cH0jT/LiliOfkY78WpT/Vv32gphOGvvf7tevyPf5Mn4myGjEx6IPCL7LmRrq+h2OPz39Bikjh9a03v0xzPJ//3dkH3tVURdBg2he0TYIdHATZ2BUXo/iGtHfk/oXbbvZ7V4y/xcE3h3THVKE06YNsqqcGBJhVYweHy0oAuSX/+PdyfWL906uaDOS01t7Z6e3B1u+fbDlG2TLt+/Y8u2DLX95QfQI6lJUcRjnToqonKIgkAwho8YjCcN4qdvsy3VUBCoZP4hI5TcjCdVtCv6C/PJPrfx2X+Sl7Edzv+bQfw6c5yMNyMqicqo47RFn5DO3b8AXyMuQc6oiTV0HEvb4qy1fRgyPEcjfkfUg3YMOeG0DkLTwoDVBDLn8eSwaRQppvxnxrpM4TRE/riCYRdXfCwn0yeso7JdffnGdOvqaPwibRB4FqkbhgE+FkS9fygoEaRxGzdcceFGB/PDrbz8g/xf5r2bdhY9rKLCW3EGEQZ8ioiZLCMzgdgSnRsbwgfR09/Cvvz28M2qXw4oK8y4OYnCfDKV9C5fRgofLPvwFbR5VBNX7Sr/HDblFEBckbiBakAvq56/5KKKAQ6tbXIMPEB+TH9B/BMBjndEn9TuG0E9BVWT3sfdIHZ3pFZX/gmwC5BMpaC70673AR2NJ90EJch/kXg9nOs03F+ZFg9Qwv+qgf0baGpo6Sv7FhaJHcDJIYk7zC7LnFVgPixT+GgG6Lw9nF3k8Ov49gh+3oZDqBxhj8w8RL4gEI7JCSqdyyqhyanAfFziPiIB18GM+FO4gObghYysARh/dM/8eecL/tCN5NDT8e0Pz6B+Qry2B4VPk/3/XM5rCrVbqYsXpCwFZSLp6esTd2K7dF7l3eLDbuE++J9G3DuSDrD5o/GuextBXVf+Xx8jgHmqPMQ9qbCsYRyqn3uWPSV/d5cYNDJgxAqpqDHLna/5RL54hPNBd9Uh9MK+TkSWKzwXHpx+aRjB5x+tvvQPyiMUROBjlSNm6aewhAQD+PSGaqBrT7d0ZMHrAmHowPyCk31uFQOkwMqD80Ssx9BisKXfoJJg2sN965MDn8HjsyKAWfutBbWFegRfkOIY5DNUacaH/buMYiMIPd1FIBiDGUMVPhOvIKR/KjC30u4LO6IsiG+PnOw+8P4QhOxYmuN5nPkKpDow2iOUNOgGmW/fw7Kee776CymZjbtwn/d7d77Yi3xe2v4w5CXX8Vidg1z/2BN+BA4m8ggE9Biys1kkNsz4D7wEEI+Fe/l8eFfzRInzq8vqHfcOP/9jW4l6Tjd977hWJmqasX1H0UTc/yuaLV2QojJG4BPWjhH55FLIvj9T78pF6X+CqX75LvS8fqfe7xR7YvSL/mMK/E/Ee6a8I/oK9YOOjXeyBMZTfPxAf/sv89GU6Pv2aq+Cb49+jY6RASMtu/1mJPobAchRWIBwHPypTPRa0G6yhd0K8V5bP4HhPnZGTwrGM1sV3KT3aNLr64clP4oaP8rEk+GOb+NhTpaP6NXh6zds0fX7KnQz8U3upka1hQEN4xj0ZvA37sCYG96vPnmy8+P2+8p52kC/84nXMPlgZYf/8jHy2ws/Ix+bkvgHMW7g7+3lsw8cl4VD453Ps56bVBU9wf9j05WjKY8c1dn/vXfkflRiTDmrsgbH2F59ZPK74ByHwSxiC6o9C5PsXJ32nEkj5Yz2FZfydAGqopw9bsmcE4gcTE+YapNAWTvjjMnCdCsA6ALl4NPcbft/MKh62/HaHoXlsW399+qCU8fujnXgEEpzwr/WBI84f9fttXM0ZZd67tTvs9174DZocj3X6u0fh2HS8PYL16RWSFHh+GsGF5S2Nh/te/umhIrTtWxcNJUC6+VKPfQcKcw1Kgt1AOdqVQKr8boHxduzfx49fXv+89f5HeeM1gCb5TDDFCNrBaBLzcQxnaI+mfTIgGZqmpt50Opv5DkMwsxmOkbMZSTsuNXUIh2KmU6jZ6PHMedcMxUdfQZs+HfK/s0d4egiFBYmYUVDqDMNxhnHoKe3QtONDIzyWJD0XdwlAYgCbkjRDMRTlYM6UdHCMwABN4w5J4SyLA48c5b03pA9N3z6a/w/vPTjlDVJzFo92EI7jMR6NT32WdigPruKSHsAJ3KdJgM1YMmAYMIXzP6e+e3B08AOMMeDL0dTqOq7z63tEjEFMTeHI9bTecI8Pj7Km4x5RV412kyqddB1JHUijNJLqVF7Sm+yrWL6k5iLXA7ZIwiVZip5mNrq1sXdEs7Dn1+I8Ca+0NqFsAhx3270pHqObLPi7lZj5+YwkwEpLNmGzODe+Nltcjr1WuuKxDpmlk1GmmJRSfLlGfL/FkpgBWyvpikpvvG5ITwmkX/WoXYcJRaCxoWVWqlqa0WugOPPEIj6t69uEuS2d/nIhplhkqLyNW5dSFUttYsqLNL3pE68/b0wNl7cSbcq7RDWdKtWmxwhjWl2c+Jme4H5+ZnSbwYNcmVoxbl7EbsOtLXNpObhygXvW9YU+rtLd9lB7dLGyqOqwvFlNfIlu2ln3tHxHH6R1K2m2k0Scwfum5ZRGLk68PVmLEM/sQjUHZUtyLd/j4TldrWZ5Vbo7c751ZubWMvcLO0vC1quSjl67eDNbdruWcoOTPd+lXs1s3H06jyvB4fdMNZH2IrEtzXm5M3JGEuKE3ujgVpvZdtRzG1wpfs21DaO51+062lqyeSN0RQj0nUmIcCF8LSzwXRRcdblYeQ5+vBhKP01Lo6DYfrtaUvQmuhQKYa9OFykkSN1YNU5rg0WyB8Yy7l0RzWxh6m8HucLtrRoqA77P54tE8qOtKhq+Va8v4FIFckLhDHlODl6o6DId1G3jV7GkyJbO04E+jwmVq2pBpBWmSYS9Tyyj1UZKDlf1CDLmVld45pyD3cAx1Kld3ApsY9L9mcJCj1xejpKpn/pZjPJAtuLLgu4krzgu0Nk5TDYnYMmFbWt5vc/PaD3JihZPTZNQ0jq9CvNOZHYLWrY3mogVoK+LrHfxsl8bMz/BoH1lFWFE0vaOLSWo23oEcOMpA8MSnauK6pO34Rqt3WGmx2BbNC4aHnG5ZNGJpGD8DgvySy6Twi2SgibeAr6pjfYS15W8EsVtZTrpUZ33HU50J3e+9sAG3/Xa8SzFKhOngn/UEjp0WCozrpdkA3xusp4qAjDrdWyadEip5qK8nDaL7eZ43q7KXiqqxYFcsJvY4DPqprr7pTfnrb28Mju74abZ7ky2/q24znF0OrvhrjukyvwwEzBLPuDrc3GIeVXHFPVErLuSqpoe665JcHRtKicixyYXrlRZk0tQ+fvUkrkrKqAWu3BvZr9PkluwpCxpYlza3YJC1xf5iG9iyz2qklnKYDpNTh19XG4ae5UIwfyKHvYKQW3jnL60U3YyR9nF0jSN1UkVgbM6xWvLuSxVenMt2ehwJiRKdSeLJJeuFYOWQN0W1+4WtsdwPUv7mCjx81Xnr1SWpoeswIrKjCb2lUoHZZVstPAo3A5HtY9Z8YZZVZ9sI7c9iVnEsQJNRReRXGJttSjNXajpjLpji8liWqKT/mSUammbCuZSJwnbFrWGtRihiexNGEI/MXtAHBwmWWO07iqwME1JfRtsSvnAVzDZ1vvJFE9zSIXWxVYtKpIlLwq4ljOxsFEMbsAnZmOXGN11bLmU8ouIJWsZ1SU7GWKREdL10V6ARdO5EXrZLRV7B1EAwcTYGJNeWbPhtS+rXLgN6XTeNnV1WPSGYRPkUJRSpKO3PD8XpU4ndaey62TJ6VA/fHveO2F/nFHdLp4WB5UC+bRpgzlPR92C3ffNGqflrEo2yxN3O532i07KMzKPF62xvikmdyK3gr0rlUlIC24ZSpXYzw7i1mjCOC2bsNGwwtms+HBIJD1cANiUq76+x0ORKZtCy3MeLC69EhrxbsMMqi5dNB6Tw+15OqPXKTHXVGIQJyvIGFZFyh3WsfIgC0p3Xmt+EAQYvJz1gxTzbpdVG6clBnSVHls/WDV9zeZnjxc0TU7tQ4dOTum6cPOLTGrYeckvg4Bat8E1nzFXyO55lV/QJuiG2QHdrsLK6xgmI5eb0+IyPzdam8hON2yHuLiUVjzDjcwrwqvC9mUjNjKWTXlxI6mBwp2qzk4layZpG1GedNsZn2X12dme8WVqz7TUstlwWfKQo3VCX+GLJYqWs6M9uV5QSlqq5ZDupXNrBLg8WIvdMViZ+XrWpzx5IlQzMJoN2hX7fi/PxMuR5Aj/QDQ6wHmzvXbW/HZgD5OjgPLEfsez2DJdmXADIqJ8SUBC3J+Szp3HgwfJbIW1jh0HKxkTOLncE+c8ZRX7tJ9Kqcgsp4vQFLHrpnQ3fTptO/YqtpvjsiwXQSmzZ8aDLHJqa3HwEm+P6wt8cznlqE5GBqdfqnDlEWzDGWaShfppbjNmbDVlkfHLgvTovjTdLNXO0vx6LB0n7c4pp04GJ3OOgkkOqolWVMjbXkHaZ3Wlq8lCvZ62U/4c4lOeml7yjS1iA837E22eCUEaFML8PLXNY04UkR1SUjbNjrwc2XuUG0qbhbzl5QVfpIvudgSL214MW90X5reqt8Muja1MPBWLapDn7U3vCSI9r7KtVa0J0p2QS1kmbDHdDhWn1yRTXVRev/nC3jl7c2zIwGx1vXYF50NGnxrlZVg0qF5EIrXHl/XWVxZ7jyCyvZJMpMtZtImjODl5M9nwsfnEbg7GXov5sxYuZ6q/Uk2YDwLHc5l72E/p7FwKs9VC3SzmsI2yAzYlzkXgN0LttIAvhW1xsqSp1BfKDJ/lBp4cVcx25oqinxWMBZOjsVxSMraLrNPaPmuoHu+mUmxjMWAP+gCmbUgue9fXL2xG761Nb6oUMZlJVLjV5Wyz4GR21rDGwdzDxgWmNR4mzGTZpmsOJSIsksJsX0TtogDXPKZFNauGlbmWDKM+OsJNiL3DVquao7/R8PhshMfygu+XHd1KAr69LGkc19tJY20vezMEpjaYbb9h5geCu0Uy61hZFSqQ/FKNMedg67SLyQn2FOqmjub5LKHswynvN0sphAURPdDaxreYhLzs8rU20w/1OkmzGTfRFdE5ot7Gjrxo12lptcJroV0dSHF72+CpLhuDsDjwElsfYkrfLLvL4VomhX6N0KAJjBMLaw+BlXPapk+H02zahVmZuCmdzSvJ0MqUmVMJuyG1xMWIdhsf2KltXB2+k1zTnPYi1Vit13v68VDVlsO4M9mRk1WUJdl6zZ1LS8lMAK6OsHHPxClbY2k8y+P5zuftduc6coAvRRWU3dWyPMcJjiqXB7OdEdctO6vLo20RxygQPfOk36yYjo0i52JMKg5yEqoi6W/og+KnG8zo/K7SunlPkBvCW1xC1mNoaiimjV2RIrbWQm6oqD0aUVSRt24tJ0beZFucMsFli4Vb+8IWh5yaT8Qu20oJl60PYHrwTpVBcqtGDw3a2Ofpok56STbkBu/7G2BUv0rkuUYW+llksU0qEUS9FStccJRLnPqZXARzkVD3mabjZT3dONe1P0y05aKuGk6L5sRkSJYnHAP+OSkPTNbuco2fp9s5UYZ7h7GdmmM4U25BcBQ6Mlop14PIHmJu3ilzL57oGar5LV1nuGiHah5Nd+7+suTZmeAfADvHlatnLNxDpt32m7bzFezEVVP2aGdmdRjMnUaxWq2sCqE0SXHFdY3XiOvMOyatKVGGaJ1Oy9XNW/HX3uMcpnKjuL6Fxp7QzwPH9Unl0hPNvLTC5bzEOD4THTMnLmHbz0iB4Y0wLpfD0kAJ+sJPo311q7XzPmT8iIK7jTQsZu1OU7ZyRgtFsZsOnlsnDcSIBcIgYpjn+8LQ9VA7io4n54M9x3ZzPLdIjU10i3ZyXtq23MGs9+CUkvUqJ7NcQw8nBjUauqOWhA8bsXwYPPoWOG0P6Oqmbq9X0meuQdPv9X5WU4m7lnt2NaPPk0sGs8nOK3Y7KTF7t8VoYaPO92ychhxQ9Zlvb3Eci9Z0M6tcwtkUym633WSSJW+ZMJufrj26A4yOqSopwC0dPmsV5+ZJu5y/hYcGxzuX6HYZroNuoM7Ven3xUCJJZGutDre9PbnYQT+9wI2CxNtXe09ahnDcCAwl5AFP1hZwKw6ch36FogRpoQur4AdBAw2KGleG1o4zli7Xs8i3si1b79gE1jUqXGfbhRwWzE5zvIPsLc/DZb5izlORuTmaPueYmddfqPRwW6Xrc55smFi+KbxLzutlpynT+lzMyHObpfKQB96w2nommdEtXjBrPgcXwtTl5aGcAevKex5OhNqww6KT7c5JdlVUXTq/dlODYUxpP8gJeotXbE8Js2husbUhceVEIYPDkmlb28cTp8IqWPO804RjbRInw77kpOVVjtrTuZ4aijrJzoEH/TtkV/yKHhWjl435kVTPBGfXvEjvlVTyhB7LHeWandILTtGWEMU7jNu58VkeWNcimWwXXDZU653WuTS5lNM+IllrRQYbu+LC6maQPrWOh4U92eH7SIhX0aVLJvFg1my8h1WSUQPJ5ZLVnIhPOT0VO92IdjVr6cNAcGRggMXJVYepseIm52aT0crpGPEWM4FNW7fLLYKfgHlUGXsr4mLGuQE0HYLWUq5WFK/oMLhw9DLbSH2Q0Qkbyxy3x2vOPuy2V12Z34rFPiZWRa0MbLS6UETHR0CprJuR8sfbdbIuOBfk7QT02HF6rjo/mVFbcCpC5hivZ3ozH3Da2Ub7BdzXynsRRavdSWADtUqI1mcoacLwy21Nq7OTwAWUxvmMJ5xumD+R15ydz28ru4PN9TrceYBhzZg0TvPbDQgnQ/fl5uZTCxTmmIiXbUYGVXScCYpJHPFetlpmAa7X/iCG5FwLpyXF+tgiqHPP2XB7iOkcnBlKPvbBuqMEQqwz6BhUncVGcKQLu+o4iW/RNhQ2FWTOK9vUW0bxXbSVq6PHYJBnDqHSDAPqSEJ/UChs46G0vDAJmbaAdT4fin3DWQGpnWg3OJPh4ni2aGYVoHAXKss6qfjDyp6kO3GxW/VCe9mewpUimEc/qAd0dtRCfIVbw9Jp5dMx5EzGmmaosLgJt+0hZC2ywzCUXMWbrCFOlZeFS1CKfu+QuF0tGPsqUwnnTKLCKNl8yQnYnlY23LyY7heno9PygkLudwfBwAjU9eYp/EMTxtVSjkNWm6HELVqBWtNyYE+pqMKoYN0fLL/WyTq47tcidwScPAVLniA42cLsw+ygpHbKDaGwXwN7Oxdoq4GVfi27mN6ogzFTnX0NveYHV6W6CmRKbYod3LjL7vnqM8S68bKUIuPOmpyODd4eJoFfzw6ZHNVGd2Xisq0O6paaSYzraaFcBvtGKlkWNpPDMSdvU2bexpsQM/PdLeyw6nAqPFEmSZ6/YpGYG0D1uxIlgVKcaG/aESt9KpNLAScu6xM64SfJfrk3k23IcU/PT/cD56dXHGNmxPPTeADxfozwL79zDoe4fHsXT9LU7Pnpf+9F5+Ol48dR5P1YATj+6331139R8789P1VeDLV8vLqu0zZ8f+H5n176fvmn3k6PIvvHcft4tto1H8c3jRPe36jHud/WTdW/1UXa3t+nQy+19fgfc+q396OOp7v5WTmem3xv7viqv4CIlM1bU7xlTpWAccj90DoDfvwYMl6G76cSz09+Dz0ee/UbSc3eQFWOALwflY1viMezsqff/h+0iwTwjigAAA== -->
