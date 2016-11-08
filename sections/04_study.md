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
specific content to present.*

### Gene expression

*Predicting gene expression levels and unsupervised approaches for learning
from gene expression.  Those could be divided into separate sub-sections.*

### Splicing

*Combine this with gene expression?*

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

### Protein secondary and tertiarty structure

*We have not surveyed this area comprehensively yet.*

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
use interesting network architectures to approach single-cell data.*

### Methylation

*Is there enough content for a sub-section?  [@tag:Angermueller2016_single_methyl]
can be discussed with the single-cell papers.*

### Metagenomics

*Is there enough content for a sub-section?*

### Sequencing

*Is there enough content for a sub-section?  We have one nanopore paper
in the issues.*
