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

Proteins play fundamental roles in all biological processes including the maintenance of cellular integrity, metabolism, transcription/translation, and cell-cell communication. Complete description of protein structures and functions is a fundamental step towards understanding biological life and also highly relevant in the development of therapeutics and drugs. Tons of protein sequences have been generated, but fewer than 100,000 of them have experimentally-solved structures. As a result, computational structure prediction is essential for a majority number of protein sequences. However, predicting protein 3D structures from sequence alone is very challenging, especially when similar templates are not available. In the past decades, various computational methods have been developed to predict protein structure from different aspects, including prediction of secondary structure, torsion angles, solvent accessibility, inter-residue contact map, disorder regions and side-chain packing.

Machine learning is extensively applied to predict protein structures and some success has been achieved. For example, secondary structure can be predicted with about 80% of Q3 accuracy by shallow machine learning methods such as PSIPRED [@doi:10.1093/bioinformatics/16.4.404]. Starting from 2012, deep learning has been gradually introduced to protein structure prediction. The adopted deep learning models include deep belief network, LSTM(long short-term memory), deep convolutional neural networks (DCNN) and deep convolutional neural fields[@doi:10.1007/978-3-319-46227-1_1 @doi:10.1038/srep18962]. Here we focus on deep learning methods for two representative subproblems: secondary structure prediction and contact map prediction. Secondary structure refers to local conformation of a sequence segment while a contact map contains information of global conformation.

Protein secondary structure prediction. Protein secondary structure can be described by 3 states or 8 states with the latter providing finer-grained information than the former. However, many more methods are developed to predict 3-state secondary structure than 8-state secondary structure. A predictor is typically evaluated by Q3 and Q8 accuracy, respectively. Qi et al. developed a multi-task deep learning method to simultaneously predict several local structure properties including secondary structures [@doi:10.1371/journal.pone.0032235]. Cheng group predicted secondary structure using deep belief networks [@doi: 10.1109/TCBB.2014.2343960]. Zhou developed an iterative deep learning framework to simultaneously predict secondary structure, backbone torsion angles and solvent accessibility [@doi:10.1038/srep11476]. However, none of these deep learning methods achieved significant improvement over PSIPRED, a 2-layer neural network method in terms of Q3 accuracy. In 2014, Zhou and Troyanskaya demonstrated that they can improve Q8 accuracy over conditional neural fields [@doi: 10.1002/pmic.201100196], a shallow architecture, by using a deep supervised and convolutional generative stochastic network[@arXiv:1403.1347], but did not report any results in terms of Q3 accuracy. In 2016 Wang and Xu developed a deep convolutional neural fields (DeepCNF) model and showed that this model can significantly improve secondary structure prediction in terms of both Q3 and Q8 accuracy[@doi:10.1038/srep18962]. DeepCNF is the first that reports Q3 accuracy of 84-85%, much higher than the 80% accuracy maintained by PSIPRED for more than 10 years. DeepCNF is also shown that it can improve prediction of solvent accessibility and disorder regions [@doi:10.1007/978-3-319-46227-1_1].

Protein contact map prediction. Contact-assisted protein folding represents a promising new direction for ab initio folding of proteins without good templates in PDB, but it requires accurate contact prediction. Evolutionary coupling analysis (ECA) is an effective contact prediction method for some proteins with a very large number (>1000) of sequence homologs, but ECA fares poorly for proteins without many sequence homologs. Since (soluble) proteins with many sequence homologs are very likely to have a good template in PDB, to make contact-assisted folding really useful for ab initio folding, it is essential to predict accurate contacts for proteins without many sequence homologs. By combining ECA with a few other protein features, shallow neural network-based supervised learning methods such as MetaPSICOV [@doi: 10.1093/bioinformatics/btu791] and CoinDCA-NN[@doi:10.1093/bioinformatics/btv472] have shown some advantage over ECA for proteins with a small number of sequence homologs, but their accuracy is still not very good. In recent years, deep learning methods have been explored for contact prediction. For example, Di Lena et al. introduced a deep spatio-temporal neural network (up to 100 layers) that utilizes both spatial and temporal features to predict protein contacts[@doi:10.1093/bioinformatics/bts475]. Cheng group applied deep belief networks and boosting techniques to protein contact prediction [@10.1093/bioinformatics/bts598]. They trained deep networks by layer-wise unsupervised learning followed by fine-tuning of the entire network. Elofsson group developed an iterative deep learning technique for contact prediction, in which Random Forests are applied to predict contacts at each iteration [@doi:10.1371/journal.pcbi.1003889]. However, when blindly tested in the well-known CASP competitions, these methods do not show any advantage over MetaPSICOV[@doi: 10.1093/bioinformatics/btu791], a 2-layer neural network method. Only until 2016, Xu group proposed a novel deep learning method [@doi:10.1371/journal.pcbi.1005324] that can significantly improve contact prediction accuracy over MetaPSICOV especially for proteins without many sequence homologs. Xu’s deep model is formed by one 1D residual neural network and one 2D residual neural network. Blindly tested in the latest CASP competition (i.e., CASP12), Xu’s deep learning method is ranked first in terms of the total F1 score (a widely-used performance metric) on free-modeling targets as well as the whole set of targets. In this test, the group ranked second also employed a deep learning method. Even MetaPSICOV, which ranked third, employed deeper and wider layers than its old version. Xu group has also demonstrated in another blind test CAMEO (which can be interpreted as a fully-automated CASP) [@url:http://www.cameo3d.org/] that the predicted contacts can fold quite a few proteins with a novel fold and only 65-300 sequence homologs. Xu’s method also works well on membrane protein contact prediction even if trained mostly by non-membrane proteins.


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

*@gailrosen will write this*

### Sequencing and variant calling

*We have one nanopore paper in the issues and very recent work on variant calling
that looks worthy of inclusion.*
