---
name: "rar-kody-w-recon-deck"
description: "Builds a recon briefing on a topic by querying Hacker News top stories and Rappterbook agent profiles over HTTP."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/recon_deck_agent", "rar_sha256": "678ff374c053126043a75147034abf4a27d05e626c83862ef7ff0371a5781ce1", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["deck", "recon", "intelligence", "borg", "rappterbook", "hackernews", "briefing", "multi-agent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/recon_deck_agent`. The original RAPP
agent is preserved byte-for-byte in `recon_deck_agent.py` and in the RCI capsule.

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

Recon Deck — Multi-source intelligence briefing agent.

Orchestrates Borg (repo/URL assimilation), Rappterbook (AI agent social network),
and HackerNews (tech news) into a unified recon briefing. Ask about any topic and
get a 360-degree view: what the code says, what agents think, and what's trending.

Drop it in. Three sources. One briefing.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "sources": {
      "description": "Comma-separated sources to query: hackernews,rappterbook,all (default: all)",
      "type": "string"
    },
    "topic": {
      "description": "The topic, keyword, or URL to run recon on",
      "type": "string"
    }
  },
  "required": [
    "topic"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `recon_deck_agent.py` and embedded as the fenced Python below (sha256 678ff374c0531260…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `recon_deck_agent.py` first:

```bash
python3 recon_deck_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 recon_deck_agent.py   # or on stdin
python3 recon_deck_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recon Deck — Multi-source intelligence briefing agent.

Orchestrates Borg (repo/URL assimilation), Rappterbook (AI agent social network),
and HackerNews (tech news) into a unified recon briefing. Ask about any topic and
get a 360-degree view: what the code says, what agents think, and what's trending.

Drop it in. Three sources. One briefing.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/recon_deck_agent",
    "version": "1.0.1",
    "display_name": "ReconDeck",
    "description": "Builds a recon briefing on a topic by querying Hacker News top stories and Rappterbook agent profiles over HTTP.",
    "author": "Kody Wildfeuer",
    "tags": ["deck", "recon", "intelligence", "borg", "rappterbook", "hackernews", "briefing", "multi-agent"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@howardh/borg_agent", "@kody-w/rappterbook_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import urllib.request
import urllib.error

try:
    from openrappter.agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        from agents.basic_agent import BasicAgent


_HN_API = "https://hacker-news.firebaseio.com/v0/"
_RB_BASE = "https://raw.githubusercontent.com/kody-w/rappterbook/main/state/"


def _http_get(url, timeout=15):
    """Fetch JSON from a URL."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, OSError):
        return None


class ReconDeckAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic, keyword, or URL to run recon on"
                    },
                    "sources": {
                        "type": "string",
                        "description": "Comma-separated sources to query: hackernews,rappterbook,all (default: all)"
                    }
                },
                "required": ["topic"]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        topic = kwargs.get("topic", "").strip()
        if not topic:
            return "Usage: provide a topic to recon (e.g. 'AI agents', 'kubernetes', a GitHub URL)"

        sources_str = kwargs.get("sources", "all").lower()
        sources = [s.strip() for s in sources_str.split(",")]
        run_all = "all" in sources

        sections = [f"# Recon Briefing: {topic}\n"]

        # --- HackerNews Intel ---
        if run_all or "hackernews" in sources:
            sections.append("## HackerNews Intel")
            hn_data = self._hn_search(topic)
            if hn_data:
                sections.append(hn_data)
            else:
                sections.append("No relevant HackerNews stories found.\n")

        # --- Rappterbook Social Intel ---
        if run_all or "rappterbook" in sources:
            sections.append("## Rappterbook Social Intel")
            rb_data = self._rappterbook_search(topic)
            if rb_data:
                sections.append(rb_data)
            else:
                sections.append("No matching agents or activity on Rappterbook.\n")

        # --- Summary ---
        source_count = sum(1 for s in sections if s.startswith("##"))
        sections.append(f"---\n*Recon complete. {source_count} source(s) queried for \"{topic}\".*")

        return "\n\n".join(sections)

    def _hn_search(self, topic) -> str:
        """Fetch top HN stories and filter for topic relevance."""
        ids = _http_get(f"{_HN_API}topstories.json")
        if not ids:
            return None

        matches = []
        topic_lower = topic.lower()
        for story_id in ids[:30]:
            story = _http_get(f"{_HN_API}item/{story_id}.json")
            if not story:
                continue
            title = story.get("title", "")
            url = story.get("url", "")
            if topic_lower in title.lower() or topic_lower in url.lower():
                matches.append(story)
            if len(matches) >= 5:
                break

        if not matches:
            top = []
            for story_id in ids[:5]:
                story = _http_get(f"{_HN_API}item/{story_id}.json")
                if story:
                    top.append(f"- {story.get('title', '?')} (score: {story.get('score', 0)})")
            return "No direct matches. Current top stories:\n" + "\n".join(top)

        lines = []
        for s in matches:
            lines.append(f"- **{s.get('title', '?')}** (score: {s.get('score', 0)}, by: {s.get('by', '?')})")
            if s.get("url"):
                lines.append(f"  {s['url']}")
        return "\n".join(lines)

    def _rappterbook_search(self, topic) -> str:
        """Search Rappterbook agents for topic relevance."""
        agents_data = _http_get(f"{_RB_BASE}agents.json")
        if not agents_data:
            return None

        agents = agents_data.get("agents", {})
        topic_lower = topic.lower()
        matches = []

        for aid, profile in agents.items():
            searchable = f"{aid} {profile.get('name', '')} {profile.get('bio', '')} {profile.get('archetype', '')}".lower()
            if topic_lower in searchable:
                matches.append((aid, profile))

        if not matches:
            trending = _http_get(f"{_RB_BASE}trending.json")
            if trending:
                posts = trending.get("trending", trending.get("posts", []))[:5]
                lines = ["No agent matches. Current trending posts:"]
                for p in posts:
                    lines.append(f"- {p.get('title', '?')[:60]} (score: {p.get('score', p.get('trending_score', 0))})")
                return "\n".join(lines)
            return None

        lines = [f"Found {len(matches)} agent(s):"]
        for aid, profile in matches[:10]:
            lines.append(f"- **{profile.get('name', aid)}** ({aid}): {profile.get('bio', 'N/A')[:100]}")
        return "\n".join(lines)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61ZaZPa2Hr+Kyrmw9hDd4N26NRNBa1oQwLEenvK1nK0oBUtSMKZ/54jwHbbM5PcVNKf0NF5t+fd1V8GVl0FWTF4HSiZ2yG7MHY9UINi8DRwQekUYV6FWQpfMzV8VSIWUgAnSxG7CIEXpj4Cf1tIleWhg9gdcoakXX88t5wIFMgCNGX/FimrDFJA+tRFVlaeV6CwsyxCLB+kFZIXmRfG8HV2gURz0zReoAKgtZIcng5e//n70yCEvwevXwZObJXwaLDq9eCAE816FvB6bKU+PM87aFAKn3NQeFmRwCMXeMjj6UMJYu8J+e23qLEKv/yIPP871K14fUuRx9/dln8g9wsvPqg+vA1uh2+DJ+Rt8Db4+AIpwvzDx+9EoYekWXWnfcer/ytAVRcpJNyU0NjX3tZL6IJvqFXZA9IP4MV/QX6dSXdQyl+fkF+j2gZFCirQP1mIGFbz2kY2K/UjVCT9LqjM6sIB5Seo2M+qP17dlbfiuNc/zhpQvNf/cQnS/rP8ah0C8UJKJEzfc38p8zjs2T5BPr9/Z1DU6SfIHDJ4CHlH94OiwOkD6ibJexv8gtzciDCPcHpFvtxQ+eMNEg1+f0/5C/L8/PyIq1tYSWkF4v7wBzd8VQTq/jYIbrdTePsHhX7y0FedXmBcgtSFxv3yy58EQXN/pArST65VWdCQPqRePsHnEliFE3y4WfDTbajZg+An4X+lwOPmTyxAXIJ/gfhtsOgjKgYXC2bWOzO+pqCX1an7cgP4458Bfp+c68wJrfhfAbr4TvW/RvrvJP4J8cL+EfF3Qv8H6B+U/wJ6j5v/B+gTq3KCvgTes7jHx4LXLmHV9cXynbV/64N1nSRW0f0I+R3RTw70XtVDUCcf0Hcp+jWvoLV9BltFVTZhFdwghkI+/jkFv2oN07AX9Jb+ds9FJ+urbgVekC/vZf7x0OADLJp9mQ+BexP/9vY2+Ja0b4OX334y6Vv9663tDX45ZWH64asWHwd/wNqewtJS3w9gvYZBoYVOkZWZVyFrKL3qo60KE9AzNoMQmgnbSgAgc9gwytCOweMerK6nO2ck85DP/xHBrvbcjG4V9pMLu8Wnm1s+vyAmJIcJ4YcpDLjVzDDe0nszgqzzApSguEAL7a4Cz9DM5/5HD/Tnn1m95N3nW1uDL3uVVqyEOFZe1jF46dXdBSB9KOdYKQJa4NSQVZw5UO6t6z1BM8osvgBID4WXUQjTyg2hIJix3Y03NP+1Z/b582fbKoO39N7lcOTeosvRLRsf6sC4gQZ4cegH1VsKnCBDfv3yx6/IfyL/HdWNeS/DgP31AS7UUF7rCwS2kzq5RXPvKWC5N3C//PGAEbJJYd+Grgi9vsL0xHGYRsD9iul6PnvGSAqxAcQS4pjkWVH1SRJWL4jkId/0hUL7V/2gEWRlhbigj1GQOh3kakFzviHZ99vSqsLS656QugQ3qZ/twrqpmHxy4PXPiMYasMNm8a3N1ncPQeIsDSH83zx+P4dMil9L2IseLF7g+NLPI7kFK01QWA8ZnnX3S5/YD3LI3EJgm3lL+ykF9FBZfQze4YGXIDLOw6XPvc/7JEugY8uvsm93rApGnJlZUHjxlj4yBIIPbhMCVKVD/Dp0rdQB//YIqTLI6ti94Qc17Tk9vOA+vHKLwXti98MS8lZjY5RAtDquwud7RvcGgBjCD2EG3ye7e2D05DosrQBmKNQPwpMVPvKhd9MIziEIDJYwCeObuR+ffijmH76OMrBy3Mo6HGSarIg+PkHgYVC/600fKhimPYKwuDzgrNOHGT/Mmy/IrIRTo93bbqXdY4aC3N5SOO5AMpwaP7vALwBEIgTNK9LAOLi7PYNTV2l1MN9uZ4/6DHMujZ5uWdYfwwCoChhyvazedq6A02vYO7l3Zs/20dpeED39jlY/r8ahA6DXBq9pHcdPg9RKwPs5tR9JYSQlsLQWZT/JwloFp9IqBLenB9v+54+TN9uHynMJeuI+QL7OahCl27j9inwfc57e9cSnvjt/gLOvBX39isCnj1CFqst7rfoZD47LsPbeEPyz1D5wb6+ekAh00G3uUx/xvcsfqXR3zG3U/okp5FqAcw3D3YWz+0PC79+uZXZfonvZOYyb+4z+ZQBxsfrW+0DmUcXh9cIqnss+2EfoyxgKg8/3ogXf/V19f1wrAwtWHXiPoieeh9OEMyZxFKPGBG7RJErQY5ywbI+wMNodk4DCKGeCTygMeLTnjXEatUh6gjoAhfy+9cIkCXvRY4zy0IlNjKc4wIEzph3Mw8mp604pdELgEzDGxtbYBt9JozB1H/bcleyB+tZqersfZn0Z2BQBb86JUprd/9jRdHvYY6NTzQgjlHL8WHKl83qc6noXaDJXyDagYwyj8Wi3Xq2GXRAxdqVhqCrmsnImA1EP5hRv0AwYmq5kRbaWrxdFtPO2/mnJrrrjKRh518VGlGxGPdaKX7TJuNuT9Go0kuphsTf0IZ/vHK2U1KunOFc0YtTWkLFDs3fGarBfu8yEF3Rh3OZrc2uSQiHphyhSJnt/PEQ9drtTCjzQFytXwFkdr9gGjVotiMM1BRJX4NldkupWdJhnFcmpNWObUjfDXDWPnNLehNHONpldd9keujPLy/LWmx2PbbJa1ZWVH1bOeb0LeFTIl1m5GFtqtMFPin9KOMFTudPQm560cXwYrlflaLcsGHfD06h/ZLNuFZjuWSZdjchyTFcFWKrWV0PKCz7YHefBhle7XRauHH+cyfV26G902NmPM6N1BGO9YllAaOakqkejUTodZfNhhTqeQSrFfjrU6DKlz1ORrrBRTUfY+cJYEc/kbLlSDJUVPUFbxWU2x/UDKDGZkVtP1zqwhrEoWkV4iuZgRSW5rJb+WBrxkoDZw5A4sjxfKLR9lVNHFp3gitH76WzbTDEv7lR7unC4iJZzJtvtxOps0bkgM9sdm2usu1+Yhbh1Y/Pk5qrjbJTKztOMzc9gDXf7654SCQFzqZJbqgYqbPiV7hYtWIowrlx+u8hKvt4IJRuYGk2Tu1ytjquwTY1DEDOqky5Go6uYoxa73fuhLF4agWO3o1mHJhxP5dPrzlWmwZTl9JNO++rU0eZzlG68pXQ4+L7eDo2iSUJFE1kpFXDiwsn+0R6TbukuZgc6WSbkMrOSZSHYJ2u8vRYnkJNlkynY4Xq6MCY9vmAVUNbn43J7ok410EcxH2bedmamIrcYri4bkacKopoRETOPAjReJWEztwgW35fm9BDr9Bbf43iwmjfbdRLJ8XCj6EW6jmRJbhKKb4rEkreyslsuZ1ymnfZuujl3MD8dmuk2O681jHqykmvNihW0kbHFMC0WZnRxwnMqYbwX1mcprbnsjG8u3mnKu8NdgJlG53YqyEVxeeTAaaEUp+FkppaKgJ43FucfsNOoPnRapG18lNdYan3e+ot5OZkf4P392dtvcffiMaSMThKHGm/Q82ptbjjHAt2wq7hFUSrKRGT9BbPk1n7InDRSCTNmTR1myxXFzBfbprNIfS+cp6HFrPGz6hrLozedTLF5xLHmsmGMcr9GvSISzayZpRMpY2DtwEeYfpg1rL6dR0vfHMkuu1Gj61ZWkzCRzksmNNcq4a/8WZ53gnCk0Mv0JGruELDS6NSqy/F4nR3Hu4C1JosSvnREBxClkdP1eqUwPmHJBZfwKlaLOSu0WEgZoSaiC+Dw3GitChOyTDm0WTJioiYukczl9GwkTVPkSSwuXByPLvl+SnRTTCCvNZESq8alwFA7XWA55GfH3PdPO2Mhs1PlMFY3R+1SMDl+DC0+4ZLDVrY5sVVLQWnaa0fipi+RvsYRm6k5P+1wQJ62J6MBO1tanKTqeGpCGUamuhIsgcLzGb6OryiObijWwkeksbsQp214OWyXo2mRSLRjWWFHOQvOqYPKsIZrcDWN9XItr6g5wy2TSbsZHgT7OhurZ/RoHafYOlz4GNEGnbtdOmwwZ+rcJvUucbZtyU5MQvbl2lQiYy9jVbYGuuQFF29inhgHRIs8J2X1MFqaQQciwTB1jcdXY9HZ0uBEXCPqEFCH9Xoia6zC0GFiqNLBUi5MS2vcUdvzm4sfp4y1v+Ib6zB01HMp1wFZqyNG7Kypg6NL02TjZlryi0WyzM/zdeTIYyrjJJ5VTb1dZVO3bBR7NjwvsmTmESF7JrSLPhMzgmVbYWLNa57Rc9IXY9SatEMpZ6Yb5byz9ETapEJZQITrpaSAhYBb3mzF6yYLInw4olGqxXXJhiPw6DJMgyXajmYGt7N8K9iu16x62FJKk+smGsQBLjLHhluVG5eLNk1xCWOR2PJHkV4f2rNuZgE15o0rbfPmQSiFriXRlON3R+0aEPl0vjVGeEaltXCIJIYjMH0+PBnX1MYPRl0dvCk33R/JKVXMTtykkscTYyga+WJ7vYjkCI9ZY2pvqUl2ZWjahiUr3SgMFfCia3c4EI/Y8NLVs7QTEsq+HOoL587OzDgJiOqQ1RflXCiNpbWKEm3C2rEqtpha11UOp72A04YCBrAm4YZKqs1OGWxvYIHRl5kkzUbt3JxuCC3xGjpbNkNTqyhZLCYTYSe7E97uJCrTpltjozQNrDvbSN164DoX6NSOrIXYog5esqtVUKsnFjYUrBlRx3R5JPw4oIRWSGhXUktuETpNs4sKW+Gvk/kxLFsMo6KN6SxrhcAOo/UMHTbZkbQomMhrHvaQmAxykSdaSjTIzjgRmaAcic7f1ZiYtIVkVyf92tocP6aD/XxIRntBDGqLaq+pMTFOIIhqbEvvJGmfV5tIYls0yiTzwpvcjlVad1ln/vxyZMwCt9HqTF54Mnbwa9EwrQh45xCRk7qzaiydRRqlXXw4P+nnTaKLbijBHFh53B4GWzHSDoFed4ClDPOqwF2Z63hyYdHiBDBGPhL11ew8kpaNLYgHWdHo037faLVC+TM36xI1TMDIiUjZVdZFU4JqagUxh5Kz6WF0pomDM+UCstm3xK5raUEv2lLEKepaUvi51IvyqurFcasbJmfNT06SkFlh76xM37ndyh17Z17mSGd2HudD3ZWH55nvEHJQYvMLQdXTVaPjQdJNU6ecrht2VyiUbR6u4wVuuEPCXHKOBnwZzCRXP49r72oWW9WfUfbca+lGVZhSwjQ4VNfcjlTx5LDSCL1gA5RjrrvxfhVmM0xjpoSLmXmStDkhTLio4fKcjjqCWpCzZNldNhhB22LqnfaTuX2khGoS4lpGeqHg1dSIMiV3OhrVo1r0ttiOrtYKY3iXJQeraWMHKiAPThBMd7zTNqGOb3ZCudlp5XHoYQFj7jA94hwdE7RO5AO0UMysLbNNgtHKQl6OuPlkNJ9H3c40w1w/tiy1FBIsPXWqyRBVRmN2nghkWbqYly3snTNl9vqRJro6SmcON9FVYpKELNrRnc9Hu2yJyivNqMfVaaEGLIliTkpPeM6YcJUEZmfFt+Fs/g844vdL/WPh+4sPRP0O8P+2ity3huwC5cF9vV+wCmC5rzdZr38lHG5ehRNC0ff9qYxr/7GG3Len5xvRs3vfUcvu/vkkSyvQVl+X2cry+//DDB6XbhSD/sPd9y8H8NHOCv+2en1bQuHT9+20v/HYl+HP5PYJ4r7yQBVvH/JuCx9U8wWa+V+0eAODnBoAAA== -->
