---
name: "rar-cowork-cookbook-adaptive-card-define-business-intelligence-reporting-and-analytics-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "142fe7a4c98b67372439413ae616da74666923217cd9934c1403b3fc40dc7cdd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and in the RCI capsule.

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

Define business intelligence, reporting, and analytics strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and embedded as the fenced Python below (sha256 142fe7a4c98b6737…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` first:

```bash
python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py   # or on stdin
python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business intelligence, reporting, and analytics strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy',
    "version": '2.0.1',
    "display_name": 'Define business intelligence, reporting, and analytics strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd552dae8cdc9ebe9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-business-intelligence-reporting-and-analytics-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy'
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
    print(AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abOjSLLlX9Hc96GqnjKvEDvZVmaDAAmxSUIgBJVlt9j3RSwCVFP/fQJJ92bWq+430zbdH0ZpmRIQ4e7hyzkeQf7+YndtVNYvX16Ovl3MNnaWxZFfz+zCmzFlX9Yp+CpTB/yduWXR1rHTtWXdvHx68fzGreOqjcsCTN/Xpde5fjOzZ7XfNbaT+TPas8Hjqz9j7NqbCcedMmsKu2qisp2Vwczzg7jwZ07XgK+mmcVF6wP1oV+4/icgpSrrNi7CT3dj7MLOxjZ2m1nT1nbrhyP4YbddMwvKeubnju95YDAQMvPsJnJKoLL5BB7YcQa+wRjNt/PmFRjuD3ZeZX7z8uWXXz+9xOD3y5ffX9zMbsCtl3ejJ5vZu4Wrp4Hb7+xT362jC49+N+34tAzoyOwiBMKqEXi3ANeVXwM7c3ALrHr2vPqx8bPg0+w//zPt7TpsfvrytZg9P19fpj9qV8zayJ+1pd20vjdz7cp24ixux9cZnfX22AA3tV1dTG4HfgH2vD5mfpNUVrOfp2c/PpS8hn7749eXEphgT6H7+vLT5JyvL3U3/X6dpFQ//vSalb1f//jTNzlN5yS+207CgNWvb8/rp1gw8NvQOLhr/RlIfSSJ4399+W5x0+dh97ROMPPlNSnj4seH4Kour35hAyf/+NM/EutGvptmcdP+X8n95SE48m0PrOlp+E+f7k7+dTZ/LuhD5j9WW4Gw/jMrAcPf1X2aPR31j2Tf/f9fRGdT3n14/O+K+3sT5j/PfvmHa/vvJnyaBV9fWD8D6V9PFfxl9vvbcc8xv/zgfbv5w69/ANH/RzHHsqvdu4S33C7iwG/at7dffmjut3/49ZcfugrkGqjJt67O/p7Mv+fXu54/efA56sc/zwX69SItyr6YfWT67Pey+h/1H6+zk53F3rf7zZfZ9/UyfeazaRHvSh8u+K5mGmDrd3786eUPACMFWE3n3h+DKv+P/5jJsVuXTRm0s6Nbdu0MBLiNc38yXotiAHfNvbZrH/i1iSe8fIwD+T9FeLIYgORv/9O9w/Bn9wnDC/sJUG8uQKi3B4i+vYPo2/cg+vaBoW8AQt8+IPTtHUJ/e51pwISyjsMYPJyp9H7/tbDB5HYyr6r9xq+vAHicsfU/A8j6PP2YMPa3f6EVb3eFr9X42x3p4wfmqcx2wrumy/zXyWdG5BdPD7mAqfzBdztgS1a6wPAgBng+cUZTZoBv2sm/TRpn2cyLa+DMsh7vskEMvkzCfvvtNwewxNfiAdDI7EFlzQIM+DBn9vkz8EAAlhG1XwvfjcrZD7//8cPsf83+u1l34ZOOPeCTZ4SBhXf2AxXb5WDYxHUA0G3vHuHf/3jGAYgpAPeCfIiD2H9MBhmf+t57UI48/RnG8Jnjg2CAQORPz87i9nW2DWYf9j7pc+KFqGxawLWVX3ggHCOQaoPlfHiyAGTcgLRugvHTrGv8u9bfnNq+m5gD6LDb32YyswcsVGbgn8nM+yAwuSxi4P6PlHncB0LqH5rZ6l3E60yZcnxW2bVdRbX91BHYj7gA9nmfDoTbs8LvvxYTK/uTq+4F93APGAQ84z5D+nmKOehJcoAuXvOu+z7GnrhSu3Nm/bVonsVk11MoXEAuQGnYxd5EMX97phToSbrMu/sPWDpJekbBe0blnoPs/2PHcnx0LH/ui752MLREZ/+/NFCTH+jNRuU2tMaxM07RVPMRn6k/nOL4aClBk3KXfK/Fb43LO+y9o//XIotBstXj3x4j71F9jnkgaleDIKi0epcPUgrEZ5J7z/gpg+t6qhX7a/FOM2C9szumgqADeADlM2Xtu8Lp6bulEVjodP2t5bhnSD15a6q5WdU5Gci4wPc9x3ZTYFU9Ve0zZCD9/SkOfRS70Z9WNQPSQZYB+TNgRAzqEFDR3XVKCZYJ3BzUZf5teDw1ctUjA7wZaMD915kBCm9KvgZUO+jGpjHACz/cRc1yH/gYmPjh4Sayq4cxU8/+NNCeYlHmINrfR+D58Fup3G2ZzAdSAa63wJf9hPKePzwi+2HnM1bA2Hwq7vukP4f7udbZ93z4t6/F3cYPYgGYkd0T/JtzZqBW8+aeqRPkNQC2cv+ZQCAT7l3D64P4H53Fhy1f/rJR+fGf28vcqVz/c+S+zKK2rZovi8WDft/Z9xUAzgLkSFz5zQcTf5448POjGj+/V+Pn76vx80cxfgbWfP6oxc/vtfgnEx4e/TL755bxJxHP/P8yW75Cr9D0SIrdyZL3pgV4jfm8Mj+j09Ovhep/S4dnzkzIno2A+j9o7n0I4Lqw9sNp8IP2mokte0DQd5wHAftafKTMs6AAjRThxNFN+V2h3/keJMAjvh90BB4VLdDtTT1n6E+btmwyv/FfvhRdln16Kezc/5dt1iZiAqkPXDZtBEEZgkavjf371UfTN138ect7L1CALF75ZarTT7OpQf80++i1P83edz/3XWfRge3fL1OfP6kEQ8HXx9iP/bTjv4BNaTtW0/IeW7qpvXy2/X81YipPYLE74f9En896nzT+RQj4EYZ+/Vchu/sPO3uCDuCFqXWI23eoaICdHmjEAB1cpxIGVQnAtgMT/qoG6Kn9Swc42puW+81/35ZVPtbyx90N7WNf/PvLO/g8Y/DsgcFwUOWfm4mlFyCZgUJw/Ug78Ozf2R0/VQFkBS0X0LVE4cAnbNSlSAcnEAJGEQpdIraPL3HPJlAcxykYgZeE61EUgrpLFEIcJHBRyHPBPQ/Ie+T529S1xJP5PhT4CLWEXQ/BYQxDqSUB25Rno4RtexBJEhAReIB8vk1NASw/ffLwweTwj0Z98t3TNb+/ODgKRvJos6UfH2ZBnWwckZwhOs9veGCWCVkKR7XsUMSB1nrRxCOBN8ediojOeAxdi+aa0VzS0rZfC5Js3/xDRJYqlhZYIRGxmhXKEDTHRF2pMDUfsWJOutswZiBtN2RSFro2MhzhJiehKs1Po7BfcdqprJjMOsunYb8hB21BGoMz6ofb2TJI7tK0HR6hJ6OFi70Yp63PFAE9WtqCIhmFONsXSCvVnF+rl5uvyCzvUPO5WJ+gW3FVVvVJ2yytXXbFuJNzruyLtdlq8U1bW9EqEr2gNnZrce9yTDZkc5MknV5zcX4L785Ej+6R5bDYOdBGaynKd8gcYyjj0BmiMvon9HZeni6npi1BgZ1su3L6sHHHEg7QCynlXUhrWzYQrfVtdK9XzskGkdnBsMntvBOvV3phzYMNsXXRyNrU4si0mbVyhUzUM8DsyB47SSUD7tvL9eVyFo2LfxCr8Xo6c35dNOQyEo+LeCl4MTawlrcyy7Q+ntiaIW/1zpJF43A5DBpO0NwYmfpcF40ymDuUORpBkJr2ynXKFKb73dhf5g7PVER1pINMapql7Xgsl0XC5opk4nIt6hJMWdW5FofbzRDVi3q16QXPRxHrMLsQ5jVDXBqtb3CY7hsnE8XVRWuuqW55KdbneL2VuiILi3jTqegYN/Ou5A1yeSQbzGrm/H5DW0oftqNdGZQvjOudgSgrIqiFcc9uTriamQuokSnCtUv1VLZDiWK2dRNJyMA7xd2jzIh3uEYfoaGN13Mv7OXcLcYywstWPSX7hdmb53B37lbiqEHWGO5ajF0dh4yVbH2+kpEFtYGW1ry7iFeVVNKr3LtHjxl2y9zlEovhoURq6UKWEuiSKx2e7zs4RYiLpcAcsrpJR6G7gHsxyp+q7EY1HYevhf6aYAVLyjx62DUBk2pmucMCijXHQKsUarcwizUkZWXhbtB41CpnHcuWIOqNmCA3YxTnRnWKVatJTKjx1lmH7gVrENXssmRjkcGG9BbsTgdJOlyi/V6gCQuxyhNRscVxTdpHJF9flruyPd1WCL0Z8TEWA0blOa0F/Zh83LassIlR87bODuRFNDeFladsbMJ7w3V61RiWlMlBOMWqHaEaR2QE3SlZ2CCKtrSp27XJRhdiZWEAH7yzTiSeAiX4fowCDBPPhkpukAxsRCkG8vqslnSXR+Y61PFWC2P7Yk+OwyIoRII47ngIU1vx0ntbGIov9VG9JozaIFh6yqPTFtq7e1478WqFYTxMu06ud0qyUk9iJq7dM2ZvBUPfYLx4a8lakqoaiqFGOxBjRvqBam+bIbzyZ31r651hYLvOtZ1oAXJLHDOQ3B634rmyq4xYNtAL0h7HdZKqc+207TYX+UynKa4t2QHni351OLPSzrIFkA00ESxv/SE/rzkJPvsdmurVTexqYmBOMRAtymv3OlyIHY/FZdQPOBq1B7rNifW5bFIo6zYcrpo0gL2Vsk5cCF1WuWifybUinEqzTdJeoq/bZY33g5I3/E2B9VboYBtRKcGIyr1ZdGRHznmkYXiqG5sR7WGk2oNY+GQQi97y2ODUwEu9hxH75uYTS8akCuk4nu28Lw6IdVIvrWKg0k0glvH+ikpXWDusaZRlU26zW2zI0yrh+BHhErNnzygip4K/KJV+1HP9eLgoFoGS3aDYKyZWx3Qz6sOpyJGC3KxTsTyFdG7WChoTC5yHfC9K3GWbQX3HCSufR5ArvwyXtq0y8nAi/QO9KRVb7YS1ddmuhZPDpCfj2vQ54kKVy6C3VpH1lZAm9tiTRJRgg7FdSpuhhqz4LOXkjr1W8Jk0rPHip/Z4k0hqp2WUV6wEobngRsqfCRwPj4l5WehEYRNr1kQRMqXk25UlFudxmyG8u4f1HsOO+9qyUOooXXG/kotiG9nBDvKGCN3mKdZpxFgnXBOhELPLVgV7KzaerSv4acRPMn652UnnE0etTg404aNHAVTRGe/tPQ/1AerrIaEUp/VQLrdhSFj0hWtvZzuARW9LrBWRkKy5zuTC8aJf9rZzhDBbsW0jv+Z9swMt87FeLnBo6OJ0aErxWElLDKfaa+zBvBvu+45MTuWeGwwUsfbtcSmXkrFszAIPM6/2kUOADeQSm68M1riWIpZllUg47kHgdaEbLuehYbdnXi0b6iDu2qpGFClf8Ah7CIYC7R366OuRdhgj1eau6pyjKAVmoVRgeVS5NofkYJSgYPxc2AaGdYCIyMF2y3l88WTGFHu61Cz8PCiW667ickPAZ8HG89jqHa8Zr4DYOvtEKtzaICEdr1tOqHptZXJki9WWi879DZmBWhMz/mLpujUyqdMzGF3LsiYTO0N26v06JfyESQ6h3lq0Q/trHjCy2mAtbyVrKB15ZzVIZ7rOjYVhd3LdrbYrIqF1TTpE/IVvS2O/sslt7dqkKrV8Vbgjh2FyL819v9UB02stye0SCd3Pz2ltXyrzFPapfY5hKZKdTr3IaiwTimHtbmd1oYV6L5uHcG/piwrSOGpjZkh8DC9UJJq7SCkRgaytHaE16TGx4sg6EAceSxH7MMY9s4bX6l4ZS86Aoy1HH4+WkmtRQ1HbBRxJR7Y44NSmRRo7vaowfNtHlYXhqe5GSxm5Oli4cLxLpp1Vi1fT7aGh9sYiaeeoYbaCDmceU7GODKs9osVuefPSnNdyZs8ZKjFH9S6D/US+ncq+0fCzRrh4GHrQtt2X1na3q704YUVlzq5U2tG4vYxwW8k0UtMnVrqgxZtkJe7K8nquxkAXthjGBLeKxNIgXDPoJosuzYKuDhWLr7PNoWO3JxkglMFsUkDGDkYcu/lJSJV9XjpibDVXyDVpXQwXXTd3dC69HD3lOs9YuVB1yW0hSugiS0kC3LksVzSqhsMBvgTpYbc5HK+KcOUUGZ4O1Q/FIO36VdP5x76irMFK2mG3VZa93ZbDdXsR2oALjlUtCmgS4mynbfU8HYUEQO71oFQ4x6PzPR9cBFFM+OrKlQvIS0fORZXbgqfpbNj0B1vFRZvHAYTxjJkSiltBaS0wtHdqjudLbsaIaEOKMA7G8Zo3yQbFs+oMBUtMwzUHGmpVtjjlZrHy7TbUB2u98W3Zkw+AOGhykLzqkmZdiS/WULZGq4y08UI7gvYodgrhqJ+dayJ4irtwBRq1rmK/ZU5VMIjnNPKjtiazJceIBoHRF4a+1PoJrI+oHPOiVPsLtKtXNL0KlG4LFWQa1S2epI2BnNFW1qIIrTa7i8bmS8FY08etTnEoRWvWrskuELrXXPPEsPSu6htVCqGlKm1UJtUVubBPOlxZjkuyAoJqzD4mFfi8maNDjNlJz16PaSdDMSFfZSrXdxS33HoaJuA67HIdefOkRX4yBc04ayHcGGGuUsOmMCkGu5W9HZ+j7U4jTyIWi8kRX13VRN+dbU3U+o282JoxRhYhX5VcaxJgJ89SNnY1Wka1QcWi5fKGXw5nK6lO/P6w1IKBjWBUCHuG9Tpaa3cU21F5Y2U2ZK40SLhZGjSk1hVNTSR2TR6WhC0lecfTWKBHuT8yoQLTzShvLVkK+7mX9wcWY3cNpl/bbUoYKNSol/yWhytPXXhtwXhsfjxbAUmf5LSUyEM+wJ6T3zB3w53LMNVyeSf3qWwaC/mQZ0FUnLZCew20PvEYhzchyjOToaZl83Zb+nuZ0EyUNKRhMPebqK7jLj2oLHqBh7a4qSfIs4gxWc+vLF0m4sZS5ihov6AROSIqipJhjyTQ9VrNYfw6Dy6ahbCLSurneeLBA26cFq7GkbDVeGyIwcvSKbQ1CPjm5uUUCeFLdW7rYp2IDZdSYBu7qrmzceZPhNf60cI5X+ZYnty2wppCT3idr2lIC5saDbA9JJBjEaxkbnshkSs+bH1JDXtTFRAYHuANXyCdOBzxvBVunR7kSwo+71VgsdfN15Ed2qArsfmhA9upTeM1jQOH5K5f97VBLeqdn0TjuMcLHlnQLL6yo2pvL4Kcn+9S7lrv8H7enpV5jHuMu+LocX5oMc5EAMZLSOn3YJuGmysmHx0rwSMayhnatReALpXxoGx2BMsd4H5BywCGcvLAb630NpfChvdkqUOEuYkLqaPVcu3XJcmz59RyGIxgyrXZDUjO76y9FGsb4tD0TYjMw1Ih7TPof4/7i7SjKKHak3J0dTsaWWxPW3bNq7eAl6613Kmb3XyhKYIllkqZUHuEaDfktdlk2xV6xfQ1DBF+vFU0x16qU/0o9kIiQO2I3FVcVYsDB9FLMWWJPSUloYs3REfgseBmQWAXna7aCYPLFWflSm3Nz+s6k9p9TjIqvNA5N+gIuU2cRaovey1FmQCm2MFsuIWFaUJIrMwjfJyvRu5oDBsJKrrdNXABFBVXEMp6lPIjEoHd1FkDSLni9dSXFTHJ+jpf9fJy6/hUqG4E0awHvxVatLjlRIysd33WrOtDjO+WygahTJlPBnxtGuFCX8Hb6sDLiEHYGe0aBLPJGXylHiQCWWUhim64wVud2eDmhwGvO2VkI4vbFtXy2DBPWNeIy35A7LMjr8EmLSiqlRJ7ud8b/NFrrhljH9woOxTuBSUTZO+S8XKJ8MFp6bYNAeqHWZMluqJ8lvWJmhF7j60OS2XH7lc3mw3Ja1jxy6Fv+jlWIms4SdmcbjZDT9hC3WDQLifm44hc8gxAFNTmiabn59jyeM1yF2rumnNn3h/0QtkRwv64OTDNsN+ysRwM/hiM4fYsoLt9RZe78YKX49xG1iVMYT2DzGmb8IKR4/vC2FOnG5vfHL5bwyxSXOWrVjOrgEqKDvL5gg6gyOKxsgnl4VpfRSHFEmGxg+H5iuBuTWzkp3lh7oNu78jd5oBkbp/fMskhzZ6P950oBvRmsdJtb71begMhFx1lJ16i8KyShLoES1gcDLG5KleC1tUXNPYDYqVyHq/M/Vq4yvzFRQKm9fJarSIIOUDqhU4g4eTf4pDGN20R0qxuSowryIi6yol8VTK4RV6Dcwi1geNctaOn+3Meva5paYWqe68lOknnuluKujsKEy42yazxOcaxUClWHI12Cn3KF7DOnc5ojvSOzu5Y+QxIFeWXGYy3kISfkbKyqaYdWddyVg1iXuDYmROXUB+N0yD1ZwJqKzIX2qbboucOzjrXITdsAO/qdtyE8Hq8idQ4xrgyEIJzCsZqJbI42IukcEKcSYjf4RbYMfe8fXM38VL1zQ2X2lm2iqvBh0yGPOqdpWLbAaRDA9r0RCua/WGFIOxN4JQruVcXgN3WfY/EcUPT9M8/v3x6mY7Jn4fd/45X7tPB4r/sfPNxFPn+Ku1+2O3b3pe7ri//Fut//fRSu/Fk+/1kuMm68Hk4+l/OhT//C9/VTIrGx7vx6T3i0L6/lGjtcPpPZS9x4XVg8PjWlFl3P8T+9PKx0udh/cvdVXk1nfz/yTX36zwu4unt9Vtbvj1O0P2X6f+YTC/JfC/+dhk+D9c/vXgjSJPJSwiOvfl1Nfnm+RYIuAR+hV6XL3/8bziwcHDwJwAA -->
