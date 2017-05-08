## Deep learning and patient categorization

In a healthcare setting, individuals are diagnosed with a disease or condition
based on symptoms, the results of certain diagnostic tests, or other factors.
Once diagnosed with a disease an individual might be assigned a stage based on
another set of human-defined rules. While these rules are refined over time, the
process is evolutionary rather than revolutionary.

We might imagine that deep learning or artificial intelligence methods could
reinvent how individuals are categorized for healthcare. A deep neural network
might identify entirely new categories of health or disease that are only
present when data from multiple lab tests are integrated. As a potential
example, consider the condition Latent Autoimmune Diabetes in Adults (LADA). The
history of this disease classification is briefly reviewed in Stenström et
al.[@doi:10.2337/diabetes.54.suppl_2.S68].

Imagine that a deep neural network operating in the early 1980s had access to
electronic health records with comprehensive clinical tests. It might have
identified a subgroup of individuals with blood glucose levels that indicated
diabetes as well as auto-antibodies, even though the individuals had never been
diagnosed with type 1 diabetes - the autoimmune form of the disease that arises
in young people. Such a neural network would be identifying patients with LADA.
As no such computational approach existed, LADA was actually identified by Groop
et al. [@doi:10.2337/diab.35.2.237]. However, this represents a potential hope
of this area. Perhaps deep neural networks, by reevaluating data without the
context of our assumptions, can reveal novel classes of treatable conditions.

Alternatively, imagine that a deep neural network is provided with clinical test
results gleaned from electronic health records. Because physicians may order
certain tests based on the diagnosis that they suspect a patient has, a deep
neural network may learn to "diagnose" patients simply based on the tests that
are ordered. For some objective function this may offer good performance (i.e.
predicting an ICD code), even though it does not provide insight into the
underlying disease beyond physician activity. This challenge is not unique to
deep learning approaches; however, it is important for practitioners to be aware
of these challenges and the possibility in this domain of constructing highly
predictive classifiers of questionable actual utility.

Our goal in this section is to assess the extent to which deep learning is
already contributing to the discovery of novel categories. Where it isn't, we
focus on barriers to achieving these goals. We also highlight approaches that
researchers are taking to address challenges within the field, particularly with
regards to data availability and labeling.

#### Imaging applications in healthcare

One area where deep learning methods have had substantial success has been in
image analysis. Applications in areas of medicine that use imaging extensively
are also emerging. To the date, deep learning has been employed for a wide
range of tasks in medical imaging, including classification of exams and
lesions/nodules, localization of organs, regions, landmarks, and lesions,
segmentation of organs, organ substructures, and lesions, medical image
registration, content-based image retrieval, image generation and enhancement,
and combining image data with clinical reports [@tag:Litjens2017_medimage_survey
@tag:Shen2017_medimg_review].

Closest to natural images are applications of deep learning aimed at
detection and recognition of melanoma, the deadliest form of skin cancer.
Recent works included applications to both dermoscopy
[@tag:Codella2016_ensemble_melanoma @tag:Yu2016_melanoma_resnet] and
non-dermoscopic clinical photography images of skin lesions
[@tag:Jafari2016_skin_lesions @tag:Esfahani2016_melanoma
@tag:Esteva2017_skin_cancer_nature]. For both modalities pre-training on natural
images appears to be common model initialization that allows the use of very
deep networks without overfitting. Reported performance is competitive or better
compared to a board of certified dermatologists
[@tag:Codella2016_ensemble_melanoma @tag:Esteva2017_skin_cancer_nature].
This approach is known as transfer learning (see Discussion).

Another fast emerging area of deep learning method applications is detection of
ophthalmological diseases such as diabetic retinopathy and age-related macular
degeneration. Diagnosis of diabetic retinopathy through color fundus images
became of interest for deep learning researchers and practitioners after the
large labeled image set was made publicly available during the corresponding
2015 Kaggle competition [@tag:Pratt2016_dr]. Most attempts included training
a network from scratch [@tag:Pratt2016_dr @tag:Abramoff2016_dr
@tag:Leibig2016_dr], while Gulshan et al. [@tag:Gulshan2016_dt] employed
48-layer Inception-v3 deep architecture pre-trained on natural images and
demonstrated substantial increase over the state-of-the-art in both specificity
and sensitivity. Interestingly, Leibig et al. [@tag:Leibig2016_dr] proposed a
method to estimate the uncertainty of deep networks in diabetic retinopathy
diagnosis based on a recent theoretical insight on the link between dropout
networks and approximate Bayesian inference. Such developments are important
for the whole medical image analysis field, because they have a potential to
provide information about a level of confidence for every black-box algorithm's
classification result and, thus, improve pathologist-computer interaction.
Deep networks were also recently applied to age-related macular degeneration
detection, similarly demonstrating the power of transfer learning when training
set is limited [@tag:Burlina2016_amd] as well as the efficient use of a deep
16-layer architecture combined with EMR data for training set enrichment.

Mammography has been one area with numerous contributions
[@tag:Dhungel2015_struct_pred_mamm @tag:Dhungel2016_mamm
@tag:Zhu2016_mult_inst_mamm @tag:Zhu2016_advers_mamm
@tag:Dhungel2017_mamm_min_interv]. In the most of this work, the researchers
must work around a typical for the domain challenge - the limited number of
well annotated training images. To expand the number and diversity of images,
the researchers have employed approaches where they use adversarial examples
[@tag:Zhu2016_advers_mamm] or first train towards human-created features before
subsequent fine tuning [@tag:Dhungel2016_mamm]. Adaptation to the medical image
domain can further improved by combining in the latter approach with other
machine learning techniques, for example, as a cascade of deep learning and
random forest models [@tag:Dhungel2017_mamm_min_interv]. Using large dataset,
Kooi et al. [@tag:Kooi2016_mamm_lesions] demonstrated that deep neural
networks can outperform the traditional computer-aided diagnosis (CAD)
system at low sensitivity and perform comparably at high sensitivity.
They also compared network performance to certified screening
radiologists on a patch level and found no significant difference between the
network and the readers. Similarly, Geras et al. [@tag:Geras2017_multiview_mamm]
showed that both using large dataset and using multi-view network architecture
help to improve classification performance. The presence of a publicly available
large bank of well-annotated mammography images would aid in the application
of deep neural networks to this area and shift research focus from model
generalization to effective processing of large image sets. Deep network
pre-trained on large annotated mammogram set can be helpful for related tasks
that do not have as much data using transfer learning [@tag:Kooi2017_mamm_tl].
Though this strategy has not yet been employed in this domain, high-quality
feature detectors can be constructed from large collections of unlabeled images
in an unsupervised context. The small number of labeled examples could
be used for subsequent training. Similar strategies have been employed for
EHR data where high-quality labeled examples are also difficult to obtain
[@tag:BeaulieuJones2016_ehr_encode].

In radiological image analysis, deep learning techniques are increasingly used
even when dataset size is not big enough to train large capacity models from
scratch [@tag:Bar2015_nonmed_tl @tag:Shin2016_cad_tl
@tag:Rajkomar2017_radiographs @tag:Lakhani2017_radiography]. All these
studies demonstrate successful transfer of features learnt from natural image
datasets, such as ImageNet [@tag:Russakovsky2015_imagenet]. Rajkomar et al.
[@tag:Rajkomar2017_radiographs] showed that a deep CNN trained on natural
images can boost performance in radiology image classification. However, the
target task required either re-training the initial model from scratch with
special pre-processing or fine-tuning of the whole network on radiographs with
heavy data augmentation to avoid overfitting. Shin et al. [@tag:Shin2016_cad_tl]
compared various deep network architectures, dataset characteristics, and
training procedures for computer tomography-based (CT) abnormality detection.
They concluded that in case of three-dimensional data networks as deep as 22
layers can be useful for such problems despite the limited size of training
datasets. However, they note, that choice of a specific architecture,
parameter setting, and model fine-tuning needed is very problem and
dataset-specific. Moreover, this type of tasks often depends on both lesion
localization and appearance that pose challenges for CNN-based approaches.
Straightforward attempts to capture useful information from full-size images
in all three dimensions simultaneously make applications of standard neural
network architectures computationally unfeasible due to the curse of
dimensionality. Instead, two dimensional models are often used to either process
image slices individually (2D), or aggregate information from a number of 2D
projections in the native space (2.5D). Roth et al. compared 2D, 2.5D, and
3D CNNs on a number of tasks for computer-aided detection from CT scans and
showed that 2.5D CNNs performed comparably well to 3D analogs, while requiring
much less training time, especially on augmented training sets
[@tag:Roth2015_view_agg_cad]. Another advantage of 2D and 2.5D networks is a
possibility to use widely available models pre-trained on natural images.

Similarly, in magnetic resonance image (MRI) analysis, limited size of training
sets and large dimensionality represent challenges to deep learning
applications. For example, Amit et al. [@tag:Amit2017_breast_mri] investigated
the tradeoffs between using pre-trained models from a different domain and
retraining a small-size CNN on MRI images. They showed that smaller network
trained with sufficient data augmentation on few hundred images from a
few dozen patients can outperform a pre-trained out-of-domain classifier.
Nie et al. [@tag:Nie2016_3d_survival] showed that multimodal, multi-channel
3D deep architecture was successful at learning high-level brain tumor
appearance features jointly from MRI, functional MRI and diffusion MRI images,
outperforming single-modality or 2D models. Overall, the variety of modalities,
properties and sizes of training sets, dimensionality of input, and, finally,
the importance of end goals in medical image analysis are provoking a
development of specialized deep neural network architectures, training and
validation protocols, and input representations that are not characteristic of
widely studied natural images.

In addition to medical imaging, histology slides are also being analyzed
with deep learning approaches [@tag:Litjens2016_histopath_survey].
Ciresan et al. [@tag:Ciresan2013_mitosis]
developed one of the earliest examples, winning the 2012 International
Conference on Pattern Recognition's Contest on Mitosis Detection while
achieving human competitive accuracy. Their approach uses what has become a
standard convolutional neural network architecture trained on public data.
In more recent work, Wang et al. [@tag:Wang2016_breast_cancer] analyzed stained
slides to identify cancers within slides of lymph node slices. The approach
provided a probability map for each slide. On this task a pathologist has about
a 3% error rate. The pathologist did not produce any false positives, but did
have a number of false negatives. While the algorithm had about twice the
error rate of a pathologist, the errors were not strongly correlated with those
of a pathologist, suggesting that the two could be combined, theoretically,
reducing error rate to under 1%. In this area, these algorithms may be ready to
incorporate into existing tools to aid pathologists. The authors' work suggests
that this could reduce the false negative rate of such evaluations. This theme
of an ensemble between deep learning algorithm and human expert may help
overcome some of the challenges presented by data limitations.

One source of training examples with rich clinical annotations is the electronic
health records. Recently Lee et al.[@tag:Lee2016_emr_oct_amd] developed an
approach to distinguish individuals with age-related macular degeneration
from control individuals. They extracted approximately 100,000 images from
structured electronic health records, which they used to train and evaluate a
deep neural network. Combining this data resource with standard deep learning
techniques, the authors reach greater than 93% accuracy. One item that is
important to note with regards to this work is that the authors used their test
set for evaluating when training had concluded. In other domains, this has
resulted in a minimal change in the estimated accuracy
[@tag:Krizhevsky2013_nips_cnn]. However, there is not yet a single accepted
standard within the field of biomedical research for such evaluations.
We recommend the use of an independent test set wherever it is feasible.
Despite this minor limitation, the work clearly illustrates the potential that
can be unlocked from images stored in electronic health records.

These examples demonstrate that, except for few natural image-like problems
(e.g. melanoma detection), biomedical imaging poses a number of challenges for
deep learning applications. Dataset sizes are typically limited, annotations
can be sparse, and images are often high-dimensional, multimodal, and
multi-channel. Techniques like transfer learning, heavy dataset augmentation,
multi-view and multi-stream architectures are used more commonly compared
to natural image domain. Furthermore, sensitivity and specificity of a model
in this case often can translate directly into a clinical value. Thus,
results evaluation, uncertainty estimation, and model interpretation methods are
also of great importance in this domain (see Discussion). Finally, there is
a need for better pathologist-computer interaction techniques that will allow
to combine the power of deep learning methods with human expertise and
lead to better informed decisions for patient treatment and care.

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

In recent work, Yoon et al.[@tag:Yoon2016_cancer_reports] analyzed simple
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
This demonstrates how deep learning methods can repurpose features across tasks,
improving overall predictions as the field tackles new challenges. For the
further review of this type of approaches see Discussion.

Several authors have created reusable feature sets for medical terminologies
using natural language processing (NLP) and neural embedding models, as
popularized by Word2vec [@tag:Word2Vec]. A goal of learning terminologies
for different entities in the same vector space is to find relationships
between different domains (e.g. drugs and the diseases they treat). It is
difficult for us to provide a strong statement on the broad utility of these
methods. Manuscripts in this area tend to compare algorithms applied to the
same data but lack a comparison against overall best-practices for one or more
tasks addressed by these methods. Techniques have been developed for free text
medical notes [@doi:10.1145/2661829.2661974], ICD and NDC, and claims data
[@doi:10.1145/2939672.2939823]. Methods for neural embeddings learned from
electronic health records have at least some ability to predict disease-disease
associations and implicate genes with a statistical association with a disease
[@doi:10.1038/srep32404]. However, the evaluations performed did not
differentiate between simple predictions (i.e. the same disease in different
sites of the body) and non-intuitive ones. While promising, a lack of rigorous
evaluations of the real-world utility of these kinds of features makes
current contributions in this area difficult to evaluate. To examine the true
utility, comparisons need to be performed against leading approaches (i.e.
algorithms and data) as opposed to simply evaluating multiple algorithms on
the same potentially limited dataset.

Identifying consistent subgroups of individuals and individual health
trajectories from clinical tests is also an active area of research. Approaches
inspired by deep learning have been used for both unsupervised feature
construction and supervised prediction. Early work by Lasko et al.
[@doi:10.1371/journal.pone.0066341], combined sparse autoencoders and Gaussian
processes to distinguish gout from leukemia from uric acid sequences. Later work
showed that unsupervised feature construction of many features via denoising
autoencoder neural networks could dramatically reduce the number of labeled
examples required for subsequent supervised analyses
[@doi:10.1016/j.jbi.2016.10.007 @doi:10.1101/039800]. In addition, it pointed
towards learned features being useful for subtyping within a single disease. In
a concurrent large-scale analysis of EHR data from 700,000 patients, Miotto et
al. [@doi:10.1038/srep26094] used a deep denoising autoencoder architecture
applied to the number and co-occurrence of clinical events ("DeepPatient") to
learn a representation of patients. The model was able to predict disease
trajectories within one year with over 90% accuracy and patient-level
predictions were improved by up to 15% when compared to other methods. Razavian
et al. [@arxiv:1608.00647] used a set of 18 common lab tests to predict disease
onset using both CNN and LSTM architectures and demonstrated and improvement
over baseline regression models. However, numerous challenges including data
integration (patient demographics, family history, laboratory tests, text-based
patient records, image analysis, genomic data) and better handling of streaming
temporal data with many features, will need to be overcome before we can fully
assess the potential of deep learning for this application area.

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
stratified patients as a function of disease risk score compared to the current
clinical implementation.

There is a computational cost for these methods, however, when compared to
traditional, non-network approaches. For the exponential family models, despite
their scalability [@arxiv:1206.7051], an important question for the investigator
is whether he or she is interested in estimates of posterior uncertainty. Given
that these models are effectively Bayesian neural networks, much of their
utility simplifies to whether a Bayesian approach is warranted for a given
increase in computational cost. Moreover, as with all variational methods,
future work must continue to explore just how well the posterior distributions
are approximated, especially as model complexity increases [@arxiv:1511.02386].

##### Challenges and opportunities in patient categorization

###### Generating ground-truth labels can be expensive or impossible

A dearth of true labels is perhaps among the biggest obstacles for EHR-based
analyses that employ machine learning. Popular deep learning (and machine
learning) methods are often used to tackle classification tasks and thus require
ground-truth labels for training.  For EHRs this can mean that researchers must
hire multiple clinicians to manually read and annotate individual patients'
records through a process called chart review. This allows researchers to assign
"true" labels, i.e. those that match our best available knowledge. Depending on
the application, sometimes the features constructed by algorithms also need to
be manually validated and interpreted by clinicians. This can be time consuming
and expensive [@doi:10.1016/j.ijmedinf.2016.09.014]. Because of these costs,
much of this research, including the work cited in this review, skips the
process of expert review. Clinicians' skepticism for research without expert
review may greatly dampen their enthusiasm for the work and consequently reduce
its impact. To date, even well-resourced large national consortia have been
challenged by the task of acquiring enough expert-validated labeled data. For
instance, in the eMERGE consortia and PheKB database
[@url:https://phekb.org/implementations], most samples with expert validation
contain only 100 to 300 patients. These datasets are quite small, even for
simple machine learning algorithms. The challenge is greater for deep learning
models with many parameters. While unsupervised and semi-supervised approaches
can help with small sample sizes, the field would benefit greatly from large
collections of anonymized records in which a substantial number of records have
undergone expert review. This challenge is not unique to EHR-based studies. Work
on medical images, -omics data in applications for which detailed metadata are
required, and other applications for which labels are costly to obtain will be
hampered as long as abundant curated data are unavailable.

Successful approaches to date in this domain have sidestepped this challenge by
making methodological choices that either reduce the need for labeled examples
or that use transformations to training data to increase the number of times it
can be used before overfitting occurs. For example, the unsupervised and
semi-supervised methods that we've discussed reduce the need for labeled
examples [@doi:10.1016/j.jbi.2016.10.007]. The anchor and learn framework
[@doi:10.1093/jamia/ocw011] uses expert knowledge to identify high confidence
observations from which labels can be inferred. The adversarial training example
strategies that we've mentioned can reduce overfitting, if transformations are
available that preserve the meaningful content of the data while transforming
irrelevant features [@doi:10.1101/095786]. While adversarial training examples
can be easily imagined for certain methods that operate on images, it's more
challenging to figure out what an equivalent transformation would be for a
patient's clinical test results. Consequently, it may be hard to employ
adversarial training examples, not to be confused with generative adversarial
neural networks, with other applications. Finally, approaches that transfer
features can also help use valuable training data most efficiently. Rajkomar et
al. trained a deep neural network using generic images before tuning using only
radiology images [@doi:10.1007/s10278-016-9914-9]. Datasets that require many of
the same types of features might be used for initial training, before fine
tuning takes place with the more sparse biomedical examples. Though the analysis
hasn't yet been attempted, it's possible that analogous strategies may be
possible with electronic health records. For example, features learned from the
electronic health record for one type of clinical test (e.g. a decrease over
time in a lab value) may transfer across phenotypes.

Methods to accomplish more with little high-quality labeled data are also being
applied in other domains and may also be adapted to this challenge, e.g. data
programming [@arxiv:1605.07723]. In data programming, noisy automated labeling
functions are integrated. Numerous writers have described data as the new oil
[@url:http://ana.blogs.com/maestros/2006/11/data_is_the_new.html,
@url:https://medium.com/twenty-one-hundred/data-is-the-new-oil-a-ludicrous-proposition-1d91bba4f294].
The idea behind this metaphor is that data are available in large quantities,
valuable once refined, and the underlying resource that will enable a
data-driven revolution in how work is done. Contrasting with this perspective,
Ratner, Bach, and Ré described labeled training data as "The _New_ New Oil"
[@url:http://hazyresearch.github.io/snorkel/blog/weak_supervision.html]. In this
framing, data are abundant and not a scarce resource. Instead, new approaches to
solve problems arise when labeled training data become sufficient to enable
them. Based on our review of research on deep learning methods to categorize
disease, the latter framing rings true.

We expect improved methods for domains with limited data to play an important
role if deep learning is going to transform how we categorize states of human
health. We don't expect that deep learning methods will replace expert review.
We expect them to complement expert review by allowing more efficient use of the
costly practice of manual annotation.

###### Data sharing is hampered by standardization and privacy considerations

To construct the types of very large datasets that deep learning methods thrive
on, we need robust sharing of large collections of data. This is in part a
cultural challenge. We touch on this challenge in the Discussion section. Beyond
the cultural hurdles around data sharing, there are also technological hurdles
related to sharing individual health records or deep models built from such
records. This subsection deals primarily with these challenges.

EHRs are designed chiefly for clinical, administrative and financial purposes,
such as patient care, insurance and  billing [@doi:10.1038/nrg3208]. Research is
at best a tertiary priority, presenting  significant challenges to EHR-based
research in general, and particularly to data intensive deep learning research.
These difficulties can be grouped into three areas: local bias, wider standards
and legal issues. Note these problems are not restricted to EHR but can also
apply to any large biomedical dataset, e.g. clinical trial data.

Even within the same healthcare system, EHRs can be used differently
[@pmid:24159271 @pmid:21347133]. Individual users have unique usage patterns,
with different departments and different hospitals having different priorities
which code patients and introduce missing data in a non-random fashion
[@doi:10.1016/S0168-8510(02)00208-7]. Patient data may be kept across several
"silos" within a single health system. Even the most basic task of matching
patients across systems can be challenging due to data entry issues
[@pmid:27134610]. The situation is further exacerbated by the ongoing
introduction, evolution and migration of EHR systems, especially where
reorganized and acquired healthcare facilities have to merge. As a result, EHR
can be less complete and less objective than expected.

In the wider picture, standards for EHRs are many and evolving. Proprietary
systems, indifferent and scattered use of health information standards and
controlled terminologies makes combining and comparison of data across systems
challenging [@url:http://www.ncrr.nih.gov/publications/informatics/ehr.pdf
@doi:10.1016/j.jbi.2014.10.006]. Further diversity arises from variation in
languages, healthcare practices and demographics. Merging EHR gathered in
different systems (and even under different assumptions) is challenging
[@doi:10.1007/978-3-319-44839-8].

Combining or replicating studies across systems thus requires controlling for
both the above biases and dealing with mismatching standards. This has the
practical effect of reducing cohort size, limiting statistical significance,
preventing the detection of weak effects
[@doi:10.1590/2176-9451.19.4.027-029.ebo] and restricting the number of
parameters that can be trained in a model. Further, rules-based algorithms have
been popular in EHR-based research but because these are developed at a single
institution and trained with a specific patient population they do not transfer
easily to other populations [@doi:10.1136/amiajnl-2013-001935]. For example,
Wiley et al. [@doi:10.1142/9789813207813_0050] showed that warfarin dosing
algorithms often under-perform in African Americans, illustrating that some of
these issues are unresolved even at a treatment best practices level. Lack of
standardization also makes it challenging for investigators skilled in deep
learning to enter the field, as numerous data processing steps must be performed
before algorithms are applied.

Finally, even if data were perfectly consistent and compatible across systems,
attempts to share and combine EHR data face considerable legal and ethical
barriers. Patient privacy can severely restrict the sharing and use of EHR
[@doi:10.1093/ije/dyn022]. Here again, standards are
heterogeneous and evolving but often EHR data can often not be exported or even
accessed directly for research purposes without appropriate consent. Once again,
this has the effect of making data gathering more laborious, expansive and
reducing sample size and study power.

Several technological solutions have been proposed in this direction, allowing
access to sensitive data satisfying privacy and legal concerns. Software like
DataShield [@doi:10.1093/ije/dyu188] and ViPAR
[@doi:10.1093/ije/dyv193], although not EHR specific, allows querying and
combining of datasets and calculation of summary statistics across remote sites
by "taking the analysis to the data". The computation is carried out at the
remote site. Conversely, the EH4CR project [@doi:10.1016/j.jbi.2014.10.006]
allows analysis of private data by use of an inter-mediation layer that
intreprets remote queries across internal   formats and datastores and returns
the results in a de-identified standard form, thus giving real-time consistent
but secure access. Continuous Analysis [@doi:10.1038/nbt.3780] can allow
reproducible computing on private data. Using such techniques intermediate
results can be automatically tracked and shared without sharing the original
data. While none of these have been used in deep learning, the potential is
there.

Even without sharing data, algorithms trained on confidential patient data may
present security risks or accidentally allow for the exposure of individual
level patient data. Tramer et al. [@arxiv:1609.02943] showed the ability to
steal trained models via public APIs and Dwork and Roth
[@doi:10.1561/0400000042] demonstrate the ability to expose individual level
information from accurate answers in a machine learning model. Attackers can use
similar attacks to find out if particular data instance was present in the
original training set for the machine learning model [@arxiv:1610.05820] - in
this case, whether a person's record was present. This presents a potential
hazard for approaches that aim to generate data. Choi et al. propose generative
adversarial neural networks as a tool to make sharable EHR data
[@arxiv:1703.06490v1]; however, the authors didn't take steps to protect the
model from such attacks.

There are approaches to protect models, but they pose their own challenges.
Training algorithms in a differentially private manner provides a limited
guarantee that an algorithm's output will be equally
likely to occur regardless of the participation of any one individual. The limit
is determined by a single parameter which provides a quantification of privacy.
Simmons et al. [@doi:10.1016/j.cels.2016.04.013] present the ability to perform
GWASs in a differentially private manner and Abadi et al. [@arxiv:1607.00133]
show the ability to train deep learning classifiers under the differential
privacy framework. Federated learning
[@arxiv:1602.05629] and secure aggregations
[@url:http://proceedings.mlr.press/v54/mcmahan17a.html
@url:https://eprint.iacr.org/2017/281.pdf @tag:Papernot2017_pate]
are complementary approaches that reinforce differential privacy.
Both aim to maintain privacy by training deep learning models from
decentralized data sources such as personal mobile devices
without transferring actual training instances. This is becoming of increasing
importance with the rapid growth of mobile health applications. However, the
training process in these approaches places constraints on the algorithms used
and can make fitting a model substantially more challenging. In our own
experience it can be trivial to train a model without differential privacy, but
quite difficult to train one within the differential privacy framework. The
problem can be particularly pronounced with small sample sizes.

While none of these problems are insurmountable or restricted to deep learning,
they present challenges that cannot be ignored. Technical evolution in EHRs and
data standards will doubtless ease - although not solve - the problems of data
sharing and merging. More problematic are the privacy issues. Those applying
deep learning to the domain should consider the potential of inadvertently
disclosing the participants identity. Techniques that enable training on data
without sharing the raw data may have a part to play. Training within a
differential privacy framework may often be warranted.

###### Discrimination and "right to an explanation" laws

In April 2016, the European Union adopted new rules regarding the use of
personal information, the General Data Protection Regulation (GDPR)
[@arxiv:1606.08813v3]. A component of these rules can be summed up by the phrase
"right to an explanation". Those who use machine learning algorithms must be
able to explain how a decision was reached. For example, a clinician treating a
patient who is aided by a machine learning algorithm may be expected to explain
decisions that use the patient's data. The new rules were designed to target
categorization or recommendation systems, which inherently profile individuals.
Such systems can do so in ways that are discriminatory and unlawful `TODO:
@traversc citation needed`.

As datasets become larger and more complex, we may begin to identify
relationships in data that are important for human health but difficult to
understand. The algorithms described in this review and others like them may
become highly accurate and useful for various purposes, including within medical
practice. However, to discover and avoid discriminatory applications it will be
important to consider algorithm interpretability alongside accuracy. A number of
properties of genomic data will make this difficult.  First, Research samples are 
frequently non-representative of the general population of interest; they tend to 
be sicker [@doi:10.1086/512821], more male [@doi:10.1016/j.neubiorev.2010.07.002], 
and more European in ancestry [@doi:10.1371/journal.pbio.1001661]. One well-known 
consequence of these biases in genomics is that penetrance is consistently lower 
in the general population than would be implied by case-control data, as reviewed 
in @doi:10.1086/512821. Moreover, genetic associations that hold in one population 
may not hold in other populations with different patterns of linkage 
disequilibrium [even when population stratification is explicitly controlled for; 
@doi:10.1038/nrg2813]. As a result, many genomic findings are of limited value for 
people of non-European ancestry[@doi:10.1371/journal.pbio.1001661] and may lead
to worse treatment outcomes for them. Methods have been developed for mitigating 
some of these problems in genomic studies [@doi:10.1086/512821; 
@doi:10.1038/nrg2813], but it is not clear how easily they can be adapted for 
deep models that are designed specifically to extract subtle effects from 
high-dimensional data. For example, differences in the equipment that tended to
be used for cases versus controls have led to spurious genetic findings 
[e.g. @doi:10.1126/science.333.6041.404-a]; in some contexts, it may not be possible 
to correct for all of these differences to the degree that a deep network is 
unable to use them. Moreover, the complexity of deep networks makes it difficult
to determine when their predictions are likely to be based on such 
nominally-irrelevant features of the data [called "leakage" in other fields; 
@doi:10.1145/2382577.2382579]. When we are not careful with our data and models,
we may inadvertently say more about the way the data was collected than about
anything of scientific or predictive value, with potentially disastrous 
and discriminatory consequences [@doi:10.1111/j.1740-9713.2016.00960.x]. 
@doi:10.1145/2382577.2382579 discuss some ways in which these problems can be
mitigated, but it remains difficult to predict when they will arise, how to
diagnose them, and how to resolve them.


To reach their potential in this domain, deep learning methods will need to be
interpretable. Researchers need to consider the extent to which biases may be
learned by the model and whether or not a model is sufficiently interpretable to
identify biases. We discuss the challenge of model interpretability more
completely in the discussion section.

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
patient sizes due to discrete combinatorial bucketing. Lasko et al.
[@doi:10.1371/journal.pone.0066341] used autoencoders on longitudinal sequences
of serum urine acid measurements to identify population subtypes. More recently,
deep learning has shown promise working with both sequences (Convolutional
Neural Networks) [@arxiv:1607.07519] and the incorporation of past and current
state (Recurrent Neural Networks, Long Short Term Memory
Networks)[@arxiv:1602.00357]. This may be a particular area of opportunity for
deep neural networks. The ability to discover relevant sequences of events from
large number of trajectories requires powerful and flexible feature construction
methods - an area at which deep neural networks tend to excel.
