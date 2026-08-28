---
name: "rar-cowork-cookbook-scheduled-brief-clean-up-and-archive-background-jobs"
description: "Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs", "rar_sha256": "05a11b1ed1f6a2fbb68e388e32d2f971f8b87884844f7c0d587dd83938fb5d0e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` and in the RCI capsule.

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

Clean up and archive background jobs Scheduled Email Brief — Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` and embedded as the fenced Python below (sha256 05a11b1ed1f6a2fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` first:

```bash
python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py   # or on stdin
python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and archive background jobs Scheduled Email Brief — Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs',
    "version": '2.0.0',
    "display_name": 'Clean up and archive background jobs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-clean-up-and-archive-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9238531aa1706a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/clean-up-and-archive-background-jobs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-clean-up-and-archive-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCleanUpAndArchiveBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCleanUpAndArchiveBackgroundJobs'
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
    print(ScheduledBriefCleanUpAndArchiveBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSJLtX9HEfMiqITPEDso+fc5DaEECAZLYpMo6UeyL2B2EoF799+dIisiqru6Z6Z758JQZJwS4m5lfM7tm7sSvL3bbREX98vXl6Nv5ZG2naRz59cTOvQlfdEV9gb+KiwN/Jm6RN3XstE1Rg5fPL54P3Doum7jIx+lu5HttajupP8mKOo/z8ItTx34w8TM7TiegzTK7jgd4f+Kmo662vGuxazeKr/7Esd1LWBctvJUUDpgERT1pIn9S+6AschCPgosu9+u/TKDmOMx9b9IUk7rNJx5U0E/g+M73L2n/Co3zb3ZWpj54+frTz59fYvj95euvL25qA/DdWN+bjxbyozl6yeUe97Bl/mHKFloCpaV2HsJpZQ+xyuF16dfQvAze8uACn1c/AD8NPk/+4z8unV2H4Mev3/LJ8/PtZfx3gKaOK2oKGzTQetcubSdO46Z/nXBpZ/cALrZp6xxM7AmAUOfh62Pmd0lFOfnr+OyHh5LX0G9++PZSQBPs0RHfXn4ccfj2AmGB319HKeUPP76mRefXP/z4XQ5oncR3m1EYtPr17Xn9FAsHfh8aB3etf4VSHy53/G8vv1vc+HnYPa4Tznx5TYo4/+EhuKyLq5/buev/8OM/Egu94V7SGDT/Lbk/PQRHvu3BNT0N//HzHeSfJ8hzQR8y/7HaErr1n1kJHP6u7vPkCdQ/kn3H/29Ep3Hugw/E/664vzcB+evkp3+4tv9swudJ8O1l4acwousxL79Ofn07qkv+p0/e95uffv4Niv4vxRyLtnbvEt4yO48DHzRvbz99Avfbn37+6VNbwljz7eytrdO/J/Pv4XrX8wcEn6N++ONcqF/PLznM/slHpE9+Lcp/q397nRh2Gnvf74Ovk9/ny/hBJuMi3pU+IPhdzgBo6+9w/PHlN0gYOVxN694fwyz/93+f7GK3LkARNJOjW7TNyDtNnPmj8VoUgwn8/2AriOuDrB7jYPyPHh4tLoLJL//HvZPqF/dJqlPwTkVvd7Z8u3PjW1u+QW58e3Lj23dufBu58ZfXiQZ1FXUcxrmdTg6cqn7L7dDPm9GOElKmX18hwzh943+B3PRl/DKJ88kv/4q6t7vk17L/5U7Y8YPFDvxmZDAAhb2OKJiRnz/X7EJ292++20KlaeFCC4MYcvHnkcuLFHJ9MyIGLnGaTry4hvAUdX+XDVH9Ogr75ZdfHBtE3/IH5RKTR6kBUzjgw5zJly9wqUEah1HzLffdqJh8+vW3T5P/O/nPZt2FjzpUWAuePoMWbo+KDGtR2GZwGHQnDABIMHef/frbE3AoBtafCfRwHMT+YzKM4YvvvaN/FLgvOEVPHB+iDhHPyqJuxpIXN6+TTTD5sBcqHR+NTB8VoIElrfRzz8/dHkq14XI+kMyLZgJgoIKg/zxpgX/X+otT23cTM0gGdvPLZMersK4U6XtJHAfByUUeQ/g/YuNxHwqpP4HJ/F3E60Qeo3ZS2rVdRrX91BHYD7/AevI+HQq3J7nffcvHiuqPUN1T6AEPHASRcZ8u/TL6HPYMsOznHnjXfR9jj9VPu1fB+lsOnulh16MrXFguoNKwjb2xaPzlGVIgKtrUu+PnP/qCpxe8p1fuMcj/dxqLj+I/Wd47k3sPMPnW4ihGTv5/amPGFXHr9WG55rTlYrKUtcPpgfTYiY0eeTRvsIF4qoFZ9b2peKekd2b+lqcxDJu6/8tj5N0/zzEPtmtraMyBO9zlw+CASI9y77E7xmJdj1Fvf8vfS8BnGA53voPug4l+eazlXeH49N3SCGbzeP29Hbj7uvZG8GB8TsrWSWHsBL7vjRBCq+ox/55ugYHsj7nYRbEb/WFVEygdxguUP4FGxDCjILp36OQCLhO6KaiL7PvweGyyoBVe60JrYavrv05MmEKjBwDMW9gpjWMgCp/uoiaZDzGGJn4gDCK7fBgzdsdPA+3RF0UGI/v3Hng+/B70d1tG86FU27MbiGU3ErPn3x6e/bDz6StobDam6X3SH939XOvk97XqL9/yu40ftQBm/yOYv4MzgVmXgXvQjuQFIAFl/kecPir666MoP6r+hy1f/7Ql+OGf2zXcy6z+R899nURNU4Kv0+mjNL5XxldIHVMYI3Hpg+9V8pGMX+6p96Utv0CNX56p9+V76n0ZU+8Puh7QfZ38c/b+QcQz0L9OsFf0FR0fSbHrj5H8/EB4+C/z0xdyfPotP/jf/f4MjpGMYYo7/Udleh8Cy1NY++E4+FGpwFjgOlhT79QMPfMt/4iNZ+ZA5s/DsayC4ncZfS/R0NMPR35UEPgob6Bub2z8Qn/cI6Wj+cB/+Zq3afr5Jbcz/1/YG41VA0YzBGfcYcHMgn1VE/v3q48ea7z4437xnnOQLLzi65h6nydjP/x58tHafp68bzbu27m8hbutn8a2elQJh8JfH2M/NqOO/wJ3e01fjgt57KDGbu7ZZf/ZiDHjoMWuP3YCxUcKjxr/JAR+CUO//rMQ5f7FTp88Ahp7rOtx857977H7eQJdCbMSJhrkzxZO+LMaqKf2qxYWUG9c7nf8vi+reKzltzsMzWMb+uvLO588ffBsOeFwmLhfwFhCpzBsoUJ4/Qgw+Ox/pRl9yoSsCBsfKBSlbAxzMN/DAtrGA8ehWZ9g4Q/u4cGMwQLWYRmWJVmSDBgX9SiW8TyWmBFs4FAe6kN5j9B9G3uHeLQTt22XdRmM9GaMTbs+gTqE62M45jGEj1IzIoDySQjZx9QLpNTn4h+LHZH96ItHkJ4Y/Pri0CQcKZBgwz0+/HRm2I6lOrdIQIZ0djto1P54STZeWaGl3SjnpYETp4uXIB16wZYkzS3JS+bPlXkoHNcnNAOZ2vPTnYRkg0+6VljvXWWmnG+tulzmPNEw7nUYaOY855bFTN71xqBH5zklZsdzrR6NZb3aSaWfVoFQNKes8bcZMFZlLkZGbtOXgbUT3Y5XyDTILKrAd7veMktww67lsJ6unNsxba8YI+kqsqaOAvyyb7Q4q9KDmIKTJdZHh6eG1KJ0URPpTFe2xyLpk8IS98yJF/up0RY9Th4T1M20LeLlGkr5uYU2Q0lPlSsbrUQ2FJMVVQZbsZdKOzO21ppANk0sHqLTDTuAabemMGfFnKrU6NVdhFug6ViPA9Y6r8mtEe23mOHtS3W4EDtTGnT0LK1pHlgaX2wlc7cUFaOWLB7R6+OZj+PGMDOsv5zzC9rgiXJifDmv2nJFHBjUKOt037LkEVzOYb91FZmVemVH4ZvI2JTmnqX3uiQyIJIX+a65qYa4pdsG6aKNlLgXE+XmlpH14mXACWWOuDs6lpWm3ZmULZZ9gIU5aonpMfIlJrWHDZM6SzFRrYZzLIHZhcCwO0crq4XZWCDn7UwVj8ZZvgSMYqZ+6eQeCVanXqDoVAvr41rZ5uKxoNtToLOGiXhb7Dq7Ckq4FTfAw5mzVyHTjXViPFYAs3a98c6yBJItoxLKAcfSpSGWrkkye03xLaMadmZtzG0d87ZhaS6RTTqdhdUuUvKomtE2uKWJOl12eivOYpfcAxmRhDUZzW8+HUWZ6KPRWaAJxm7P5sowTqYnHLr0qqk9slsI9QY9LqVyPwMXrGph1LjlVqZxUeRoF+nts3e5oBChUlDsq3yD2YFTQRgSRcYUAdHlDcxwTFlxZjPtVC1fksFUW8x2GK3A2MudA6tmTd8tg9UaFzX9YJpqFpsHi6ekxtZWS+0qR0BfgxNhKds9u8uKpMu8DSglSm8uW0s2JEsqFMVLqAXBqC6228aYR0W2rOFi5HYVO+eEpX7QCfFQLslV4ibt5cB5KSOdeJvXI7uTqnSI5kBYTl0kxdtVgyjXXESyxNnRc9QCxSb0VrKxmot6zNB84WLz5SIqmcKj0a3qzteOR+VZ6ZyFjSafPETdxMSy1IdrMoVrzs31zfBKaYsLt2M9BJQoxRhukd1cXJjxOZLPl5mBktPVMlFUmwNKk5zmNB/Q6Xka3SxDQ1GW386WcWZTWM0z/UaMlHMYK6bVxu5uOWZ5wCzj6WzvX9ZWo2wTjZmyRbNJXYNkroYEBKrsQ8IDkp9jwUyW9pe+QOGuM9zuTysi9+UNEGXTMYHKXdzqSovSgNX+iiucjN8XR3WPIEXEIXFlGbHb1h1kxoN0K2yULKbtTtLLQ1WuNExA9ke3AuCYxYR1vM1mCXEhlsfMN1d1v9xUTmTtQbjj8gXvdfViu9W1Ba1TmaUAsNUPypHBi305m+VStCcyM4lJ1xTUBWsYWX0MAqU+zVA67LH0LCSEZTRChgvomTa8c37okpZrHaQE+uwCiHKLDOS6DlwxkFj/Snscs8D7OSwXPr5YxoPIB0oD8M1ill/dy76fomqBpJUabjhLurWri3xZnZN4MeQVo7H8aoX6ceFPj/OOX3vTUyoqtempFmns+kNpd/Ihsq9bsENlPazDc8l5G71O1+IVXfbrlIyA0vbZci1d0nmMRu2+MfGZyKeLDdPJm241iKHh2cStDE8reWeuWXlJ7ZOwA/sD2Pm9Kx7AUVgciEhXBfXkthv7qODnpTlNSxosAE1YEqqf+zOySVr/qsnoTBmofqoe+eMpY5a2N8PYfHU86m5GbJOgFvYpwxVoG3hHsMBmTiffmoERnM1yc7hcmabzvenUlwYEk/wp284kRLfUdMGWFb86zxiqacU9t3HmSakBVLFvg9jFMH6kSGeqxZwjcdbyNFHk5W5p7SGn+BxFJ4ugbmMxP1QHSsP6+VY20XpnFaI2p49R0sShYER2iJb1Nqli2ZufI/PclHoopFfpbLpej6xIQuKYYUElOaVFgDmjh8NZN3bkrQbcDqFM49zyF/oC21AsWzFbG7WvMzMn3XDJs9Epb0qX7AEQZGWzsgar3kV6tju55klz5Usk20GbVyYiFgRDXC9kdgKZqwwewuO8pBcHe123vHTEfAonFWxJ8Cuo63wF12CbLVURX5o6Oog9L2o225ZHqSoydjGNnFDX6710Nb1mlhhh2mnR3N4ZieUVkI8sszlgVzs1Wn69yTixyi7ghGkcq2Q3ZWcujEE+GNO6S+ldCw32q6hsjvONAGQ70jp7NvdY43ABgNbSsy9Yi2XhkpbSbeTAyM0q0aLKlPeHit9w0jYh5UYkrp5bX2bLwzLKFI7pLlQ4W/YMwJXV6Yhcoq6bb5plZ3LXQTl0nEbjeJqsI9Gqhf7gIMRKgpFXVkam7/PTdQZLjx67tHVC1xehSFS3X6jALFyvjlakVVbDckOU6P4yW9MZHseXgt3dtKMtkLDq9X56NOjN1rkI8qrJJGOTFtLsEC2Pc4GYh4Z15kKSd6gY7YXpqbb1acMfLyszjOnt1EtxYqsopE00wmauz1JuNYNh69YLrAzP2NZZocY67JweVYOpKuQpdTN3+3XqiUXioHTEqAUT4uta3zKYr8pUSGO+tW2wXU1OTzElaFVwxAkzN/decpCyIPRchOlOp5DfuOJyYZ9EYXF1KKPfNWGwSfRtU62qqFIL6tQOOlJNb8X+VhXr6xkSZ+vWLroXwNrbHLEq0vdeYFQnKSE8ThA9U7Kue0ve4nuesg4zcd5Xrm0gi1XHc+cFIjKXdO94BWV0beX481WyQWMXuMra3ID4piYy1odb5cKpNQfSzeZGX/Z0TW2nuqn4aZ/hJ6WU5H7NxgGPllNyPyx6NF/ZeHbWC6XXGTZL2UMmZrDLtnfqUmL4iOs1U0r2B3Wx3bfzzJiXMMrQxjrRwLtsY7c/tZrnywUZl5sl4iis1B2nC4Y3MLyvHHR2O644nTijMrrqVrhh9P0WT+yzcrpujHTanGUk3bHL6ermrv18EzSCGopT1QSHfHcLUa2h7VtN9326biwN77wrdt4ePC9pBOtYnRpwKg4qW/vx2Zv1QQ8GlQW8v3UNXQNW7DA77XSkCzCfh0k82/eFX4lbUPJJtkubeHNwqXMnE7yhMabpeTdaNAHBMIfBDTumxqjpHMU81RV0fyahmNqLtVXaZCGeeaIKiY6HpaTfL84kpBfh3K0Rm9p1AWyNL6y+oLD9tlzGGqZULglkZ8qZtiEn1uy4JmMt4M+W20hrPopEYXfOWn9tZ+4tYvfA1o+GeKXJ7rQqpzNtRVZ7bXFFGVXWDszxuPVXmuHQp43oiCS+L8xjyEbWQIncur3tOupUCSoR787IYZGjsPlC4nBpJIAS1tp1IRNYcRSXoNss6NnFKKx4u4ekVuAIUWWEvQXNQpPD0zkIbacg5sGN3Q2ytI6KKmtQ+gTmnjTFxCGLNiEJ8DZP3ezSGjK9WC7AbrXugnWc9G5onupb1pihKa6dbX8O1nnZ1Fdqa1akUu0sklsVl7NxPedzwjKpa8hfVhvd2mVLZFgV1D7FwsM6wg3fLUhNxG8ndAND4Toky6qvqGlTbzJBW/Q+UpFk7+20w80NGnO4WcMi2xteE+wvclhxB7qq6VLEhbrZaNdE86Y0d4mSYYljbed3Jm1RgyDQWuOrx3ad04Phr53YnDNopjEzk19jFEtbWT/NuRnhAKKaRw3DkA6zXgDj0hjtwpDsGXaIbXde4ioxPwvuigvXlCFdKPSCCmSmWkVtCDq27278NtYTJeG37F5wnamJx0HMOSfFmRtWxU7r+R5NdtxhHjplHWugEuQ89mIDW5myoF8CE7VwQTgyN/aMxGXQlyKNsTJ/vp5xwtIXpilQ3XpNrq6ndsaY3EwQcnzagquK7K70Kl7nnjNFioDE0ebGEJbaH5ErauRnqyo0zEGXq2pLKWHCmtc9Hrqk5OQbHiPrm4aE/SVbcOQYL5G86yC5a3m8ofbu3teTdnGSFhf1dhbmt9bxdlJDKDiJbzjXIDKmxQpW4KQWO4tlzhctFVhX0XXJYVdSDb3fFdeQ6ZOjzPae1J0ha82atrBQgRU6ArYLznqr5zM2ZoXccQw2UqkVldLWrQoPg6rbwpWd0kzICfvBPg2kkxWZJdxoCUNtJqWF3sOQckrfZkRicKa8OE3DtR7G7TDvcWTR0UJDqJWf7WOmqXH8hiXLlRyZ+TZraga3KKZZez6wV0REFTMKI3Z1gzCRpoLdjdtbZOWBGY848Y5Y3/jNEWYrcToGh3l1c28CgyUI2WYVeeRUsznB7a182+M36TiztGG4hsQhVBeKzN1Ycdjoc8ffIgwrkrzF0lQ/3Or2CrjW98Na31gR57C2qAT0cCWsa7fhbotZpxqhEQ68TxHDqvMP0lzIeILbLWEvXKYhqfMCos11U50h+8QyHDdSp2olkTzcsu6NKe/yWDsQgQWrW7vM2Pws+3GdGZ01+Au2xmH0elK6z3hx1ggt3Alt82vUNgXenwhzel0H/paPBbmTjSRUUYtrWWUOTidlqhDLcz2/Lc83HOZiiLg2mBkhcSTnfWcunL3nbZpbQ18DE+9LrGyTPGgi/RzlpSad7CSmMc7Bpi0f7NbhZjsggFwF7sKHcB326uV0TU60iscrYU4rRLkrWvoM+0Xk4K+YRqujucrzaItO16669hxIA8YZbq6mRaDLOFVPcz88JMuIaJGWMAtf5wN2usiVYWDxK9ku2JldiamHose9ytxuLo0IhEoBZCDI3GMr/hT018JyfH42g2VpsxZSIdtsi24lJ4bmUuyMzfEDJAUyOaCJTiDxNUTQmj2Zoc3zp1VlI1JO0LR+WxyaQdcuFrEYKNggZTSQyWu6KoEQeVorH7c74IKFHw02u1+i6zma8gt50M49daOXXmbWlaPv2oyonQEjaaZOyhu+wTZ8JxdTAKM9r+bquUME/tpKp+y6nPpBe+JMhRNJP+VNfDFulHRKC6rBPmT7dYD38X7B9Fcn0XPimBe5PUuZdADkEEtkWzYzDywCgQx5SznD5/OAKQsZuFlKEzHCE+rQ9sSGzVucDYEStfzJQuyllBHLOGq0qXhZFkFFDIJmq44/cL6D9qSQczIRn2TmzKPVTt5gK15OSgQluhWGHSlMuOSuEzBDQgIuV05efPGIKwB6i3az1ZQzyrxSbpkYctzL55fxhPt5Tv0/epM9nhT+rx1YPs4W399r3Y+pfdv7etf19X9m5s+fX2o3hkY+Dm9B2obPY82/Obr98q+8IRkl9o+XyONrulvz/iqgscPxL6de4txrQVP3b6BI2/uB8ucXpwXjn22At+fB+ct98Vk5nsL/zWLhHdvL4jweX/S+NcXb4zx7POKN8/EtlO/F3y/D51H35xevhz6Gze4bQVNvfl2OMDzfvoynwePrl5ff/h/XhmcquyYAAA== -->
