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

#### Imaging Applications in Health Care

One of the general areas where deep learning methods have had substantial
success has been in image analysis. Applications in areas of medicine that use
imaging extensively are also emerging. Mammography has been one area with
numerous contributions [@doi:10.1007/978-3-319-46723-8_13,
@doi:10.1007/978-3-319-24553-9_74, @doi:10.1101/095794, @doi:10.1101/095786]. In
all of this work, the researchers must work around a specific challenge - the
limited number of well annotated training images. To expand the number and
diversity of images, the researchers have employed approaches where they employ
adversarial examples [@doi:10.1101/095786] or first train towards human-created
features before subsequent fine tuning [@doi:10.1007/978-3-319-46723-8_13]. The
presence of a large bank of well-annotated mammography images would aid in the
application of deep neural networks to this area. Though this strategy has not
yet been employed in this domain, large collections of unlabeled images might
first be used in an unsupervised context to construct high-quality feature
detectors. Then the small number of labeled examples could be used for
subsequent training. Similar strategies have been employed for EHR data where
high-quality labeled examples are also difficult to obtain
[@doi:10.1101/039800].

In addition to radiographic images, histology slides are also being analyzed
with deep learning approaches. In recent work, Wang et al.[@arxiv:1606.05718]
analyzed stained slides to identify cancers within slides of lymph node slices.
The approach provided a probability map for each slide. On this task a
pathologist has about a 3% error rate. Their algorithm had about a 7% error
rate. However, their algorithms errors were not strongly correlated with the
pathologist - combining both dropped the error rate to under 1%. In this area,
these algorithms may be ready to incorporate into existing tools to aid
pathologists. The authors' work suggest that this could reduce the false
negative rate of such evaluations. `TODO: Incorporate #71 via @brettbj who has
covered in journal club and has notes.`

One source of training examples with rich clinical annotations is the electronic
health record. Recently Lee et al.[@doi:10.1101/094276] developed an approach to
distinguish individuals with Age-related Macular Degeneration from control
individuals. They extracted approximately 100,000 images from structured
electronic health records, which they used to train and evaluate a deep neural
network. Combining this data resource with standard deep learning techniques,
the authors reach greater than 93% accuracy. One item that is important to note
with regards to this work is that the authors used their test set for evaluating
when training had concluded. In other domains, this has resulted in a minimal
change in the estimated accuracy
[@url:http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf].
However, there is not yet a single accepted standard within the field of
biomedical research for such evaluations. We recommend the use of an independent
test set wherever it is feasible. Despite this minor limitation, the work
clearly illustrates the potential that can be unlocked from images stored in
electronic health records.

#### Electronic Health Records

`TODO: @brettbj to incorporate
https://github.com/greenelab/deep-review/issues/78 and
https://github.com/greenelab/deep-review/issues/77`

EHR data include substantial amounts of free text, which remains challenging to
approach [@doi:10.1136/amiajnl-2011-000501]. Often, researchers developing
algorithms that perform well on specific tasks must design and implement
domain-specific features [@doi:10.1136/amiajnl-2011-000150]. These features
capture unique aspects of the literature being processed. Deep learning methods
are natural feature constructors. In recent work, the authors evaluated the
extent to which deep learning methods could be applied on top of generic
features for domain-specific concept extraction [@arxiv:1611.08373]. They found
that performance was in line with, but did not exceed, existing state of the art
methods. The deep learning method had performance lower than the best performing
domain-specific method in their evaluation [@arxiv:1611.08373]. This highlights
the challenge of predicting the eventual impact of deep learning on the field.
This provides support that deep learning may impact the field by reducing the
researcher time and cost required to develop specific solutions, but it may not
lead to performance increases.

In recent work, Yoon et al.[@doi:10.1007/978-3-319-47898-2_21] analyzed simple
features using deep neural networks and found that the patterns recognized by
the algorithms could be re-used across tasks. Their aim was to analyze the free
text portions of pathology reports to identify the primary site and laterality
of tumors. The only features the authors supplied to the algorithms that they
evaluated were unigrams and bigrams. These are the counts for single words and
two-word combinations in a free text document. They subset the full set of words
and word combinations to the 400 most commonly used ones. The machine learning
algorithms that they employed (naive bayes, logistic regression, and deep neural
networks) all performed relatively similarly on the task of identifying the
primary site. However, when the authors evaluated the more challenging task,
i.e. evaluating the laterality of each tumor, the deep neural network
outperformed the other methods. Of particular interest, when the authors first
trained a neural network to predict primary site and then repurposed those
features as a component of a secondary neural network trained to predict
laterality, the performance was higher than a laterality-trained neural network.
This indicates a potential strength of deep methods. It may be possible to
repurpose features from task to task, improving overall predictions as the field
tackles new challenges.

TODO: survival analysis/readmission prediction methods from EHR/EMR style data
(@sw1 + maybe @traversc). These include:
* https://github.com/greenelab/deep-review/issues/81
* https://github.com/greenelab/deep-review/issues/82
* https://github.com/greenelab/deep-review/issues/152
* https://github.com/greenelab/deep-review/issues/155

Identifying consistent subgroups of individuals and individual health
trajectories from clinical tests is also an active area of research. Approaches
inspired by deep learning have been used for both unsupervised feature
construction and supervised prediction. In the unsupervised space, early work
demonstrated that unsupervised feature construction via denoising autoencoder
neural networks could dramatically reduce the number of labeled examples
required for subsequent supervised analyses [@doi:10.1101/039800]. A concurrent
large-scale analysis of an electronic health records system found that a deep
denoising autoencoder architecture applied to the number and co-occurrence of
clinical test events, though not the results of those tests, constructed
features that were more useful for disease prediction than other existing
feature construction methods [@doi:10.1038/srep26094]. While each of these
touched on clinical tests, neither considered full text records. Taken together,
these results support the potential of unsupervised feature construction in this
domain. However, there are numerous challenges that will need to be overcome
before we can fully assess the potential of deep learning for this application
area.

##### Opportunities

However, significant work needs to be done to move these from conceptual
advances to practical game-changers.

##### Unique challenges

Additionally, unique barriers exist in this space that may hinder progress in
this field.

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
