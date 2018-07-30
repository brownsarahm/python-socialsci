---
layout: page
permalink: /exercise-list/
---

{%for ex in site.exercises %}

{% include exercise_output.html keyword=ex.keyword num=forloop.index %}
{%endfor%}
