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

### Morphological phenotypes

A field poised for dramatic revolution by deep learning is 
bioimage analysis - and not in the way you might first think. 
Thus far, the primary use of deep learning for biological 
images has been for segmentation - that is, for the identification 
of biologically relevant structures in images such as nuclei, 
infected cells, or vasculature. Once so-called regions of 
interest have been identified, it is often straightforward 
to measure biological properties of interest, such as fluorescence 
intensities, textures, and sizes. Given the dramatic successes of 
deep learning in biological imaging, we simply refer to recent reviews
`TODO: insert deep learning/bioimaging reviews here, one candidate is 
Kraus OZ, Frey BJ: Computer vision for high content screening. Crit Rev Biochem Mol Biol 2016, 51:102-109 `. 
We believe deep learning will become a commonplace tool for 
biological image segmentation once user-friendly tools exist.

We anticipate an additional kind of paradigm shift in bioimaging that 
will be brought about by deep learning: what if images of biological 
samples, from simple cell cultures to three-dimensional organoids and 
tissue samples, could be mined for much more extensive biologically 
meaningful information than is currently standard? In biomedical research, 
by far the most common paradigm is for biologists to decide in advance 
what feature to measure in images from their assay system. But images 
of cells contain a wide variety of quantitative information, and deep 
learning may just be the tool to extract it. Although classical methods 
of segmentation and feature extraction can produce hundreds of metrics 
per cell in an image, deep learning is unconstrained by human intuition 
and can in theory extract more subtle features.

The impact on biomedicine could be enormous. Comparing cell population 
morphologies using conventional methods of segmentation and feature 
extraction has already proven useful for functionally annotating genes 
and alleles, identifying the cellular target of small molecules, and 
identifying disease-specific phenotypes suitable for drug screening 
[@doi:10.1016/j.copbio.2016.04.003] [@doi:10.1002/cyto.a.22909] [@doi:10.1083/jcb.201610026].  
Deep learning would bring to these new kinds of experiments - known 
as image-based profiling or morphological profiling - a higher degree of 
accuracy, stemming from the freedom from human-tuned feature extraction strategies. 

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
