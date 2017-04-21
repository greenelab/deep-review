## The impact of deep learning in treating disease and developing new treatments

*There will be some overlap with the Categorize section, and we may have to
determine which methods categorize individuals and which more directly match
patients with treatments.  The sub-section titles are merely placeholders.*

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
clinical application is unlikely until the model has been shown to be effective
. The impressive applications of deep reinforcement learning to other domains
[@tag:Silver2016_alphago] have relied on knowledge of the underlying
processes (e..g the rules of the game). Some models have been developed for
targeted medical problems [@tag:Gultepe2014_sepsis], but a
generalized engine is beyond current capabilities. Further development of the
rules underlying biological processes could unleash deep learning methods that
are currently hampered by the difficulties of counter-factual inference.

##### Efficient Clinical trials

A clinical task to deep learning which has been more successfully applied is
the assignment of patients to clinical trials. Ithapu et al
[@tag:Ithapu2015_efficient] used a randomized denoising autoenconder
 to learn a multimodal imaging marker that predicts future cognitive 
 and neural decline from positron emission tomography (PET), amyloid
florbetapir PET, and structural magnetic resonance imaging. 
By accurately predicting which cases will progress to dementia, they
 were able to efficiently assign patients to a clinical trial and reduced
  the required sample sizes by a factor of five.  Similarly, Artemov et al
[@tag:Artemov2016_clinical] applied deep learning to predict which
 clinical trials were likely to fail and which were likely to succeed. By 
 predicting the side effects and pathway activations of each drug, and 
 then translating these activations to a success proability, their deep 
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

### Effects of drugs on transcriptomic responses

*We discussed a few papers that operate on Library of Network-Based Cellular
Signatures (LINCS) gene expression data.  We could briefly introduce the
goals of that resource and comment on the deep learning applications.  In the
Issues, we had reservations about whether the improvements in expression
prediction are good enough to make a practical difference in the domain and
feature selection and construction.*

### Ligand-Based Prediction of Bioactivity

**TODO: expand outline**

- Short introduction to problem, related reviews, use vHTS definition from
[@tag:Swamidass2009_irv] (vHTS doesn't fit neatly into classic classification,
regression, or ranking)
- Introduce ligand-based approaches, hype and excitement surrounding
performance of a "high-parameter" network on the Merck Kaggle challenge,
cover other neural networks trained on fingerprints or descriptors as features
that followed, Tox21 Data Challenge
- Multitask networks related to the above point
- Realistic view of where things stand today, high-parameter networks struggle
with overfitting, cross validation needs to be done carefully because of temporal
structure [@tag:Kearnes2016_admet], low parameter networks based on chemical
similarity (IRV) work very well, especially well-suited for the domain in which
training data can be limited and contains few positive instances, may touch on
BACE example here and other discussions of training data limitations (e.g.
[@tag:AltaeTran2016_one_shot])
- "Creative experimentation" phase of the field, new ideas for representation
learning and novel approaches including graph convolutions, autoencoders,
one shot learning, and generative models
- These "creative" approaches are definitely interesting but aren't necessarily
outperforming existing methods, improvements on the software and
reusability side could be important to help establish more rigorous
benchmarking, DeepChem as example of this
- Future outlook, what would need to happen for the "creative" approaches
to overtake the current state of the art, can representation learning be
improved by incorporating more information about chemical properties or
even more "tasks" during training, how much will future growth depend on
data versus algorithms
- Future outlook part 2, how the above approaches relate to traditional
methods like docking (note neural networks that include docking scores as
features), deep learning efforts in this direction that use structure (e.g.
[@tag:Wallach2015_atom_net @tag:Ragoza_protein]), "zero-shot learning",
analogies to other domains where deep learning can capture the behavior
of complex physics (e.g. quantum physics example), maybe briefly mention
other compound-protein interaction-based networks although that doesn't seem
to fit here and is somewhat out of scope
- Future output part 3 (most speculative), what would successful generative
networks mean for the HTS field?

### Modeling Metabolism and Chemical Reactivity

*Add a review here of metabolism and chemical reactivity.*
