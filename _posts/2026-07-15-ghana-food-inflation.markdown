---
layout: post
title:  "Food was Ghana's tame inflation component — until 2020"
date:   2026-07-15 09:00:00 +0000
categories: inflation ghana
---

Ask most people what drives inflation in Ghana and the answer comes back
quickly: food. It is the largest single item in the household basket, it is what
people notice at the market, and it is what the headline number is assumed to be
made of.

For fourteen straight years, the data said otherwise. Between 2006 and 2019,
food inflation ran **below** non-food inflation in every single year — usually by
a wide margin. Then 2020 happened.

![Year-on-year food and non-food inflation in Ghana, monthly from January 2006 to August 2020. Non-food runs above food for almost the whole period, peaking near 25 per cent in 2014-16 while food sits near 7 per cent. The two converge from 2018 and food spikes above non-food in April 2020.]({{ '/images/ghana-food-vs-nonfood-inflation.svg' | relative_url }})

## The gap, and how wide it got

The Bank of Ghana publishes food and non-food inflation as separate series. Over
the 176 months from January 2006 to August 2020, food inflation averaged 8.7%
and non-food 15.5% — a gap of nearly seven percentage points sustained across
fourteen years. Headline inflation sits between the two components in 99% of
months, which is a useful sanity check that we are reading the series correctly
rather than an artefact.

The gap was not stable. It widened sharply through the middle of the last
decade, reaching **18.9 percentage points in August 2014** — the widest on
record — and averaging nearly 16 points across 2015. In that year food inflation
was 7.5% while non-food ran at 23.3%. A household buying mostly food and a
household buying mostly everything else were living in different economies.

| Year | Food | Non-food | Gap |
|---|---:|---:|---:|
| 2006 | 9.9% | 13.0% | −3.1 |
| 2008 | 15.1% | 17.5% | −2.4 |
| 2010 | 7.7% | 15.6% | −8.0 |
| 2012 | 4.9% | 12.9% | −7.9 |
| 2014 | 6.8% | 21.8% | −15.0 |
| 2015 | 7.5% | 23.3% | **−15.8** |
| 2016 | 8.7% | 22.5% | −13.9 |
| 2018 | 7.9% | 10.7% | −2.8 |
| 2019 | 7.6% | 9.2% | −1.6 |
| 2020 | 11.6% | 8.5% | **+3.1** |

*Annual means of the monthly year-on-year series. 2020 covers January–August
only. Full annual detail is in the [chart
script](https://github.com/Joseph1Otoo/Joseph1otoo.github.io/blob/gh-pages/scripts/make_inflation_chart.py),
which prints every figure quoted here.*

Why would the non-food basket run hotter for a decade? The plausible account is
that non-food carries Ghana's imported and administered costs — fuel, transport,
utilities, and anything priced against the dollar. The gap is at its widest in
2014–2016, which is exactly the cedi's worst stretch and the period of large
utility tariff adjustments. Food, grown and traded largely domestically, was
partly insulated from that.

I want to be careful here. That is a hypothesis consistent with the timing, not
a result. This post is describing two series, not identifying a mechanism, and
the correspondence between the gap and the exchange rate is something I have
looked at by eye rather than estimated.

## 2020

In 2020 the ordering flipped. Food inflation rose to 11.6% while non-food fell
to 8.5% — the first year in the series where food was the hotter component.

The flip itself is less remarkable than its size. Food had briefly edged above
non-food before: July 2007, November 2018, and three months of 2019. But those
were scratches, the largest of them 1.5 percentage points. **In April and May
2020, food ran 6.7 points above non-food** — more than four times any previous
excess. Across the whole 176-month record, food exceeded non-food in only twelve
months, and seven of them are in 2020.

The timing is hard to miss. Ghana's partial lockdown of Accra and Kumasi ran from
30 March to 20 April 2020. April and May are the two extreme months. Restricted
movement, disrupted market days, and buying ahead of an uncertain lockdown are
the obvious candidates, and they all push in the same direction.

Again: the timing is suggestive, and I am not claiming more than that. A
month-level correspondence between a policy and a price series is a place to
start an analysis, not the conclusion of one.

## Why it matters

If food is normally Ghana's *stabilising* component, then a food shock does not
just raise the headline number — it removes the thing that was holding it down.
That has a distributional edge. Food is a much larger share of spending for poor
households than for rich ones, so an inflation episode led by food is felt more
sharply at the bottom of the distribution than the headline rate suggests.

It also has a measurement implication for anyone forecasting Ghanaian inflation.
A model fitted on 2006–2019 has learned that food is the tame component and that
non-food carries the variance. April 2020 is exactly the kind of month that
breaks that assumption, and a model that cannot express the reversal will miss
it precisely when the number matters most.

The series here ends in August 2020, so this is a description of what happened at
the start of the pandemic rather than of how it resolved. Whether the reversal
persisted is the obvious next question, and it needs the data since.

*Data: Bank of Ghana. The chart and every figure quoted are reproducible from
[`scripts/make_inflation_chart.py`](https://github.com/Joseph1Otoo/Joseph1otoo.github.io/blob/gh-pages/scripts/make_inflation_chart.py).*
