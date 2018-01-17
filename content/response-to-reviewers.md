# Response to Reviewers

Dear Dr. Holt,

We thank you and the reviewers for their thoughtful comments.
Based on their feedback, we have revised the manuscript.
We address each reviewer suggestion point-by-point below.
Major section-level changes include the addition of a section on uncertainty quantification, a revision to our drug development section to more clearly discuss chemical featurization and representation learning, and a more conscious and planned discussion of latent space representations throughout the review.
We feel that these revisions have substantially strengthened the manuscript.

Sincerely,
Casey and Tony

***

## Referee 1

> The authors summarized over 400 literature references purely by narratives.
The authors provided synopsis for each important reference, but lacks synthesis of related work.
It would be better to synthesize related work into a table and analyze their characteristics.

TODO in [issue #683](https://github.com/greenelab/deep-review/issues/683)

> The authors discussed deep learning models such as sDA, CNN, RNN etc.
It would be better to have a figure illustrating their architectures.
This way, the reader will have a concrete visualization that will aid the understanding of the discussion points in the manuscript.

We agree that having illustrated architectures would be helpful to the reader.
We selected certain key architectures that we judged to be most fundamental to an understanding of deep learning within this domain and illustrated them.
The new Figure 1 illustrates these architectures and can be paired with Table 1 for a more full synthesis of architectures used in this area.

> The authors gave a case study of LADA to suggest that integrating multiple data sources may lead to breakthrough medical discoveries.
However, it is unclear from the authors’ description that deep why learning models possess such integrating capability.
In fact, the tensor model seems to be the widely acknowledged model that can easily integrating multiple data sources.

We agree with the reviewer that the LADA description did not illustrate the benefits of deep learning particularly well.
We've now substantially revised the introduction to this section, which included dropping the discussion of LADA from the manuscript.

> The authors mentioned “One source of training examples with rich clinical annotations is electronic health records”.
What does it mean by “rich clinical annotations”? Can the authors provide a definition and a few examples.

We agree with the reviewer that "rich clinical annotations" did not make sense in this context.
Instead, we intended to say that phenotypic information can be extracted from the EHR.
We've revised the section to say:
> One source of training examples with rich phenotypical annotations is the EHR.
> Billing information in the form of ICD codes are simple annotations but phenotypic algorithms can combine laboratory tests, medication prescriptions, and patient notes to generate more reliable phenotypes.
> Recently, Lee et al.[@tag:Lee2016_emr_oct_amd] developed an approach to distinguish individuals with age-related macular degeneration from control individuals.

TODO in [issue #686](https://github.com/greenelab/deep-review/issues/686)

> Some existing biomedical informatics systems are not cited.
For example, please provide a citation to NegBio.

TODO in [issue #687](https://github.com/greenelab/deep-review/issues/687)

## Referee 2

> There is little explanation of key deep learning concepts: layers, autoencoders, RNNs, etc.
It might be impossible to do that within the space limitations of the current review, I wonder whether a link to a dedicated website or supplementary material where the most often used deep learning concepts are explained in a way an uninitiated reader can quickly read through and understand would be a solution.
There is certainly a large readership whose interest has been peaked by countless references to deep learning even in the popular press, but who are very confused when autoencoders, LSTMs and RNNs get thrown at them without any even brief explanation what they are.
Just sending readers off to fend for themselves through internet searches or to study the excellent but still quite technical book [Goodfellow et al.](http://www.deeplearningbook.org/ "Deep Learning. Ian Goodfellow, Yoshua Bengio, Aaron Courville. 2016") is probably not the most satisfactory answer.

TODO in [issue #688](https://github.com/greenelab/deep-review/issues/688)

> There is a slight imbalance in the presentation of various application areas.
The [section on drug development](https://github.com/greenelab/deep-review/blob/v0.9-preprint/sections/05_treat.md#drug-development), for example, is quite extensive and provides a lot of technical details which might be less relevant for a reader who tries to get a general overview of deep learning in biomedical research.
An area which is little mentioned on the other hand are deep learning approaches to brain data, eg connectivity maps, and the area of learning from structured data, such as graphs.

TODO in [issue #689](https://github.com/greenelab/deep-review/issues/689)

> The main issue with machine learning solutions in a medical, particularly clinical or public health setting is the lack of proper measures of uncertainty, as it is traditionally provided either in the framework of hypothesis testing or in the increasing acceptance of posterior Bayesian inference for public health decisions.
Although this is mentioned throughout the review, this issue deserves a much more prominent place in the introduction and the discussion, since it is one of the key obstacles for the acceptance of machine learning approaches outside exploratory analyses in basic biological research.

TODO in [issue #690](https://github.com/greenelab/deep-review/issues/690)

***

## Additional revisions

In addition to the revisions described above, we have continued to improve the manuscript based on community feedback.
These updates include adding new literature to existing sections...

TODO summarize other [pull requests made since the initial submission](https://github.com/greenelab/deep-review/pulls?q=created%3A>2017-05-28%20is%3Apr%20)
