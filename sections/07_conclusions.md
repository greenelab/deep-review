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
[@arxiv:1610.05256 @arxiv:1703.02136] `TODO: need better source for this error
trajectory`. The phenomenal improvements on benchmark datasets are undeniable,
but halving the error rate on these benchmarks did not fundamentally transform
the domain.  Widespread adoption of conversational speech technologies will
require not only improvements over baseline methods but truly solving the
problem, in this case exceeding human-level performance, as well as convincing
users to embrace the technology [@tag:Speech_recognition].  We see parallels to
the healthcare domain, where achieving the full potential of deep learning will
require outstanding predictive performance as well as acceptance and adoption by
biologists and clinicians.

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
addressed.

Conversely, the most challenging tasks may be those in which predictions are
used directly for downstream modeling or decision-making, especially in the
clinic.  As an example, errors in a predicted protein contact map could be
amplified if that contact map is used directly for 3D structure prediction.  In
addition, the stochasticity and complexity of biological systems implies that
for some problems, for instance, predicting gene regulation in disease, perfect
accuracy will be unattainable.

We are witnessing deep learning models achieving human-level performance across
a number of biomedical domains, and yet we do not believe that biologists and
clinicians will be out of a job anytime soon. While deep learning and other
advanced algorithms will soon be (or already are) better than scientists at
specific tasks, in many cases they would still be unable to fully grasp the
bigger picture. Deep neural networks are also prone to mistakes that humans are
much more unlikely to make, such as incorrectly classifying negative images
[@arXiv:1703.06857], an important reminder that these algorithms do not really
understand or "recognise the semantic of the object", they merely "memorize the
inputs". Until true and reliable artificial intelligence becomes standard
in the laboratory and in the clinic, the human factor still has a critical role
to play. In some cases, cooperation between human experts and deep learning
algorithms can achieve better performance than either of them individually
[@tag:Wang2016_breast_cancer]. Particularly for sample and patient
classification tasks, we expect deep learning methods to complement and assist
biomedical researchers rather than compete with or even replace them.

Even if deep learning in biology and healthcare is not yet transformative today,
we are extremely optimistic about its future.  Given how rapidly deep learning
is evolving, its full potential in biomedicine has not been explored.  We have
highlighted numerous challenges beyond improving training and predictive
accuracy, such as preserving patient privacy and interpreting models.  Ongoing
research has begun to address these problems and shown they are not
insurmountable.  Deep learning offers the flexibility to model data in its most
natural form, for example, longer DNA sequences instead of k-mers for
transcription factor binding prediction and molecular graphs instead of
pre-computed bit vectors for drug discovery. These flexible input feature
representations have spurred creative modeling approaches that would be
infeasible with other machine learning techniques. Unsupervised methods are
currently less developed than their supervised counterparts, but they may have
the most potential because of how expensive and time-consuming it is to label
the large amounts of unlabelled data existing in the field of biomedicine. When
deep learning algorithms can summarize very large collections of input data into
interpretable models that spur scientists to ask questions that they didn't know
how to ask, it will be clear that deep learning has transformed biology and
medicine.

### Author contributions

`TODO: not sure if it should go here, but somewhere we should talk about how we
wrote this thing, since it is still somewhat unconventional to have a review
written in this manner.` We recognized that writing a review on a rapidly
developing area in a manner that allowed us to provide a forward-looking
perspective on diverse approaches and biological problems would require
expertise from across computational biology and medicine. We created an open
repository on the GitHub version control system and engaged with numerous
authors from papers within and outside of the area. Paper review was conducted
in the open by `#` individuals, and the manuscript was drafted in a series of
commits from `#` authors. Individuals who met the ICJME standards of authorship
are included as authors. These were individuals who contributed to the review of
the literature; drafted the manuscript or provided substantial critical
revisions; approved the final manuscript draft; and agreed to be accountable in
all aspects of the work. Individuals who did not contribute in one or more of
these ways, but who did participate, are acknowledged at the end of the
manuscript.

`TODO: update after finalizing discussion in #369`
