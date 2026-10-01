---
name: home
version: 1.0.0
description: Household lists, download janitor, bookmarks, and reading queue.
keywords: [grocery, groceries, chore, chores, download, downloads folder, bookmark, reading, household, shopping list]
---

# Home Skill

Household and file-janitor butler. Loaded lazily on grocery, chore,
download-cleanup, bookmark, or reading-queue prompts.

## Tools

| Tool | Tier | Purpose |
| ---- | ---- | ------- |
| `add_grocery_item` | 1 | Add an item to the grocery list. |
| `add_household_chore` | 1 | Add a household chore. |
| `get_household_summary` | 0 | Summarize household state. |
| `scan_downloads_folder` | 0 | Scan downloads for clutter. |
| `organize_downloads` | 2 | Organize downloads (mutating). |
| `add_bookmark` | 1 | Save an auto-tagged bookmark. |
| `add_to_learning_queue` | 1 | Queue an article for later reading. |
