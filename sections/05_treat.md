## The impact of deep learning in treating disease and developing new treatments

*There will be some overlap with the Categorize section, and we may have to
determine which methods categorize individuals and which more directly match
patients with treatments.  The sub-section titles are merely placeholders.*

### Categorizing patients for clinical decision making

*How can deep learning match patients with clinical trails, therapies, or
other interventions?  As an example, [@doi:10.1016/j.jalz.2015.01.010]
predicts individuals who are most likely to decline during a clinical trial
and benefit from the treatment.*

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
