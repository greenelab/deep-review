# Referencing machinery for this review

For information on how to add references using our extended markdown, see the
[contributing guidelines](../CONTRIBUTING.md#markdown).

## Contents

[`tags.tsv`](tags.tsv) contains manually created reference tags.
You should edit this table to contain any new citation tags you create.

[`generated`](generated) contains auto-generated files related to referencing.
You should not edit these files manually.

[`manual-references.json`](manual-references.json) contains manually managed
reference data, which overrides the automatically extracted data.

## Reference overrides
Overriding the automatically extracted reference data should be reserved for references that contain errors, which is most common for `[@url:]` references.
Create a new record in [`manual-references.json`](manual-references.json) in [CSL JSON](http://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html) format.
The record must contain the field `"standard_citation"` with the appropriate reference identifier as the value.
The identifier can be obtained from the `standard_citation` column of `processed-citations.tsv`, which is located in the base directory of the `references` branch or in the `references/generated` subdirectory if you build the manuscript locally.
`manual-references.json` contains the record `"standard_citation": "url:https://github.com/greenelab/manubot-rootstock"` as an example.
