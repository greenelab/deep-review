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
learning methods more challenging or less fruitful to apply.

### What is deep learning?

Deep learning is built on a biologically-inspired approach from machine learning
termed neural networks. Each neuron in a computational neural network, termed a
node, has inputs, an activation function, and outputs. Each value from the
inputs is usually multiplied by some weight and combined and summarized by the
activation function. The value of the activation function is then multiplied by
another set of weights to produce the output `TODO: we probably need a figure
here - I see no way that we don't include this type of description in our paper,
despite the fact that it's been done tons of times before.` These neural
networks are trained by identifying weights that produce a desired output from
some specific input.

Neural networks can also be stacked. The outputs from one can be used as inputs
to another. This process produces a stacked or multi-layer neural network. The
multi-layer neural network techniques that underlie deep learning have a long
history. Multi-layer methods have been discussed in the literature for more than
five decades [@doi:10.1103/RevModPhys.34.135]. Given this context, it's
challenging to consider "deep learning" as a new advance, though the term has
only become widespread to describe analysis methods in the last decade. For the
purposes of this review, we identify deep learning approaches as those that use
multi-layer neural networks to construct complex features from large-scale
datasets. `TODO: somehow, I feel like we should work in some of the early
examples like [@doi:10.1126/science.1127647]. I don't know if we want an entire
separate paragraph, or if we should work it into this one.`

We also identify a class of algorithms that we term "shallow learning"
approaches. We do not use this as a pejorative term, but instead to denote
algorithms which have all of the hallmarks of deep approaches except that they
employ networks of limited depth. We found it valuable to include these as we
sought to identify the current contributions of deep learning and to predict its
future impact. Researchers may employ these shallow learning methods for a
number of reasons including:

1. Shallow networks provide a degree of interpretability that better matches
   their use case.
2. The available data are insufficient to support deeper architectures, however
   new datasets that will support deep methods are expected.
3. As building blocks to be combined with other non-neural-network-based
   approaches at subsequent stages.

Deep learning is a general term for algorithms that employ multi-layer neural networks

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
