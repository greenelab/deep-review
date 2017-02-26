## Discussion

*This section provides meta-commentary that spans the Categorize, Study, and
Treat subject areas.  The candidate sub-sections below are initial ideas that
can be further pruned.*

### Evaluation

*What are the challenges in evaluating deep learning models that are specific to
this domain?  This can include a discussion of ROC versus precision-recall
curves for the imbalanced classes often encountered in biomedical datasets.
It could also mention alternative metrics that are used in specific sub-areas
such as enrichment factors in virtual screening.  A lack of true gold standard
data for some problems complicates both training and evaluation.  Confidence-
weighted labels are valuable when available.*

### Interpretation

*Most of our examples pertain to the Study papers.  Does this discussion
belong there or can we generalize it and keep it here?  Specific points would
include the dangers of over-interpreting hidden units, pros/cons of specific
techniques (see issues), and recommendations.  Some other reviews have addressed
this in part as well.*

### Data limitations

*Related to evaluation, are there data quality issues in genomic, clinical, and
other data that make this domain particularly challenging?  Are these worse than
what is faced in other non-biomedical domains?*

*Many applications have used relatively small training datasets.  We might
discuss workarounds (e.g. semi-synthetic data, splitting instances, etc.) and
how this could impact future progress.  Might this be why some studies have
resorted to feature engineering instead of learning representations from low-
level features?  Is there still work to be done in finding the right low-level
features in some problems?*

### Hardware limitations and scaling

*Several papers have stated that memory or other hardware limitations
artificially restricted the number of training instances, model inputs/outputs,
hidden layers, etc.  Is this a general problem worth discussing or will it be
solved naturally as hardware improves and/or groups move to distributed deep
learning frameworks?  Does hardware limit what types of problems are accessible
to the average computational group, and if so, will that limit future progress?
For instance, some hyperparameter search strategies are not feasible for a lab
with only a couple GPUs.*

*Some of this is also outlined in the Categorize section.  We can decide where
it best fits.*

Efficiently scaling deep learning is challenging, and there is a high
computational cost (e.g., time, memory, energy) associated with training neural
networks and using them for classification. As such, neural networks
have only recently found widespread use [@tag:Schmidhuber2014_dnn_overview].

Many have sought to curb the costs of deep learning, with methods ranging from
the very applied (e.g., reduced numerical precision [@tag:Gupta2015_prec
@tag:Bengio2015_prec @tag:Sa2015_buckwild @tag:Hubara2016_qnn]) to the exotic
and theoretic (e.g., training small networks to mimic large networks and
ensembles [@tag:Caruana2014_need @tag:Hinton2015_dark_knowledge]). The largest
gains in efficiency have come from computation with graphics processing units
(GPUs) [@tag:Raina2009_gpu @tag:Vanhoucke2011_cpu @tag:Seide2014_parallel
@tag:Hadjas2015_cc @tag:Edwards2015_growing_pains
@tag:Schmidhuber2014_dnn_overview], which excel at the matrix and vector
operations so central to deep learning. The massively parallel nature of GPUs
allows additional optimizations, such as accelerated mini-batch gradient
descent [@tag:Vanhoucke2011_cpu @tag:Seide2014_parallel @tag:Su2015_gpu
@tag:Li2014_minibatch]. However, GPUs also have a limited quantity of memory,
making it difficult to implement networks of significant size and
complexity on a single GPU or machine [@tag:Raina2009_gpu
@tag:Krizhevsky2013_nips_cnn]. This restriction has sometimes forced
computational biologists to use workarounds or limit the size of an analysis.
For example, Chen et al. [@tag:Chen2016_gene_expr] aimed to infer the
expression level of all genes with a single neural network, but due to
memory restrictions they randomly partitioned genes into two halves and
analyzed each separately. In other cases, researchers limited the size
of their neural network [@tag:Wang2016_protein_contact
@tag:Gomezb2016_automatic]. Some have also chosen to use slower
CPU implementations rather than sacrifice network size or performance
[@tag:Yasushi2016_cgbvs_dnn].

Steady improvements in GPU hardware may alleviate this issue somewhat, but it
is not clear whether they can occur quickly enough to keep up with the growing
amount of available biological data or increasing network sizes. Much has
been done to minimize the memory
requirements of neural networks [@tag:CudNN @tag:Caruana2014_need
@tag:Gupta2015_prec @tag:Bengio2015_prec @tag:Sa2015_buckwild
@tag:Chen2015_hashing @tag:Hubara2016_qnn], but there is also growing
interest in specialized hardware, such as field-programmable gate arrays
(FPGAs) [@tag:Edwards2015_growing_pains @tag:Lacey2016_dl_fpga] and
application-specific integrated circuits (ASICs). Specialized hardware promises
improvements in deep learning at reduced time, energy, and memory
[@tag:Edwards2015_growing_pains]. Logically, there is less software for highly
specialized hardware [@tag:Lacey2016_dl_fpga], and it could be a difficult
investment for those not solely interested in deep learning. However, it is
likely that such options will find increased support as they become a more
popular platform for deep learning and general computation.

Distributed computing is a general solution to intense computational
requirements, and has enabled many large-scale deep learning efforts. Early
approaches to distributed computation [@tag:Mapreduce @tag:Graphlab] were
not suitable for deep learning [@tag:Dean2012_nips_downpour],
but significant progress has been made. There
now exist a number of algorithms [@tag:Dean2012_nips_downpour @tag:Dogwild
@tag:Sa2015_buckwild], tools [@tag:Moritz2015_sparknet @tag:Meng2016_mllib
@tag:TensorFlow], and high-level libraries [@tag:Keras @tag:Elephas] for deep
learning in a distributed environment, and it is possible to train very complex
networks with limited infrastructure [@tag:Coates2013_cots_hpc]. Besides
handling very large networks, distributed or parallelized approaches offer
other advantages, such as improved ensembling [@tag:Sun2016_ensemble] or
accelerated hyperparameter optimization [@tag:Bergstra2011_hyper
@tag:Bergstra2012_random].

Cloud computing, which has already seen adoption in genomics
[@tag:Schatz2010_dna_cloud], could facilitate easier sharing of the large
datasets common to biology [@tag:Gerstein2016_scaling @tag:Stein2010_cloud],
and may be key to scaling deep learning. Cloud computing affords researchers
significant flexibility, and enables the use of specialized hardware (e.g.,
FPGAs, ASICs, GPUs) without significant investment. With such flexibility, it
could be easier to address the different challenges associated with the
multitudinous layers and architectures available
[@tag:Krizhevsky2014_weird_trick]. Though many are reluctant to store sensitive
data (e.g., patient electronic health records) in the cloud,
secure/regulation-compliant cloud services do exist [@tag:RAD2010_view_cc].

*TODO: Write the transition once more of the Discussion section has been
fleshed out.*

### Code, data, and model sharing

*Reproducibiliy is important for science to progress. In the context of deep
learning applied to advance human healthcare, does reproducibility have
different requirements or alternative connotations? With vast hyperparameter
spaces, massively heterogeneous and noisy biological data sets, and black box
interpretability problems, how can we best ensure reproducible models? What
might a clinician, or policy maker, need to see in a deep model in order to
influence healthcare decisions? Or, is deep learning a hypothesis generation
machine that requires manual validation?*

### Transfer learning/transferability of features

* https://github.com/greenelab/deep-review/issues/139#issuecomment-268901804
