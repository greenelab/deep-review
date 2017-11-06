# Response to Reviewers

The Deep Review ([preprint version 1](https://www.biorxiv.org/content/early/2017/05/28/142760)) was submitted _Journal of the Royal Society Interface_.
We have now [received](https://github.com/greenelab/deep-review/issues/678) the peer reviews and are working on addressing the comments.
When submitting a pull request to revise the Deep Review in response to reviewers, please also comment on the relevant section in this document.
The comments should respond to the reviewer comments and should link to the pull requests or issues where they are addressed.

After each reviewer criticism, there is a `TODO`.
Replace the TODO with the relevant response.
Feel free to also break up paragraphs as necessary, but remember to keep the reviews formatted as blockquotes.

***

## Referee 1

> The authors summarized over 400 literature references purely by narratives. The authors provided synopsis for each important reference, but lacks synthesis of related work. It would be better to synthesize related work into a table and analyze their characteristics.

TODO in [issue #683](https://github.com/greenelab/deep-review/issues/683)

> The authors discussed deep learning models such as sDA, CNN, RNN etc. It would be better to have a figure illustrating their architectures. This way, the reader will have a concrete visualization that will aid the understanding of the discussion points in the manuscript.

TODO in [issue #684](https://github.com/greenelab/deep-review/issues/684)

> The authors gave a case study of LADA to suggest that integrating multiple data sources may lead to breakthrough medical discoveries. However, it is unclear from the authors’ description that deep why learning models possess such integrating capability. In fact, the tensor model seems to be the widely acknowledged model that can easily integrating multiple data sources.

TODO in [issue #685](https://github.com/greenelab/deep-review/issues/685)

> The authors mentioned “One source of training examples with rich clinical annotations is electronic health records”. What does it mean by “rich clinical annotations”? Can the authors provide a definition and a few examples.

TODO in [issue #686](https://github.com/greenelab/deep-review/issues/686)

> Some existing biomedical informatics systems are not cited. For example, please provide a citation to NegBio.

TODO in [issue #687](https://github.com/greenelab/deep-review/issues/687)

## Referee 2

> There is little explanation of key deep learning concepts: layers, autoencoders, RNNs, etc. It might be impossible to do that within the space limitations of the current review, I wonder whether a link to a dedicated website or supplementary material where the most often used deep learning concepts are explained in a way an uninitiated reader can quickly read through and understand would be a solution. There is certainly a large readership whose interest has been peaked by countless references to deep learning even in the popular press, but who are very confused when autoencoders, LSTMs and RNNs get thrown at them without any even brief explanation what they are. Just sending readers off to fend for themselves through internet searches or to study the excellent but still quite technical book [Goodfellow et al.](http://www.deeplearningbook.org/ "Deep Learning. Ian Goodfellow, Yoshua Bengio, Aaron Courville. 2016") is probably not the most satisfactory answer.

TODO in [issue #688](https://github.com/greenelab/deep-review/issues/688)

> There is a slight imbalance in the presentation of various application areas. The [section on drug development](https://github.com/greenelab/deep-review/blob/v0.9-preprint/sections/05_treat.md#drug-development), for example, is quite extensive and provides a lot of technical details which might be less relevant for a reader who tries to get a general overview of deep learning in biomedical research. An area which is little mentioned on the other hand are deep learning approaches to brain data, eg connectivity maps, and the area of learning from structured data, such as graphs.

TODO in [issue #689](https://github.com/greenelab/deep-review/issues/689)

> The main issue with machine learning solutions in a medical, particularly clinical or public health setting is the lack of proper measures of uncertainty, as it is traditionally provided either in the framework of hypothesis testing or in the increasing acceptance of posterior Bayesian inference for public health decisions. Although this is mentioned throughout the review, this issue deserves a much more prominent place in the introduction and the discussion, since it is one of the key obstacles for the acceptance of machine learning approaches outside exploratory analyses in basic biological research.

TODO in [issue #690](https://github.com/greenelab/deep-review/issues/690)
