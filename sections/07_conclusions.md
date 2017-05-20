## Conclusions

Deep learning-based methods now match or surpass the previous state of the art
in a diverse array of tasks in patient and disease categorization, fundamental
biological study, genomics, and treatment development.  Returning to our central
question: given this rapid progress, has deep learning transformed the study of
human disease?  Though the answer is highly dependent on the specific domain and
problem being addressed, we conclude that deep learning has not *yet* realized
its transformative potential or induced a strategic inflection point.  Despite
its dominance over competing machine learning approaches in many of the areas
reviewed here and quantitative improvements in predictive performance, deep
learning has not yet definitively "solved" those problems.

As an analogy, consider recent progress in conversational speech recognition.
Since 2009 there have been drastic performance improvements, with error rates
dropping from more than 20% to less than 6% [@tag:Speech_recognition] and
finally approaching or exceeding human performance in the past year
[@arxiv:1610.05256 @arxiv:1703.02136]. The phenomenal improvements on benchmark
datasets are undeniable, but greatly reducing the error rate on these benchmarks did not
fundamentally transform the domain.  Widespread adoption of conversational
speech technologies will require not only improvements over baseline methods but
truly solving the problem, in this case exceeding human-level performance, as
well as convincing users to embrace the technology [@tag:Speech_recognition].
We see parallels to the healthcare domain, where achieving the full potential of
deep learning will require outstanding predictive performance as well as
acceptance and adoption by biologists and clinicians.

Some of the areas we have discussed are closer to surpassing this lofty bar than
others, generally those that are more similar to the non-biomedical tasks that
are now monopolized by deep learning.  In medical imaging, diabetic retinopathy
[@doi:10.1001/jama.2016.17216], diabetic macular edema
[@doi:10.1001/jama.2016.17216], tuberculosis [@doi:10.1148/radiol.2017162326],
and skin lesion [@doi:10.1038/nature21056] classifiers are highly accurate and
comparable to clinician performance in the latter case.

In other domains, perfect accuracy will not be required because deep learning
will be used primarily to prioritize experiments and assist discovery. For
example, in chemical screening for drug discovery, a deep learning system that
successfully identifies dozens or hundreds of target-specific, active small
molecules from a massive search space would have immense practical value even if
its overall precision is modest.  In medical imaging, deep learning can point an
expert to the most challenging cases that require manual review
[@doi:10.1148/radiol.2017162326], though the risk of false negatives must be
addressed.  In protein structure prediction, errors in individual
residue-residue contacts can be tolerated when using the contacts jointly for 3D
structure modeling.  Improved contact map predictions
[@tag:Wang2016_protein_contact] have led to notable improvements in fold and 3D
structure prediction for some of the most challenging proteins, such as membrane
proteins [@arxiv:1704.07207].

Conversely, the most challenging tasks may be those in which predictions are
used directly for downstream modeling or decision-making, especially in the
clinic.  As an example, errors in sequence variant calling will be amplified if
they are used directly for GWAS. In addition, the stochasticity and complexity
of biological systems implies that for some problems, for instance, predicting
gene regulation in disease, perfect accuracy will be unattainable.

We are witnessing deep learning models achieving human-level performance across
a number of biomedical domains, and yet do not believe that biologists and
clinicians will be displaced anytime soon. While deep learning methods will
soon be (or already are) better than scientists at specific tasks, they may not
fully grasp the bigger picture. Machine learning algorithms, including deep
neural networks, are also prone to mistakes that humans are much less likely to
make, such as misclassification of adversarial examples [@arxiv:1312.6199
@arxiv:1412.6572], a reminder that these algorithms do not understand the
semantics of the objects presented. Despite progress in addressing some of these
limitations [@arxiv:1611.03814 @arxiv:1704.01155], we expect human experts will retain
their critical roles in the laboratory and clinic
for the foreseeable future. In some cases, cooperation
between human experts and deep learning algorithms can achieve better
performance than either individually [@arxiv:1606.05718]. Especially for sample
and patient classification tasks, we expect deep learning methods to complement
and assist biomedical researchers rather than compete with or even replace them.

Even if deep learning in biology and healthcare is not yet transformative today,
we are extremely optimistic about its future. Given how rapidly deep learning is
evolving, its full potential in biomedicine has not been explored.  We have
highlighted numerous challenges beyond improving training and predictive
accuracy, such as preserving patient privacy and interpreting models.  Ongoing
research has begun to address these problems and shown they are not
insurmountable.  Deep learning offers the flexibility to model data in its most
natural form, for example, longer DNA sequences instead of k-mers for
transcription factor binding prediction and molecular graphs instead of
pre-computed bit vectors for drug discovery. These flexible input feature
representations have spurred creative modeling approaches that would be
infeasible with other machine learning techniques. Unsupervised methods are
currently less-developed than their supervised counterparts, but they may have
the most potential because of how expensive and time-consuming it is to label
large amounts of biomedical data. When deep learning algorithms can summarize
very large collections of input data into interpretable models that spur
scientists to ask questions that they did not know how to ask, it will be clear
that deep learning has transformed biology and medicine.
