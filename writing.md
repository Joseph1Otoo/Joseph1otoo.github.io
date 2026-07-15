---
layout: page
title: Writing
permalink: /writing/
---

Shorter analyses of current data — the kind of thing that does not belong in a
journal but is worth saying. For peer-reviewed work, see
[Publications]({{ '/publications/' | relative_url }}).

{%- if site.posts.size == 0 %}

*Nothing here yet.*

{%- else %}

<ul class="writing-list">
  {%- for post in site.posts %}
  <li class="writing-item">
    <span class="writing-date">
      <time datetime="{{ post.date | date_to_xmlschema }}">
        {{ post.date | date: "%-d %B %Y" }}
      </time>
    </span>
    <span class="writing-title">
      <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
    </span>
    {%- if post.categories.size > 0 %}
    <span class="writing-tags">
      {%- for c in post.categories %}<span class="writing-tag">{{ c }}</span>{% endfor -%}
    </span>
    {%- endif %}
    {%- if post.excerpt %}
    <span class="writing-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncate: 200 }}</span>
    {%- endif %}
  </li>
  {%- endfor %}
</ul>

{%- endif %}
