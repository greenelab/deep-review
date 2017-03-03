Transcription Factor and RNA-binding proteins are key components for gene
regulation, making them very important to understand for higher level
biological processes. While high-throughput sequencing techniques such as
ChIP-seq have been able to accurately identify binding regions for DNA and
RNA proteins, these experiments are both time consuming and expensive. In
addition, the sequencing methods do not provide any sort of analysis on the
proteins which would lead to a better understanding of the underlying process.
Thus, there is a need to computationally predict and understand these binding
regions de novo from sequences.

####Transcription Factors

Transcription Factors (TFs) are regulatory proteins which bind to certain
locations on a DNA sequence and controls the rate of genetic information
transcription. Chromatin immunoprecipitation and massively parallel DNA
sequencing (ChIP-seq) technologies are able to identify highly likely binding
sites for a certain TF, and databases such as ENCODE have provided ChIP-seq
data for hundreds of different TFs across many laboratories. However, ChIP-seq
experiments are expensive and time consuming. Since the data that scientists
have discovered is available, in silico methods to predict binding sites are of
great interest, thus eliminating the need to do new ChIP-seq experiments every
time analysis is done on a new sequence.

In order to computationally predict TFBSs on a DNA sequence, researchers
initially used consensus sequences and position weight matrices to match
against a test sequence [@tag:Stormo2000_dna]. Simple neural network
classifiers were then proposed to differentiate positive and negative binding
sites, but did not show significant improvements over the weight matrix
matching methods [@tag:Horton1992_assessment]. Later, SVM techniques
outperformed the generative methods by using k-mer features
\cite{Ghandi2014_enhanced, Setty2015_seqgl}, but string kernel based SVM
systems are limited by expensive computational cost proportional to the number
of training and testing sequences. Most recently,
[@tag:Alipanahi2015_predicting] showed that a convolutional neural network
models could achieve state of the art results on the TFBS task, are scalable
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
@tag:Lanchantin2016_motif@tag:Shrikumar2016_blackbox].
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
