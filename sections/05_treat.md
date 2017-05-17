## The impact of deep learning in treating disease and developing new treatments

Given the ever-present need to make better interventions faster at the point of
care -- incorporating the complex calculus of a patients symptoms, diagnostics
and life history -- there is a long history of attempts to apply deep learning
to patient treatment. Success in this area would also be very useful for
directions like personalized healthcare or precision medicine
[@doi:10.1056/NEJMp1006304 @doi:10.1155/2013/769639]. Earlier, we have written
of the possibilities for patient categorization. Here, we examine the potential
for better treatment, which broadly, may divided into methods for improved
choices of interventions for patients and those for development of new
interventions.

### Categorizing patients for clinical decision making

As long ago as 1996, Tu [@tag:Tu1996_anns] compared the effectiveness of
artificial neural networks and logistic regression, questioning whether deep
learning would replace traditional statistical methods for predicting medical
outcomes such as myocardial infarction [@tag:Baxt1991_myocardial] or mortality
[@tag:Wasson1985_clinical]. He posited that while neural networks have several
advantages in representational power, the difficulties in interpretation may
limit clinical applications. Similarly, in 2006 Lisboa and Taktak
[@tag:Lisboa2006_review] examined the use of artificial neural networks in
medical journals, concluding that they improved healthcare relative to
traditional screening methods in 21 of 27 studies.

`TODO: could really use some references for following paragraph`

While further progress has been made in using deep learning for clinical
decision making, it is hindered by a challenge common to many deep learning
applications: it is much easier to predict an outcome than to suggest an action
to change the outcome. Several attempts at recasting the clinical decision
making problem into a prediction problem (i.e., prediction of which treatment
will most improve the patient's health) have accurately predicted prescription
habits, but technical and medical challenges remain for clinical adoption
(similar to those for categorization). In particular, remaining challenges
include actionable interpretability of deep learning models, fitting deep models
to limited and heterogeneous data, and integrating complex predictive models
into a dynamic clinical environment.

A critical challenge in moving from prediction to treatment recommendations is
the necessity to establish a causal relationship for a recommendation. Causal
inference is often framed in terms of counterfactual question
[@doi:10.1037/h0037350]. Johansson et al. [@arxiv:1605.03661] use deep neural
networks to create representation models for covariates that capture nonlinear
effects and show significant performance improvements over existing models. In a
less formal approach, Kale et al. [@pmid:26958203] first create a deep neural
network to model clinical time series and then analyze the relationship of the
hidden features to the output using a causal approach.

#### Applications

##### Trajectory prediction for treatment

A common application for deep learning techniques in this domain is to leverage
the temporal structure of healthcare records. As previously discussed, many
studies [@tag:Lipton2016_missing @tag:Che2016_rnn @tag:Huddar2016_predicting
@tag:Lipton2015_lstm] have used deep recurrent networks to categorize patients
but most stop short of suggesting clinical decisions. Nemati et al.
[@tag:Nemati2016_rl] used deep reinforcement learning to optimize a heparin
dosing policy for intensive care patients. However, because the ideal dosing
policy is unknown, the model's predictions must be evaluated on counter-factual
data. This represents a common challenge when bridging the gap between research
and clinical practice: because the ground-truth is unknown, researchers struggle
to evaluate model predictions in the absence of interventional data, but
clinical application is unlikely until the model has been shown to be effective.
The impressive applications of deep reinforcement learning to other domains
[@tag:Silver2016_alphago] have relied on knowledge of the underlying processes
(e.g. the rules of the game). Some models have been developed for targeted
medical problems [@tag:Gultepe2014_sepsis], but a generalized engine is beyond
current capabilities. Further development of the rules underlying biological
processes could unleash deep learning methods that are currently hampered by the
difficulties of counter-factual inference.

##### Efficient clinical trials

A clinical task to deep learning which has been more successfully applied is the
assignment of patients to clinical trials. Ithapu et al
[@tag:Ithapu2015_efficient] used a randomized denoising autoencoder to learn a
multimodal imaging marker that predicts future cognitive and neural decline from
positron emission tomography (PET), amyloid florbetapir PET, and structural
magnetic resonance imaging. By accurately predicting which cases will progress
to dementia, they were able to efficiently assign patients to a clinical trial
and reduced the required sample sizes by a factor of five.  Similarly, Artemov
et al [@tag:Artemov2016_clinical] applied deep learning to predict which
clinical trials were likely to fail and which were likely to succeed. By
predicting the side effects and pathway activations of each drug, and then
translating these activations to a success probability, their deep
learning-based approach was able to significantly outperform a random forest
classifier trained on gene expression changes. These approaches suggest
promising directions to improve the efficiency of clinical trials and accelerate
drug development.

#### Challenges

##### Actionable interpretability

A common challenge in many applied deep learning problems is the consideration
of deep learning models as uninterpretable "black boxes". Without human-
intelligible reasoning for the model's predictions, it is difficult to trust the
model. This presents a major challenge for the risk-averse task of clinical
decision making. As described above, there has been some work to directly assign
treatment plans without interpretability; however, the removal of human experts
from the decision-making loop make the models difficult to integrate with
clinical practice. To alleviate this challenge, several studies have attempted
to create more interpretable deep models, either specifically for healthcare or
as a general procedure for deep learning.  Further work in interpreting
predictions and understanding the knowledge learned by deep neural networks seem
necessary for transformative impact in clinical practice. Interpretability in
deep learning is reviewed more extensively in the Discussion.

##### Integrating deep learning with clinical practice

As deep learning models are difficult to interpret, many current models have
been designed to replace aspects of clinical practice rather than to assist
trained clinicians. This makes it difficult to integrate deep learning with
clinical decision making. In addition, the challenges that physicians face are
largely similar to those faced by machine learning models. For a given patient,
the number of possible diseases is very large, with a long tail of rare
diseases. Furthermore, patients are highly heterogeneous and may present with
very different signs and symptoms for the same disease. Physicians are
experienced in treating patients with common diseases, but rare diseases are
extremely challenging. Unfortunately, machine learning methods also struggle for
rare diseases. Directly applying current deep learning models to diagnose
patients with rare diseases would require prohibitively large datasets to
provide sufficient training data to capture the rare instances. Focused effort
in reducing the data requirements of deep learning by integrating pre-existing
knowledge or compiling large datasets of patient records may unlock the power of
deep learning for clinical practice.

### Drug repositioning

Drug repositioning (or repurposing) is an attractive option for delivering new
drugs to the market because of the high costs and failure rates associated with
more traditional drug discovery approaches [@doi:10.1016/j.jhealeco.2016.01.012
@doi:10.1038/nrd4609]. A decade ago, the concept of the Connectivity Map
[@doi:10.1126/science.1132939] had a sizeable impact on the field: reverse
matching disease gene expression signatures with a large set of reference
compound profiles allowed to formulate repurposing hypotheses at scale using a
simple non-parametric test. Since then, several advanced computational methods
have been applied to formulate and validate drug repositioning hypotheses
[@doi:10.1093/bib/bbv020 @doi:10.1093/bib/bbw112 @doi:10.1093/bib/bbw110]. Using
supervised learning and collaborative filtering to tackle this type of problems
is proving successful in different scenarios, especially when coupling disease
or compound omic data with topological information from protein-protein or
protein-compound interaction networks [@doi:10.1186/1758-2946-5-30
@doi:10.1021/ci500340n @doi:10.1186/s12859-015-0845-0].

For example, Menden et al. [@doi:10.1371/journal.pone.0061318] used a shallow
neural network to predict sensitivity of cancer cell lines to drug treatment
using both cell line and drug features, opening the door to precision medicine
and drug repositioning opportunities in cancer. More recently, Aliper et al
[@doi:10.1021/acs.molpharmaceut.6b00248] used gene- and pathway-level drug
perturbation transcriptional profiles from the Library of Network-Based Cellular
Signatures (LINCS) [@doi:10.3389/fgene.2014.00342] to train a fully connected
deep neural network able to predict drug therapeutic uses and indications. By
using confusion matrices and leveraging misclassification, the authors formulate
a number of interesting hypotheses, including repurposing cardiovascular drugs
such as otenzepad and pinacidil for neurological disorders.

Drug repositioning can also be approached by attempting to predict novel
drug-target interactions and then repurposing the drug for the associated
indication [@doi:10.1371/journal.pcbi.1005219
@doi:10.1371/journal.pcbi.1005135]. Wang et al. [@doi:10.1109/BIBM.2014.6999129]
devised a pairwise input neural network with two hidden layers that takes two
inputs, a drug and a target binding site, and predicts whether they interact.
Wang et al [@doi:10.1093/bioinformatics/btt234] trained individual RBMs for each
target in a drug-target interaction network and used these models to predict
novel interactions pointing to new indications for existing drugs. Wen et al.
[@doi:10.1021/acs.jproteome.6b00618] extended this concept to deep learning by
creating a DBN of stacked RBMs called DeepDTIs, which is able to predict
interactions on the basis of chemical structure and protein sequence features.

Drug repositioning appears to be an obvious candidate for the development of
deep learning applications both because of the large amount of high-dimensional
data available and the complexity of the question being asked. However, what is
perhaps the most promising piece of work in this space
[@doi:10.1021/acs.molpharmaceut.6b00248] is more a proof of concept than a
real-world hypothesis-generation tool; notably, deep learning was used to
predict drug indications but not for the actual repositioning. At present, some
of the most popular state-of-the-art methods for signature-based drug
repurposing [@doi:10.1038/npjsba.2016.15] do not use predictive modelling. While
this might change in the future, we believe that a mature and production-ready
framework where deep learning is directly applied to the problem of drug
repositioning is currently missing.

### Drug development

#### Ligand-based prediction of bioactivity

In the biomedical domain, high-throughput chemical screening aims to improve
therapeutic options over a long term horizon [@tag:PerezSianes2016_screening].
The objective is to discover which small molecules (also referred to as chemical
compounds or ligands) effectively and specifically affect the activity of a
target, such as a kinase, protein-protein interaction, or broader cellular
phenotype.  This screening process can serve as one of the first steps in the
long drug discovery pipeline, where novel chemicals are pursued for their
ability to inhibit or enhance disease-relevant biological mechanisms
[@doi:10.1038/nrd1086].  Initial hits are confirmed to eliminate false positives
and proceed to the lead generation stage [@doi:10.1016/j.drudis.2006.06.016],
where they are evaluated for absorption, distribution, metabolism, excretion,
and toxicity (ADMET) and other properties.  It is desirable to advance multiple
lead series, clusters of structurally-similar active chemicals, for further
optimization by medicinal chemists to protect against unexpected failures in the
later stages of drug discovery [@doi:10.1038/nrd1086].

The appeal of machine learning in this domain is the need to improve the
efficiency of the initial high-throughput screens such that sufficient candidate
active compounds can be identified without exhaustively screening libraries of
hundreds of thousands or millions of chemicals.  Predicting chemical activity
computationally is known as virtual screening.  This task has been treated
variously as a classification, regression, or ranking problem. In reality, it
does not fit neatly into any of those categories.  An ideal algorithm will rank
a sufficient number of active compounds before the inactives, but the rankings
of actives relative to other actives and inactives are less important
[@tag:Swamidass2009_irv].  Computational modeling also has the potential to
predict ADMET traits for lead generation [@tag:Kearnes2016_admet] and how drugs
are metabolized [@doi:10.1021/ci400518g].

Here we primarily focus on ligand-based approaches that train on chemicals'
features without requiring prior knowledge of the target. Chemical features may
be represented as a list of molecular descriptors such as molecular weight, atom
counts, functional groups, charge representations, summaries of atom-atom
relationships in the molecular graph, and more sophisticated derived properties
[@doi:10.1002/9783527628766].   Alternatively, chemicals can be characterized
with the fingerprint bit vectors, textual strings, or novel learned
representations described below. Neural networks have a long history in this
domain [@tag:Baskin2015_drug_disc @doi:10.1002/minf.201501008], and the 2012
Merck Molecular Activity Challenge on Kaggle generated substantial excitement
about the potential for high-parameter deep learning approaches.  The winning
submission was an ensemble that included a multitask multilayer perceptron
network [@tag:Dahl2014_multi_qsar], and the sponsors noted drastic improvements
over a random forest (RF) baseline, remarking "we have seldom seen any method in
the past 10 years that could consistently outperform RF by such a margin"
[@tag:Ma2015_qsar_merck]. Subsequent work (reviewed in more detail by Goh et al.
[@doi:10.1002/jcc.24764]) explored the effects of jointly modeling far more
targets than the Merck challenge [@tag:Unterthiner2014_screening
@tag:Ramsundar2015_multitask_drug], with [@tag:Ramsundar2015_multitask_drug]
showing that the benefits of multi-task networks had not yet saturated even with
259 targets.  Although a deep learning approach, DeepTox
[@tag:Mayr2016_deep_tox], was also the overall winner of another competition,
the Toxicology in the 21st Century (Tox21) Data Challenge, it did not dominate
alternative methods as thoroughly as in other domains. DeepTox was the top
performer on 9 of 15 targets and highly competitive with the top performer on
the others.  However, for many targets there was little separation between the
top two or three methods.

The nuanced Tox21 performance may be more reflective of the practical challenges
encountered in ligand-based chemical screening than the extreme enthusiasm
generated by the Merck competition.  A study of 22 ADMET tasks demonstrated that
there are limitations to multi-task transfer learning that are in part a
consequence of the degree to which tasks are related [@tag:Kearnes2016_admet].
Some of the ADMET datasets showed superior performance in multi-task models with
only 22 ADMET tasks compared to multi-task models with over 500 less-similar
tasks. In addition, training datasets encountered in practical applications may
be tiny relative to what is available in public datasets and organized
competitions.  A study of BACE-1 inhibitors included only 1547 compounds
[@tag:Subramanian2016_bace1].  Machine learning models were able to train on
this limited dataset, but overfitting was a challenge and the differences
between random forests and a deep neural were negligible, especially in the
classification setting.   Overfitting is still a problem in larger chemical
screening datasets with tens or hundreds of thousands of compounds because the
number of active compounds can be very small, on the order of 0.1% of all tested
chemicals for a typical target [@doi:10.1002/wcms.1104]. This is consistent with
the strong performance of low-parameter neural networks that emphasize
compound-compound similarity, such as influence-relevance voter,
[@tag:Swamidass2009_irv @tag:Lusci2015_irv] instead of predicting compound
activity directly from chemical features.

Much of the recent excitement in this domain has come from what could be
considered a creative experimentation phase, in which deep learning has offered
novel possibilities for feature representation and modeling of chemical
compounds.  A molecular graph, where atoms are labeled nodes and bonds are
labeled edges, is a natural way to represent a chemical structure.  Traditional
machine learning approaches relied on preprocessing the graph into a feature
vector, such as a fixed-width bit vector fingerprint
[@tag:Rogers2010_fingerprints].  The same fingerprints have been used by some
drug-target interaction methods discussed above
[@doi:10.1021/acs.jproteome.6b00618].  An overly simplistic but approximately
correct view of chemical fingerprints is that each bit represents the presence
of absence of a particular chemical substructure in the molecular graph. Modern
neural networks can operate directly on the molecular graph as input.  Duvenaud
et al. [@tag:Duvenaud2015_graph_conv] generalized standard circular fingerprints
by substituting discrete operations in the fingerprinting algorithm with
operations in a neural network, producing a real-valued feature vector instead
of a bit vector.  Other approaches offer trainable networks that can in theory
learn chemical feature representations that are optimized for a particular
prediction task.  Lusci et al. [@tag:Lusci2013_rnn] adapted recursive neural
networks for directed acyclic graphs for undirected molecular graphs by creating
an ensemble of directed graphs in which one atom is selected as the root node. A
single feature vector is obtained by summing over all feature vectors for all
directed graphs in the ensemble.  Graph convolutions on undirected molecular
graphs have eliminated the need to enumerate artificial directed graphs,
learning feature vectors for atoms that are a function of the properties of
neighboring atoms and local regions on the molecular graph
[@tag:Kearnes2016_graph_conv @tag:AltaeTran2016_one_shot].

Advances in chemical representation learning have also enabled new strategies
for learning chemical-chemical similarity functions.  Altae-Tran et al.
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
superior for predicting solubility or photovoltaic efficiency).  In the original
study, graph convolutions [@tag:Kearnes2016_graph_conv] performed comparably to
a multitask network using standard fingerprints and slightly better than the
neural fingerprints [@tag:Duvenaud2015_graph_conv] on the drug efficacy task but
were slightly worse than the influence-relevance voter method on an HIV dataset.
[@tag:Swamidass2009_irv].  Broader recent benchmarking has shown that relative
merits of these methods depends on the dataset and cross validation strategy
[@tag:Wu2017_molecule_net], though we caution against over-interpreting AUC
ROC-based results, a popular metric in this domain despite the active/inactive
class imbalance (see Discussion).

We remain optimistic for the potential of deep learning and specifically
representation learning in this domain and propose that rigorous benchmarking on
broad and diverse prediction tasks will be as important as novel neural network
architectures to advance the state of the art and convincingly demonstrate
superiority over traditional cheminformatics techniques. Fortunately, there has
recently been much progress in this direction. The DeepChem software
[@tag:AltaeTran2016_one_shot @tag:DeepChem] and MoleculeNet benchmarking suite
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
implications for representation learning.  The typical approach to improve deep
learning models by expanding the dataset size may not be applicable if only
"related" tasks are beneficial, especially because task-task relatedness is
ill-defined. The massive chemical state space will also influence the
development of unsupervised representation learning methods
[@tag:Gomezb2016_automatic]. Future work will establish whether it is better to
train on massive collections of diverse compounds, drug-like small molecules, or
specialized subsets.

#### Structure-based prediction of bioactivity

When protein structure is available, virtual screening has traditionally relied
on docking programs to predict how a compound best fits in the target's binding
site and score the predicted ligand-target complex
[@doi:10.1208/s12248-012-9322-0].  Recently, deep learning approaches have been
developed to model protein structure, which is expected to improve upon the
simpler drug-target interaction algorithms described above that represent
proteins with feature vectors derived from amino acid sequences
[@doi:10.1109/BIBM.2014.6999129 @doi:10.1021/acs.jproteome.6b00618].

Structure-based deep learning methods differ in whether they use
experimentally-derived or predicted ligand-target complexes and how they
represent the 3D structure.  The Atomic Convolutional Neural Network
[@arxiv:1703.10603] takes 3D crystal structures from PDBBind
[@doi:10.1021/jm048957q] as input, ensuring it uses the correct ligand-target
complex.  Alternatively, AtomNet [@tag:Wallach2015_atom_net] samples multiple
ligand poses within the target binding site, and DeepVS
[@tag:Pereira2016_docking] and Ragoza et al. [@tag:Ragoza2016_protein] use a
docking program to generate protein-compound complexes.  If they are
sufficiently accurate, these latter approaches would have wider applicability to
a much larger set of compounds and proteins.  However, incorrect ligand poses
will be misleading during training, and the predictive performance is sensitive
to the docking quality [@tag:Pereira2016_docking].  A 3D grid can be used to
represent a protein-compound complex [@tag:Wallach2015_atom_net
@tag:Ragoza2016_protein]. Each entry in the grid tracks the types of protein and
ligand atoms in that region of the 3D space or descriptors derived from those
atoms.  Both DeepVS [@tag:Pereira2016_docking] and atomic convolutions
[@arxiv:1703.10603] offer greater flexibility in their convolutions by eschewing
the 3D grid.  Instead, they each implement techniques for executing convolutions
over atoms' neighboring atoms in the 3D space.  Gomes et al. demonstrate that
currently random forest on a 1D feature vector that describes the 3D
ligand-target structure generally outperforms neural networks on the same
feature vector, atomic convolutions, and ligand-based neural networks when
predicting the continuous-valued inhibition constant on the PDBBind refined
dataset. However, in the long term atomic convolutions may ultimately overtake
grid-based methods, as they provide greater freedom to model atom-atom
interactions and the forces that govern binding affinity.

#### *De novo* drug design

Whereas the goal of virtual screening is to find active molecules by predicting
the biochemical activity of hundreds of thousands to millions of chemicals using
existing (virtual) collections of molecules, analogous to robot based
high-throughput "wet lab" screening, _de novo_ drug design aims to directly
_generate_ active compounds [@doi:10.1002/wcms.49
@doi:10.1021/acs.jmedchem.5b01849].

Drug design attempts to model the typical design-synthesize-test cycle of drug
discovery [@doi:10.1002/wcms.49]. Thus *de novo* design explores in principle
without explicit enumeration the much larger space of an estimated
10<sup>60</sup> synthesizable organic molecules with drug-like properties
[@doi:10.1002/wcms.1104]. To test or score structures, machine learning
algorithms like those discussed earlier are used. To "design" and "synthesize",
traditional *de novo* design software relied on classical optimizers such as
genetic algorithms. Unfortunately, this often leads to overfitted, "weird"
molecules, which are difficult to synthesize in the lab.  To generate molecules,
current programs have therefore settled on rule-based virtual chemical reactions
to generate molecular structures [@doi:10.1021/acs.jmedchem.5b01849].

Neural network models that learn to generate realistic, synthesizable molecules
have been proposed as an alternative to provide the large molecule sets needed
for virtual screening or even create and refine focussed molecules for *de novo*
design.  In contrast to the classical, symbolic approaches, generative models
learned from data do not depend on laboriously encoded expert knowledge. The
problem is related to the generation of syntactically and semantically correct
text [@arxiv:1308.0850].

As deep learning models that directly output (molecular) graphs remain
under-explored, generative neural networks for drug design typically represent
chemicals with the simplified molecular-input line-entry system (SMILES), a
standard way string-based representation with characters that represent atoms,
bonds, and rings [@tag:Segler2017_drug_design].  This allows treating molecules
as sequences and leveraging recent progress in recurrent neural networks.
Gómez-Bombarelli et al. designed a SMILES-to-SMILES autoencoder to learn a
continuous latent feature space for chemicals [@tag:Gomezb2016_automatic]. In
this learned continuous space it was possible to interpolate between continuous
representations of chemicals in a manner that is not possible with discrete
(e.g. bit vector or string) features or in symbolic, molecular graph space. Even
more interesting is the prospect of performing gradient-based or Bayesian
optimization of molecules within this latent space. The strategy of constructing
simple, continuous features before applying supervised learning techniques is
reminiscent of autoencoders trained on high-dimensional EHR data
[@tag:BeaulieuJones2016_ehr_encode]. A drawback of the SMILES-to-SMILES
autoencoder is that not all SMILES strings produced by the autoencoder's decoder
correspond to valid chemical structures. Recently, the Grammar Variational
Autoencoder, which takes the SMILES grammar into account and is guaranteed to
produce syntactically valid SMILES, has been proposed to alleviate this issue
[@arxiv:1703.01925].

Another approach to drug design is to train character-based RNNs on large
collections of molecules, for example, ChEMBL, [@doi:10.1093/nar/gkr777] to
first obtain a generic generative model for drug-like compounds
[@tag:Segler2017_drug_design]. These generative models successfully learn the
grammar of compound representations, with 94% [@tag:Olivecrona2017_drug_design]
or nearly 98% [@tag:Segler2017_drug_design] of generated SMILES corresponding to
valid molecular structures.  The initial RNN is then fine-tuned to generate
molecules that are likely to be active against a specific target by either
continuing training on a small set of positive examples
[@tag:Segler2017_drug_design] or adopting reinforcement learning strategies
[@tag:Olivecrona2017_drug_design @arxiv:1611.02796].  Both fine-tuning and
reinforcement learning strategies could rediscover known, held-out active
molecules. The great flexibility of neural networks, and progress in generative
models offers many opportunites for deep architectures in *de novo* design, for
example, the adaptation of Generative Adversarial Networks (GANs) for molecules.
