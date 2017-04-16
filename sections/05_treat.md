## The impact of deep learning in treating disease and developing new treatments

*There will be some overlap with the Categorize section, and we may have to
determine which methods categorize individuals and which more directly match
patients with treatments.  The sub-section titles are merely placeholders.*

### Categorizing patients for clinical decision making

There has been sustained interest in applying deep learning to clinical
decision making for over two decades. In 1996, Tu
[@doi:10.1016/S0895-4356(96)00002-9] compared the effectiveness of artificial
neural networks and logistic regression, questioning whether deep learning
would replace traditional statistical methods for predicting medical
outcomes such as myocardial infarction [@doi:10.7326/0003-4819-115-11-843] or
mortality [@doi:10.1056/NEJM198509263131306]. He posited that while neural
networks have several advantages in representational power, the difficulties in
interpretation may limit clinical applications. In 2007, Lisboa and Taktak
[@doi:10.1016/j.neunet.2005.10.007] examined the use of artificial neural
networks in medical journals, concluding that neural networks provided an
increase in benefit to healthcare relative to traditional screening methods in
21 of 27 studies.

While significant progress has been made in developing deep learning methods
for diagnosis, it is not clear that these methods have yet transformed
clinical decision making. The difficulty in applying deep learning to clinical
decision making represents a challenge common to many deep learning
applications: it is much easier to predict an outcome than to suggest an
action to change the outcome. Several attempts at recasting the clinical
decision making problem into a prediction problem (i.e. prediction of which
treatment will most improve the patient's health) have accurately predicted
prescription habits, but technical and medical challenges remain for clinical
adoption. In particular, remaining challenges include actionable
interpretability of deep learning models, fitting deep models to limited and
heterogeneous data, and integrating complex predictive models into a dynamic
clinical environment.

#### Applications

##### Trajectory Prediction for Treatment

A common application for deep learning techniques in this domain is to
leverage the temporal structure of healthcare records. As previously
discussed, many studies [@arxiv:1606.04130
@arxiv:1606.01865 @doi:10.1109/ACCESS.2016.2618775 @arxiv:1510.07641]
have used deep recurrent networks to categorize patients but most stop short
of suggesting clinical decisions. Nemati et al [@doi:10.1109/EMBC.2016.7591355]
used deep reinforcement learning to optimize a heparin dosing policy for
intensive care patients. However, because the ideal dosing policy is unknown,
the model's predictions must be evaluated on counter-factual data. This
represents a common challenge when bridging the gap between research and
clinical practice: because the ground-truth is unknown, researchers struggle
to evaluate model predictions in the absence of interventional data, but
clinical application is unlikely until the model has been shown to be effective
. The impressive applications of deep reinforcement learning to other domains
[@doi:10.1038/nature16961] have relied on knowledge of the underlying
processes (e..g the rules of the game). Some models have been developed for
targeted medical problems [@doi:10.1136/amiajnl-2013-001815], but a
generalized engine is beyond current capabilities. Further development of the
rules underlying biological processes could unleash deep learning methods that
are currently hampered by the difficulties of counter-factual inference.

##### Efficient Clinical trials

A clinical task to deep learning which has been more successfully applied is
the assignment of patients to clinical trials. Ithapu et al
[@doi:10.1016/j.jalz.2015.01.010] used a randomized denoising autoenconder to
learn a multimodal imaging marker that predicts future cognitive and neural
decline from positron emission tomography (PET), amyloid
florbetapir PET, and structural magnetic resonance imaging. By accurately
predicting which cases will progress to dementia, they were able to
efficiently assign patients to a clinical trial and reduced the required
sample sizes by a factor of five.  Similarly, Artemov et al
[@doi:10.1101/095653] applied deep learning to predict which clinical trials
were likely to fail and which were likely to succeed. By predicting the side
effects and pathway activations of each drug, and then translating these
activations to a success proability, their deep learning-based approach was
able to significantly outperform a random forest classifier trained on gene
expression changes. These approaches suggest promising directions to improve
the efficiency of clinical trials and accelerate drug development.

#### Challenges

##### Actionable Interpretability

A common challenge in many applied deep learning problems is the consideration
of deep learning models as uninterpretable "black boxes". Without human-
intelligible reasoning for the model's predictions, it is difficult to trust
the model. This presents a major challenge for the risk-averse task of
clinical decision making. As described above, there has been some work to
directly assign treatment plans without interpretability; however, the removal
of human experts from the decision-making loop make the models difficult to
integrate with clinical practice. To alleviate this challenge, several studies
have attempted to create more interpretable deep models, either specifically
for healthcare or as a general procedure for deep learning.

For domain-specific models, studies have primarily focused on integrating
attention mechanisms with the neural networks. Attention mechanisms
dynamically weight the importance the neural network gives to each feature. By
inspecting the attention weights for a particular sample, a practitioner can
identify the important features for a particular prediction. Choi et al
[@arxiv:1608.05745] inverted the typical architectue of recurrent neural
networks to improve interpretability. In particular, they only used recurrent
connections in the attention generating procedure, leaving the hidden state
directly connected to the input variables. This model was able to produce
accurate diagnoses in which the contribution of previous hospital visits could
be directly interpreted. Choi et al [@arxiv:1611.07012] later extended this
work to take into account the structure of disease ontologies and found that
the concepts represented by the model were aligned with medical knowledge. Che
et al [@arxiv:1512.03542] introduced a knowledge-distillation approach which
used gradient boosted trees to learn interpretable healthcare features from
trained deep models.

As this challenge of interpretability is common across many domains, there is
significant interest in developing generic procedures for knowledge extraction
from deep models. Ribeiro et al [@arxiv:1602.04938] focus on interpreting
individual predictions rather than interpreting the model. By fitting simple
linear models to mimic the predictions of the deep learning model in a small
neighborhood of a data sample, they generated an interpretable model for each
prediction. While this procedure can provide interpretable models for each
sample, it is unclear whether these interpretable models are reliable.
Theoretical guarantees on the curvature of the predictions of deep learning
models are not known, and it is unclear whether predictions from deep learning
models are robust to sample noise. Toward quantifying the uncertainty of
predictions, there has been a renewed interest in confidence intervals for
deep neural networks. Early work from Chryssolouris et al
[@doi:10.1109/72.478409] provided confidence intervals under the assumption of
normally distributed error. However, Nguyen et al [@arxiv:1412.1897v4] showed
that the confidence of convolutional neural networks is not reliable; they can
output confidence scores over 99.99% even for samples that are purely noise.
Recently, Fong and Vedaldi [@arxiv:1704.03296] provided a framework for
understanding black box algorithms by perturbing input data. Further work in
interpreting predictions and understanding the knowledge learned by deep
neural networks seem necessary for transformative impact in clinical practice.

##### Integrating Deep Learning with Clinical Practice

As deep learning models are difficult to interpret, many current models have
been designed to replace aspects of clinical practice rather than to assist
trained clinicians. This makes it difficult to integrate deep learning with
clinical decision making. In addition, the challenges that physicians face are
largely similar to those faced by machine learning models. For a given
patient, the number of possible diseases is very large, with a long tail of
rare diseases. Furthermore, patients are highly heterogeneous and may present
with very different signs and symptoms for the same disease. Physicians are
experienced in treating patients with common diseases, but rare diseases are
extremely challenging. Unfortunately, machine learning methods also struggle
for rare diseases. Because deep learning models are data-intensive, directly
applying current deep learning models to diagnose patients with rare diseases
would require prohibitively large datasets. Focused effort in reducing the
data requirements of deep learning by integrating pre-existing knowledge or
compiling large datasets of patient records may unlock the power of deep
learning for clinical practice.

### Effects of drugs on transcriptomic responses

*We discussed a few papers that operate on Library of Network-Based Cellular
Signatures (LINCS) gene expression data.  We could briefly introduce the
goals of that resource and comment on the deep learning applications.  In the
Issues, we had reservations about whether the improvements in expression
prediction are good enough to make a practical difference in the domain and
feature selection and construction.*

### Ligand-Based Prediction of Bioactivity

In the biomedical domain, high-throughput chemical screening aims to improve
therapeutic options over a long term horizon [@tag:PerezSianes2016_screening]
`TODO: add another general screening reference`.  The objective is to discover
which small molecules (also referred to as chemical compounds or ligands)
effectively and specifically affect the activity of a target, such as a kinase,
protein-protein interaction, or broader cellular phenotype.  This screening
process can serve as the first step in the long drug discovery pipeline, where
novel chemicals are pursued for their ability to inhibit or enhance
disease-relevant biological mechanisms.  The appeal of machine learning in this
domain is the need to improve the efficiency of the initial high-throughput
screens such that sufficient candidate active compounds can be identified
without exhaustively screening libraries of hundreds of thousands or millions of
chemicals.  This task has been treated as a classification, regression, and
ranking problem.  In reality, it does not fit neatly into any of those
categories.  An ideal algorithm will rank a sufficient number of active
compounds before the inactives, but the rankings of actives relative to other
actives and inactives to other inactives is less important
[@tag:Swamidass2009_irv]. `TODO: can improve this first attempt at an intro by
reviewing more existing literature on the topic` `TODO: check which other
existing reviews should be referenced`

We primarily focus on ligand-based approaches that train on chemicals' features
without requiring knowledge of the target, as opposed to alternative strategies
that use target features such as the protein structure `TODO: add examples`.
Neural networks have a long history in this domain [@tag:Baskin2015_drug_disc]
`TODO: can add additional references besides this review`, and the 2012 Merck
Molecular Activity Challenge on Kaggle `TODO: need URL?` generated substantial
excitement about the potential for high-parameter deep learning approaches.  The
winning submission was an ensemble that included a multitask multilayer
perceptron network [@tag:Dahl2014_multi_qsar], and the Merck sponsors noted
drastic improvements over a random forest (RF) baseline, remarking "we have
seldom seen any method in the past 10 years that could consistently outperform
RF by such a margin" [@tag:Ma2015_qsar_merck].  Subsequent work explored the
effects of jointly modeling far more targets than the Merck challenge
[@tag:Unterthiner2014_screening @tag:Ramsundar2015_multitask_drug], with
[@tag:Ramsundar2015_multitask_drug] showing that the benefits of multitask
networks had not yet saturated even with 259 targets.  Although a deep learning
approach, DeepTox, was also the overall winner of another competition, the
Toxicology in the 21st Century (Tox21) Data Challenge, it did not dominate
alternative methods as thoroughly as in other domains.  DeepTox was the top
performer on only 9 of 15 targets, and in some cases there was little separation
between DeepTox and the second best method on those 9 tasks.  A reliance on AUC
ROC `TODO: define here?` for the evaluation (see Discussion) further hinders the
ability to declare Tox21 as an outright success for deep learning.

In retrospect, the nuanced Tox21 performance may be more reflective of the
practical challenges encountered in ligand-based chemical screening than the
extreme enthusiasm generated by the Merck competition.  A study of 22 absorption
distribution, metabolism, excretion, and toxicity (ADMET) tasks demonstrated
that there are limitations to multitask transfer learning that are in part a
consequence of the degree to which tasks are related [@tag:Kearnes2016_admet].
Some of the ADMET datasets showed far superior performance in multitask models
of only the 22 ADMET tasks relative to more expansive multitask networks that
included over 500 less-similar tasks.  `TODO: also has a good discussion of
information leakage in cross validation but that may be too detailed` In
addition, training datasets encountered in practical applications may be tiny
relative to what is available in public datasets and organized competitions.  A
study of BACE-1 inhibitors included only 1547 compounds
[@tag:Subramanian2016_bace1].  Machine learning models were able to train on
this limited dataset, but overfitting was a challenge and the differences
between random forests and a deep neural were negligible, especially in the
classification setting.  Overfitting is still a problem in larger chemical
screening datasets with tens or hundreds of thousands of compounds because the
number of active compounds can be very small, on the order of 0.1% or 1% of all
tested chemicals `TODO: verify those estimates`. This is consistent with the
strong performance of low-parameter neural networks that emphasize
compound-compound similarity, such as influence-relevance voter,
[@tag:Swamidass2009_irv  @tag:Lusci2015_irv] instead of predicting compound
activity directly from chemical features. `TODO: include recent DeepChem IRV
benchmarks?`

Much of the recent excitement in this domain has come from what could be
considered a creative experimentation phase, in which deep learning has offered
novel possibilities for feature representation and modeling of chemical
compounds.  A molecular graph, where atoms are nodes and bonds are edges, is a
natural way to represent a chemical structure.  Traditional machine learning
approaches relied on preprocessing the graph into a feature vector, such as a
fixed-width bit vector fingerprint [@tag:Rogers2010_fingerprints] in which each
bit represents the presence of absence of a particular chemical substructure in
the molecular graph. `TODO: this is a massive oversimplification because there
can be collisions, but I don't know how much detail to get into` Modern neural
networks can operate directly on the molecular graph as input.  Duvenaud et al
[@tag:Duvenaud2015_graph_conv] generalized standard circular fingerprints by
substituting discrete operations in the fingerprinting algorithm with operations
in a neural network, producing a real-valued feature vector instead of a bit
vector.  Other approaches offer trainable networks that can in theory learn
chemical feature representations that are optimized for a particular prediction
task.   Lusci et al adapted recursive neural networks for directed acyclic
graphs for undirected molecular graphs by creating an ensemble of directed
graphs in which one atom is selected as the root node [@tag:Lusci2013_rnn].  A
single feature vector is obtained by summing over all feature vectors for all
directed graphs in the ensemble.  Graph convolutions on undirected molecular
graphs have eliminated the need to enumerate artificial directed graphs,
learning feature vectors for atoms that are a function of the properties of
neighboring atoms and local regions on the molecular graph
[@tag:Kearnes2016_graph_conv @tag:AltaeTran2016_one_shot]. `TODO: add more
details on how graph convolutions work?`

Advances in chemical representation learning have not been limited to
graph-based neural networks.  The simplified molecular-input line-entry system
(SMILES) is a standard way to transform a chemical into string-based
representation.  A SMILES-to-SMILES autoencoder learns a continuous latent
feature space for chemicals [@tag:Gomezb2016_automatic].  In this learned
continuous space is it possible to train some types of supervised learning
algorithms or interpolate between continuous representations of chemicals in a
manner that is not possible with discrete (e.g. bit vector or string) features.
A drawback is that not all SMILES strings produced by the autoencoder's decoder
correspond to valid chemical structures. `TODO: could mention GANs here`
Altae-Tran et al developed a one-shot learning network
[@tag:AltaeTran2016_one_shot] to address the reality that most practical
chemical screening studies are unable to provide the thousands or millions of
training compounds that are needed to train larger multitask networks.  Using
graph convolutions to featurize chemicals, the network learns an embedding from
compounds into a continuous feature space such that compounds with similar
activities in a set of training tasks have similar embeddings.  The approach is
evaluated in an extremely challenging setting where the embedding is learned
from a subset of prediction tasks (e.g. activity assays for individual proteins)
and only one to ten labeled examples are provided as training data on a new
task.  On Tox21 targets, even when trained with _one_ task-specific active
compound and _one_ inactive compound, the model is able generalize reasonably
well because it has learned an informative embedding function from the related
tasks. Random forests, which cannot take advantage of the related training
tasks, trained in the same setting achieve near random performance.  Despite the
success on Tox21, performance on MUV datasets, which contains assays designed to
be challenging for chemical informatics algorithms, is considerably worse.  The
authors also demonstrate the limitations of transfer learning as embeddings
learned from the Tox21 assays have little utility for a drug adverse reaction
dataset.

In the long term, these novel, learned chemical feature representations may
prove to be essential for accurately predicting why some compounds with similar
structures yield similar target effects and others produce drastically different
results.  Currently, these methods are enticing but do not necessarily
outperform classic approaches by a large margin.  The neural fingerprints
[@tag:Duvenaud2015_graph_conv] were narrowly beaten by regression using
traditional circular fingerprints on a drug efficacy prediction task (but were
superior for predicting solubility or photovoltaic efficiency).  Graph
convolutions [@tag:Kearnes2016_graph_conv] performed comparably to a multitask
network using standard fingerprints and slightly better than the neural
fingerprints [@tag:Duvenaud2015_graph_conv] on the drug efficacy task but were
slightly worse than the influence-relevance voter method on an HIV dataset.
[@tag:Swamidass2009_irv].  `TODO: there are also problems with some papers using
ROC primarily for benchmarking, which skews results and makes it hard to assess
absolute performance, but I already alluded to that above and may leave further
discussion to the Discussion section`

We remain optimistic for the potential of deep learning and specifically
representation learning in this domain and propose that rigorous benchmarking on
broad and diverse prediction tasks will be as important as novel neural network
architectures to advance the state of the art _and convincingly demonstrate
superiority over traditional cheminformatics techniques_. Fortunately, there has
recently been significant progress in this direction. The DeepChem software
[@tag:AltaeTran2016_one_shot @url:https://github.com/deepchem/deepchem] and
MoleculeNet benchmarking suite [@tag:Wu2017_molecule_net] built upon it contain
chemical bioactivity and toxicity prediction datasets, multiple compound
featurization approaches including graph convolutions, and various machine
learning algorithms ranging from standard baselines like logistic regression and
random forests to recent neural network architectures.  Independent research
groups have already contributed additional datasets and prediction algorithms,
and adoption of common benchmarking evaluation metrics, datasets, and baseline
algorithms has the potential to establish the practical utility of deep learning
in chemical bioactivity prediction and lower the barrier to entry for machine
learning researchers without biochemistry expertise.

One open question in ligand-based screening pertains to the benefits and
limitations of transfer learning.  Multitask neural networks have shown the
advantages of jointly modeling many targets [@tag:Unterthiner2014_screening
@tag:Ramsundar2015_multitask_drug].  Other studies have shown the limitations of
transfer learning when the prediction tasks are insufficiently related
[@tag:Kearnes2016_admet @tag:AltaeTran2016_one_shot].  This has important
implications for representation learning.  The typical approach of improving
deep learning models by expanding the dataset size may not be applicable if only
"related" tasks are beneficial, especially because task-task relatedness is
ill-defined. The massive chemical state space will also influence the
development of unsupervised representation learning methods
[@tag:Gomezb2016_automatic]. Future work will establish whether it is better to
train on massive collections of diverse compounds, drug-like small molecules, or
specialized subsets.

`TODO: other papers to add such as generative models`

`TOOD: relationship to traditional docking (some networks include docking
scores), deep learning with structure (e.g. [@tag:Wallach2015_atom_net
@arxiv:1612.02751 @arxiv:1703.10603])`

`TODO: analogies to other domains where deep learning can capture the behavior
of complex physics (e.g. quantum physics example)?`

### Modeling Metabolism and Chemical Reactivity

*Add a review here of metabolism and chemical reactivity.*
