---
title: 00-missing_topics
created: 2026-05-14
updated: 2026-05-14
tags: []
kind: moc
status: in_progress
area:
- quotes
tool: []
source: ''
author: ''
url: ''
---

# Missing Topics

```dataview
TABLE author
FROM "02-Active/Quotes"
WHERE kind = "note" AND !topics
SORT file.name ASC
```
