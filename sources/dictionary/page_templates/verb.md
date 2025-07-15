---
title: {{ meta.title }}
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
    - imperativ: 
      - du: {{ meta.konjugation[1]['imperativ'][0]['du'] }}
      - wir: {{ meta.konjugation[1]['imperativ'][1]['wir'] }}
      - ihr: {{ meta.konjugation[1]['imperativ'][2]['ihr'] }}
      - sie: {{ meta.konjugation[1]['imperativ'][3]['sie'] }}
partizip2: {{ meta.partizip2 }}
hilfsverb: {{ meta.hilfsverb }}
tags: {{ meta.tags }}
---

# {{ meta.title }}

**Німецькою:** {{ meta.title }}

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
**Partizip II:** {{ meta.partizip2 }} {{ meta.hilfsverb }}
{% endif %}

## Imperativ
|   Subjekt     |   Form    |
|--------|-------|
| du     | {{ meta.konjugation[1]['imperativ'][0]['du'] }} |
| wir    | {{ meta.konjugation[1]['imperativ'][1]['wir'] }} |
| ihr    | {{ meta.konjugation[1]['imperativ'][2]['ihr'] }} |
| Sie| {{ meta.konjugation[1]['imperativ'][3]['sie'] }} |


