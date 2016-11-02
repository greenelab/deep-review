## Introduction

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

### General deep learning introduction

*Definitions, specific architectures, etc.  We may want to clarify what we mean
by "deep" learning when most methods use few hidden layers.*

### Types of biological problems

In this review, we are interested in the application of deep learning to 
topics of biomedical importance. This covers a large range of topics, which 
we divide into three broad classes based on their applied areas. We then 
briefly introduce the types of questions, approaches and data which are 
typical for each class in the application of deep learning.

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
to answer fundamental biological questions with unprecedented accuracy. One 
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
