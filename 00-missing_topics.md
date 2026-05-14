---
title: Missing Topics
created: 2026-05-14
updated: 2026-05-14
kind: moc
status: in_progress
area:
- quotes
tool: []
source: ''
author: ''
url: ''
tags: []
---

# Missing Topics

```dataview
TABLE author
FROM "02-Active/Quotes"
WHERE kind = "note" AND !topics
SORT file.name ASC
```
