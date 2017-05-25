## Methods

### Continuous collaborative manuscript drafting

We recognized that deep learning in precision medicine is a rapidly developing area.
Hence, diverse expertise was required to provide a forward-looking perspective.
Accordingly, we collaboratively wrote this review in the open, enabling anyone with expertise to contribute.
We wrote the manuscript in markdown and tracked changes using git.
Contributions were handled through GitHub, with individuals submitting "pull requests" to suggest additions to the manuscript.

To facilitate citation, we [defined](https://github.com/greenelab/deep-review/blob/master/CONTRIBUTING.md#markdown) a markdown citation syntax.
We supported citations to the following identifier types (in order of preference): DOIs, PubMed IDs, arXiv IDs, and URLs.
References were automatically generated from citation metadata by querying APIs to generate [Citation Style Language](http://citationstyles.org/) (CSL) JSON items for each reference.
[Pandoc](http://pandoc.org/) and [pandoc-citeproc](https://github.com/jgm/pandoc-citeproc) converted the markdown to HTML and PDF, while rendering the formatted citations and references.
In total, referenced works consisted of {{reference_counts.doi}} DOIs, {{reference_counts.pmid}} PubMed records, {{reference_counts.arxiv}} arXiv manuscripts, and {{reference_counts.url}} URLs (webpages as well as manuscripts lacking standardized identifiers).

We implemented continuous analysis so the manuscript was automatically regenerated whenever the source changed [@doi:10.1038/nbt.3780].
We configured Travis CI -- a continuous integration service -- to fetch new citation metadata and rebuild the manuscript for every commit.
Accordingly, formatting or citation errors in pull requests would cause the Travis CI build to fail, automating quality control.
In addition, the build process renders templated variables, such as the reference counts mentioned above, to automate the updating of dynamic content.
When contributions were merged into the `master` branch, Travis CI deployed the built manuscript by committing back to the GitHub repository.
As a result, the latest manuscript version is always available at https://greenelab.github.io/deep-review.
To ensure a consistent software environment, we defined a versioned [conda](https://conda.io) environment of the software dependencies.

In addition, we instructed the Travis CI deployment script to perform blockchain timestamping [@url:https://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/ @url:http://blog.dhimmel.com/irreproducible-timestamps/].
Using [OpenTimestamps](https://opentimestamps.org/), we submitted hashes for the manuscript and the source git commit for timestamping in the Bitcoin blockchain [@url:https://opentimestamps.org/].
These timestamps attest that a given version of this manuscript (and its history) existed at a given point in time.
The ability to irrefutably prove manuscript existence at a past time could be important to establish scientific precedence and enforce an immutable record of authorship.

### Author contributions

We created an open repository on the GitHub version control platform ([`greenelab/deep-review`](https://github.com/greenelab/deep-review)) [@url:https://github.com/greenelab/deep-review].
Here, we engaged with numerous authors from papers within and outside of the area.
The manuscript was drafted via GitHub commits by 26 individuals who met the ICMJE standards of authorship.
These were individuals who contributed to the review of the literature;
drafted the manuscript or provided substantial critical revisions;
approved the final manuscript draft; and agreed to be accountable in all aspects of the work.
Individuals who did not contribute in all of these ways, but who did participate, are acknowledged below.
We grouped authors into the following four classes of approximately equal contributions and randomly ordered authors within each contribution class.
Drafted multiple sub-sections along with extensive editing, pull request reviews, or discussion: A.A.K., B.K.B., B.T.D., D.S.H., E.F., G.P.W., P.A., T.C.
Drafted one or more sub-sections: A.E.C., A.S., B.J.L., E.M.C., G.L.R., J.I., J.L., J.X., S.W., W.X.
Revised specific sub-sections or supervised drafting one or more sub-sections: A.K., D.D., D.J.H., L.K.W., M.H.S.S., Y.P., Y.Q.
Drafted sub-sections, edited the manuscript, reviewed pull requests, and coordinated co-authors: A.G., C.S.G..

### Acknowledgements

We gratefully acknowledge Christof Angermueller, Kumardeep Chaudhary, Gökcen
Eraslan, Michael M. Hoffman, Mikael Huss, Bharath Ramsundar and Xun Zhu for
their discussion of the manuscript and reviewed papers on GitHub. We would like
to thank Zhiyong Lu for revisions to the text that were not captured on GitHub
as well as GitHub users aaronsheldon, swamidass, and traversc who contributed
text but did not formally approve the manuscript. Finally, we acknowledge
funding from the Gordon and Betty Moore Foundation awards GBMF4552 (C.S.G. and
D.S.H.) and GBMF4563 (D.J.H.); the National Institutes of Health awards
DP2GM123485 (A.K.), R01AI116794 (B.K.B.), R01GM089652 (A.E.C.), R01GM089753
(J.X.), T32GM007753 (B.T.D.), and U54AI117924 (A.G.); the National Science
Foundation awards 1245632 (G.L.R.), 1531594 (E.M.C.), and 1564955 (J.X.); and
the National Institutes of Health Intramural Research Program and National
Library of Medicine (Y.P.).
