---
title: 00-missing_quotes
created: 2026-05-14
updated: 2026-05-17
kind: moc
status: in_progress
area:
  - quotes
tool: []
source: ""
author: ""
url: ""
tags: []
---

# Missing Quotes

```dataview
TABLE author
FROM "02-Active/Quotes"
WHERE kind = "note" AND !quote
SORT file.name ASC
```
