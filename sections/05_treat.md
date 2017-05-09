## The impact of deep learning in treating disease and developing new treatments

`TODO: write Treat intro`
`TODO: Add representative papers about Modeling Metabolism and Chemical
Reactivity`

### Categorizing patients for clinical decision making

There has been sustained interest in applying deep learning to clinical
decision making for over two decades. In 1996, Tu
[@tag:Tu1996_anns] compared the effectiveness of artificial
neural networks and logistic regression, questioning whether deep learning
would replace traditional statistical methods for predicting medical
outcomes such as myocardial infarction [@tag:Baxt1991_myocardial] or
mortality [@tag:Wasson1985_clinical]. He posited that while neural
networks have several advantages in representational power, the difficulties in
interpretation may limit clinical applications. In 2006, Lisboa and Taktak
[@tag:Lisboa2006_review] examined the use of artificial neural
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

A critical challenge in moving from prediction to treatment recommendations
is the necessity to establish a causal relationship for a recommendation.
Causal inference is often framed in terms of counterfactual question
[@doi:10.1037/h0037350]. Johansson et al [@arxiv:1605.03661] use deep neural
networks to create representation models for covariates that capture nonlinear
effects and show significant performance improvements over existing models. In
a less formal approach, Kale et al [@pmid:26958203] first create a deep neural
network to model clinical time series and then analyze the relationship of the
hidden features to the output using a causal approach.

#### Applications

##### Trajectory Prediction for Treatment

A common application for deep learning techniques in this domain is to
leverage the temporal structure of healthcare records. As previously
discussed, many studies [@tag:Lipton2016_missing
@tag:Che2016_rnn @tag:Huddar2016_predicting @tag:Lipton2015_lstm]
have used deep recurrent networks to categorize patients but most stop short
of suggesting clinical decisions. Nemati et al [@tag:Nemati2016_rl]
used deep reinforcement learning to optimize a heparin dosing policy for
intensive care patients. However, because the ideal dosing policy is unknown,
the model's predictions must be evaluated on counter-factual data. This
represents a common challenge when bridging the gap between research and
clinical practice: because the ground-truth is unknown, researchers struggle
to evaluate model predictions in the absence of interventional data, but
clinical application is unlikely until the model has been shown to be effective.
The impressive applications of deep reinforcement learning to other domains
[@tag:Silver2016_alphago] have relied on knowledge of the underlying
processes (e.g. the rules of the game). Some models have been developed for
targeted medical problems [@tag:Gultepe2014_sepsis], but a
generalized engine is beyond current capabilities. Further development of the
rules underlying biological processes could unleash deep learning methods that
are currently hampered by the difficulties of counter-factual inference.

##### Efficient Clinical trials

A clinical task to deep learning which has been more successfully applied is
the assignment of patients to clinical trials. Ithapu et al
[@tag:Ithapu2015_efficient] used a randomized denoising autoencoder
to learn a multimodal imaging marker that predicts future cognitive
and neural decline from positron emission tomography (PET), amyloid
florbetapir PET, and structural magnetic resonance imaging.
By accurately predicting which cases will progress to dementia, they
were able to efficiently assign patients to a clinical trial and reduced
the required sample sizes by a factor of five.  Similarly, Artemov et al
[@tag:Artemov2016_clinical] applied deep learning to predict which
clinical trials were likely to fail and which were likely to succeed. By
predicting the side effects and pathway activations of each drug, and
then translating these activations to a success probability, their deep
learning-based approach was able to significantly outperform a random
forest classifier trained on gene expression changes. These approaches
suggest promising directions to improve the efficiency of clinical trials
and accelerate drug development.

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
for healthcare or as a general procedure for deep learning.  Further work in
interpreting predictions and understanding the knowledge learned by deep neural
networks seem necessary for transformative impact in clinical practice.
Interpretability in deep learning is reviewed more extensively in the
Discussion.

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

### Drug repositioning

Drug repositioning (or repurposing) is an attractive option for delivering new
drugs to the market because of the high costs and failure rates associated with
more traditional drug discovery approaches [@doi:10.1016/j.jhealeco.2016.01.012
@doi:10.1038/nrd4609]. A decade ago, the concept of the Connectivity Map
[@doi:10.1126/science.1132939] had a sizeable impact on the field: reverse
matching disease gene expression signatures with a large set of reference
compound profiles allowed to formulate repurposing hypothesis at scale
using a simple non-parametric test. Since then, several advanced computational
methods have been applied to formulate and validate drug repositioning
hypotheses [@doi:10.1093/bib/bbv020 @doi:10.1093/bib/bbw112
@doi:10.1093/bib/bbw110]. Using supervised learning and collaborative filtering
to tackle this type of problems is proving successful in different scenarios,
especially when coupling disease or compound omic data  with topological
information from protein-protein or protein-compound interaction networks
[@doi:10.1186/1758-2946-5-30 @doi:10.1021/ci500340n
@doi:10.1186/s12859-015-0845-0].

Menden et al [@doi:10.1371/journal.pone.0061318] used a shallow neural network
to predict sensitivity of cancer cell lines to drug treatment using both cell
line and drug features, opening the door to precision medicine and drug
repositioning opportunities in cancer. More recently, Aliper et al
[@doi:10.1021/acs.molpharmaceut.6b00248] used gene- and pathway-level drug
perturbation transcriptional profiles from the Library of Network-Based Cellular
Signatures (LINCS) [@doi:10.3389/fgene.2014.00342] to train a fully connected
deep neural network able to predict drug therapeutic uses and indications. By
using confusion matrices and leveraging misclassification, the authors formulate
a number of interesting hypotheses, including repurposing cardiovascular drugs
such as otenzepad and pinacidil for neurological disorders.

Drug repositioning can also be approached by attempting to predict novel
drug-target interactions and then repurposing the drug for the associated
indication [@doi:10.1371/journal.pcbi.1005219 @doi:10.1371/journal.pcbi.1005135].
Wang et al [@doi:10.1109/BIBM.2014.6999129] devised a pairwise input neural
network with two hidden layers that takes two inputs, a drug and a target
binding site, and predicts whether they interact. Wang et al
[@doi:10.1093/bioinformatics/btt234] trained individual RBMs for each target in
a drug-target interaction network and used these models to predict novel
interactions pointing to new indications for existing drugs. Wen et al.
[@doi:10.1021/acs.jproteome.6b00618] extended this concept to deep learning by
creating a DBN of stacked RBMs called DeepDTIs, which is able to predict
interactions on the basis of chemical structure and protein sequence features.

Drug repositioning appears to be an obvious candidate for the development of
deep learning applications both because of the large amount of high-dimensional
data available and because of the complexity of the question being asked.
However, what is perhaps the most promising piece of work in this space
[@doi:10.1021/acs.molpharmaceut.6b00248] is more a proof of concept than a
real-world hypothesis-generation tool; notably, deep learning was used to
predict drug indications but not for the actual repositioning. At present, some
of the most popular state-of-the-art methods for signature-based drug
repurposing [@doi:10.1038/npjsba.2016.15] do not use predictive modelling. While
this might change in the future, we believe that a mature and production-ready
framework where deep learning is directly applied to the problem of drug
repositioning is currently missing.

### Ligand-Based Prediction of Bioactivity

In the biomedical domain, high-throughput chemical screening aims to improve
therapeutic options over a long term horizon [@tag:PerezSianes2016_screening]
`TODO: add another general screening reference`.  The objective is to discover
which small molecules (also referred to as chemical compounds or ligands)
effectively and specifically affect the activity of a target, such as a kinase,
protein-protein interaction, or broader cellular phenotype.  `TODO: clarify
desired outputs, what will be done with the top-ranked hits, one vs multiple
hits, abandoning lead compounds` This screening process can serve as the first
step in the long drug discovery pipeline, where novel chemicals are pursued for
their ability to inhibit or enhance disease-relevant biological mechanisms.  The
appeal of machine learning in this domain is the need to improve the efficiency
of the initial high-throughput screens such that sufficient candidate active
compounds can be identified without exhaustively screening libraries of hundreds
of thousands or millions of chemicals.  `TODO: is the sufficient number target
dependent?` This task has been treated as a classification, regression, and
ranking problem. In reality, it does not fit neatly into any of those
categories.  An ideal algorithm will rank a sufficient number of active
compounds before the inactives, but the rankings of actives relative to other
actives and inactives are less important
[@tag:Swamidass2009_irv]. `TODO: can improve this first attempt at an intro by
reviewing more existing literature on the topic` `TODO: check which other
existing reviews should be referenced`

We primarily focus on ligand-based approaches that train on chemicals' features
without requiring knowledge of the target, as opposed to alternative strategies
that use target features such as the protein structure `TODO: add examples`.
Chemical features may be represented as a list of molecular descriptors such as
molecular weight, atom counts, charge representations, summaries of atom-atom
relationships in the molecular graph, and more sophisticated derived properties
[@doi:10.1002/9783527628766].   Alternatively, chemicals can be characterized
with the fingerprint bit vectors, textual strings, or novel learned
representations described below. Neural networks have a long history in this
domain [@tag:Baskin2015_drug_disc] `TODO: can add additional references besides
this review`, and the 2012 Merck Molecular Activity Challenge on Kaggle
generated substantial excitement about the potential for high-parameter deep
learning approaches.  The winning submission was an ensemble that included a
multitask multilayer perceptron network [@tag:Dahl2014_multi_qsar], and the
Merck sponsors noted drastic improvements over a random forest (RF) baseline,
remarking "we have seldom seen any method in the past 10 years that could
consistently outperform RF by such a margin" [@tag:Ma2015_qsar_merck].
Subsequent work explored the effects of jointly modeling far more targets than
the Merck challenge [@tag:Unterthiner2014_screening
@tag:Ramsundar2015_multitask_drug], with [@tag:Ramsundar2015_multitask_drug]
showing that the benefits of multitask networks had not yet saturated even with
259 targets.  Although a deep learning approach, DeepTox
[@tag:Mayr2016_deep_tox], was also the overall winner of another competition,
the Toxicology in the 21st Century (Tox21) Data Challenge, it did not dominate
alternative methods as thoroughly as in other domains.  DeepTox was the top
performer on 9 of 15 targets and highly competitive with the top performer on
the others.  However, for many targets there was little separation between the
top two or three methods.  A reliance on AUC ROC `TODO: define here?` for the
evaluation (see Discussion) further hinders the ability to declare Tox21 as an
outright success for deep learning.

In retrospect, the nuanced Tox21 performance may be more reflective of the
practical challenges encountered in ligand-based chemical screening than the
extreme enthusiasm generated by the Merck competition.  A study of 22 absorption
distribution, metabolism, excretion, and toxicity (ADMET) tasks demonstrated
that there are limitations to multitask transfer learning that are in part a
consequence of the degree to which tasks are related [@tag:Kearnes2016_admet].
Some of the ADMET datasets showed far superior performance in multitask models
of only the 22 ADMET tasks relative to more expansive multitask networks that
included over 500 less-similar tasks.  `TODO: also has a good discussion of
information leakage in cross validation, include that in the Discussion section`
In addition, training datasets encountered in practical applications may be tiny
relative to what is available in public datasets and organized competitions.  A
study of BACE-1 inhibitors included only 1547 compounds
[@tag:Subramanian2016_bace1].  Machine learning models were able to train on
this limited dataset, but overfitting was a challenge and the differences
between random forests and a deep neural were negligible, especially in the
classification setting.  Overfitting is still a problem in larger chemical
screening datasets with tens or hundreds of thousands of compounds because the
number of active compounds can be very small, on the order of 0.1% or 1% of all
tested chemicals for a typical target  `TODO: verify those estimates`. This is
consistent with the strong performance of low-parameter neural networks that
emphasize compound-compound similarity, such as influence-relevance voter,
[@tag:Swamidass2009_irv  @tag:Lusci2015_irv] instead of predicting compound
activity directly from chemical features. `TODO: include recent DeepChem IRV
benchmarks?`

Much of the recent excitement in this domain has come from what could be
considered a creative experimentation phase, in which deep learning has offered
novel possibilities for feature representation and modeling of chemical
compounds.  A molecular graph, where atoms are nodes and bonds are edges, is a
natural way to represent a chemical structure.  Traditional machine learning
approaches relied on preprocessing the graph into a feature vector, such as a
fixed-width bit vector fingerprint [@tag:Rogers2010_fingerprints].  An overly
simplistic but approximately correct view of these fingerprints is that each bit
represents the presence of absence of a particular chemical substructure in the
molecular graph. Modern neural networks can operate directly on the molecular
graph as input.  Duvenaud et al [@tag:Duvenaud2015_graph_conv] generalized
standard circular fingerprints by substituting discrete operations in the
fingerprinting algorithm with operations in a neural network, producing a
real-valued feature vector instead of a bit vector.  Other approaches offer
trainable networks that can in theory learn chemical feature representations
that are optimized for a particular prediction task.   Lusci et al adapted
recursive neural networks for directed acyclic graphs for undirected molecular
graphs by creating an ensemble of directed graphs in which one atom is selected
as the root node [@tag:Lusci2013_rnn].  A single feature vector is obtained by
summing over all feature vectors for all directed graphs in the ensemble.  Graph
convolutions on undirected molecular graphs have eliminated the need to
enumerate artificial directed graphs, learning feature vectors for atoms that
are a function of the properties of neighboring atoms and local regions on the
molecular graph [@tag:Kearnes2016_graph_conv @tag:AltaeTran2016_one_shot].

Advances in chemical representation learning have not been limited to
graph-based neural networks.  The simplified molecular-input line-entry system
(SMILES) is a standard way to transform a chemical into string-based
representation.  A SMILES-to-SMILES autoencoder learns a continuous latent
feature space for chemicals [@tag:Gomezb2016_automatic]. `TODO: connect to
related EHR paper` `TODO: autoencoder doesn't fit cleanly with supervised
methods, revisit organization after adding GANs` In this learned continuous
space is it possible to train some types of supervised learning algorithms or
interpolate between continuous representations of chemicals in a manner that is
not possible with discrete (e.g. bit vector or string) features. A drawback is
that not all SMILES strings produced by the autoencoder's decoder correspond to
valid chemical structures. `TODO: could mention GANs here` Altae-Tran et al
developed a one-shot learning network [@tag:AltaeTran2016_one_shot] to address
the reality that most practical chemical screening studies are unable to provide
the thousands or millions of training compounds that are needed to train larger
multitask networks.  Using graph convolutions to featurize chemicals, the
network learns an embedding from compounds into a continuous feature space such
that compounds with similar activities in a set of training tasks have similar
embeddings.  The approach is evaluated in an extremely challenging setting where
the embedding is learned from a subset of prediction tasks (e.g. activity assays
for individual proteins) and only one to ten labeled examples are provided as
training data on a new task.  On Tox21 targets, even when trained with _one_
task-specific active compound and _one_ inactive compound, the model is able to
generalize reasonably well because it has learned an informative embedding
function from the related tasks. Random forests, which cannot take advantage of
the related training tasks, trained in the same setting are only slightly better
than a random classifier.  Despite the success on Tox21, performance on MUV
datasets, which contains assays designed to be challenging for chemical
informatics algorithms, is considerably worse.  The authors also demonstrate the
limitations of transfer learning as embeddings learned from the Tox21 assays
have little utility for a drug adverse reaction dataset.

These novel, learned chemical feature representations may prove to be essential
for accurately predicting why some compounds with similar structures yield
similar target effects and others produce drastically different results.
Currently, these methods are enticing but do not necessarily outperform classic
approaches by a large margin.  The neural fingerprints
[@tag:Duvenaud2015_graph_conv] were narrowly beaten by regression using
traditional circular fingerprints on a drug efficacy prediction task (but were
superior for predicting solubility or photovoltaic efficiency).  Graph
convolutions [@tag:Kearnes2016_graph_conv] performed comparably to a multitask
network using standard fingerprints and slightly better than the neural
fingerprints [@tag:Duvenaud2015_graph_conv] on the drug efficacy task but were
slightly worse than the influence-relevance voter method on an HIV dataset.
[@tag:Swamidass2009_irv].  `TODO: there are also problems with some papers using
ROC primarily for benchmarking, which skews results and makes it hard to assess
absolute performance.  Add to the Discussion section.`

We remain optimistic for the potential of deep learning and specifically
representation learning in this domain and propose that rigorous benchmarking on
broad and diverse prediction tasks will be as important as novel neural network
architectures and expanded public datasets to advance the state of the art and
convincingly demonstrate superiority over traditional cheminformatics
techniques. Fortunately, there has recently been significant progress in this
direction. The DeepChem software [@tag:AltaeTran2016_one_shot
@tag:DeepChem] and MoleculeNet benchmarking suite
[@tag:Wu2017_molecule_net] built upon it contain chemical bioactivity and
toxicity prediction datasets, multiple compound featurization approaches
including graph convolutions, and various machine learning algorithms ranging
from standard baselines like logistic regression and random forests to recent
neural network architectures.  Independent research groups have already
contributed additional datasets and prediction algorithms to DeepChem, and
adoption of common benchmarking evaluation metrics, datasets, and baseline
algorithms has the potential to establish the practical utility of deep learning
in chemical bioactivity prediction and lower the barrier to entry for machine
learning researchers without biochemistry expertise.

One open question in ligand-based screening pertains to the benefits and
limitations of transfer learning.  Multitask neural networks have shown the
advantages of jointly modeling many targets [@tag:Unterthiner2014_screening
@tag:Ramsundar2015_multitask_drug].  Other studies have shown the limitations of
transfer learning when the prediction tasks are insufficiently related
[@tag:Kearnes2016_admet @tag:AltaeTran2016_one_shot].  This has important
implications for representation learning.  The typical approach to improve
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

`TODO: link to drug repurposing section above,  DeepDTIs uses ECFPs as
features for its 1412 compounds and protein sequence composition (PSCs)
features for its targets (1520).`
