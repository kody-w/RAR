# RAPP Agent Building for Absolute Beginners

## The No-Code-Required Guide to Building AI Agents That Actually Work

### By Kody Wildfeuer

---

*No tech skills required. The AI does the grunt work.*

---

## Copyright

Copyright 2026 Kody Wildfeuer. All rights reserved.

Published independently via Kindle Direct Publishing.

The RAPP Agent ecosystem is open source under the MIT License. This book is an independent guide to using the platform.

---

## Dedication

To everyone who was told "you need to learn to code first."

You don't. Not anymore. This book proves it.

---

## Table of Contents

- Foreword: Why This Book Exists
- Part I: The 10-Minute Foundation
  - Chapter 1: What Are AI Agents (And Why Should You Care)?
  - Chapter 2: The RAPP Ecosystem in Plain English
  - Chapter 3: Your First 10 Minutes — Opening the Agent Store
- Part II: Using Agents Without Writing Code
  - Chapter 4: Browsing and Installing Agents
  - Chapter 5: The Agent Card System — Collecting Your Toolkit
  - Chapter 6: Building Decks — Your Personal Agent Portfolio
  - Chapter 7: Using Agents from Chat
- Part III: Building Your First Agent (The AI Helps)
  - Chapter 8: The Agent Workbench — Your Browser-Based Workshop
  - Chapter 9: What's Inside a Single-File Agent
  - Chapter 10: Your First Agent — Step by Step
  - Chapter 11: Testing Without the Terminal
  - Chapter 12: Publishing to the Store
- Part IV: Going Deeper (Still No CS Degree Required)
  - Chapter 13: Making Agents That Connect to Things
  - Chapter 14: The Holo Card System — Making Your Agent Collectible
  - Chapter 15: Running Your Own Agent Store
  - Chapter 16: The Community — Forum, Wiki, and Getting Help
- Part V: Real-World Playbooks
  - Chapter 17: The Sales Team Playbook
  - Chapter 18: The Small Business Playbook
  - Chapter 19: The Creative Professional Playbook
  - Chapter 20: The Enterprise Team Playbook
- Appendix A: Glossary
- Appendix B: Quick Reference Card
- Appendix C: Troubleshooting — When Things Don't Work

---

## Foreword: Why This Book Exists

There's a lie in the tech industry that goes something like this: *"To build AI tools, you need to be a software engineer."*

It's not true. Not anymore.

The RAPP Agent ecosystem was built on a radical idea: every AI agent should be one file. One file you can read. One file you can copy. One file that an AI assistant can write for you while you describe what you want in plain English.

This book is for people who have never written a line of code but want to harness AI agents for their work. Maybe you're in sales and want an agent that researches prospects. Maybe you run a small business and want an agent that drafts customer emails. Maybe you're just curious about what all the AI agent hype is about.

Here's the deal: **you don't need to understand the code.** You need to understand the concepts. The AI tools built into the RAPP ecosystem — the Agent Workbench, the Virtual Brainstem, the chat interface — handle the technical work. You provide the intent. The machines provide the implementation.

This book will take you from "what's an agent?" to "I just published one to the store" in a weekend. No terminal required. No Python installation headaches. Just a web browser and an idea.

Let's get started.

---

# Part I: The 10-Minute Foundation

---

## Chapter 1: What Are AI Agents (And Why Should You Care)?

### The Simplest Explanation

An AI agent is a small program that does one thing well, on your behalf.

That's it. Not a sentient robot. Not a replacement for human judgment. Just a focused little helper that takes an input, does some work, and gives you a result.

Think of agents like apps on your phone:

- Your weather app takes your location and gives you a forecast
- Your calculator app takes numbers and gives you answers
- Your maps app takes a destination and gives you directions

AI agents work the same way, but they can handle messier, more human tasks:

- A sales agent takes a company name and gives you a research brief
- An email agent takes bullet points and gives you a polished draft
- A CRM agent takes a contact name and gives you their full history

### Why Agents Instead of Just Using ChatGPT?

You might be thinking, "I can already ask ChatGPT to do these things." And you're right — you can. But there's a difference between asking a general-purpose AI to figure something out from scratch every time, and having a specialized agent that already knows:

- What format you want the output in
- What data sources to check
- What your preferences are
- How to connect to your specific tools

It's the difference between calling a general contractor every time your sink leaks versus having a plumber on speed dial. Both can fix the sink. One is faster.

### Why Should Non-Technical People Care?

Because the barrier just dropped to zero.

In the RAPP ecosystem, agents are single files. One file. You can look at it in your browser, see what it does, and install it by dragging it into a folder. You can build new agents using a browser-based workshop where the AI writes the code for you.

You don't need to understand Python syntax. You need to understand what you want the agent to do. The rest is handled.

This book shows you how.

---

## Chapter 2: The RAPP Ecosystem in Plain English

### The Big Picture

The RAPP ecosystem has three parts:

1. **The Agent Store** — A website where you browse, collect, and install agents. Think of it like an app store, but every app is one file.

2. **The Agents Themselves** — Over 125 ready-to-use agents covering sales, customer service, healthcare, manufacturing, finance, and more. Plus a growing collection of community-built agents.

3. **The Tools to Build Your Own** — A browser-based workbench where you can create, test, and publish agents without installing anything on your computer.

### How It's Different

Most AI platforms require you to:
- Set up a development environment
- Install packages and dependencies
- Learn a programming framework
- Deploy to a server
- Pay for hosting

RAPP requires you to:
- Open a web page

That's not an exaggeration. The entire Agent Store — all 125+ agents, the search, the card system, the workbench — is a single HTML file that works in any browser, including offline. No server. No account. No installation.

### The Single-File Principle

This is the core idea that makes everything work. Every agent in RAPP is one `.py` file. Inside that one file:

- The documentation (what the agent does)
- The metadata (name, version, category, author)
- The code (how it works)

Why does this matter to you? Because one file is easy to understand. One file is easy to share. One file is easy for an AI to read, modify, or create from scratch. When you use the Workbench to build an agent, the AI produces one file. When you install an agent, you download one file. When you want to know what an agent does, you read one file.

Simple beats complex. Always.

### The Publisher System

Agents are organized by who made them:

- **@rapp** — The official base. The foundation everything else builds on.
- **@kody** — Core tools: the registry client, memory agents, the workbench.
- **@discreetRappers** — Integrations with business tools like Dynamics 365, SharePoint, PowerPoint.
- **@aibast-agents-library** — 104 industry-specific templates. This is the gold mine for non-technical users.
- **@borg** — The card system and code analysis tools.
- **@yourname** — Your namespace. Once you publish, it's yours forever.

### Quality Tiers

Not all agents are created equal. The store has a trust system:

- **Community** — Anyone can publish. It passed basic automated checks.
- **Verified** — A human reviewed it. It's tested. It follows the rules.
- **Official** — The core team maintains it. Guaranteed to work.
- **Frontier** — Experimental. Pushing the edge. May change rapidly.

When you're starting out, stick with Verified and Official agents. They're the most reliable.

---

## Chapter 3: Your First 10 Minutes — Opening the Agent Store

### Step 1: Open the Store

Go to the Agent Store in your browser. That's it. The page loads with every agent ready to browse.

If you're working offline or want a local copy, you can download the `index.html` file and open it directly — it works from your hard drive.

### Step 2: Browse

The store opens to the Browse view. You'll see agent cards arranged in a grid. Each card shows:

- The agent's name and a one-line description
- Who published it (the @namespace)
- Its quality tier (look for the Verified or Official badges)
- Its category (Sales, Healthcare, DevTools, etc.)

### Step 3: Search

Use the search bar at the top. Try searching for something relevant to your work:

- "email" — agents that help with email
- "sales" — agents for sales teams
- "CRM" — agents that connect to customer databases
- "report" — agents that generate reports

### Step 4: Click an Agent

Click any agent card to see its details:

- **Full description** — What it does, in detail
- **Source code** — The actual Python file (don't worry, you don't need to read it)
- **Required environment variables** — What API keys or settings it needs
- **Reviews and votes** — What the community thinks
- **Download button** — Get the `.py` file

### Step 5: Switch to Holo View

At the top of the store, you can switch between "Business" and "Holo" card styles. Holo cards turn every agent into a collectible trading card with generative art, stats, and abilities — inspired by Magic: The Gathering.

This isn't just decoration. The card system makes agent discovery fun and helps you remember what agents do.

### What You've Done

In about 10 minutes, you've:

1. Opened the agent store
2. Browsed 125+ agents
3. Searched for agents relevant to your work
4. Explored an agent's details
5. Seen the card collection system

No installation. No account creation. No technical setup. Welcome to RAPP.

---

# Part II: Using Agents Without Writing Code

---

## Chapter 4: Browsing and Installing Agents

### Finding the Right Agent

The store has 19 categories. Here are the most useful for non-technical users:

| Category | What You'll Find |
|----------|-----------------|
| Sales & CRM | Lead research, pipeline management, proposal writing |
| Customer Service | Ticket handling, FAQ generation, satisfaction surveys |
| Healthcare | Patient intake, appointment scheduling, compliance |
| Finance | Invoice processing, budget analysis, reporting |
| Manufacturing | Quality control, supply chain, production planning |
| Marketing | Content creation, campaign analysis, SEO |

Start with the **@aibast-agents-library** namespace. It has 104 industry-specific templates designed to be immediately useful.

### Installing an Agent

There are three ways to install an agent:

**Method 1: Download and Drop**
1. Click the agent in the store
2. Click "Download .py"
3. Save the file to your `agents/` folder

**Method 2: Drag and Drop**
1. If you already have a `.py` agent file, drag it into the browser window
2. The store saves it to your local collection (IndexedDB)
3. It appears alongside cloud agents

**Method 3: Ask the AI**
If you're using CommunityRAPP with chat:
- Say: *"Install the dynamics-crud agent"*
- The RAR Remote Agent handles the rest

### Understanding What You've Installed

Every agent file is self-documented. If you open the `.py` file in any text editor (even Notepad), the first few lines tell you everything:

- A description at the top (the "docstring")
- A block called `__manifest__` with the name, version, category, and description
- The actual code below

You don't need to understand the code. But knowing where to find the description and name is useful.

### Local-First Privacy

When you drag agents into the browser or download them, they're stored on YOUR device. Nothing gets uploaded to any server. Nothing gets shared unless you explicitly submit it. The store works completely offline and air-gapped.

This matters for enterprise users who can't put proprietary tools on external servers.

---

## Chapter 5: The Agent Card System — Collecting Your Toolkit

### Why Cards?

Every agent is a collectible card. This isn't a gimmick — it's a design decision.

When you're managing dozens of agents across different projects, visual cards are easier to browse than a list of filenames. The card system gives each agent a memorable visual identity.

### Business Cards

The default "Business" skin shows:
- Agent name and publisher
- One-line description
- Category and quality tier
- Key stats (file size, line count)

Clean, professional, informational. Like a business card you'd hand someone.

### Holo Cards

Switch to "Holo" skin for the full trading card experience:
- Procedurally generated artwork (unique to each agent)
- Mana pips and colors (inspired by Magic: The Gathering)
- Creature type and abilities
- Power/toughness stats
- Flavor text

The Holo cards are generated by the CardSmith agent — one of the most creative pieces of the ecosystem. Each agent gets a deterministic card based on its name, so the art is always consistent.

### Why This Matters for Non-Technical Users

Cards make agents approachable. Instead of staring at a list of filenames, you're browsing a visual collection. You remember "the blue card with the shield" more easily than "dynamics-crud.py."

The card system also makes demos and presentations more engaging. When you're showing a client what agents you've deployed for them, a deck of Holo cards tells a better story than a directory listing.

---

## Chapter 6: Building Decks — Your Personal Agent Portfolio

### What Are Decks?

Decks are named collections of agents. Think of them as playlists for your agent toolkit.

Examples:
- **"Client Demo"** — The agents you show prospects
- **"Sales Stack"** — Your daily driver agents for sales work
- **"My Builds"** — Agents you've created
- **"Healthcare Suite"** — Agents deployed for a healthcare client

### Creating a Deck

1. In the Agent Store, click any agent card
2. Click "Add to Deck"
3. Name your deck (or add to an existing one)
4. Repeat for other agents

### Sharing Decks

Decks can be shared via URL. Send the link to a colleague and they'll see the same agent collection in their browser.

### Present Mode

This is where decks really shine. Click "Present" on any deck and it becomes a full-screen slideshow:

- Arrow keys to navigate between agents
- Toggle between Business and Holo card views
- Each slide shows the agent's full details

Use this for:
- Client presentations ("Here's your deployed AI toolkit")
- Team onboarding ("These are the agents we use")
- Agent showcases ("Look what the community built this month")

---

## Chapter 7: Using Agents from Chat

### The RAR Remote Agent

If you're using the CommunityRAPP chat interface, you have a built-in agent manager. The `@kody/rar_remote_agent` can:

- Search the registry for agents by name, category, or keyword
- Install agents directly from chat
- Tell you what agents are available for your use case

### Natural Language Commands

Just talk to it:

> *"What agents are available for CRM?"*
> *"Install the email drafting agent"*
> *"Show me all verified agents in the sales category"*
> *"What does the dynamics-crud agent do?"*

### The Virtual Brainstem

The Virtual Brainstem is a more advanced chat interface that can:

- Load any agent from the registry
- Execute agent operations directly
- Switch between agents in a conversation
- Show agent source code and operations

You select an agent, pick an operation, and provide the input. The Brainstem handles execution and shows you the result.

No terminal. No code. Just conversation.

---

# Part III: Building Your First Agent (The AI Helps)

---

## Chapter 8: The Agent Workbench — Your Browser-Based Workshop

### What Is the Workbench?

The Agent Workbench is a code editor built into the Agent Store. But here's the key: **you don't need to write code from scratch.** The Workbench provides:

1. **Templates** — Pre-filled agent structures you can modify
2. **Validation** — Real-time checks that tell you if something's wrong
3. **Card Preview** — See your agent as a Business or Holo card
4. **Download** — Export your agent as a `.py` file
5. **Submit** — Publish directly to the store

### Opening the Workbench

In the Agent Store, click the "Workbench" tab in the navigation bar. You'll see a code editor with a template already loaded.

### The Template

The template gives you a working agent with all the required pieces filled in:

- The description at the top
- The `__manifest__` metadata block
- The class definition
- The `perform()` method

All you need to change is:
- The name and description
- What the agent actually does (the `perform()` method body)
- The parameters it accepts

### Using AI to Write the Code

Here's where the "no tech skills required" promise delivers. You can:

1. Open the Workbench
2. Describe what you want the agent to do in plain English
3. Use an AI assistant (Claude, ChatGPT, Copilot) to generate the code
4. Paste it into the Workbench
5. Click Validate
6. Fix any issues the AI or validator flags
7. Download or Submit

The AI writes the Python. The Workbench validates it. You provide the idea.

### What to Tell the AI

When asking an AI to write a RAPP agent for you, include these details:

> "Write me a RAPP agent that [what it does]. It should accept [these inputs] and return [this output]. The manifest name should be @myname/agent-name. Use the standard RAPP agent template with __manifest__, BasicAgent inheritance, and a perform(**kwargs) method that returns a string."

The more specific you are about inputs and outputs, the better the result.

---

## Chapter 9: What's Inside a Single-File Agent

You don't need to understand every line of code. But knowing the structure helps you customize agents and fix issues. Here's what's inside every agent file, in plain English.

### Part 1: The Description (Lines 1-5)

```
"""
My Agent — Does something useful.

A longer explanation of what this agent does.
"""
```

This is the documentation. It's what shows up in the store and what other people read to understand your agent. Write it for humans, not machines.

### Part 2: The Manifest (Lines 7-20)

```
__manifest__ = {
    "name": "@yourname/my-agent",
    "description": "One sentence about what it does.",
    "category": "productivity",
    ...
}
```

This is the metadata — the agent's ID card. The store reads this to know the agent's name, category, version, and what it needs to run. Here's what each field means:

| Field | What It Is | Example |
|-------|-----------|---------|
| `name` | Unique identifier | `@yourname/email-drafter` |
| `display_name` | Human-readable name | `EmailDrafter` |
| `description` | One-sentence summary | `Drafts professional emails from bullet points.` |
| `category` | Where it shows up in the store | `productivity` |
| `version` | Current version | `1.0.0` |
| `tags` | Search keywords | `["email", "drafting", "productivity"]` |
| `requires_env` | API keys it needs | `["OPENAI_API_KEY"]` |

### Part 3: The Class (Lines 22-35)

```
class MyAgent(BasicAgent):
    def __init__(self):
        self.name = "MyAgent"
        ...
```

This creates the agent. Don't worry about the syntax — just know that every agent "inherits from" BasicAgent, which means it gets standard capabilities for free.

### Part 4: The Perform Method (Lines 37-45)

```
def perform(self, **kwargs):
    input_data = kwargs.get('input', '')
    # Do something with input_data
    return "The result"
```

This is the heart of the agent. When someone runs your agent, this is the code that executes. It takes inputs (`kwargs`), does work, and returns a text result.

**The only hard rule**: `perform()` must return a string. Always. Even if something goes wrong, return an error message as a string — never crash.

---

## Chapter 10: Your First Agent — Step by Step

Let's build a real agent together. We'll create an agent that takes meeting notes (bullet points) and turns them into a formatted summary.

### Step 1: Open the Workbench

Go to the Agent Store and click "Workbench."

### Step 2: Modify the Template

Change these fields in the manifest:

- `name`: `@yourname/meeting-summary`
- `display_name`: `MeetingSummary`
- `description`: `Converts meeting bullet points into a formatted summary with action items.`
- `category`: `productivity`
- `tags`: `["meetings", "summary", "productivity", "notes"]`
- `requires_env`: `[]` (this agent doesn't need any API keys)

### Step 3: Write the Perform Method

Here's what the `perform()` method should do:

```python
def perform(self, **kwargs):
    notes = kwargs.get('input', '')
    if not notes:
        return "Please provide meeting notes as the 'input' parameter."

    lines = [line.strip() for line in notes.strip().split('\n') if line.strip()]

    actions = []
    decisions = []
    discussion = []

    for line in lines:
        clean = line.lstrip('- ').lstrip('* ')
        lower = clean.lower()
        if any(kw in lower for kw in ['action', 'todo', 'follow up', 'assign', 'will ']):
            actions.append(clean)
        elif any(kw in lower for kw in ['decided', 'agreed', 'approved', 'confirmed']):
            decisions.append(clean)
        else:
            discussion.append(clean)

    parts = ["# Meeting Summary\n"]
    if decisions:
        parts.append("## Decisions Made")
        for d in decisions:
            parts.append(f"- {d}")
    if actions:
        parts.append("\n## Action Items")
        for a in actions:
            parts.append(f"- [ ] {a}")
    if discussion:
        parts.append("\n## Discussion Points")
        for d in discussion:
            parts.append(f"- {d}")

    return '\n'.join(parts)
```

Don't panic if this looks like gibberish. You can ask an AI assistant to write this for you. Tell it:

> "Write me a RAPP perform method that takes meeting notes as bullet points and sorts them into Decisions, Action Items, and Discussion Points. Return a formatted summary."

### Step 4: Validate

Click the "Validate" button in the Workbench. It checks:

- Is the manifest complete?
- Does the name follow the right format?
- Does the class inherit from BasicAgent?
- Does perform() exist?

Fix any errors it flags.

### Step 5: Preview

Click "Card Preview" to see your agent as a Business or Holo card. This is what it'll look like in the store.

### Step 6: Download or Submit

- **Download**: Saves the `.py` file to your computer. Use this to test locally.
- **Submit**: Publishes to the RAR registry via GitHub. Your agent goes live in the store.

### What You Just Did

You created a working AI agent. It categorizes meeting notes into decisions, action items, and discussion points. It follows the RAPP single-file standard. It can be installed by anyone in the community.

And you didn't need to install Python, set up a development environment, or open a terminal.

---

## Chapter 11: Testing Without the Terminal

### Using the Workbench Validator

The Workbench's "Validate" button runs the same checks that the official registry builder uses:

1. **Manifest check** — All required fields present and correctly formatted
2. **Name format** — Follows the `@publisher/slug` convention
3. **Class check** — Inherits from BasicAgent
4. **Method check** — Has a `perform()` method
5. **Schema version** — Uses `rapp-agent/1.0`

If validation passes, your agent will pass the automated CI checks when submitted.

### Manual Testing in the Workbench

You can test your agent right in the browser:

1. In the Workbench, look for the "Test" or "Run" option
2. Enter sample input
3. See the output

For our MeetingSummary agent, try:

```
- Discussed Q3 marketing budget
- Decided to increase digital spend by 15%
- Action: Sarah will prepare revised budget by Friday
- Talked about new product launch timeline
- Agreed to push launch to March
- Todo: Mike to update project plan
```

The agent should sort these into Decisions, Action Items, and Discussion Points.

### Using the Virtual Brainstem

For more thorough testing:

1. Open the Virtual Brainstem
2. Select your agent from the model selector
3. Choose the `perform` operation
4. Enter your test input
5. See the result in the chat window

This is the same environment where end users will interact with your agent, so it's the closest thing to a production test.

---

## Chapter 12: Publishing to the Store

### The Submission Flow

You have two paths:

**Path 1: Submit from the Workbench**
1. Click "Submit" in the Workbench
2. The store creates a GitHub Issue with your agent code
3. Automation processes the issue
4. Your agent appears in the registry

**Path 2: Pull Request (for more control)**
1. Fork the RAR repository on GitHub
2. Add your file to `agents/@yourname/`
3. Open a pull request
4. The CI system validates your agent
5. Maintainers review and merge

For beginners, Path 1 is easier. For teams, Path 2 gives more control.

### What Happens After Submission

1. Your agent starts at the **Community** quality tier
2. The automation validates your manifest
3. Your agent appears in the store with a Community badge
4. The community can vote and review it
5. Maintainers may promote it to **Verified** after review

### Your Namespace

When you publish as `@yourname`, that namespace is yours forever. Nobody else can publish under your namespace. It's tied to your GitHub username.

### Updating Your Agent

To update an existing agent:

1. Bump the `version` in the manifest (e.g., `1.0.0` to `1.1.0`)
2. Make your changes
3. Submit again (same process)

Use semantic versioning:
- **1.0.x** — Bug fixes and small tweaks
- **1.x.0** — New features (backward compatible)
- **x.0.0** — Breaking changes (rare for single agents)

---

# Part IV: Going Deeper (Still No CS Degree Required)

---

## Chapter 13: Making Agents That Connect to Things

### The Environment Variable Pattern

Many useful agents need to connect to external services — your CRM, email system, project management tool, etc. These connections require API keys or credentials.

In RAPP, credentials are handled through **environment variables**. This means:

1. Your API key lives on YOUR machine (not in the code)
2. The agent asks for the key by name when it runs
3. If the key isn't there, the agent returns a helpful error message

### Setting Environment Variables

**On Mac/Linux:**
Open Terminal and type:
```
export MY_API_KEY="your-key-here"
```

**On Windows:**
Open Command Prompt and type:
```
set MY_API_KEY=your-key-here
```

**Permanently (so it survives restarts):**
Add the line to your shell profile (`.bashrc`, `.zshrc`, or Windows Environment Variables in System Settings).

### How Agents Use Environment Variables

In the agent code, it looks like this:
```python
api_key = os.environ.get("MY_API_KEY", "")
if not api_key:
    return "Error: Please set the MY_API_KEY environment variable."
```

The key thing: agents NEVER hardcode credentials. And they always tell you what's missing.

### Example: Building a Simple API Agent

Want an agent that connects to a service? Tell the AI:

> "Write me a RAPP agent that calls the [Service Name] REST API. It should accept a query parameter and return the API response. The API key should come from the [SERVICE]_API_KEY environment variable. If the key is missing, return an error message."

The AI will generate the code. You paste it in the Workbench. Validate. Done.

---

## Chapter 14: The Holo Card System — Making Your Agent Collectible

### How Cards Are Generated

Every agent gets a card automatically. The CardSmith agent uses your agent's name to generate a deterministic card with:

- Unique artwork (procedurally generated from the agent name)
- Mana cost and colors (based on category and complexity)
- Creature type (based on what the agent does)
- Abilities (derived from the agent's operations)
- Flavor text (from the agent description)
- Power/toughness stats (based on code metrics)

### Influencing Your Card

You can't directly design your card, but you can influence it:

- **Name** affects the artwork pattern
- **Category** affects the card colors
- **Description** becomes flavor text
- **Tags** influence creature type
- **Code complexity** affects power/toughness

Choose a memorable name and a vivid description, and your card will stand out in the collection.

### Why Cards Matter for Business

Cards aren't just fun. They're a communication tool:

- **Client demos**: Show agents as collectible cards instead of boring file lists
- **Team dashboards**: Display deployed agents as a card deck
- **Onboarding**: New team members browse agent cards to learn what's available
- **Presentations**: Present mode turns any deck into a slideshow

---

## Chapter 15: Running Your Own Agent Store

### What Is Federation?

RAR is a template repository. You can create your own copy and run it independently. This is called **federation**.

Your private store can:

- Host agents only your team can see
- Pull public agents from the main store
- Run completely air-gapped (no internet required)
- Submit agents back to the main store if you choose

### Why Federation Matters

**For enterprises**: Keep proprietary agents internal while still using community agents.

**For teams**: Curate a specific set of agents for your use case.

**For educators**: Create a private store for a class or workshop.

### Setting It Up

1. Go to the RAR GitHub repository
2. Click "Use this template" to create your own copy
3. The setup automation runs automatically
4. Edit `rar.config.json` with your settings
5. Add your agents to `agents/@yournamespace/`

Your store will run at `https://yourusername.github.io/your-repo/` — free hosting courtesy of GitHub Pages.

---

## Chapter 16: The Community — Forum, Wiki, and Getting Help

### Rappterpedia

Rappterpedia is the community knowledge base for the RAPP ecosystem. It has two parts:

**Wiki** — Articles covering everything from beginner guides to deep architecture dives. Categories include Getting Started, Agents, Architecture, Integrations, Best Practices, Troubleshooting, Federation, and Community.

**Forum** — Discussion threads organized into channels: General Discussion, Help & Support, Agent Showcase, Ideas & Requests, Bug Reports, and Meta & Governance.

### Getting Help

If you're stuck:

1. **Search the wiki first** — Most common questions are already answered
2. **Search the forum** — Someone probably had the same issue
3. **Post in Help & Support** — The community is friendly and responsive
4. **Check the Agent Store Workbench validator** — It catches most manifest issues

### Contributing Back

You don't need to write code to contribute:

- **Vote** on agents you use and like
- **Review** agents you've tried
- **Write wiki articles** about your experience
- **Answer questions** in the forum
- **Share your decks** — curated agent collections help others discover useful tools

The community runs on participation. Every vote, review, and forum post makes the ecosystem better for everyone.

---

# Part V: Real-World Playbooks

---

## Chapter 17: The Sales Team Playbook

### Your Agent Stack

| Agent | What It Does | Category |
|-------|-------------|----------|
| Deal Desk | B2B sales process management | Sales |
| Recon Deck | Prospect research and briefing | Sales |
| Proposal Copilot | Generates competitive proposals | Sales |
| Sales Assistant | Meeting prep and follow-up | Sales |
| Email Drafting | Professional email composition | Productivity |
| Demo Script Generator | Creates demo scripts and flows | Productivity |

### Workflow: New Prospect

1. **Recon Deck**: "Research Acme Corp for a discovery call"
   - Returns: Company overview, key contacts, recent news, competitive landscape

2. **Demo Script Generator**: "Create a demo flow for a manufacturing company interested in quality control"
   - Returns: Step-by-step demo script with talking points

3. **Proposal Copilot**: "Generate a proposal for Acme Corp's quality control needs"
   - Returns: Full proposal with pricing models and win themes

4. **Email Drafting**: "Draft a follow-up email after a demo with Acme Corp"
   - Returns: Professional follow-up with next steps

### Building a Sales Deck

Create a deck called "Sales Stack" with all your go-to agents. Use Present mode when onboarding new sales reps — each card explains what the agent does and when to use it.

---

## Chapter 18: The Small Business Playbook

### Your Agent Stack

| Agent | What It Does |
|-------|-------------|
| Customer Loyalty & Rewards | Points tracking, program management |
| Email Drafting | Professional communications |
| General Ask HR | HR questions and policy lookup |
| Invoice Processing | Invoice data extraction and validation |
| MeetingSummary (your custom build!) | Meeting notes to action items |

### Getting Started

1. Open the Agent Store
2. Search for agents in your industry vertical (the @aibast-agents-library has 104 templates)
3. Install 3-5 agents that match your daily work
4. Create a deck called "Daily Drivers"
5. Use them through the chat interface or Virtual Brainstem

### The 80/20 Rule

You don't need 50 agents. Start with 3-5 that handle your most repetitive tasks. Master those. Then expand.

The meeting summary agent from Chapter 10? That alone saves 15 minutes per meeting. Three meetings a day, five days a week — that's almost 4 hours saved per week from one agent.

---

## Chapter 19: The Creative Professional Playbook

### Your Agent Stack

| Agent | What It Does |
|-------|-------------|
| Architecture Diagram | Generates visual system diagrams |
| PowerPoint Generator | Creates presentation slides |
| Content Creation agents | Blog posts, social media, copywriting |
| Rappterbook | Document generation and management |

### Creative Workflow

1. **Brainstorm** with the chat interface — describe your project
2. **Draft** using content agents — get a first pass quickly
3. **Visualize** with the diagram and presentation agents
4. **Refine** by feeding the output back with specific feedback

The key insight for creative work: agents give you a starting point, not a finished product. They eliminate the blank page problem. You edit and refine from a draft instead of creating from nothing.

---

## Chapter 20: The Enterprise Team Playbook

### Federation First

For enterprise teams, start with federation:

1. Create a private RAR instance for your organization
2. Pull public agents you've vetted
3. Build proprietary agents under your company namespace
4. Set up CI/CD for automated testing and deployment

### Governance

Use the quality tier system for internal governance:

- **Community tier** — Any team member can publish (dev/test)
- **Verified tier** — IT reviews and approves (staging)
- **Official tier** — Production-ready, maintained by platform team

### Compliance

- Agents never hardcode credentials (uses environment variables)
- The store works offline and air-gapped
- Local-first storage (IndexedDB) — nothing leaves the device
- Full audit trail through GitHub Issues and PR history
- Federation keeps proprietary agents internal

### Scale

Start with one team. Build 5-10 agents. Prove the value. Then expand to other teams through federation. Each team gets their own namespace but can share agents through the internal store.

---

# Appendix A: Glossary

**Agent** — A single-file Python program that takes inputs and returns a text result.

**BasicAgent** — The base class every agent inherits from. Provides standard capabilities.

**Card** — Visual representation of an agent. Business (professional) or Holo (trading card) styles.

**Deck** — A named collection of agent cards. Used for organization and presentations.

**Federation** — Running your own copy of the agent store, optionally connected to the main store.

**Manifest** — The `__manifest__` metadata dictionary in every agent file. Contains name, version, description, etc.

**Namespace** — Your publisher identity (`@yourname`). Tied to your GitHub username.

**Perform** — The `perform(**kwargs)` method. The heart of every agent — takes inputs, returns a string.

**Quality Tier** — Trust level: Community, Verified, Official, or Frontier.

**RAR** — RAPP Agent Registry. The open agent store and ecosystem.

**RAPP** — The broader AI agent platform that agents are built for.

**Registry** — The `registry.json` index of all agents. Auto-generated by the build system.

**Single-File Principle** — Every agent is one `.py` file. Documentation, metadata, and code in one place.

**Workbench** — Browser-based agent development environment built into the store.

---

# Appendix B: Quick Reference Card

### Creating an Agent

1. Open Agent Store > Workbench
2. Modify the template manifest
3. Write or AI-generate the perform() method
4. Validate
5. Download or Submit

### Required Manifest Fields

```
schema, name, version, display_name,
description, author, tags, category
```

### Agent Name Format

```
@yourname/agent-slug
(lowercase kebab-case for the slug)
```

### Categories

```
core | pipeline | integrations | productivity | devtools
```

### Quality Tiers

```
Frontier > Community > Verified > Official
```

### The Golden Rules

1. One file. Always.
2. perform() returns a string. Always.
3. No secrets in code. Use environment variables.
4. Handle errors gracefully. Return a message, don't crash.
5. No network calls in __init__(). Keep startup fast.

---

# Appendix C: Troubleshooting — When Things Don't Work

### "Validation says my manifest is missing"

Your `__manifest__` dict must be at the top level of the file, not inside a class or function. It should be right after the docstring.

### "My agent name is rejected"

Format must be `@publisher/slug` where:
- publisher = your GitHub username (lowercase)
- slug = lowercase letters, numbers, and hyphens only

### "perform() returns None"

Your perform method must explicitly `return` a string. If you forget the return statement, Python returns None by default.

### "display_name mismatch"

The `display_name` in your manifest must exactly match `self.name` in your class. Copy-paste to be safe.

### "Agent works in Workbench but not after download"

Make sure you're running Python 3.11+. Check with `python --version` in your terminal. Older versions may not support some syntax.

### "Environment variable not found"

Set it before running the agent:
- Mac/Linux: `export VAR_NAME="value"`
- Windows: `set VAR_NAME=value`

### "I'm completely stuck"

1. Search Rappterpedia wiki
2. Post in the Help & Support forum
3. Look at a working agent in the same category for reference
4. Ask an AI assistant: "Why doesn't this RAPP agent work?" and paste your code

---

## Afterword

You made it.

You've gone from "what's an agent?" to understanding how to browse, install, build, test, and publish AI agents — without writing code from scratch, without a computer science background, without any of the traditional barriers.

The RAPP ecosystem is designed to be exactly this accessible. One file. One idea. One AI assistant to help with the implementation.

The agents you build don't need to be perfect. They don't need to be clever. They just need to be useful — to you, to your team, to your customers. Start with one small agent that saves you 15 minutes a day. Then build another. Then share them.

The best tools aren't built by the most technical people. They're built by the people who understand the problem best.

That's you.

Now go build something.

---

*Single file. Single principle. Single source of truth.*

---

## About the Author

Kody Wildfeuer is the creator of the RAPP Agent ecosystem and the RAR (RAPP Agent Registry). He builds tools that make AI accessible to everyone, not just engineers. When he's not shipping agents, he's probably thinking about how to make the next thing simpler.

Find the Agent Store at: https://kody-w.github.io/RAR/

Find Rappterpedia at: https://kody-w.github.io/RAR/rappterpedia/
