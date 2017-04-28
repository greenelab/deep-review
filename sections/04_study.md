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

`TODO: dropped signaling subsection, decide whether to discuss in intro
and why it has received less attention, @tag:Chen2015_trans_species as example`

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
[@tag:Gupta2015_exprs_yeast] and also to stratify yeast strains based on
chemical and mutational perturbations [@tag:Chen2016_exprs_yeast]. Shallow
(one hidden layer) denoising autoencoders have also been fruitful in extracting
biological insight from thousands of _Pseudomonas aeruginosa_ experiments
[@tag:Tan2015_adage @tag:Tan2016_eadage] and in aggregating features relevant
to specific breast cancer subtypes [@tag:Tan2014_psb]. These unsupervised
approaches applied to gene expression data are powerful methods for aggregating
features and identifying gene signatures that may otherwise be overlooked by
alternative methods. An additional benefit of unsupervised approaches is that
ground truth labels, which are often difficult to acquire or are incorrect, are
nonessential. However, careful interpretation must be performed regarding how
the genes are aggregated into features. Precisely attributing node activations to
specific biological functions risks over-interpreting models and can lead to
incorrect conclusions.

Alternatively, deep learning approaches are also being applied for gene
expression prediction tasks. For example, a deep neural network with
three hidden layers outperformed linear regression in inferring the expression
of over 20,000 target genes based on a representative, well-connected set of
about 1,000 landmark genes [@tag:Chen2016_gene_expr]. However, while the deep
learning model outperformed already existing algorithms in nearly every
scenario, the model still displayed poor performance. The paper was also limited
by computational bottlenecks that required data to be split randomly into two
distinct models and trained separately. It is unclear how much performance
would have increased if not for computational restrictions. Furthermore, a
convolutional neural network applied to histone modifications, termed
DeepChrome, [@tag:Singh2016_deepchrome] was shown to predict gene expression
output. DeepChrome greatly improved high or low expression prediction accuracy
over existing methods. Deep learning applied to epigenetic data for gene
expression inference is a promising approach to study gene regulation. Deep
learning approaches have also been applied to study cancer gene expression data
with goals of identifying subtypes of patients with different molecular features
and clinical manifestations [@tag:Liang2015_exprs_cancer]. In the study, the
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
single-cell RNA-seq data [@tag:Shaham2016_batch_effects]. Moreover, deep
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
underlie many diseases [@tag:Scotti2016_missplicing]. For instance, in Becker
muscular dystrophy, a point mutation in dystrophin creates an ESS that induces
skipping of exon 31. A recent study found that quantitative trait loci (QTLs)
that affect splicing in lymphoblastoid cell lines are enriched within risk loci
for schizophrenia, multiple sclerosis and other immune diseases, implicating
mis-splicing as a much more widespread feature of human pathologies than
previously thought [@tag:Li2016_variation].

Sequencing studies routinely return thousands of unannotated variants. Which
cause functional changes in splicing, and if so, how? Prediction of a “splicing
code” has been a holy grail over the past decade. Initial machine learning
approaches used a naive Bayes model and a 2-layer Bayesian neural network with
thousands of hand-derived sequence-based features to predict the probability of
exon skipping [@tag:Barash2010_splicing_code @tag:Xiong2011_bayesian]. With the
advent of deep learning, more complex models were built that provided better
predictive accuracy [@tag:Xiong2015_splicing_code
@tag:Jha2017_integrative_models]. Importantly, these new approaches can take in
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
[@tag:Qin2017_onehot].

A parallel effort has been to use more data with simpler models. An exhaustive
study using readouts of splicing for millions of synthetic intronic sequences
was able to describe motifs that influence the strength of alternative splice
sites [@tag:Rosenberg2015_synthetic_seqs]. Interestingly, they built a simple
linear model using hexamer motif frequencies that successfully generalized to
exon skipping: in a limited analysis using SNPs from three genes, it predicted
exon skipping with three times the accuracy of Xiong et al.’s framework. This
case is instructive in that clever sources of data, not just more powerful
models, can lead to novel insights.

We already understand how mis-splicing of a single gene can cause diseases such
as Duchenne muscular dystrophy. The challenge now is to uncover how alternative
splicing genome-wide gives rise to or is involved in complex, non-Mendelian
diseases such as autism, schizophrenia, Type 1 diabetes, and multiple sclerosis
[@tag:JuanMateu2016_t1d]. As a proof of concept, Xiong et al.
[@tag:Xiong2015_splicing_code] sequenced five ASD and 12 control samples, each
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
ENCODE [@tag:Consortium2004_encode] have provided ChIP-seq
data for hundreds of different TFs across many laboratories.
However, ChIP-seq experiments are expensive and time consuming.
Since the data that scientists have discovered is available, in
silico methods to predict binding sites are of great interest, thus
eliminating the need to do new ChIP-seq experiments every
time analysis is done on a new sequence.

In order to computationally predict TFBSs on a DNA sequence, researchers
initially used consensus sequences and position weight matrices to match
against a test sequence [@tag:Stormo2000_dna]. Simple neural network
classifiers were then proposed to differentiate positive and negative binding
sites, but did not show significant improvements over the weight matrix
matching methods [@tag:Horton1992_assessment]. Later, SVM techniques
outperformed the generative methods by using k-mer features
[@tag:Ghandi2014_enhanced @tag:Setty2015_seqgl], but string kernel based SVM
systems are limited by expensive computational cost proportional to the number
of training and testing sequences. More recently,
[@tag:Alipanahi2015_predicting] showed that convolutional neural network
models could achieve state of the art results on the TFBS task and are scalable
to a large number of genomic sequences. [@tag:Lanchantin2016_motif] introduced
several new convolutional and recurrent neural network models for predicting
TFBSs, but it remains unclear which neural architectures work best for all
samples and TFs. While neural architectures are rapidly changing and producing
better results, it is clear that deep learning can be efficiently and
effectively used to do functional prediction on the genome given raw data.

While accurately predicting transcription factors computationally is useful,
it is important to understand how these computational models make their
predictions. To handle this, several papers have focused on understanding
machine learning models [@tag:Alipanahi2015_predicting
@tag:Lanchantin2016_motif @tag:Shrikumar2016_blackbox].
[@tag:Alipanahi2015_predicting] was the first to introduce a visualization
method for a deep learning model on the TFBS task, and they did so by
visualizing the learned convolution filters which were informative for the
model’s prediction of a specific sample. However, this approach was specific to
visualizing certain samples fed through their particular model.
[@tag:Lanchantin2016_motif] introduced a suite of state-of-the-art deep
learning models and new visualizations techniques for a more in-depth analysis
of TFBSs. Furthermore, [@tag:Shrikumar2016_blackbox] introduced an advanced
visualization method and toolbox for analyzing possible TFBS sequences.
[@tag:Alipanahi2015_predicting] also introduced mutation maps, where they could
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

`TODO: cut RNA-binding proteins from above section, refer to representative
papers`

### Promoters, enhancers, and related epigenomic tasks

`TODO: There's inevitably a lot of overlap been this and the transcription
binding section. Maybe in the long term think about restructuring to one big
"regulome" section`

Identification of promoters and other cis-regulatory elements (CREs) presents an
obvious use case for deep learning. Transcriptional control is undoubtedly a
vital - and early - part of the regulation of gene expression. An abundance of
sequence and associated functional data (e.g. ENCODE, ExAC) exists across
species. At the same time,  studies of gene regulation have often focused on the
protein (binding) rather than promoter level [@doi:10.1093/bib/4.1.22], perhaps
due to the ill-defined nature of CREs. A promoter itself can be seen as an
assemblage of "active" binding sites for  transcription factors interspersed by
less-characterized and perhaps functionally silent spacer regions. However, the
sequence signals that control the start and stop of transcription and
translation are still not well understood, compounded by incomplete
understanding of alternative transcripts and the context for these
alternatives. Sequence similarity is poor even between functionally correlated
genes. While homologs might be studied for insight, they may not exist or may be
just as poorly characterized.

Recognizing enhancers presents additional challenges. Enhancers may be up to 1
Mbp upstream or downstream from  the target promoter, on either strand, even
within the introns of other genes [@doi:10.1038/nrg3458]. They do not
necessarily operate on the nearest gene and may in fact effect multiple genes.
Their activity is frequently tissue- or context-specific. A substantial fraction
of enhancers displays modest or no conservation across species. There is no
universal enhancer sequence signal or marker for enhancers, and some literature
suggests that enhancers and promoters may be just categories along a spectrum
[@doi:10.1016/j.tig.2015.05.007]. One study [@doi:10.1101/gr.173518.114] even
showed that only 33% of predicted regulatory regions could be validated, while a
class of "weak" predicted enhancers were strong drivers of expression. Yet there
is growing evidence for their vast ubiquity, making them possibly the
predominant functional non-coding element. Thus, identifying enhancers is
critical yet the the search space is embarrassingly large.

While prior (non-deep learning) approaches have made steady improvements on
promoter prediction, there is little consensus on the best approach and
performance is poor. Typically algorithms will recognize only half of all
promoters, with an accompanying high false positive rate
[@url:http://genome.cshlp.org/content/7/9/861.long].
Methods with better sensitivity generally do so at the cost of poorer
specificity. Conventional identification of enhancers has leaned heavily on
simple conservation or laborious experimental techniques, with only moderate
sensitivity and specificity. For example, while chromatin accessibility has
often been used for identifying enhancers, this also "recognizes" a wide variety
of other functional elements, like promoters, silencers and repressors.

The complex nature of CREs (and our ignorance at to what are the important
features of them) therefore seems a good subject for deep learning approaches.
Indeed, neural networks were used for promoter recognition as early as 1996,
albeit with mixed results [@doi:10.1016/S0097-8485(96)80015-5]. Since then,
there have been much work in applying deep learning to this area, although
little in the way of comparative studies or reviews. We will therefore focus on
a few recent characteristic studies to outline the state of the art and extant
problems.

Most broadly, Kelley et al. [@doi:10.1101/gr.200535.115] trained CNNs on DNA
accessibility datasets, getting an marked improvement on previous methods,
albeit still with a high false positive rate. (Note as above, using DNA
accessibility conflates enhancers with other functional sites.) This study also
featured a useful interpetability approach (analogous to in silico mutagenesis
[@doi:10.1093/nar/gkm238]) introducing known protein binding motifs into
sequences and measuring the change in predicted accessibility.

Umarov et al. [@doi:10.1371/journal.pone.0171410] demonstrated the use of
Convolutional Neural Networks in recognizing promoter sequences, achieving
markedly better performance than conventional methods (sensitivity and
specificity exceeding 90%). While some results were achieved over bacterial
promoters (which are considerably simpler in structure), surprisingly roughly
similar performance was found for human promoters. This work also included a
promising and simple method for interpretability (randomly substituting bases in
a recognized promoter region, then checking for a change in recognition) that
would be useful to exploit more widely.

Xu et al [@doi:10.1109/BIBM.2016.7822593] applied CNNs to the detection of
enhancers, achieving incremental improvements in specificity and sensitivity
over previous SVM-based approach, and markedly better performance for
cell-specific enhancers. A massive improvement in speed was also achieved.
Additionally, they compared the performance of different CNN architectures,
finding that while layers for batch normalization improved performance,
surprisingly deeper architectures decreased performance.

Singh et al. [@doi:10.1101/085241] also used batch normalization, approaching
the problem of predicting enhancer-promoter interactions from solely the
sequence and location of putative enhancers and promoters in a particular cell
type. Performance was comparative to state of the art conventional techniques
that used the whole gamut of full functional genomic and non-sequence data.

Given the conflation between different CREs, the study of Li et al.
[@doi:10.1101/041616] is particularly interesting.  They used a feed-forward
neural network to distinguish classes of CRES and activity states. Active
enhancers and promoters could be easily be distinguished, as could active and
inactive elements. Perhaps unsurprisingly, it was difficult to distinguish
between inactive enhancers and promoters. They also investigated the power of
sequence features to drive classification, finding that beyond CpG islands, few
were useful.

In summary, deep learning is a promising approach for identifying CREs, able to
interrogate sequence features that are complex and ill-understood, already
offering marked improvements on the prior state of the art. However, the exact
methodology is up for debate and needs examination and more comparative study.
Work needs to be done in understanding the best architecture to be used. Further
concern surrounds the training data. CNNs require a large training set to avoid
over-fitting, yet in many cases we do not have a large "gold standard" dataset
to train against. Further more, the quality and meaning of training data needs
to be closely considered, given that a "promoter" or "enhancer" may only be
putative or dependent on the experimental method or context of identification.
Else we risk building detectors not for CREs but putative CREs. The best model
of negative sample needs also to be considered, as does the problem of
imbalanced data. In a sentence, these methods can only be as good as their
training data. Finally, intepretability is a problem but one that appears to be
solvable given empirical approaches.

`TODO: discuss enhancer-promoter and enhancer-target prediction`

### Micro-RNA binding

Prediction of microRNAs (miRNAs) in the genome as well as miRNA targets is of
great interest, as they are critical components of gene regulatory networks and
are often conserved across great evolutionary distance [@tag:Bracken2016_mirna
@tag:Berezikov2011_mirna]. While many machine learning algorithms have been
applied to solve these prediction tasks, they currently require extensive
feature selection and optimization. For instance, one of the most widely adopted
tools for miRNA target prediction, TargetScan, trained multiple linear
regression models on 14 hand-curated features including structural accessibility
of the target site on the mRNA, the degree of site conservation, and predicted
thermodynamic stability of the miRNA:mRNA complex [@tag:Agarwal2015_targetscan].
Some of these features, including structural accessibility, are imperfect or
empirically derived. In addition, current algorithms suffer from low specificity
[@tag:Lee2016_deeptarget].

As in other applications, deep learning promises to achieve equal or better
performance in predictive tasks by automatically engineering complex features to
minimize an objective function. Two recently published tools use different
recurrent neural network-based architectures to perform miRNA and target
prediction with solely sequence data as input [@tag:Park2016_deepmirgene
@tag:Lee2016_deeptarget]. Though the results are preliminary and still based on
a validation set rather than a completely independent test set, they were able
to predict microRNA target sites with 15-25% higher specificity and sensitivity
than TargetScan. Excitingly, these tools seem to show that RNNs can accurately
align sequences and predict bulges, mismatches, and wobble base pairing without
requiring the user to input secondary structure predictions or thermodynamic
calculations.

Further incremental advances in neural-network approaches for miRNA and target
prediction will likely be sufficient to meet the current needs of systems
biologists and other researchers, who use prediction tools mainly to nominate
candidates that are then tested experimentally. Similar to other applications,
the major contribution of deep learning will be to deliver deep insights into
the biology of miRNA targeting as we learn to interrogate the hidden nodes
within neural networks.

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
method PSIPRED [@doi:10.1093/bioinformatics/16.4.404]. Starting from
2012, deep learning has been gradually introduced to protein structure
prediction. The adopted deep learning models include deep belief network,
LSTM(long short-term memory), deep convolutional neural networks (DCNN)
and deep convolutional neural fields[@doi:10.1007/978-3-319-46227-1_1
@doi:10.1038/srep18962]. Here we focus on deep learning methods for
two representative sub-problems: secondary structure prediction and
contact map prediction. Secondary structure refers to local conformation of
a sequence segment while a contact map contains information of global
conformation. Secondary structure prediction is a basic problem and almost
an essential module of any protein structure prediction package. It has also
been used as sequence labeling benchmark in the machine learning community.
Contact prediction is much more challenging than secondary structure prediction,
but it has a much larger impact on tertiary structure prediction.
In recent years, contact prediction has made good progress and its accuracy
has been significantly improved [@doi:10.1371/journal.pcbi.1005324
@doi:10.1093/bioinformatics/btu791 @doi:10.1073/pnas.0805923106
@doi:10.1371/journal.pone.0028766].

Protein secondary structure can exhibit three different states (alpha helix,
beta strand and loop regions) or eight finer-grained states. More methods are
developed to predict 3-state secondary structure than 8-state. A predictor is
typically evaluated by 3-state (i.e., Q3) and 8-state (i.e., Q8) accuracy, respectively.
Qi et al. developed a multi-task deep learning method to simultaneously predict several
local structure properties including secondary structures [@doi:10.1371/journal.pone.0032235].
Spencer, Eickholt and Cheng predicted secondary structure using deep belief networks
[@doi:10.1109/TCBB.2014.2343960]. Heffernan and Zhou et al. developed an iterative
deep learning framework to simultaneously predict secondary structure, backbone torsion
angles and solvent accessibility [@doi:10.1038/srep11476]. However, none of these deep
learning methods achieved significant improvement over PSIPRED [@doi:10.1006/jmbi.1999.3091]
in terms of Q3 accuracy. In 2014, Zhou and Troyanskaya demonstrated that they could
improve Q8 accuracy over a shallow learning architecture conditional neural fields [@doi:10.1002/pmic.201100196]
by using a deep supervised and convolutional generative stochastic network[@arxiv:1403.1347],
but did not report any results in terms of Q3 accuracy. In 2016 Wang and Xu et al. developed a deep
convolutional neural fields (DeepCNF) model that can significantly improve secondary
structure prediction in terms of both Q3 and Q8 accuracy[@doi:10.1038/srep18962].
DeepCNF possibly is the first that reports Q3 accuracy of 84-85%, much higher than
the 80% accuracy maintained by PSIPRED for more than 10 years.
It is also reported that DeepCNF can improve prediction of solvent accessibility
and disorder regions [@doi:10.1007/978-3-319-46227-1_1]. This improvement may be mainly
due to the introduction of convolutional neural fields to capture long-range
sequential information, which is important for beta strand prediction. Nevertheless,
improving secondary structure prediction from 80% to 84-85% is unlikely to
result in a similar amount of improvement in tertiary structure prediction since secondary
structure mainly reflects coarse-grained local conformation of a protein structure.

Protein contact prediction and contact-assisted folding (i.e., folding proteins using
predicted contacts as restraints) represents a promising new direction for ab initio folding
of proteins without good templates in PDB.
Evolutionary coupling analysis (ECA) is an effective contact prediction method for some
proteins with a very large number (>1000) of sequence homologs [@doi:10.1371/journal.pone.0028766],
but ECA fares poorly for proteins without many sequence homologs. Since (soluble) proteins with
many sequence homologs are likely to have a good template in PDB, to make contact-assisted
folding practically useful for ab initio folding, it is essential to predict accurate contacts
for proteins without many sequence homologs. By combining ECA with a few other protein features,
shallow neural network-based methods such as MetaPSICOV [@doi:10.1093/bioinformatics/btu791] and
CoinDCA-NN [@doi:10.1093/bioinformatics/btv472] have shown some advantage over ECA
for proteins with a small number of sequence homologs, but their accuracy is still not very good.
In recent years, deep learning methods have been explored for contact prediction. For example,
Di Lena et al. introduced a deep spatio-temporal neural network (up to 100 layers) that utilizes both
spatial and temporal features to predict protein contacts[@doi:10.1093/bioinformatics/bts475].
Eickholt and Cheng combined deep belief networks and boosting techniques to predict protein contacts
[@doi:10.1093/bioinformatics/bts598] and trained deep networks by layer-wise unsupervised
learning followed by fine-tuning of the entire network. Skwark and Elofsson et al. developed
an iterative deep learning technique for contact prediction by stacking a series of Random Forests
[@doi:10.1371/journal.pcbi.1003889]. However, blindly tested in the well-known CASP competitions,
these methods did not show any advantage over MetaPSICOV [@doi:10.1093/bioinformatics/btu791], a method
using two cascaded neural networks. Very recently, Wang and Xu et al. proposed a novel deep learning method
RaptorX-Contact [@doi:10.1371/journal.pcbi.1005324] that can significantly improve contact prediction
over MetaPSICOV especially for proteins without many sequence homologs. RaptorX-Contact employs a network
architecture formed by one 1D residual neural network and one 2D residual neural network.
Blindly tested in the latest CASP competition (i.e., CASP12 [@url:http://www.predictioncenter.org/casp12/rrc_avrg_results.cgi]),
RaptorX-Contact is ranked first in terms of the total F1 score (a widely-used performance metric) on
free-modeling targets as well as the whole set of targets. In the CASP12 test, the group ranked second
also employed a deep learning method. Even MetaPSICOV, which ranked third in CASP12, employed more
and wider hidden layers than its old version. Wang and Xu et al. have also
demonstrated in another blind test CAMEO (which can be interpreted as a fully-automated
CASP) [@url:http://www.cameo3d.org/] that their predicted contacts can help fold quite a few proteins
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

### Morphological phenotypes

A field poised for dramatic revolution by deep learning is
bioimage analysis.
Thus far, the primary use of deep learning for biological
images has been for segmentation - that is, for the identification
of biologically relevant structures in images such as nuclei,
infected cells, or vasculature, in fluorescence or even brightfield
channels [@doi:10.1371/journal.pcbi.1005177]. Once so-called regions of
interest have been identified, it is often straightforward
to measure biological properties of interest, such as fluorescence
intensities, textures, and sizes. Given the dramatic successes of
deep learning in biological imaging, we simply refer to articles that
review recent advancements [@doi:10.3109/10409238.2015.1135868
@doi:10.1371/journal.pcbi.1005177 @doi:10.1007/978-3-319-24574-4_28].
We believe deep learning will become a commonplace tool for
biological image segmentation once user-friendly tools exist.

We anticipate an additional kind of paradigm shift in bioimaging that
will be brought about by deep learning: what if images of biological
samples, from simple cell cultures to three-dimensional organoids and
tissue samples, could be mined for much more extensive biologically
meaningful information than is currently standard? For example, a
recent study demonstrated the ability to predict lineage fate in
hematopoietic cells up to three generations in advance of
differentiation [@doi:10.1038/nmeth.4182]. In biomedical research,
by far the most common paradigm is for biologists to decide in advance
what feature to measure in images from their assay system. But images
of cells contain a wide variety of quantitative information, and deep
learning may just be the tool to extract it. Although classical methods
of segmentation and feature extraction can produce hundreds of metrics
per cell in an image, deep learning is unconstrained by human intuition
and can in theory extract more subtle features. Already, there is evidence
deep learning can surpass the efficacy of classical methods
[@doi:10.1101/081364], even using generic deep convolutional networks
trained on natural images [@doi:10.1101/085118], known as transfer learning.

The impact of further improvements on biomedicine could be enormous.
Comparing cell population
morphologies using conventional methods of segmentation and feature
extraction has already proven useful for functionally annotating genes
and alleles, identifying the cellular target of small molecules, and
identifying disease-specific phenotypes suitable for drug screening
[@doi:10.1016/j.copbio.2016.04.003 @doi:10.1002/cyto.a.22909
@doi:10.1083/jcb.201610026].
Deep learning would bring to these new kinds of experiments - known
as image-based profiling or morphological profiling - a higher degree of
accuracy, stemming from the freedom from human-tuned feature extraction
strategies.

`TODO: Make sure that at the end we clearly emphasize our excitement around
unsupervised uses.`

### Single-cell

Single-cell methods are generating extreme excitement as biologists recognize
the vast heterogeneity within unicellular species and between cells of the same
tissue type in the same organism [@tag:Gawad2016_singlecell]. For instance,
tumor cells and neurons can both harbor extensive somatic variation
[@tag:Lodato2015_neurons]. Understanding single-cell diversity in all its
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
ATAC-seq [@tag:Liu2016_sc_transcriptome @tag:Vera2016_sc_analysis].

However, large challenges exist in studying single cells. Relatively few cells
can be assayed at once using current droplet, imaging, or microwell
technologies, and low-abundance molecules or modifications may not be detected
by chance in a phenomenon known as dropout. To solve this problem, Angermueller
et al. [@tag:Angermueller2016_single_methyl] trained a neural network to predict
the presence or absence of methylation of a specific CpG site in single cells
based on surrounding methylation signal and underlying DNA sequence, achieving
several percentage points of improvement compared to random forests or deep
networks trained only on CpG or sequence information. Similar deep learning
methods have been applied to impute low-resolution ChIP-seq signal from bulk
tissue with great success, and they could easily be adapted to single cell data
[@tag:Qin2017_onehot @tag:Koh2016_denoising].

Examining populations of single cells can reveal biologically meaningful subsets
of cells as well as their underlying gene regulatory networks
[@tag:Gaublomme2015_th17]. Unfortunately, machine learning generally struggles
with unbalanced data — when there are many more inputs of class 1 than class 2 —
because prediction accuracy is usually evaluated over the entire dataset. To
tackle this challenge, Arvaniti et al. [@tag:Arvaniti2016_rare_subsets]
classified healthy and cancer cells expressing 25 markers by using the most
discriminative filters from a CNN trained on the data as a linear classifier.
They achieved an impressive precision of 50% to 90% with 80% recall on cells
where the subset percentage ranged from 0.1 to 1%, which significantly
outperformed logistic regression and distance-based outlier detection methods.
However, they did not benchmark against random forests, which tend to be better
with unbalanced data, or against the neural network itself, and their data was
fairly low dimensional. Future work will be needed to establish the utility of
deep learning in cell subset identification, but the stunning improvements in
image classification over the past 5 years [@tag:He2015_images] suggest that
this goal will be achievable.

The sheer quantity of “omic” information that can be obtained from each cell, as
well as the number of cells in each dataset, uniquely position single-cell data
to benefit from deep learning. In the future, lineage tracing could be
revolutionized by using autoencoders to reduce the feature space of
transcriptomic or variant data followed by algorithms to learn optimal cell
differentiation trajectories [@tag:Qiu2017_graph_embedding], or by feeding cell
morphology and movement into neural networks
[@tag:Buggenthin2017_imaged_lineage]. Reinforcement learning algorithms
[@tag:Silver2016_alphago] could be trained on the evolutionary dynamics of
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
before assembling.  Binning methods began with many k-mer techniques [@tag:Karlin]
and then delved into other clustering algorithms, such as self-organizing maps
(SOM) [@tag:Abe].  Then came the taxonomic classification problem,  with researchers
naturally using BLAST [@tag:blast], followed by other machine learning techniques
such as SVMs [@tag:McHardy], naive Bayesian classifiers [@tag:nbc], etc. to classify
each read.  Then, researchers began to use techniques that could be used to
estimate relative abundances of an entire sample, instead of the precise but
painstakingly slow read-by-read classification.  Relative abundance
estimators (a.k.a diversity profilers) are MetaPhlan [@tag:Metaphlan], (WGS)Quikr [@tag:wgsquikr],
and some configurations of tools like OneCodex [@tag:onecodex] and LMAT [@tag:lmat].  While one
cannot identify which reads were mapped back to an organism using relative
abundance estimators, they can be useful for faster comparative and other
downstream analyses.   Newer methods hope to classify reads and estimate
relative abundances at faster rates [@tag:Vervier] and as of this writing, there
are more than 70 metagenomic taxonomic classifiers in existence.  Besides
binning and classification of species, there is functional identification and
annotation of sequence reads [@tag:yok @tag:Soueidan]. However, the focus on
taxonomic/functional annotation is just the first step.  Once organisms are
identified, there is the interest in understanding the interrelationship
between these organisms and host/environment phenotypes [@tag:Guetterman].  One of
the first attempts was a survey of supervised classification methods for
microbes->phenotype classification [@tag:Knights], followed by similar studies
that are more massive in scale [@tag:Stratnikov @tag:Segata].  There have been
techniques that bypass the taxonomic classification step altogether [@tag:Ding],
(sequence composition to phenotype classification).  Also, researchers have
looked into how feature selection can improve classification [@tag:Liu @tag:Segata],
and techniques have been proposed that are classifier-independent
[@tag:Ditzler @tag:Ditzler2].

So, how have neural networks (NNs) been of use?    Most neural networks are being
used for short sequence->taxa/function classification, where there is a lot of data
for training (and thus suitable for NNs).  Neural networks have been applied
successfully to gene annotation (e.g. Orphelia [@tag:Hoff] and FragGeneScan [@doi:10.1093/nar/gkq747]),
which usually has plenty of training examples.  Representations (similar to Word2Vec [@tag:Word2Vec] in
natural language processing) for protein family classification has been introduced and classified
with a skip-gram  neural network [@tag:Asgari].  Recurrent neural networks show good performance for
homology and protein family identification [@tag:Hochreiter @tag:Sonderby].  Interestingly,
Hochreiter, who invented Long Short Term Memory, delved into homology/protein family
classification in 2007, and therefore, deep learning is deeply rooted in
functional classification methods.

One of the first techniques of “de novo” genome binning used self-organizing maps, a
type of NN [@tag:Abe].  Essinger et al. use ART, a neural network algorithm called Adaptive
Resonance Theory, to cluster similar genomic fragments and showed that it has better
performance than K-means.  However, other methods based on interpolated Markov models
[@tag:Salzberg] have performed better than these early genome binners.  Also, neural networks
can be slow, and therefore, have had limited use for reference-based taxonomic
classification, with TAC-ELM [@tag:TAC-ELM] being the only NN-based algorithm to taxonomically
classify massive amounts of metagenomic data.  Also, neural networks can fail to perform
if there are not enough training examples, which is the case with taxonomic classification
(since only ~10% of estimated species have been sequenced). An initial study shows that
deep neural networks have been successfully applied to  taxonomic classification of 16S rRNA genes,
with convolutional networks  provide about 10% accuracy genus-level improvement over RNNs and even random
forests [@tag:Mrzelj].  However, this study performed 10-fold cross-validation on 3000 sequences in total.

Due to the traditionally small numbers of metagenomic samples in studies, neural network uses for
classifying phenotype from microbial composition are just beginning.   A standard MLP
was able to classify wound severity from microbial species present in the wound [@doi:10.1016/j.bjid.2015.08.013].
Recently, multi-layer, recurrent networks (and convolutional
networks) have been applied to microbiome genotype-phenotype, with Ditzler et
al. being the first to associate soil samples with pH level using multi-layer
perceptrons, deep-belief networks, and recursive neural networks (RNNs)
[@tag:Ditzler3]. Besides classifying the samples appropriately, Ditzler shows
that internal phylogenetic tree nodes inferred by the networks are
appropriate features representing low/high pH, which can provide additional
useful information and new features for future metagenomic sample comparison.
 Also, an initial study has show promise of these networks for diagnosing
disease [@tag:Faruqi].  

There are still a lot of challenges with applying deep neural networks to metagenomics problems.  They are not ideal for microbial/functional composition->phenotype classification because most studies contain tens of samples (~20->40) and
hundreds/thousands of features (aka species).  Such underdetermined/ill-conditioned problems
are still a challenge for deep neural networks that require many more training examples than
features to sufficiently converge the weights on the hidden layers.  Also, due to convergence issues
(slowness and instability due to large neural networks modeling very large datasets [@arxiv:1212.0901v2]),
taxonomic classification of reads from whole genome sequencing seems out of reach at the moment for deep neural
networks -- due to only thousands of full-sequenced genomes as compared to hundreds of thousands of 16S rRNA sequences
available for training.

However, because recurrent neural networks are showing success for base-calling (and thus removing the large error in
the measurement of a pore's current signal) for the relatively new Oxford Nanopore sequencer [@tag:Boza], there is hope that
the process of denoising->organism/function classification can be combined into one step in using powerful LSTM's. LSTM's
are working miracles in raw speech signal->meaning translation [@tag:Sutskever], and combining steps in metagenomics are not
out of the question.  For example, metagenomic assembly usually requires binning then assembly, but could deep neural nets
accomplish both tasks in one network? Does functional/taxonomic classification need to be separate processes?  The largest
potential in deep learning is to learn "everything" in one complex network, with a plethora of labeled (reference) data and
unlabeled (microbiome experiments) examples.

### Sequencing and variant calling

While we have so far discussed the role of deep learning in analyzing genomic
data, deep learning approaches can also substantially improve our ability to
obtain the genomic data itself. We will discuss two specific challenges: calling
SNPs (single nucleotide polymorphisms) and indels (insertions and deletions)
with high specificity and sensitivity, and improving the accuracy of new types
of data such as nanopore sequencing. These two tasks are critical for studying
rare variation, allele-specific transcription and translation, and splice site
mutations, among others. In the clinical realm, sequencing of rare tumor clones
and other genetic diseases will require accurate calling of SNP and indels.

Current methods achieve relatively high (>99%) precision at 90% recall for SNPs
and indel calls from Illumina short-read data [@tag:Poplin2016_deepvariant], yet
this leaves a large number of potentially clinically significant remaining false
positives and false negatives. These methods have so far relied on experts to
build probabilistic models that reliably separate signal from noise. However,
this process is time consuming and, more importantly, fundamentally limited by
how well we understand and can model the factors that contribute to noise.
Recently, two groups have applied deep learning to construct data-driven and,
therefore, unbiased noise models. One of these models, DeepVariant, leverages
Inception, a neural network trained for image classification by Google Brain, by
encoding reads around a candidate SNP as a 221x100 bitmap image, where each
column is a nucleotide and each row is a read from the sample library
[@tag:Poplin2016_deepvariant]. The top 5 rows represent the reference, and the
bottom 95 rows represent randomly sampled reads that overlap the candidate
variant. Each RGBA (red/green/blue/alpha) image pixel encodes the base (A, C, T,
G) as a different R value, quality score as a G value, strand as a B value, and
variation from the reference as the alpha value. The neural network outputs
genotype probabilities for each candidate variant. They were able to achieve
better performance than GATK, a leading genotype caller, even when GATK was
given information about population variation for each candidate variant. Another
method, still in its infancy, hand-developed 642 features for each candidate
variant and fed these vectors into a fully connected deep neural network
[@tag:Torracinta2016_deep_snp]. Unfortunately, this feature set required at
least 15 iterations of software development to fine-tune, which will likely not
be generalizable.

Going forward, we believe that variant calling will benefit more from optimizing
neural network architectures than from developing features by hand. An
interesting and informative next step would be to rigorously test whether
encoding raw sequence and quality data as an image, tensor, or some other mixed
format produces the best variant calls. Because many of the latest neural
network architectures (ResNet, Inception, Xception, and others) are already
optimized for and pre-trained on generic, large-scale image datasets
[@tag:Chollet2016_xception], encoding genomic data as images could prove to be a
generally effective, and efficient, strategy.

In limited experiments, DeepVariant was robust to sequencing depth, read length,
and even species [@tag:Poplin2016_deepvariant]. However, a model built on
Illumina data, for instance, may not be applicable to PacBio long-read data or
MinION nanopore data, which have vastly different specificity and sensitivity
profiles and signal-to-noise characteristics. Recently, Boza et al. used
bidirectional recurrent neural networks to infer the *E. coli* sequence from
MinION nanopore electric current data with 2% higher per-base accuracy than the
proprietary hidden Markov model-based algorithm Metrichor (86% to 88%)
[@tag:Boza]. Unfortunately, training any neural network requires a large amount
of data, which is often not available for new sequencing technologies. To
circumvent this, one very preliminary study simulated mutations and spiked them
into somatic and germline RNA-seq data, then trained and tested a neural network
on simulated paired RNA-seq and exome sequencing data [@tag:Torracinta2016_sim].
However, because this model was not subsequently tested on ground-truth
datasets, it is unclear whether simulation can produce sufficiently realistic
data to produce reliable models.

Method development for interpreting new types of sequencing data has
historically taken two steps: first, easily implemented hard cutoffs that
prioritize specificity over sensitivity, then expert development of
probabilistic models with hand-developed inputs [@tag:Torracinta2016_sim]. We
anticipate that these steps will be replaced by deep learning, which will infer
features simply by its ability to optimize a complex model against data.
