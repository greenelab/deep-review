# Opportunities and obstacles for deep learning in biology and medicine

This article is also available as a [preprint on bioRxiv](https://doi.org/10.1101/142760).

{% for author in authors.authors -%}
  {{author.name}}<sup>{{author.affiliation}}{{author.symbol}}</sup>{{ ',' if not loop.last }}
{% endfor %}

<sup>*</sup> Author order was determined with a randomized algorithm

<sup>†</sup> To whom correspondence should be addressed: {{authors.corresponding}}

{% for affiliation in authors.affiliations -%}
  {{affiliation.index}}. {{affiliation.institution}}
{% endfor %}
