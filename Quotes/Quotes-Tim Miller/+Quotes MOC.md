---
title: +Quotes MOC
url: 
tags:
  - Meta
creation date: 2024-02-09
modification date: 2024-03-06
Author: 
date: 2023-03-22T09:35
---

# +Quotes MOC

## All Authors

```dataviewjs
var quotes = dv.pages('#quote and !"Umami/Templates"');
dv.paragraph("Total quote authors: " + quotes.length);
```

```dataview
List
from #quote and !"Umami/Templates"
Sort file.name asc
```
