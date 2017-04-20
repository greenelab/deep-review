# Deep Learning, Genomics, and Precision Medicine

For preliminary authorship information, see the [contributors](https://github.com/greenelab/deep-review/graphs/contributors) on GitHub.


## Abstract

Abstract goes here.


## Introduction

Biology and medicine are rapidly becoming data-intensive with
respect to both research and practice. A recent comparison of genomics with
social media, online videos and other data-intensive scientific disciplines
suggested that the field of genomics alone would equal or surpass other fields
in data generation and analysis within the next decade
[@13bxiY1vo]. These data present new opportunities, but
also new challenges. The data volume and complexity both indicate that
automated algorithms will be needed to extract
meaningful patterns and provide actionable knowledge allowing us to better
treat, categorize, or study disease, all within data constrained and privacy
critical environments.

Concurrent with this explosive growth in biomedical data, a new enthusiasm for a
class of machine learning algorithms, known as deep learning, is revolutionizing
domains from image search to the game of Go [@2gn6PKkv]. As
recently applied to image analysis problems, these architectures readily surpass
previous best-in-class results, and computer scientists are now building
many-layered neural networks from collections of millions of images. In a famous
and early example, scientists from Google demonstrated that a neural network
could learn to identify cats simply by watching online videos
[@IiNJE32f].

What if, more generally, deep learning could solve the challenges
presented by the growth of data in biomedicine? Could these algorithms
identify the "cats" hidden in our data - the patterns unknown to the
researcher - and act on them? Deep learning has transformed image analysis, but
what about biomedicine more broadly? In this review,
we examine whether this transformation is simply a matter of time or
if there are unique challenges posed by biomedical data that render deep
learning methods more challenging or less fruitful to apply.

### What is deep learning?

Deep learning is built on a biologically-inspired approach from machine learning
termed neural networks. Each neuron in a computational neural network, termed a
node, has inputs, an activation function, and outputs. Each value from the
inputs is usually multiplied by some weight and combined and summarized by the
activation function. The value of the activation function is then multiplied by
another set of weights to produce the output **TODO: we probably need a figure
here - I see no way that we don't include this type of description in our paper,
despite the fact that it's been done tons of times before. - I'm really partial
to this nature review's explanation about making non-linear problems linear -
figure 1 [@BeijBSRE]** These neural networks are trained by
identifying weights that produce a desired output from some specific input.

Neural networks can also be stacked. The outputs from one network can be used as
inputs to another. This process produces a stacked, also known as a multi-layer,
neural network. The multi-layer neural network techniques that underlie deep
learning have a long history. Multi-layer methods have been discussed in the
literature for more than five decades [@1G5eCiq4d]. Given
this context, it's challenging to consider "deep learning" as a new advance,
though the term has only become widespread to describe analysis methods in the
last decade. Much of the early history of neural networks has been extensively
covered in a recent review [@BQS8ClV0]. For the purposes
of this review, we identify deep learning approaches as those that use
multi-layer neural networks to construct complex features.

We also discuss a class of algorithms that we term "shallow learning"
approaches. We do not use this as a pejorative term, but instead to denote
algorithms which have all of the hallmarks of deep approaches except that they
employ networks of limited depth. We found it valuable to include these as we
sought to identify the current contributions of deep learning and to predict its
future impact. Researchers may employ these shallow learning methods for a
number of reasons including: 1) shallow networks provide a degree of
interpretability that better matches their use case; 2) the available data are
insufficient to support deeper architectures, however new datasets that will
support deep methods are expected; 3) or as building blocks to be combined with
other non-neural-network-based approaches at subsequent stages.

### Will deep learning transform the study of human disease?

With this review, we set out to address the question: what would need to be true
for deep learning to transform how we categorize, study, and treat individuals
to maintain or restore health? We chose a high bar for "transform." Andrew
Grove, the former CEO of Intel, coined the term Strategic Inflection Point to
refer to a change in technologies or environment that requires a business to be
fundamentally reshaped
[@mAXsmd43]. Here, we
ought to identify whether deep learning was an innovation that would induce a
strategic inflection point on the practice of biology or medicine. We considered
this with an eye towards the concept of precision medicine.

There are numerous examples where deep learning
has been applied to biological problems and produced somewhat improved results,
and there are numerous reviews that have focused on general applications of deep
learning in biology [@yXqhuueV; @gJE0ExFr; @MmRGFVUu; @1VZjheOA; @irSe12Sm; @G00xvi94]. We sought cases where deep
learning was enabling researchers to solve challenges that were previously
considered infeasible, or if it made difficult, tedious, and non-routine
analyses routine.

Based on our guiding question, we focused on the application of deep learning to
topics of biomedical importance. We divided the large range of topics into three
broad classes: Disease and Patient Categorization,
Fundamental Biological Study, and Patient Treatment. We briefly introduce the
types of questions, approaches and data that are typical for each class in the
application of deep learning.

#### Disease and Patient Categorization

A key challenge in biomedicine is the accurate classification of
diseases and disease subtypes. In oncology, current "gold standard"
approaches involve histology, requiring manual
human expertise for quantification, or small panel of molecular markers,
such as cell surface
receptors or genes' expression. One example is the PAM50 approach
to classifying breast cancer where the expression of 50 marker
genes divides breast cancer patients into four subtypes.
Significant heterogeneity still remains within these four subtypes
[@lnK82Ey6; @pEIw87Mp]. Given the
increasing wealth of molecular data available, a more
comprehensive subtyping seems possible.

Several studies have used deep learning methods in order to better categorize
breast cancer patients. For example, Tan et al. applied denoising
autoencoders (DA), an unsupervised approach, in order to cluster breast
cancer patients [@PBiRSdXv]. Ciresan et al. utilized
convolutional neural networks (CNN) to count mitotic divisions in
histological images; a feature that is highly correlated with disease
outcome [@koEdZRcY]. Despite these recent advances, a
number of challenges exist in this area of research, such as the integration
of disparate types of data, including electronic health records (EHR),
imaging and histology data, and molecular omics data.

#### Fundamental Biological Study

Deep learning can be applied to answer more fundamental
biological questions, and is especially suited to leveraging
large amounts of data from high throughput omics studies. One
classic biological problem where machine learning has been extensively
applied is the prediction of molecular targets. Recent advances using deep
learning have shown higher accuracy in determining molecular targets. For
example, Lee et al. used deep recurrent neural networks (RNN) to predict gene
targets of micro-RNAs [@YUms527e]. Wang et al. used a
residual CNN to predict protein-protein contact on a genome-wide scale
[@W3grN7jy]. Other biological questions that have been investigated
include the prediction of protein secondary structure based on sequence data
[@ZzaRyGuJ; @UO8L6nd],
recognition of functional genomic elements such as enhancers and
promoters [@s5sy4AOi; @17B2QAA1k; @12aqvAgz6], predicting the deleterious effects of nucleotide
polymorphisms [@15E5yG1Ho], etc.

#### Patient Treatment

Although the application of deep learning to patient treatment is just beginning,
we expect a dramatic increase in methods aiming to recommend patient
treatment, predict
treatment outcome, and guide future development of new therapies.
Specifically, effort in this area aims to identify drug targets, identify
drug interactions or predict drug response. One recent approach for
predicting drug response is the use of protein structure to predict drug
interactions and drug bioactivity through CNN [@Z7fd0BYf]. Since CNNs
leverage spatial relationships within the data, this particular deep learning
framework is well suited to the problem. Drug discovery and drug
"repurposing" are two other hot topics. Aliper et al. used transcriptomic
data to predict which drugs might be repurposed for other diseases through
deep fully connected neural networks
[@EMDwvRGb]. In a similar vein, Wang et al. used
restricted boltzman machines (RBM) to predict drug molecular targets
[@1AU7wzPqa].


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
numerous contributions [@JK8NuXy3; @VFw1VXDP; @9G9Hv1Pp; @Xxb4t3zO]. In
all of this work, the researchers must work around a specific challenge - the
limited number of well annotated training images. To expand the number and
diversity of images, the researchers have employed approaches where they employ
adversarial examples [@Xxb4t3zO] or first train towards human-created
features before subsequent fine tuning [@JK8NuXy3]. The
presence of a large bank of well-annotated mammography images would aid in the
application of deep neural networks to this area. Though this strategy has not
yet been employed in this domain, large collections of unlabeled images might
first be used in an unsupervised context to construct high-quality feature
detectors. Then the small number of labeled examples could be used for
subsequent training. Similar strategies have been employed for EHR data where
high-quality labeled examples are also difficult to obtain
[@aM2Uy2ix].

In addition to radiographic images, histology slides are also being analyzed
with deep learning approaches. Ciresan et al.
[@koEdZRcY] developed one of the earliest examples,
winning the 2012 International Conference on Pattern Recognition's Contest on
Mitosis Detection while achieving human competitive accuracy. Their approach
uses what has become a standard convolutional neural network architecture
trained on public data.  In more recent work,  Wang et al.[@mbEp6jNr]
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
health record. Recently Lee et al.[@SxsZyrVM] developed an approach to
distinguish individuals with Age-related Macular Degeneration from control
individuals. They extracted approximately 100,000 images from structured
electronic health records, which they used to train and evaluate a deep neural
network. Combining this data resource with standard deep learning techniques,
the authors reach greater than 93% accuracy. One item that is important to note
with regards to this work is that the authors used their test set for evaluating
when training had concluded. In other domains, this has resulted in a minimal
change in the estimated accuracy [@lTBZomqa]. However,
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
approach [@uDaRUyh9]. Often, researchers developing
algorithms that perform well on specific tasks must design and implement domain-
specific features [@sG3iVOTS]. These features capture
unique aspects of the literature being processed. Deep learning methods are
natural feature constructors. In recent work, the authors evaluated the extent
to which deep learning methods could be applied on top of generic features for
domain-specific concept extraction [@dO844vZn]. They found that
performance was in line with, but did not exceed, existing state of the art
methods. The deep learning method had performance lower than the best performing
domain-specific method in their evaluation [@dO844vZn]. This highlights
the challenge of predicting the eventual impact of deep learning on the field.
This provides support that deep learning may impact the field by reducing the
researcher time and cost required to develop specific solutions, but it may not
lead to performance increases.

In recent work, Yoon et al.[@yUgE09ve] analyzed simple
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
[@FLX0o7bL], combined sparse autoencoders and Gaussian
processes to distinguish gout from leukemia from uric acid sequences. Later work
showed that unsupervised feature construction of many features via denoising
autoencoder neural networks could dramatically reduce the number of labeled
examples required for subsequent supervised analyses
[@5x3uMSKi]. In addition, it pointed towards learned
features being useful for subtyping within a single disease. A concurrent large-
scale analysis of an electronic health records system found that a deep
denoising autoencoder architecture applied to the number and co-occurrence of
clinical test events, though not the results of those tests, constructed
features that were more useful for disease prediction than other existing
feature construction methods [@WrNCJ9sO].  Taken together, these
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
specific starting point [@qXdO2aMm]. Early approaches, such as the
Faraggi-Simon feed-forward network, aimed to relax the linearity assumption,
but performance gains were lacking [@1921Mctzh].
Katzman et al. in turn developed a deep implementation of the Faraggi-Simon
network that, in addition to outperforming Cox regression, was capable of
comparing the risk between a given pair of treatments, thus potentially acting
as recommender system [@1FE0F2pQ]. To overcome the remaining
difficulties, researchers have turned to deep exponential families, a class of
latent generative models that are constructed from any type of exponential
family distributions [@pxdeuhMS]. The result was a deep survival
analysis model capable of overcoming challenges posed by missing data and
heterogeneous data types, while uncovering nonlinear relationships between
covariates and failure time. They showed their model more accurately
stratified patients as a function of disease risk score compared the current
clinical implementation.

There is a computational cost for these methods, however, when compared to
traditional, non-network approaches. For the exponential family models,
despite their scalability [arXiv:1206.7051], an important question for the
investigator is whether he or she is interested in estimates of posterior
uncertainty. Given that these models are effectively Bayesian neural networks,
much of their utility simplifies to whether a Bayesian approach is warranted
for a given increase in computational cost. Moreover, as with all variational
methods, future work must continue to explore just how well the posterior
distributions are approximated, especially as model complexity increases
[arXiv:1511.02386].

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
[@1Ar4f4vfR]. Because of these costs, much of this
research, including the work cited in this review, skips the process of expert
review. Clinicians' skepticism for research without expert review may greatly
dampen their enthusiasm for the work and consequently reduce its impact. To
date, even well-resourced large national consortia have been challenged by the
task of acquiring enough expert-validated labeled data. For instance, in the
eMERGE consortia and PheKB database [@ziudr6hx],
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
provide one path forward [@5x3uMSKi], as do adversarial
training examples [@Xxb4t3zO]. We also expect the recently described
data programming strategy [@5Il3kN32] to play a role in addressing this
challenge. In data programming, noisy automated labeling functions are
integrated. Numerous writers have described data as the new oil
[@daemz8Fm; @o8mib4CN].
The idea behind this metaphor is that data are available in large quantities,
valuable once refined, and the underlying resource that will enable a
data-driven revolution in how work is done. Contrasting with this perspective,
Ratner, Bach, and Ré described labeled training data as "The _New_ New Oil"
[@hfcf5Hmi]. In this
framing, data are abundant and not a scarce resource. Instead, new approaches
to solve problems arise when labeled training data become sufficient to enable
them. Based on our review of research on deep learning methods to categorize
disease, the latter framing rings true. We expect each of these approaches to
play an important role if deep learning is going to transform how we analyze
data to categorize states of human health. Finally, we don't expect that these
methods will replace expert review. We expect them to complement expert review
by allowing more efficient use of the costly practice of manual annotation.

###### Discrimination and "right to an explanation" laws

In April 2016, the European Union adopted new rules regarding the use of
personal information, the General Data Protection Regulation (GDPR)
[@7yE9K08a]. A component of these rules can be summed up by the phrase
"right to an explanation". Those who use machine learning algorithms must be
able to explain how a decision was reached. For example, a clinician treating a
patient who is aided by a machine learning algorithm may be expected to explain
decisions that use the patient's data. The new rules were designed to target
categorization or recommendation systems, which inherently profile individuals.
Such systems can do so in ways that are discriminatory and unlawful `TODO: @traversc citation needed`.

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
[@1CuDxTLXa; @6XtEfQMC]*

###### Standardization/integration

EHRs are designed and optimized primarily for patient care and billing purposes,
meaning research is at most a tertiary priority. This presents significant
challenges to EHR based research in general, and particularly to data intensive
deep learning research. EHRs are used differently even within the same health
care system [@11sli93ov; @y9ONtSZ9]. Individual users have unique
usage patterns, and different departments have different priorities which
introduce missing data in a non-random fashion. Just et al. demonstrated that
even the most basic task of matching patients can be challenging due to data
entry issues [@4rTluXLs]. This is before considering challenges caused by
system migrations and health care system expansions through acquisitions.
Replication between hospital systems requires controlling for both these
systematic biases as well as for population and demographic effects.
Historically, rules-based algorithms have been popular in EHR-based research but
because these are developed at a single institution and trained with a specific
patient population they do not transfer easily to other populations
[@11OyzMl87]. Wiley et al.
[@qe90c1CL] showed that warfarin dosing algorithms often
under perform in African Americans, illustrating that some of these issues are
unsolved even at a treatment best practices level. This may be a promising
application of deep learning, as rules-based algorithms were also the standard
in most natural language processing but have been superseded by machine learning
and in particular deep learning methods
[@Qnd0SYhm].

###### Temporal Patient Trajectories

Traditionally, physician training programs justified long training hours by
citing increased continuity of care and learning by following the progression of
a disease over time, despite the known consequences of decreased mental and
quality of life [@XJw23xy0; @wzfGJdXI; @nPRpl05n; @17hjNSIIc]. Yet, a common practice in EHR-based
research is to take a point in time snapshot and convert patient data to a
traditional vector for machine learning and statistical analysis. This results
in significant signal losses as timing and order of events provide insight into
a patient's disease and treatment. Efforts to account for the order of events
have shown promise [@ogs3PPp7] but require exceedingly large
patient sizes due to discrete combinatorial bucketing.

Lasko et al. [@FLX0o7bL] used
autoencoders on longitudinal sequences of serum urine acid measurements to
identify population subtypes. More recently, deep learning has shown promise
working with both sequences (Convolutional Neural Networks) [@Ohd1Q9Xw]
and the incorporation of past and current state (Recurrent Neural Networks, Long
Short Term Memory Networks)[@HRXii6Ni].

###### Data sharing and privacy

Early successes using deep learning involved very large training datasets
(ImageNet 1.4 million images) [@HKA6hi9E], but a responsibility to
protect patient privacy limits the ability openly share large patient datasets.
Limited dataset sizes may restrict the number of parameters that can be trained
in a model, but the lack of sharing may also hamper reproducibility and
confidence in results. Even without sharing data, algorithms trained on
confidential patient data may present security risks or accidentally allow for
the exposure of individual level patient data. Tramer et al. [@ULSPV0rh]
showed the ability to steal trained models via public APIs and Dwork and Roth
[@v8Lp4ibI] demonstrate the ability to expose individual level
information from accurate answers in a machine learning model.

Training algorithms in a differentially private manner provides a limited
guarantee that the algorithms output will be equally likely to occur regardless
of the participation of any one individual. The limit is determined by a single
parameter which provides a quantification of privacy. Simmons et al.
[@6XtEfQMC] present the ability to perform GWASs in a
differentially private manner and Abadi et al. [@ucHUOABT] show the
ability to train deep learning classifiers under the differential privacy
framework. Finally, Continuous Analysis [@7MR5St9Q] allows for the
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


## How is deep learning used to study basic biological processes in a manner that may provide future insights into human disease?

*The (awkward) placeholder section title is intended to help define the scope.
We do not want this section to become a miscellaneous collection of everything
that does not fit in Categorize and Treat.*

*One proposal is that we organize this roughly by what is being predicted,
which will generally correspond to the types of data being used.  For each
sub-section we can quickly introduce the prediction problem and cite some
examples of the relevance to disease.  Hypothetically, if we had an algorithm
that produced perfect predictions on the task, what would we learn and how
could those predictions be used?*

*Existing reviews could be mentioned briefly.*

*It may not fit here, but there could be a general discussion of why different
neural network architectures are particularly well-suited for different types
of input data.  For example, CNNs and RNNs for 1-dimensional data are used
in several categories below.*

*A few suggestions for sub-sections follow.  Some of these could be left out
because our goal is not an exhaustive enumeration of methods.  Some
are important areas of biology, but there may not be much deep learning-
specific content to present.  Others may be important areas where we lack
expertise, in which case we may acknowledge the application area but not
dive into merits or weaknesses of individual methods.*

### Gene expression

Gene expression measurements characterize the abundance of many thousands of
RNA transcripts within a given organism, tissue, or cell. This characterization
can represent the underlying state of the given system and can be used to study
heterogeneity across samples as well as how the system reacts to perturbation.
While gene expression measurements have been traditionally made by quantitative
polymerase chain reaction (qPCR), low throughput fluorescence based methods,
and microarray technologies, the field has shifted in recent years to primarily
performing RNA sequencing (RNA-seq) to catalog whole transcriptomes. As such
next generation sequencing technologies continue to fall in price and rise in
throughput, applying deep learning to study gene expression data is likely to
make training deep models more feasible. With increased modeling ability, deep
learning approaches are likely to grow in popularity and lead to novel
biological insights.

Already several deep learning approaches have been applied to gene expression
data with varying aims. For instance, many researchers have applied unsupervised
deep learning models to extract meaningful representations of gene modules
or sample clusters. Denoising autoencoders have been used to cluster yeast
expression microarrays into known modules representing cell cycle processes
[@AnenJOuU] and also to stratify yeast strains based on
chemical and mutational perturbations [@yVBx9Qx4]. Shallow
(one hidden layer) denoising autoencoders have also been fruitful in extracting
biological insight from thousands of _Pseudomonas aeruginosa_ experiments
[@1CFhfCyWN; @zuLdSQx3] and in aggregating features relevant
to specific breast cancer subtypes [@PBiRSdXv]. These unsupervised
approaches applied to gene expression data are powerful methods for aggregating
features and identifying gene signatures that may otherwise be overlooked by
alternative methods. An additional benefit of unsupervised approaches is that
ground truth labels, which are often difficult to acquire or are incorrect, are
nonessential. However, careful interpretation must be performed regarding how
the genes are agregated into features. Precisely attributing node activations to
specific biological functions risks overinterpreting models and can lead to
incorrect conclusions.

Alternatively, deep learning approaches are also being applied for gene
expression prediction tasks. For example, a deep neural network with
three hidden layers outperformed linear regression in inferring the expression
of over 20,000 target genes based on a representative, well-connected set of
about 1,000 landmark genes [@12QQw9p7v]. However, while the deep
learning model outperformed already existing algorithms in nearly every
scenario, the model still displayed poor performance. The paper was also limited
by computational bottlenecks that required data to be split randomly into two
distinct models and trained separately. It is unclear how much performance
would have increased if not for computational restrictions. Furthermore, a
convolutional neural network applied to histone modifications, termed
DeepChrome, [@G10wkFHt] was shown to predict gene expression
output. DeepChrome greatly improved high or low expression prediction accuracy
over existing methods. Deep learning applied to epigenetic data for gene
expression inference is a promising approach to study gene regulation. Deep
learning approaches have also been applied to study cancer gene expression data
with goals of identifying subtypes of patients with different molecular features
and clinical manifestations [@1EtavGKI4]. In the study, the
authors combine RBMs to integrate gene expression, DNA methylation, and miRNA
data and use the constructed features in search of ovarian cancer subtypes.
While the aforementioned approaches are promising, many convert gene expression
measurements to categorical or binary variables thus ablating many complex gene
expression signatures present in intermediate and relative numbers.

Deep learning applied to gene expression data is in its infancy but the future
is bright. Many hypotheses can now be interrogated because of increasing
amounts of data and new developing technologies. For example, there is a
growing appreciation for the large impact of disease heterogeneity on research
and treatment strategies for disease. New technologies are being developed,
such as single cell RNA-seq and high throughput fluorescence based imaging that
are good matches for deep learning. Concurrently, deep learning methods are
being developed to address novel problems such as adjusting for batch effects in
single-cell RNA-seq data [@T2Md9xLY]. Moreover, deep
learning is already well established in the image processing community, so the
marriage of fluorescence based imaging techniques and deep learning is natural.
These technologies are growing in popularity and will provide increasingly novel 
perspectives with respect to how cellular heterogeneity impacts gene expression
coordination within a sample. In general, as the flow of gene expression data
increases, and techniques to integrate heterogeneous genomic measurements made
on the same samples are enhanced, the quality and types of questions deep
learning can address is poised to improve.

### Splicing

Pre-mRNA transcripts can be spliced into different isoforms by retaining or
skipping subsets of exons, or including parts of introns. This alternative
splicing provides cells with enormous spatiotemporal flexibility to generate
multiple distinct proteins from a single gene. Splicing is catalyzed by small
nuclear RNAs (snRNAs) and spliceosomal proteins, which detect sequence motifs
such as splice sites and exon sequence enhancers and silencers (ESE and ESS).
Various RNA-binding proteins and noncoding RNAs can bias these reactions by
altering binding affinities, blocking splice sites, or sequestering splicing
factors. This remarkable complexity unfortunately lends itself to defects that
underlie many diseases [@QFK6GapR]. For instance, in Becker
muscular dystrophy, a point mutation in dystrophin creates an ESS that induces
skipping of exon 31. A recent study found that quantitative trait loci (QTLs)
that affect splicing in lymphoblastoid cell lines are enriched within risk loci
for schizophrenia, multiple sclerosis and other immune diseases, implicating
mis-splicing as a much more widespread feature of human pathologies than
previously thought [@b6p6wxpC].

Sequencing studies routinely return thousands of unannotated variants. Which
cause functional changes in splicing, and if so, how? Prediction of a “splicing
code” has been a holy grail over the past decade. Initial machine learning
approaches used a naive Bayes model and a 2-layer Bayesian neural network with
thousands of hand-derived sequence-based features to predict the probability of
exon skipping [@11ETDdRKr; @8VPGUHcf]. With the
advent of deep learning, more complex models were built that provided better
predictive accuracy [@17sgPdcMT; @N0HBi8MH]. Importantly, these new approaches can take in
not only genomic features, but also tissue identity and CLIP-seq measurements of
interactions between splicing factors and RNA, which all improve predictive
accuracy.

The massive improvement seen with deep learning seems to stem from hidden layers
being able to create new higher-order “features”, whereas earlier approaches
often assumed independence of features and were unable to generalize.
Higher-order understanding is especially important in splicing, which depends
not only on the primary sequence, but also local RNA structure, tissue identity,
splicing factor binding, and other currently unknown factors — all of which
interact in complex, incompletely characterized ways. With new tools to
interpret these meta-features, a major focus of current deep learning research,
we will soon have the ability to extract a more nuanced biological understanding
of splicing — perhaps by interrogating informative hidden nodes within neural
networks that take in tissue type as part of the input, or by building separate
networks for each tissue type and looking for common versus distinctive nodes
[@Qbtqlmhf].

A parallel effort has been to use more data with simpler models. An exhaustive
study using readouts of splicing for millions of synthetic intronic sequences
was able to describe motifs that influence the strength of alternative splice
sites [@mlqKTlZY]. Interestingly, they built a simple
linear model using hexamer motif frequencies that successfully generalized to
exon skipping: in a limited analysis using SNPs from three genes, it predicted
exon skipping with three times the accuracy of Xiong et al.’s framework. This
case is instructive in that clever sources of data, not just more powerful
models, can lead to novel insights.

We already understand how mis-splicing of a single gene can cause diseases such
as Duchenne muscular dystrophy. The challenge now is to uncover how alternative
splicing genome-wide gives rise to or is involved in complex, non-Mendelian
diseases such as autism, schizophrenia, Type 1 diabetes, and multiple sclerosis
[@CNz9HwZ3]. As a proof of concept, Xiong et al.
[@17sgPdcMT] sequenced five ASD and 12 control samples, each
with an average of 42,000 rare variants, and identified 19 genes with neural
functions that are mis-spliced. Deep learning will allow scientists and
clinicians to rapidly profile thousands of unannotated variants for functional
effects on splicing and nominate candidates for further investigation. Moreover,
these nonlinear algorithms can deconvolve the effects of multiple variants on a
single splice event without the need to perform combinatorial in vitro
experiments.

Our end goal is to predict an individual’s tissue-specific, exon-specific
splicing patterns from their genome sequence and other measurements. Knowing
exactly which genes are mis-spliced in each tissue could enable a new branch of
precision diagnostics that also stratifies patients and suggests targeted
therapies to correct splicing defects. A continued focus on interpreting the
“black box” of deep neural networks, along with integrating more comprehensive
and diverse data sources, will likely provide the path forward to a better
understanding of the basic determinants of splicing and its links to complex
disease, which will lead to novel diagnostics and therapeutics.

### Transcription factors and RNA-binding proteins

Transcription Factor and RNA-binding proteins are key components for gene
regulation, making them very important to understand for higher level
biological processes. While high-throughput sequencing techniques such as
chromatin immunoprecipitation and massively parallel DNA
sequencing (ChIP-seq) have been able to accurately identify binding regions
for DNA and RNA proteins, these experiments are both time consuming and
expensive. In addition, the sequencing methods do not provide any sort of
analysis on the proteins which would lead to a better understanding of
the underlying process. Thus, there is a need to computationally predict
and understand these binding regions de novo from sequences.

#### Transcription Factors

Transcription Factors (TFs) are regulatory proteins that bind to certain
locations on a DNA sequence and control the rate of mRNA
production. ChIP-seq and related technologies are able to identify highly
likely binding sites for a certain TF, and databases such as
ENCODE [@1Bs5k1MVg] have provided ChIP-seq
data for hundreds of different TFs across many laboratories.
However, ChIP-seq experiments are expensive and time consuming.
Since the data that scientists have discovered is available, in
silico methods to predict binding sites are of great interest, thus
eliminating the need to do new ChIP-seq experiments every
time analysis is done on a new sequence.

In order to computationally predict TFBSs on a DNA sequence, researchers
initially used consensus sequences and position weight matrices to match
against a test sequence [@ywDQIvZJ]. Simple neural network
classifiers were then proposed to differentiate positive and negative binding
sites, but did not show significant improvements over the weight matrix
matching methods [@uZvDdFZo]. Later, SVM techniques
outperformed the generative methods by using k-mer features
[@JxuQvvyk; @138dgb9Ca], but string kernel based SVM
systems are limited by expensive computational cost proportional to the number
of training and testing sequences. More recently,
[@2UI1BZuD] showed that convolutional neural network
models could achieve state of the art results on the TFBS task and are scalable
to a large number of genomic sequences. [@Dwi2eAvT] introduced
several new convolutional and recurrent neural network models for predicting
TFBSs, but it remains unclear which neural architectures work best for all
samples and TFs. While neural architectures are rapidly changing and producing
better results, it is clear that deep learning can be efficiently and
effectively used to do functional prediction on the genome given raw data.

While accurately predicting transcription factors computationally is useful,
it is important to understand how these computational models make their
predictions. To handle this, several papers have focused on understanding
machine learning models [@2UI1BZuD; @Dwi2eAvT; @xAbGxia4].
[@2UI1BZuD] was the first to introduce a visualization
method for a deep learning model on the TFBS task, and they did so by
visualizing the learned convolution filters which were informative for the
model’s prediction of a specific sample. However, this approach was specific to
visualizing certain samples fed through their particular model.
[@Dwi2eAvT] introduced a suite of state-of-the-art deep
learning models and new visualizations techniques for a more in-depth analysis
of TFBSs. Furthermore, [@xAbGxia4] introduced an advanced
visualization method and toolbox for analyzing possible TFBS sequences.
[@2UI1BZuD] also introduced mutation maps, where they could
easily mutate, add, or delete basepairs in a sequence and see how the model
changed its prediction. This is something that would be very time consuming
in a lab setting, but easy to simulate using their model. Visualization
techniques on deep learning models are important because they can provide
new insights on regulatory mechanisms and can lead biologists to test and
verify in a lab setting, leading to new biomedical knowledge. Since the
“linguistics” of DNA are unclear, interpretability of models is crucial to
pushing our understanding forward.

`TODO: Add discussion about the large number of deep learning works
in this area since the DeepBind paper. In particular, add
[#43](https://github.com/greenelab/deep-review/issues/43),
[#215](https://github.com/greenelab/deep-review/issues/215),
and [#258](https://github.com/greenelab/deep-review/issues/258).`

### Promoters, enhancers, and related epigenomic tasks

*We may want to be selective about what we discuss and not list every
application in this area.*

### Micro-RNA binding

*miRNAs are important biologically, but have neural networks produced anything
particularly notable in this area?*

### Protein secondary and tertiary structure

Proteins play fundamental roles in all biological processes including the 
maintenance of cellular integrity, metabolism, transcription/translation, and 
cell-cell communication. Complete description of protein structures and 
functions is a fundamental step towards understanding biological life and 
also highly relevant in the development of therapeutics and drugs. UnitProt 
currently has about 94 millions of protein sequences. Even if we remove 
redundancy at 50% sequence identity level, UnitProt still has about 
20 millions of protein sequences. However, fewer than 100,000 proteins 
have experimentally-solved structures in Protein Data Bank (PDB). As a result, 
computational structure prediction is essential for a majority number of 
protein sequences. However, predicting protein 3D structures from sequence alone 
is very challenging, especially when similar solved structures (called templates) 
are not available in PDB. In the past decades, various computational methods have 
been developed to predict protein structure from different aspects, 
including prediction of secondary structure, torsion angles, solvent accessibility, 
inter-residue contact map, disorder regions and side-chain packing.

Machine learning is extensively applied to predict protein structures and 
some success has been achieved. For example, secondary structure can be 
predicted with about 80% of 3-state (i.e., Q3) accuracy by a neural network 
method PSIPRED [@cRuWK1eG]. Starting from 
2012, deep learning has been gradually introduced to protein structure 
prediction. The adopted deep learning models include deep belief network, 
LSTM(long short-term memory), deep convolutional neural networks (DCNN) 
and deep convolutional neural fields[@pNoAbBEu; @UO8L6nd]. Here we focus on deep learning methods for 
two representative subproblems: secondary structure prediction and 
contact map prediction. Secondary structure refers to local conformation of 
a sequence segment while a contact map contains information of global 
conformation. Secondary structure prediction is a basic problem and almost 
an essential module of any protein structure prediction package. It has also
been used as sequence labeling benchmark in the machine learning community. 
Contact prediction is much more challenging than secondary structure prediction,
but it has a much larger impact on tertiary structure prediction. 
In recent years, contact prediction has made good progress and its accuracy 
has been significantly improved [@BhfjKSY3; @7atXz0r; @kboAopkh; @10dNuD89l].

Protein secondary structure can exhibit three different states (alpha helix, 
beta strand and loop regions) or eight finer-grained states. More methods are 
developed to predict 3-state secondary structure than 8-state. A predictor is 
typically evaluated by 3-state (i.e., Q3) and 8-state (i.e., Q8) accuracy, respectively. 
Qi et al. developed a multi-task deep learning method to simultaneously predict several 
local structure properties including secondary structures [@1AlhRKQbe]. 
Spencer, Eickholt and Cheng predicted secondary structure using deep belief networks 
[@ZzaRyGuJ]. Heffernan and Zhou et al. developed an iterative 
deep learning framework to simultaneously predict secondary structure, backbone torsion 
angles and solvent accessibility [@UpFrhdJf]. However, none of these deep 
learning methods achieved significant improvement over PSIPRED [@Aic7UyXM] 
in terms of Q3 accuracy. In 2014, Zhou and Troyanskaya demonstrated that they could 
improve Q8 accuracy over a shallow learning architecture conditional neural fields [@NnpYUsi] 
by using a deep supervised and convolutional generative stochastic network[@8t43CQ9m], 
but did not report any results in terms of Q3 accuracy. In 2016 Wang and Xu et al. developed a deep 
convolutional neural fields (DeepCNF) model that can significantly improve secondary 
structure prediction in terms of both Q3 and Q8 accuracy[@UO8L6nd]. 
DeepCNF possibly is the first that reports Q3 accuracy of 84-85%, much higher than 
the 80% accuracy maintained by PSIPRED for more than 10 years. 
It is also reported that DeepCNF can improve prediction of solvent accessibility 
and disorder regions [@pNoAbBEu]. This improvement may be mainly 
due to the introduction of convolutional neural fields to capture long-range 
sequential information, which is important for beta strand prediction. Nevertheless, 
improving secondary structure prediction from 80% to 84-85% is unlikely to 
result in a similar amount of improvement in tertiary structure prediction since secondary
structure mainly reflects coarse-grained local conformation of a protein structure.

Protein contact prediction and contact-assisted folding (i.e., folding proteins using 
predicted contacts as restraints) represents a promising new direction for ab initio folding 
of proteins without good templates in PDB. 
Evolutionary coupling analysis (ECA) is an effective contact prediction method for some 
proteins with a very large number (>1000) of sequence homologs [@10dNuD89l], 
but ECA fares poorly for proteins without many sequence homologs. Since (soluble) proteins with 
many sequence homologs are likely to have a good template in PDB, to make contact-assisted 
folding practically useful for ab initio folding, it is essential to predict accurate contacts 
for proteins without many sequence homologs. By combining ECA with a few other protein features, 
shallow neural network-based methods such as MetaPSICOV [@7atXz0r] and 
CoinDCA-NN [@kqjqFesT] have shown some advantage over ECA 
for proteins with a small number of sequence homologs, but their accuracy is still not very good. 
In recent years, deep learning methods have been explored for contact prediction. For example, 
Di Lena et al. introduced a deep spatio-temporal neural network (up to 100 layers) that utilizes both 
spatial and temporal features to predict protein contacts[@xdoT1yUx]. 
Eickholt and Cheng combined deep belief networks and boosting techniques to predict protein contacts 
[@18bNbDNlc] and trained deep networks by layer-wise unsupervised 
learning followed by fine-tuning of the entire network. Skwark and Elofsson et al. developed 
an iterative deep learning technique for contact prediction by stacking a series of Random Forests 
[@F13xtRbV]. However, blindly tested in the well-known CASP competitions, 
these methods did not show any advantage over MetaPSICOV [@7atXz0r], a method 
using two cascaded neural networks. Very recently, Wang and Xu et al. proposed a novel deep learning method 
RaptorX-Contact [@BhfjKSY3] that can significantly improve contact prediction 
over MetaPSICOV especially for proteins without many sequence homologs. RaptorX-Contact employs a network 
architecture formed by one 1D residual neural network and one 2D residual neural network. 
Blindly tested in the latest CASP competition (i.e., CASP12 [@zScWGveU]), 
RaptorX-Contact is ranked first in terms of the total F1 score (a widely-used performance metric) on 
free-modeling targets as well as the whole set of targets. In the CASP12 test, the group ranked second 
also employed a deep learning method. Even MetaPSICOV, which ranked third in CASP12, employed more
and wider hidden layers than its old version. Wang and Xu et al. have also 
demonstrated in another blind test CAMEO (which can be interpreted as a fully-automated 
CASP) [@u9uApoaB] that their predicted contacts can help fold quite a few proteins 
with a novel fold and only 65-330 sequence homologs and that their method also works well on membrane 
protein contact prediction even if trained mostly by non-membrane proteins. In fact, most of the top 10 
contact prediction groups in CASP12 employed some kind of deep learning techniques. The RaptorX-Contact 
method performed better mainly due to introduction of residual neural networks and exploiting contact
occurrence patterns by simultaneous prediction of all the contacts in a single protein. 
It is still possible to further improve contact prediction by studying new deep network architectures. 
However, current methods fail when proteins in question have almost no sequence homologs. It is unclear if there
is an effective way to deal with this type of proteins or not except waiting for more sequence homologs.
Finally, the deep learning methods summarized above also apply to interfacial contact prediction 
of a protein complex, but may be less effective since on average protein complexes have fewer sequence homologs. 

### Signaling

*There is not much content here.  Can [@rmjDc5rm] be covered
elsewhere?*

### Morphological phenotypes

A field poised for dramatic revolution by deep learning is
bioimage analysis.
Thus far, the primary use of deep learning for biological
images has been for segmentation - that is, for the identification
of biologically relevant structures in images such as nuclei,
infected cells, or vasculature, in fluorescence or even brightfield
channels [@40EG4ZEU]. Once so-called regions of
interest have been identified, it is often straightforward
to measure biological properties of interest, such as fluorescence
intensities, textures, and sizes. Given the dramatic successes of
deep learning in biological imaging, we simply refer to articles that
review recent advancements [@MmRGFVUu; @40EG4ZEU; @TutLhFSz].
We believe deep learning will become a commonplace tool for
biological image segmentation once user-friendly tools exist.

We anticipate an additional kind of paradigm shift in bioimaging that
will be brought about by deep learning: what if images of biological
samples, from simple cell cultures to three-dimensional organoids and
tissue samples, could be mined for much more extensive biologically
meaningful information than is currently standard? For example, a
recent study demonstrated the ability to predict lineage fate in
hematopoietic cells up to three generations in advance of
differentiation [@On4vW5aU]. In biomedical research,
by far the most common paradigm is for biologists to decide in advance
what feature to measure in images from their assay system. But images
of cells contain a wide variety of quantitative information, and deep
learning may just be the tool to extract it. Although classical methods
of segmentation and feature extraction can produce hundreds of metrics
per cell in an image, deep learning is unconstrained by human intuition
and can in theory extract more subtle features. Already, there is evidence
deep learning can surpass the efficacy of classical methods
[@gllSeTW], even using generic deep convolutional networks
trained on natural images [@BMg062hc], known as transfer learning.

The impact of further improvements on biomedicine could be enormous.
Comparing cell population
morphologies using conventional methods of segmentation and feature
extraction has already proven useful for functionally annotating genes
and alleles, identifying the cellular target of small molecules, and
identifying disease-specific phenotypes suitable for drug screening
[@hkKO4QYl; @m3Ij21U8; @McjXFLLq].
Deep learning would bring to these new kinds of experiments - known
as image-based profiling or morphological profiling - a higher degree of
accuracy, stemming from the freedom from human-tuned feature extraction
strategies.

`TODO: Make sure that at the end we clearly emphasize our excitement around
unsupervised uses.`

### Single-cell

Single-cell methods are generating extreme excitement as biologists recognize
the vast heterogeneity within unicellular species and between cells of the same
tissue type in the same organism [@1AWC7HsO0]. For instance,
tumor cells and neurons can both harbor extensive somatic variation
[@1GvfSy48x]. Understanding single-cell diversity in all its
dimensions — genetic, epigenetic, transcriptomic, proteomic, morphologic, and
metabolic — is key if precision medicine is to be targeted not only to a
specific individual, but also to specific pathological subsets of cells.
Single-cell methods also promise to uncover a wealth of new biological
knowledge. A sufficiently large population of single cells will have enough
representative “snapshots” to recreate timelines of rapid biological processes.
If tracking processes over time is not the limiting factor, single cell
techniques can provide maximal resolution compared to averaging across all cells
in bulk tissue, enabling the study of transcriptional bursting with single-cell
FISH or the heterogeneity of epigenetic patterns with single-cell Hi-C or
ATAC-seq [@QafUwNKn; @v97iPXDw].

However, large challenges exist in studying single cells. Relatively few cells
can be assayed at once using current droplet, imaging, or microwell
technologies, and low-abundance molecules or modifications may not be detected
by chance in a phenomenon known as dropout. To solve this problem, Angermueller
et al. [@19EJTHByG] trained a neural network to predict
the presence or absence of methylation of a specific CpG site in single cells
based on surrounding methylation signal and underlying DNA sequence, achieving
several percentage points of improvement compared to random forests or deep
networks trained only on CpG or sequence information. Similar deep learning
methods have been applied to impute low-resolution ChIP-seq signal from bulk
tissue with great success, and they could easily be adapted to single cell data
[@Qbtqlmhf; @XimuXZlz].

Examining populations of single cells can reveal biologically meaningful subsets
of cells as well as their underlying gene regulatory networks
[@1HPu3R2B4]. Unfortunately, machine learning generally struggles
with unbalanced data — when there are many more inputs of class 1 than class 2 —
because prediction accuracy is usually evaluated over the entire dataset. To
tackle this challenge, Arvaniti et al. [@r3Gbjksq]
classified healthy and cancer cells expressing 25 markers by using the most
discriminative filters from a CNN trained on the data as a linear classifier.
They achieved an impressive precision of 50% to 90% with 80% recall on cells
where the subset percentage ranged from 0.1 to 1%, which significantly
outperformed logistic regression and distance-based outlier detection methods.
However, they did not benchmark against random forests, which tend to be better
with unbalanced data, or against the neural network itself, and their data was
fairly low dimensional. Future work will be needed to establish the utility of
deep learning in cell subset identification, but the stunning improvements in
image classification over the past 5 years [@j7KrVyi8] suggest that
this goal will be achievable.

The sheer quantity of “omic” information that can be obtained from each cell, as
well as the number of cells in each dataset, uniquely position single-cell data
to benefit from deep learning. In the future, lineage tracing could be
revolutionized by using autoencoders to reduce the feature space of
transcriptomic or variant data followed by algorithms to learn optimal cell
differentiation trajectories [@Oljj2W96], or by feeding cell
morphology and movement into neural networks
[@On4vW5aU]. Reinforcement learning algorithms
[@2gn6PKkv] could be trained on the evolutionary dynamics of
cancer cells or bacterial cells undergoing selection pressure and reveal whether
patterns of adaptation are random or deterministic, allowing us to develop
therapeutic strategies that forestall resistance. It will be exciting to see the
creative applications of deep learning to single-cell biology that emerge over
the next few years.

`TODO: https://github.com/greenelab/deep-review/issues/153`

### Metagenomics

`TODO: Add reference tags to this section`
Metagenomics (which refers to the study of genetic material, 16S rRNA 
and/or whole-genome shotgun DNA, from microbial communities) has 
revolutionized the study of micro-scale ecosystems within us and around us. 
There is increasing literature of applying machine learning in general to 
metagenomic analysis.  In the late 2000’s, a plethora of machine learning 
methods were applied to classifying DNA sequencing reads to the thousands of 
species within a sample.  An important problem is genome assembly from these 
mixed-organism samples. And to do that, the organisms should be “binned” 
before assembling.  Binning methods began with many k-mer techniques [@N9NzkOjA] 
and then delved into other clustering algorithms, such as self-organizing maps 
(SOM) [@1HhqhBwrM].  Then came the taxonomic classification problem,  with researchers 
naturally using BLAST [@s9ycaHcq], followed by other machine learning techniques 
such as SVMs [@QV551Nlx], naive Bayesian classifiers [@1HtJuEkb2], etc. to classify
each read.  Then, researchers began to use techniques that could be used to 
estimate relative abundances of an entire sample, instead of the precise but
painstakingly slow read-by-read classification.  Relative abundance
estimators (a.k.a diversity profilers) are MetaPhlan [@56wEWVIl], (WGS)Quikr [@RqhGD9c7],
and some configurations of tools like OneCodex [@EbkFuLrS] and LMAT [@189TQrQA9].  While one
cannot identify which reads were mapped back to an organism using relative
abundance estimators, they can be useful for faster comparative and other
downstream analyses.   Newer methods hope to classify reads and estimate
relative abundances at faster rates [@8DLzxOEt] and as of this writing, there
are more than 70 metagenomic taxonomic classifiers in existence.  Besides
binning and classification of species, there is functional identification and
annotation of sequence reads [@qUGH5CX8; @yFOAeemA]. However, the focus on
taxonomic/functional annotation is just the first step.  Once organisms are
identified, there is the interest in understanding the interrelationship
between these organisms and host/environment phenotypes [@W0cYSf89].  One of
the first attempts was a survey of supervised classification methods for
microbes->phenotype classification [@aI9g2UOc], followed by similar studies
that are more massive in scale [@c5P9jHCg; @y9s5irW].  There have been
techniques that bypass the taxonomic classification step altogether [@5W4KMSdT],
(sequence composition to phenotype classification).  Also, researchers have
looked into how feature selection can improve classification [@Kt9NojjR; @y9s5irW],
and techniques have been proposed that are classifier-independent
[@1AN5UPfb1; @O9D66oYa].

So, how have neural networks (NNs) been of use?    Most neural networks are being 
used for short sequence->taxa/function classification, where there is a lot of data 
for training (and thus suitable for NNs).  Neural networks have been applied 
successfully to gene annotation (e.g. Orphelia [@q1A2AEtO] and FragGeneScan [@QlbXLqH]), 
which usually has plenty of training examples.  Representations (similar to Word2Vec [@1GhHIDxuW] in 
natural language processing) for protein family classification has been introduced and classified 
with a skip-gram  neural network [@1E1PWjqTm].  Recurrent neural networks show good performance for 
homology and protein family identification [@G8RKF6sz; @81Cl5QSM].  Interestingly, 
Hochreiter, who invented Long Short Term Memory, delved into homology/protein family
classification in 2007, and therefore, deep learning is deeply rooted in
functional classification methods.

One of the first techniques of “de novo” genome binning used self-organizing maps, a 
type of NN [@1HhqhBwrM].  Essinger et al. use ART, a neural network algorithm called Adaptive 
Resonance Theory, to cluster similar genomic fragments and showed that it has better 
performance than K-means.  However, other methods based on interpolated Markov models 
[@c4rnN1wo] have performed better than these early genome binners.  Also, neural networks 
can be slow, and therefore, have had limited use for reference-based taxonomic 
classification, with TAC-ELM [@Wz7VUS03] being the only NN-based algorithm to taxonomically 
classify massive amounts of metagenomic data.  Also, neural networks can fail to perform 
if there are not enough training examples, which is the case with taxonomic classification 
(since only ~10% of estimated species have been sequenced). An initial study shows that 
deep neural networks have been successfully applied to  taxonomic classification of 16S rRNA genes,
with convolutional networks  provide about 10% accuracy genus-level improvement over RNNs and even random 
forests [@iPIJrVVs].  However, this study performed 10-fold cross-validation on 3000 sequences in total. 

Due to the traditionally small numbers of metagenomic samples in studies, neural network uses for 
classifying phenotype from microbial composition are just beginning.   A standard MLP 
was able to classify wound severity from microbial species present in the wound [@oas5tbC7].
Recently, multi-layer, recurrent networks (and convolutional
networks) have been applied to microbiome genotype-phenotype, with Ditzler et
al. being the first to associate soil samples with pH level using multi-layer
perceptrons, deep-belief networks, and recursive neural networks (RNNs) 
[@i38A0beL]. Besides classifying the samples appropriately, Ditzler shows
that internal phylogenetic tree nodes inferred by the networks are
appropriate features representing low/high pH, which can provide additional
useful information and new features for future metagenomic sample comparison.
 Also, an initial study has show promise of these networks for diagnosing
disease [@NQ5jiN7B].  

There are still a lot of challenges with applying deep neural networks to metagenomics problems.  They are not ideal for microbial/functional composition->phenotype classification because most studies contain tens of samples (~20->40) and
hundreds/thousands of features (aka species).  Such underdetermined/ill-conditioned problems
are still a challenge for deep neural networks that require many more training examples than 
features to sufficiently converge the weights on the hidden layers.  Also, due to convergence issues 
(slowness and instability due to large neural networks modeling very large datasets [@g2vvbB91]), 
taxonomic classification of reads from whole genome sequencing seems out of reach at the moment for deep neural 
networks -- due to only thousands of full-sequenced genomes as compared to hundreds of thousands of 16S rRNA sequences 
available for training.

However, because recurrent neural networks are showing success for base-calling (and thus removing the large error in 
the measurement of a pore's current signal) for the relatively new Oxford Nanopore sequencer [@1BTJ1KqRa], there is hope that
the process of denoising->organism/function classification can be combined into one step in using powerful LSTM's. LSTM's
are working miracles in raw speech signal->meaning translation [@2cMhMv5A], and combining steps in metagenomics are not
out of the question.  For example, metagenomic assembly usually requires binning then assembly, but could deep neural nets
accomplish both tasks in one network? Does functional/taxonomic classification need to be separate processes?  The largest 
potential in deep learning is to learn "everything" in one complex network, with a plethora of labeled (reference) data and
unlabeled (microbiome experiments) examples.

### Sequencing and variant calling

*We have one nanopore paper in the issues and very recent work on variant calling
that looks worthy of inclusion.*


## The impact of deep learning in treating disease and developing new treatments

*There will be some overlap with the Categorize section, and we may have to
determine which methods categorize individuals and which more directly match
patients with treatments.  The sub-section titles are merely placeholders.*

### Categorizing patients for clinical decision making

There has been sustained interest in applying deep learning to clinical
decision making for over two decades. In 1996, Tu
[@kL0B4m9d] compared the effectiveness of artificial
neural networks and logistic regression, questioning whether deep learning
would replace traditional statistical methods for predicting medical
outcomes such as myocardial infarction [@jdg2u7bX] or
mortality [@xX68eyvs]. He posited that while neural
networks have several advantages in representational power, the difficulties in
interpretation may limit clinical applications. In 2007, Lisboa and Taktak
[@qxxwkSAT] examined the use of artificial neural
networks in medical journals, concluding that neural networks provided an
increase in benefit to healthcare relative to traditional screening methods in
21 of 27 studies.

While significant progress has been made in developing deep learning methods
for diagnosis, it is not clear that these methods have yet transformed
clinical decision making. The difficulty in applying deep learning to clinical
decision making represents a challenge common to many deep learning
applications: it is much easier to predict an outcome than to suggest an
action to change the outcome. Several attempts at recasting the clinical
decision making problem into a prediction problem (i.e. prediction of which
treatment will most improve the patient's health) have accurately predicted
prescription habits, but technical and medical challenges remain for clinical
adoption. In particular, remaining challenges include actionable
interpretability of deep learning models, fitting deep models to limited and
heterogeneous data, and integrating complex predictive models into a dynamic
clinical environment.

#### Applications

##### Trajectory Prediction for Treatment

A common application for deep learning techniques in this domain is to
leverage the temporal structure of healthcare records. As previously
discussed, many studies [@4zpZxjHR; @O7Vbecm2; @fOaBA9Vc; @glyI7H6F]
have used deep recurrent networks to categorize patients but most stop short
of suggesting clinical decisions. Nemati et al [@16OQvsRqJ]
used deep reinforcement learning to optimize a heparin dosing policy for
intensive care patients. However, because the ideal dosing policy is unknown,
the model's predictions must be evaluated on counter-factual data. This
represents a common challenge when bridging the gap between research and
clinical practice: because the ground-truth is unknown, researchers struggle
to evaluate model predictions in the absence of interventional data, but
clinical application is unlikely until the model has been shown to be effective
. The impressive applications of deep reinforcement learning to other domains
[@2gn6PKkv] have relied on knowledge of the underlying
processes (e..g the rules of the game). Some models have been developed for
targeted medical problems [@eCrLGgiX], but a
generalized engine is beyond current capabilities. Further development of the
rules underlying biological processes could unleash deep learning methods that
are currently hampered by the difficulties of counter-factual inference.

##### Efficient Clinical trials

A clinical task to deep learning which has been more successfully applied is
the assignment of patients to clinical trials. Ithapu et al
[@eehGXQlY] used a randomized denoising autoenconder to
learn a multimodal imaging marker that predicts future cognitive and neural
decline from positron emission tomography (PET), amyloid
florbetapir PET, and structural magnetic resonance imaging. By accurately
predicting which cases will progress to dementia, they were able to
efficiently assign patients to a clinical trial and reduced the required
sample sizes by a factor of five.  Similarly, Artemov et al
[@mo3GQwJj] applied deep learning to predict which clinical trials
were likely to fail and which were likely to succeed. By predicting the side
effects and pathway activations of each drug, and then translating these
activations to a success proability, their deep learning-based approach was
able to significantly outperform a random forest classifier trained on gene
expression changes. These approaches suggest promising directions to improve
the efficiency of clinical trials and accelerate drug development.

#### Challenges

##### Actionable Interpretability

A common challenge in many applied deep learning problems is the consideration
of deep learning models as uninterpretable "black boxes". Without human-
intelligible reasoning for the model's predictions, it is difficult to trust
the model. This presents a major challenge for the risk-averse task of
clinical decision making. As described above, there has been some work to
directly assign treatment plans without interpretability; however, the removal
of human experts from the decision-making loop make the models difficult to
integrate with clinical practice. To alleviate this challenge, several studies
have attempted to create more interpretable deep models, either specifically
for healthcare or as a general procedure for deep learning.

For domain-specific models, studies have primarily focused on integrating
attention mechanisms with the neural networks. Attention mechanisms
dynamically weight the importance the neural network gives to each feature. By
inspecting the attention weights for a particular sample, a practitioner can
identify the important features for a particular prediction. Choi et al
[@UcRbawKo] inverted the typical architectue of recurrent neural
networks to improve interpretability. In particular, they only used recurrent
connections in the attention generating procedure, leaving the hidden state
directly connected to the input variables. This model was able to produce
accurate diagnoses in which the contribution of previous hospital visits could
be directly interpreted. Choi et al [@10nDTiETi] later extended this
work to take into account the structure of disease ontologies and found that
the concepts represented by the model were aligned with medical knowledge. Che
et al [@14DAmZTDg] introduced a knowledge-distillation approach which
used gradient boosted trees to learn interpretable healthcare features from
trained deep models.

As this challenge of interpretability is common across many domains, there is
significant interest in developing generic procedures for knowledge extraction
from deep models. Ribeiro et al [@QwXSJhr0] focus on interpreting
individual predictions rather than interpreting the model. By fitting simple
linear models to mimic the predictions of the deep learning model in a small
neighborhood of a data sample, they generated an interpretable model for each
prediction. While this procedure can provide interpretable models for each
sample, it is unclear whether these interpretable models are reliable.
Theoretical guarantees on the curvature of the predictions of deep learning
models are not known, and it is unclear whether predictions from deep learning
models are robust to sample noise. Toward quantifying the uncertainty of
predictions, there has been a renewed interest in confidence intervals for
deep neural networks. Early work from Chryssolouris et al
[@9SnNyc8Y] provided confidence intervals under the assumption of
normally distributed error. However, Nguyen et al [@1AkF8Wsv7] showed
that the confidence of convolutional neural networks is not reliable; they can
output confidence scores over 99.99% even for samples that are purely noise.
Recently, Fong and Vedaldi [@y4t9EzPn] provided a framework for
understanding black box algorithms by perturbing input data. Further work in
interpreting predictions and understanding the knowledge learned by deep
neural networks seem necessary for transformative impact in clinical practice.

##### Integrating Deep Learning with Clinical Practice

As deep learning models are difficult to interpret, many current models have
been designed to replace aspects of clinical practice rather than to assist
trained clinicians. This makes it difficult to integrate deep learning with
clinical decision making. In addition, the challenges that physicians face are
largely similar to those faced by machine learning models. For a given
patient, the number of possible diseases is very large, with a long tail of
rare diseases. Furthermore, patients are highly heterogeneous and may present
with very different signs and symptoms for the same disease. Physicians are
experienced in treating patients with common diseases, but rare diseases are
extremely challenging. Unfortunately, machine learning methods also struggle
for rare diseases. Because deep learning models are data-intensive, directly
applying current deep learning models to diagnose patients with rare diseases
would require prohibitively large datasets. Focused effort in reducing the
data requirements of deep learning by integrating pre-existing knowledge or
compiling large datasets of patient records may unlock the power of deep
learning for clinical practice.

### Effects of drugs on transcriptomic responses

*We discussed a few papers that operate on Library of Network-Based Cellular
Signatures (LINCS) gene expression data.  We could briefly introduce the
goals of that resource and comment on the deep learning applications.  In the
Issues, we had reservations about whether the improvements in expression
prediction are good enough to make a practical difference in the domain and
feature selection and construction.*

### Ligand-Based Prediction of Bioactivity

**TODO: expand outline**

- Short introduction to problem, related reviews, use vHTS definition from
[@cjj5vT3H] (vHTS doesn't fit neatly into classic classification,
regression, or ranking)
- Introduce ligand-based approaches, hype and excitement surrounding
performance of a "high-parameter" network on the Merck Kaggle challenge,
cover other neural networks trained on fingerprints or descriptors as features
that followed, Tox21 Data Challenge
- Multitask networks related to the above point
- Realistic view of where things stand today, high-parameter networks struggle
with overfitting, cross validation needs to be done carefully because of temporal
structure [@uP7SgBVd], low parameter networks based on chemical
similarity (IRV) work very well, especially well-suited for the domain in which
training data can be limited and contains few positive instances, may touch on
BACE example here and other discussions of training data limitations (e.g.
[@HRoooKGh])
- "Creative experimentation" phase of the field, new ideas for representation
learning and novel approaches including graph convolutions, autoencoders,
one shot learning, and generative models
- These "creative" approaches are definitely interesting but aren't necessarily
outperforming existing methods, improvements on the software and
reusability side could be important to help establish more rigorous
benchmarking, DeepChem as example of this
- Future outlook, what would need to happen for the "creative" approaches
to overtake the current state of the art, can representation learning be
improved by incorporating more information about chemical properties or
even more "tasks" during training, how much will future growth depend on
data versus algorithms
- Future outlook part 2, how the above approaches relate to traditional
methods like docking (note neural networks that include docking scores as
features), deep learning efforts in this direction that use structure (e.g.
[@Z7fd0BYf; @bNBiIiTt]), "zero-shot learning",
analogies to other domains where deep learning can capture the behavior
of complex physics (e.g. quantum physics example), maybe briefly mention
other compound-protein interaction-based networks although that doesn't seem
to fit here and is somewhat out of scope
- Future output part 3 (most speculative), what would successful generative
networks mean for the HTS field?

### Modeling Metabolism and Chemical Reactivity

*Add a review here of metabolism and chemical reactivity.*


## Discussion

*This section provides meta-commentary that spans the Categorize, Study, and
Treat subject areas.  The candidate sub-sections below are initial ideas that
can be further pruned.*

### Evaluation

*What are the challenges in evaluating deep learning models that are specific to
this domain?  This can include a discussion of ROC versus precision-recall
curves for the imbalanced classes often encountered in biomedical datasets.
It could also mention alternative metrics that are used in specific sub-areas
such as enrichment factors in virtual screening.  A lack of true gold standard
data for some problems complicates both training and evaluation.  Confidence-
weighted labels are valuable when available.*

*Is progress in some biomedical areas slowed when new predictions (e.g. from
generative models) cannot be assessed by any human expert and require
experimental testing?  For example, contrast a painting or song generated by
a GAN versus a novel chemical compound.  Related is the idea that on some tasks
(e.g. the recent wave of deep learning versus MD image classification papers)
it is easy to tell when deep learning has produced a breakthrough because
human-level performance is an impressive baseline.  In many tasks we reviewed,
human-level performance is irrelevant.*

### Interpretation

*Most of our examples pertain to the Study papers.  Does this discussion
belong there or can we generalize it and keep it here?  Specific points would
include the dangers of over-interpreting hidden units, pros/cons of specific
techniques (see issues), and recommendations.  LIME and DeepLIFT are specific
strategies.  Some other reviews have addressed this in part as well.*

### Data limitations

*Related to evaluation, are there data quality issues in genomic, clinical, and
other data that make this domain particularly challenging?  Are these worse than
what is faced in other non-biomedical domains?*

*Many applications have used relatively small training datasets.  We might
discuss workarounds (e.g. semi-synthetic data, splitting instances, etc.) and
how this could impact future progress.  Might this be why some studies have
resorted to feature engineering instead of learning representations from low-
level features?  Is there still work to be done in finding the right low-level
features in some problems?*

### Hardware limitations and scaling

*Several papers have stated that memory or other hardware limitations
artificially restricted the number of training instances, model inputs/outputs,
hidden layers, etc.  Is this a general problem worth discussing or will it be
solved naturally as hardware improves and/or groups move to distributed deep
learning frameworks?  Does hardware limit what types of problems are accessible
to the average computational group, and if so, will that limit future progress?
For instance, some hyperparameter search strategies are not feasible for a lab
with only a couple GPUs.*

*Some of this is also outlined in the Categorize section.  We can decide where
it best fits.*

Efficiently scaling deep learning is challenging, and there is a high
computational cost (e.g., time, memory, energy) associated with training neural
networks and using them for classification. As such, neural networks
have only recently found widespread use [@BQS8ClV0].

Many have sought to curb the costs of deep learning, with methods ranging from
the very applied (e.g., reduced numerical precision [@CKcJuj03; @1G3owNNps; @w6CoVmFK; @1GUizyE8e]) to the exotic
and theoretic (e.g., training small networks to mimic large networks and
ensembles [@1AhGoHZP9; @1CRF3gAV]). The largest
gains in efficiency have come from computation with graphics processing units
(GPUs) [@F3e4wfzQ; @NSgduYNT; @IULiPa6L; @13KjSCKB2; @1FocAi7N0; @BQS8ClV0], which excel at the matrix and vector
operations so central to deep learning. The massively parallel nature of GPUs
allows additional optimizations, such as accelerated mini-batch gradient
descent [@NSgduYNT; @IULiPa6L; @aClNvbyM; @fNkl8HFz]. However, GPUs also have a limited quantity of memory,
making it difficult to implement networks of significant size and
complexity on a single GPU or machine [@F3e4wfzQ; @CCS5KSIM]. This restriction has sometimes forced
computational biologists to use workarounds or limit the size of an analysis.
For example, Chen et al. [@12QQw9p7v] aimed to infer the
expression level of all genes with a single neural network, but due to
memory restrictions they randomly partitioned genes into two halves and
analyzed each separately. In other cases, researchers limited the size
of their neural network [@W3grN7jy; @2dU8f4XJ]. Some have also chosen to use slower
CPU implementations rather than sacrifice network size or performance
[@x0M6vals].

Steady improvements in GPU hardware may alleviate this issue somewhat, but it
is not clear whether they can occur quickly enough to keep up with the growing
amount of available biological data or increasing network sizes. Much has
been done to minimize the memory
requirements of neural networks [@YwdqeYZi; @1AhGoHZP9; @CKcJuj03; @1G3owNNps; @w6CoVmFK; @15lYGmZpY; @1GUizyE8e], but there is also growing
interest in specialized hardware, such as field-programmable gate arrays
(FPGAs) [@1FocAi7N0; @9NKsJjSw] and
application-specific integrated circuits (ASICs). Specialized hardware promises
improvements in deep learning at reduced time, energy, and memory
[@1FocAi7N0]. Logically, there is less software for highly
specialized hardware [@9NKsJjSw], and it could be a difficult
investment for those not solely interested in deep learning. However, it is
likely that such options will find increased support as they become a more
popular platform for deep learning and general computation.

Distributed computing is a general solution to intense computational
requirements, and has enabled many large-scale deep learning efforts. Early
approaches to distributed computation [@xE3EYmck; @1XcexUAV] were
not suitable for deep learning [@17cBimWgp],
but significant progress has been made. There
now exist a number of algorithms [@17cBimWgp; @HIiQN4bd; @w6CoVmFK], tools [@rmJZ2Aui; @rZnxDitd; @Gp4OR9Lf], and high-level libraries [@FwEK0msb; @y9IoEy4r] for deep
learning in a distributed environment, and it is possible to train very complex
networks with limited infrastructure [@4MZ2tmZ8]. Besides
handling very large networks, distributed or parallelized approaches offer
other advantages, such as improved ensembling [@JUF9VoRD] or
accelerated hyperparameter optimization [@wz83yfHF; @Wsa952Ax].

Cloud computing, which has already seen adoption in genomics
[@B6g0qKf4], could facilitate easier sharing of the large
datasets common to biology [@1E7bFCRV4; @q0SsFrZd],
and may be key to scaling deep learning. Cloud computing affords researchers
significant flexibility, and enables the use of specialized hardware (e.g.,
FPGAs, ASICs, GPUs) without significant investment. With such flexibility, it
could be easier to address the different challenges associated with the
multitudinous layers and architectures available
[@ZSVsnPVO]. Though many are reluctant to store sensitive
data (e.g., patient electronic health records) in the cloud,
secure/regulation-compliant cloud services do exist [@ObFN78yp].

*TODO: Write the transition once more of the Discussion section has been
fleshed out.*

### Code, data, and model sharing

*Reproducibiliy is important for science to progress. In the context of deep
learning applied to advance human healthcare, does reproducibility have
different requirements or alternative connotations? With vast hyperparameter
spaces, massively heterogeneous and noisy biological data sets, and black box
interpretability problems, how can we best ensure reproducible models? What
might a clinician, or policy maker, need to see in a deep model in order to
influence healthcare decisions? Or, is deep learning a hypothesis generation
machine that requires manual validation? DeepChem and DragoNN are worth
discussing here.*

### Transfer learning/transferability of features

* https://github.com/greenelab/deep-review/issues/139#issuecomment-268901804


## Conclusions

Final thoughts and future outlook here. The Discussion will give an overview
and the Conclusion will provide a short, punchy take home message.

Points to mention based on discussion thus far that may make the bar for
conclusions:

* Limitations of data & workarounds (availability impacts on amount, etc)
* Transferability of features
* Strong enthusiasm for unsupervised approaches.
* Right to an explanation (possibly, depends if raised in multiple areas)

### Author contributions

`TODO: not sure if it should go here, but somewhere we should talk about how we
wrote this thing, since it is still somewhat unconventional to have a review
written in this manner.` We recognized that writing a review on a rapidly
developing area in a manner that allowed us to provide a forward-looking
perspective on diverse approaches and biological problems would require
expertise from across computational biology and medicine. We created an open
repository on the GitHub version control system and engaged with numerous
authors from papers within and outside of the area. Paper review was conducted
in the open by `#` individuals, and the manuscript was drafted in a series of
commits from `#` authors. Individuals who met the ICJME standards of authorship
are included as authors. These were individuals who contributed to the review of
the literature; drafted the manuscript or provided substantial critical
revisions; approved the final manuscript draft; and agreed to be accountable in
all aspects of the work. Individuals who did not contribute in one or more of
these ways, but who did participate, are acknowledged at the end of the
manuscript.
