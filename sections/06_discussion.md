## Discussion

Despite the disparate types of data and scientific goals in the learning tasks
covered above, several challenges are broadly important for deep
learning in the biomedical domain.  Here we examine these factors that may
impede further progress, ask what steps have already been taken to overcome
them, and suggest future research directions.

### Evaluation

There are unique challenges to evaluating deep learning predictions in the
biomedical domain. We focus on TF binding prediction as a representative task to
illustrate some of these issues. The human genome has 3E9 base pairs, and only a
small fraction of them are implicated in specific biochemical activities. As a
result, classification of genomic regions based on their biochemical activity
results in highly imbalanced classification.  Class imbalance also arises in other problems
we review, such as virtual screening for drug discovery. What are appropriate
evaluation metrics that account for the label imbalance? The classification
labels are formulated based on continuous value experimental signals. Practitioners must determine
an appropriate procedure for formulating binary classification labels based on
these signals. In addition, the experimental signals are only partially reproducible across
experimental replicates.  An appropriate upper bound for classification
performance must account for the experimental reproducibility.

#### Evaluation metrics for imbalanced classification

Less than 1% of the genome
can be confidently labeled as bound for most transcription factors. Therefore,
it is important to evaluate the genome-wide recall and false discovery rate
(FDR) of classification models of biochemical activities. Targeted validation
experiments of specific biochemical activities usually necessitate an FDR of
5-25%. When predicted biochemical activities are used as features in other
models, such as gene expression models, a low FDR may not be as critical if the
downstream models can satisfy their evaluation criteria.  An FDR of 50% in this
context may suffice.

What is the correspondence between these metrics and commonly used
classification metrics such as auPRC and auROC? auPRC evaluates the average
precision, or equivalently, the average FDR across all recall thresholds. This
metric provides an overall estimate of performance across all possible use cases,
which can be misleading for targeted validation experiments. For example,
classification of TF binding sites can exhibit a recall of 0% at 10% FDR and
auPRC greater than 0.6. In this case, the auPRC may be competitive, but the
predictions are ill-suited for targeted validation that can only examine a few
of the highest-confidence predictions. Likewise, auROC evaluates the average recall across all false
positive rate (FPR) thresholds, which is often a highly misleading metric in
class-imbalanced domains [@doi:10.1145/1143844.1143874 @doi:10.1038/nmeth.3945].
For example, consider a classification model with recall of 0% at FDR less than
25% and 100% recall at FDR greater than 25%. In the context of TF binding
predictions where only 1% of genomic regions are bound by the TF, this is
equivalent to a recall of 100% for FPR greater than 0.33%. In other words, the
auROC would be 0.9967 and not indicative of the predictive utility for targeted
validation. It is not unusual to obtain a chromosome-wide auROC greater than
0.99 for TF binding predictions but a recall of 0% at 10% FDR. The classifier
would appear to be nearly perfect based on auROC but has no practical utility to
prioritize high-confidence binding sites for experimental validation.

#### Formulation of classification labels

Genome-wide continuous signals are commonly formulated into classification
labels through signal peak detection. For example, peaks in ChIP-seq signal are
used to identify locations of TF binding and histone modifications. Such
procedures rely on thresholding criteria to define what constitutes a peak in
the signal. This inevitably results in a set of signal peaks that are close to
the threshold, not sufficient to constitute a positive label but too similar to
positively labeled examples to constitute a negative label. To avoid an
arbitrary label for these example they may be labeled as "ambiguous".
Ambiguously labeled examples can then be ignored during model training and
evaluation of recall and FDR. The correlation between model predictions on these
examples and their signal values can be used to evaluate if the model correctly
ranks these examples between positive and negative examples.

#### Formulation of a performance upper bound

Genome-wide signals across experiments can lead to different sets of positive
examples. When experimental replicates do not completely agree, perfect recall at
a low FDR is not possible. The upper bound on the recall is the fraction of
positive examples that are in agreement across experiments. This fraction will
vary depending on the available experimental data. For example, reproducibility
for experimental replicates from the same lab is typically higher than
experimental replicates across multiple labs. One way to handle the range of
reproducibility is the use of multiple reproducibility criteria such as
reproducibility across technical replicates, biological replicates from the same
lab, and biological replicates from multiple labs.

### Interpretation

As deep learning models achieve state-of-the-art performance in a variety of
domains, there is a growing need to make the models more interpretable.
Interpretability matters for two main reasons. First, a model that achieves
breakthrough performance may have identified patterns in the data that
practitioners in the field would like to understand. However, this would not be
possible if the model is a black box. Second, interpretability is important for
trust. If a model is making medical diagnoses, it is important to ensure the
model is making decisions for reliable reasons and is not focusing on an
artifact of the data. A motivating example of this can be found in Ba and Caruana
[@tag:Caruana2014_need], where a model trained to predict the likelihood of
death from pneumonia assigned lower risk to patients with asthma, but only
because such patients were treated as higher priority by the hospital. In the
context of deep learning, understanding the basis of a model's output is
particularly important as deep learning models are unusually susceptible to
adversarial examples [@tag:Nguyen2014_adversarial] and can output confidence
scores over 99.99% for samples that resemble pure noise.

As the concept of interpretability is quite broad, many methods described as
improving the interpretability of deep learning models take disparate and often
complementary approaches. Some key themes are discussed below.

#### Assigning example-specific importance scores

Several approaches ascribe importance on an example-specific basis to the parts
of the input that are responsible for a particular output. These can be broadly
divided into perturbation-based approaches and backpropagation-based approaches.

##### Perturbation-based approaches

These approaches make perturbations to parts of the input and observe the impact
on the output of the network. Alipanahi et al. [@tag:Alipanahi2015_predicting]
and Zhou & Troyanskaya [@tag:Zhou2015_deep_sea] scored genomic sequences by
introducing virtual mutations at individual positions in the sequence and
quantifying the change in the output. Umarov et al.
[@doi:10.1371/journal.pone.0171410] used a similar strategy, but with sliding
windows where the sequence within each sliding window was substituted with a
random sequence. Kelley et al. [@tag:Kelley2016_basset] inserted known
protein-binding motifs into the centers of sequences and assessed the change in
predicted accessibility.

Ribeiro et al. [@tag:Ribeiro2016_lime] introduced LIME, which constructs a linear
model to locally approximate the output of the network on perturbed versions of
the input and assigns importance scores accordingly. For analyzing images,
Zeiler and Fergus [@tag:Zeiler2013_visualizing] applied constant-value masks to
different input patches and studied the changes in the activations of later
layers. As an alternative to using masks, which can look artificial compared to
typical values for an input patch, Zintgraf et al.
[@tag:Zintgraf2017_visualizing] proposed a novel strategy based on marginalizing
over plausible values of an input patch to more accurately estimate its
contribution.

A common drawback to perturbation-based approaches is computational efficiency:
each perturbed version of an input requires a separate forward propagation
through the network to compute the output. As noted by Shrikumar et al.
[@tag:Shrikumar2017_learning], such methods may also underestimate the impact of
features that have saturated their contribution to the output, as can happen
when multiple redundant features are present.

To reduce the computational overhead of perturbation-based approaches, Fong and
Vedaldi [@tag:Fong2017_perturb] solve an optimization problem using gradient
descent to discover a minimal subset of inputs to perturb in order to decrease
the predicted probability of a selected class. When tested on image data, their
method took about 300 iterations to converge, compared to the ~5000 iterations
used by LIME. One drawback of this approach is that the use of gradient descent
requires the perturbation to have a differentiable form.

##### Backpropagation-based approaches

A second strategy for addressing the computational inefficiency of
perturbation-based approaches is to propagate an important signal from a target
output neuron backwards through the layers to the input layer in a single
backpropagation-like pass. A classic example of this is calculating the gradients
of the output with respect to the input [@tag:Simonyan2013_deep] to compute a "saliency
map". Bach et al. [@tag:Bach2015_on] proposed a strategy called Layerwise
Relevance Propagation, which was shown to be equivalent to the elementwise
product of the gradient and input [@tag:Shrikumar2017_learning
@tag:Kindermans2016_investigating]. Several variants of gradients exist, which
differ in their handling of the ReLU nonlinearity. While gradients zero-out the
importance signal at ReLUs if the input to the ReLU is negative, deconvolutional
networks [@tag:Zeiler2013_visualizing] zero-out the importance signal if the
signal itself is negative. Guided backpropagation
[@tag:Springenberg2014_striving] combines the two strategies to zero-out the
importance signal if either the input to ReLU is negative or the importance
signal is negative, in effect discarding negative gradients. However, Mahendran
and Vedaldi [@tag:Mahendran2016_salient] showed that while guided
backpropagation excelled at identifying salient features in the input image,
these features showed little class-specificity, producing very similar saliency
maps regardless of the class under consideration. Selvaraju et al.
[@tag:Selvaraju2016_grad] attempted to alleviate this by combining gradients and
guided backpropagation in Gradient-weighted Class Activation Mapping. Feature
maps in the last convolutional layer were associated with classes using
gradients, and the weighted activation of these feature maps was multiplied with
the result of guided backpropagation to introduce more class specificity. Note
that these approaches still would not highlight features that have saturated
their contribution to the output, as the gradients with respect to such features
would be zero at the input.

To address the saturation failure mode, strategies have been developed to
consider how the output changes between some reference input and the actual
input, where the reference input represents a "null" input that it is
informative to measure differences against. Sundararajan et al.
[@tag:Sundararajan2017_axiomatic] integrated the gradients as the input was
linearly increased from the reference to its actual value.  In their examples,
which were on image-like data, they used a reference of all zeros. While the
numerical integration adds computational overhead, the method is still more
efficient on average than perturbation approaches. Further, by relying only on
the gradients, the method is a fully black-box approach that is guaranteed to
give the same answer for functionally equivalent networks. Shrikumar et al.
[@tag:Shrikumar2017_learning] developed DeepLIFT, a strategy that used the
difference between a neuron's activation on the reference input compared to its
activation on the actual input to improve the backpropagation of importance
scores. DeepLIFT is a white box method that requires knowledge of the network
architecture, but it is more computationally efficient than integrated
gradients. Lundberg and Lee [@tag:Lundberg2016_an] noted that several importance
scoring methods, including DeepLIFT, integrated gradients and LIME, could all be
considered approximations to the Shapely values [@tag:Shapely], which have a long history in
game theory for assigning contributions to players in cooperative games.
Briefly, the Shapely values measure the average marginal benefit of including a
player over all possible orders in which the players could be included.
In the case of DeepLIFT, the "inclusion" of a player is
analogous to setting a particular input to its actual value rather than its
reference value. DeepLIFT introduced a modification that treated positive and
negative contributions separately to address some failure cases of integrated
gradients.  The modification can be understood as an improved approximation of
the Shapely values.

#### Matching or exaggerating the hidden representation

Another approach to understanding the network's predictions is to find
artificial inputs that produce similar hidden representations to a chosen
example. This can elucidate the features that the network uses for prediction
and drop the features that the network is insensitive to. In the context of
natural images, Mahendran and Vedaldi [@tag:Mahendran2014_understanding]
introduced the "inversion" visualization, which uses gradient descent and
backpropagation to reconstruct the input from its hidden representation. The
method required placing a prior on the input to favor results that resemble
natural images. For genomic sequence, Finnegan and Song
[@tag:Finnegan2017_maximum] used a Markov chain Monte Carlo algorithm to find
the maximum-entropy distribution of inputs that produced a similar hidden
representation to the chosen input.

A related idea is "caricaturization", where an initial image is altered to
exaggerate patterns that the network searches for [@tag:Mahendran2016_visualizing].
This is done by maximizing the response of neurons that are active in the
network, subject to some regularizing constraints. Mordvintsev et al.
[@tag:Mordvintsev2015_inceptionism] leveraged caricaturization to generate
aesthetically pleasing images using neural networks.

#### Activation maximization

Activation maximization can reveal patterns detected by an individual neuron in
the network by generating images which maximally activate that neuron, subject
to some regularizing constraints. This technique was first introduced in Ehran
et al. [@tag:Ehran2009_visualizing] and applied in Simonyan et al.
[@tag:Simonyan2013_deep], Mordvintsev et al.
[@tag:Mordvintsev2015_inceptionism], Yosinksi et al.
[@tag:Yosinksi2015_understanding], and Mahendran and Vedaldi
[@tag:Mahendran2016_visualizing]. Lanchantin et al. [@tag:Lanchantin2016_motif]
applied activation maximization to genomic sequence data. One drawback of this
approach is that neural networks often learn highly distributed representations
where several neurons cooperatively describe a pattern of interest. Thus,
visualizing patterns learned by individual neurons may not always be
informative.

#### RNN-specific approaches

Several interpretation methods are specifically tailored to recurrent neural
network architectures. A few key approaches are summarized below.

The most common form of interpretability provided by RNNs is through attention
mechanisms, which have been used in diverse problems such as image captioning
and machine translation to select portions of the input to focus on
generating a particular output [@tag:Bahdanu2014_neural @tag:Xu2015_show].
Deming et al. [@tag:Deming2016_genetic] applied the attention mechanism to
models trained on genomic sequence. Attention mechanisms provide insight into
the model's decision-making process by revealing which portions of the input are
used by different outputs. In the clinical domain, Choi et al.
[@tag:Choi2016_retain] leveraged attention mechanisms to highlight which aspects
of a patient's medical history were most relevant for making diagnoses. Choi et
al. [@tag:Choi2016_gram] later extended this work to take into account the
structure of disease ontologies and found that the concepts represented by the
model aligned with medical knowledge. Note that interpretation strategies
that rely on an attention mechanism do not provide insight into the internal
logic used by the attention layer to decide which inputs to attend to.

Visualizing the activation patterns of the hidden state of a recurrent neural
network can also be instructive. Early work by Ghosh and Karamcheti
[@tag:Ghosh1992_sequence] used cluster analysis to study hidden states of
comparatively small networks trained to recognize strings from a finite state
machine. More recently, Karpathy et al. [@tag:Karpathy2015_visualizing] showed
the existence of individual cells in LSTMs that kept track of quotes and
brackets in character-level language models. To facilitate such analyses, LSTMVis
[@tag:Strobelt2016_visual] allows interactive exploration of the hidden
state of LSTMs on different inputs.

Another strategy, adopted by Lanchatin et al. [@tag:Lanchantin2016_motif] looks
at how the output of a recurrent neural network changes as longer and longer
subsequences are supplied as input to the network, where the subsequences begin
with just the first position and end with the entire sequence. In a binary
classification task, this can identify those positions which are responsible for
flipping the output of the network from negative to positive. If the RNN is
bidirectional, the same process can be repeated on the reverse sequence. As
noted by the authors, this approach was less effective at identifying motifs
compared to the gradient-based backpropagation approach of Simonyan et al.
[@tag:Simonyan2013_deep], illustrating the need for more sophisticated strategies
to assign importance scores in recurrent neural networks.

Murdoch and Szlam [@tag:Murdoch2017_automatic] showed that the output of an LSTM
can be decomposed into a product of factors, where each factor can be interpreted
as the contribution at a particular timestep. The contribution scores were then
used to identify key phrases from a model trained for sentiment analysis and
obtained superior results compared to scores derived via a gradient-based
approach.

#### Miscellaneous approaches

Toward quantifying the uncertainty of predictions, there has been a renewed
interest in confidence intervals for deep neural networks. Early work from
Chryssolouris et al. [@tag:Chryssolouris1996_confidence] provided confidence
intervals under the assumption of normally-distributed error. A more recent
technique known as test-time dropout [@tag:Gal2015_dropout] can also be used to
obtain a probabilistic interpretation of a network's outputs.

It can often be informative to understand how the training data affects
model learning. Toward this end, Koh and Liang [@tag:Koh2017_understanding]
used influence functions, a technique from robust statistics, to trace a model's
predictions back through the learning algorithm to identify the datapoints in
the training set that had the most impact on a given prediction.
A more free-form approach to interpretability is to visualize the activation
patterns of the network on individual inputs and on subsets of the data. ActiVis
and CNNvis [@tag:Kahng2017_activis @tag:Liu2016_towards] are two frameworks that
enable interactive visualization and exploration of large-scale deep learning
models.

An orthogonal strategy is to use a knowledge distillation approach to replace a
deep learning model with a more interpretable model that achieves comparable
performance. Towards this end, Che et al. [@tag:Che2015_distill] used gradient
boosted trees to learn interpretable healthcare features from trained deep
models.

Finally, it is sometimes possible to train the model to provide justifications
for its predictions. Lei et al. [@tag:Lei2016_rationalizing] used a generator to
identify "rationales", which are short and coherent pieces of the input text
that produce similar results to the whole input when passed through an encoder.
The authors applied their approach to a sentiment analysis task and obtained
substantially superior results compared to an attention-based method.

#### Future outlook

While deep learning certainly lags behind most Bayesian models in terms of
interpretability, one can safely argue that the interpretability of deep
learning is comparable to or exceeds that of many other widely-used machine
learning methods such as random forests or SVMs. While it is possible to obtain
importance scores for different inputs in a random forest, the same is true for
deep learning. Similarly, SVMs trained with a nonlinear kernel are not easily
interpretable because the use of the kernel means that one does not obtain an
explicit weight matrix. Finally, it is worth noting that some simple machine learning
methods are less interpretable in practice than one might expect.  For example, a
linear model trained on heavily engineered features might be difficult to
interpret as the input features themselves are difficult to interpret.
Similarly, a decision tree with many nodes and branches may also be difficult
for a human to make sense of.

There are several directions that might benefit the development of
interpretability techniques. The first is the introduction of gold standard
benchmarks that different interpretability approaches could be compared against,
similar in spirit to how datasets like ImageNet and CIFAR spurred the
development of deep learning for computer vision. It would also be helpful if
the community placed more emphasis on domains outside of computer vision.
Computer vision is often used as the example application of interpretability
methods, but it is arguably not the domain with the most pressing need. Finally,
closer integration of interpretability approaches with popular deep learning
frameworks would make it easier for practitioners to apply and experiment with
different approaches to understanding their deep learning models.

### Data limitations

A lack of large-scale, high-quality, correctly labeled training data has
impacted deep learning in nearly all applications we have discussed, from
healthcare to genomics to drug discovery.  The challenges of training complex,
high-parameter neural networks from few examples are obvious, but uncertainty in
the labels of those examples can be just as problematic.  For example, in
genomics, labeled data may be derived from an experimental assay with known and
unknown technical artifacts, biases, and error profiles.  It is possible to
weight training examples or construct Bayesian models to account for uncertainty
or non-independence in the data, as described in the TF binding example above. As another example, Park et al.
[@doi:10.1371/journal.pcbi.1002957] estimated shared non-biological signal
between datasets to correct for non-independence related to assay platform or
other factors in a Bayesian integration of many datasets. However, such
techniques are rarely placed front and center in any description of methods and
may be easily overlooked.

For some types of data, especially images, it is straightforward to augment
training datasets by splitting a single labeled example into multiple examples.
For example, an image can easily be rotated, flipped, or translated and retain
its label [@doi:10.1101/095794].  3D MRI and 4D fMRI (with time as a dimension)
data can be decomposed into sets of 2D images [@doi:10.1101/070441]. This can
greatly expand the number of training examples but artificially treats such
derived images as independent instances and sacrifices the structure inherent in
the data.  CellCnn trains a model to recognize rare cell populations in
single-cell data by creating training instances that consist of subsets
of cells that are randomly sampled with replacement from the full dataset
[@tag:Arvaniti2016_rare_subsets].

Simulated or semi-synthetic training data has been employed in multiple
biomedical domains, though many of these ideas are not specific to deep
learning.  Training and evaluating on simulated data, for instance, generating
synthetic TF binding sites with position weight matrices
[@tag:Shrikumar2017_reversecomplement] or RNA-seq reads for predicting mRNA
transcript boundaries [@doi:10.1101/125229], is a standard practice in
bioinformatics.  This strategy can help benchmark algorithms when the available
gold standard dataset are imperfect, but it should be paired with an evaluation
on real data, as in the prior examples [@tag:Shrikumar2017_reversecomplement
@doi:10.1101/125229].  In rare cases, models trained on simulated data have been
successfully applied directly to real data [@doi:10.1101/125229].

Simulated data can also be create negative examples when only positive training
instances are available.  DANN [@doi:10.1093/bioinformatics/btu703] adopts this
approach to predict the pathogenicity of genetic variants using semi-synthetic
training data from Combined Annotation-Dependent Depletion
[@doi:10.1038/ng.2892].  Though our emphasis here is on the training strategy,
it should be noted that logistic regression outperformed DANN when
distinguishing known pathogenic mutations from likely benign variants in real
data. Similarly, a somatic mutation caller has been trained by injecting
mutations into real sequencing datasets [@tag:Torracinta2016_sim].  This method
was successful at detecting mutations in other semi-synthetic datasets but was
not validated on real data.

In settings where the experimental observations are biased toward positive
instances, such as MHC protein and peptide ligand binding affinity
[@doi:10.1101/054775], or the negative instances vastly outnumber the positives,
such as high-throughput chemical screening [@tag:Lusci2015_irv], training
datasets have been augmented by adding additional instances and assuming they
are negative.  There is some evidence that this can improve performance
[@tag:Lusci2015_irv], but in other cases it was only beneficial when the real
training datasets were extremely small [@doi:10.1101/054775]. Overall, training
with simulated and semi-simulated data is a valuable idea for overcoming limited
sample sizes but one that requires more rigorous evaluation on real ground-truth
datasets before we can recommend it for widespread use. There is a risk that a
model will easily discriminate synthetic examples but not generalize to real
data.

Multimodal, multi-task, and transfer learning, discussed in detail below, can
also combat data limitations to some degree. There are also emerging network
architectures, such as Diet Networks for high-dimensional SNP data
[@tag:Romero2017_diet]. These use multiple networks to drastically reduce the
number of free parameters by first flipping the problem and training a network
to predict parameters (weights) for each input (SNP) to learn a feature
embedding. This embedding (e.g. from principal component analysis, per class histograms, or a Word2vec
[@tag:Word2Vec] generalization) can be learned directly from input data or take
advantage of other datasets or domain knowledge. Additionally, in this task the
features are the examples, an important advantage when it is typical to have 500
thousand or more SNPs and only a few thousand patients. Finally, this embedding
is of a much lower dimension, allowing for a large reduction in the number of
free parameters. In the example given, the number of free parameters from was
reduced from 30 million to 50 thousand, a factor of 600.

### Hardware limitations and scaling

Efficiently scaling deep learning is challenging, and there is a high
computational cost (e.g. time, memory, and energy) associated with training neural
networks and using them to make predictions. This is one of the reasons why
neural networks have only recently found widespread use
[@tag:Schmidhuber2014_dnn_overview].

Many have sought to curb these costs, with methods ranging from the very applied
(e.g. reduced numerical precision [@tag:Gupta2015_prec @tag:Bengio2015_prec
@tag:Sa2015_buckwild @tag:Hubara2016_qnn]) to the exotic and theoretic (e.g.
training small networks to mimic large networks and ensembles
[@tag:Caruana2014_need @tag:Hinton2015_dark_knowledge]). The largest gains in
efficiency have come from computation with graphics processing units (GPUs)
[@tag:Raina2009_gpu @tag:Vanhoucke2011_cpu @tag:Seide2014_parallel
@tag:Hadjas2015_cc @tag:Edwards2015_growing_pains
@tag:Schmidhuber2014_dnn_overview], which excel at the matrix and vector
operations so central to deep learning. The massively parallel nature of GPUs
allows additional optimizations, such as accelerated mini-batch gradient descent
[@tag:Vanhoucke2011_cpu @tag:Seide2014_parallel @tag:Su2015_gpu
@tag:Li2014_minibatch]. However, GPUs also have a limited quantity of memory,
making it difficult to implement networks of useful size and complexity on a
single GPU or machine [@tag:Raina2009_gpu @tag:Krizhevsky2013_nips_cnn]. This
restriction has sometimes forced computational biologists to use workarounds or
limit the size of an analysis. For example, Chen et al.
[@tag:Chen2016_gene_expr] aimed to infer the expression level of all genes with
a single neural network, but due to memory restrictions they randomly
partitioned genes into two halves and analyzed each separately. In other cases,
researchers limited the size of their neural network
[@tag:Wang2016_protein_contact] or the total number of training instances [@tag:Gomezb2016_automatic]. Some have also chosen
to use CPU implementations rather than sacrifice network size or
performance [@tag:Yasushi2016_cgbvs_dnn].

While steady improvements in GPU hardware may alleviate this issue, it is
unclear whether advances can occur quickly enough to keep up with the growing
amount of available biological data or increasing network complexity. Much has been
done to minimize the memory requirements of neural networks [@tag:CudNN
@tag:Caruana2014_need @tag:Gupta2015_prec @tag:Bengio2015_prec
@tag:Sa2015_buckwild @tag:Chen2015_hashing @tag:Hubara2016_qnn], but there is
also growing interest in specialized hardware, such as field-programmable gate
arrays (FPGAs) [@tag:Edwards2015_growing_pains @tag:Lacey2016_dl_fpga] and
application-specific integrated circuits (ASICs) [@arxiv:1704.04760]. Specialized hardware promises
improvements in deep learning at reduced time, energy, and memory
[@tag:Edwards2015_growing_pains]. Obviously, there is less software
available for such highly specialized hardware [@tag:Lacey2016_dl_fpga], and it
could be a difficult investment for those not solely interested in deep
learning. However, it is likely that such options will find increased support as
they become a more popular platform for deep learning and general computation.

Distributed computing is a general solution to intense computational
requirements and has enabled many large-scale deep learning efforts. Some types of
distributed computation [@tag:Mapreduce @tag:Graphlab] are not
suitable for deep learning [@tag:Dean2012_nips_downpour], but much progress has
been made. There now exist a number of algorithms [@tag:Dean2012_nips_downpour
@tag:Dogwild @tag:Sa2015_buckwild], tools [@tag:Moritz2015_sparknet
@tag:Meng2016_mllib @tag:TensorFlow], and high-level libraries [@tag:Keras
@tag:Elephas] for deep learning in a distributed environment, and it is possible
to train very complex networks with limited infrastructure
[@tag:Coates2013_cots_hpc]. Besides handling very large networks, distributed or
parallelized approaches offer other advantages, such as improved ensembling
[@tag:Sun2016_ensemble] or accelerated hyperparameter optimization
[@tag:Bergstra2011_hyper @tag:Bergstra2012_random].

Cloud computing, which has already seen wide adoption in genomics
[@tag:Schatz2010_dna_cloud], could facilitate easier sharing of the large
datasets common to biology [@tag:Gerstein2016_scaling @tag:Stein2010_cloud], and
may be key to scaling deep learning. Cloud computing affords researchers
flexibility, and enables the use of specialized hardware (e.g., FPGAs, ASICs,
GPUs) without major investment. As such, it could be easier to address the
different challenges associated with the multitudinous layers and architectures
available [@tag:Krizhevsky2014_weird_trick]. Though many are reluctant to store
sensitive data (e.g. patient electronic health records) in the cloud,
secure, regulation-compliant cloud services do exist [@tag:RAD2010_view_cc].

### Data, code, and model sharing

A robust culture of data, code, and model sharing would do much to speed
advances in this domain. The cultural barriers of data sharing in particular are
perhaps best captured by the implications of using the term "research parasite"
to describe scientists who use data from other researchers
[@doi:10.1056/NEJMe1516564]. In short, a field that honors only discoveries and
not the hard work of generating useful data will have difficulty encouraging
scientists to share their hard-won data. Unfortunately, it's precisely those
data that would help to power deep learning in the domain. Efforts are underway
to recognize those who promote an ecosystem of rigorous sharing and analysis
[@doi:10.1038/ng.3830].

The sharing of high-quality, labeled datasets will be especially valuable.  In
addition, researchers who invest time to preprocess datasets to be suitable for
deep learning can make the preprocessing code (e.g. Basset
[@tag:Kelley2016_basset] and variationanalysis [@tag:Torracinta2016_deep_snp])
and cleaned data (e.g. MoleculeNet [@tag:Wu2017_molecule_net]) publicly
available to catalyze further research. However, there are complex privacy and
legal issues involved in sharing patient data that cannot be ignored.
Furthermore, in some domains, some of the best training data has been generated
privately, for example, high-throughput chemical screening data at
pharmaceutical companies. One perspective is that there is little expectation or
incentive for this private data to be shared. However, data are not inherently
valuable. Instead, the insights that we glean from them are where the value
lies. Private companies may establish a competitive advantage by releasing
sufficient data for improved methods to be developed.

Code sharing and open source licensing is essential for continued progress in
this domain.  We strongly advocate following established best practices for
sharing source code, archiving code in repositories that generate digital object
identifiers, and open licensing [@doi:10.1126/science.aah6168] regardless of the
minimal requirements, or lack thereof, set by journals, conferences, or preprint
servers.  In addition, it is important for authors to share not only code for
their core models but also scripts and code used for data cleaning (see above)
and hyperparameter optimization.  These improve reproducibility and serve as
documentation of the detailed decisions that impact model performance but may
not be exhaustively captured in a manuscript's methods text.

Because many deep learning models are often built using one of several popular
software frameworks, it is also possible to directly share trained predictive
models.  The availability of pre-trained models can accelerate research, with
image classifiers as an apt example.  A pre-trained neural network can be
quickly fine-tuned on new data and used in transfer learning, as discussed
below.  Taking this idea to the extreme, genomic data has been artificially
encoded as images in order to benefit from pre-trained image classifiers
[@tag:Poplin2016_deepvariant]. "Model zoos" -- collections of pre-trained models --
are not yet common in biomedical domains but have started to appear in genomics
applications [@tag:Angermueller2016_single_methyl @tag:Dragonn].  Sharing models
for patient data requires great care because deep learning models can be
attacked to identify examples used in training.  We discuss this issue as well
as recent techniques to mitigate these concerns in the patient categorization
section.

DeepChem [@tag:AltaeTran2016_one_shot @tag:DeepChem @tag:Wu2017_molecule_net]
and DragoNN [@tag:Dragonn] exemplify the benefits of sharing pre-trained models
and code under an open source license. DeepChem, which targets drug discovery
and quantum chemistry, has actively encouraged and received community
contributions of learning algorithms and benchmarking datasets.  As a
consequence, it now supports of a large suite of machine learning approaches,
both deep learning and competing strategies, that can be run on diverse test
cases.  This realistic, continual evaluation will play a critical role in
assessing which techniques are most promising for chemical screening and drug
discovery.  Like formal, organized challenges such as the ENCODE-DREAM *in vivo*
Transcription Factor Binding Site Prediction Challenge [@tag:Dream_tf_binding],
DeepChem provides a forum for the fair, critical evaluations that are not always
conducted in individual methodological papers, which can be biased toward
favoring a new proposed algorithm.  Likewise DragoNN (Deep RegulAtory GenOmic
Neural Networks), offers not only code and a model zoo but also a detailed
tutorial and partner package for simulating training data.  These resources,
especially the ability to simulate datasets that are sufficiently complex to
demonstrate the challenges of training neural networks but small enough to train
quickly on a CPU, are important for (human) training and attracting machine
learning researchers to problems in genomics and healthcare.  We have even
included DragoNN and hands-on model training into the curriculum of a graduate
student course.

### Multimodal, multi-task, and transfer learning

As discussed above, the fact that biomedical datasets often contain a limited
number of instances or labels can be a cause of poor performance of machine
learning algorithms. When trained on such datasets, deep learning models are
particularly prone to overfitting due to their high representational power.
However, transfer learning techniques, also known as domain adaptation, enable
transfer of extracted patterns between different datasets and even domains. This
approach consists of training a model for the base task and subsequently
reusing the trained model for the target problem in hand. The first step allows
a model to take advantage of a larger amount of data and/or labels to extract
better feature representations. Transferring learnt features in deep neural
networks improves performance compared to randomly initialized features even
when pre-training and target sets are dissimilar. However, transferability of
features decreases as the distance between the base task and target task
increases [@tag:Yosinski2014].

In image analysis, previous examples of deep transfer learning applications
proved large-scale natural image sets [@tag:Russakovsky2015_imagenet] to be
useful for pre-training models that can then serve as generic feature extractors
applied to various types of biological images [@tag:Zhang2015_multitask_tl
@tag:Zeng2015 @tag:Angermueller2016_dl_review @tag:Pawlowski2016]. More
recently, deep learning models trained to predict protein sub-cellular
localization successfully performed predictions for proteins not originally
present in the training set [@tag:Parnamaa2017]. Moreover, in this type of task,
learnt features performed reasonably well even when applied to images obtained
using different fluorescent labels, imaging techniques, and different cell types
[@tag:Kraus2017_deeploc]. However, there are no established theoretical
guarantees for feature transferability between distant domains such as natural
images and various modalities of biological imaging. Because learnt patterns are
represented in deep neural networks in a layer-wise hierarchical fashion, this
issue is usually addressed by fixing an empirically chosen number of layers that
preserve generic characteristics of both training and target datasets. The model
is then fine-tuned by re-training multiple networks' top layers on the specific
dataset in order to re-learn domain-specific high level concepts (e.g.
fine-tuning for radiology image classification [@tag:Rajkomar2017_radiographs]).
Fine-tuning on specific biological datasets enables more focused predictions.

In genomics, the Basset package [@tag:Kelley2016_basset] for predicting
chromatin accessibility was shown to rapidly learn and accurately predict
on new data by leveraging a model pre-trained on available public data. To
simulate this scenario, authors put aside 15 of 164 cell type datasets and
trained the Basset model on the remaining 149 datasets. Then, they fine-tuned
the model with one training pass of each of the remaining datasets and achieved
results close to the model trained on all 164 datasets together. In another
example, Min et al. [@tag:Min2016_deepenhancer] demonstrated how training on the
experimentally validated FANTOM5 permissive enhancer dataset followed by
fine-tuning on ENCODE enhancer datasets improved cell type-specific predictions,
outperforming state-of-the-art results.  In drug design, general RNN models
trained to generate molecules from the ChEMBL database have been fine-tuned to
produce drug-like compounds for specific targets [@tag:Segler2017_drug_design
@tag:Olivecrona2017_drug_design].

Related to transfer learning, multimodal learning assumes simultaneous learning
from various types of inputs, such as images and text. It can capture
features that describe common concepts across input modalities. Generative
graphical models like restricted Boltzmann machines (RBM) and their stacked
versions, deep Boltzmann machines (DBM), and deep belief networks (DBN),
demonstrate successful extraction of more informative features for one modality
(images or video) when jointly learnt with other modalities (audio or text)
[@tag:Ngiam2011]. Deep graphical models such as DBNs are considered to be
well-suited for multimodal learning tasks because they learn a joint probability
distribution from inputs. They can be pre-trained in an unsupervised fashion on
large unlabeled data and then fine-tuned on a smaller number of labeled
examples. When labels are available, convolutional neural networks are
ubiquitously used because they can be trained end-to-end with backpropagation and
demonstrate state-of-the-art performance in many discriminative tasks
[@tag:Angermueller2016_dl_review].

Jha et al. [@tag:Jha2017_integrative_models] showed that an integrated training
approach delivers better performance compared to individual networks. They
compared a number of feed-forward architectures trained on RNA-seq data with and
without an additional set of CLIP-seq, knockdown, and over-expression based
input features. Results showed that the integrative deep model generalized well
for combined data, offering large performance improvement for alternative
splicing event estimation. Chaudhary et al.
[@tag:Chaudhary2017_multiom_liver_cancer] trained a deep autoencoder model
jointly on RNA-seq, miRNA-seq, and methylation data from The Cancer Genome Atlas to predict
survival subgroups of hepatocellular carcinoma patients. This multimodal
approach that treated different omic data types as different modalities outperformed both
traditional methods (PCA) and single-omic models. Interestingly, multi-omic
model performance did not improve when combined with clinical information,
suggesting that the model was able to capture redundant contributions of
clinical features through their correlated genomic features. Chen et al.
[@tag:Chen2015_trans_species] used deep belief networks to learn phosphorylation
states of a common set of signaling proteins in primary cultured bronchial cells
collected from rats and humans treated with distinct stimuli. By interpreting
species as different modalities representing similar high-level concepts, they
showed that DBNs were able to capture cross-species representation of signaling
mechanisms in response to a common stimuli. Another application used DBNs for
joint unsupervised feature learning from cancer datasets containing gene
expression, DNA methylation, and miRNA expression data
[@tag:Liang2015_exprs_cancer]. This approach allowed for the capture of
intrinsic relationships in different modalities and for better clustering
performance over conventional k-means.

Multimodal learning with CNNs is usually implemented as a collection of
individual networks in which each learns representations from single data type.
These individual representations are further concatenated before or within
fully-connected layers. FIDDLE [@tag:Eser2016_fiddle] is an example of
a multimodal CNN that represents an ensemble of individual networks that take
NET-seq, MNase-seq, ChIP-seq,
RNA-seq, and raw DNA sequence as input to predict Transcription Start Site-seq.
The combined model radically improves performance over separately
trained datatype-specific networks, suggesting that it learns the synergistic
relationship between datasets.

Multi-task learning is an approach related to transfer learning. In a multi-task learning
framework, a model learns a number of tasks simultaneously such that features
are shared across them. DeepSEA [@tag:Zhou2015_deep_sea] implemented a
multi-task joint learning of diverse chromatin factors sharing predictive
features from raw DNA sequence. This allowed, for example, a sequence feature
that is effective in recognizing binding of a specific TF to be simultaneously
used by another predictor for a physically interacting TF. Similarly, TFImpute
[@tag:Qin2017_onehot] learned information shared across
transcription factors and cell lines to predict cell-specific TF binding for
TF-cell line combinations. Yoon et al. [@tag:Yoon2016_cancer_reports] demonstrated
that predicting the primary cancer site from cancer pathology reports
together with its laterality substantially improved the performance for the
latter task, suggesting that multi-task learning can effectively leverage the commonality
between two tasks using a shared representation. A number of studies from the
drug development section employed multi-task
learning to predict chemical bioactivity [@tag:Dahl2014_multi_qsar @tag:Ramsundar2015_multitask_drug]
and drug toxicity [@tag:Mayr2016_deep_tox
@tag:Hughes2016_macromol_react]. Kearnes et al. [@tag:Kearnes2016_admet]
systematically compared single-task and multi-task models for
ADMET properties. They showed that multi-task learning generally improve
performance and smaller datasets
tend to benefit more than larger datasets.

The multi-task learning approach is complementary to multimodal and transfer learning. All three
techniques can be used together in the same model. For example, Zhang et al.
[@tag:Zhang2015_multitask_tl] combined deep model-based transfer and multi-task
learning for cross-domain image annotation. One could imagine extending that
approach to multimodal inputs as well. A common characteristic of these methods
is better generalization of extracted features at various hierarchical levels of abstraction,
which is attained by leveraging relationships
between various inputs and task objectives.

Despite demonstrated improvements, transfer learning approaches also pose a
number of challenges. As mentioned above, there are no theoretically sound
principles for pre-training and fine-tuning. Most best practice recommendations
are heuristic and have to take into account additional hyper-parameters that
depend on specific deep architectures, sizes of the pre-training and target
datasets, and similarity of domains. However, similarity of datasets and domains
in transfer learning and relatedness of tasks in multi-task learning is difficult to access.
Most studies address these limitations by empirical evaluation of the
model using established best practices or heuristics and cross-validation.
Unfortunately, negative results are typically not reported.
Rajkomar et al.
[@tag:Rajkomar2017_radiographs] showed that a deep CNN trained on natural images
can boost radiology image classification performance. However, due to
differences in imaging domains, the target task required either re-training the
initial model from scratch with special pre-processing or fine-tuning of the
whole network on radiographs with heavy data augmentation to avoid overfitting.
Exclusively fine-tuning top layers led to much lower validation accuracy (81.4
versus 99.5). Fine-tuning the aforementioned Basset model
required no more than one training pass.
Otherwise, the model overfit new data [@tag:Kelley2016_basset].
DeepChem successfully improved results for low-data drug discovery with one-shot
learning for related tasks. However, it demonstrated clear limitations to
cross-task generalization across unrelated tasks in one-shot models,
specifically nuclear receptor assays and patient adverse reactions
[@tag:AltaeTran2016_one_shot].

In the medical domain, multimodal, multi-task and transfer learning strategies not only inherit most
methodological issues from natural image, text, and audio domains, but also pose
domain-specific challenges.
There is a compelling need for the development of privacy-preserving
transfer learning algorithms, such as Private Aggregation of Teacher Ensembles
[@tag:Papernot2017_pate]. We
suggest that these types of models deserve deeper investigation to establish
sound theoretical guarantees and determine limits for the
transferability of features between various closely related and distant learning
tasks.
