---
layout: page
title: Research
permalink: /research/
---

<!--
  TODO(Joseph): this is my draft of the arc you described, now reconciled
  against your four CVs. Facts should hold; the framing is my reading of your
  work rather than your words, so revise freely. Two things I could not get
  from the CVs are marked in [brackets] below.
-->

My work has moved through three areas: optimization first, then statistical and
mathematical modelling, and now explainable AI. The path was not planned. Each
move came from something concrete — a dataset that happened to be available, a
community of people worth working with, a problem encountered in the course of
a thesis — rather than from a strategy set out in advance.

What has stayed constant is narrower than a grand theme. I am interested in
what can honestly be inferred from the data actually to hand, and in whether
the people expected to act on a result have any reason to trust it.

For the formal record, see [Publications]({{ '/publications/' | relative_url }}).

## Optimization under constraint

The earliest work was concerned with allocating scarce resources well. My MSc
thesis at KNUST, *Efficient Irrigation and Cropping Patterns — A Linear
Programming Approach*, set the pattern, and the papers that followed applied it
directly: optimal allocation of irrigation water at the Kpong Irrigation
Project, and optimal crop selection among small-scale farms in the Fanteakwa
district. Each had the same structure — a decision-maker with real constraints,
a limited resource, and a measurable objective. Ghanaian smallholder
agriculture is an unforgiving setting for this kind of analysis, because a
recommendation that ignores what a farmer can actually do is worth nothing
regardless of its elegance.

The habit of starting from what a decision-maker can actually do, rather than
from the method, has stayed with me.

## Statistical and mathematical modelling

The modelling work extends the same reasoning from decision to inference. In
public health this has meant identifying the drivers of intermittent preventive
treatment of malaria during pregnancy using a negative-binomial generalized
linear model, examining correlates of hepatitis B infection among antenatal
clinic attendees at the Volta Regional Hospital in Ho, and forecasting
caesarean-section births nationally. In macroeconomics it has meant modelling
Ghana's macroeconomic variables through principal component analysis and
multiple linear regression, and tracing the dynamic response of commodity
prices to monetary-policy shocks.

The COVID-19 pandemic pulled these threads together. I worked with the WHO, the
Ghana Health Service and the University of Health and Allied Sciences on the
instruments and databases behind Ghana's national survey of COVID-19
behavioural insights, which became the PLOS ONE paper on knowledge among
Ghanaians. Alongside it, my own work compared a single forecast model against a
multi-model ensemble for Ghana's case trajectory.

The honest account of how that work began is that the data was there. Ghana's
case counts were published daily, and I started exploring them to see what they
would support. The projections paper, and the comparison of a single forecast
model against a multi-model ensemble, came out of that exploration rather than
out of a plan. I mention this because research narratives are usually written
backwards, and the backwards version would be tidier and less true.

## From NLP to explainable AI

This strand started with **NLP Ghana**, a collaboration addressing a
straightforward inequity: the tools that make modern natural language
processing useful were not built for the languages most Ghanaians speak. I was
one of twenty-seven contributors to the resulting work — an English–Twi
parallel corpus for machine translation, contextual text embeddings for Twi,
and a broader survey of NLP for Ghanaian languages. Working on low-resource
languages is a useful education in what deep learning does when the data is
thin, which is not what the benchmarks suggest.

That work led me into the architecture itself. My PhD thesis at UTAS Navrongo,
*Modified Hexpo — An Improved Vanishing-Gradient Mitigation Activation Function
for Neural Networks*, proposes the Shifted Hexpo activation function, evaluated
on cervical-cancer classification using the SIPaKMeD dataset across ResNet,
DenseNet, and lightweight CNN architectures. Lightweight matters for a
practical reason: a model that needs a data centre is not available to a
district hospital, so computational efficiency is a precondition for the model
being used at all rather than an optimisation nicety.

The thesis is also where the current interest began. Alongside the accuracy and
gradient-stability results, I used Grad-CAM to show which regions of an image
were driving each prediction — and the question of whether a model can account
for its own output has held my attention since. That is where my work now sits:
explainable AI, and the broader question of what it takes for a model to be
trusted by the people expected to act on it. Several projects in this area are
underway, and I will write about them here as they develop.

## Climate and health

The newest strand joins the health work to climate. I hold a CLEAR PhD
Scholarship — Climate and Health Evaluation for Adaptive Resilience — at the
Kintampo Health Research Centre, and have trained with the Centre on building a
climate cohort to monitor the health impacts of climate change in Ghana. The
methodological question is a familiar one in a new setting: measuring an
exposure that is diffuse, gradual, and unevenly distributed, and attributing
health outcomes to it credibly enough to justify adaptation spending.

---

## Data and code

Public code lives on [GitHub](https://github.com/{{ site.github_username }}).
Recent work includes an
[eCedi CBDC prototype](https://github.com/Joseph1Otoo/eCedi-cbdc-prototype) — a
central-bank digital-currency implementation with issuance controls and
KYC-gated transfers, and a Python analytics layer computing net issuance, money
velocity, and Herfindahl–Hirschman holder concentration.
