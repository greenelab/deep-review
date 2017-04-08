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
definition (i.e. as more data are accumulated) actually be harmful? What
impacts would this have on the training of physicians?*

*What are the major challenges in this space, and does deep learning enable us
to tackle any of them? Are there example approaches whereby deep learning is
already having a transformational impact? I (Casey) have added some sections
below where I think we could contribute to the field with our discussion.*

### Major areas of existing contributions

*There are a number of major challenges in this space. How do we get data
together from multiple distinct systems? How do we find biologically meaningful
patterns in that data? How do we store and compute on this data at scale? How
do we share these data while respecting privacy? I've made a section for each
of these. Feel free to add more. I see each section as something on the order
of 1-2 paragraphs in our context.*

#### Clinical care

#### Imaging applications in health care

One of the general areas where deep learning methods have had substantial
success has been in image analysis. Applications in areas of medicine that use
imaging extensively are also emerging. Mammography has been one area with
numerous contributions [@doi:10.1007/978-3-319-46723-8_13
@doi:10.1007/978-3-319-24553-9_74 @doi:10.1101/095794 @doi:10.1101/095786]. In
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
with deep learning approaches. Ciresan et al.
[@doi:10.1007/978-3-642-40763-5_51] developed one of the earliest examples,
winning the 2012 International Conference on Pattern Recognition's Contest on
Mitosis Detection while achieving human competitive accuracy. Their approach
uses what has become a standard convolutional neural network architecture
trained on public data.  In more recent work,  Wang et al.[@arxiv:1606.05718]
analyzed stained slides to identify cancers  within slides of lymph node slices.
The approach provided a probability map for  each slide. On this task a
pathologist has about a 3% error rate. The  pathologist did not produce any
false positives, but did have a number of false  negatives. Their algorithm had
about twice the error rate of a pathologist.  However, their algorithms errors
were not strongly correlated with the  pathologist. Theoretically, combining
both could reduce the error rate to  under 1%. In this area, these algorithms
may be ready to incorporate into  existing tools to aid pathologists. The
authors' work suggests that this could  reduce the false negative rate of such
evaluations. This theme of an ensemble  between deep learning algorithm and
human expert may help overcome some of the  challenges presented by data
limitations.

One source of training examples with rich clinical annotations is the electronic
health record. Recently Lee et al.[@doi:10.1101/094276] developed an approach to
distinguish individuals with Age-related Macular Degeneration from control
individuals. They extracted approximately 100,000 images from structured
electronic health records, which they used to train and evaluate a deep neural
network. Combining this data resource with standard deep learning techniques,
the authors reach greater than 93% accuracy. One item that is important to note
with regards to this work is that the authors used their test set for evaluating
when training had concluded. In other domains, this has resulted in a minimal
change in the estimated accuracy [@url:http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf]. However,
there is not yet a single accepted standard within the field of biomedical
research for such evaluations. We recommend the use of an independent test set
wherever it is feasible. Despite this minor limitation, the work clearly
illustrates the potential that can be unlocked from images stored in electronic
health records.

`TODO: Potential remaining topics: #122 & #151 looked interesting from an early
glance. - Do we want to make the point that most of the imaging examples don't
really do anything different/unique from standard image processing examples
(Imagenet etc.)`

#### Electronic health records

EHR data include substantial amounts of free text, which remains challenging to
approach [@doi:10.1136/amiajnl-2011-000501]. Often, researchers developing
algorithms that perform well on specific tasks must design and implement domain-
specific features [@doi:10.1136/amiajnl-2011-000150]. These features capture
unique aspects of the literature being processed. Deep learning methods are
natural feature constructors. In recent work, the authors evaluated the extent
to which deep learning methods could be applied on top of generic features for
domain-specific concept extraction [@arxiv:1611.08373]. They found that
performance was in line with, but did not exceed, existing state of the art
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
algorithms that they employed (naive Bayes, logistic regression, and deep neural
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

Identifying consistent subgroups of individuals and individual health
trajectories from clinical tests is also an active area of research. Approaches
inspired by deep learning have been used for both unsupervised feature
construction and supervised prediction. Early work by Lasko et al.
[@doi:10.1371/journal.pone.0066341], combined sparse autoencoders and Gaussian
processes to distinguish gout from leukemia from uric acid sequences. Later work
showed that unsupervised feature construction of many features via denoising
autoencoder neural networks could dramatically reduce the number of labeled
examples required for subsequent supervised analyses
[@doi:10.1016/j.jbi.2016.10.007]. In addition, it pointed towards learned
features being useful for subtyping within a single disease. A concurrent large-
scale analysis of an electronic health records system found that a deep
denoising autoencoder architecture applied to the number and co-occurrence of
clinical test events, though not the results of those tests, constructed
features that were more useful for disease prediction than other existing
feature construction methods [@doi:10.1038/srep26094].  Taken together, these
results support the potential of unsupervised feature construction in this
domain. However, numerous challenges including data integration (patient
demographics, family history, laboratory tests, text-based patient records,
image analysis, genomic data) and better handling of streaming temporal data
with many features, will need to be overcome before we can fully assess the
potential of deep learning for this application area.

Still, recent work has also revealed domains in which deep networks have
proven superior to traditional methods. Survival analysis models the time
leading to an event of interest from a shared starting point, and in the
context of EHR data, often associates these events to subject covariates.
Exploring this relationship is difficult, however, given that EHR data types
are often heterogeneous, covariates are often missing, and conventional
approaches require the covariate-event relationship be linear and aligned to a
specific starting point [@arxiv:1608.02158]. Early approaches, such as the
Faraggi-Simon feed-forward network, aimed to relax the linearity assumption,
but performance gains were lacking [@doi:10.1016/S0167-9473(99)00098-5].
Katzman et al. in turn developed a deep implementation of the Faraggi-Simon
network that, in addition to outperforming Cox regression, was capable of
comparing the risk between a given pair of treatments, thus potentially acting
as recommender system [@arxiv:1606.00931]. To overcome the remaining
difficulties, researchers have turned to deep exponential families, a class of
latent generative models that are constructed from any type of exponential
family distributions [@arxiv:1411.2581v1]. The result was a deep survival
analysis model capable of overcoming challenges posed by missing data and
heterogeneous data types, while uncovering nonlinear relationships between
covariates and failure time. They showed their model more accurately
stratified patients as a function of disease risk score compared the current
clinical implementation.
`TODO: @sw1: Are there specific challenges with using a deep neural network
as opposed to current standard methods?`

##### Opportunities

However, significant work needs to be done to move these from conceptual
advances to practical game-changers.

* Large data resources (see sample # issues that mammography researchers are
  working around)
* Semi-supervised methods to take advantage of large number of unlabeled
  examples
* Transfer learning.

##### Unique challenges

Additionally, unique barriers exist in this space that may hinder progress in
this field.

###### Lack of ground-truth labels in data, and high cost in post-study validation by clinician experts.

Lack of true labels is perhaps among the biggest obstacles for EHR-based
analyses that employ machine learning (e.g., phenotyping). Popular deep
learning (and machine learning) methods are often used to tackle classification
tasks and thus require ground-truth labels for training.  For EHRs,
unfortunately, this means that researchers need to hire multiple clinicians to
manually read and annotate individual patients' records through a process called
chart review. This allows researchers to assign "true" labels, i.e. those that
match our best available knowledge. Depending on the application, sometimes the
features constructed by algorithms also need to be manually validated and
interpreted by clinicians. This can be time consuming and expensive
[@doi:10.1016/j.ijmedinf.2016.09.014]. Because of these costs, much of this
research, including the work cited in this review, skips the process of expert
review. Clinicians' skepticism for research without expert review may greatly
dampen their enthusiasm for the work and consequently reduce its impact. To
date, even well-resourced large national consortia have been challenged by the
task of acquiring enough expert-validated labeled data. For instance, in the
eMERGE consortia and PheKB database [@url:https://phekb.org/implementations],
most samples with expert validation contain only 100 to 300 patients. These
datasets are quite small, even for simple machine learning algorithms. The
challenge is greater for deep learning models with many parameters. While
unsupervised and semi-supervised approaches can help with small sample sizes,
the field would benefit greatly from large collections of anonymized records in
which a substantial number of records have undergone expert review.

This challenge is not unique to EHR-based studies. Work on medical images,
-omics data in applications for which detailed metadata are required, and other
applications for which labels are costly to obtain will be hampered as long as
abundant curated data are unavailable. Unsupervised and semi-supervised methods
provide one path forward [@doi:10.1016/j.jbi.2016.10.007], as do adversarial
training examples [@doi:10.1101/095786]. We also expect the recently described
data programming strategy [@arxiv:1605.07723] to play a role in addressing this
challenge. In data programming, noisy automated labeling functions are
integrated. While numerous writers have described data as the new oil [@url:http://ana.blogs.com/maestros/2006/11/data_is_the_new.html, @url:https://medium.com/twenty-one-hundred/data-is-the-new-oil-a-ludicrous-proposition-1d91bba4f294],
Ratner, Bach, and Ré described training data as "The _New_ New Oil" [@url:http://hazyresearch.github.io/snorkel/blog/weak_supervision.html].
Based on our review of research on deep learning methods to categorize disease,
this rings true. We expect each of these approaches to play an important role
if deep learning is going to transform how we analyze data to categorize states
of human health. Finally, we don't expect that these methods will replace expert
review. We expect them to complement expert review by allowing more efficient
use of the costly practice of manual annotation.

###### "Right to explanation" laws and potential for discrimination

In April 2016, the European Union adopted new rules regarding the use of
personal information, the General Data Protection Regulation (GDPR)
[@arxiv:1606.08813v3]. The new rules are perhaps best summed up by the phrase
"right to explanation". Those who use machine learning algorithms must be able
to explain how a decision was reached. For example, a clinician treating a
patient who is aided by a machine learning algorithm may be expected to explain
decisions that use the patient's data.  The new rules were designed to target
categorization or recommendation systems, which inherently profile individuals,
but can do so in ways that are discriminatory and unlawful `TODO: @traversc citation needed`.

As datasets become larger and more complex, we may begin to identify
relationships in data that are important for human health but difficult to
understand. The algorithms described in this review and others like them may
become highly accurate and useful for various purposes, including within medical
practice. However, to discover and avoid discriminatory applications it will be
important to consider algorithm interpretability alongside accuracy. For
example, if we train an algorithm to predict which drugs would be prescribed
during a patient's visit to the doctor and there's an existing pattern of racial
differences in prescription behavior (`TODO: @traversc - you can pick a different example but I think we need one - whichever one you think is most fully supported by the literature.`),
this pattern could become baked into the predictions made by the algorithm.
Machine learning practitioners, and particularly those who use deep neural
networks, which are challenging to interpret, must remain cognizant of this
possibility and make every effort to prevent harm from discriminatory
predictions.

###### Data sharing and privacy?

*This is clearly a big issue. We should at least mention it. Deep learning likes
lots of data, and sharing restrictions don't allow that. Perhaps a paragraph on
current best practices and how they relate to deep learning. A lack of data (due
to privacy and sharing restrictions) may hamper deep learning's utility in this
area in ways that it doesn't for image analysis, etc. Perhaps this will be the
Achilles heal of deep learning in this area. A couple things to think about
[@doi:10.1126/science.1229566 @doi:10.1016/j.cels.2016.04.013]*

###### Standardization/integration

EHRs are designed and optimized primarily for patient care and billing purposes,
meaning research is at most a tertiary priority. This presents significant
challenges to EHR based research in general, and particularly to data intensive
deep learning research. EHRs are used differently even within the same health
care system [@pmid:24159271 @pmid:21347133]. Individual users have unique
usage patterns, and different departments have different priorities which
introduce missing data in a non-random fashion. Just et al. demonstrated that
even the most basic task of matching patients can be challenging due to data
entry issues [@pmid:27134610]. This is before considering challenges caused by
system migrations and health care system expansions through acquisitions.
Replication between hospital systems requires controlling for both these
systematic biases as well as for population and demographic effects.
Historically, rules-based algorithms have been popular in EHR-based research but
because these are developed at a single institution and trained with a specific
patient population they do not transfer easily to other populations
[@doi:10.1136/amiajnl-2013-001935]. Wiley et al.
[@doi:10.1142/9789813207813_0050] showed that warfarin dosing algorithms often
under perform in African Americans, illustrating that some of these issues are
unsolved even at a treatment best practices level. This may be a promising
application of deep learning, as rules-based algorithms were also the standard
in most natural language processing but have been superseded by machine learning
and in particular deep learning methods
[@url:https://aclweb.org/anthology/D/D13/D13-1079.pdf].

###### Temporal Patient Trajectories

Traditionally, physician training programs justified long training hours by
citing increased continuity of care and learning by following the progression of
a disease over time, despite the known consequences of decreased mental and
quality of life [@doi:10.1016/j.socscimed.2003.08.016
@doi:10.1016/S1072-7515(03)00097-8 @doi:10.1097/00000542-199004000-00024
@doi:10.1016/S0277-9536(96)00227-4]. Yet, a common practice in EHR-based
research is to take a point in time snapshot and convert patient data to a
traditional vector for machine learning and statistical analysis. This results
in significant signal losses as timing and order of events provide insight into
a patient's disease and treatment. Efforts to account for the order of events
have shown promise [@doi:10.1038/ncomms5022] but require exceedingly large
patient sizes due to discrete combinatorial bucketing.

Lasko et al. [@doi:10.1371/journal.pone.0066341] used
autoencoders on longitudinal sequences of serum urine acid measurements to
identify population subtypes. More recently, deep learning has shown promise
working with both sequences (Convolutional Neural Networks) [@arxiv:1607.07519]
and the incorporation of past and current state (Recurrent Neural Networks, Long
Short Term Memory Networks)[@arxiv:1602.00357].

###### Data sharing and privacy

Early successes using deep learning involved very large training datasets
(ImageNet 1.4 million images) [@arxiv:1409.0575], but a responsibility to
protect patient privacy limits the ability openly share large patient datasets.
Limited dataset sizes may restrict the number of parameters that can be trained
in a model, but the lack of sharing may also hamper reproducibility and
confidence in results. Even without sharing data, algorithms trained on
confidential patient data may present security risks or accidentally allow for
the exposure of individual level patient data. Tramer et al. [@arxiv:1609.02943]
showed the ability to steal trained models via public APIs and Dwork and Roth
[@doi:10.1561/0400000042] demonstrate the ability to expose individual level
information from accurate answers in a machine learning model.

Training algorithms in a differentially private manner provides a limited
guarantee that the algorithms output will be equally likely to occur regardless
of the participation of any one individual. The limit is determined by a single
parameter which provides a quantification of privacy. Simmons et al.
[@doi:10.1016/j.cels.2016.04.013] present the ability to perform GWASs in a
differentially private manner and Abadi et al. [@arxiv:1607.00133] show the
ability to train deep learning classifiers under the differential privacy
framework. Finally, Continuous Analysis [@doi:10.1101/056473] allows for the
ability to automatically track and share intermediate results for the purposes
of reproducibility without sharing the original data.

###### Biomedical data is often "Wide"

*Biomedical studies typically deal with relatively small sample sizes but each
sample may have millions of measurements (genotypes and other omics data, lab
tests etc).*

*Classical machine learning recommendations were to have 10x samples per number
of parameters in the model.*

*Number of parameters in an MLP. Convolutions and similar strategies help but do
not solve*

*Bengio diet networks paper*

*(Wei Xie; @XieConnect): I personally do not think this subsection is necessary.
It does not seem a big issue for health care data. For instance, EHR is mostly
textual and very small in size and easy to compute even for large medical centers.
Medical images and some medical tests may be larger, but they are still
way behind MNIST or ImageNet in scale and compute requirement.*

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
