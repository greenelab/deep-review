## Introduction

Biology and medicine are rapidly becoming particularly data-intensive field with
respect to both research and practice. A recent comparison of genomics with
social media, online videos and other data-intensive scientific disciplines
suggested that the field of genomics alone would equal or surpass other fields
in data generation and analysis within the next decade
[@doi:10.1371/journal.pbio.1002195]. These data present new opportunities, but
also new challenges. We expect that algorithms to automatically extract
meaningful patterns and provide sufficient context to enable us to act will be
required.

Concurrent with this explosive growth in biomedical data, a new class of machine
learning algorithm has become widespread in the domain of image analysis.
Computer scientists are now building many-layered neural networks from
collections of millions of images. In a famous example, scientists from Google
demonstrated that a neural network could learn to identify cats simply by
watching online videos [@doi:10.1109/ICASSP.2013.6639343]. Such approaches,
termed deep learning, seem like a solution to the challenge presented by the
growth of data in biomedicine. Perhaps these algorithms could identify the
biological "cats" hidden in our data - the patterns that exist but that we don't
know to look for - and could act on them.

Deep learning has transformed image analysis, but researchers' initial forays
into the use of these techniques in biomedicine have been relatively limited.
There are certainly numerous promising examples, but we have not yet seen the
massive convergence on these approaches that occurred in the field of image
analysis. In this review, we discuss whether this is simply a matter of time or
if there are unique challenges posed by biomedical data that render deep
learning methods more challenging or less fruitful.

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

### Potential writing prompt

One potential future that we could imagine is a world in which data, once
gathered, is rapidly integrated into our understanding of living systems. What
we learn is rapidly put to use. Our health-related activities are constantly
monitored (e.g. by wearables) and all of our interactions with health care
systems are extensively tracked. These sources of information are combined to
help to guide our health care and maintenance. We'd be able to compare our state
and trajectory to (anonymized) others, and identify means to improve our health.
These means might contain drug combinations selected based on personalized
predictions.

### If this happens, is deep learning required for any of it? Are we any closer
### because of the advent of deep learning?

*"Categorize" and "treat" sound a bit like PMI goals. Another way to think about
this would be: do we think that deep learning will make much of a difference
for the precision medicine initiative (PMI)?*

### What is deep learning?

*Definitions, specific architectures, etc.  We may want to clarify what we mean
by "deep" learning when most methods use few hidden layers.*

### Types of biological problems

With this review, we specifically set out to address the question: "what would
need to be true for deep learning to transform how we categorize, study, and
treat individuals to maintain or restore health?." We set a high bar for the
term "transform." Specifically we sought to identify whether deep learning was a
disruptive innovation that would induce a strategic inflection point on the
practice of biology or medicine. There are numerous examples where deep learning
has been applied to biological problems and produced somewhat improved results,
and there are numerous reviews that have focused on general applications of deep
learning in biology [@doi:10.1038/nbt.3313 @doi:10.1002/minf.201501008
@doi:10.3109/10409238.2015.1135868 @doi:10.1021/acs.molpharmaceut.5b00982
@doi:10.15252/msb.20156651 @doi:10.1093/bib/bbw068]. We sought cases where deep
learning was enabling researchers to solve challenges that were previously
considered infeasible, or if it made difficult, tedious, and non-routine
analyses routine.

Based on our guiding question, we focused on the application of deep learning to
topics of biomedical importance. This covers a large range of topics. We divided
these into three broad classes based on their applied areas. We briefly
introduce the types of questions, approaches and data which are typical for each
class in the application of deep learning.

#### Disease and Patient Categorization

One important topic in the biomedical field is the accurate classification of
diseases and disease subtypes. In the oncology field, current "gold standard"
approaches are limited to either histological approaches, requiring manual
human expertise, or shallow molecular markers, such as the cell surface
receptors or small panels of genes. One example is the current PAM50 approach
in classifying breast cancer, which utilizes the expression of 50 marker
genes in order to divide breast cancer patients into four subtypes.
Significant heterogeneity still remains within these four subtypes
[@doi:10.1200/JCO.2008.18.1370 @doi:10.1158/1078-0432.CCR-13-0583]. Given the
increasing wealth of molecular data available, it seems that a more
comprehensive subtyping is possible.

Several studies have used deep learning methods in order to better categorize
breast cancer patients. For example, Tan et al. applied denoising
autoencoders (DA), an unsupervised approach, in order to cluster breast
cancer patients [@doi:10.1142/9789814644730_0014]. Ciresan et al. utilized
convolutional neural networks (CNN) to count mitotic divisions in
histological images; a feature which is highly correlated with disease
outcome [@doi:10.1007/978-3-642-40763-5_51]. Despite these recent advances, a
number of challenges exist in this area of research, such as the integration
of disparate types of data, including electronic health records (EHR),
imaging and histology data and molecular omics data.

#### Fundamental Biological Study

Broadly speaking, topics in this class aim to answer more fundamental
biological questions. Deep learning is especially suited in leveraging the
large amounts of data from high throughput omics studies. The development of
deep learning techniques and complex network architectures allow researchers
to answer fundamental biological questions with unprecedented accuracy.
`TODO: revisit "unprecedented accuracy" once we set the overall tone`. One
classic biological problem where machine learning has been extensively
applied is the prediction of molecular targets. Recent advances using deep
learning have shown higher accuracy in determining molecular targets. For
example, Lee et al. used deep recurrent neural networks (RNN) to predict gene
targets of micro-RNAs [@doi:10.1109/icnn.1994.374637]. Wang et al. used a
residual CNN to predict protein-protein contact on a genome-wide scale
[@doi:10.1101/073239]. Other biological questions that have been investigated
include the prediction of protein secondary structure based on sequence data
[@doi:10.1109/tcbb.2014.2343960 @doi:10.1038/srep18962 @doi:10.1038/srep18
962], recognition of functional genomic elements such as enhancers and
promoters [@doi:10.1101/036129 @doi:10.1007/978-3-319-16706-0_20
@doi:10.1093/nar/gk u1058], predicting the deleterious effects of nucleotide
polymorphisms [@doi:10.1093/bioinformatics/btu703], etc.

#### Patient Treatment

Studies in this category aim to recommend patient treatment, predict
treatment outcome, or guide future development of new therapies..
Specifically, effort in this area aims to identify drug targets, identify
drug interactions or predict drug response. One recent approach for
predicting drug response is the use of protein structure to predict drug
interactions and drug bioactivity through CNN [@arxiv:1510.02855]. Since CNNs
leverage spatial relationships within the data, this particular deep learning
framework is well suited to the problem. Drug discovery and drug
"repurposing" are two other hot topics. Aliper et al. used transcriptomic
data to predict which drugs might be repurposed for other diseases through
deep fully connected neural networks
[@doi:10.1021/acs.molpharmaceut.6b00248]. In a similar vein, Wang et al. used
restricted boltzman machines (RBM) to predict drug molecular targets
[@doi:10.1093/bioinformatics/btt234].
