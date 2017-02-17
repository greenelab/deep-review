## Introduction

Biology and medicine are rapidly becoming data-intensive with
respect to both research and practice. A recent comparison of genomics with
social media, online videos and other data-intensive scientific disciplines
suggested that the field of genomics alone would equal or surpass other fields
in data generation and analysis within the next decade
[@doi:10.1371/journal.pbio.1002195]. These data present new opportunities, but
also new challenges. The data volume and complexity both indicate that
automated algorithms will be needed to extract
meaningful patterns and provide actionable knowledge allowing us to better
treat, categorize, or study disease, all within data constrained and privacy
critical environments.

Concurrent with this explosive growth in biomedical data, a new class of machine
learning algorithm - artificial neural networks, also known as deep learning -
is revolutionizing domains from X to Y (I dunno - playing chess? serving ads?).
As recently applied to image analysis problems,
these architectures are blowing away prior best-in-class results, and
computer scientists are now building many-layered neural networks from
collections of millions of images. In an early famous example, scientists from
Google demonstrated that a neural network could learn to identify cats simply by
watching online videos
[@url:http://research.google.com/archive/unsupervised_icml2012.html].

What if, more generally, deep learning could solve the challenges
presented by the growth of data in biomedicine? Could these algorithms
identify the "cats" hidden in our data - the patterns unknown to the
researcher - and act on them? Deep learning has transformed image analysis, but
what about biomedicine more broadly? In this review,
we examine whether this is simply a matter of time or
if there are unique challenges posed by biomedical data that render deep
learning methods more challenging or less fruitful to apply.

### What is deep learning?

[This section needs citations]

Deep Learning is a collection of new techniques that together have recently demonstrated 
breakthrough gains over existing approaches in several fields. 

Deep learning is built on a very old idea, neural networks, that was first
proposed in 1943 [doi:10.1007/BF02478259] as a model for how biological
brains proces information. Since then, interest in neural networks a computational
models has waxed and waned several times. This history is interesting in its own right  [@doi:10.1103/RevModPhys.34.135, @doi:10.1103/RevModPhys.34.135],
but in recent years, with the advances of Deep Learning, attention has shifted back.

Several important advances make the current surge of work done in this area possible.

First, several easy to use software packages (Tensorflow, Caffe, Theano) now enable a much broader range of scientists
to build and train complicated. In the past, neural networks required very specialized knoweldge to 
build and modify, including the ability to robustly code differentials of matrix 
expressions. Errors here are often subtle and difficult to detect, so it could be 
very difffult to tailor networks to specific problems without substantial experience
and training. Now, however, with these new packages, even very complex neural networks 
are automatically differentiated, and high level scripting instructions can transparently
run very efficently on GPUs. The technology has progressed to the point that even
algorithms can be differentiated [cite neural stack and neural memory papers].

Second, key technical insight has been uncovered that guides the construction of 
much more complicated networks that previously possible. In the past, most neural networks 
included just a single network. A network with an arbitrary number of hidden nodes, but 
just a single layer, can learn arbitrarily complex functions. And networks with more than one hidden
layer (deep networks), were hard to train. However, it turns out, deep networks can more
efficiently represent many tasks when they are built to mirror the underlying structure of the data.
Moroever, deep networks are more robust and trainable when employing several
architectural innovations: weight replication, better behaived non-linearities like rectified-linear units, residual networks, 
and better weight initialization, and persistent memory. Likewise the central role of 
dimensionality reduction as a strength of neural networks was elucidated, and this has
motivated designs built to capitalize on this strength [cite autoencoders and word2vec].

Third, several advances in training algorithms have enabled applications of neural networks in ways
not obviously possible. The number of training strategies for deep learning is growing rapidly and a complete
reveiw is beyond our scope. But these algorithms can train networks in domains where earlier algorithms struggled. 
For example, newer optimizers can very efficiently learn using batched training, where only a portion of the data
needs to be processed at a time. These optimizers more effectively optimize very large weight vectors where many weights are only
rarely updated. Noise constrastive error has proven particularly useful in 
modeling language. Reinforcement learning has enabled neural networks to learn how to play games 
like chess, GO, and poker. Curriculumn learning enables networks to gradually build up expertise to
solve particularly challenging algorithmic problems. Dropout nodes and layers make networks much more
robust, even when the number of weights are dramatically increased.

Fourth, the convergence of these factors currently makes deep learning extremely adaptable, and capable 
of addressing the nuanced differences of each domain to which it is applied. Many of the advances in deep learning
were first developed for image analysis and text analysis, but the lessons and techniques learnt there
enable the construction of very powerful models specifically suited to the challenges presented by 
each unique domain. 

### Deep learning in scientific inquiry

Given the intrinsic flexibility of deep learning, it is important to consider the specific values and goals
that are particularly important in scientific inquiry.

First, in scientific contexts understanding the patterns in the data may be just as important as fitting the data.
For this reason, interpretability can be more important here than other domains. Scientific work often 
aimes to understand the underlying principles behind the data we see, and architectures and techniques that expose the
non-obvious patterns in the data are particualrly important and very active area of research [cite examples from all sections].

Second, there are important and pressing questions about how to build networks that can efficently represent 
the underlying logic of the data. This concern of "representability" is important, because it gives insight into
the structure of scientific data, and when understood can guide the design of more efficent and effective networks. For example,
one particularly important study was published in Science, which demonstrates that a simple neural network can very efficiently and
accuratly model (i.e. respresent) a theoretically important quantum mechanical system [http://science.sciencemag.org/content/355/6325/602].

Third, science is full of domain expertise, where there are deep traditions of thought stretching back decades and even centuries. Deep learning
will always be in dialogue with thise expertise, to understand the key problems, encode the most salient prior knoweledge, and
understand how to judge success or failure. There is a great deal of excitement about deep learning, but in most scientific corners
careful thought needs to be put into bringing deep learning alongside existing experts and efforts.

Fourth, data availability and complexity is unevenly distributed accross science. Some areas of science like genomics and particle physics are swamped in petabytes and 
exobytes of high quality data. Others, like chemistry, are comparatively data poor with well developed domain specific and effective algorithms. These
differences become consequential and define the most successul approachs. For example, the convergence of lower amounts of data
and important nuances to the domain might favor lower parameter networks that incorporate domain specific knowledge and fuse data of multiple
different types. This flexibility, remember, is one of the most striking strengths of neural networks. In the long run,
it is an open question the most effect strategies will be, but in this time of creative experimenation optimism is justified.

None of these scientific concerns should dampen enthusiasm about deep learning. Rather, because the approaches flexibility,
there is good reason to believe that carefully defined networks might enbable important scientific advances.

### Will deep learning transform the study of human disease?

What would need to be true for deep learning to transform how we
categorize, study, and
treat individuals to maintain or restore health? With this review
we set out to address this question, setting a high bar for
"transform." Specifically, we sought to identify whether deep learning was a
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
[@doi:10.1200/JCO.2008.18.1370 @doi:10.1158/1078-0432.CCR-13-0583]. Given the
increasing wealth of molecular data available, a more
comprehensive subtyping seems possible.

Several studies have used deep learning methods in order to better categorize
breast cancer patients. For example, Tan et al. applied denoising
autoencoders (DA), an unsupervised approach, in order to cluster breast
cancer patients [@doi:10.1142/9789814644730_0014]. Ciresan et al. utilized
convolutional neural networks (CNN) to count mitotic divisions in
histological images; a feature that is highly correlated with disease
outcome [@doi:10.1007/978-3-642-40763-5_51]. Despite these recent advances, a
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

Although the application of deep learning to patient treatment is just beginning,
we expect a dramatic increase in methods aiming to recommend patient
treatment, predict
treatment outcome, and guide future development of new therapies.
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
