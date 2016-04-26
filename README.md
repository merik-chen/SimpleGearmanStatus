Simple Gearman worker status
===================================

##### Get worker status on Gearman in python.

### Req. Packages:

    None (std. packages)

### Demo:

    python SimpleGearmanStatus/SimpleGearmanStatus.py

### Usage:

```python
    >>> import SimpleGearmanStatus

    >>> SGS = SimpleGearmanStatus.SimpleGearmanStatus()

    >>> print(SGS.get_all_status())

    >>> print(SGS.get_status(JOB_NAME))
```
