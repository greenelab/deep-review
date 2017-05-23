## Deep learning to study the fundamental biological processes underlying human
## disease

The study of cellular structure and core biological processes -- transcription,
translation, signaling, metabolism, etc. -- in humans and model organisms will
greatly impact our understanding of human disease over the long horizon
[@tag:Nih_curiosity]. Predicting how cellular systems respond to environmental
perturbations and are altered by genetic variation remain daunting tasks. Deep
learning offers new approaches for modeling biological processes and integrating
multiple types of omic data [@doi:10.1038/ncomms13090], which could eventually
help predict how these processes are disrupted in disease. Recent work has
already advanced our ability to identify and interpret genetic variants, study
microbial communities, and predict protein structures, which also relates to the
problems discussed in the drug development section. In addition, unsupervised
deep learning has enormous potential for discovering novel cellular states from
gene expression, fluorescence microscopy, and other types of data that may
ultimately prove to be clinically relevant.

Progress has been rapid in genomics and imaging, fields where important tasks
are readily adapted to well-established deep learning paradigms.
One-dimensional convolutional and recurrent neural networks are well-suited for
tasks related to DNA- and RNA-binding proteins, epigenomics, and RNA splicing.
Two dimensional CNNs are ideal for segmentation, feature extraction, and
classification in fluorescence microscopy images
[@doi:10.3109/10409238.2015.1135868]. Other areas, such as cellular signaling,
are biologically important but studied less-frequently to date, with some
exceptions [@tag:Chen2015_trans_species].  This may be a consequence of data
limitations or greater challenges in adapting neural network architectures to
the available data.  Here, we highlight several areas of investigation and
assess how deep learning might move these fields forward.

### Gene expression

Gene expression technologies characterize the abundance of many thousands of RNA
transcripts within a given organism, tissue, or cell. This characterization can
represent the underlying state of the given system and can be used to study
heterogeneity across samples as well as how the system reacts to perturbation.
While gene expression measurements were traditionally made by quantitative
polymerase chain reaction (qPCR), low-throughput fluorescence-based methods, and
microarray technologies, the field has shifted in recent years to primarily
performing RNA sequencing (RNA-seq) to catalog whole transcriptomes. As RNA-seq
continues to fall in price and rise in throughput, sample sizes will increase
and training deep models to study gene expression will become even more useful.

Already several deep learning approaches have been applied to gene expression
data with varying aims. For instance, many researchers have applied unsupervised
deep learning models to extract meaningful representations of gene modules or
sample clusters. Denoising autoencoders have been used to cluster yeast
expression microarrays into known modules representing cell cycle processes
[@tag:Gupta2015_exprs_yeast] and to stratify yeast strains based on chemical and
mutational perturbations [@tag:Chen2016_exprs_yeast]. Shallow (one hidden layer)
denoising autoencoders have also been fruitful in extracting biological insight
from thousands of _Pseudomonas aeruginosa_ experiments [@tag:Tan2015_adage
@tag:Tan2016_eadage] and in aggregating features relevant to specific breast
cancer subtypes [@tag:Tan2014_psb]. These unsupervised approaches applied to
gene expression data are powerful methods for identifying gene signatures that
may otherwise be overlooked. An additional benefit of unsupervised approaches is
that ground truth labels, which are often difficult to acquire or are incorrect,
are nonessential. However, the genes that have been aggregated into features
must be interpreted carefully. Attributing each node to a single specific
biological function risks over-interpreting models. Batch effects could cause
models to discover non-biological features, and downstream analyses should take
this into consideration.

Deep learning approaches are also being applied to gene expression prediction
tasks. For example, a deep neural network with three hidden layers outperformed
linear regression in inferring the expression of over 20,000 target genes based
on a representative, well-connected set of about 1,000 landmark genes
[@tag:Chen2016_gene_expr]. However, while the deep learning model outperformed
existing algorithms in nearly every scenario, the model still displayed poor
performance. The paper was also limited by computational bottlenecks that
required data to be split randomly into two distinct models and trained
separately. It is unclear how much performance would have increased if not for
computational restrictions.

Epigenetic data, combined with deep learning, may have sufficient explanatory
power to infer gene expression. For instance, a convolutional neural network
applied to histone modifications, termed DeepChrome, [@tag:Singh2016_deepchrome]
improved prediction accuracy of high or low gene expression over existing
methods. Deep learning can also integrate different data types. For example,
Liang et al. combined RBMs to integrate gene expression, DNA methylation, and
miRNA data to define ovarian cancer subtypes [@tag:Liang2015_exprs_cancer].
While these approaches are promising, many convert gene expression measurements
to categorical or binary variables, thus ablating many complex gene expression
signatures present in intermediate and relative numbers.

Deep learning applied to gene expression data is still in its infancy, but the
future is bright. Many previously untestable hypotheses can now be interrogated
as deep learning enables analysis of increasing amounts of data generated by new
technologies. For example, the effects of cellular heterogeneity on basic
biology and disease etiology can now be explored by single-cell RNA-seq and
high-throughput fluorescence-based imaging, techniques we discuss below that
will benefit immensely from deep learning approaches.

### Splicing

Pre-mRNA transcripts can be spliced into different isoforms by retaining or
skipping subsets of exons or including parts of introns, creating enormous
spatiotemporal flexibility to generate multiple distinct proteins from a single
gene. This remarkable complexity can lend itself to defects that underlie many
diseases [@tag:Scotti2016_missplicing]. For instance, in Becker muscular
dystrophy, a point mutation in dystrophin creates an exon splice silencer that
induces skipping of exon 31. A recent study found that quantitative trait loci
(QTLs) that affect splicing in lymphoblastoid cell lines are enriched within
risk loci for schizophrenia, multiple sclerosis, and other immune diseases,
implicating mis-splicing as a more widespread feature of human pathologies than
previously thought [@tag:Li2016_variation].

Sequencing studies routinely return thousands of unannotated variants, but which
cause functional changes in splicing and how are those changes manifested?
Prediction of a "splicing code" has been a goal of the field for the past
decade. Initial machine learning approaches used a naïve Bayes model and a
2-layer Bayesian neural network with thousands of hand-derived sequence-based
features to predict the probability of exon skipping
[@tag:Barash2010_splicing_code @tag:Xiong2011_bayesian]. With the advent of deep
learning, more complex models were built that provided better predictive
accuracy [@tag:Xiong2015_splicing_code @tag:Jha2017_integrative_models].
Importantly, these new approaches can take in multiple kinds of epigenomic
measurements as well as tissue identity and RNA binding partners of splicing
factors. Deep learning is critical in furthering these kinds of integrative
studies where different data types and inputs interact in unpredictable (often
nonlinear) ways to create higher-order features. Moreover, as in gene expression
network analysis, interrogating the hidden nodes within neural networks could
potentially illuminate important aspects of splicing behavior. For instance,
tissue-specific splicing mechanisms could be inferred by training networks on
splicing data from different tissues, then searching for common versus
distinctive hidden nodes, a technique employed by Qin et al. for tissue-specific
transcription factor (TF) binding predictions [@tag:Qin2017_onehot].

A parallel effort has been to use more data with simpler models. An exhaustive
study using readouts of splicing for millions of synthetic intronic sequences
uncovered motifs that influence the strength of alternative splice sites
[@tag:Rosenberg2015_synthetic_seqs]. The authors built a simple linear model
using hexamer motif frequencies that successfully generalized to exon skipping.
In a limited analysis using SNPs (single nucleotide polymorphisms) from three
genes, it predicted exon skipping with three times the accuracy of an existing
deep learning-based framework [@tag:Xiong2015_splicing_code]. This case is
instructive in that clever sources of data, not just more descriptive models,
are still critical.

We already understand how mis-splicing of a single gene can cause diseases such
as Duchenne muscular dystrophy. The challenge now is to uncover how genome-wide
alternative splicing underlies complex, non-Mendelian diseases such as autism,
schizophrenia, Type 1 diabetes, and multiple sclerosis [@tag:JuanMateu2016_t1d].
As a proof of concept, Xiong et al. [@tag:Xiong2015_splicing_code] sequenced
five autism spectrum disorder and 12 control samples, each with an average of
42,000 rare variants, and identified mis-splicing in 19 genes with neural
functions. Such methods may one day enable scientists and clinicians to rapidly
profile thousands of unannotated variants for functional effects on splicing and
nominate candidates for further investigation. Moreover, these nonlinear
algorithms can deconvolve the effects of multiple variants on a single splice
event without the need to perform combinatorial *in vitro* experiments. The
ultimate goal is to predict an individual’s tissue-specific, exon-specific
splicing patterns from their genome sequence and other measurements to enable a
new branch of precision diagnostics that also stratifies patients and suggests
targeted therapies to correct splicing defects. However, to achieve this we
expect that methods to interpret the "black box" of deep neural networks and
integrate diverse data sources will be required.

### Transcription factors and RNA-binding proteins

Transcription factors and RNA-binding proteins are key components in gene
regulation and higher-level biological processes. TFs are regulatory proteins
that bind to certain genomic loci and control the rate of mRNA production. While
high-throughput sequencing techniques such as chromatin immunoprecipitation and
massively parallel DNA sequencing (ChIP-seq) have been able to accurately
identify targets for TFs, these experiments are both time consuming and
expensive. Thus, there is a need to computationally predict binding sites and
understand binding specificities *de novo* from sequence data. In this section
we focus on TFs, with the understanding that deep learning methods for TFs are
similar to those for RNA-binding proteins, though RNA-specific models do exist
[@doi:10.1186/s12859-017-1561-8].

ChIP-seq and related technologies are able to identify highly likely binding
sites for a certain TF, and databases such as ENCODE
[@tag:Consortium2012_encode] have made freely available ChIP-seq data for
hundreds of different TFs across many laboratories. In order to computationally
predict transcription factor binding sites (TFBSs) on a DNA sequence,
researchers initially used consensus sequences and position weight matrices to
match against a test sequence [@tag:Stormo2000_dna]. Simple neural network
classifiers were then proposed to differentiate positive and negative binding
sites but did not show significant improvements over the weight matrix matching
methods [@tag:Horton1992_assessment]. Later, support vector machines (SVMs)
outperformed the generative methods by using k-mer features
[@tag:Ghandi2014_enhanced @tag:Setty2015_seqgl], but string kernel-based SVM
systems are limited by their expensive computational cost, which is proportional
to the number of training and testing sequences.

With the advent of deep learning, Alipanahi et al.
[@tag:Alipanahi2015_predicting] showed that convolutional neural network models
could achieve state of the art results on the TFBS task and are scalable to a
large number of genomic sequences. Lanchantin et al. [@tag:Lanchantin2016_motif]
introduced several new convolutional and recurrent neural network models that
further improved TFBS predictive accuracy. Due to the motif-driven nature of the
TFBS task, most architectures have been convolution-based
[@tag:Zeng2016_convolutional]. While many models for TFBS prediction resemble
computer vision and NLP tasks, it is important to note that DNA sequence tasks
are fundamentally different. Thus the models should be adapted from traditional
deep learning models in order to account for such differences. For example,
motifs may appear in either strand of a DNA sequence, resulting in two different
forms of the motif (forward and reverse complement) due to complementary base
pairing. To handle this issue, specialized reverse complement convolutional
models share parameters to find motifs in both directions
[@tag:Shrikumar2017_reversecomplement].

Despite these advances, several challenges remain. First, because the inputs
(ChIP-seq measurements) are continuous and most current algorithms are designed
to produce binary outputs (whether or not there is TF binding at a particular
site), false positives or false negatives can result depending on the threshold
chosen by the algorithm. Second, most methods predict binding of TFs at sites in
isolation, whereas in reality multiple TFs may compete for binding at a single
site or act synergistically to co-occupy it. Fortunately, multi-task models are
rapidly improving at simultaneous prediction of many TFs' binding at any given
site [@tag:Zhou2015_deep_sea]. Third, it is unclear exactly how to define a
non-binding or "negative" site in the training data because the number of
positive binding sites of a particular TF is relatively small with respect to
the total number of base-pairs in a genome (see Discussion).

While deep learning-based models can automatically extract features for TFBS
prediction at the sequence level, they often cannot predict binding patterns for
cell types or conditions that have not been previously studied. One solution
could be to introduce a multimodal model that, in addition to sequence data,
incorporates cell-line specific features such as chromatin accessibility, DNA
methylation, or gene expression. Without cell-specific features, another
solution could be to use domain adaptation methods where the model trains on a
source cell type and uses unsupervised feature extraction methods to predict on
a target cell type. TFImpute [@tag:Qin2017_onehot] predicts binding in new cell
type-TF pairs, but the cell types must be in the training set for other TFs.
This is a step in the right direction, but a more general domain transfer model
across cell types would be more useful.

Deep learning can also illustrate TF binding preferences. Lanchantin et al.
[@tag:Lanchantin2016_motif] and Shrikumar et al. [@tag:Shrikumar2017_learning]
developed tools to visualize TF motifs learned from TFBS classification tasks.
Alipanahi et al. [@tag:Alipanahi2015_predicting] also introduced mutation maps,
where they could easily mutate, add, or delete base pairs in a sequence and see
how the model changed its prediction. Though time consuming to assay in a lab,
this was easy to simulate with a computational model. As we learn to better
visualize and analyze the hidden nodes within deep learning models, our
understanding of TF binding motifs and dynamics will likely improve.

### Promoters, enhancers, and related epigenomic tasks

Transcriptional control is undoubtedly a vital, early part of the regulation of
gene expression. An abundance of sequence and associated functional data (e.g.
ENCODE [@tag:Consortium2012_encode] and ExAC [@doi:10.1038/nature19057]) exists
across species. At the same time, studies of gene regulation have often focused
on the protein (binding) rather than the promoter level
[@doi:10.1093/bib/4.1.22], perhaps due to the ill-defined nature of
cis-regulatory elements (CREs). A promoter itself can be seen as an assemblage
of "active" binding sites for transcription factors interspersed by
less-characterized and perhaps functionally silent spacer regions. However, the
sequence signals that control the start and stop of transcription and
translation are still not well understood, compounded by incomplete
understanding of alternative transcripts and the context for these alternatives.
Sequence similarity is poor even between functionally correlated genes. While
homologs might be studied for insight, they may not exist or may be just as
poorly characterized.

Recognizing enhancers presents additional challenges. Enhancers may be up to one
million base pairs upstream or downstream from the affected promoter on either
strand and even within the introns of other genes [@doi:10.1038/nrg3458]. They
do not necessarily operate on the nearest gene and may affect multiple genes.
Their activity is frequently tissue- or context-specific. A substantial fraction
of enhancers displays modest or no conservation across species. There is no
universal enhancer sequence signal or marker for enhancers, and some literature
suggests that enhancers and promoters may be just categories along a spectrum
[@doi:10.1016/j.tig.2015.05.007]. One study [@doi:10.1101/gr.173518.114] even
showed that only 33% of predicted regulatory regions could be validated, while a
class of "weak" predicted enhancers were strong drivers of expression. Yet there
is growing evidence for their vast ubiquity, making them possibly the
predominant functional non-coding element. Thus, identifying enhancers is
critical yet the search space is large.

While prior (non-deep learning) approaches have made steady improvements on
promoter prediction, there is little consensus on the best approach and
performance is poor. Typically algorithms will recognize only half of all
promoters, with an accompanying high false positive rate
[@doi:10.1101/gr.7.9.861]. Methods with better sensitivity generally do so at
the cost of poorer specificity. Conventional identification of enhancers has
leaned heavily on simple conservation or laborious experimental techniques, with
only moderate sensitivity and specificity. For example, while chromatin
accessibility has often been used for identifying enhancers, this also
"recognizes" a wide variety of other functional elements, like promoters,
silencers, and repressors.

The complex nature of CREs and our lack of understanding makes them a natural
candidate for deep learning approaches. Indeed, neural networks were used for
promoter recognition as early as 1996, albeit with mixed results
[@doi:10.1016/S0097-8485(96)80015-5]. Since then, there has been much work in
applying deep learning to this area, although little in the way of comparative
studies or formal benchmarks. We therefore focus on a few recent important
studies to outline the state of the art and extant problems.

Basset [@doi:10.1101/gr.200535.115] trained CNNs on DNA accessibility datasets,
getting a marked improvement on previous methods, albeit still with a high false
positive rate. The multi-task architecture resembles DeepSEA
[@tag:Zhou2015_deep_sea], which predicted open chromatin regions and histone
modifications in addition to TF binding. As noted above, predicting DNA
accessibility conflates enhancers with other functional sites. Basset also
featured a useful interpretability approach, introducing known protein binding
motifs into sequences and measuring the change in predicted accessibility.

Umarov et al. [@doi:10.1371/journal.pone.0171410] demonstrated the use of CNNs
in recognizing promoter sequences, outperforming conventional methods
(sensitivity and specificity exceeding 90%). While some results were achieved
over bacterial promoters (which are considerably simpler in structure), roughly
similar performance was found for human promoters. This work also included a
simple method for model interpretation, randomly substituting bases in a
recognized promoter region, then checking for a change in recognition (see
Discussion).

Xu et al. [@doi:10.1109/BIBM.2016.7822593] applied CNNs to the detection of
enhancers, achieving incremental improvements in specificity and sensitivity
over a previous SVM-based approach, and much better performance for
cell-specific enhancers. A massive improvement in speed was also achieved.
Additionally, they compared the performance of different CNN architectures,
finding that while layers for batch normalization improved performance, deeper
architectures decreased performance.

Singh et al. [@doi:10.1101/085241] approached the problem of predicting
enhancer-promoter interactions from solely the sequence and location of putative
enhancers and promoters in a particular cell type. Performance was comparative
to state-of-the-art conventional techniques that used the whole gamut of full
functional genomic and non-sequence data.

Given the conflation between different CREs, the study of Li et al.
[@doi:10.1101/041616] is particularly interesting.  They used a feed-forward
neural network to distinguish classes of CREs and activity states. Active
enhancers and promoters could be easily be distinguished, as could active and
inactive elements. Perhaps unsurprisingly, it was difficult to distinguish
between inactive enhancers and promoters. They also investigated the power of
sequence features to drive classification, finding that beyond CpG islands, few
were useful.

In summary, deep learning is a promising approach for identifying CREs, able to
interrogate sequence features that are complex and ill-understood, already
offering marked improvements on the prior state of the art. However, neural
network architectures for this task need to be systematically compared. The
challenges in predicting TF binding -- such as the lack of large gold standard
datasets, model interpretation, and defining negative examples -- are pertinent
to CRE identification as well. Furthermore, the quality and meaning of training
data needs to be closely considered, given that a "promoter" or "enhancer" may
only be putative or dependent on the experimental method or context of
identification. Otherwise we risk building detectors not for CREs but putative
CREs. Most deep learning studies in this area currently predict the 1D location
of enhancers, but modeling 3D chromatin conformations, enhancer-promoter
interactions [@doi:10.1101/085241], and enhancer-target gene interactions will
be critical for understanding transcriptional regulation.

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
thermodynamic stability of the miRNA-mRNA complex [@tag:Agarwal2015_targetscan].
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
to predict microRNA target sites with higher specificity and sensitivity than
TargetScan. Excitingly, these tools seem to show that RNNs can accurately align
sequences and predict bulges, mismatches, and wobble base pairing without
requiring the user to input secondary structure predictions or thermodynamic
calculations. Further incremental advances in deep learning for miRNA and target
prediction will likely be sufficient to meet the current needs of systems
biologists and other researchers who use prediction tools mainly to nominate
candidates that are then tested experimentally.

### Protein secondary and tertiary structure

Proteins play fundamental roles in almost all biological processes, and
understanding their structure is critical for basic biology and drug
development. UniProt currently has about 94 million protein sequences, yet fewer
than 100,000 proteins across all species have experimentally-solved structures
in Protein Data Bank (PDB). As a result, computational structure prediction is
essential for a majority of proteins. However, this is very challenging,
especially when similar solved structures, called templates, are not available
in PDB. Over the past several decades, many computational methods have been
developed to predict aspects of protein structure such as secondary structure,
torsion angles, solvent accessibility, inter-residue contact maps, disorder
regions, and side-chain packing. In recent years, multiple deep learning
architectures have been applied, including deep belief networks, LSTM (long
short-term memory), CNNs, and deep convolutional neural fields (DeepCNF)
[@doi:10.1007/978-3-319-46227-1_1 @doi:10.1038/srep18962].

Here we focus on deep learning methods for two representative sub-problems:
secondary structure prediction and contact map prediction. Secondary structure
refers to local conformation of a sequence segment, while a contact map contains
information on all residue-residue contacts. Secondary structure prediction is a
basic problem and an almost essential module of any protein structure prediction
package. Contact prediction is much more challenging than secondary structure
prediction, but it has a much larger impact on tertiary structure prediction. In
recent years, the accuracy of contact prediction has significantly improved
[@doi:10.1371/journal.pcbi.1005324 @doi:10.1093/bioinformatics/btu791
@doi:10.1073/pnas.0805923106 @doi:10.1371/journal.pone.0028766].

Protein secondary structure can exhibit three different states (alpha helix,
beta strand, and loop regions) or eight finer-grained states. Q3 and Q8 accuracy
pertain to 3-state or 8-state predictions, respectively. Several groups
[@doi:10.1371/journal.pone.0032235 @doi:10.1109/TCBB.2014.2343960
@doi:10.1038/srep11476] initiated the application of deep learning to protein
secondary structure prediction but were unable to achieve significant
improvement over the *de facto* standard method PSIPRED
[@doi:10.1006/jmbi.1999.3091], which uses two shallow feedforward neural
networks. In 2014, Zhou and Troyanskaya demonstrated that they could improve Q8
accuracy by using a deep supervised and convolutional generative stochastic
network [@arxiv:1403.1347]. In 2016 Wang et al. developed a DeepCNF model that
significantly improved Q3 and Q8 accuracy as well as prediction of solvent
accessibility and disorder regions [@doi:10.1038/srep18962
@doi:10.1007/978-3-319-46227-1_1]. DeepCNF achieved a higher Q3 accuracy than
the standard maintained by PSIPRED for more than 10 years. This improvement may
be mainly due to the ability of convolutional neural fields to capture
long-range sequential information, which is important for beta strand
prediction. Nevertheless, the improvements in secondary structure prediction
from DeepCNF are unlikely to result in a commensurate improvement in tertiary
structure prediction since secondary structure mainly reflects coarse-grained
local conformation of a protein structure.

Protein contact prediction and contact-assisted folding (i.e. folding proteins
using predicted contacts as restraints) represents a promising new direction for
*ab initio* folding of proteins without good templates in PDB. Co-evolution
analysis is effective for proteins with a very large number (>1000) of sequence
homologs [@doi:10.1371/journal.pone.0028766], but otherwise fares poorly for
proteins without many sequence homologs. By combining co-evolution information
with a few other protein features, shallow neural network methods such as
MetaPSICOV [@doi:10.1093/bioinformatics/btu791] and CoinDCA-NN
[@doi:10.1093/bioinformatics/btv472] have shown some advantage over pure
co-evolution analysis for proteins with few sequence homologs, but their
accuracy is still far from satisfactory. In recent years, deeper architectures
have been explored for contact prediction, such as CMAPpro
[@doi:10.1093/bioinformatics/bts475], DNCON [@doi:10.1093/bioinformatics/bts598]
and PConsC [@doi:10.1371/journal.pcbi.1003889]. However, blindly tested in the
well-known CASP competitions, these methods did not show any advantage over
MetaPSICOV [@doi:10.1093/bioinformatics/btu791].

Recently, Wang et al. proposed the deep learning method RaptorX-Contact
[@doi:10.1371/journal.pcbi.1005324], which significantly improves contact
prediction over MetaPSICOV and pure co-evolution methods, especially for
proteins without many sequence homologs. It employs a network architecture
formed by one 1D residual neural network and one 2D residual neural network.
Blindly tested in the latest CASP competition (i.e. CASP12
[@url:http://www.predictioncenter.org/casp12/rrc_avrg_results.cgi]),
RaptorX-Contact ranked first in F1 score (a widely-used performance metric
combining sensitivity and specificity) on free-modeling targets as well as the
whole set of targets. In CAMEO (which can be interpreted as a fully-automated
CASP) [@url:http://www.cameo3d.org/], its predicted contacts were also able to
fold proteins with a novel fold and only 65-330 sequence homologs. This
technique also worked well on membrane proteins even when trained on
non-membrane proteins [@arxiv:1704.07207]. RaptorX-Contact performed better
mainly due to introduction of residual neural networks and exploitation of
contact occurrence patterns by simultaneously predicting all the contacts in a
single protein.

Taken together, *ab initio* folding is becoming much easier with the advent of
direct evolutionary coupling analysis and deep learning techniques. We expect
further improvements in contact prediction for proteins with fewer than 1000
homologs by studying new deep network architectures. However, it is unclear if
there is an effective way to use deep learning to improve prediction for
proteins with few or no sequence homologs. Finally, the deep learning methods
summarized above also apply to interfacial contact prediction for protein
complexes but may be less effective since on average protein complexes have
fewer sequence homologs.

### Morphological phenotypes

A field poised for dramatic revolution by deep learning is bioimage analysis.
Thus far, the primary use of deep learning for biological images has been for
segmentation -- that is, for the identification of biologically relevant
structures in images such as nuclei, infected cells, or vasculature -- in
fluorescence or even brightfield channels [@doi:10.1371/journal.pcbi.1005177].
Once so-called regions of interest have been identified, it is often
straightforward to measure biological properties of interest, such as
fluorescence intensities, textures, and sizes. Given the dramatic successes of
deep learning in biological imaging, we simply refer to articles that review
recent advancements [@doi:10.3109/10409238.2015.1135868
@doi:10.1371/journal.pcbi.1005177 @doi:10.1007/978-3-319-24574-4_28]. For deep
learning to become commonplace for biological image segmentation, user-friendly
tools need to be developed.

We anticipate an additional kind of paradigm shift in bioimaging that will be
brought about by deep learning: what if images of biological samples, from
simple cell cultures to three-dimensional organoids and tissue samples, could be
mined for much more extensive biologically meaningful information than is
currently standard? For example, a recent study demonstrated the ability to
predict lineage fate in hematopoietic cells up to three generations in advance
of differentiation [@doi:10.1038/nmeth.4182]. In biomedical research, by far the
most common paradigm is for biologists to decide in advance what feature to
measure in images from their assay system. Although classical methods of
segmentation and feature extraction can produce hundreds of metrics per cell in
an image, deep learning is unconstrained by human intuition and can in theory
extract more subtle features through its hidden nodes. Already, there is
evidence deep learning can surpass the efficacy of classical methods
[@doi:10.1101/081364], even using generic deep convolutional networks trained on
natural images [@doi:10.1101/085118], known as transfer learning. Recent work by
Johnson et al. [@tag:Johnson2017_integ_cell] demonstrated how the use of a
conditional adversarial autoencoder allows for a probabilistic interpretation of
cell and nuclear morphology and structure localization from fluorescence images.
The proposed model is able to generalize well to a wide range of subcellular
localizations. The generative nature of the model allows it to produce
high-quality synthetic images predicting localization of subcellular structures
by directly modeling the localization of fluorescent labels. Notably, this
approach reduces the modeling time by omitting the subcellular structure
segmentation step.

The impact of further improvements on biomedicine could be enormous. Comparing
cell population morphologies using conventional methods of segmentation and
feature extraction has already proven useful for functionally annotating genes
and alleles, identifying the cellular target of small molecules, and identifying
disease-specific phenotypes suitable for drug screening
[@doi:10.1016/j.copbio.2016.04.003 @doi:10.1002/cyto.a.22909
@doi:10.1083/jcb.201610026]. Deep learning would bring to these new kinds of
experiments -- known as image-based profiling or morphological profiling -- a
higher degree of accuracy, stemming from the freedom from human-tuned feature
extraction strategies.

### Single-cell data

Single-cell methods are generating excitement as biologists recognize the vast
heterogeneity within unicellular species and between cells of the same tissue
type in the same organism [@tag:Gawad2016_singlecell]. For instance, tumor cells
and neurons can both harbor extensive somatic variation
[@tag:Lodato2015_neurons]. Understanding single-cell diversity in all its
dimensions -- genetic, epigenetic, transcriptomic, proteomic, morphologic, and
metabolic -- is key if treatments are to be targeted not only to a specific
individual, but also to specific pathological subsets of cells. Single-cell
methods also promise to uncover a wealth of new biological knowledge. A
sufficiently large population of single cells will have enough representative
"snapshots" to recreate timelines of dynamic biological processes. If tracking
processes over time is not the limiting factor, single-cell techniques can
provide maximal resolution compared to averaging across all cells in bulk
tissue, enabling the study of transcriptional bursting with single-cell
fluorescence *in situ* hybridization or the heterogeneity of epigenetic patterns
with single-cell Hi-C or ATAC-seq [@tag:Liu2016_sc_transcriptome
@tag:Vera2016_sc_analysis].  Joint profiling of single-cell epigenetic and
transcriptional states provides unprecedented views of regulatory processes
[@doi:10.1101/138685].

However, large challenges exist in studying single cells. Relatively few cells
can be assayed at once using current droplet, imaging, or microwell
technologies, and low-abundance molecules or modifications may not be detected
by chance due to a phenomenon known as dropout. To solve this problem,
Angermueller et al. [@tag:Angermueller2016_single_methyl] trained a neural
network to predict the presence or absence of methylation of a specific CpG site
in single cells based on surrounding methylation signal and underlying DNA
sequence, achieving several percentage points of improvement compared to random
forests or deep networks trained only on CpG or sequence information. Similar
deep learning methods have been applied to impute low-resolution ChIP-seq signal
from bulk tissue with great success, and they could easily be adapted to
single-cell data [@tag:Qin2017_onehot @tag:Koh2016_denoising]. Deep learning has
also been useful for dealing with batch effects [@tag:Shaham2016_batch_effects].

Examining populations of single cells can reveal biologically meaningful subsets
of cells as well as their underlying gene regulatory networks
[@tag:Gaublomme2015_th17]. Unfortunately, machine learning methods generally
struggle with imbalanced data -- when there are many more examples of class 1
than class 2 -- because prediction accuracy is usually evaluated over the entire
dataset. To tackle this challenge, Arvaniti et al.
[@tag:Arvaniti2016_rare_subsets] classified healthy and cancer cells expressing
25 markers by using the most discriminative filters from a CNN trained on the
data as a linear classifier. They achieved impressive performance, even for cell
types where the subset percentage ranged from 0.1 to 1%, significantly
outperforming logistic regression and distance-based outlier detection methods.
However, they did not benchmark against random forests, which tend to work
better for imbalanced data, and their data was relatively low dimensional.
Future work is needed to establish the utility of deep learning in cell subset
identification, but the stunning improvements in image classification over the
past 5 years [@tag:He2015_images] suggest transformative potential.

The sheer quantity of omic information that can be obtained from each cell, as
well as the number of cells in each dataset, uniquely position single-cell data
to benefit from deep learning. In the future, lineage tracing could be
revolutionized by using autoencoders to reduce the feature space of
transcriptomic or variant data followed by algorithms to learn optimal cell
differentiation trajectories [@tag:Qiu2017_graph_embedding] or by feeding cell
morphology and movement into neural networks
[@tag:Buggenthin2017_imaged_lineage]. Reinforcement learning algorithms
[@tag:Silver2016_alphago] could be trained on the evolutionary dynamics of
cancer cells or bacterial cells undergoing selection pressure and reveal whether
patterns of adaptation are random or deterministic, allowing us to develop
therapeutic strategies that forestall resistance. We are excited to see the
creative applications of deep learning to single-cell biology that emerge over
the next few years.

### Metagenomics

Metagenomics, which refers to the study of genetic material -- 16S rRNA and/or
whole-genome shotgun DNA -- from microbial communities, has revolutionized the
study of micro-scale ecosystems within and around us. In recent years, machine
learning has proved to be a powerful tool for metagenomic analysis. 16S rRNA has
long been used to deconvolve mixtures of microbial genomes, yet this ignores
more than 99% of the genomic content. Subsequent tools aimed to classify
300-3000 base pair reads from complex mixtures of microbial genomes based on
tetranucleotide frequencies, which differ across organisms [@tag:Karlin], using
supervised [@tag:McHardy @tag:nbc] or unsupervised methods [@tag:Abe]. Then,
researchers began to use techniques that could estimate relative abundances from
an entire sample faster than classifying individual reads [@tag:Metaphlan
@tag:wgsquikr @tag:lmat @tag:Vervier]. There is also great interest in
identifying and annotating sequence reads [@tag:yok @tag:Soueidan]. However, the
focus on taxonomic and functional annotation is just the first step. Several
groups have proposed methods to determine host or environment phenotypes from
the organisms that are identified [@tag:Guetterman @tag:Knights @tag:Stratnikov
@tag:Segata] or overall sequence composition [@tag:Ding]. Also, researchers have
looked into how feature selection can improve classification [@tag:Liu
@tag:Segata], and techniques have been proposed that are classifier-independent
[@tag:Ditzler @tag:Ditzler2].

How have neural networks been of use? Most neural networks are being used for
phylogenetic classification or functional annotation from sequence data where
there is ample data for training. Neural networks have been applied successfully
to gene annotation (e.g. Orphelia [@tag:Hoff] and FragGeneScan
[@doi:10.1093/nar/gkq747]). Representations (similar to Word2Vec [@tag:Word2Vec]
in natural language processing) for protein family classification have been
introduced and classified with a skip-gram neural network [@tag:Asgari].
Recurrent neural networks show good performance for homology and protein family
identification [@tag:Hochreiter @tag:Sonderby].

One of the first techniques of *de novo* genome binning used self-organizing
maps, a type of neural network [@tag:Abe]. Essinger et al.
[@tag:Essinger2010_taxonomic] used Adaptive Resonance Theory to cluster similar
genomic fragments and showed that it had better performance than k-means.
However, other methods based on interpolated Markov models [@tag:Salzberg] have
performed better than these early genome binners. Neural networks can be slow
and therefore have had limited use for reference-based taxonomic classification,
with TAC-ELM [@tag:TAC-ELM] being the only neural network-based algorithm to
taxonomically classify massive amounts of metagenomic data. An initial study
successfully applied neural networks to taxonomic classification of 16S rRNA
genes, with convolutional networks providing about 10% accuracy genus-level
improvement over RNNs and random forests [@tag:Mrzelj]. However, this study
evaluated only 3000 sequences.

Neural network uses for classifying phenotype from microbial composition are
just beginning. A standard multi-layer perceptron (MLP) was able to classify
wound severity from microbial species present in the wound
[@doi:10.1016/j.bjid.2015.08.013]. Recently, Ditzler et al. associated soil
samples with pH level using MLPs, DBNs, and RNNs [@tag:Ditzler3]. Besides
classifying samples appropriately, internal phylogenetic tree nodes inferred by
the networks represented features for low and high pH. Thus, hidden nodes might
provide biological insight as well as new features for future metagenomic sample
comparison. Also, an initial study has shown promise of these networks for
diagnosing disease [@tag:Faruqi].

Challenges remain in applying deep neural networks to metagenomics problems.
They are not yet ideal for phenotype classification because most studies contain
tens of samples and hundreds or thousands of features (species). Such
underdetermined, or ill-conditioned, problems are still a challenge for deep
neural networks that require many training examples. Also, due to convergence
issues [@arxiv:1212.0901v2], taxonomic classification of reads from whole genome
sequencing seems out of reach at the moment for deep neural networks.  There are
only thousands of full-sequenced genomes as compared to hundreds of thousands of
16S rRNA sequences available for training.

However, because RNNs have been applied to base calls for the Oxford Nanopore
long-read sequencer with some success [@tag:Boza] (discussed further in the next
section), one day the entire pipeline, from denoising of through functional
classification, may be combined into one step by using powerful LSTMs
[@tag:Sutskever]. For example, metagenomic assembly usually requires binning
then assembly, but could deep neural nets accomplish both tasks in one network?
We believe the greatest potential in deep learning is to learn the complete
characteristics of a metagenomic sample in one complex network.

### Sequencing and variant calling

While we have so far primarily discussed the role of deep learning in analyzing
genomic data, deep learning can also substantially improve our ability to obtain
the genomic data itself. We discuss two specific challenges: calling SNPs and
indels (insertions and deletions) with high specificity and sensitivity and
improving the accuracy of new types of data such as nanopore sequencing. These
two tasks are critical for studying rare variation, allele-specific
transcription and translation, and splice site mutations. In the clinical realm,
sequencing of rare tumor clones and other genetic diseases will require accurate
calling of SNPs and indels.

Current methods achieve relatively high (>99%) precision at 90% recall for SNPs
and indel calls from Illumina short-read data [@tag:Poplin2016_deepvariant], yet
this leaves a large number of potentially clinically-important remaining false
positives and false negatives. These methods have so far relied on experts to
build probabilistic models that reliably separate signal from noise. However,
this process is time consuming and fundamentally limited by how well we
understand and can model the factors that contribute to noise. Recently, two
groups have applied deep learning to construct data-driven unbiased noise
models. One of these models, DeepVariant, leverages Inception, a neural network
trained for image classification by Google Brain, by encoding reads around a
candidate SNP as a 221x100 bitmap image, where each column is a nucleotide and
each row is a read from the sample library [@tag:Poplin2016_deepvariant]. The
top 5 rows represent the reference, and the bottom 95 rows represent randomly
sampled reads that overlap the candidate variant. Each RGBA
(red/green/blue/alpha) image pixel encodes the base (A, C, T, G) as a different
red value, quality score as a green value, strand as a blue value, and variation
from the reference as the alpha value. The neural network outputs genotype
probabilities for each candidate variant. They were able to achieve better
performance than GATK, a leading genotype caller, even when GATK was given
information about population variation for each candidate variant. Another
method, still in its infancy, hand-developed 642 features for each candidate
variant and fed these vectors into a fully connected deep neural network
[@tag:Torracinta2016_deep_snp]. Unfortunately, this feature set required at
least 15 iterations of software development to fine-tune, which suggests that
these models may not generalize.

Going forward, variant calling will benefit more from optimizing neural network
architectures than from developing features by hand. An interesting and
informative next step would be to rigorously test if encoding raw sequence and
quality data as an image, tensor, or some other mixed format produces the best
variant calls. Because many of the latest neural network architectures (ResNet,
Inception, Xception, and others) are already optimized for and pre-trained on
generic, large-scale image datasets [@tag:Chollet2016_xception], encoding
genomic data as images could prove to be a generally effective and efficient
strategy.

In limited experiments, DeepVariant was robust to sequencing depth, read length,
and even species [@tag:Poplin2016_deepvariant]. However, a model built on
Illumina data, for instance, may not be optimal for PacBio long-read data or
MinION nanopore data, which have vastly different specificity and sensitivity
profiles and signal-to-noise characteristics. Recently, Boza et al. used
bidirectional recurrent neural networks to infer the *E. coli* sequence from
MinION nanopore electric current data with higher per-base accuracy than the
proprietary hidden Markov model-based algorithm Metrichor [@tag:Boza].
Unfortunately, training any neural network requires a large amount of data,
which is often not available for new sequencing technologies. To circumvent
this, one very preliminary study simulated mutations and spiked them into
somatic and germline RNA-seq data, then trained and tested a neural network on
simulated paired RNA-seq and exome sequencing data [@tag:Torracinta2016_sim].
However, because this model was not subsequently tested on ground-truth
datasets, it is unclear whether simulation can produce sufficiently realistic
data to produce reliable models.

Method development for interpreting new types of sequencing data has
historically taken two steps: first, easily implemented hard cutoffs that
prioritize specificity over sensitivity, then expert development of
probabilistic models with hand-developed inputs [@tag:Torracinta2016_sim]. We
anticipate that these steps will be replaced by deep learning, which will infer
features simply by its ability to optimize a complex model against data.
