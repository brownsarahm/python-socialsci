{% assign cur_ex = site.exercises | where:"keyword", {{ include.keyword }} | first %}
test text
{{ include.keyword }}
{{cur_ex.content}}
{{cur_ex.output}}
