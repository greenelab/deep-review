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

*Predicting gene expression levels and unsupervised approaches for learning
from gene expression.  Those could be divided into separate sub-sections.*

### Splicing

*A separate section from general gene expression section above.*

### Transcription factors and RNA-binding proteins

*Existing reviews have covered some of these papers rather well and we do not
want to repeat what has already been well-stated elsewhere.  This could
be split into two sub-sections or kept very brief.*

### Promoters, enhancers, and related epigenomic tasks

*We may want to be selective about what we discuss and not list every
application in this area.*

### Micro-RNA binding

*miRNAs are important biologically, but have neural networks produced anything
particularly notable in this area?*

### Protein secondary and tertiary structure

*Jinbo Xu is writing this*

### Signaling

*There is not much content here.  Can [@tag:Chen2015_trans_species] be covered
elsewhere?*

### Cellular phenotypes

*These are primarily imaging-based phenotypes.  We have not surveyed this area
very comprehensively.  We could decide to not make imaging a primary focus,
refer to existing reviews, and mention only a few particularly noteworthy
representative papers.  Alternatively, we need to expand our literature review
and summaries immediately if someone wants to be responsible for this
sub-section.*

*Transfer learning from non-biological datasets to biological imaging
data could fit here, and that does seem like an important topic.  Or
transfer learning could be a more general topic for the Discussion section.*

### Single-cell

*There are not many neural network papers in this area (yet), unless we count
imaging applications.  But there is still plenty to discuss.  The existing
methods [@tag:Arvaniti2016_rare_subsets @tag:Angermueller2016_single_methyl]
use interesting network architectures to approach single-cell data.
[@tag:Shaham2016_batch_effects] could fit here.*

### Metagenomics

*@gailrosen will write this:*
Metagenomics (which refers to the study of microbial communities derived from 16S rRNA and/or whole-genome shotgun DNA) has revolutionized the study of micro-scale ecosystems within us and around us. There is increasing literature of applying machine learning in general to metagenomic analysis.   In the late 2000’s, a plethora of machine learning methods were applied to classifying DNA sequencing reads to the thousands of species within a sample.  An important problem is genome assembly from these mixed-organism samples.  And to do that, the organisms should be “binned” before assembling.  Binning methods began with many k-mer techniques [refs] and then delved into other clustering algorithms, such as self-organizing maps (SOM).  Then came the taxonomic classification problem,  with researchers naturally using BLAST [blast], followed by other machine learning techniques such as SVMs [McHardy], naive Bayesian classifiers [nbc], etc. to classify each read.  Then, researchers began to use techniques that could be used to estimate relative abundances of an entire sample, instead of the precise but painstakingly slow read-by-read classification.  Relative abundance estimators (a.k.a diversity profilers) are MetaPhlan[ref], (WGS)Quikr[ref], and some configurations of tools like OneCodex[ref] and LMAT[ref].  While one cannot identify which reads were mapped back to an organism using relative abundance estimators, they can be useful for faster comparative and other downstream analyses.   Newer methods hope to classify reads and estimate relative abundances at faster rates [Vervier] and as of this writing, there are more than 70 metagenomic taxonomic classifiers in existence.  Besides binning and classification of species, there is functional identification and annotation of sequence reads [Yok,Soueidan].
	However, the focus on taxonomic/functional annotation is just the first step.  Once organisms are identified, there is the interest in understanding the interrelationship between these organisms and host/environment phenotypes [Guetterman].  One of the first attempts was a survey of supervised classification methods for microbes->phenotype classification [Knights], followed by similar studies that are more massive in scale [Stratnikov, Segata].  There have been techniques that bypass the taxonomic classification step altogether [Ding] (sequence composition->phenotype classification).  Also, researchers have looked into how feature selection can improve classification [Liu, Segata], and techniques have been proposed that are classifier-independent [Ditzler,Ditzler].

So, how have neural networks been of use?  One of the first techniques of genome binning used neural networks [Abe]. Neural networks can be slow, and so far only TAC-ELM [tac-elm] has utilized it to taxonomically classify massive amounts of metagenomic data.  Also, neural networks can fail to perform if there are not enough training examples, which is the case with taxonomic classification (since only ~10% of estimated species have been sequenced).  For “de novo” genome binning, Essinger et al. use ART, a neural network algorithm called Adaptive Resonance Theory, to cluster similar genomic fragments and showed that it has better performance than K-means;  however, other methods based on interpolated Markov models [Salzberg] have performed better.  Due to the complexity of the problem, neural networks have been applied more to gene annotation (e.g. Orphelia [Hoff]), which usually have plenty of training examples.  Representations (similar to Word2Vec [ref] in natural language processing) for protein family classification has been introduced and classified with a skip-gram neural network [Asgari].  Recurrent neural networks show good performance for homology and protein family identification [Hochreiter, Sonderby].  Interestingly, Hochreiter, who invented Long Short Term Memory, delved into homology/protein family classification in 2007, and therefore, deep learning is deeply rooted in functional classification methods.  

Most neural networks are being used for short sequence->taxa/function classification, where there is a lot of data for training (and thus suitable for NNs).  And, as a short side note, recurrent neural networks are showing success for base-calling (and thus removing the large error in the measurement of a pore's current signal) for the relatively new Oxford Nanopore sequencer [Boza].  However, due to small nubmers of metagenomic samples in studies, neural network uses for classifying phenotype from microbial composition are just beginning.   A standard MLP was able to classify wound severity from microbial species present in the wound [Kizek, 2015].  Recently, multi-layer, recurrent networks (and convolutional networks) have been applied to microbiome genotype-phenotype, with Ditzler et al. being the first to associate soil samples with pH level using multi-layer perceptrons, deep-belief networks, and recursive neural networks (RNNs)  [Ditzler] .  Besides classifying the samples appropriately, Ditzler shows that internal phylogenetic tree nodes inferred by the networks are appropriate features representing low/high pH, which can provide additional useful information and new features for future metagenomic sample comparison.  Also, an initial study has show promise of these networks for diagnosing disease [Faruqi].  However, deep neural networks are not ideal for such problems since there are tens of samples (~20->40) available and hundreds/thousands of features (aka species).  Such underdetermined problems are still a challenge for deep neural networks that require many more training examples than features to sufficiently converge the weights on the hidden layers.  

In fact, due to convergence issues of neural networks, one would think that taxonomic classification would be impossible for deep neural networks.  However, with the 16S rRNA having hundreds of thousands of full-sequenced examples (compared to several thousand fully-sequenced whole-genome sequences), deep neural networks have been successfully applied to taxonomic classification of 16S rRNA genes, with convolutional networks outperforming RNNs and even random forests [Mrzelj].

### Sequencing and variant calling

*We have one nanopore paper in the issues and very recent work on variant calling
that looks worthy of inclusion.*
