---
icon: material/notebook-multiple
hide:
  - navigation
---
<!-- docs/dictionary/index.md -->
# Словник
{% for term in terms() %}
<div class="card-wrapper" data-url="{{ term.url }}" data-part-of-speech="{{ term.part_of_speech }}"{% if term.part_of_speech == 'nomen' and term.artikel %} data-artikel="{{ term.artikel | lower }}"{% endif %}>
<div class="card">
    <a href="{{ term.url }}">{{ term.title }}</a> <em>{{ term.part_of_speech }}</em> {% if term.verb_type %}<em><strong>{{ term.verb_type }}</em></strong> {% if term.hilfsverb %}<em>{{ term.hilfsverb }}</em> {% endif %}
    {% endif %}
    
    {% if term.artikel and term.part_of_speech == 'nomen' %}
    <br><span class="artikel-{{ term.artikel | lower }}"><em><strong>{{ term.artikel }}</strong></em></span> <em>{{ term.title }}</em>
    {% elif term.artikel %}
    <br><em><strong>{{ term.artikel }}</strong></em> <em>{{ term.title }}</em> 
    {% endif %}
    {% if term.translate %}
    <br>{{ term.translate }}
    {% endif %}
</div>
</div>
{% endfor %}