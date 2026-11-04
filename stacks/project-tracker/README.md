# Project Tracker

A local-first tracker for a portfolio of AI-agent projects and their MVP statements. The web UI is a 1:1 clone of the aibast-agents-library project-tracker tool; the bundled ProjectTracker agent manages the same portfolio headlessly over /chat. Both speak the tool's native projectTrackerData JSON, so exports and imports round-trip with it. Self-contained and stdlib-only: the UI works offline via localStorage, and unifies with the agent's on-device store when the rapplication's local server is running.

Moved here from the RAPP Store (now an alias of RAR); the original page keeps working: https://kody-w.github.io/RAPP_Store/#project_tracker
