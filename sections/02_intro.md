## Introduction

Biology and medicine are rapidly becoming data-intensive. A recent comparison of
genomics with social media, online videos, and other data-intensive scientific
disciplines suggested that genomics alone would equal or surpass other fields in
data generation and analysis within the next decade
[@doi:10.1371/journal.pbio.1002195]. The volume and complexity of these data
present not only new opportunities, but also new challenges. Automated
algorithms will be crucial in extracting meaningful patterns and actionable
knowledge that allow us to better treat, categorize, or study disease, all
within data constrained and privacy critical environments.

Over the past five years, a class of machine learning algorithms known as deep
learning has revolutionized image classification as well as a wide variety of
other fields. In a famous and early example, scientists from Google demonstrated
that a neural network could learn to identify cats simply by watching online
videos [@url:http://research.google.com/archive/unsupervised_icml2012.html].
These architectures quickly surpassed previous best-in-class methods that
required extensive customization. More recently, "off-the-shelf" deep neural
network approaches have demonstrated success from the game of Go
[@doi:10.1038/nature16961] to quantum physics [@doi:10.1126/science.aag2302].

What if, more generally, deep learning could solve the challenges presented by
the growth of data in biomedicine? Could these algorithms identify the "cats"
hidden in our data - the patterns unknown to the researcher - and act on them?
In this review, we examine whether deep learning's transformation of biomedical
science is simply a matter of time or if there are unique challenges posed by
biomedical data that render deep learning methods either more challenging or
less fruitful to apply.

### Defining deep learning

The term deep learning has come to refer to a collection of new techniques that,
together, have demonstrated breakthrough gains over existing best-in-class
machine learning algorithms across several fields. It is built on artificial
neural networks, an idea that was first proposed in 1943
[@doi:10.1007/BF02478259] as a model for how biological brains process
information. Since then, interest in neural networks as computational models has
waxed and waned several times. This history is interesting in its own right
[@doi:10.1103/RevModPhys.34.135]. In recent years, attention has shifted back to
neural networks as processing power has allowed deep learning techniques to
surge ahead of other machine learning techniques. Our focus is primarily on the
downstream applications enabled by these advances.

Several important advances make the current surge of work done in this area
possible. Easy-to-use software packages have brought the techniques of the field
out of the specialist's toolkit to a broad community of computational
scientists. Additionally, new techniques for fast training have enabled their
application to larger datasets [@arxiv:1106.5730]. Dropout of nodes, edges and
layers makes networks more robust, even when the number of parameters is very
large. New neural network approaches are also well suited for addressing
distinct challenges. For example, neural networks structured as autoencoders or
as adversarial networks require no labels and are now regularly used for
unsupervised tasks. In this review, we do not exhaustively discuss the different
types of deep neural network architectures. A recent book from Goodfellow et al
[@url:http://www.deeplearningbook.org/] covers these in detail. Finally, the
larger datasets now available are also well suited to fitting the many
parameters that exist for deep neural networks. The convergence of these factors
currently makes deep learning extremely adaptable and capable of addressing the
nuanced differences of each domain to which it is applied. 

### Will deep learning transform the study of human disease?

With this review, we set out to address the question: what would need to be true
for deep learning to transform how we categorize, study, and treat individuals
to maintain or restore health? We choose a high bar for "transform." Andrew
Grove, the former CEO of Intel, coined the term Strategic Inflection Point to
refer to a change in technologies or environment that requires a business to be
fundamentally reshaped
[@url:http://www.intel.com/pressroom/archive/speeches/ag080998.htm]. Here, we
seek to identify whether deep learning is an innovation that can induce a
strategic inflection point in the practice of biology or medicine. We structure
the review with an eye on precision medicine.

There are numerous examples where deep learning has been applied to biological
problems and produced somewhat improved results, and there are numerous reviews
that have focused on general applications of deep learning in biology
[@doi:10.1038/nbt.3313 @doi:10.1002/minf.201501008
@doi:10.3109/10409238.2015.1135868 @doi:10.1021/acs.molpharmaceut.5b00982
@doi:10.15252/msb.20156651 @doi:10.1093/bib/bbw068]. Specifically, we have
sought cases where deep learning enables researchers to solve challenges that
were previously considered infeasible, or if it makes difficult, tedious, and
non-routine analyses routine.

We find that domain-specific considerations have greatly influenced how to best
harness the power and flexibility of deep learning. Model interpretability is
often critical: understanding the patterns in data may be just as important as
fitting the data. In addition, there are important and pressing questions about
how to build networks that can efficiently represent the underlying structure
and logic of the data. Domain experts can play important roles in designing
networks to represent data appropriately, encoding the most salient prior
knowledge and assessing success or failure. There is also great potential to
create deep learning systems that are not intended to replace biologists and
clinicians but rather cooperate with them, working to prioritize experiments or
streamline tasks that do not require expert judgment.

Based on our guiding question, we focus on the application of deep learning to
topics of biomedical importance. We have divided the large range of topics into
three broad classes: Disease and Patient Categorization, Fundamental Biological
Study, and Patient Treatment. Below, we briefly introduce the types of
questions, approaches and data that are typical for each class in the
application of deep learning.

#### Disease and Patient Categorization

A key challenge in biomedicine is the accurate classification of diseases and
disease subtypes. In oncology, current "gold standard" approaches include
histology, which requires interpretation by experts, or a small panel of
molecular markers, such as cell surface receptors or gene expression. One
example is the PAM50 approach to classifying breast cancer where the expression
of 50 marker genes divides breast cancer patients into four subtypes.
Significant heterogeneity still remains within these four subtypes
[@doi:10.1200/JCO.2008.18.1370 @doi:10.1158/1078-0432.CCR-13-0583]. Given the
increasing wealth of molecular data available, a more comprehensive subtyping
seems possible.

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

Deep learning can be applied to answer more fundamental biological questions; it
is especially suited to leveraging large amounts of data from high-throughput
"omics" studies. One classic biological problem where machine learning, and now
deep learning, has been extensively applied is molecular target prediction. For
example, Lee et al. used deep recurrent neural networks (RNN) to predict gene
targets of microRNAs [@doi:10.1109/icnn.1994.374637]. Wang et al. used a
residual CNN to predict protein-protein contacts on a genome-wide scale
[@doi:10.1101/073239]. Some of the many recent exciting applications of deep
learning include the prediction of protein secondary structure based on sequence
data [@doi:10.1109/tcbb.2014.2343960 @doi:10.1038/srep18962], recognition of
functional genomic elements such as enhancers and promoters [@doi:10.1101/036129
@doi:10.1007/978-3-319-16706-0_20 @doi:10.1093/nar/gku1058], and predicting the
deleterious effects of nucleotide polymorphisms
[@doi:10.1093/bioinformatics/btu703].

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
