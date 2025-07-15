---
title: {{ meta.title }}
german: {{ meta.german }}
translate: {{ meta.translate }}
part_of_speech: {{ meta.part_of_speech }}
verb_type: {{ meta.verb_type }}
konjugation: 
    - präsens: 
      - ich: {{ meta.konjugation[0]['präsens'][0]['ich'] }}
      - du: {{ meta.konjugation[0]['präsens'][1]['du'] }}
      - er_sie_es: {{ meta.konjugation[0]['präsens'][2]['er_sie_es'] }}
      - wir: {{ meta.konjugation[0]['präsens'][3]['wir'] }}
      - ihr: {{ meta.konjugation[0]['präsens'][4]['ihr'] }}
      - sie_sie: {{ meta.konjugation[0]['präsens'][5]['sie_sie'] }}
partizip2: {{ meta.partizip2 }}
tags: {{ meta.tags }}
---

# {{ meta.title }}

**Німецькою:** {{ meta.german }}

**Переклад:** {{ meta.translate }}

**Частина мови:** {{ meta.part_of_speech }}


{% if meta.konjugation %}
## Konjugation (Präsens)
|   Subjekt     |   Form    |
|--------|-------|
| ich    | {{ meta.konjugation[0]['präsens'][0]['ich'] }} |
| du     | {{ meta.konjugation[0]['präsens'][1]['du'] }} |
| er/sie/es | {{ meta.konjugation[0]['präsens'][2]['er_sie_es'] }} |
| wir    | {{ meta.konjugation[0]['präsens'][3]['wir'] }} |
| ihr    | {{ meta.konjugation[0]['präsens'][4]['ihr'] }} |
| sie/Sie| {{ meta.konjugation[0]['präsens'][5]['sie_sie'] }} |
{% endif %}


{% if meta.partizip2 %}
**Partizip II:** {{ meta.partizip2 }}
{% endif %}

