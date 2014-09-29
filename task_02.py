#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal

def str_to_bool(INTERVAL, RATE = None, TOTAL = None, PRINCIPAL, DURATION, PREQUALIFICATION):
    """calculator function rewritten. """


# Function conversion work you do should start here
INTERVAL = 12
RATE = None
TOTAL = None

if PRINCIPAL >= 0 and PRINCIPAL <= 199999:
    if DURATION >= 1 and DURATION <= 15:
        if PREQUALIFICATION:
            RATE = '0.0363'
        else:
            RATE = '0.0465'
    elif DURATION >= 16 and DURATION <= 20:
        if PREQUALIFICATION:
            RATE = '0.0404'
        else:
            RATE = '0.0498'
    elif DURATION >= 21 and DURATION <= 30:
        if PREQUALIFICATION:
            RATE = '0.0577'
        else:
            RATE = '0.0639'
elif PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
    if DURATION >= 1 and DURATION <= 15:
        if PREQUALIFICATION:
            RATE = '0.0302'
        else:
            RATE = '0.0398'
    elif DURATION >= 16 and DURATION <= 20:
        if PREQUALIFICATION:
            RATE = '0.0327'
        else:
            RATE = '0.0408'
    elif DURATION >= 21 and DURATION <= 30:
        if PREQUALIFICATION:
            RATE = '0.0466'
elif PRINCIPAL >= 1000000:
    if DURATION >= 1 and DURATION <= 15:
        if PREQUALIFICATION:
            RATE = '0.0205'
    elif DURATION >= 16 and DURATION <= 20:
        if PREQUALIFICATION:
            RATE = '0.0262'

if RATE is not None:
    RATE = decimal.Decimal(R)
    TOTAL = PRINCIPAL * ((1 + RATE / INTERVAL) ** (INTERVAL * DURATION))
    TOTAL = int(round(TOTAL))


