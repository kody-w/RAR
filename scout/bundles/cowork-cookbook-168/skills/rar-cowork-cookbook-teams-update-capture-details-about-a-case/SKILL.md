---
name: "rar-cowork-cookbook-teams-update-capture-details-about-a-case"
description: "Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_capture_details_about_a_case", "rar_sha256": "5176fda4b97810fe61f50368fb5f6dd7aa26bc51f4542bdc3af3d4fe263ebabf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_capture_details_about_a_case`. The original RAPP
agent is preserved byte-for-byte in `teams_update_capture_details_about_a_case_agent.py` and in the RCI capsule.

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

Capture details about a case Teams Channel Update — Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 5176fda4b97810fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_capture_details_about_a_case_agent.py` first:

```bash
python3 teams_update_capture_details_about_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_capture_details_about_a_case_agent.py   # or on stdin
python3 teams_update_capture_details_about_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Capture details about a case Teams Channel Update — Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_capture_details_about_a_case',
    "version": '2.0.0',
    "display_name": 'Capture details about a case Teams Channel Update',
    "description": 'Drafts a Teams channel post on capture details about a case status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-capture-details-about-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-capture-details-about-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6c7ead08e3c572b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/capture-details-about-a-case'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-capture-details-about-a-case', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCaptureDetailsAboutACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCaptureDetailsAboutACase'
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
    print(TeamsUpdateCaptureDetailsAboutACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebObSLbnV2Hu+6OqnmyzL3JHRwyglVVCgBDlDhdLsohVLBKiXn33SST5uupVd0/3i4kY2dcWcPLs53dOJvfXN6/vkqp5+/x2AF6JrL08TxPQIF4ZImJ1q5oM/ldlPvxBgqrsmtTvu6pp3z68haANmrTu0qqEyxeNF3Ut4iEm8IoWCRKvLEGO1FXbIVWJBF7d9Q1AQtB5aQ7p/KrvIHXgtQBpO6/rW+SWdgkUjKRlBxov6NIrQPgQLpy+iF4TIlHVIJc+DTIEKuLF4BNUAwxeUeegffv8898+vKXw+9vnX9+C3GvhrbeHNlYdeh0QnyosnhrwkwK8CMVDHrlXxpC4vkNflPC6Bg0UVcBbIYiQ19WPLcijD8h//md285q4/enzlxJ5fb68TX+MvkS6BCBd5bUdCCebPT/N0+7+CeHzm3dvkQZAFcrJTS20oIw/PVd+51TVyF+nZz8+hXyKQffjl7cKquBNjv7y9hMCffDlremn758mLvWPP33KqxtofvzpO5+2988g6CZmUOtPX1/XL7aQ8DtpGj2k/hVyfYbUB1/efmfc9HnqPdkJV759Oldp+eOTcd1UV1B6ZQB+/OkfsQ0SEGR52nb/Et+fn4wT4IXQppfiP314OPlvyOxl0DvPfyy2hmH9dyyB5N/EfUBejvpHvB/+/2+s87QE7bvH/y67v7dg9lfk539o2z9b8AGJvrwtQA7Lo/H8HHxGfv162C3Fn38Iv9/84W+/Qdb/VzaHqm+CB4evhVemEWi7r19//qF93P7hbz//0Ncw12Axfe2b/O/x/Ht+fcj5gwdfVD/+cS2Ub5VZWd1K5D3TkV+r+n81v31CbC9Pw+/328/I7+tl+syQyYhvQp8u+F3NtFDX3/nxp7ffIEyU0Jo+eDyGVf4f/4GoadBUbRV1yCGYoAkGuEsLMClvJmmLwL9TbTcA+rVNoWNfdDD/pwhPGlcR8sv/Dh6g+TF4gSbaTQD0tX8g0NcXCn59oeDXBwp+9b5OKPjLJ8SEAqomjdPSyxGD3+2+lBDkym4SXjegBc0Vwop/78BHCEgfpy8QLJFf/mUZXx/sPtX3Xx4Anz7xyhC3E1a1fQ4+TfYeE1C+rAsgHIMBBD2UlFcBVCtKIdZ+gH5oqxzCcjf5ps3SPEfCtIGOqJr7gzf03+eJ2S+//OJ7bfKlfIIriTybRotCgnd1kI8foX1RnsZJ96UEQVIhP/z62w/IfyH/bNWD+SRjB7H+FR2ooXTQNQRWW19AMhg4GGoIJY/o/Prby8uQTQm7HIxlGqXguRhmawbCby4/bPiPBM0gPoCuhm4u6qrpIGIjafcJ2UbIu75Q6PRowvRkanYhqEEZgjK4Q64eNOfdk2XVIS1MyTa6f0D6Fjyk/uI33kPFApa91/2CqOIOdpAqh/9Maj6I4OKqTKH73xPieR8yaX5oEeEbi0+INuUnUnuNVyeN95IRec+4wM7xbTlk7iEluH0pp44JJlc9iuXpHkgEPRO8Qvpxijns/gVEhrD9JvtB4019znz0u+ZL2b4KwWumUASwMUChcZ+GU3v4yyul2qTq8/DhP6jpxOkVhfAVlUcOiv9sXniOGOJrxHh2d+RLT2A4hfz/mUMmlfn12liueXO5QJaaaZyerpyGpsnlzzkLzgKPxY+y+T4ffEOXbyD7pcxTmBfN/S9PykcAXjRP4II2hBAijAd/GH3oyonvIzmnZGuaKa29L+U3NP8AjXxAF3QCrGSY6VOCfRM4Pf2maQLLdbr+3tkfwYRmw/DDBETq3s9hckQAhL43+SBppgJ7BQBmKpiK7ZakQfIHqxDIHSYE5D9FIoVRgoj/cJ1WQTNhbUVNVXwnT6d5CWoR9gHUFk6l4BNyhDUy5UkLCxMOPRMN9MIPD1ZIAaCPoYrvHm4Tr34qMw2yLwW9KRZVMeXM7yLwevg9qx+6TOpDrh7MMOjL2wS3IRiekX3X8xUrqGwx1eFj0R/D/bIV+X3b+cuX8qHjO8LD8s6njv075yAwAWEST3g6oVMLEaYArwSCmfBozp+e/fXZwN91+fyn6f3Hf2/Af3RM64+R+4wkXVe3n1H02eW+NblPEBtQmCNpDdpnw/v4bEYfX+X28VVuHx/l9tH7OJXbHwQ8/fUZ+feU/AOLV3Z/RvBP2CdseqSkAZjS9/WBPhE/CqeP1PT0S2mA78F+ZcQEsfkddtj3fvONBDaduAHxRPzsP+3Utm6wUz4AF4bjS/meEK9ymbAnnpplW/2ujB+NF4b3Gb33vgAflR2UHU6D23Nnk0/qw/3J57LP8w9vpVeAf3lHM3UAmLjQJdNuCBYRnIa6FDyu3iej6eKPu7hHeUFcCKvPU5V9QKYp9gPyPpB+QL5tER5br7KHe6Sfp2F4EglJ4X/vtO9bRB+8wZ1Zd68n9Z/7nmkGe83Gf1ZiKi6ocQCmrl69V+sk8U9M4Jc4Bs2fmeiPL17+ggwI7VOPTrtvhd5CPUM48XxAYABhAcKaglDZwwV/FgPlNADiPcTcydzv/vtuVvW05beHG7rn5vHXt2/Q8YrBa1CE5LBGP7ZTO0RhskKB8PqZVvDZ/3yEfDGCqAcnF8iJxlkmCj3Kn7McjkWAwSMaIxku8umICUPW8wjGD2g8omiK8MOA9CIypCJAMCTwPT+C/J5Z+nVq/umkHOF5ARewOBXOWY8JAIn5ZABwAg9ZEmD0nIw4DlDQT+9LMwiZL4ufFk7ufJ9mJ8+8DP/1zWcoSLmh2i3//Ijo3Pb8I+obiTJr8tkwkMyetGqryFk/JrczfHMMnC1fLNwRS9utTYhHOoOZ3/N3p5PVcbEzNnMhIvL5bWy51rFOF3++4SltGfup2bL6DB3HlSQst6PurjZ2bcj15WLqjSQOl0ObGAe5W15mNrlKhq526easDI67kQ9VGUXX3N6JbN7G8lBjMWccV61k3fUxCm6de2y9tOtDxTqqScA0+L7OsDqSybV3SrW5Lmm5XHvFaj2/lPZdunTGvQ4Ug9mZNUZdx5oB13GYKdwArgpJbQfQ48sqE87DbYNrjpcrjcd17qU54NK20EPM1LgLJgQr9nTZRlaFkcv6PsPOBnu2imO93a/4sl7yFyWjroVCWv3h4jYeLXLeTaRYxRIvF007K86BODaiceDsi2OrS6HI0mvbZAO7kTEiuDC5E+7I6mw6ch3SVXaol7Fuuy6jc8pdV2liW9tSrSzLuWammb87B/Tycqr9xGWIw7yiOJ4mJeWqZot1Rw3amKvzVuKv5C3PL44bqua+W+2pHYOZdyU/1vtmNSc6N/UVvTkltlswW6G/7Ap3c5K1mNj4x3V37Fx9masgOKYHX0YJW9zO5UGX7+2Kmq1optrHl2Clb+smY3j3OOI7HC+Lex5wrIBJ/WnTlHlOkiAmBoLNFLcBOyO9+afYPrr9vCxOY0KoVMp363W6PSaB5c7cwPF86bBbkWeAr20xPvhLGWVP4nnruJRr78xdIbcuSvWpvb/Gs8FYevNC1/eDdAdyfi7kIzbMFjTpMVe6kEL7dAxH4iT52Mhdz/xQDFm6TyJ5TBu5XZdab0Z4ajrTTz5IjSwf7GPJciNuD1yxTeaLM3OgZ4rJLTcUL14jZmkY9a5CWzVy53ob1SW6ovpEDA8ssfcW0jxvDZ+ytUOOW2Hn7Y2NjMvdUU7FHZHzhKLst959TC1yIVxunFgK4dHJ/a05k4HTeHsdhBa9CFg9wFUpZY7crVvWYpZL9kHjC6NbWa5eWgdDH3Rim/NJ22YeLziqkSvbqk5HfSFUmyULwJ0iReYaNzQj1NR9U+ZBQkuRBFJ/cLZXV5bE3R3u/qBTTpkbo1LVkqOttWk27ysdFAuG3CiHRb6YYbvZbjgyy8BfbbhyOBmbEyuj2R0mOm2keGWdWl/UmrausTWGLnWZ6u7NGl/u61NcovXapPu0qmZzG1+QWJFfFpJxiSruKBfaoTmWVc81iRxGZhPe0iXdzrXMKTFwUdSTouCZOKutumMM38e4ZuZ2ntURinzBTxFj3uuWHWpxWa0Ot/XxINsOrcvp3EUTa5uMgoatnApESyvRT32On0ol40QzSg3QVdh5tUBpKDhfp/kBPZnBXmYsY1/W4bkHI+NuyvV1u4EVxOP0tnGx/rg5SWdDLyzGkILYOW7E61JlaDzPt3Ht2cC+bHZSRi9FfXa/Y7ZYzAYKbS4t7hl+gB4MsyaS8Cy11yXq1G3S8wIRN2qvQvq6ueLa2cHSYm41xDUCUhTE+ZxD0a2mzLjVCBInx3B6dfJkNW1sHC8aeb5d4dRl7cxq4XoVztm4WS3OkXwZCoG+QSQMeH8IylNxvdICJSx0Tj1km6WzK1lMX1tL3HFvLBqaGeF4+myph6oVL09SfY8Zk9boesPf+tPZGwLnJB5WErMlDqfKD68acWOv3DJbqLyQHXPXGi4pJXn+aZkIdzwB/WkrKOlxoWPY6GaCjGKGDTY7wPW8bOqFfz3aByyHcNWyashybDqq+xErHWL09XHC47HK8ljyhnVT9+iQOErR3Jug1NwKXcQgTutjoEVROhrWmmXGnOjw4UaXhBHxOTcDwpVpdhl356LhTO9R2YuVYM1xBLnanlYXwewOx0z3pBGWf3UpnJTGrSKowutuLtadNNeoghKlrWYE13jtDe0la4KiXmbX6LSyko15NDrNZdJ1NqvXTS+arIXKFVGzUsIIR0fuForpXFbRnE/rmr0v/Nh1addJHUUfwagNtz2Ti9uLZ595kG+HwcClTuSYU3Pucca+br0MVwTo/1ip+CTh6TYPmDuWsgS5FF261IpFr6xVlVIP3Zy+1nus3DdqSNd06MFmtaFogJ/Ui1EwnNot/VpOa9cOjty5ATSJafiSVDUx45Jr26Hndi867ak9SWSUZXxuLlm65q/teZMwfHWv4qzC5poQ2ss83lsrlcO8Y1fHRYpZmOATte1fiqW5ErdFTZ3w4dzHIj3KiXYcbZwcNM6XU8LlaswuLdz0KtG47tec6MTufrXnlnTRcoTZzQ7r2UKoj5WpxvgqtMtjdXZj7FBUuSM6N8/cDRbNRPuCdSSGT6WFehLKRD3ze0Ul7b0nc/lWoU98KNwkpwCieyuzbr5ba+q+P0YdQYawJYfuaHpGcdyXpyvt2Kl1rmiCwtbVpi534b2InPh6CveJRln1ZVziqFnlEqPiWrdcuTZ1zrLRopNVOcQWger3YWOKpXSDBpNjl8u5lxbpgVdZI1wbdpgdFvFWLJSDjfrpuTbny2WyXVELct6y6KmrDqZ/pYKzPd5s3s/FA3s1ukgw9Fr1+j69r8+9dJvPUQ41cZRl4m2npufbqr9pYztwt6VxYwNUz7Sh2RyJcc7ABCVmJRwtsJPu5rI/7+eEncdh5qm8vJ4zOuUKkl2lvFDEt3VkkOsm13cCmoj1wec1x1wGhjcHZY0a7uJwlIAALLbwCpcxNHnF29hul7nezbhYsgV3UGJFk+EobC82i+HnojuyubXek2NutTjbGDtLpSthW9rHnG74BUgTTTUwJquWWrSMgq2aU5S138Oy1fa1OiarRXGb+lDYi3xotUSEr65ZrXZdH2/jwnX8/Y4OrGuluENcSMPqWq/t22Inhtg+ZbeNcdCtnbTZJmAmng5BnS0pe2vaYqDwTmcwuOqe3T7brODGTzsXi+XdA0ay6U/rC26s185tXZvY2ZXd64GhsnphCtmBrZQl3tnOWS0vOKBHKNQV+2vYjNeMLpm9vPb2JycQZnDCcW2amceq2++M5BZJhHJk9rVfGeFw8gUSbSRZxnXtwrBnc2MH5pa8H3Cq2V57u7bX/syLy1XP3LZ9A5FAXlrxoAutMRPimzEEVWTtNIEnrMQYdQIXxCWpHINFfdt7s+Y+NpkmXcgczURVuyuijsYyaMrLoZ+p+5zyey1ILxpz7GWx2HdMpXF8cQlpOXFhnmKlG6/6A6vGTmne2itmDti+zpfxeVAuAdd17CgcYfjPlmasqcaMxLkVdLu1mLmLjerGPdg2ikQuKEG919n9AHKtTOQFxeohr1aKDPvbTjtH9Cw7MMoatsI4MMnVUCf8LefZ47UQLrvmtAHC8k5DGHB36mnkLqtdzUW8zi+YO4txfi2RbMt41koX12CTdMH9YiljKtM1AScJkkmx9WkJW6jgEqLLFAK+450xLNzMJsH20ltXwhYC4jqXjgF24tcrgsiAffdk2iKNUxYKseULnCfvpJtgpH2P32/isB9dfbGj77VMzNAs95qYqW5OzPN39h5zDSbgI9pS62IlwckmhbqHvo3R3CmzTu7KLDCwvXXBSRcDO3CkusQlKURnhrIpg4gWZ/vNuafAsq64aK8ed+uKYdezYO8KmCLcr854CLONQzIF3Cjs2EpYryM5J9olSRKljEonNNpz/sCsyPms9MpijMggJdE7YO/USu4iNCR7v6fWOhv0luX7+r1bROFQ2sbWVLoRDde9Nfa5h/mLJqbgaGLc9KtcBE2AdjgpbJpuuIyEt60Wiuxtz5qjy3ScCw56RxWgmphhDItCtnG63clop8F9aBzz3d1GWXJQCnIDhpE5N8vNJUCJ81LfbAzypvozNiXzGescb5lWzksfhPsVHDXHStduUmiEbM+tmN1O2qJ+GEXcKtrLnKozJDq7RBSBdS1LHndXZt6rS8d1qq3ZKLhIBnocCgZ1bG9DHFDKpohFjfQHCbtZB3PBsxpMFiajbut8cy6zLZfqt53ok0K7Gg47qoXoT3Z9kRNjGQXjWvZzsvBLCwNKYrahK9cQ5TCuU8hE171xKdG5uy0gWoSjmR05X8opPb36SSNVO2zDbW7k2tn7+la+NsmC2ulEz9I8Wvq54/prKy4sUMkDWi9wcr/uF1oeq8bMS7lENzOzqUhSwaKMaeYOip/n+tnmj6GWzwW151dhsbhDZKOYTbfZkDtzdWDDBiduq3QpdsmxlIquYQlnhXbr0Dlo4nhHLYsLDbZozuM1Xw4309qKUR+S40lczpZuBLceie+phl6VIChbO51v2U6hW2kZ33RswaORAeDuSTqWlxmA6bxhL+fhLF70SIxvbGbXSxol4CBVoFtWPQIpZPqbM8aq5g0FJ+lmcnRJ7riYU9xOSNZbv+fRo3Bc7GI4Jm1IgV4GW9FVTnzBhyUojotkv/VX6so4oSUtaiHepcuKQ4/2regWoaDM0ZDRupEEzild9UsCLWspTM9n6aTsaoHwmR1habx7Um5Eaxno2ZFO53lgsC0BbXa1GbVYMRVlzIMFf52v+fV1wxOqtonOs9vauwVGEYQAJWYH+kyWl7YfAR+oq5iAY5KmBD4od1jTpqHnV+zVxpogKS/kURh0vwnEyCA4SzxpN6uCIBvpc6FhM/ps8Iv8hKYjFuXGfWZSYLdnU1+6XooI61v97DmRqICtUIXEfKSUFMw7IrpbN5+NcHJchD0zp2d3bs2BNWAJLjwk7F4fupnNqY7jt2g1W7Ero4410mSH+zwlBdLZDjQeXjGASgEKZ6QNqjArgoyvqJMuyLyOAgwXNF2sW+/CSpGK0mZ8sqPWrii7YevLNda5hvOA4O3F00o+zBSS5TibXgyKeSQ3VND3MTce2QwvL+NRYMqZLe+T5r5ODiURWPxuP7ZczK/PsG8lbkFtVTS4dbxmmv68u60d00ev7oEDobbTTg3v8bW1gjvK08wcyIWTYLNdm/bsvkCHGXcLMsGleDahLMU/8VRk5It8B+zCWui8egtpOEnsOkCuaz6gr4aObzQz31T3cSHQ5JweQgrMo+giU4rO5tSGdjQDPUo16CnOnhX2NfCxTUGyui2NsbdqI06+RBcs89p+4awcrOIvJSqZchQGYxvh0jDTUf5Uiaq+qon5VjW2GGFtV47P5MaGM6zmstteOAxNnLUVXQO8GzcLVyINOF12SgNjH/n3NUyMuOZ5/q9vH96mA+rXMfO//055OvL7f3by+Dwk/PYC6nHIDLzw80PW5/+Bbn/78NYEKdTsed7a5n38OpT8b6etH//l9xcTm/vzxe305mzovh3Ud148/TbSW1qGfds1969tlfePg98Pb37fTr8U0X59HXC/Pcws6um0/PdmTQfpkwFd9fXxqv3b+sc7yQKE6ZNmuoxfh9Ef3sI7DF4atF9Jhv4Kmnqy+vVWZDq6nV6LvP32fwDbmz9f8yUAAA== -->
