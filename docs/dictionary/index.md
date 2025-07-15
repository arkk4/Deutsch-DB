---
icon: material/notebook-multiple
hide:
  - navigation
---
<!-- docs/dictionary/index.md -->
# Словник — картки
{% for term in terms() %}
<div class="card-wrapper" data-url="{{ term.url }}" data-part-of-speech="{{ term.part_of_speech }}"{% if term.part_of_speech == 'nomen' and term.artikel %} data-artikel="{{ term.artikel | lower }}"{% endif %}>
<div class="card">
    <strong><a href="{{ term.url }}">{{ term.title }}</a></strong>
    
    {# Решта полів #}
    {% if term.artikel and term.part_of_speech == 'nomen' %}
    <br><span class="artikel-{{ term.artikel | lower }}"><em><strong>{{ term.artikel }}</strong></em></span> <em>{{ term.german }}</em>
    {% elif term.artikel %}
    <br><em><strong>{{ term.artikel }}</strong></em> <em>{{ term.german }}</em>
    {% endif %}
    
    {% if term.translate %}
    <br><strong>{{ term.translate }}</strong>
    {% endif %}
    
    {% if term.verb_type %}
    <br><em>{{ term.verb_type }}</em>
    {% endif %}
</div>
</div>
{% endfor %}