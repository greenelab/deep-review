## Does deep learning create a strategic inflection point in how we categorize individuals with respect to health and disease?

*Focus for the purpose of this review - within a health care context.*

We currently categorize individuals using relatively *ad hoc* categories. These
are divided, to an extent, by organ (e.g. cancers by tumor site), perhaps to an
extent symptom, and to an extent by immediate cause. This system undergoes
continual refinement (e.g. new subtypes of disease) as our understanding
improves.

*Would deep learning enable us to do this automatically in some principled way?
Are there reasons to believe that this would be advantageous? Would it be
positive to have disease categories changed by data, or would the changing
definition (i.e. as more data are accumulated) actually be harmful? What impacts
would this have on the training of physicians?*

*What are the major challenges in this space, and does deep learning enable us to
tackle any of them? Are there example approaches whereby deep learning is
already having a transformational impact? I (Casey) have added some sections
below where I think we could contribute to the field with our discussion.*

### Major Areas of Existing Contributions

*There are a number of major challenges in this space. How do we get data
together from multiple distinct systems? How do we find biologically meaningful
patterns in that data? How do we store and compute on this data at scale? How do
we share these data while respecting privacy? I've made a section for each of
these. Feel free to add more. I see each section as something on the order of
1-2 paragraphs in our context.*

#### Clinical Care

#### Imaging Modalities (static + dynamic)

* Imaging #163, #164

#### Electronic Health Records

##### Approaches

EHR data include substantial amounts of free text, which remains challenging to approach [@doi:10.1136/amiajnl-2011-000501]. Often, researchers developing algorithms that perform well on specific tasks must design and implement domain-specific features [@doi:10.1136/amiajnl-2011-000150]. These features capture unique aspects of the literature being processed. Deep learning methods are natural feature constructors. In recent work, the authors evaluated the extent to which deep learning methods could be applied on top of generic features for domain-specific concept extraction [@arxiv:1611.08373]. They found that performance was in line with, but did not exceed, existing state of the art methods. The deep learning method had performance lower than the best performing domain-specific method in their evaluation[@arxiv:1611.08373]. This highlights the challenge of predicting the eventual impact of deep learning on the field. This provides support that deep learning may impact the field by reducing the researcher time and cost required to develop specific solutions, but it may not lead to performance increases.

Identifying consistent subgroups of individuals and individual health trajectories from clinical tests is also an active area of research. Approaches inspired by deep learning have been used for both unsupervised feature construction and supervised prediction. In the unsupervised space, early work demonstrated that unsupervised feature construction via denoising autoencoder neural networks could dramatically reduce the number of labeled examples required for subsequent supervised analyses [@doi:http://dx.doi.org/10.1101/039800]. A concurrent large-scale analysis of an electronic health records system found that a deep denoising autoencoder architecture applied to the number and co-occurrence of clinical test events, though not the results of those tests, constructed features that were more useful for disease prediction than other existing feature construction methods [@doi:http://doi.org/10.1038/srep26094]. While each of these touched on clinical tests, neither considered full text records. Taken together, these results support the potential of unsupervised feature construction in this domain. However, there are numerous challenges that will need to be overcome before we can fully assess the potential of deep learning for this application area.

##### Potential
However, significant work needs to be done to move these from conceptual advances to practical game-changers.


##### Unique challenges
Additionally, unique barriers exist in this space that may hinder progress in this field.

###### Data sharing and privacy?

*This is clearly a big issue. We should at least mention it. Deep learning likes
lots of data, and sharing restrictions don't allow that. Perhaps a paragraph on
current best practices and how they relate to deep learning. A lack of data (due
to privacy and sharing restrictions) may hamper deep learning's utility in this
area in ways that it doesn't for image analysis, etc. Perhaps this will be the
Achilles heal of deep learning in this area. A couple things to think about
[doi: 10.1126/science.1229566 doi:10.1016/j.cels.2016.04.013]*


###### Standardization/integration

*EHR standardization remains challenging. Even the most basic task of matching
patients can be challenging due to data entry issues [@pmid:27134610]. From
anecdotal conversations with colleagues, it sounds like the same information is
often entered in distinct fields in different departments and different health
care systems. It would be nice for someone to quickly survey the literature and
provide a 1-2 paragraph summary of the state of the field. References to recent
solid reviews would be great to include. A quick summary (with papers) of any
deep learning approaches used in this area would be great in the "where do we
see deep learning currently being used" section below.*

*How do we find meaningful patterns from health data (including EHR, clinical
trials, etc) that indicate categories of individuals? We should at least raise
the distinct challenges of snapshot in time data and dynamic data that capture
changes over time. It would be nice for someone to quickly survey the literature
and provide a 1-2 paragraph summary of the state of the field. References to
recent solid reviews would be great to include. A quick summary (with papers) of
any deep learning approaches used in this area would be great in the "where do
we see deep learning currently being used" section below.*

#### Storage/compute

*This bit I am less excited about. However, this recent preprint
[@arxiv:1608.05148] is pretty cool, so maybe we want to consider it. Storage is
expensive, so it may be helpful. I leave it here as a stub in case someone wants
to take it on.*

#### Where do we see deep learning currently being used?

*This one is targeted at allowing us to summarize the areas that deep learning
has touched. We should aim to highlight exemplar papers in this area. This will
probably become a relatively lengthy subsubsubsub-section, perhaps with its own
subsubsubsubsub-sections. To provide value to the review, I would suggest that
we view contributions critically, and that we attempt to ask not only has deep
learning been used but also did it matter?*

#### Has deep learning already induced a strategic inflection point for one or more aspects?

*I have looked through the papers that we have. I don't see a case in our
collection where I felt that we'd be justified to say that deep learning has
transformed how we categorize individuals with respect to health and disease.
There are definitely interesting applications, but I don't see anything that we
couldn't do similarly with some other method.*

### Will deep learning induce a strategic inflection point for categorization?

*This section attempts to get at whether or not we think that deep learning will
be transformational. Since we have some room to provide our perspective, I'd
suggest that we take a relatively tough look at this once we review where we
are in the parts above.*


#### What unique potential does deep learning bring to this?

*Are there areas that we expect deep learning to transform how we categorize
disease that we haven't seen yet? Let's get fun with speculation/dreaming on
this one.*

#### Where would you point your deep learning efforts if you had the time?

*This can be fun. We might eventually merge this with the section immediately
above on deep learning's unique potential here.*
