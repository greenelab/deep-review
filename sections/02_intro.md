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

Concurrent with this explosive growth in biomedical data, a new enthusiasm for a
class of machine learning algorithms, known as deep learning, is revolutionizing
domains from image search to the game of Go [@doi:10.1038/nature16961]. As
recently applied to image analysis problems, these architectures readily surpass
previous best-in-class results, and computer scientists are now building
many-layered neural networks from collections of millions of images. In a famous
and early example, scientists from Google demonstrated that a neural network
could learn to identify cats simply by watching online videos
[@url:http://research.google.com/archive/unsupervised_icml2012.html].

What if, more generally, deep learning could solve the challenges
presented by the growth of data in biomedicine? Could these algorithms
identify the "cats" hidden in our data - the patterns unknown to the
researcher - and act on them? Deep learning has transformed image analysis, but
what about biomedicine more broadly? In this review,
we examine whether this transformation is simply a matter of time or
if there are unique challenges posed by biomedical data that render deep
learning methods more challenging or less fruitful to apply.

### What is deep learning?

One version:
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

Another version:

Deep learning is built on a biologically-inspired approach from machine learning
termed neural networks. Each neuron in a computational neural network, termed a
node, has inputs, an activation function, and outputs. Each value from the
inputs is usually multiplied by some weight and combined and summarized by the
activation function. The value of the activation function is then multiplied by
another set of weights to produce the output **TODO: we probably need a figure
here - I see no way that we don't include this type of description in our paper,
despite the fact that it's been done tons of times before. - I'm really partial
to this nature review's explanation about making non-linear problems linear -
figure 1 [@doi:10.1038/nature14539]** These neural networks are trained by
identifying weights that produce a desired output from some specific input.

Neural networks can also be stacked. The outputs from one network can be used as
inputs to another. This process produces a stacked, also known as a multi-layer,
neural network. The multi-layer neural network techniques that underlie deep
learning have a long history. Multi-layer methods have been discussed in the
literature for more than five decades [@doi:10.1103/RevModPhys.34.135]. Given
this context, it's challenging to consider "deep learning" as a new advance,
though the term has only become widespread to describe analysis methods in the
last decade. Much of the early history of neural networks has been extensively
covered in a recent review [@doi:10.1016/j.neunet.2014.09.003]. For the purposes
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
[@url:http://www.intel.com/pressroom/archive/speeches/ag080998.htm]. Here, we
ought to identify whether deep learning was an innovation that would induce a
strategic inflection point on the practice of biology or medicine. We considered
this with an eye towards the concept of precision medicine.

There are numerous examples where deep learning
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
[@doi:10.1109/tcbb.2014.2343960 @doi:10.1038/srep18962],
recognition of functional genomic elements such as enhancers and
promoters [@doi:10.1101/036129 @doi:10.1007/978-3-319-16706-0_20
@doi:10.1093/nar/gku1058], predicting the deleterious effects of nucleotide
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
framework is well suited to the problem. Drug repositioning is another active
area of research. Aliper et al. used transcriptomic data to predict which drugs
might be repurposed for other diseases through deep neural networks
[@doi:10.1021/acs.molpharmaceut.6b00248]. Similarly, it was shown that
restricted Boltzmann machines (RBM) can be combined into deep belief networks
(DBNs) to predict novel drug - target interactions and formulate drug
repositioning hypotheses [@doi:10.1093/bioinformatics/btt234
@doi:10.1021/acs.jproteome.6b00618]. Finally, deep learning is also being
succesfully used to prioritize chemicals in the early stages of drug discovery
for new targets [@doi:10.1080/17460441.2016.1201262].
