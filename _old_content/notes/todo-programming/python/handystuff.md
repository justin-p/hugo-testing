---
title: "Handystuff"
date: 2020-03-06T11:23:52+01:00
draft: false
---

### get current function name

```python
functionname = inspect.stack()[0][3]
```

### get callers name of current function

```python
functionname = inspect.stack()[1][3]
```
