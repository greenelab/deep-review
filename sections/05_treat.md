## The impact of deep learning in treating disease and developing new treatments

*There will be some overlap with the Categorize section, and we may have to
determine which methods categorize individuals and which more directly match
patients with treatments.  The sub-section titles are merely placeholders.*


### Categorizing patients for clinical decision making

*How can deep learning match patients with clinical trails, therapies, or
other interventions?  As an example, [@doi:10.1016/j.jalz.2015.01.010]
predicts individuals who are most likely to decline during a clinical trial
and benefit from the treatment.*

There has been sustained interest in applying deep learning to clinical decision making for over two decades. In 1996, Tu (http://www.sciencedirect.com/science/article/pii/S0895435696000029) compared the effectiveness of both artificial neural networks and logistic regression, questioning whether deep learning would replace traditional statistical methods for predicting medical outcomes. He posited that while neural networks have several advantages in representational power, the difficulties in interpretation may limit clinical applications. In 2007, Lisboa and Taktak (http://www.sciencedirect.com/science/article/pii/S0893608005002844) examined the use of artificial neural networks in medical journals, concluding that neural networks provided an increase in benefit to healthcare provision in 21 of 27 studies.

While significant progress has been made in developing deep learning methods for diagnosis, it is not clear that these methods have yet transformed clinical decision making. The difficulty in applying deep learning to clinical decision making represents a challenge common to many deep learning applications: it is much easier to predict an outcome than to suggest an action to change the outcome. Several attempts at recasting the clinical decision making problem into a prediction problem (i.e. prediction of which treatment will most improve the patient's health) have accurately predicted prescription habits, but technical and medical challenges remain for clinical adoption. In particular, remaining challenges include actionable interpretability of deep learning models, fitting deep models to limited and heterogeneous data, and integrating complex predictive models into a dynamic clinical environment. 

#### Applications

##### Trajectory Prediction for Treatment
A common application for deep learning techniques in this domain is to leverage the temporal structure of healthcare records. As previously discussed, many studies (https://pdfs.semanticscholar.org/8d4b/b3790805d73d9ede46e47c0a103c42d94dd6.pdf, https://arxiv.org/abs/1606.01865, http://ieeexplore.ieee.org/abstract/document/7593335/, https://arxiv.org/abs/1510.07641) have used deep recurrent networks to categorize patients but most stop short of suggesting clinical decisions.  Nemati et al (http://ieeexplore.ieee.org/abstract/document/7591355/) used deep reinforcement learning to optimize a heparin dosing policy for intensive care patients. However, because the ideal dosing policy is unknown, the model's predictions must be evaluated on counter-factual data. This represents a common challenge when bridging the gap between research and clinical practice: because the ground-truth is unknown, researchers struggle to evaluate model predictions in the absence of interventional data, but clinical application is unlikely until the model has been shown to be effective. The impressive applications of deep reinforcement learning to other domains (@doi:10.1038/nature16961) have relied on knowledge of the "rules" underlying the game. Some models have been developed for targeted medical problems (https://www.ncbi.nlm.nih.gov/pubmed/23959843), but a generalized engine is beyond current capabilities. Further development of the rules underlying biological processes could unleash deep learning methods that are currently hampered by the difficulties of counter-factual inference.

##### Efficient Clinical trials
A clinical task which has experienced more success is the assignment of patients to clinical trials. Ithapu et al (https://github.com/greenelab/deep-review/issues/98) used a randomized denoising autoenconder to learn a multimodal imaging marker that predicts future cognitive and neural decline from fluorodeoxyglucose positron emission tomography, amyloid florbetapir PET, and structural magnetic resonance imaging. By accurately predicting which cases will progress to dementia, they were able to efficiently assign patients to a clinical trial and reduced the required sample sizes by a factor of five.  Similarly, Artemov et al (http://biorxiv.org/content/early/2016/12/20/095653) applied deep learning to predict which clinical trials were likely to fail and which were likely to succeed. By predicting the side effects and pathway activations of each drug, and then translating these activations to a success proability, their deep learning-based approach was able to significantly outperform a random forest classifier trained on gene expression changes. These approaches suggest promising directions to improve the efficiency of clinical trials and accelerate drug development.

#### Challenges
##### Actionable Interpretability
A common challenge in many applied deep learning problems is the consideration of deep learning models as uninterpretable "black boxes". Without human-intelligible reasoning for the model's predictions, it is difficult to trust the model. This presents a major challenge for the risk-averse task of clinical decision making. As described above, there has been some work to directly assign treatment plans without interpretability; however, the removal of human experts from the decision-making loop make the models difficult to integrate with clinical practice. To alleviate this challenge, several studies have attempted to create more interpretable deep models, either specifically for healthcare or as a general procedure for deep learning.

For domain-specific models, studies have primarily focused on integrating attention mechanisms with the neural networks. Attention mechanisms dynamically weight the importance the neural network gives to each feature. By inspecting the attention weights for a particular sample, a practitioner can identify the important features for a particular prediction. Choi et al (https://github.com/greenelab/deep-review/issues/189) inverted the typical architectue of recurrent neural networks to improve interpretability. In particular, they only used recurrent connections in the attention generating procedure, leaving the hidden state directly connected to the input variables. This model was able to produce accurate diagnoses in which the contribution of previous hospital visits could be directly interpreted. Choi et al (https://arxiv.org/pdf/1611.07012.pdf) later extended this work to take into account the structure of disease ontologies and found that the concepts represented by the model were aligned with medical knowledge. Che et al (https://arxiv.org/abs/1512.03542) introduced a knowledge-distillation approach which used gradient boosted trees to learn interpretable healthcare features from trained deep models.

As this challenge of interpretability is common across many domains, there is significant interest in developing generic procedures for knowledge extraction from deep models. Ribeiro et al (https://arxiv.org/abs/1602.04938) focus on interpreting individual predictions rather than interpreting the model. By fitting simple linear models to mimic the predictions of the deep learning model in a small neighborhood of a data sample, they generated an interpretable model for each prediction. While this procedure can provide interpretable models for each sample, it is unclear whether these interpretable models are reliable. Theoretical guarantees on the curvature of the predictions of deep learning models are not known, and it is unclear whether predictions from deep learning models are robust to sample noise. Toward quantifying the uncertainty of predictions, there has been a renewed interest in confidence intervals for deep neural networks. Early work from Chryssolouris et al (http://ieeexplore.ieee.org/abstract/document/478409/) provided confidence intervals under the assumption of normally distributed error. However, Nguyen et al (http://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Nguyen_Deep_Neural_Networks_2015_CVPR_paper.html) showed that the confidence of convolutional neural networks is not reliable; they can output confidence scores over 99.99% even for samples that are purely noise. Recently, Fong and Vedaldi (https://github.com/greenelab/deep-review/issues/308) provided a framework for understanding black box algorithms by perturbing input data. Further work in interpreting predictions and understanding the knowledge learned by deep neural networks seem necessary for transformative impact in clinical practice.

##### Integrating Deep Learning with Clinical Practice
As deep learning models are difficult to interpret, many current models have been designed to replace aspects of clinical practice rather than to assist trained clinicians. This makes it difficult to integrate deep learning with clinical decision making. In addition, the challenges that physicians face are largely similar to those faced by machine learning models. For a given patient, the number of possible diseases is very large, with a long tail of rare diseases. Furthermore, patients are highly heterogeneous and may present with very different signs and symptoms for the same disease. Physicians are experienced in treating patients with common diseases, but rare diseases are extremely challenging. Unfortunately, machine learning methods also struggle for rare diseases. Because deep learning models are data-intensive, directly applying current deep learning models to diagnose patients with rare diseases would require prohibitively large datasets. Focused effort in reducing the data requirements of deep learning by integrating pre-existing knowledge or compiling large datasets of patient records may unlock the power of deep learning for clinical practice.


#### Other Ideas 
Finally, medical knowledge matches well with patient segmentation from shallow learning models. It is unclear whether deep learning will help us treat patients better until we develop more complex treatment regimens.
Shallow learning is sufficient to divide patients into treatment regimens that we understand: ER+ vs ER-, for instance

- ML in genomic medicine (http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7347331)
- ML in medicine (http://circ.ahajournals.org/content/132/20/1920.short)

Unclear what RL policy to actually optimize
- An Application of Inverse Reinforcement Learning to Medical Records of Diabetes Treatment (http://www.ke.tu-darmstadt.de/events/PBRL-13/papers/02-Asoh.pdf)

##### Data Challenges
Data scale (fat, wide)
Lack of ground-truth? (Dont know best treatment)
Missing Data
Must protect privacy
- Privacy-preserving DL (http://dl.acm.org/citation.cfm?id=2813687)


##### Diagnosis (maybe not for here)
- Diagnosis Code Assignment Using Sparsity-Based Disease Correlation Embedding (http://ieeexplore.ieee.org/abstract/document/7559717/)
- Doctor AI: Predicting Clinical Events via RNNs (https://arxiv.org/abs/1511.05942)
- Learning to Diagnose with LSTMs (https://arxiv.org/abs/1511.03677)
- Detection of age-related macular degeneration via deep learning (http://ieeexplore.ieee.org/abstract/document/7493240/)
- Deep Learning-Based Feature Representation for AD/MCI Classification (http://link.springer.com/chapter/10.1007/978-3-642-40763-5_72)
- Deep Learning in Diagnosis of Brain Disorders (http://link.springer.com/chapter/10.1007/978-94-017-7239-6_14#page-1)
- Deep 3D Convolutional Encoder Networks With Shortcuts for Multiscale Feature Integration Applied to Multiple Sclerosis Lesion Segmentation (http://ieeexplore.ieee.org/document/7404285/?arnumber=7404285&tag=1)


##### Clinical Time Series
- Penalized Q-Learning for Dynamic Treatment Regimes (http://europepmc.org/abstract/med/26257504)
- Directly Modeling Missing Data in Sequences with RNNs: Improved Classification of Clinical Time Series (https://pdfs.semanticscholar.org/8d4b/b3790805d73d9ede46e47c0a103c42d94dd6.pdf)
- Recurrent Neural Networks for Multivariate Time Series with Missing Values (https://arxiv.org/abs/1606.01865)
- Predicting Complications in Critical Care Using Heterogeneous Clinical Data (http://ieeexplore.ieee.org/abstract/document/7593335/)
- Big Healthcare Data Analytics: Challenges and Applications (https://pdfs.semanticscholar.org/c259/a279d11baa718547370df944f758c7114d16.pdf)
- Phenotyping of Clinical Time Series with LSTM Recurrent Neural Networks (https://arxiv.org/abs/1510.07641)
- Big Data and machine learning in radiation oncology: State of the art and future prospects (http://www.sciencedirect.com/science/article/pii/S0304383516303469)


##### Treatment Strategies
- Prediction of Clinical Drug Response Based on Differential Gene Expression Levels (http://link.springer.com/chapter/10.1007/978-3-319-22186-1_48)
- Optimal Individualized Treatment Strategy: Flexible Modeling with/without Imaging Covariates. (https://repository.lib.ncsu.edu/handle/1840.16/11138)
- Risk Factor Analysis Based on Deep Learning Models (http://dl.acm.org/citation.cfm?id=2975208)

##### Old Papers
- Artificial neural networks improve the accuracy of cancer survival prediction 1997 (http://onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-0142(19970215)79:4%3C857::AID-CNCR24%3E3.0.CO;2-Y/full)
- Toxicity prediction using deep learning (https://arxiv.org/abs/1503.01445)
- Deep Computational Phenotyping (https://github.com/greenelab/deep-review/issues/77)
- PhenoTree: Interactive Visual Analytics for Hierarchical Phenotyping From Large-Scale Electronic Health Records (http://ieeexplore.ieee.org/abstract/document/7577842/)
- Hierarchical feature representation and multimodal fusion with deep learning for AD/MCI diagnosis (http://www.sciencedirect.com/science/article/pii/S1053811914005540)





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
[@tag:Wallach2015_atom_net @arxiv:1612.02751]), "zero-shot learning",
analogies to other domains where deep learning can capture the behavior
of complex physics (e.g. quantum physics example), maybe briefly mention
other compound-protein interaction-based networks although that doesn't seem
to fit here and is somewhat out of scope
- Future output part 3 (most speculative), what would successful generative
networks mean for the HTS field?

### Modeling Metabolism and Chemical Reactivity

*Add a review here of metabolism and chemical reactivity.*
