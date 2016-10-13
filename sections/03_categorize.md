## Does deep learning create a strategic inflection point in how we categorize individuals with respect to health and disease?

Focus for the purpose of this review - within a health care context.

We currently categorize individuals using relatively ad hoc categories. These
are divided, to an extent, by organ (e.g. cancers by tumor site), perhaps to an
extent symptom, and to an extent by immediate cause. This system undergoes
continual refinement (e.g. new subtypes of disease) as our understanding
improves.

Would deep learning enable us to do this automatically in some principled way?
Are there reasons to believe that this would be advantageous? Would it be
positive to have disease categories changed by data, or would the changing
definition (i.e. as more data are accumulated) actually be harmful? What impacts
would this have on the training of physicians?

What are the major challenges in this space, and does deep learning enable us to
tackle any of them? Are there example approaches whereby deep learning is
already having a transformational impact? I (Casey) have added some sections
below where I think we could contribute to the field with our discussion.

### Major challenges

There are a number of major challenges in this space. How do we get data
together from multiple distinct systems? How do we find biologically meaningful
patterns in that data? How do we store and compute on this data at scale? How do
we share these data while respecting privacy? I've made a section for each of
these. Feel free to add more. I see each section as something on the order of
1-2 paragraphs in our context.

#### Standardization/integration

EHR standardization remains challenging. Even the most basic task of matching
patients can be challenging due to data entry issues [@pmid:27134610]. From
anecdotal conversations with colleagues, it sounds like the same information is
often entered in distinct fields in different departments and different health
care systems. It would be nice for someone to quickly survey the literature and
provide a 1-2 paragraph summary of the state of the field. References to recent
solid reviews would be great to include. A quick summary (with papers) of any
deep learning approaches used in this area would be great in the "where do we
see deep learning currently being used" section below.

#### Pattern Recognition (static + dynamic)

How do we find meaningful patterns from health data (including EHR, clinical
trials, etc) that indicate categories of individuals? We should at least raise
the distinct challenges of snapshot in time data and dynamic data that capture
changes over time. It would be nice for someone to quickly survey the literature
and provide a 1-2 paragraph summary of the state of the field. References to
recent solid reviews would be great to include. A quick summary (with papers) of
any deep learning approaches used in this area would be great in the "where do
we see deep learning currently being used" section below.

#### Storage/compute

This bit I am less excited about. However, this recent preprint
[@arxiv:1608.05148] is pretty cool, so maybe we want to consider it. Storage is
expensive, so it may be helpful. I leave it here as a stub in case someone wants
to take it on.

#### Data sharing and privacy?

This is clearly a big issue. We should at least mention it. Deep learning likes
lots of data, and sharing restrictions don't allow that. Perhaps a paragraph on
current best practices and how they relate to deep learning. A lack of data (due
to privacy and sharing restrictions) may hamper deep learning's utility in this
area in ways that it doesn't for image analysis, etc. Perhaps this will be the
Achilles heal of deep learning in this area. A couple things to think about
[doi: 10.1126/science.1229566 doi:10.1016/j.cels.2016.04.013]

### Will deep learning induce a strategic inflection point for categorization?

#### Where do we see deep learning currently being used?

#### Has deep learning already transformed one or more aspects?

I have looked through the papers that we have. I don't see a case in our
collection where I felt that we'd be justified to say that deep learning has
transformed how we categorize individuals with respect to health and disease.
There are definitely interesting applications, but I don't see anything that we
couldn't do similarly with some other method.

#### What unique potential does deep learning bring to this?

#### Where would you point your deep learning efforts if you had the time?
