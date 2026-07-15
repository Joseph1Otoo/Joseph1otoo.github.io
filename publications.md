---
layout: page
title: Publications
permalink: /publications/
---

{%- if site.scholar_url or site.orcid_url -%}
<p class="pub-profiles">
  Full list also on
  {%- if site.scholar_url %} <a href="{{ site.scholar_url }}">Google Scholar</a>{% endif -%}
  {%- if site.scholar_url and site.orcid_url %} and{% endif -%}
  {%- if site.orcid_url %} <a href="{{ site.orcid_url }}">ORCID</a>{% endif -%}.
</p>
{%- endif -%}

{%- comment -%}
  site.data.publications is nil while the YAML file holds only comments, so
  guard on the raw value before filtering.
{%- endcomment -%}
{%- assign raw = site.data.publications -%}
{%- if raw -%}
  {%- assign pubs = raw | where_exp: "p", "p.title" -%}
{%- else -%}
  {%- assign pubs = "" | split: "," -%}
{%- endif -%}

{%- if pubs.size == 0 -%}

*This list is being compiled. In the meantime, please see my
[Google Scholar profile]({{ site.scholar_url | default: '#' }}) — or
[email me]({{ 'mailto:' | append: site.email }}) and I will send you anything
you are looking for.*

{%- else -%}

{%- comment -%}
  group_by returns `name` as a string, so this is a string sort. That is fine
  for four-digit years, and it puts the "0" (undated) group last on reverse.
{%- endcomment -%}
{%- assign years = pubs | group_by: "year" | sort: "name" | reverse -%}
{%- for year in years %}

## {% if year.name == "0" %}Undated{% else %}{{ year.name }}{% endif %}

<ul class="pub-list">
{%- assign sorted = year.items | sort: "title" -%}
{%- for p in sorted %}
  <li class="pub">
    <span class="pub-title">
      {%- if p.url -%}
        <a href="{{ p.url }}">{{ p.title }}</a>
      {%- else -%}
        {{ p.title }}
      {%- endif -%}
    </span>
    {%- if p.authors %}
    <span class="pub-authors">
      {{- p.authors | markdownify | remove: '<p>' | remove: '</p>' -}}
      {%- if p.authors_truncated %} <span class="pub-etal" title="Full author list to be completed">et al.</span>{% endif -%}
    </span>
    {%- endif %}
    {%- if p.venue %}
    <span class="pub-venue">
      <em>{{ p.venue }}</em>{% if p.volume %}, {{ p.volume }}{% endif %}.
    </span>
    {%- endif %}
    {%- if p.note %}
    <span class="pub-note">{{ p.note }}</span>
    {%- endif %}
    <span class="pub-links">
      {%- if p.doi %}<a href="https://doi.org/{{ p.doi }}">doi</a>{% endif -%}
      {%- if p.pdf %} <a href="{{ p.pdf | relative_url }}">pdf</a>{% endif -%}
      {%- if p.type and p.type != 'journal' %} <span class="pub-type">{{ p.type }}</span>{% endif -%}
    </span>
  </li>
{%- endfor %}
</ul>

{%- endfor -%}
{%- endif -%}
