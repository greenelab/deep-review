---
author-meta:
- Daniel S. Himmelstein
- Brock C. Christensen
- Joshua J. Levy
- Casey S. Greene
- Alexander J. Titus
bibliography:
- content/manual-references-2020-01-29.json
- content/manual-references.json
date-meta: '2020-08-09'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Opportunities and obstacles for deep learning in biology and medicine [update in progress]" />

  <meta name="citation_title" content="Opportunities and obstacles for deep learning in biology and medicine [update in progress]" />

  <meta property="og:title" content="Opportunities and obstacles for deep learning in biology and medicine [update in progress]" />

  <meta property="twitter:title" content="Opportunities and obstacles for deep learning in biology and medicine [update in progress]" />

  <meta name="dc.date" content="2020-08-09" />

  <meta name="citation_publication_date" content="2020-08-09" />

  <meta name="dc.language" content="en-US" />

  <meta name="citation_language" content="en-US" />

  <meta name="dc.relation.ispartof" content="Manubot" />

  <meta name="dc.publisher" content="Manubot" />

  <meta name="citation_journal_title" content="Manubot" />

  <meta name="citation_technical_report_institution" content="Manubot" />

  <meta name="citation_author" content="Daniel S. Himmelstein" />

  <meta name="citation_author_institution" content="Department of Systems Pharmacology and Translational Therapeutics, University of Pennsylvania, Philadelphia, Pennsylvania, United States of America" />

  <meta name="citation_author_orcid" content="0000-0002-3012-7446" />

  <meta name="citation_author" content="Brock C. Christensen" />

  <meta name="citation_author_institution" content="Department of Epidemiology, Geisel School of Medicine, Dartmouth College, Lebanon, NH" />

  <meta name="citation_author_orcid" content="0000-0003-3022-426X" />

  <meta name="citation_author" content="Joshua J. Levy" />

  <meta name="citation_author_institution" content="Program in Quantitative Biomedical Sciences, Geisel School of Medicine at Dartmouth, Lebanon, NH" />

  <meta name="citation_author_orcid" content="0000-0001-8050-1291" />

  <meta name="citation_author" content="Casey S. Greene" />

  <meta name="citation_author_institution" content="Department of Systems Pharmacology and Translational Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA" />

  <meta name="citation_author_institution" content="Childhood Cancer Data Lab, Alex&#39;s Lemonade Stand Foundation, Philadelphia, PA" />

  <meta name="citation_author_orcid" content="0000-0001-8713-9213" />

  <meta name="citation_author" content="Alexander J. Titus" />

  <meta name="citation_author_institution" content="Department of Epidemiology, Geisel School of Medicine, Dartmouth College, Lebanon, NH" />

  <meta name="citation_author_orcid" content="0000-0002-0145-9564" />

  <link rel="canonical" href="https://greenelab.github.io/deep-review/" />

  <meta property="og:url" content="https://greenelab.github.io/deep-review/" />

  <meta property="twitter:url" content="https://greenelab.github.io/deep-review/" />

  <meta name="citation_fulltext_html_url" content="https://greenelab.github.io/deep-review/" />

  <meta name="citation_pdf_url" content="https://greenelab.github.io/deep-review/manuscript.pdf" />

  <link rel="alternate" type="application/pdf" href="https://greenelab.github.io/deep-review/manuscript.pdf" />

  <link rel="alternate" type="text/html" href="https://greenelab.github.io/deep-review/v/1173b9b646a7a86ef64d14d1eda3bd6441c85910/" />

  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/deep-review/v/1173b9b646a7a86ef64d14d1eda3bd6441c85910/" />

  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/deep-review/v/1173b9b646a7a86ef64d14d1eda3bd6441c85910/manuscript.pdf" />

  <meta property="og:type" content="article" />

  <meta property="twitter:card" content="summary_large_image" />

  <meta property="og:image" content="https://github.com/greenelab/deep-review/raw/1173b9b646a7a86ef64d14d1eda3bd6441c85910/thumbnail.png" />

  <meta property="twitter:image" content="https://github.com/greenelab/deep-review/raw/1173b9b646a7a86ef64d14d1eda3bd6441c85910/thumbnail.png" />

  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />

  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />

  <meta name="theme-color" content="#ad1457" />

  <!-- end Manubot generated metadata -->'
keywords:
- deep learning
- review
- precision medicine
- genomics
- machine learning
- neural networks
- collaborative
- manubot
lang: en-US
manubot-clear-requests-cache: false
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
title: Opportunities and obstacles for deep learning in biology and medicine [update in progress]
...



<!-- include the Font Awesome library, per: https://fontawesome.com/start -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css">
[
[]{.fas .fa-info-circle .fa-lg} **Update Underway**<br>
A published version of this manuscript from 04 April 2018, termed version 1.0, is available at <https://doi.org/10.1098/rsif.2017.0387>.
A new effort is underway to update the manuscript to a version 2.0 that is current as of the first half of 2020.
New authors and links to new sections are available in [GitHub Issue #959](https://github.com/greenelab/deep-review/issues/959).
]{.banner .lightred}


<small><em>
This manuscript
([permalink](https://greenelab.github.io/deep-review/v/1173b9b646a7a86ef64d14d1eda3bd6441c85910/))
was automatically generated
from [greenelab/deep-review@1173b9b](https://github.com/greenelab/deep-review/tree/1173b9b646a7a86ef64d14d1eda3bd6441c85910)
on August 9, 2020.
</em></small>

## Authors

### Version 2.0 authors


  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-3012-7446)
    Daniel S. Himmelstein<sup>2.1⚄</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-3022-426X)
    Brock C. Christensen<sup>2.2⚄</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-8050-1291)
    Joshua J. Levy<sup>2.3⚄</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-8713-9213)
    Casey S. Greene<sup>2.4,2.5⚄,†</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-0145-9564)
    Alexander J. Titus<sup>2.2⚄</sup>,
[The Version 1.0 Deep Review Authors](#version-1.0-authors)

<sup>⚄</sup> --- Author order for version 2.0 is currently randomized [with each new build](https://github.com/greenelab/deep-review/pull/997).<br>
<sup>†</sup> --- To whom correspondence should be addressed: greenescientist@gmail.com (C.S.G.)

<small>


2.1. Department of Systems Pharmacology and Translational Therapeutics, University of Pennsylvania, Philadelphia, Pennsylvania, United States of America<br>
2.2. Department of Epidemiology, Geisel School of Medicine, Dartmouth College, Lebanon, NH<br>
2.3. Program in Quantitative Biomedical Sciences, Geisel School of Medicine at Dartmouth, Lebanon, NH<br>
2.4. Department of Systems Pharmacology and Translational Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA<br>
2.5. Childhood Cancer Data Lab, Alex's Lemonade Stand Foundation, Philadelphia, PA<br>

</small>

### Version 1.0 authors

  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-5577-3516)
    Travers Ching<sup>1.1,☯</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-3012-7446)
    Daniel S. Himmelstein<sup>1.2</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-6700-1468)
    Brett K. Beaulieu-Jones<sup>1.3</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-4563-3226)
    Alexandr A. Kalinin<sup>1.4</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-4992-2623)
    Brian T. Do<sup>1.5</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-0503-9348)
    Gregory P. Way<sup>1.2</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-8362-100X)
    Enrico Ferrero<sup>1.8</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-1126-1479)
    Paul-Michael Agapow<sup>1.9</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-0539-630X)
    Michael Zietz<sup>1.2</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-4517-1562)
    Michael M. Hoffman<sup>1.10,1.11,1.12</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-1871-6846)
    Wei Xie<sup>1.13</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-1763-5750)
    Gail L. Rosen<sup>1.14</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-8690-9554)
    Benjamin J. Lengerich<sup>1.15</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-1633-5780)
    Johnny Israeli<sup>1.16</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-0811-0944)
    Jack Lanchantin<sup>1.17</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-0568-298X)
    Stephen Woloszynek<sup>1.14</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-1555-8261)
    Anne E. Carpenter<sup>1.18</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-6443-4671)
    Avanti Shrikumar<sup>1.19</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-7111-4839)
    Jinbo Xu<sup>1.20</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-3877-0433)
    Evan M. Cofer<sup>1.21,1.22</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-7762-1089)
    Christopher A. Lavender<sup>1.23</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-3247-6487)
    Srinivas C. Turaga<sup>1.24</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-8655-8109)
    Amr M. Alexandari<sup>1.19</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-9998-916X)
    Zhiyong Lu<sup>1.25</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-3332-9307)
    David J. Harris<sup>1.26</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-8931-9461)
    Dave DeCaprio<sup>1.27</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-5796-7453)
    Yanjun Qi<sup>1.17</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-3084-2287)
    Anshul Kundaje<sup>1.19,1.28</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-9309-8331)
    Yifan Peng<sup>1.25</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-6681-9754)
    Laura K. Wiley<sup>1.29</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-8008-0546)
    Marwin H.S. Segler<sup>1.30</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-1400-3398)
    Simina M. Boca<sup>1.31</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-2191-0778)
    S. Joshua Swamidass<sup>1.32</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0003-1349-4030)
    Austin Huang<sup>1.33</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-5324-9833)
    Anthony Gitter<sup>1.34,1.35,†</sup>,
  [![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-8713-9213)
    Casey S. Greene<sup>1.2,†</sup>

<sup>☯</sup> --- Author order was determined with a randomized algorithm<br>
<sup>†</sup> --- To whom correspondence should be addressed: gitter@biostat.wisc.edu (A.G.) and greenescientist@gmail.com (C.S.G.)

<small>

1.1. Molecular Biosciences and Bioengineering Graduate Program, University of Hawaii at Manoa, Honolulu, HI  
1.2. Department of Systems Pharmacology and Translational Therapeutics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA  
1.3. Genomics and Computational Biology Graduate Group, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA  
1.4. Department of Computational Medicine and Bioinformatics, University of Michigan Medical School, Ann Arbor, MI  
1.5. Harvard Medical School, Boston, MA  
1.6. Program in Quantitative Biomedical Sciences, Geisel School of Medicine at Dartmouth, Lebanon, NH  
1.7. Department of Epidemiology, Geisel School of Medicine, Dartmouth College, Lebanon, NH  
1.8. Computational Biology and Stats, Target Sciences, GlaxoSmithKline, Stevenage, United Kingdom  
1.9. Data Science Institute, Imperial College London, London, United Kingdom  
1.10. Princess Margaret Cancer Centre, Toronto, ON, Canada  
1.11. Department of Medical Biophysics, University of Toronto, Toronto, ON, Canada  
1.12. Department of Computer Science, University of Toronto, Toronto, ON, Canada  
1.13. Electrical Engineering and Computer Science, Vanderbilt University, Nashville, TN  
1.14. Ecological and Evolutionary Signal-processing and Informatics Laboratory, Department of Electrical and Computer Engineering, Drexel University, Philadelphia, PA  
1.15. Computational Biology Department, School of Computer Science, Carnegie Mellon University, Pittsburgh, PA  
1.16. Biophysics Program, Stanford University, Stanford, CA  
1.17. Department of Computer Science, University of Virginia, Charlottesville, VA  
1.18. Imaging Platform, Broad Institute of Harvard and MIT, Cambridge, MA  
1.19. Department of Computer Science, Stanford University, Stanford, CA  
1.20. Toyota Technological Institute at Chicago, Chicago, IL  
1.21. Department of Computer Science, Trinity University, San Antonio, TX  
1.22. Lewis-Sigler Institute for Integrative Genomics, Princeton University, Princeton, NJ  
1.23. Integrative Bioinformatics, National Institute of Environmental Health Sciences, National Institutes of Health, Research Triangle Park, NC  
1.24. Howard Hughes Medical Institute, Janelia Research Campus, Ashburn, VA  
1.25. National Center for Biotechnology Information and National Library of Medicine, National Institutes of Health, Bethesda, MD  
1.26. Department of Wildlife Ecology and Conservation, University of Florida, Gainesville, FL  
1.27. ClosedLoop.ai, Austin, TX  
1.28. Department of Genetics, Stanford University, Stanford, CA  
1.29. Division of Biomedical Informatics and Personalized Medicine, University of Colorado School of Medicine, Aurora, CO  
1.30. Institute of Organic Chemistry, Westfälische Wilhelms-Universität Münster, Münster, Germany  
1.31. Innovation Center for Biomedical Informatics, Georgetown University Medical Center, Washington, DC  
1.32. Department of Pathology and Immunology, Washington University in Saint Louis, Saint Louis, MO  
1.33. Department of Medicine, Brown University, Providence, RI  
1.34. Department of Biostatistics and Medical Informatics, University of Wisconsin-Madison, Madison, WI  
1.35. Morgridge Institute for Research, Madison, WI  

</small>


## Abstract {.page_break_before}

Deep learning describes a class of machine learning algorithms that are capable of combining raw inputs into layers of intermediate features. These algorithms have recently shown impressive results across a variety of domains.
Biology and medicine are data-rich disciplines, but the data are complex and often ill-understood. Hence, deep learning techniques may be particularly well-suited to solve problems of these fields.
We examine applications of deep learning to a variety of biomedical problems---patient classification, fundamental biological processes, and treatment of patients---and discuss whether deep learning will be able to transform these tasks or if the biomedical sphere poses unique challenges.
Following from an extensive literature review, we find that deep learning has yet to revolutionize biomedicine or definitively resolve any of the most pressing challenges in the field, but promising advances have been made on the prior state of the art.
Even though improvements over previous baselines have been modest in general, the recent progress indicates that deep learning methods will provide valuable means for speeding up or aiding human investigation.
Though progress has been made linking a specific neural network's prediction to input features, understanding how users should interpret these models to make testable hypotheses about the system under study remains an open challenge.
Furthermore, the limited amount of labeled data for training presents problems in some domains, as do legal and privacy constraints on work with sensitive health records.
Nonetheless, we foresee deep learning enabling changes at both bench and bedside with the potential to transform several areas of biology and medicine.


## Introduction to deep learning

Biology and medicine are rapidly becoming data-intensive.
A recent comparison of genomics with social media, online videos, and other data-intensive disciplines suggests that genomics alone will equal or surpass other fields in data generation and analysis within the next decade [@doi:10.1371/journal.pbio.1002195].
The volume and complexity of these data present new opportunities, but also pose new challenges.
Automated algorithms that extract meaningful patterns could lead to actionable knowledge and change how we develop treatments, categorize patients, or study diseases, all within privacy-critical environments.

The term _deep learning_ has come to refer to a collection of new techniques that, together, have demonstrated breakthrough gains over existing best-in-class machine learning algorithms across several fields.
For example, over the past five years these methods have revolutionized image classification and speech recognition due to their flexibility and high accuracy [@doi:10.1038/nature14539].
More recently, deep learning algorithms have shown promise in fields as diverse as high-energy physics [@doi:10.1038/ncomms5308], computational chemistry [@doi:10.1002/jcc.24764], dermatology [@doi:10.1038/nature21056], and translation among written languages [@arxiv:1609.08144].
Across fields, "off-the-shelf" implementations of these algorithms have produced comparable or higher accuracy than previous best-in-class methods that required years of extensive customization, and specialized implementations are now being used at industrial scales.

Deep learning approaches grew from research on artificial neurons, which were first proposed in 1943 [@doi:10.1007/BF02478259] as a model for how the neurons in a biological brain process information.
The history of artificial neural networks---referred to as "neural networks" throughout this article---is interesting in its own right [@doi:10.1103/RevModPhys.34.135].
In neural networks, inputs are fed into the input layer, which feeds into one or more hidden layers, which eventually link to an output layer.
A layer consists of a set of nodes, sometimes called "features" or "units," which are connected via edges to the immediately earlier and the immediately deeper layers.
In some special neural network architectures, nodes can connect to themselves with a delay.
The nodes of the input layer generally consist of the variables being measured in the dataset of interest---for example, each node could represent the intensity value of a specific pixel in an image or the expression level of a gene in a specific transcriptomic experiment.
The neural networks used for deep learning have multiple hidden layers.
Each layer essentially performs feature construction for the layers before it.
The training process used often allows layers deeper in the network to contribute to the refinement of earlier layers.
For this reason, these algorithms can automatically engineer features that are suitable for many tasks and customize those features for one or more specific tasks.

Deep learning does many of the same things as more familiar machine learning approaches.
In particular, deep learning approaches can be used both in *supervised* applications---where the goal is to accurately predict one or more labels or outcomes associated with each data point---in the place of regression approaches, as well as in *unsupervised*, or "exploratory" applications---where the goal is to summarize, explain, or identify interesting patterns in a data set---as a form of clustering.
Deep learning methods may in fact combine both of these steps.
When sufficient data are available and labeled, these methods construct features tuned to a specific problem and combine those features into a predictor.
In fact, if the dataset is "labeled" with binary classes, a simple neural network with no hidden layers and no cycles between units is equivalent to logistic regression if the output layer is a sigmoid (logistic) function of the input layer.
Similarly, for continuous outcomes, linear regression can be seen as a single-layer neural network.
Thus, in some ways, supervised deep learning approaches can be seen as an extension of regression models that allow for greater flexibility and are especially well-suited for modeling non-linear relationships among the input features.
Recently, hardware improvements and very large training datasets have allowed these deep learning techniques to surpass other machine learning algorithms for many problems.
In a famous and early example, scientists from Google demonstrated that a neural network "discovered" that cats, faces, and pedestrians were important components of online videos [@url:http://research.google.com/archive/unsupervised_icml2012.html] without being told to look for them.
What if, more generally, deep learning takes advantage of the growth of data in biomedicine to tackle challenges in this field? Could these algorithms identify the "cats" hidden in our data---the patterns unknown to the researcher---and suggest ways to act on them? In this review, we examine deep learning's application to biomedical science and discuss the unique challenges that biomedical data pose for deep learning methods.

Several important advances make the current surge of work done in this area possible.
Easy-to-use software packages have brought the techniques of the field out of the specialist's toolkit to a broad community of computational scientists.
Additionally, new techniques for fast training have enabled their application to larger datasets [@arxiv:1106.5730].
Dropout of nodes, edges, and layers makes networks more robust, even when the number of parameters is very large.
Finally, the larger datasets now available are also sufficient for fitting the many parameters that exist for deep neural networks.
The convergence of these factors currently makes deep learning extremely adaptable and capable of addressing the nuanced differences of each domain to which it is applied.

![Neural networks come in many different forms.
Left: a key for the various types of nodes used in neural networks.
Simple FFNN: a feed forward neural network in which inputs are connected via some function to an output node and the model is trained to produce some output for a set of inputs.
MLP: the multi-layer perceptron is a feed forward neural network in which there is at least one hidden layer between the input and output nodes.
CNN: the convolutional neural network is a feed forward neural network in which the inputs are grouped spatially into hidden nodes.
In the case of this example, each input node is only connected to hidden nodes alongside their neighboring input node.
Autoencoder: a type of MLP in which the neural network is trained to produce an output that matches the input to the network.
RNN: a deep recurrent neural network is used to allow the neural network to retain memory over time or sequential inputs.
This figure was inspired by the [Neural Network Zoo](http://www.asimovinstitute.org/neural-network-zoo/) by Fjodor Van Veen.
<!-- Figure source at https://docs.google.com/drawings/d/1TEzlqiCewmJ-EITvogMqDz7N6CizMtBvWE4H_BXqnuQ -->
](images/petting-zoo.svg){#fig:nn-petting-zoo .white}

This review discusses recent work in the biomedical domain, and most successful applications select neural network architectures that are well suited to the problem at hand.
We sketch out a few simple example architectures in Figure @fig:nn-petting-zoo.
If data have a natural adjacency structure, a convolutional neural network (CNN) can take advantage of that structure by emphasizing local relationships, especially when convolutional layers are used in early layers of the neural network.
Other neural network architectures such as autoencoders require no labels and are now regularly used for unsupervised tasks.
In this review, we do not exhaustively discuss the different types of deep neural network architectures; an overview of the principal terms used herein is given in Table @tbl:glossary.
Table @tbl:glossary also provides select example applications, though in practice each neural network architecture has been broadly applied across multiple types of biomedical data.
A recent book from Goodfellow et al. covers neural network architectures in detail [@tag:goodfellow2016deep], and LeCun et al. provide a more general introduction [@doi:10.1038/nature14539].

| Term | Definition | Example applications |
|-----|----------|----------|
| Supervised learning | Machine-learning approaches with goal of prediction of labels or outcomes | |
| Unsupervised learning | Machine-learning approaches with goal of data summarization or pattern identification | |
| Neural network (NN) | Machine-learning approach inspired by biological neurons where inputs are fed into one or more layers, producing an output layer | |
| Deep neural network | NN with multiple hidden layers. Training happens over the network, and consequently such architectures allow for feature construction to occur alongside optimization of the overall training objective. | |
| Feed-forward neural network (FFNN) | NN that does not have cycles between nodes in the same layer | Most of the examples below are special cases of FFNNs, except recurrent neural networks. |
| Multi-layer perceptron (MLP) | Type of FFNN with at least one hidden layer where each deeper layer is a nonlinear function of each earlier layer | MLPs do not impose structure and are frequently used when there is no natural ordering of the inputs (e.g. as with gene expression measurements). |
| Convolutional neural network (CNN) | A NN with layers in which connectivity preserves local structure. _If the data meet the underlying assumptions_ performance is often good, and such networks can require fewer examples to train effectively because they have fewer parameters and also provide improved efficiency. | CNNs are used for sequence data---such as DNA sequences---or grid data---such as medical and microscopy images. |
| Recurrent neural network (RNN) | A neural network with cycles between nodes within a hidden layer. | The RNN architecture is used for sequential data---such as clinical time series and text or genome sequences. |
| Long short-term memory (LSTM) neural network | This special type of RNN has features that enable models to capture longer-term dependencies. | LSTMs are gaining a substantial foothold in the analysis of natural language, and may become more widely applied to biological sequence data. |
| Autoencoder (AE) | A NN where the training objective is to minimize the error between the output layer and the input layer. Such neural networks are unsupervised and are often used for dimensionality reduction. | Autoencoders have been used for unsupervised analysis of gene expression data as well as data extracted from the electronic health record. |
| Variational autoencoder (VAE) | This special type of generative AE learns a probabilistic latent variable model. | VAEs have been shown to often produce meaningful reduced representations in the imaging domain, and some early publications have used VAEs to analyze gene expression data. |
| Denoising autoencoder (DA) | This special type of AE includes a step where noise is added to the input during the training process. The denoising step acts as smoothing and may allow for effective use on input data that is inherently noisy. | Like AEs, DAs have been used for unsupervised analysis of gene expression data as well as data extracted from the electronic health record. |
| Generative neural network | Neural networks that fall into this class can be used to generate data similar to input data. These models can be sampled to produce hypothetical examples. | A number of the unsupervised learning neural network architectures that are summarized here can be used in a generative fashion. |
| Restricted Boltzmann machine (RBM) | A generative NN that forms the building block for many deep learning approaches, having a single input layer and a single hidden layer, with no connections between the nodes within each layer | RBMs have been applied to combine multiple types of omic data (e.g. DNA methylation, mRNA expression, and miRNA expression). |
| Deep belief network (DBN) | Generative NN with several hidden layers, which can be obtained from combining multiple RBMs | DBNs can be used to predict new relationships in a drug-target interaction network. |
| Generative adversarial network (GAN) | A generative NN approach where two neural networks are trained. One neural network, the generator, is provided with a set of randomly generated inputs and tasked with generating samples. The second, the discriminator, is trained to differentiate real and generated samples. After the two neural networks are trained against each other, the resulting generator can be used to produce new examples. | GANs can synthesize new examples with the same statistical properties of datasets that contain individual-level records and are subject to sharing restrictions. They have also been applied to generate microscopy images. |
| Adversarial training | A process by which artificial training examples are maliciously designed to fool a NN and then input as training examples to make the resulting NN robust (no relation to GANs) | Adversarial training has been used in image analysis. |
| Data augmentation | A process by which transformations that do not affect relevant properties of the input data (e.g. arbitrary rotations of histopathology images) are applied to training examples to increase the size of the training set. | Data augmentation is widely used in the analysis of images because rotation transformations for biomedical images often do not change relevant properties of the image. |

Table: Glossary.
{#tbl:glossary}

While deep learning shows increased flexibility over other machine learning approaches, as seen in the remainder of this review, it requires large training sets in order to fit the hidden layers, as well as accurate labels for the supervised learning applications.
For these reasons, deep learning has recently become popular in some areas of biology and medicine, while having lower adoption in other areas.
At the same time, this highlights the potentially even larger role that it may play in future research, given the increases in data in all biomedical fields.
It is also important to see it as a branch of machine learning and acknowledge that it has the same limitations as other approaches in that field.
In particular, the results are still dependent on the underlying study design and the usual caveats of correlation versus causation still apply---a more precise answer is only better than a less precise one if it answers the correct question.

### Will deep learning transform the study of human disease?

With this review, we ask the question: what is needed for deep learning to transform how we categorize, study, and treat individuals to maintain or restore health? We choose a high bar for "transform." Andrew Grove, the former CEO of Intel, coined the term Strategic Inflection Point to refer to a change in technologies or environment that requires a business to be fundamentally reshaped [@url:http://www.intel.com/pressroom/archive/speeches/ag080998.htm].
Here, we seek to identify whether deep learning is an innovation that can induce a Strategic Inflection Point in the practice of biology or medicine.

There are already a number of reviews focused on applications of deep learning in biology [@doi:10.1038/nbt.3313; @doi:10.1021/acs.molpharmaceut.5b00982; @tag:Angermueller2016_dl_review; @doi:10.1093/bib/bbw068; @doi:10.3109/10409238.2015.1135868], healthcare [@doi:10.1093/bib/bbx044; @tag:Litjens2017_medimage_survey; @tag:Kalinin2018_pgx], and drug discovery [@doi:10.1002/minf.201501008; @doi:10.1002/jcc.24764; @tag:PerezSianes2016_screening; @tag:Baskin2015_drug_disc].
Under our guiding question, we sought to highlight cases where deep learning enabled researchers to solve challenges that were previously considered infeasible or makes difficult, tedious analyses routine.
We also identified approaches that researchers are using to sidestep challenges posed by biomedical data.
We find that domain-specific considerations have greatly influenced how to best harness the power and flexibility of deep learning.
Model interpretability is often critical.
Understanding the patterns in data may be just as important as fitting the data.
In addition, there are important and pressing questions about how to build networks that efficiently represent the underlying structure and logic of the data.
Domain experts can play important roles in designing networks to represent data appropriately, encoding the most salient prior knowledge and assessing success or failure.
There is also great potential to create deep learning systems that augment biologists and clinicians by prioritizing experiments or streamlining tasks that do not require expert judgment.
We have divided the large range of topics into three broad classes: Disease and Patient Categorization, Fundamental Biological Study, and Treatment of Patients.
Below, we briefly introduce the types of questions, approaches and data that are typical for each class in the application of deep learning.

#### Disease and patient categorization

A key challenge in biomedicine is the accurate classification of diseases and disease subtypes.
In oncology, current "gold standard" approaches include histology, which requires interpretation by experts, or assessment of molecular markers such as cell surface receptors or gene expression.
One example is the PAM50 approach to classifying breast cancer where the expression of 50 marker genes divides breast cancer patients into four subtypes.
Substantial heterogeneity still remains within these four subtypes [@doi:10.1200/JCO.2008.18.1370; @doi:10.1158/1078-0432.CCR-13-0583].
Given the increasing wealth of molecular data available, a more comprehensive subtyping seems possible.
Several studies have used deep learning methods to better categorize breast cancer patients: For instance, denoising autoencoders, an unsupervised approach, can be used to cluster breast cancer patients [@doi:10.1142/9789814644730_0014], and CNNs can help count mitotic divisions, a feature that is highly correlated with disease outcome in histological images [@doi:10.1007/978-3-642-40763-5_51].
Despite these recent advances, a number of challenges exist in this area of research, most notably the integration of molecular and imaging data with other disparate types of data such as electronic health records (EHRs).

#### Fundamental biological study

Deep learning can be applied to answer more fundamental biological questions; it is especially suited to leveraging large amounts of data from high-throughput
"omics" studies.
One classic biological problem where machine learning, and now deep learning, has been extensively applied is molecular target prediction.
For example, deep recurrent neural networks (RNNs) have been used to predict gene targets of microRNAs [@doi:10.1109/icnn.1994.374637], and CNNs have been applied to predict protein residue-residue contacts and secondary structure [@doi:10.1371/journal.pcbi.1005324; @doi:10.1109/TCBB.2014.2343960; @doi:10.1038/srep18962].
Other recent exciting applications of deep learning include recognition of functional genomic elements such as enhancers and promoters [@doi:10.1101/036129; @doi:10.1007/978-3-319-16706-0_20; @doi:10.1093/nar/gku1058] and prediction of the deleterious effects of nucleotide polymorphisms [@doi:10.1093/bioinformatics/btu703].

#### Treatment of patients

Although the application of deep learning to patient treatment is just beginning, we expect new methods to recommend patient treatments, predict treatment outcomes, and guide the development of new therapies.
One type of effort in this area aims to identify drug targets and interactions or predict drug response.
Another uses deep learning on protein structures to predict drug interactions and drug bioactivity [@tag:Wallach2015_atom_net].
Drug repositioning using deep learning on transcriptomic data is another exciting area of research [@doi:10.1021/acs.molpharmaceut.6b00248].
Restricted Boltzmann machines (RBMs) can be combined into deep belief networks (DBNs) to predict novel drug-target interactions and formulate drug repositioning hypotheses [@doi:10.1093/bioinformatics/btt234; @doi:10.1021/acs.jproteome.6b00618].
Finally, deep learning is also prioritizing chemicals in the early stages of drug discovery for new targets [@tag:Baskin2015_drug_disc].


## Deep learning and patient categorization

In healthcare, individuals are diagnosed with a disease or condition based on symptoms, the results of certain diagnostic tests, or other factors.
Once diagnosed with a disease, an individual might be assigned a stage based on another set of human-defined rules.
While these rules are refined over time, the process is evolutionary and ad hoc, potentially impeding the identification of underlying biological mechanisms and their corresponding treatment interventions.

Deep learning methods applied to a large corpus of patient phenotypes may provide a meaningful and more data-driven approach to patient categorization.
For example, they may identify new shared mechanisms that would otherwise be obscured due to ad hoc historical definitions of disease.
Perhaps deep neural networks, by reevaluating data without the context of our assumptions, can reveal novel classes of treatable conditions.

In spite of such optimism, the ability of deep learning models to indiscriminately extract predictive signals must also be assessed and operationalized with care.
Imagine a deep neural network is provided with clinical test results gleaned from electronic health records.
Because physicians may order certain tests based on their suspected diagnosis, a deep neural network may learn to "diagnose" patients simply based on the tests that are ordered.
For some objective functions, such as predicting an International Classification of Diseases (ICD) code, this may offer good performance even though it does not provide insight into the underlying disease beyond physician activity.
This challenge is not unique to deep learning approaches; however, it is important for practitioners to be aware of these challenges and the possibility in this domain of constructing highly predictive classifiers of questionable utility.

Our goal in this section is to assess the extent to which deep learning is already contributing to the discovery of novel categories.
Where it is not, we focus on barriers to achieving these goals.
We also highlight approaches that researchers are taking to address challenges within the field, particularly with regards to data availability and labeling.

### Imaging applications in healthcare

Deep learning methods have transformed the analysis of natural images and video, and similar examples are beginning to emerge with medical images.
Deep learning has been used to classify lesions and nodules; localize organs, regions, landmarks and lesions; segment organs, organ substructures and lesions; retrieve images based on content; generate and enhance images; and combine images with clinical reports [@tag:Litjens2017_medimage_survey; @tag:Shen2017_medimg_review].

Though there are many commonalities with the analysis of natural images, there are also key differences.
In all cases that we examined, fewer than one million images were available for training, and datasets are often many orders of magnitude smaller than collections of natural images.
Researchers have developed subtask-specific strategies to address this challenge.

Data augmentation provides an effective strategy for working with small training sets.
The practice is exemplified by a series of papers that analyze images from mammographies [@tag:Dhungel2015_struct_pred_mamm; @tag:Dhungel2016_mamm; @tag:Zhu2016_mult_inst_mamm; @tag:Zhu2016_advers_mamm; @tag:Dhungel2017_mamm_min_interv].
To expand the number and diversity of images, researchers constructed adversarial [@tag:Zhu2016_advers_mamm] or augmented [@tag:Dhungel2017_mamm_min_interv] examples.
Adversarial training examples are constructed by selecting targeted small transformations to input data that cause a model to produce very different outputs.
Augmented training applies perturbations to the input data that do not change the underlying meaning, such as rotations for pathology images.
An alternative in the domain is to train towards human-created features before subsequent fine-tuning [@tag:Dhungel2016_mamm], which can help to sidestep this challenge though it does give up deep learning techniques' strength as feature constructors.

A second strategy repurposes features extracted from natural images by deep learning models, such as ImageNet [@tag:Russakovsky2015_imagenet], for new purposes.
Diagnosing diabetic retinopathy through color fundus images became an area of focus for deep learning researchers after a large labeled image set was made publicly available during a 2015 Kaggle competition [@tag:Pratt2016_dr].
Most participants trained neural networks from scratch [@tag:Pratt2016_dr; @tag:Abramoff2016_dr; @tag:Leibig2016_dr], but Gulshan et al. [@tag:Gulshan2016_dt] repurposed a 48-layer Inception-v3 deep architecture pre-trained on natural images and surpassed the state-of-the-art specificity and sensitivity.
Such features were also repurposed to detect melanoma, the deadliest form of skin cancer, from dermoscopic [@tag:Codella2016_ensemble_melanoma; @tag:Yu2016_melanoma_resnet] and non-dermoscopic images of skin lesions [@tag:Jafari2016_skin_lesions; @tag:Esfahani2016_melanoma; @tag:Esteva2017_skin_cancer_nature] as well as age-related macular degeneration [@tag:Burlina2016_amd].
Pre-training on natural images can enable very deep networks to succeed without overfitting.
For the melanoma task, reported performance was competitive with or better than a board of certified dermatologists [@tag:Codella2016_ensemble_melanoma; @tag:Esteva2017_skin_cancer_nature].
Reusing features from natural images is also an emerging approach for radiographic images, where datasets are often too small to train large deep neural networks without these techniques [@tag:Bar2015_nonmed_tl; @tag:Shin2016_cad_tl; @tag:Rajkomar2017_radiographs; @tag:Lakhani2017_radiography].
A deep CNN trained on natural images boosts performance in radiographic images [@tag:Rajkomar2017_radiographs].
However, the target task required either re-training the initial model from scratch with special pre-processing or fine-tuning of the whole network on radiographs with heavy data augmentation to avoid overfitting.

The technique of reusing features from a different task falls into the broader area of transfer learning (see Discussion).
Though we've mentioned numerous successes for the transfer of natural image features to new tasks, we expect that a lower proportion of negative results have been published.
The analysis of magnetic resonance images (MRIs) is also faced with the challenge of small training sets.
In this domain, Amit et al. [@tag:Amit2017_breast_mri] investigated the tradeoff between pre-trained models from a different domain and a small CNN trained only with MRI images.
In contrast with the other selected literature, they found a smaller network trained with data augmentation on a few hundred images from a few dozen patients can outperform a pre-trained out-of-domain classifier.

Another way of dealing with limited training data is to divide rich data---e.g. 3D images---into numerous reduced projections.
Shin et al. [@tag:Shin2016_cad_tl] compared various deep network architectures, dataset characteristics, and training procedures for computer tomography-based (CT) abnormality detection.
They concluded that networks as deep as 22 layers could be useful for 3D data, despite the limited size of training datasets.
However, they noted that choice of architecture, parameter setting, and model fine-tuning needed is very problem- and dataset-specific.
Moreover, this type of task often depends on both lesion localization and appearance, which poses challenges for CNN-based approaches.
Straightforward attempts to capture useful information from full-size images in all three dimensions simultaneously via standard neural network architectures were computationally unfeasible.
Instead, two-dimensional models were used to either process image slices individually (2D) or aggregate information from a number of 2D projections in the native space (2.5D).

Roth et al. compared 2D, 2.5D, and 3D CNNs on a number of tasks for computer-aided detection from CT scans and showed that 2.5D CNNs performed comparably well to 3D analogs, while requiring much less training time, especially on augmented training sets [@tag:Roth2015_view_agg_cad].
Another advantage of 2D and 2.5D networks is the wider availability of pre-trained models.
However, reducing the dimensionality is not always helpful.
Nie et al. [@tag:Nie2016_3d_survival] showed that multimodal, multi-channel 3D deep architecture was successful at learning high-level brain tumor appearance features jointly from MRI, functional MRI, and diffusion MRI images, outperforming single-modality or 2D models.
Overall, the variety of modalities, properties and sizes of training sets, the dimensionality of input, and the importance of end goals in medical image analysis are provoking a development of specialized deep neural network architectures, training and validation protocols, and input representations that are not characteristic of widely-studied natural images.

Predictions from deep neural networks can be evaluated for use in workflows that also incorporate human experts.
In a large dataset of mammography images, Kooi et al. [@tag:Kooi2016_mamm_lesions] demonstrated that deep neural networks outperform a traditional computer-aided diagnosis system at low sensitivity and perform comparably at high sensitivity.
They also compared network performance to certified screening radiologists on a patch level and found no significant difference between the network and the readers.
However, using deep methods for clinical practice is challenged by the difficulty of assigning a level of confidence to each prediction.
Leibig et al. [@tag:Leibig2016_dr] estimated the uncertainty of deep networks for diabetic retinopathy diagnosis by linking dropout networks with approximate Bayesian inference.
Techniques that assign confidences to each prediction should aid physician-computer interactions and improve uptake by physicians.

Systems to aid in the analysis of histology slides are also promising use cases for deep learning [@tag:Litjens2016_histopath_survey].
Ciresan et al.
[@tag:Ciresan2013_mitosis] developed one of the earliest approaches for histology slides, winning the 2012 International Conference on Pattern Recognition's Contest on Mitosis Detection while achieving human-competitive accuracy.
In more recent work, Wang et al. [@tag:Wang2016_breast_cancer] analyzed stained slides of lymph node slices to identify cancers.
On this task a pathologist has about a 3% error rate.
The pathologist did not produce any false positives, but did have a number of false negatives.
The algorithm had about twice the error rate of a pathologist, but the errors were not strongly correlated.
Combining pre-trained deep network architectures with multiple augmentation techniques enabled accurate detection of breast cancer from a very small set of histology images with less than 100 images per class [@tag:Rakhlin2018_histology].
In this area, these algorithms may be ready to be incorporated into existing tools to aid pathologists and reduce the false negative rate.
Ensembles of deep learning and human experts may help overcome some of the challenges presented by data limitations.

One source of training examples with rich phenotypical annotations is the EHR.
Billing information in the form of ICD codes are simple annotations but phenotypic algorithms can combine laboratory tests, medication prescriptions, and patient notes to generate more reliable phenotypes.
Recently, Lee et al. [@tag:Lee2016_emr_oct_amd] developed an approach to distinguish individuals with age-related macular degeneration from control individuals.
They trained a deep neural network on approximately 100,000 images extracted from structured electronic health records, reaching greater than 93% accuracy.
The authors used their test set to evaluate when to stop training.
In other domains, this has resulted in a minimal change in the estimated accuracy [@tag:Krizhevsky2013_nips_cnn], but we recommend the use of an independent test set whenever feasible.

Rich clinical information is stored in EHRs.
However, manually annotating a large set requires experts and is time consuming.
For chest X-ray studies, a radiologist usually spends a few minutes per example.
Generating the number of examples needed for deep learning is infeasibly expensive.
Instead, researchers may benefit from using text mining to generate annotations [@doi:10.3115/1572392.1572411], even if those annotations are of modest accuracy.
Wang et al. [@arxiv:1705.02315] proposed to build predictive deep neural network models through the use of images with *weak labels*.
Such labels are automatically generated and not verified by humans, so they may be noisy or incomplete.
In this case, they applied a series of natural language processing (NLP) techniques to the associated chest X-ray radiological reports.
They first extracted all diseases mentioned in the reports using a state-of-the-art NLP tool, then applied a new method, NegBio [@arxiv:1712.05898], to filter negative and equivocal findings in the reports.
Evaluation on four independent datasets demonstrated that NegBio is highly accurate for detecting negative and equivocal findings (~90% in F₁ score, which balances precision and recall [@doi:10.1038/nmeth.3945]).
The resulting dataset [@url:https://nihcc.app.box.com/v/ChestXray-NIHCC] consisted of 112,120 frontal-view chest X-ray images from 30,805 patients, and each image was associated with one or more *text-mined* (weakly-labeled) pathology categories (e.g. pneumonia and cardiomegaly) or "no finding" otherwise.
Further, Wang et al. [@arxiv:1705.02315] used this dataset with a unified weakly-supervised multi-label image classification framework to detect common thoracic diseases.
It showed superior performance over a benchmark using fully-labeled data.

Another example of semi-automated label generation for hand radiograph segmentation employed positive mining, an iterative procedure that combines manual labeling with automatic processing [@tag:Iglovikov2017_baa].
First, the initial training set was created by manually labeling 100 of 12,600 unlabeled radiographs that were used to train a model and predict labels for the rest of the dataset.
Then, poor quality predictions were discarded through manual inspection, the initial training set was expanded with the acceptable segmentations, and the process was repeated.
This procedure had to be repeated six times to obtain good quality segmentation labeling for all radiographs, except for 100 corner cases that still required manual annotation.
These annotations allowed accurate segmentation of all hand images in the test set and boosted the final performance in radiograph classification [@tag:Iglovikov2017_baa].

With the exception of natural image-like problems (e.g. melanoma detection), biomedical imaging poses a number of challenges for deep learning.
Datasets are typically small, annotations can be sparse, and images are often high-dimensional, multimodal, and multi-channel.
Techniques like transfer learning, heavy dataset augmentation, and the use of multi-view and multi-stream architectures are more common than in the natural image domain.
Furthermore, high model sensitivity and specificity can translate directly into clinical value.
Thus, prediction evaluation, uncertainty estimation, and model interpretation methods are also of great importance in this domain (see Discussion).
Finally, there is a need for better pathologist-computer interaction techniques that will allow combining the power of deep learning methods with human expertise and lead to better-informed decisions for patient treatment and care.

### Text applications in healthcare

Due to the rapid growth of scholarly publications and EHRs, biomedical text mining has become increasingly important in recent years.
The main tasks in biological and clinical text mining include, but are not limited to, named entity recognition, relation/event extraction, and information retrieval (Figure @fig:biotm).
Deep learning is appealing in this domain because of its competitive performance versus traditional methods and ability to overcome challenges in feature engineering.
Relevant applications can be stratified by the application domain (biomedical literature vs. clinical notes) and the actual task (e.g. concept or relation extraction).

![Deep learning applications, tasks, and models based on NLP perspectives.](images/biotm.png){#fig:biotm .white width="100%"}

Named entity recognition (NER) is a task of identifying text spans that refer to a biological concept of a specific class, such as disease or chemical, in a controlled vocabulary or ontology.
NER is often needed as a first step in many complex text mining systems.
The current state-of-the-art methods typically reformulate the task as a sequence labeling problem and use conditional random fields [@doi:10.1093/bioinformatics/btw343; @doi:10.1093/bioinformatics/btt156; @doi:10.1093/bioinformatics/btt474].
In recent years, word embeddings that contain rich latent semantic information of words have been widely used to improve the NER performance.
Liu et al. studied the effect of word embeddings on drug name recognition and compared them with traditional semantic features [@doi:10.3390/info6040848].
Tang et al. investigated word embeddings in gene, DNA, and cell line mention detection tasks [@doi:10.1155/2014/240403].
Moreover, Wu et al. examined the use of neural word embeddings for clinical abbreviation disambiguation [@doi:10.18653/v1/w15-3822].
Liu et al. exploited task-oriented resources to learn word embeddings for clinical abbreviation expansion [@doi:10.18653/v1/w15-3810].

Relation extraction involves detecting and classifying semantic relationships between entities from the literature.
At present, kernel methods or feature-based approaches are commonly applied [@doi:10.1371/journal.pcbi.1000837; @doi:10.1186/s13321-016-0165-z; @doi:10.1093/bioinformatics/btp602].
Deep learning can relieve the feature sparsity and engineering problems.
Some studies focused on jointly extracting biomedical entities and relations simultaneously [@tag:li2016joint; @doi:10.1186/s12859-017-1609-9], while others applied deep learning on relation classification given the relevant entities.
For example, both multichannel dependency-based CNNs [@doi:10.18653/v1/w17-2304] and shortest path-based CNNs [@doi:10.1155/2016/8479587; @doi:10.1155/2016/1850404] are well-suited for sentence-based protein-protein extraction.
Jiang et al. proposed a biomedical domain-specific word embedding model to reduce the manual labor of designing semantic representation for the same task [@doi:10.1504/IJDMB.2016.074878].
Gu et al. employed a maximum entropy model and a CNN model for chemical-induced disease relation extraction at the inter- and intra-sentence level, respectively [@doi:10.1093/database/bax024].
For drug-drug interactions, Zhao et al. used a CNN that employs word embeddings with the syntactic information of a sentence as well as features of part-of-speech tags and dependency trees [@doi:10.1093/bioinformatics/btw486].
Asada et al. experimented with an attention CNN [@doi:10.18653/v1/w17-2302], and Yi et al. proposed an RNN model with multiple attention layers [@arxiv:1705.03261].
In both cases, it is a single model with attention mechanism, which allows the decoder to focus on different parts of the source sentence.
As a result, it does not require dependency parsing or training multiple models.
Both attention CNN and RNN have comparable results, but the CNN model has an advantage in that it can be easily computed in parallel, hence making it faster with recent graphics processing units (GPUs).

For biotopes event extraction, Li et al. employed CNNs and distributed representation [@doi:10.18653/v1/w16-3012] while Mehryary et al. used long short-term memory (LSTM) networks to extract complicated relations [@doi:10.18653/v1/w16-3009].
Li et al. applied word embedding to extract complete events from biomedical text and achieved results comparable to the state-of-the-art systems [@doi:10.18653/v1/w15-3814].
There are also approaches that identify event triggers rather than the complete event [@doi:10.1142/S0219720015410012; @arxiv:1705.09516].
Taken together, deep learning models outperform traditional kernel methods or feature-based approaches by 1--5% in f-score.
Among various deep learning approaches, CNNs stand out as the most popular model both in terms of computational complexity and performance, while RNNs have achieved continuous progress.

Information retrieval is a task of finding relevant text that satisfies an information need from within a large document collection.
While deep learning has not yet achieved the same level of success in this area as seen in others, the recent surge of interest and work suggest that this may be quickly changing.
For example, Mohan et al. described a deep learning approach to modeling the relevance of a document's text to a query, which they applied to the entire biomedical literature [@doi:10.18653/v1/w17-2328].

To summarize, deep learning has shown promising results in many biomedical text mining tasks and applications.
However, to realize its full potential in this domain, either large amounts of labeled data or technical advancements in current methods coping with limited labeled data are required.

### Electronic health records

EHR data include substantial amounts of free text, which remains challenging to approach [@doi:10.1136/amiajnl-2011-000501].
Often, researchers developing algorithms that perform well on specific tasks must design and implement domain-specific features [@doi:10.1136/amiajnl-2011-000150].
These features capture unique aspects of the literature being processed.
Deep learning methods are natural feature constructors.
In recent work, Chalapathy et al. evaluated the extent to which deep learning methods could be applied on top of generic features for domain-specific concept extraction [@arxiv:1611.08373].
They found that performance was in line with, but lower than the best domain-specific method [@arxiv:1611.08373].
This raises the possibility that deep learning may impact the field by reducing the researcher time and cost required to develop specific solutions, but it may not always lead to performance increases.

In recent work, Yoon et al. [@tag:Yoon2016_cancer_reports] analyzed simple features using deep neural networks and found that the patterns recognized by the algorithms could be re-used across tasks.
Their aim was to analyze the free text portions of pathology reports to identify the primary site and laterality of tumors.
The only features the authors supplied to the algorithms were unigrams (counts for single words) and bigrams (counts for two-word combinations) in a free text document.
They subset the full set of words and word combinations to the 400 most common.
The machine learning algorithms that they employed (naïve Bayes, logistic regression, and deep neural networks) all performed relatively similarly on the task of identifying the primary site.
However, when the authors evaluated the more challenging task, evaluating the laterality of each tumor, the deep neural network outperformed the other methods.
Of particular interest, when the authors first trained a neural network to predict the primary site and then repurposed those features as a component of a secondary neural network trained to predict laterality, the performance was higher than a laterality-trained neural network.
This demonstrates how deep learning methods can repurpose features across tasks, improving overall predictions as the field tackles new challenges.
The Discussion further reviews this type of transfer learning.

Several authors have created reusable feature sets for medical terminologies using natural language processing and neural embedding models, as popularized by word2vec [@arxiv:1301.3781].
Minarro-Giménez et al. [@doi:10.3233/978-1-61499-432-9-584] applied the word2vec deep learning toolkit to medical corpora and evaluated the efficiency of word2vec in identifying properties of pharmaceuticals based on mid-sized, unstructured medical text corpora without any additional background knowledge.
A goal of learning terminologies for different entities in the same vector space is to find relationships between different domains (e.g. drugs and the diseases they treat).
It is difficult for us to provide a strong statement on the broad utility of these methods.
Manuscripts in this area tend to compare algorithms applied to the same data but lack a comparison against overall best-practices for one or more tasks addressed by these methods.
Techniques have been developed for free text medical notes [@doi:10.1145/2661829.2661974], ICD and National Drug Codes [@doi:10.18653/v1/w17-2342; @tag:world2004international], and claims data [@doi:10.1145/2939672.2939823].
Methods for neural embeddings learned from electronic health records have at least some ability to predict disease-disease associations and implicate genes with a statistical association with a disease [@doi:10.1038/srep32404], but the evaluations performed did not differentiate between simple predictions (i.e. the same disease in different sites of the body) and non-intuitive ones.
Jagannatha and Yu [@pmcid:PMC5119627] further employed a bidirectional LSTM structure to extract adverse drug events from electronic health records, and Lin et al. [@doi:10.18653/v1/w17-2341] investigated using CNNs to extract temporal relations.
While promising, a lack of rigorous evaluation of the real-world utility of these kinds of features makes current contributions in this area difficult to evaluate.
Comparisons need to be performed to examine the true utility against leading approaches (i.e. algorithms and data) as opposed to simply evaluating multiple algorithms on the same potentially limited dataset.

Identifying consistent subgroups of individuals and individual health trajectories from clinical tests is also an active area of research.
Approaches inspired by deep learning have been used for both unsupervised feature construction and supervised prediction.
Early work by Lasko et al. [@doi:10.1371/journal.pone.0066341], combined sparse autoencoders and Gaussian processes to distinguish gout from leukemia from uric acid sequences.
Later work showed that unsupervised feature construction of many features via denoising autoencoder neural networks could dramatically reduce the number of labeled examples required for subsequent supervised analyses [@doi:10.1016/j.jbi.2016.10.007].
In addition, it pointed towards features learned during unsupervised training being useful for visualizing and stratifying subgroups of patients within a single disease.
In a concurrent large-scale analysis of EHR data from 700,000 patients, Miotto et al. [@doi:10.1038/srep26094] used a deep denoising autoencoder architecture applied to the number and co-occurrence of clinical events to learn a representation of patients (DeepPatient).
The model was able to predict disease trajectories within one year with over 90% accuracy, and patient-level predictions were improved by up to 15% when compared to other methods.
Choi et al. [@arxiv:1511.05942] attempted to model the longitudinal structure of EHRs with an RNN to predict future diagnosis and medication prescriptions on a cohort of 260,000 patients followed for 8 years (Doctor AI).
Pham et al. [@arxiv:1602.00357] built upon this concept by using an RNN with a LSTM architecture enabling explicit modelling of patient trajectories through the use of memory cells.
The method, DeepCare, performed better than shallow models or plain RNN when tested on two independent cohorts for its ability to predict disease progression, intervention recommendation and future risk prediction.
Nguyen et al. [@doi:10.1109/JBHI.2016.2633963] took a different approach and used word embeddings from EHRs to train a CNN that could detect and pool local clinical motifs to predict unplanned readmission after six months, with performance better than the baseline method (Deepr).
Razavian et al. [@arxiv:1608.00647] used a set of 18 common lab tests to predict disease onset using both CNN and LSTM architectures and demonstrated an improvement over baseline regression models.
However, numerous challenges including data integration (patient demographics, family history, laboratory tests, text-based patient records, image analysis, genomic data) and better handling of streaming temporal data with many features will need to be overcome before we can fully assess the potential of deep learning for this application area.

Still, recent work has also revealed domains in which deep networks have proven superior to traditional methods.
Survival analysis models the time leading to an event of interest from a shared starting point, and in the context of EHR data, often associates these events to subject covariates.
Exploring this relationship is difficult, however, given that EHR data types are often heterogeneous, covariates are often missing, and conventional approaches require the covariate-event relationship be linear and aligned to a specific starting point [@arxiv:1608.02158].
Early approaches, such as the Faraggi-Simon feed-forward network, aimed to relax the linearity assumption, but performance gains were lacking [@tag:Xiang].
Katzman et al. in turn developed a deep implementation of the Faraggi-Simon network that, in addition to outperforming Cox regression, was capable of comparing the risk between a given pair of treatments, thus potentially acting as recommender system [@arxiv:1606.00931].
To overcome the remaining difficulties, researchers have turned to deep exponential families, a class of latent generative models that are constructed from any type of exponential family distributions [@arxiv:1411.2581v1].
The result was a deep survival analysis model capable of overcoming challenges posed by missing data and heterogeneous data types, while uncovering nonlinear relationships between covariates and failure time.
They showed their model more accurately stratified patients as a function of disease risk score compared to the current clinical implementation.

There is a computational cost for these methods, however, when compared to traditional, non-neural network approaches.
For the exponential family models, despite their scalability [@arxiv:1206.7051], an important question for the investigator is whether he or she is interested in estimates of posterior uncertainty.
Given that these models are effectively Bayesian neural networks, much of their utility simplifies to whether a Bayesian approach is warranted for a given increase in computational cost.
Moreover, as with all variational methods, future work must continue to explore just how well the posterior distributions are approximated, especially as model complexity increases [@arxiv:1511.02386].

### Challenges and opportunities in patient categorization

#### Generating ground-truth labels can be expensive or impossible

A dearth of true labels is perhaps among the biggest obstacles for EHR-based analyses that employ machine learning.
Popular deep learning (and other machine learning) methods are often used to tackle classification tasks and thus require ground-truth labels for training.
For EHRs this can mean that researchers must hire multiple clinicians to manually read and annotate individual patients' records through a process called chart review.
This allows researchers to assign "true" labels, i.e. those that match our best available knowledge.
Depending on the application, sometimes the features constructed by algorithms also need to be manually validated and interpreted by clinicians.
This can be time consuming and expensive [@doi:10.1016/j.ijmedinf.2016.09.014].
Because of these costs, much of this research, including the work cited in this review, skips the process of expert review.
Clinicians' skepticism for research without expert review may greatly dampen their enthusiasm for the work and consequently reduce its impact.
To date, even well-resourced large national consortia have been challenged by the task of acquiring enough expert-validated labeled data.
For instance, in the eMERGE consortia and PheKB database [@url:https://phekb.org/implementations], most samples with expert validation contain only 100 to 300 patients.
These datasets are quite small even for simple machine learning algorithms.
The challenge is greater for deep learning models with many parameters.
While unsupervised and semi-supervised approaches can help with small sample sizes, the field would benefit greatly from large collections of anonymized records in which a substantial number of records have undergone expert review.
This challenge is not unique to EHR-based studies.
Work on medical images, omics data in applications for which detailed metadata are required, and other applications for which labels are costly to obtain will be hampered as long as abundant curated data are unavailable.

Successful approaches to date in this domain have sidestepped this challenge by making methodological choices that either reduce the need for labeled examples or that use transformations to training data to increase the number of times it can be used before overfitting occurs.
For example, the unsupervised and semi-supervised methods that we have discussed reduce the need for labeled examples [@doi:10.1016/j.jbi.2016.10.007].
The anchor and learn framework [@doi:10.1093/jamia/ocw011] uses expert knowledge to identify high-confidence observations from which labels can be inferred.
If transformations are available that preserve the meaningful content of the data, the adversarial and augmented training techniques discussed above can reduce overfitting.
While these can be easily imagined for certain methods that operate on images, it is more challenging to figure out equivalent transformations for a patient's clinical test results.
Consequently, it may be hard to employ such training examples with other applications.
Finally, approaches that transfer features can also help use valuable training data most efficiently.
Rajkomar et al. trained a deep neural network using generic images before tuning using only radiology images [@doi:10.1007/s10278-016-9914-9].
Datasets that require many of the same types of features might be used for initial training, before fine tuning takes place with the more sparse biomedical examples.
Though the analysis has not yet been attempted, it is possible that analogous strategies may be possible with electronic health records.
For example, features learned from the electronic health record for one type of clinical test (e.g. a decrease over time in a lab value) may transfer across phenotypes.
Methods to accomplish more with little high-quality labeled data arose in other domains and may also be adapted to this challenge, e.g. data programming [@arxiv:1605.07723].
In data programming, noisy automated labeling functions are integrated.

Numerous commentators have described data as the new oil [@url:http://ana.blogs.com/maestros/2006/11/data_is_the_new.html; @url:https://medium.com/twenty-one-hundred/data-is-the-new-oil-a-ludicrous-proposition-1d91bba4f294].
The idea behind this metaphor is that data are available in large quantities, valuable once refined, and this underlying resource will enable a data-driven revolution in how work is done.
Contrasting with this perspective, Ratner, Bach, and Ré described labeled training data, instead of data, as "The _New_ New Oil"
[@url:http://hazyresearch.github.io/snorkel/blog/weak_supervision.html].
In this framing, data are abundant and not a scarce resource.
Instead, new approaches to solving problems arise when labeled training data become sufficient to enable them.
Based on our review of research on deep learning methods to categorize disease, the latter framing rings true.

We expect improved methods for domains with limited data to play an important role if deep learning is going to transform how we categorize states of human health.
We don't expect that deep learning methods will replace expert review.
We expect them to complement expert review by allowing more efficient use of the costly practice of manual annotation.

#### Data sharing is hampered by standardization and privacy considerations

To construct the types of very large datasets that deep learning methods thrive on, we need robust sharing of large collections of data.
This is in part a cultural challenge.
We touch on this challenge in the Discussion section.
Beyond the cultural hurdles around data sharing, there are also technological and legal hurdles related to sharing individual health records or deep models built from such records.
This subsection deals primarily with these challenges.

EHRs are designed chiefly for clinical, administrative and financial purposes, such as patient care, insurance, and billing [@doi:10.1038/nrg3208].
Science is at best a tertiary priority, presenting challenges to EHR-based research in general and to deep learning research in particular.
Although there is significant work in the literature around EHR data quality and the impact on research [@doi:10.1136/amiajnl-2011-000681], we focus on three types of challenges: local bias, wider standards, and legal issues.
Note these problems are not restricted to EHRs but can also apply to any large biomedical dataset, e.g. clinical trial data.

Even within the same healthcare system, EHRs can be used differently [@pmcid:PMC3797550; @pmcid:PMC3041534].
Individual users have unique documentation and ordering patterns, with different departments and different hospitals having different priorities that code patients and introduce missing data in a non-random fashion [@tag:Serden].
Patient data may be kept across several "silos" within a single health system (e.g. separate nursing documentation, registries, etc.).
Even the most basic task of matching patients across systems can be challenging due to data entry issues [@pmcid:PMC4832129].
The situation is further exacerbated by the ongoing introduction, evolution, and migration of EHR systems, especially where reorganized and acquired healthcare facilities have to merge.
Further, even the ostensibly least-biased data type, laboratory measurements, can be biased based by both the healthcare process and patient health state [@doi:10.1016/j.jbi.2014.03.016].
As a result, EHR data can be less complete and less objective than expected.

In the wider picture, standards for EHRs are numerous and evolving.
Proprietary systems, indifferent and scattered use of health information standards, and controlled terminologies makes combining and comparison of data across systems challenging [@doi:10.1016/j.jbi.2014.10.006].
Further diversity arises from variation in languages, healthcare practices, and demographics.
Merging EHRs gathered in different systems (and even under different assumptions) is challenging [@doi:10.1007/978-3-319-44839-8].

Combining or replicating studies across systems thus requires controlling for both the above biases and dealing with mismatching standards.
This has the practical effect of reducing cohort size, limiting statistical significance, preventing the detection of weak effects [@doi:10.1590/2176-9451.19.4.027-029.ebo], and restricting the number of parameters that can be trained in a model.
Further, rule-based algorithms have been popular in EHR-based research, but because these are developed at a single institution and trained with a specific patient population, they do not transfer easily to other healthcare systems [@doi:10.1136/amiajnl-2013-001935].
Genetic studies using EHR data are subject to even more bias, as the differences in population ancestry across health centers (e.g. proportion of patients with African or Asian ancestry) can affect algorithm performance.
For example, Wiley et al. [@doi:10.1142/9789813207813_0050] showed that warfarin dosing algorithms often under-perform in African Americans, illustrating that some of these issues are unresolved even at a treatment best practices level.
Lack of standardization also makes it challenging for investigators skilled in deep learning to enter the field, as numerous data processing steps must be performed before algorithms are applied.

Finally, even if data were perfectly consistent and compatible across systems, attempts to share and combine EHR data face considerable legal and ethical barriers.
Patient privacy can severely restrict the sharing and use of EHR data [@doi:10.1093/ije/dyn022].
Here again, standards are heterogeneous and evolving, but often EHR data cannot be exported or even accessed directly for research purposes without appropriate consent.
In the United States, research use of EHR data is subject both to the Common Rule and the Health Insurance Portability and Accountability Act (HIPAA).
Ambiguity in the regulatory language and individual interpretation of these rules can hamper use of EHR data [@doi:10.1093/jamia/ocv111].
Once again, this has the effect of making data gathering more laborious and expensive, reducing sample size and study power.

Several technological solutions have been proposed in this direction, allowing access to sensitive data satisfying privacy and legal concerns.
Software like DataShield [@doi:10.1093/ije/dyu188] and ViPAR [@doi:10.1093/ije/dyv193], although not EHR-specific, allow querying and combining of datasets and calculation of summary statistics across remote sites by "taking the analysis to the data".
The computation is carried out at the remote site.
Conversely, the EH4CR project [@doi:10.1016/j.jbi.2014.10.006] allows analysis of private data by use of an inter-mediation layer that interprets remote queries across internal formats and datastores and returns the results in a de-identified standard form, thus giving real-time consistent but secure access.
Continuous Analysis [@doi:10.1038/nbt.3780] can allow reproducible computing on private data.
Using such techniques, intermediate results can be automatically tracked and shared without sharing the original data.
While none of these have been used in deep learning, the potential is there.

Even without sharing data, algorithms trained on confidential patient data may present security risks or accidentally allow for the exposure of individual level patient data.
Tramer et al. [@arxiv:1609.02943] showed the ability to steal trained models via public application programming interfaces (APIs).
Dwork and Roth [@doi:10.1561/0400000042] demonstrate the ability to expose individual level information from accurate answers in a machine learning model.
Attackers can use similar attacks to find out if a particular data instance was present in the original training set for the machine learning model [@arxiv:1610.05820], in this case, whether a person's record was present.
To protect against these attacks, Simmons et al. [@doi:10.1016/j.cels.2016.04.013] developed the ability to perform genome-wide association studies (GWASs) in a differentially private manner, and Abadi et al. [@doi:10.1145/2976749.2978318] show the ability to train deep learning classifiers under the differential privacy framework.

These attacks also present a potential hazard for approaches that aim to generate data.
Choi et al. propose generative adversarial neural networks (GANs) as a tool to make sharable EHR data [@arxiv:1703.06490v1], and Esteban et al. [@arxiv:1706.02633v1] showed that recurrent GANs could be used for time series data.
However, in both cases the authors did not take steps to protect the model from such attacks.
There are approaches to protect models, but they pose their own challenges.
Training in a differentially private manner provides a limited guarantee that an algorithm's output will be equally likely to occur regardless of the participation of any one individual.
The limit is determined by parameters which provide a quantification of privacy.
Beaulieu-Jones et al. demonstrated the ability to generate data that preserved properties of the SPRINT clinical trial with GANs under the differential privacy framework [@doi:10.1101/159756].
Both Beaulieu-Jones et al. and Esteban et al. train models on synthetic data generated under differential privacy and observe performance from a transfer learning evaluation that is only slightly below models trained on the original, real data.
Taken together, these results suggest that differentially private GANs may be an attractive way to generate sharable datasets for downstream reanalysis.

Federated learning [@url:http://proceedings.mlr.press/v54/mcmahan17a.html] and secure aggregations [@url:https://eprint.iacr.org/2017/281.pdf; @tag:Papernot2017_pate] are complementary approaches that reinforce differential privacy.
Both aim to maintain privacy by training deep learning models from decentralized data sources such as personal mobile devices without transferring actual training instances.
This is becoming of increasing importance with the rapid growth of mobile health applications.
However, the training process in these approaches places constraints on the algorithms used and can make fitting a model substantially more challenging.
It can be trivial to train a model without differential privacy, but quite difficult to train one within the differential privacy framework [@doi:10.1101/159756].
This problem can be particularly pronounced with small sample sizes.

While none of these problems are insurmountable or restricted to deep learning, they present challenges that cannot be ignored.
Technical evolution in EHRs and data standards will doubtless ease---although not solve---the problems of data sharing and merging.
More problematic are the privacy issues.
Those applying deep learning to the domain should consider the potential of inadvertently disclosing the participants' identities.
Techniques that enable training on data without sharing the raw data may have a part to play.
Training within a differential privacy framework may often be warranted.

#### Discrimination and "right to an explanation" laws

In April 2016, the European Union adopted new rules regarding the use of personal information, the General Data Protection Regulation [@arxiv:1606.08813v3].
A component of these rules can be summed up by the phrase
"right to an explanation".
Those who use machine learning algorithms must be able to explain how a decision was reached.
For example, a clinician treating a patient who is aided by a machine learning algorithm may be expected to explain decisions that use the patient's data.
The new rules were designed to target categorization or recommendation systems, which inherently profile individuals.
Such systems can do so in ways that are discriminatory and unlawful.

As datasets become larger and more complex, we may begin to identify relationships in data that are important for human health but difficult to understand.
The algorithms described in this review and others like them may become highly accurate and useful for various purposes, including within medical practice.
However, to discover and avoid discriminatory applications it will be important to consider interpretability alongside accuracy.
A number of properties of genomic and healthcare data will make this difficult.

First, research samples are frequently non-representative of the general population of interest; they tend to be disproportionately sick [@doi:10.1086/512821], male [@doi:10.1016/j.neubiorev.2010.07.002], and European in ancestry [@doi:10.1371/journal.pbio.1001661].
One well-known consequence of these biases in genomics is that penetrance is consistently lower in the general population than would be implied by case-control data, as reviewed in [@doi:10.1086/512821].
Moreover, real genetic associations found in one population may not hold in other populations with different patterns of linkage disequilibrium (even when population stratification is explicitly controlled for [@doi:10.1038/nrg2813]).
As a result, many genomic findings are of limited value for people of non-European ancestry [@doi:10.1371/journal.pbio.1001661] and may even lead to worse treatment outcomes for them.
Methods have been developed for mitigating some of these problems in genomic studies [@doi:10.1086/512821; @doi:10.1038/nrg2813], but it is not clear how easily they can be adapted for deep models that are designed specifically to extract subtle effects from high-dimensional data.
For example, differences in the equipment that tended to be used for cases versus controls have led to spurious genetic findings (e.g. Sebastiani et al.'s retraction [@doi:10.1126/science.333.6041.404-a]).
In some contexts, it may not be possible to correct for all of these differences to the degree that a deep network is unable to use them.
Moreover, the complexity of deep networks makes it difficult to determine when their predictions are likely to be based on such nominally-irrelevant features of the data (called "leakage" in other fields [@doi:10.1145/2382577.2382579]).
When we are not careful with our data and models, we may inadvertently say more about the way the data was collected (which may involve a history of unequal access and discrimination) than about anything of scientific or predictive value.
This fact can undermine the privacy of patient data [@doi:10.1145/2382577.2382579] or lead to severe discriminatory consequences [@doi:10.1111/j.1740-9713.2016.00960.x].

There is a small but growing literature on the prevention and mitigation of data leakage [@doi:10.1145/2382577.2382579], as well as a closely-related literature on discriminatory model behavior [@arxiv:1610.02413], but it remains difficult to predict when these problems will arise, how to diagnose them, and how to resolve them in practice.
There is even disagreement about which kinds of algorithmic outcomes should be considered discriminatory [@arxiv:1610.09559].
Despite the difficulties and uncertainties, machine learning practitioners (and particularly those who use deep neural networks, which are challenging to interpret) must remain cognizant of these dangers and make every effort to prevent harm from discriminatory predictions.
To reach their potential in this domain, deep learning methods will need to be interpretable (see Discussion).
Researchers need to consider the extent to which biases may be learned by the model and whether or not a model is sufficiently interpretable to identify bias.
We discuss the challenge of model interpretability more thoroughly in Discussion.

#### Applications of deep learning to longitudinal analysis

Longitudinal analysis follows a population across time, for example, prospectively from birth or from the onset of particular conditions.
In large patient populations, longitudinal analyses such as the Framingham Heart Study [@tag:Mahmood] and the Avon Longitudinal Study of Parents and Children [@doi:10.1038/484155a] have yielded important discoveries about the development of disease and the factors contributing to health status.
Yet, a common practice in EHR-based research is to take a snapshot at a point in time and convert patient data to a traditional vector for machine learning and statistical analysis.
This results in loss of information as timing and order of events can provide insight into a patient's disease and treatment [@doi:10.2307/2281868].
Efforts to model sequences of events have shown promise [@doi:10.1038/ncomms5022] but require exceedingly large patient sizes due to discrete combinatorial bucketing.
Lasko et al. [@doi:10.1371/journal.pone.0066341] used autoencoders on longitudinal sequences of serum uric acid measurements to identify population subtypes.
More recently, deep learning has shown promise working with both sequences (CNNs)
[@arxiv:1607.07519] and the incorporation of past and current state (RNNs, LSTMs) [@arxiv:1602.00357].
This may be a particular area of opportunity for deep neural networks.
The ability to recognize relevant sequences of events from a large number of trajectories requires powerful and flexible feature construction methods---an area in which deep neural networks excel.


## Deep learning to study the fundamental biological processes underlying human disease

The study of cellular structure and core biological processes---transcription, translation, signaling, metabolism, etc.---in humans and model organisms will greatly impact our understanding of human disease over the long horizon [@tag:Nih_curiosity].
Predicting how cellular systems respond to environmental perturbations and are altered by genetic variation remain daunting tasks.
Deep learning offers new approaches for modeling biological processes and integrating multiple types of omic data [@doi:10.1038/ncomms13090], which could eventually help predict how these processes are disrupted in disease.
Recent work has already advanced our ability to identify and interpret genetic variants, study microbial communities, and predict protein structures, which also relates to the problems discussed in the drug development section.
In addition, unsupervised deep learning has enormous potential for discovering novel cellular states from gene expression, fluorescence microscopy, and other types of data that may ultimately prove to be clinically relevant.

Progress has been rapid in genomics and imaging, fields where important tasks are readily adapted to well-established deep learning paradigms.
One-dimensional convolutional and recurrent neural networks are well-suited for tasks related to DNA- and RNA-binding proteins, epigenomics, and RNA splicing.
Two dimensional CNNs are ideal for segmentation, feature extraction, and classification in fluorescence microscopy images [@doi:10.3109/10409238.2015.1135868].
Other areas, such as cellular signaling, are biologically important but studied less-frequently to date, with some exceptions [@tag:Chen2015_trans_species].
This may be a consequence of data limitations or greater challenges in adapting neural network architectures to the available data.
Here, we highlight several areas of investigation and assess how deep learning might move these fields forward.

### Gene expression

Gene expression technologies characterize the abundance of many thousands of RNA transcripts within a given organism, tissue, or cell.
This characterization can represent the underlying state of the given system and can be used to study heterogeneity across samples as well as how the system reacts to perturbation.
While gene expression measurements were traditionally made by quantitative polymerase chain reaction (qPCR), low-throughput fluorescence-based methods, and microarray technologies, the field has shifted in recent years to primarily performing RNA sequencing (RNA-seq) to catalog whole transcriptomes.
As RNA-seq continues to fall in price and rise in throughput, sample sizes will increase and training deep models to study gene expression will become even more useful.

Already several deep learning approaches have been applied to gene expression data with varying aims.
For instance, many researchers have applied unsupervised deep learning models to extract meaningful representations of gene modules or sample clusters.
Denoising autoencoders have been used to cluster yeast expression microarrays into known modules representing cell cycle processes [@tag:Gupta2015_exprs_yeast] and to stratify yeast strains based on chemical and mutational perturbations [@tag:Chen2016_exprs_yeast].
Shallow (one hidden layer) denoising autoencoders have also been fruitful in extracting biological insight from thousands of _Pseudomonas aeruginosa_ experiments [@tag:Tan2015_adage; @tag:Tan2016_eadage] and in aggregating features relevant to specific breast cancer subtypes [@tag:Tan2014_psb].
These unsupervised approaches applied to gene expression data are powerful methods for identifying gene signatures that may otherwise be overlooked.
An additional benefit of unsupervised approaches is that ground truth labels, which are often difficult to acquire or are incorrect, are nonessential.
However, the genes that have been aggregated into features must be interpreted carefully.
Attributing each node to a single specific biological function risks over-interpreting models.
Batch effects could cause models to discover non-biological features, and downstream analyses should take this into consideration.

Deep learning approaches are also being applied to gene expression prediction tasks.
For example, a deep neural network with three hidden layers outperformed linear regression in inferring the expression of over 20,000 target genes based on a representative, well-connected set of about 1,000 landmark genes [@tag:Chen2016_gene_expr].
However, while the deep learning model outperformed existing algorithms in nearly every scenario, the model still displayed poor performance.
The paper was also limited by computational bottlenecks that required data to be split randomly into two distinct models and trained separately.
It is unclear how much performance would have increased if not for computational restrictions.

Epigenomic data, combined with deep learning, may have sufficient explanatory power to infer gene expression.
For instance, the DeepChrome CNN [@tag:Singh2016_deepchrome] improved prediction accuracy of high or low gene expression from histone modifications over existing methods.
AttentiveChrome [@tag:Singh2017_attentivechrome] added a deep attention model to further enhance DeepChrome.
Deep learning can also integrate different data types.
For example, Liang et al. combined RBMs to integrate gene expression, DNA methylation, and miRNA data to define ovarian cancer subtypes [@tag:Liang2015_exprs_cancer].
While these approaches are promising, many convert gene expression measurements to categorical or binary variables, thus ablating many complex gene expression signatures present in intermediate and relative numbers.

Deep learning applied to gene expression data is still in its infancy, but the future is bright.
Many previously untestable hypotheses can now be interrogated as deep learning enables analysis of increasing amounts of data generated by new technologies.
For example, the effects of cellular heterogeneity on basic biology and disease etiology can now be explored by single-cell RNA-seq and high-throughput fluorescence-based imaging, techniques we discuss below that will benefit immensely from deep learning approaches.

### DNA methylation

DNA methylation is the process of adding a methyl group to a cytosine in the context of a CpG dinucleotide.
This DNA-level epigenetic modification regulates gene transcription and is critical in development.
Alterations to DNA methylation are well-established as contributing to pathophysiology of many diseases including cancers [@tag:Robertson2005; @tag:Feinberg2018].
Studies of DNA methylation have demonstrated its fundamental role in cell lineage specification starting with stem cell differentiation [@tag:Meissner2008; @tag:Nazor2012] as well as a strong relationship with aging phenotypes [@tag:Kwabi-Addo2007; @tag:Fraga2005] and pathogenesis in response to environmental exposures [@tag:Christensen2009; @tag:Relton2010].

Traditional analytic approaches to DNA methylation data often focus on estimating differential DNA methylation between groups or related with an outcome using linear mixed effects models, so-called epigenome-wide association studies [@tag:Laird2010; @tag:Wilhelm-Benartzi2013; @tag:Liu2013; @tag:Teschendorff2017].
In addition, a growing application of DNA methylation measures is to infer cellular or subject phenotypes from samples and either examine the relation of these phenotypes with outcomes or disease states directly or include them in models as covariates [@tag:Titus2017; @tag:Salas2018_GR; @tag:Zhang2019; @tag:Horvath2014; @tag:Quach2017].
For example, inference of subject age using DNA methylation clock approaches are established [@tag:Horvath2013] and are starting to be applied to test the relation of biological age with disease risk and outcomes [@tag:Kresovich2019].
Different cell types have different DNA methylation profiles.
A novel approach to immunophenotyping combines measurements with reference DNA methylation profiles of leukocytes to infer immune cell type proportions [@tag:Houseman2012; @tag:Salas2018].
This strategy is particularly helpful when only DNA is available from a sample.
Cell type inference is important for adjusting for cell-type composition in epigenome-wide association studies [@tag:Teschendorff2017].
While reference-based libraries have strong predictive value for immune cell type estimation and have broad utility, methods to incorporate estimates of mixtures pose important considerations on the interpretation of underlying biology associated with disease manifestations and phenotypes.
When a reference library is not available, reference-free deconvolution methods [@tag:Houseman2016] that do not rely on these reference libraries are available to decompose signal purported to be contributed by cell types.
However, using reference-free cell type proportion estimates as potential confounders in adjusted models can be overly conservative.
Outcome-associated variation in DNA methylation may be decomposed into putative cell type estimates.
Additional validated reference-based libraries for other tissue types, advancements in reference-free deconvolution methods, and application of deep learning methods are expected to provide new opportunities to understand and interpret DNA methylation in human health and disease.

Deep learning approaches have numerous potential applications for DNA methylation data.
Imputation methods that capture complex interactions between different regions of DNA can expand the number of CpG sites whose DNA methylation state can be studied.
Ideally these methods can derive their own informative, biologically-relevant features.
The primary deep learning methods developed to date focus on: 1) estimating regions of methylation status and imputing missing methylation values, 2) performing classification and regression tasks, and 3) using the latent embeddings of methylation states to derive biologically meaningful features, infer interpolated disease states, and uncover CpG sites that aid the above prediction tasks.

#### Inference, imputation, and prediction

Deep learning approaches are beginning to help address some of the current limitations of feature-by-feature analysis approaches to DNA methylation data and may help uncover additional important features necessary to understand the biological underpinnings behind different pathological states.
One of the more popular applications is imputing the degree of methylation at CpG sites that are within a few thousand base pairs of measured sites or present in similar samples.
DeepSignal employs a CNN to construct features from raw electrical Nanopore signals from sites near a methylated base.
It uses a bidirectional RNN on DNA sequences of the aligned signals to detect methylation [@tag:Ni2018].
DeepCpG applies a similar method using scBS-Seq, DNA sequence, and a bidirectional gated recurrent network [@tag:Angermueller2017].
Methods like MRCNN and DeepMethyl incorporate both sequence and topological structure [@tag:Tian2019; @tag:Khwaja2017; @tag:Wang2016_methyl; @tag:Fu2019].
In addition, gene expression has been used to infer and impute methylation states [@tag:Peng2019; @tag:Levy-Jurgenson2018], methylation of genes can be predicted from promoter methylation [@tag:Pan2018], and convolutional models have been able to predict methylation status from images [@tag:Momeni2018; @tag:Korfiatis2017].
While these examples of methylation imputation and inference methods have value, it is imperative to recognize limitations of imputing cytosine modifications.
Imputing DNA methylation has complexities above and beyond genotype imputation.
Correlation of DNA methylation marks can depend on cell types and other factors that vary by sample.
As the number of tissue types and cell types with whole-genome bisulfite sequencing and oxidative bisulfite sequencing grows, the accuracy of DNA methylation imputation is expected to increase.
While these methods, such as the autoencoder-based DAPL [@tag:Qiu2018], reduce the computational overhead at comparable performance to other popular methylation imputation methods such as k-nearest neighbors, random forests, singular value decomposition, and multiple imputation by chained equations, the software implementations will need to become more user-friendly to gain widespread adoption.

Once DNA methylation is measured, deep learning approaches can also be used to perform classification and regression tasks.
For instance, deep neural networks have been employed on DNA methylation data to predict triglyceride concentrations pre- and post-treatment [@tag:Islam2018; @tag:Darst2018] and differentiate cancer subtypes [@tag:Chatterjee2018; @tag:Khwaja2018] better than other methods such as support vector machines (SVMs).
Modular approaches to methylation prediction, such as MethylNet, have been able to predict age, cellular proportions, and cancer subtypes, outperforming SVM and elastic net models while remaining concordant with expected biology [@tag:Levy2019].
These approaches aim to make embedding, hyperparameter selection, regression, classification, and model interpretation tasks more tractable for epigenetics researchers and machine learning scientists.

####  Latent space construction

Unsupervised discovery of biologically-significant features is another major area of interest for researchers using DNA methylation data.
A consistent theme of these methods is that they construct a low-dimensional space that semantically encodes biologically important features from methylation profiles.
As with other applications, these low-dimensional representations are thought to capture a set of important, unmeasured sources of biological variability in the data.
Projection into these spaces results in biologically-similar examples being close together.
For this reason, they are often termed latent spaces.
One method used several stacked binary RBMs to learn a low-dimensional subspace representation of the methylation profiles of 5,000 CpG sites with the highest variance across 136 breast tissue samples, 113 breast cancer samples, and 23 non-cancerous samples.
Samples in the latent space were clustered via self-organizing maps to show that the latent space could differentiate breast cancer samples from non-neoplastic samples.
Furthermore, the latent space was visualized using t-Distributed Stochastic Neighbor Embedding (t-SNE) [@tag:Maaten2008_tsne; @arxiv:1808.01359].
Titus et al. [@doi:10.5220/0006636401400145] adapted a VAE strategy developed by Way et al. [@doi:10.1142/9789813235533_0008] to methylation data.
The VAE was modified to perform dimensionality reduction on 300,000 PAM50-assigned CpG features to 100 latent features in 862 samples.
The authors performed t-SNE visualization, clustering, and tumor subtype classification from a TCGA breast cancer dataset.
In an subsequent extension [@doi:10.1101/433763], the authors constructed a 100-dimensional latent space of 100,000 CpG sites across approximately 1,200 samples.
They selected latent space dimensions that were the most highly associated with the differentiation between estrogen receptor (ER) positive and negative tumor samples in breast cancer patients to determine the extent to which the latent space could predict responses to endocrine therapy.
Certain latent space dimensions differentiated tumors based on their ER status and provided biologically-plausible hypotheses, which suggests that VAE-derived models may have a place in summarizing DNA methylation profiles into composite features that can aid in predicting treatment response.
Another study explored the latent features of lung cancer methylation profiles that were extracted using VAEs.
After constructing a latent space representations of TCGA lung cancer samples, the authors used a logistic regression classifier on the latent dimensions to accurately classify cancer subtypes [@doi:10.1109/BIBM.2018.8621365].
These studies, along with the growing body of work using VAEs and other latent representations of genomic and epigenomic data demonstrate a suite of tools to explore the unmeasured aspects of biology.
Techniques that produce these representations provide the opportunity to discover important biological features that were previously missed.
The power of unsupervised deep learning models for this task comes from their ability to learn high-dimensional non-linear relationships among data.

Important applications in the future include predicting methylation and pathological states based on methylation profiles uncovered from datasets with more noise, such as solid tissue samples.
Unsupervised deep learning approaches such as VAEs may provide a more complete understanding of the biological processes underlying cell types, transitions in cell dynamics, and subject phenotypes.
In addition, latent representations may assist with biological hypothesis generation and have the ability to stratify patients by predicted risk.
While neural network embeddings can outperform traditional embeddings, it is important to be aware that many of these methods can be highly sensitive to hyperparameter tuning and an evaluation of the impact of hyperparameter tuning should be included [@doi:10.1101/385534].

### Splicing

Pre-mRNA transcripts can be spliced into different isoforms by retaining or skipping subsets of exons or including parts of introns, creating enormous spatiotemporal flexibility to generate multiple distinct proteins from a single gene.
This remarkable complexity can lend itself to defects that underlie many diseases.
For instance, splicing mutations in the lamin A (*LMNA*) gene can lead to specific variants of dilated cardiomyopathy and limb girdle muscular dystrophy [@tag:Scotti2016_missplicing].
A recent study found that quantitative trait loci that affect splicing in lymphoblastoid cell lines are enriched within risk loci for schizophrenia, multiple sclerosis, and other immune diseases, implicating mis-splicing as a more widespread feature of human pathologies than previously thought [@tag:Li2016_variation].
Therapeutic strategies that aim to modulate splicing are also currently being considered for disorders such as Duchenne muscular dystrophy and spinal muscular atrophy [@tag:Scotti2016_missplicing].

Sequencing studies routinely return thousands of unannotated variants, but which cause functional changes in splicing and how are those changes manifested?
Prediction of a "splicing code" has been a goal of the field for the past decade.
Initial machine learning approaches used a naïve Bayes model and a 2-layer Bayesian neural network with thousands of hand-derived sequence-based features to predict the probability of exon skipping [@tag:Barash2010_splicing_code; @tag:Xiong2011_bayesian].
With the advent of deep learning, more complex models provided better predictive accuracy [@tag:Xiong2015_splicing_code; @tag:Jha2017_integrative_models].
Importantly, these new approaches can take in multiple kinds of epigenomic measurements as well as tissue identity and RNA binding partners of splicing factors.
Deep learning is critical in furthering these kinds of integrative studies where different data types and inputs interact in unpredictable (often nonlinear) ways to create higher-order features.
Moreover, as in gene expression network analysis, interrogating the hidden nodes within neural networks could potentially illuminate important aspects of splicing behavior.
For instance, tissue-specific splicing mechanisms could be inferred by training networks on splicing data from different tissues, then searching for common versus distinctive hidden nodes, a technique employed by Qin et al. for tissue-specific transcription factor (TF) binding predictions [@tag:Qin2017_onehot].

A parallel effort has been to use more data with simpler models.
An exhaustive study using readouts of splicing for millions of synthetic intronic sequences uncovered motifs that influence the strength of alternative splice sites [@tag:Rosenberg2015_synthetic_seqs].
The authors built a simple linear model using hexamer motif frequencies that successfully generalized to exon skipping.
In a limited analysis using single nucleotide polymorphisms (SNPs) from three genes, it predicted exon skipping with three times the accuracy of an existing deep learning-based framework [@tag:Xiong2015_splicing_code].
This case is instructive in that clever sources of data, not just more descriptive models, are still critical.

We already understand how mis-splicing of a single gene can cause diseases such as limb girdle muscular dystrophy.
The challenge now is to uncover how genome-wide alternative splicing underlies complex, non-Mendelian diseases such as autism, schizophrenia, Type 1 diabetes, and multiple sclerosis [@tag:JuanMateu2016_t1d].
As a proof of concept, Xiong et al. [@tag:Xiong2015_splicing_code] sequenced five autism spectrum disorder and 12 control samples, each with an average of 42,000 rare variants, and identified mis-splicing in 19 genes with neural functions.
Such methods may one day enable scientists and clinicians to rapidly profile thousands of unannotated variants for functional effects on splicing and nominate candidates for further investigation.
Moreover, these nonlinear algorithms can deconvolve the effects of multiple variants on a single splice event without the need to perform combinatorial *in vitro* experiments.
The ultimate goal is to predict an individual’s tissue-specific, exon-specific splicing patterns from their genome sequence and other measurements to enable a new branch of precision diagnostics that also stratifies patients and suggests targeted therapies to correct splicing defects.
However, to achieve this we expect that methods to interpret the "black box" of deep neural networks and integrate diverse data sources will be required.

### Transcription factors

Transcription factors are proteins that bind regulatory DNA in a sequence-specific manner to modulate the activation and repression of gene transcription.
High-throughput *in vitro* experimental assays that quantitatively measure the binding specificity of a TF to a large library of short oligonucleotides [@doi:10.1016/j.tibs.2014.07.002] provide rich datasets to model the naked DNA sequence affinity of individual TFs in isolation.
However, *in vivo* TF binding is affected by a variety of other factors beyond sequence affinity, such as competition and cooperation with other TFs, TF concentration, and chromatin state (chemical modifications to DNA and other packaging proteins that DNA is wrapped around) [@doi:10.1016/j.tibs.2014.07.002].
TFs can thus exhibit highly variable binding landscapes across the same genomic DNA sequence across diverse cell types and states.
Several experimental approaches such as chromatin immunoprecipitation followed by sequencing (ChIP-seq) have been developed to profile *in vivo* binding maps of TFs [@doi:10.1016/j.tibs.2014.07.002].
Large reference compendia of ChIP-seq data are now freely available for a large collection of TFs in a small number of reference cell states in humans and a few other model organisms [@tag:Consortium2012_encode].
Due to fundamental material and cost constraints, it is infeasible to perform these experiments for all TFs in every possible cellular state and species.
Hence, predictive computational models of TF binding are essential to understand gene regulation in diverse cellular contexts.

Several machine learning approaches have been developed to learn generative and discriminative models of TF binding from *in vitro* and *in vivo* TF binding datasets that associate collections of synthetic DNA sequences or genomic DNA sequences to binary labels (bound/unbound) or continuous measures of binding.
The most common class of TF binding models in the literature are those that only model the DNA sequence affinity of TFs from *in vitro* and *in vivo* binding data.
The earliest models were based on deriving simple, compact, interpretable sequence motif representations such as position weight matrices (PWMs) and other biophysically inspired models [@tag:Stormo2000_dna; @doi:10.1093/nar/gkp335; @doi:10.1038/nbt.2486].
These models were outperformed by general k-mer based models including SVMs with string kernels [@doi:10.1371/journal.pcbi.1000916; @tag:Ghandi2014_enhanced].

In 2015, Alipanahi et al. developed DeepBind, the first CNN to classify bound DNA sequences based on *in vitro* and *in vivo* assays against random DNA sequences matched for dinucleotide sequence composition [@tag:Alipanahi2015_predicting].
The convolutional layers learn pattern detectors reminiscent of PWMs from a one-hot encoding of the raw input DNA sequences.
DeepBind outperformed several state-of-the-art methods from the DREAM5 *in vitro* TF-DNA motif recognition challenge [@doi:10.1038/nbt.2486].
Although DeepBind was also applied to RNA-binding proteins, in general RNA binding is a separate problem [@doi:10.1186/s12859-017-1561-8] and accurate models will need to account for RNA secondary structure.
Following DeepBind, several optimized convolutional and recurrent neural network architectures as well as novel hybrid approaches that combine kernel methods with neural networks have been proposed that further improve performance [@tag:Zeng2016_convolutional; @tag:Lanchantin2016_motif; @arxiv:1706.00125; @doi:10.1101/217257].
Specialized layers and regularizers have also been proposed to reduce parameters and learn more robust models by taking advantage of specific properties of DNA sequences such as their reverse complement equivalence [@tag:Shrikumar2017_reversecomplement; @doi:10.1101/146431].

While most of these methods learn independent models for different TFs, *in vivo* multiple TFs compete or cooperate to occupy DNA binding sites, resulting in complex combinatorial co-binding landscapes.
To take advantage of this shared structure in *in vivo* TF binding data, multi-task neural network architectures have been developed that explicitly share parameters across models for multiple TFs [@tag:Zhou2015_deep_sea; @doi:10.1093/nar/gkw226; @doi:10.1101/217257].
Some of these multi-task models train and evaluate classification performance relative to an unbound background set of regulatory DNA sequences sampled from the genome rather than using synthetic background sequences with matched dinucleotide composition.

The above-mentioned TF binding prediction models that use only DNA sequences as inputs have a fundamental limitation.
Because the DNA sequence of a genome is the same across different cell types and states, a sequence-only model of TF binding cannot predict different *in vivo* TF binding landscapes in new cell types not used during training.
One approach for generalizing TF binding predictions to new cell types is to learn models that integrate DNA sequence inputs with other cell-type-specific data modalities that modulate *in vivo* TF binding such as surrogate measures of TF concentration (e.g. TF gene expression) and chromatin state.
Arvey et al. showed that combining the predictions of SVMs trained on DNA sequence inputs and cell-type specific DNase-seq data, which measures genome-wide chromatin accessibility, improved *in vivo* TF binding prediction within and across cell types [@doi:10.1101/gr.127712.111].
Several "footprinting" based methods have also been developed that learn to discriminate bound from unbound instances of known canonical motifs of a target TF based on high-resolution footprint patterns of chromatin accessibility that are specific to the target TF [@doi:10.1038/nmeth.3772].
However, the genome-wide predictive performance of these methods in new cell types and states has not been evaluated.

Recently, a community challenge known as the "ENCODE-DREAM *in vivo* TF Binding Site Prediction Challenge" was introduced to systematically evaluate genome-wide performance of methods that can predict TF binding across cell states by integrating DNA sequence and *in vitro* DNA shape with cell-type-specific chromatin accessibility and gene expression [@tag:Dream_tf_binding].
A deep learning model called FactorNet was amongst the top three performing methods in the challenge [@tag:Quang2017_factor].
FactorNet uses a multi-modal hybrid convolutional and recurrent architecture that integrates DNA sequence with chromatin accessibility profiles, gene expression, and evolutionary conservation of sequence.
It is worth noting that FactorNet was slightly outperformed by an approach that does not use neural networks [@doi:10.1101/230011].
This top ranking approach uses an extensive set of curated features in a weighted variant of a discriminative maximum conditional likelihood model in combination with a novel iterative training strategy and model stacking.
There appears to be significant room for improvement because none of the current approaches for cross cell type prediction explicitly account for the fact that TFs can co-bind with distinct co-factors in different cell states.
In such cases, sequence features that are predictive of TF binding in one cell state may be detrimental to predicting binding in another.

Singh et al. developed transfer string kernels for SVMs for cross-context TF binding [@tag:Singh2016_tsk].
Domain adaptation methods that allow training neural networks which are transferable between differing training and test set distributions of sequence features could be a promising avenue going forward [@arxiv:1502.02791; @arxiv:1505.07818].
These approaches may also be useful for transferring TF binding models across species.

Another class of imputation-based cross cell type *in vivo* TF binding prediction methods leverage the strong correlation between combinatorial binding landscapes of multiple TFs.
Given a partially complete panel of binding profiles of multiple TFs in multiple cell types, a deep learning method called TFImpute learns to predict the missing binding profile of a target TF in some target cell type in the panel based on the binding profiles of other TFs in the target cell type and the binding profile of the target TF in other cell types in the panel [@tag:Qin2017_onehot].
However, TFImpute cannot generalize predictions beyond the training panel of cell types and requires TF binding profiles of related TFs.

It is worth noting that TF binding prediction methods in the literature based on neural networks and other machine learning approaches choose to sample the set of bound and unbound sequences in a variety of different ways.
These choices and the choice of performance evaluation measures significantly confound systematic comparison of model performance (see Discussion).

Several methods have also been developed to interpret neural network models of TF binding.
Alipanahi et al. visualize convolutional filters to obtain insights into the sequence preferences of TFs [@tag:Alipanahi2015_predicting].
They also introduced *in silico* mutation maps for identifying important predictive nucleotides in input DNA sequences by exhaustively forward propagating perturbations to individual nucleotides to record the corresponding change in output prediction.
Shrikumar et al. [@tag:Shrikumar2017_learning] proposed efficient backpropagation based approaches to simultaneously score the contribution of all nucleotides in an input DNA sequence to an output prediction.
Lanchantin et al. [@tag:Lanchantin2016_motif] developed tools to visualize TF motifs learned from TF binding site classification tasks.
These and other general interpretation techniques (see Discussion) will be critical to improve our understanding of the biologically meaningful patterns learned by deep learning models of TF binding.

### Promoters and enhancers

#### From TF binding to promoters and enhancers

Multiple TFs act in concert to coordinate changes in gene regulation at the genomic regions known as promoters and enhancers.
Each gene has an upstream promoter, essential for initiating that gene's transcription.
The gene may also interact with multiple enhancers, which can amplify transcription in particular cellular contexts.
These contexts include different cell types in development or environmental stresses.

Promoters and enhancers provide a nexus where clusters of TFs and binding sites mediate downstream gene regulation, starting with transcription.
The gold standard to identify an active promoter or enhancer requires demonstrating its ability to affect transcription or other downstream gene products.
Even extensive biochemical TF binding data has thus far proven insufficient on its own to accurately and comprehensively locate promoters and enhancers.
We lack sufficient understanding of these elements to derive a mechanistic "promoter code" or "enhancer code".
But extensive labeled data on promoters and enhancers lends itself to probabilistic classification.
The complex interplay of TFs and chromatin leading to the emergent properties of promoter and enhancer activity seems particularly apt for representation by deep neural networks.

#### Promoters

Despite decades of work, computational identification of promoters remains a stubborn problem [@doi:10.1093/bib/4.1.22].
Researchers have used neural networks for promoter recognition as early as 1996 [@tag:matis].
Recently, a CNN recognized promoter sequences with sensitivity and specificity exceeding 90% [@doi:10.1371/journal.pone.0171410].
Most activity in computational prediction of regulatory regions, however, has moved to enhancer identification.
Because one can identify promoters with straightforward biochemical assays [@doi:10.1073/pnas.2136655100; @doi:10.1101/gr.110254.110], the direct rewards of promoter prediction alone have decreased.
But the reliable ground truth provided by these assays makes promoter identification an appealing test bed for deep learning approaches that can also identify enhancers.

#### Enhancers

Recognizing enhancers presents additional challenges.
Enhancers may be up to 1,000,000 bp away from the affected promoter, and even within introns of other genes [@doi:10.1038/nrg3458].
Enhancers do not necessarily operate on the nearest gene and may affect multiple genes.
Their activity is frequently tissue- or context-specific.
No biochemical assay can reliably identify all enhancers.
Distinguishing them from other regulatory elements remains difficult, and some believe the distinction somewhat artificial [@doi:10.1016/j.tig.2015.05.007].
While these factors make the enhancer identification problem more difficult, they also make a solution more valuable.

Several neural network approaches yielded promising results in enhancer prediction.
Both Basset [@doi:10.1101/gr.200535.115] and DeepEnhancer [@tag:Min2016_deepenhancer] used CNNs to predict enhancers.
DECRES used a feed-forward neural network [@doi:10.1101/041616] to distinguish between different kinds of regulatory elements, such as active enhancers, and promoters.
DECRES had difficulty distinguishing between inactive enhancers and promoters.
They also investigated the power of sequence features to drive classification, finding that beyond CpG islands, few were useful.

Comparing the performance of enhancer prediction methods illustrates the problems in using metrics created with different benchmarking procedures.
Both the Basset and DeepEnhancer studies include comparisons to a baseline SVM approach, gkm-SVM [@doi:10.1371/journal.pcbi.1003711].
The Basset study reports gkm-SVM attains a mean area under the precision-recall curve (AUPR) of 0.322 over 164 cell types [@doi:10.1101/gr.200535.115].
The DeepEnhancer study reports for gkm-SVM a dramatically different AUPR of 0.899 on nine cell types [@tag:Min2016_deepenhancer].
This large difference means it's impossible to directly compare the performance of Basset and DeepEnhancer based solely on their reported metrics.
DECRES used a different set of metrics altogether.
To drive further progress in enhancer identification, we must develop a common and comparable benchmarking procedure (see Discussion).

#### Promoter-enhancer interactions

In addition to the location of enhancers, identifying enhancer-promoter interactions in three-dimensional space will provide critical knowledge for understanding transcriptional regulation.
SPEID used a CNN to predict these interactions with only sequence and the location of putative enhancers and promoters along a one-dimensional chromosome [@doi:10.1101/085241].
It compared well to other methods using a full complement of biochemical data from ChIP-seq and other epigenomic methods.
Of course, the putative enhancers and promoters used were themselves derived from epigenomic methods.
But one could easily replace them with the output of one of the enhancer or promoter prediction methods above.

### Micro-RNA binding

Prediction of microRNAs (miRNAs) and miRNA targets is of great interest, as they are critical components of gene regulatory networks and are often conserved across great evolutionary distance [@tag:Bracken2016_mirna; @tag:Berezikov2011_mirna].
While many machine learning algorithms have been applied to these tasks, they currently require extensive feature selection and optimization.
For instance, one of the most widely adopted tools for miRNA target prediction, TargetScan, trained multiple linear regression models on 14 hand-curated features including structural accessibility of the target site on the mRNA, the degree of site conservation, and predicted thermodynamic stability of the miRNA-mRNA complex [@tag:Agarwal2015_targetscan].
Some of these features, including structural accessibility, are imperfect or empirically derived.
In addition, current algorithms suffer from low specificity [@tag:Lee2016_deeptarget].

As in other applications, deep learning promises to achieve equal or better performance in predictive tasks by automatically engineering complex features to minimize an objective function.
Two recently published tools use different recurrent neural network-based architectures to perform miRNA and target prediction with solely sequence data as input [@tag:Park2016_deepmirgene; @tag:Lee2016_deeptarget].
Though the results are preliminary and still based on a validation set rather than a completely independent test set, they were able to predict microRNA target sites with higher specificity and sensitivity than TargetScan.
Excitingly, these tools seem to show that RNNs can accurately align sequences and predict bulges, mismatches, and wobble base pairing without requiring the user to input secondary structure predictions or thermodynamic calculations.
Further incremental advances in deep learning for miRNA and target prediction will likely be sufficient to meet the current needs of systems biologists and other researchers who use prediction tools mainly to nominate candidates that are then tested experimentally.

### Protein secondary and tertiary structure

Proteins play fundamental roles in almost all biological processes, and understanding their structure is critical for basic biology and drug development.
UniProt currently has about 94 million protein sequences, yet fewer than 100,000 proteins across all species have experimentally-solved structures in Protein Data Bank (PDB).
As a result, computational structure prediction is essential for a majority of proteins.
However, this is very challenging, especially when similar solved structures, called templates, are not available in PDB.
Over the past several decades, many computational methods have been developed to predict aspects of protein structure such as secondary structure, torsion angles, solvent accessibility, inter-residue contact maps, disorder regions, and side-chain packing.
In recent years, multiple deep learning architectures have been applied, including deep belief networks, LSTMs, CNNs, and deep convolutional neural fields (DeepCNFs)
[@doi:10.1007/978-3-319-46227-1_1; @doi:10.1038/srep18962].

Here we focus on deep learning methods for two representative sub-problems: secondary structure prediction and contact map prediction.
Secondary structure refers to local conformation of a sequence segment, while a contact map contains information on all residue-residue contacts.
Secondary structure prediction is a basic problem and an almost essential module of any protein structure prediction package.
Contact prediction is much more challenging than secondary structure prediction, but it has a much larger impact on tertiary structure prediction.
In recent years, the accuracy of contact prediction has greatly improved [@doi:10.1371/journal.pcbi.1005324; @doi:10.1093/bioinformatics/btu791; @doi:10.1073/pnas.0805923106; @doi:10.1371/journal.pone.0028766].

One can represent protein secondary structure with three different states (alpha helix, beta strand, and loop regions) or eight finer-grained states.
Accuracy of a three-state prediction is called Q3, and accuracy of an 8-state prediction is called Q8.
Several groups [@doi:10.1371/journal.pone.0032235; @doi:10.1109/TCBB.2014.2343960; @doi:10.1038/srep11476] applied deep learning to protein secondary structure prediction but were unable to achieve significant improvement over the *de facto* standard method PSIPRED [@doi:10.1006/jmbi.1999.3091], which uses two shallow feedforward neural networks.
In 2014, Zhou and Troyanskaya demonstrated that they could improve Q8 accuracy by using a deep supervised and convolutional generative stochastic network [@arxiv:1403.1347].
In 2016 Wang et al. developed a DeepCNF model that improved Q3 and Q8 accuracy as well as prediction of solvent accessibility and disorder regions [@doi:10.1038/srep18962; @doi:10.1007/978-3-319-46227-1_1].
DeepCNF achieved a higher Q3 accuracy than the standard maintained by PSIPRED for more than 10 years.
This improvement may be mainly due to the ability of convolutional neural fields to capture long-range sequential information, which is important for beta strand prediction.
Nevertheless, the improvements in secondary structure prediction from DeepCNF are unlikely to result in a commensurate improvement in tertiary structure prediction since secondary structure mainly reflects coarse-grained local conformation of a protein structure.

Protein contact prediction and contact-assisted folding (i.e. folding proteins using predicted contacts as restraints) represents a promising new direction for
*ab initio* folding of proteins without good templates in PDB.
Co-evolution analysis is effective for proteins with a very large number (>1000) of sequence homologs [@doi:10.1371/journal.pone.0028766], but fares poorly for proteins without many sequence homologs.
By combining co-evolution information with a few other protein features, shallow neural network methods such as MetaPSICOV [@doi:10.1093/bioinformatics/btu791] and CoinDCA-NN [@doi:10.1093/bioinformatics/btv472] have shown some advantage over pure co-evolution analysis for proteins with few sequence homologs, but their accuracy is still far from satisfactory.
In recent years, deeper architectures have been explored for contact prediction, such as CMAPpro [@doi:10.1093/bioinformatics/bts475], DNCON [@doi:10.1093/bioinformatics/bts598] and PConsC [@doi:10.1371/journal.pcbi.1003889].
However, blindly tested in the well-known CASP competitions, these methods did not show any advantage over MetaPSICOV [@doi:10.1093/bioinformatics/btu791].

Recently, Wang et al. proposed the deep learning method RaptorX-Contact [@doi:10.1371/journal.pcbi.1005324], which significantly improves contact prediction over MetaPSICOV and pure co-evolution methods, especially for proteins without many sequence homologs. It employs a network architecture formed by one 1D residual neural network and one 2D residual neural network.
Blindly tested in the latest CASP competition (i.e. CASP12 [@url:http://www.predictioncenter.org/casp12/rrc_avrg_results.cgi]), RaptorX-Contact ranked first in F₁ score on free-modeling targets as well as the whole set of targets.
In CAMEO (which can be interpreted as a fully-automated CASP) [@url:https://www.cameo3d.org], its predicted contacts were also able to fold proteins with a novel fold and only 65--330 sequence homologs.
This technique also worked well on membrane proteins even when trained on non-membrane proteins [@arxiv:1704.07207].
RaptorX-Contact performed better mainly due to introduction of residual neural networks and exploitation of contact occurrence patterns by simultaneously predicting all the contacts in a single protein.

Taken together, *ab initio* folding is becoming much easier with the advent of direct evolutionary coupling analysis and deep learning techniques.
We expect further improvements in contact prediction for proteins with fewer than 1000 homologs by studying new deep network architectures.
The deep learning methods summarized above also apply to interfacial contact prediction for protein complexes but may be less effective since on average protein complexes have fewer sequence homologs.
Beyond secondary structure and contact maps, we anticipate increased attention to predicting 3D protein structure directly from amino acid sequence and single residue evolutionary information [@doi:10.1101/265231].

### Structure determination and cryo-electron microscopy

Complementing computational prediction approaches, cryo-electron microscopy (cryo-EM) allows near-atomic resolution determination of protein models by comparing individual electron micrographs [@doi:10.1016/j.cell.2015.03.049].
Detailed structures require tens of thousands of protein images [@doi:10.1016/j.cell.2015.03.050].
Technological development has increased the throughput of image capture.
New hardware, such as direct electron detectors, has made large-scale image production practical, while new software has focused on rapid, automated image processing.

Some components of cryo-EM image processing remain difficult to automate.
For instance, in particle picking, micrographs are scanned to identify individual molecular images that will be used in structure refinement.
In typical applications, hundreds of thousands of particles are necessary to determine a structure to near atomic resolution, making manual selection impractical [@doi:10.1016/j.cell.2015.03.050].
Typical selection approaches are semi-supervised; a user will select several particles manually, and these selections will be used to train a classifier [@doi:10.1016/j.jsb.2006.04.006; @doi:10.1016/j.jsb.2014.11.010].
Now CNNs are being used to select particles in tools like DeepPicker [@doi:10.1016/j.jsb.2016.07.006] and DeepEM [@doi:10.1186/s12859-017-1757-y].
In addition to addressing shortcomings from manual selection, such as selection bias and poor discrimination of low-contrast images, these approaches also provide a means of full automation.
DeepPicker can be trained by reference particles from other experiments with structurally unrelated macromolecules, allowing for fully automated application to new samples.

Downstream of particle picking, deep learning is being applied to other aspects of cryo-EM image processing.
Statistical manifold learning has been implemented in the software package ROME to classify selected particles and elucidate the different conformations of the subject molecule necessary for accurate 3D structures [@doi:10.1371/journal.pone.0182130].
These recent tools highlight the general applicability of deep learning approaches for image processing to increase the throughput of high-resolution cryo-EM.

### Protein-protein interactions

Protein-protein interactions (PPIs) are highly specific and non-accidental physical contacts between proteins, which occur for purposes other than generic protein production or degradation [@doi:10.1371/journal.pcbi.1000807].
Abundant interaction data have been generated in-part thanks to advances in high-throughput screening methods, such as yeast two-hybrid and affinity-purification with mass spectrometry.
However, because many PPIs are transient or dependent on biological context, high-throughput methods can fail to capture a number of interactions.
The imperfections and costs associated with many experimental PPI screening methods have motivated an interest in high-throughput computational prediction.

Many machine learning approaches to PPI have focused on text mining the literature [@doi:10.1016/j.jbi.2007.11.008; @arxiv:1706.01556v2], but these approaches can fail to capture context-specific interactions, motivating *de novo* PPI prediction.
Early *de novo* prediction approaches used a variety of statistical and machine learning tools on structural and sequential data, sometimes with reference to the existing body of protein structure knowledge.
In the context of PPIs---as in other domains---deep learning shows promise both for exceeding current predictive performance and for circumventing limitations from which other approaches suffer.

One of the key difficulties in applying deep learning techniques to binding prediction is the task of representing peptide and protein sequences in a meaningful way.
DeepPPI [@doi:10.1021/acs.jcim.7b00028] made PPI predictions from a set of sequence and composition protein descriptors using a two-stage deep neural network that trained two subnetworks for each protein and combined them into a single network.
Sun et al. [@doi:10.1186/s12859-017-1700-2] applied autocovariances, a coding scheme that returns uniform-size vectors describing the covariance between physicochemical properties of the protein sequence at various positions.
Wang et al. [@doi:10.1039/C7MB00188F] used deep learning as an intermediate step in PPI prediction.
They examined 70 amino acid protein sequences from each of which they extracted 1260 features.
A stacked sparse autoencoder with two hidden layers was then used to reduce feature dimensions and noisiness before a novel type of classification vector machine made PPI predictions.

Beyond predicting whether or not two proteins interact, Du et al. [@doi:10.1016/j.ymeth.2016.06.001] employed a deep learning approach to predict the residue contacts between two interacting proteins.
Using features that describe how similar a protein's residue is relative to similar proteins at the same position, the authors extracted uniform-length features for each residue in the protein sequence.
A stacked autoencoder took two such vectors as input for the prediction of contact between two residues.
The authors evaluated the performance of this method with several classifiers and showed that a deep neural network classifier paired with the stacked autoencoder significantly exceeded classical machine learning accuracy.

Because many studies used predefined higher-level features, one of the benefits of deep learning---automatic feature extraction---is not fully leveraged.
More work is needed to determine the best ways to represent raw protein sequence information so that the full benefits of deep learning as an automatic feature extractor can be realized.

### MHC-peptide binding

An important type of PPI involves the immune system's ability to recognize the body's own cells.
The major histocompatibility complex (MHC) plays a key role in regulating this process by binding antigens and displaying them on the cell surface to be recognized by T cells.
Due to its importance in immunity and immune response, peptide-MHC binding prediction is a useful problem in computational biology, and one that must account for the allelic diversity in MHC-encoding gene region.

Shallow, feed-forward neural networks are competitive methods and have made progress toward pan-allele and pan-length peptide representations.
Sequence alignment techniques are useful for representing variable-length peptides as uniform-length features [@doi:10.1110/ps.0239403; @doi:10.1093/bioinformatics/btv639].
For pan-allelic prediction, NetMHCpan [@doi:10.1007/s00251-008-0341-z; @doi:10.1186/s13073-016-0288-x] used a pseudo-sequence representation of the MHC class I molecule, which included only polymorphic peptide contact residues.
The sequences of the peptide and MHC were then represented using both sparse vector encoding and Blosum encoding, in which amino acids are encoded by matrix score vectors.
A comparable method to the NetMHC tools is MHCflurry [@doi:10.1101/174243], a method which shows superior performance on peptides of lengths other than nine.
MHCflurry adds placeholder amino acids to transform variable-length peptides to length 15 peptides.
In training the MHCflurry feed-forward neural network [@doi:10.1101/054775], the authors imputed missing MHC-peptide binding affinities using a Gibbs sampling method, showing that imputation improves performance for data-sets with roughly 100 or fewer training examples.
MHCflurry's imputation method increases its performance on poorly characterized alleles, making it competitive with NetMHCpan for this task.
Kuksa et al. [@doi:10.1093/bioinformatics/btv371] developed a shallow, higher-order neural network (HONN) comprised of both mean and covariance hidden units to capture some of the higher-order dependencies between amino acid locations.
Pre-training this HONN with a semi-restricted Boltzmann machine, the authors found that the performance of the HONN exceeded that of a simple deep neural network, as well as that of NetMHC.

Deep learning's unique flexibility was recently leveraged by Bhattacharya et al. [@doi:10.1101/154757], who used a gated RNN method called MHCnuggets to overcome the difficulty of multiple peptide lengths.
Under this framework, they used smoothed sparse encoding to represent amino acids individually.
Because MHCnuggets had to be trained for every MHC allele, performance was far better for alleles with abundant, balanced training data.
Vang et al. [@doi:10.1093/bioinformatics/btx264] developed HLA-CNN, a method which maps amino acids onto a 15-dimensional vector space based on their context relation to other amino acids before making predictions with a CNN.
In a comparison of several current methods, Bhattacharya et al. found that the top methods---NetMHC, NetMHCpan, MHCflurry, and MHCnuggets---showed comparable performance, but large differences in speed.
Convolutional neural networks (in this case, HLA-CNN) showed comparatively poor performance, while shallow and recurrent neural networks performed the best.
They found that MHCnuggets---the recurrent neural network---was by far the fastest-training among the top performing methods.

### PPI networks and graph analysis

Because interacting proteins are more likely to share a similar function, the connectivity of a PPI network itself can be a valuable information source for the prediction of protein function [@doi:10.1038/msb4100129].
To incorporate higher-order network information, it is necessary to find a lower-level embedding of network structure that preserves this higher-order structure.
Rather than use hand-crafted network features, deep learning shows promise for the automatic discovery of predictive features within networks.
For example, Navlakha [@doi:10.1162/NECO_a_00924] showed that a deep autoencoder was able to compress a graph to 40% of its original size, while being able to reconstruct 93% of the original graph's edges, improving upon standard dimension reduction methods.
To achieve this, each graph was represented as an adjacency matrix with rows sorted in descending node degree order, then flattened into a vector and given as input to the autoencoder.
While the activity of some hidden layers correlated with several popular hand-crafted network features such as k-core size and graph density, this work showed that deep learning can effectively reduce graph dimensionality while retaining much of its structural information.

An important challenge in PPI network prediction is the task of combining different networks and types of networks.
Gligorijevic et al. [@doi:10.1101/223339] developed a multimodal deep autoencoder, deepNF, to find a feature representation common among several different PPI networks.
This common lower-level representation allows for the combination of various PPI data sources towards a single predictive task.
An SVM classifier trained on the compressed features from the middle layer of the autoencoder outperformed previous methods in predicting protein function.

Hamilton et al. addressed the issue of large, heterogeneous, and changing networks with an inductive approach called GraphSAGE [@arxiv:1706.02216v2].
By finding node embeddings through learned aggregator functions that describe the node and its neighbors in the network, the GraphSAGE approach allows for the generalization of the model to new graphs.
In a classification task for the prediction of protein function, Chen and Zhu [@arxiv:1710.10568v1] optimized this approach and enhanced the graph convolutional network with a preprocessing step that uses an approximation to the dropout operation.
This preprocessing effectively reduces the number of graph convolutional layers and it significantly improves both training time and prediction accuracy.

### Morphological phenotypes

A field poised for dramatic revolution by deep learning is bioimage analysis.
Thus far, the primary use of deep learning for biological images has been for segmentation---that is, for the identification of biologically relevant structures in images such as nuclei, infected cells, or vasculature---in fluorescence or even brightfield channels [@doi:10.1371/journal.pcbi.1005177].
Once so-called regions of interest have been identified, it is often straightforward to measure biological properties of interest, such as fluorescence intensities, textures, and sizes.
Given the dramatic successes of deep learning in biological imaging, we simply refer to articles that review recent advancements [@doi:10.3109/10409238.2015.1135868; @doi:10.1371/journal.pcbi.1005177; @doi:10.1007/978-3-319-24574-4_28].
However, user-friendly tools must be developed for deep learning to become commonplace for biological image segmentation.

We anticipate an additional paradigm shift in bioimaging that will be brought about by deep learning: what if images of biological samples, from simple cell cultures to three-dimensional organoids and tissue samples, could be mined for much more extensive biologically meaningful information than is currently standard? For example, a recent study demonstrated the ability to predict lineage fate in hematopoietic cells up to three generations in advance of differentiation [@doi:10.1038/nmeth.4182].
In biomedical research, most often biologists decide in advance what feature to measure in images from their assay system.
Although classical methods of segmentation and feature extraction can produce hundreds of metrics per cell in an image, deep learning is unconstrained by human intuition and can in theory extract more subtle features through its hidden nodes.
Already, there is evidence deep learning can surpass the efficacy of classical methods [@doi:10.1101/081364], even using generic deep convolutional networks trained on natural images [@doi:10.1101/085118], known as transfer learning.
Recent work by Johnson et al. [@tag:Johnson2017_integ_cell] demonstrated how the use of a conditional adversarial autoencoder allows for a probabilistic interpretation of cell and nuclear morphology and structure localization from fluorescence images.
The proposed model is able to generalize well to a wide range of subcellular localizations.
The generative nature of the model allows it to produce high-quality synthetic images predicting localization of subcellular structures by directly modeling the localization of fluorescent labels.
Notably, this approach reduces the modeling time by omitting the subcellular structure segmentation step.

The impact of further improvements on biomedicine could be enormous.
Comparing cell population morphologies using conventional methods of segmentation and feature extraction has already proven useful for functionally annotating genes and alleles, identifying the cellular target of small molecules, and identifying disease-specific phenotypes suitable for drug screening [@doi:10.1016/j.copbio.2016.04.003; @doi:10.1002/cyto.a.22909; @doi:10.1083/jcb.201610026].
Deep learning would bring to these new kinds of experiments---known as image-based profiling or morphological profiling---a higher degree of accuracy, stemming from the freedom from human-tuned feature extraction strategies.

### Single-cell data

Single-cell methods are generating excitement as biologists characterize the vast heterogeneity within unicellular species and between cells of the same tissue type in the same organism [@tag:Gawad2016_singlecell].
For instance, tumor cells and neurons can both harbor extensive somatic variation [@tag:Lodato2015_neurons].
Understanding single-cell diversity in all its dimensions---genetic, epigenomic, transcriptomic, proteomic, morphologic, and metabolic---is key if treatments are to be targeted not only to a specific individual, but also to specific pathological subsets of cells.
Single-cell methods also promise to uncover a wealth of new biological knowledge.
A sufficiently large population of single cells will have enough representative
"snapshots" to recreate timelines of dynamic biological processes.
If tracking processes over time is not the limiting factor, single-cell techniques can provide maximal resolution compared to averaging across all cells in bulk tissue, enabling the study of transcriptional bursting with single-cell fluorescence *in situ* hybridization or the heterogeneity of epigenomic patterns with single-cell Hi-C or ATAC-seq [@tag:Liu2016_sc_transcriptome; @tag:Vera2016_sc_analysis].
Joint profiling of single-cell epigenomic and transcriptional states provides unprecedented views of regulatory processes [@doi:10.1101/138685].

However, large challenges exist in studying single cells.
Relatively few cells can be assayed at once using current droplet, imaging, or microwell technologies, and low-abundance molecules or modifications may not be detected by chance due to a phenomenon known as dropout, not to be confused with the dropout layer of deep learning.
To solve this problem, Angermueller et al. [@tag:Angermueller2016_single_methyl] trained a neural network to predict the presence or absence of methylation of a specific CpG site in single cells based on surrounding methylation signal and underlying DNA sequence, achieving several percentage points of improvement compared to random forests or deep networks trained only on CpG or sequence information.
Similar deep learning methods have been applied to impute low-resolution ChIP-seq signal from bulk tissue with great success, and they could easily be adapted to single-cell data [@tag:Qin2017_onehot; @tag:Koh2016_denoising].
Deep learning has also been useful for dealing with batch effects [@tag:Shaham2016_batch_effects].

Examining populations of single cells can reveal biologically meaningful subsets of cells as well as their underlying gene regulatory networks [@tag:Gaublomme2015_th17].
Unfortunately, machine learning methods generally struggle with imbalanced data---when there are many more examples of class 1 than class 2---because prediction accuracy is usually evaluated over the entire dataset.
To tackle this challenge, Arvaniti et al.
[@tag:Arvaniti2016_rare_subsets] classified healthy and cancer cells expressing 25 markers by using the most discriminative filters from a CNN trained on the data as a linear classifier.
They achieved impressive performance, even for cell types where the subset percentage ranged from 0.1 to 1%, significantly outperforming logistic regression and distance-based outlier detection methods.
However, they did not benchmark against random forests, which tend to work better for imbalanced data, and their data was relatively low dimensional.

Neural networks can also learn low-dimensional representations of single-cell gene expression data for visualization, clustering, and other tasks.
Both scvis [@doi:10.1101/178624] and scVI [@arxiv:1709.02082] are unsupervised approaches based on variational autoencoders (VAEs).
Whereas scvis primarily focuses on single-cell visualization as a replacement for t-SNE [@tag:Maaten2008_tsne], the scVI model accounts for zero-inflated expression distributions and can impute zero values that are due to technical effects.
Beyond VAEs, Lin et al. developed a supervised model to predict cell type [@doi:10.1093/nar/gkx681].
Similar to transfer learning approaches for microscopy images [@doi:10.1101/085118], they demonstrated that the hidden layer representations were informative in general and could be used to identify cellular subpopulations or match new cells to known cell types.
The supervised neural network's representation was better overall at retrieving cell types than alternatives, but all methods struggled to recover certain cell types such as hematopoietic stem cells and inner cell mass cells.
As the Human Cell Atlas [@doi:10.7554/eLife.27041] and related efforts generate more single-cell expression data, there will be opportunities to assess how well these low-dimensional representations generalize to new cell types as well as abundant training data to learn broadly-applicable representations.

The sheer quantity of omic information that can be obtained from each cell, as well as the number of cells in each dataset, uniquely position single-cell data to benefit from deep learning. In the future, lineage tracing could be revolutionized by using autoencoders to reduce the feature space of transcriptomic or variant data followed by algorithms to learn optimal cell differentiation trajectories [@tag:Qiu2017_graph_embedding] or by feeding cell morphology and movement into neural networks [@tag:Buggenthin2017_imaged_lineage].
Reinforcement learning algorithms [@tag:Silver2016_alphago] could be trained on the evolutionary dynamics of cancer cells or bacterial cells undergoing selection pressure and reveal whether patterns of adaptation are random or deterministic, allowing us to develop therapeutic strategies that forestall resistance.
We are excited to see the creative applications of deep learning to single-cell biology that emerge over the next few years.

### Metagenomics

Metagenomics, which refers to the study of genetic material---16S rRNA or whole-genome shotgun DNA---from microbial communities, has revolutionized the study of micro-scale ecosystems within and around us.
In recent years, machine learning has proved to be a powerful tool for metagenomic analysis.
16S rRNA has long been used to deconvolve mixtures of microbial genomes, yet this ignores more than 99% of the genomic content.
Subsequent tools aimed to classify 300--3000 bp reads from complex mixtures of microbial genomes based on tetranucleotide frequencies, which differ across organisms [@tag:Karlin], using supervised [@tag:McHardy; @tag:nbc] or unsupervised methods [@tag:Abe].
Then, researchers began to use techniques that could estimate relative abundances from an entire sample faster than classifying individual reads [@tag:Metaphlan; @tag:wgsquikr; @tag:lmat; @tag:Vervier].
There is also great interest in identifying and annotating sequence reads [@tag:yok; @tag:Soueidan].
However, the focus on taxonomic and functional annotation is just the first step.
Several groups have proposed methods to determine host or environment phenotypes from the organisms that are identified [@tag:Guetterman; @tag:Knights; @tag:Stratnikov; @tag:Segata] or overall sequence composition [@tag:Ding].
Also, researchers have looked into how feature selection can improve classification [@tag:Liu; @tag:Segata], and techniques have been proposed that are classifier-independent [@tag:Ditzler; @tag:Ditzler2].

Most neural networks are used for phylogenetic classification or functional annotation from sequence data where there is ample data for training.
Neural networks have been applied successfully to gene annotation (e.g. Orphelia [@tag:Hoff] and FragGeneScan [@doi:10.1093/nar/gkq747]).
Representations (similar to word2vec [@tag:word2vec] in natural language processing) for protein family classification have been introduced and classified with a skip-gram neural network [@tag:Asgari].
Recurrent neural networks show good performance for homology and protein family identification [@tag:Hochreiter; @tag:Sonderby].

One of the first techniques of *de novo* genome binning used self-organizing maps, a type of neural network [@tag:Abe].
Essinger et al. [@tag:Essinger2010_taxonomic] used Adaptive Resonance Theory to cluster similar genomic fragments and showed that it had better performance than k-means.
However, other methods based on interpolated Markov models [@tag:Salzberg] have performed better than these early genome binners.
Neural networks can be slow and therefore have had limited use for reference-based taxonomic classification, with TAC-ELM [@tag:TAC-ELM] being the only neural network-based algorithm to taxonomically classify massive amounts of metagenomic data.
An initial study successfully applied neural networks to taxonomic classification of 16S rRNA genes, with convolutional networks providing about 10% accuracy genus-level improvement over RNNs and random forests [@tag:Mrzelj].
However, this study evaluated only 3000 sequences.

Neural network uses for classifying phenotype from microbial composition are just beginning.
A simple multi-layer perceptron (MLP) was able to classify wound severity from microbial species present in the wound [@doi:10.1016/j.bjid.2015.08.013].
Recently, Ditzler et al. associated soil samples with pH level using MLPs, DBNs, and RNNs [@tag:Ditzler3].
Besides classifying samples appropriately, internal phylogenetic tree nodes inferred by the networks represented features for low and high pH.
Thus, hidden nodes might provide biological insight as well as new features for future metagenomic sample comparison.
Also, an initial study has shown promise of these networks for diagnosing disease [@tag:Faruqi].

Challenges remain in applying deep neural networks to metagenomics problems.
They are not yet ideal for phenotype classification because most studies contain tens of samples and hundreds or thousands of features (species).
Such underdetermined, or ill-conditioned, problems are still a challenge for deep neural networks that require many training examples.
Also, due to convergence issues [@arxiv:1212.0901v2], taxonomic classification of reads from whole genome sequencing seems out of reach at the moment for deep neural networks.
There are only thousands of full-sequenced genomes as compared to hundreds of thousands of 16S rRNA sequences available for training.

However, because RNNs have been applied to base calls for the Oxford Nanopore long-read sequencer with some success [@tag:Boza] (discussed below), one day the entire pipeline, from denoising to functional classification, may be combined into one step using powerful LSTMs [@tag:Sutskever].
For example, metagenomic assembly usually requires binning then assembly, but could deep neural nets accomplish both tasks in one network?
We believe the greatest potential in deep learning is to learn the complete characteristics of a metagenomic sample in one complex network.

### Sequencing and variant calling

While we have so far primarily discussed the role of deep learning in analyzing genomic data, deep learning can also substantially improve our ability to obtain the genomic data itself.
We discuss two specific challenges: calling SNPs and indels (insertions and deletions) with high specificity and sensitivity and improving the accuracy of new types of data such as nanopore sequencing.
These two tasks are critical for studying rare variation, allele-specific transcription and translation, and splice site mutations.
In the clinical realm, sequencing of rare tumor clones and other genetic diseases will require accurate calling of SNPs and indels.

Current methods achieve relatively high (>99%) precision at 90% recall for SNPs and indel calls from Illumina short-read data [@tag:Poplin2016_deepvariant], yet this leaves a large number of potentially clinically-important remaining false positives and false negatives.
These methods have so far relied on experts to build probabilistic models that reliably separate signal from noise.
However, this process is time consuming and fundamentally limited by how well we understand and can model the factors that contribute to noise.
Recently, two groups have applied deep learning to construct data-driven unbiased noise models.
One of these models, DeepVariant, leverages Inception, a neural network trained for image classification by Google Brain, by encoding reads around a candidate SNP as a 221x100 bitmap image, where each column is a nucleotide and each row is a read from the sample library [@tag:Poplin2016_deepvariant].
The top 5 rows represent the reference, and the bottom 95 rows represent randomly sampled reads that overlap the candidate variant.
Each RGBA (red/green/blue/alpha) image pixel encodes the base (A, C, G, T) as a different red value, quality score as a green value, strand as a blue value, and variation from the reference as the alpha value.
The neural network outputs genotype probabilities for each candidate variant.
They were able to achieve better performance than GATK [@doi:10.1038/ng.806], a leading genotype caller, even when GATK was given information about population variation for each candidate variant.
Another method, still in its infancy, hand-developed 62 features for each candidate variant and fed these vectors into a fully connected deep neural network [@tag:Torracinta2016_deep_snp].
Unfortunately, this feature set required at least 15 iterations of software development to fine-tune, which suggests that these models may not generalize.

Variant calling will benefit more from optimizing neural network architectures than from developing features by hand.
An interesting and informative next step would be to rigorously test if encoding raw sequence and quality data as an image, tensor, or some other mixed format produces the best variant calls.
Because many of the latest neural network architectures (ResNet, Inception, Xception, and others) are already optimized for and pre-trained on generic, large-scale image datasets [@tag:Chollet2016_xception], encoding genomic data as images could prove to be a generally effective and efficient strategy.

In limited experiments, DeepVariant was robust to sequencing depth, read length, and even species [@tag:Poplin2016_deepvariant].
However, a model built on Illumina data, for instance, may not be optimal for Pacific Biosciences long-read data or MinION nanopore data, which have vastly different specificity and sensitivity profiles and signal-to-noise characteristics.
Recently, Boza et al. used bidirectional recurrent neural networks to infer the *E. coli* sequence from MinION nanopore electric current data with higher per-base accuracy than the proprietary hidden Markov model-based algorithm Metrichor [@tag:Boza].
Unfortunately, training any neural network requires a large amount of data, which is often not available for new sequencing technologies.
To circumvent this, one very preliminary study simulated mutations and spiked them into somatic and germline RNA-seq data, then trained and tested a neural network on simulated paired RNA-seq and exome sequencing data [@tag:Torracinta2016_sim].
Despite subsequent evaluation [@doi:10.1101/093534] on real somatic mutation data from the International Cancer Genome Consortium [@doi:10.1038/ncomms10001], further assessments are required to determine whether simulation can produce sufficiently realistic data to train reliable models.

Method development for interpreting new types of sequencing data has historically taken two steps: first, easily implemented hard cutoffs that prioritize specificity over sensitivity, then expert development of probabilistic models with hand-developed inputs [@tag:Torracinta2016_sim].
We anticipate that these steps will be replaced by deep learning, which will infer features simply by its ability to optimize a complex model against data.

### Neuroscience

Artificial neural networks were originally conceived as a model for computation in the brain [@doi:10.1007/BF02478259].
Although deep neural networks have evolved to become a workhorse across many fields, there is still a strong connection between deep networks and the study of the brain.
The rich parallel history of artificial neural networks in computer science and neuroscience is reviewed in [@doi:10.3389/fncom.2016.00094; @doi:10.1101/133504; @doi:10.1016/j.neuron.2017.06.011].

Convolutional neural networks were originally conceived as faithful models of visual information processing in the primate visual system, and are still considered so [@doi:10.1038/nn.4244].
The activations of hidden units in consecutive layers of deep convolutional networks have been found to parallel the activity of neurons in consecutive brain regions involved in processing visual scenes.
Such models of neural computation are called "encoding" models, as they predict how the nervous system might encode sensory information in the world.

Even when they are not directly modeling biological neurons, deep networks have been a useful computational tool in neuroscience.
They have been developed as statistical time series models of neural activity in the brain.
And in contrast to the encoding models described earlier, these models are used for decoding neural activity, for instance in brain machine interfaces [@doi:10.1101/152884].
They have been crucial to the field of connectomics, which is concerned with mapping the connectivity of biological neural networks in the brain.
In connectomics, deep networks are used to segment the shapes of individual neurons and to infer their connectivity from 3D electron microscopic images [@doi:10.1016/j.conb.2010.07.004], and they have also been used to infer causal connectivity from optical measurement and perturbation of neural activity [@tag:Aitchison2017].

It is an exciting time for neuroscience.
Recent rapid progress in deep networks continues to inspire new machine learning based models of brain computation [@doi:10.3389/fncom.2016.00094].
And neuroscience continues to inspire new models of artificial intelligence [@doi:10.1016/j.neuron.2017.06.011].


## The impact of deep learning in treating disease and developing new treatments

Given the need to make better, faster interventions at the point of care---incorporating the complex calculus of a patient's symptoms, diagnostics, and life history---there have been many attempts to apply deep learning to patient treatment.
Success in this area could help to enable personalized healthcare or precision medicine [@doi:10.1056/NEJMp1006304; @doi:10.1155/2013/769639].
Earlier, we reviewed approaches for patient categorization.
Here, we examine the potential for better treatment, which broadly, may be divided into methods for improved choices of interventions for patients and those for development of new interventions.

### Clinical decision making

In 1996, Tu [@tag:Tu1996_anns] compared the effectiveness of artificial neural networks and logistic regression, questioning whether these techniques would replace traditional statistical methods for predicting medical outcomes such as myocardial infarction [@tag:Baxt1991_myocardial] or mortality [@tag:Wasson1985_clinical].
He posited that while neural networks have several advantages in representational power, the difficulties in interpretation may limit clinical applications, a limitation that still remains today.
In addition, the challenges faced by physicians parallel those encountered by deep learning.
For a given patient, the number of possible diseases is very large, with a long tail of rare diseases and patients are highly heterogeneous and may present with very different signs and symptoms for the same disease.
Still, in 2006 Lisboa and Taktak [@tag:Lisboa2006_review] examined the use of artificial neural networks in medical journals, concluding that they improved healthcare relative to traditional screening methods in 21 of 27 studies.
Recent applications of deep learning in pharmacogenomics and pharmacoepigenomics show the potential for improving patient treatment response and outcome prediction using patient-specific data, pharmacogenomic targets, and pharmacological knowledge bases [@tag:Kalinin2018_pgx].

While further progress has been made in using deep learning for clinical decision making, it is hindered by a challenge common to many deep learning applications: it is much easier to predict an outcome than to suggest an action to change the outcome.
Several attempts [@tag:Katzman2016_deepsurv; @tag:Ranganath2016_deep] at recasting the clinical decision-making problem into a prediction problem (i.e. prediction of which treatment will most improve the patient's health) have accurately predicted survival patterns, but technical and medical challenges remain for clinical adoption (similar to those for categorization).
In particular, remaining barriers include actionable interpretability of deep learning models, fitting deep models to limited and heterogeneous data, and integrating complex predictive models into a dynamic clinical environment.

A critical challenge in providing treatment recommendations is identifying a causal relationship for each recommendation.
Causal inference is often framed in terms of counterfactual question [@doi:10.1037/h0037350].
Johansson et al.
[@arxiv:1605.03661] use deep neural networks to create representation models for covariates that capture nonlinear effects and show significant performance improvements over existing models.
In a less formal approach, Kale et al.
[@pmcid:PMC4765623] first create a deep neural network to model clinical time series and then analyze the relationship of the hidden features to the output using a causal approach.

A common challenge for deep learning is the interpretability of the models and their predictions.
The task of clinical decision making is necessarily risk-averse, so model interpretability is key.
Without clear reasoning, it is difficult to establish trust in a model.
As described above, there has been some work to directly assign treatment plans without interpretability; however, the removal of human experts from the decision-making loop make the models difficult to integrate with clinical practice.
To alleviate this challenge, several studies have attempted to create more interpretable deep models, either specifically for healthcare or as a general procedure for deep learning (see Discussion).

#### Predicting patient trajectories

A common application for deep learning in this domain is the temporal structure of healthcare records.
Many studies [@tag:Lipton2016_missing; @tag:Che2016_rnn; @tag:Huddar2016_predicting; @tag:Lipton2015_lstm] have used RNNs to categorize patients, but most stop short of suggesting clinical decisions.
Nemati et al. [@tag:Nemati2016_rl] used deep reinforcement learning to optimize a heparin dosing policy for intensive care patients.
However, because the ideal dosing policy is unknown, the model's predictions must be evaluated on counter-factual data.
This represents a common challenge when bridging the gap between research and clinical practice.
Because the ground-truth is unknown, researchers struggle to evaluate model predictions in the absence of interventional data, but clinical application is unlikely until the model has been shown to be effective.
The impressive applications of deep reinforcement learning to other domains [@tag:Silver2016_alphago] have relied on knowledge of the underlying processes (e.g. the rules of the game).
Some models have been developed for targeted medical problems [@tag:Gultepe2014_sepsis], but a generalized engine is beyond current capabilities.

#### Clinical trial efficiency

A clinical deep learning task that has been more successful is the assignment of patients to clinical trials.
Ithapu et al. [@tag:Ithapu2015_efficient] used a randomized denoising autoencoder to learn a multimodal imaging marker that predicts future cognitive and neural decline from positron emission tomography
(PET), amyloid florbetapir PET, and structural magnetic resonance imaging.
By accurately predicting which cases will progress to dementia, they were able to efficiently assign patients to a clinical trial and reduced the required sample sizes by a factor of five.
Similarly, Artemov et al. [@tag:Artemov2016_clinical] applied deep learning to predict which clinical trials were likely to fail and which were likely to succeed.
By predicting the side effects and pathway activations of each drug and translating these activations to a success probability, their deep learning-based approach was able to significantly outperform a random forest classifier trained on gene expression changes.
These approaches suggest promising directions to improve the efficiency of clinical trials and accelerate drug development.

### Drug repositioning

Drug repositioning (or repurposing) is an attractive option for delivering new drugs to the market because of the high costs and failure rates associated with more traditional drug discovery approaches [@doi:10.1016/j.jhealeco.2016.01.012; @doi:10.1038/nrd4609].
A decade ago, the Connectivity Map [@doi:10.1126/science.1132939] had a sizeable impact.
Reverse matching disease gene expression signatures with a large set of reference compound profiles allowed researchers to formulate repurposing hypotheses at scale using a simple non-parametric test.
Since then, several advanced computational methods have been applied to formulate and validate drug repositioning hypotheses [@doi:10.1093/bib/bbv020; @doi:10.1093/bib/bbw112; @doi:10.1093/bib/bbw110].
Using supervised learning and collaborative filtering to tackle this type of problem is proving successful, especially when coupling disease or compound omic data with topological information from protein-protein or protein-compound interaction networks [@doi:10.1186/1758-2946-5-30; @doi:10.1021/ci500340n; @doi:10.1186/s12859-015-0845-0].

For example, Menden et al. [@doi:10.1371/journal.pone.0061318] used a shallow neural network to predict sensitivity of cancer cell lines to drug treatment using both cell line and drug features, opening the door to precision medicine and drug repositioning opportunities in cancer.
More recently, Aliper et al.
[@doi:10.1021/acs.molpharmaceut.6b00248] used gene- and pathway-level drug perturbation transcriptional profiles from the Library of Network-Based Cellular Signatures [@doi:10.3389/fgene.2014.00342] to train a fully connected deep neural network to predict drug therapeutic uses and indications.
By using confusion matrices and leveraging misclassification, the authors formulated a number of interesting hypotheses, including repurposing cardiovascular drugs such as otenzepad and pinacidil for neurological disorders.

Drug repositioning can also be approached by attempting to predict novel drug-target interactions and then repurposing the drug for the associated indication [@doi:10.1371/journal.pcbi.1005219; @doi:10.1371/journal.pcbi.1005135].
Wang et al. [@doi:10.1109/BIBM.2014.6999129] devised a pairwise input neural network with two hidden layers that takes two inputs, a drug and a target binding site, and predicts whether they interact.
Wang et al. [@doi:10.1093/bioinformatics/btt234] trained individual RBMs for each target in a drug-target interaction network and used these models to predict novel interactions pointing to new indications for existing drugs.
Wen et al. [@doi:10.1021/acs.jproteome.6b00618] extended this concept to deep learning by creating a DBN called DeepDTIs, which predicts interactions using chemical structure and protein sequence features.

Drug repositioning appears an obvious candidate for deep learning both because of the large amount of high-dimensional data available and the complexity of the question being asked.
However, perhaps the most promising piece of work in this space [@doi:10.1021/acs.molpharmaceut.6b00248] is more of a proof of concept than a real-world hypothesis-generation tool; notably, deep learning was used to predict drug indications but not for the actual repositioning.
At present, some of the most popular state-of-the-art methods for signature-based drug repurposing [@doi:10.1038/npjsba.2016.15] do not use predictive modeling.
A mature and production-ready framework for drug repositioning via deep learning is currently missing.

### Drug development

#### Ligand-based prediction of bioactivity

High-throughput chemical screening in biomedical research aims to improve therapeutic options over a long term horizon [@tag:PerezSianes2016_screening].
The objective is to discover which small molecules (also referred to as chemical compounds or ligands) specifically affect the activity of a target, such as a kinase, protein-protein interaction, or broader cellular phenotype.
This screening is often one of the first steps in a long drug discovery pipeline, where novel molecules are pursued for their ability to inhibit or enhance disease-relevant biological mechanisms [@doi:10.1038/nrd1086].
Initial hits are confirmed to eliminate false positives and proceed to the lead generation stage [@doi:10.1016/j.drudis.2006.06.016], where they are evaluated for absorption, distribution, metabolism, excretion, and toxicity (ADMET) and other properties.
It is desirable to advance multiple lead series, clusters of structurally-similar active chemicals, for further optimization by medicinal chemists to protect against unexpected failures in the later stages of drug discovery [@doi:10.1038/nrd1086].

Computational work in this domain aims to identify sufficient candidate active compounds without exhaustively screening libraries of hundreds of thousands or millions of chemicals.
Predicting chemical activity computationally is known as virtual screening.
An ideal algorithm will rank a sufficient number of active compounds before the inactives, but the rankings of actives relative to other actives and inactives are less important [@tag:Swamidass2009_irv].
Computational modeling also has the potential to predict ADMET traits for lead generation [@tag:Kearnes2016_admet] and how drugs are metabolized [@doi:10.1021/ci400518g].

Ligand-based approaches train on chemicals' features without modeling target features (e.g. protein structure).
Neural networks have a long history in this domain [@tag:Baskin2015_drug_disc; @doi:10.1002/minf.201501008], and the 2012 Merck Molecular Activity Challenge on Kaggle generated substantial excitement about the potential for high-parameter deep learning approaches.
The winning submission was an ensemble that included a multi-task multi-layer perceptron network [@tag:Dahl2014_multi_qsar].
The sponsors noted drastic improvements over a random forest baseline, remarking "we have seldom seen any method in the past 10 years that could consistently outperform [random forest] by such a margin" [@tag:Ma2015_qsar_merck], but not all outside experts were convinced [@tag:Lowe2012_kaggle].
Subsequent work (reviewed in more detail by Goh et al. [@doi:10.1002/jcc.24764]) explored the effects of jointly modeling far more targets than the Merck challenge [@tag:Unterthiner2014_screening; @tag:Ramsundar2015_multitask_drug], with Ramsundar et al.
[@tag:Ramsundar2015_multitask_drug] showing that the benefits of multi-task networks had not yet saturated even with 259 targets.
Although DeepTox [@tag:Mayr2016_deep_tox], a deep learning approach, won another competition, the Toxicology in the 21st Century (Tox21) Data Challenge, it did not dominate alternative methods as thoroughly as in other domains.
DeepTox was the top performer on 9 of 15 targets and highly competitive with the top performer on the others.
However, for many targets there was little separation between the top two or three methods.

The nuanced Tox21 performance may be more reflective of the practical challenges encountered in ligand-based chemical screening than the extreme enthusiasm generated by the Merck competition.
A study of 22 ADMET tasks demonstrated that there are limitations to multi-task transfer learning that are in part a consequence of the degree to which tasks are related [@tag:Kearnes2016_admet].
Some of the ADMET datasets showed superior performance in multi-task models with only 22 ADMET tasks compared to multi-task models with over 500 less-similar tasks.
In addition, the training datasets encountered in practical applications may be tiny relative to what is available in public datasets and organized competitions.
A study of BACE-1 inhibitors included only 1547 compounds [@tag:Subramanian2016_bace1].
Machine learning models were able to train on this limited dataset, but overfitting was a challenge and the differences between random forests and a deep neural network were negligible, especially in the classification setting.
Overfitting is still a problem in larger chemical screening datasets with tens or hundreds of thousands of compounds because the number of active compounds can be very small, on the order of 0.1% of all tested chemicals for a typical target [@doi:10.1002/wcms.1104].
This has motivated low-parameter neural networks that emphasize compound-compound similarity, such as influence-relevance voter [@tag:Swamidass2009_irv; @tag:Lusci2015_irv], instead of predicting compound activity directly from chemical features.

#### Chemical featurization and representation learning

Much of the recent excitement in this domain has come from what could be considered a creative experimentation phase, in which deep learning has offered novel possibilities for feature representation and modeling of chemical compounds.
A molecular graph, where atoms are labeled nodes and bonds are labeled edges, is a natural way to represent a chemical structure.
Chemical features can be represented as a list of molecular descriptors such as molecular weight, atom counts, functional groups, charge representations, summaries of atom-atom relationships in the molecular graph, and more sophisticated derived properties [@doi:10.1002/9783527628766].
Traditional machine learning approaches relied on preprocessing the graph into a feature vector of molecular descriptors or a fixed-width bit vector known as a fingerprint [@tag:Rogers2010_fingerprints].
The same fingerprints have been used by some drug-target interaction methods discussed above [@doi:10.1021/acs.jproteome.6b00618].
An overly simplistic but approximately correct view of chemical fingerprints is that each bit represents the presence or absence of a particular chemical substructure in the molecular graph.
Instead of using molecular descriptors or fingerprints as input, modern neural networks can represent chemicals as textual strings [@tag:Gomezb2016_automatic] or images [@arxiv:1706.06689] or operate directly on the molecular graph, which has enabled strategies for learning novel chemical representations.

Virtual screening and chemical property prediction have emerged as one of the major applications areas for graph-based neural networks.
Duvenaud et al. [@tag:Duvenaud2015_graph_conv] generalized standard circular fingerprints by substituting discrete operations in the fingerprinting algorithm with operations in a neural network, producing a real-valued feature vector instead of a bit vector.
Other approaches offer trainable networks that can learn chemical feature representations that are optimized for a particular prediction task.
Lusci et al. [@tag:Lusci2013_rnn] applied recursive neural networks for directed acyclic graphs to undirected molecular graphs by creating an ensemble of directed graphs in which one atom is selected as the root node.
Graph convolutions on undirected molecular graphs have eliminated the need to enumerate artificially directed graphs, learning feature vectors for atoms that are a function of the properties of neighboring atoms and local regions on the molecular graph [@tag:Kearnes2016_graph_conv; @tag:AltaeTran2016_one_shot; @doi:10.1021/acs.jcim.6b00601].
More sophisticated graph algorithms [@doi:10.1021/acscentsci.7b00405; @arxiv:1801.02144] addressed limitations of standard graph convolutions that primarily operate on each node's local neighborhood.
We anticipate that these graph-based neural networks could also be applicable in other types of biological networks, such as the PPI networks we discussed previously.

Advances in chemical representation learning have also enabled new strategies for learning chemical-chemical similarity functions.
Altae-Tran et al. developed a one-shot learning network [@tag:AltaeTran2016_one_shot] to address the reality that most practical chemical screening studies are unable to provide the thousands or millions of training compounds that are needed to train larger multi-task networks.
Using graph convolutions to featurize chemicals, the network learns an embedding from compounds into a continuous feature space such that compounds with similar activities in a set of training tasks have similar embeddings.
The approach is evaluated in an extremely challenging setting.
The embedding is learned from a subset of prediction tasks (e.g. activity assays for individual proteins), and only one to ten labeled examples are provided as training data on a new task.
On Tox21 targets, even when trained with _one_ task-specific active compound and _one_ inactive compound, the model is able to generalize reasonably well because it has learned an informative embedding function from the related tasks.
Random forests, which cannot take advantage of the related training tasks, trained in the same setting are only slightly better than a random classifier.
Despite the success on Tox21, performance on MUV datasets, which contains assays designed to be challenging for chemical informatics algorithms, is considerably worse.
The authors also demonstrate the limitations of transfer learning as embeddings learned from the Tox21 assays have little utility for a drug adverse reaction dataset.

These novel, learned chemical feature representations may prove to be essential for accurately predicting why some compounds with similar structures yield similar target effects and others produce drastically different results.
Currently, these methods are enticing but do not necessarily outperform classic approaches by a large margin.
The neural fingerprints [@tag:Duvenaud2015_graph_conv] were narrowly beaten by regression using traditional circular fingerprints on a drug efficacy prediction task but were superior for predicting solubility or photovoltaic efficiency.
In the original study, graph convolutions [@tag:Kearnes2016_graph_conv] performed comparably to a multi-task network using standard fingerprints and slightly better than the neural fingerprints [@tag:Duvenaud2015_graph_conv] on the drug efficacy task but were slightly worse than the influence-relevance voter method on an HIV dataset [@tag:Swamidass2009_irv].
Broader recent benchmarking has shown that relative merits of these methods depends on the dataset and cross validation strategy [@tag:Wu2017_molecule_net], though evaluation in this domain often uses area under the receiver operating characteristic curve (AUROC) [@doi:10.1007/s10822-008-9170-2], which has limited utility due to the large class imbalance (see Discussion).

We remain optimistic for the potential of deep learning and specifically representation learning in drug discovery.
Rigorous benchmarking on broad and diverse prediction tasks will be as important as novel neural network architectures to advance the state of the art and convincingly demonstrate superiority over traditional cheminformatics techniques.
Fortunately, there has recently been much progress in this direction.
The DeepChem software [@tag:AltaeTran2016_one_shot; @tag:DeepChem] and MoleculeNet benchmarking suite [@tag:Wu2017_molecule_net] built upon it contain chemical bioactivity and toxicity prediction datasets, multiple compound featurization approaches including graph convolutions, and various machine learning algorithms ranging from standard baselines like logistic regression and random forests to recent neural network architectures.
Independent research groups have already contributed additional datasets and prediction algorithms to DeepChem.
Adoption of common benchmarking evaluation metrics, datasets, and baseline algorithms has the potential to establish the practical utility of deep learning in chemical bioactivity prediction and lower the barrier to entry for machine learning researchers without biochemistry expertise.

One open question in ligand-based screening pertains to the benefits and limitations of transfer learning.
Multi-task neural networks have shown the advantages of jointly modeling many targets [@tag:Unterthiner2014_screening; @tag:Ramsundar2015_multitask_drug].
Other studies have shown the limitations of transfer learning when the prediction tasks are insufficiently related [@tag:Kearnes2016_admet; @tag:AltaeTran2016_one_shot].
This has important implications for representation learning.
The typical approach to improve deep learning models by expanding the dataset size may not be applicable if only
"related" tasks are beneficial, especially because task-task relatedness is ill-defined.
The massive chemical state space will also influence the development of unsupervised representation learning methods [@tag:Gomezb2016_automatic; @doi:10.1021/acs.jcim.7b00616].
Future work will establish whether it is better to train on massive collections of diverse compounds, drug-like small molecules, or specialized subsets.

#### Structure-based prediction of bioactivity

When protein structure is available, virtual screening has traditionally relied on docking programs to predict how a compound best fits in the target's binding site and score the predicted ligand-target complex [@doi:10.1208/s12248-012-9322-0].
Recently, deep learning approaches have been developed to model protein structure, which is expected to improve upon the simpler drug-target interaction algorithms described above that represent proteins with feature vectors derived from amino acid sequences [@doi:10.1109/BIBM.2014.6999129; @doi:10.1021/acs.jproteome.6b00618].

Structure-based deep learning methods differ in whether they use experimentally-derived or predicted ligand-target complexes and how they represent the 3D structure.
The Atomic CNN [@arxiv:1703.10603] and TopologyNet [@doi:10.1371/journal.pcbi.1005690] models take 3D structures from PDBBind [@doi:10.1021/jm048957q] as input, ensuring the ligand-target complexes are reliable.
AtomNet [@tag:Wallach2015_atom_net] samples multiple ligand poses within the target binding site, and DeepVS [@tag:Pereira2016_docking] and Ragoza et al. [@tag:Ragoza2016_protein] use a docking program to generate protein-compound complexes.
If they are sufficiently accurate, these latter approaches would have wider applicability to a much larger set of compounds and proteins.
However, incorrect ligand poses will be misleading during training, and the predictive performance is sensitive to the docking quality [@tag:Pereira2016_docking].

There are two established options for representing a protein-compound complex.
One option, a 3D grid, can featurize the input complex [@tag:Wallach2015_atom_net; @tag:Ragoza2016_protein].
Each entry in the grid tracks the types of protein and ligand atoms in that region of the 3D space or descriptors derived from those atoms.
Alternatively, DeepVS [@tag:Pereira2016_docking] and atomic convolutions [@arxiv:1703.10603] offer greater flexibility in their convolutions by eschewing the 3D grid.
Instead, they each implement techniques for executing convolutions over atoms' neighboring atoms in the 3D space.
Gomes et al. demonstrate that currently random forest on a 1D feature vector that describes the 3D ligand-target structure generally outperforms neural networks on the same feature vector as well as atomic convolutions and ligand-based neural networks when predicting the continuous-valued inhibition constant on the PDBBind refined dataset [@arxiv:1703.10603].
However, in the long term, atomic convolutions may ultimately overtake grid-based methods, as they provide greater freedom to model atom-atom interactions and the forces that govern binding affinity.

#### *De novo* drug design

*De novo* drug design attempts to model the typical design-synthesize-test cycle of drug discovery *in silico* [@doi:10.1002/wcms.49; @doi:10.1021/acs.jmedchem.5b01849].
It explores an estimated 10<sup>60</sup> synthesizable organic molecules with drug-like properties without explicit enumeration [@doi:10.1002/wcms.1104].
To score molecules after generation or during optimization, physics-based simulation could be used [@tag:Sumita2018], but machine learning models based on techniques discussed earlier may be preferable [@tag:Gomezb2016_automatic], as they are much more computationally expedient.
Computational efficiency is particularly important during optimization as the "scoring function" may need to be called thousands of times.

To "design" and "synthesize", traditional *de novo* design software relied on classical optimizers such as genetic algorithms.
These algorithms use a list of hard-coded rules to perform virtual chemical reactions on molecular structures during each iteration, leading to physically stable and synthesizable molecules [@doi:10.1021/acs.jmedchem.5b01849].
Deep learning models have been proposed as an alternative.
In contrast to the classical approaches, in theory generative models learned from big data would not require laboriously encoded expert knowledge to generate realistic, synthesizable molecules.

In the past few years, a large number of techniques for the generative modeling and optimization of molecules with deep learning have been explored, including RNNs, VAEs, GANs, and reinforcement learning---for a review see Elton et al. [@tag:Elton_molecular_design_review] or Vamathevan et al. [@tag:Vamathevan2019].

Building off the large amount of work that has already gone into text generation [@arxiv:1308.0850], many generative neural networks for drug design initially represented chemicals with the simplified molecular-input line-entry system (SMILES), a standard string-based representation with characters that represent atoms, bonds, and rings [@tag:Segler2017_drug_design].

The first successful demonstration of a deep learning based approach for molecular optimization occurred in 2016 with the development of a SMILES-to-SMILES autoencoder capable of learning a continuous latent feature space for molecules [@tag:Gomezb2016_automatic].
In this learned continuous space it is possible to interpolate between molecular structures in a manner that is not possible with discrete (e.g. bit vector or string) features or in symbolic, molecular graph space.
Even more interesting is that one can perform gradient-based or Bayesian optimization of molecules within this latent space.
The strategy of constructing simple, continuous features before applying supervised learning techniques is reminiscent of autoencoders trained on high-dimensional EHR data [@tag:BeaulieuJones2016_ehr_encode].
A drawback of the SMILES-to-SMILES autoencoder is that not all SMILES strings produced by the autoencoder's decoder correspond to valid chemical structures.
The Grammar Variational Autoencoder, which takes the SMILES grammar into account and is guaranteed to produce syntactically valid SMILES, helps alleviate this issue to some extent [@arxiv:1703.01925].

Another approach to *de novo* design is to train character-based RNNs on large collections of molecules, for example, ChEMBL [@doi:10.1093/nar/gkr777], to first obtain a generic generative model for drug-like compounds [@tag:Segler2017_drug_design].
These generative models successfully learn the grammar of compound representations, with 94% [@tag:Olivecrona2017_drug_design] or nearly 98% [@tag:Segler2017_drug_design] of generated SMILES corresponding to valid molecular structures.
The initial RNN is then fine-tuned to generate molecules that are likely to be active against a specific target by either continuing training on a small set of positive examples [@tag:Segler2017_drug_design] or adopting reinforcement learning strategies [@tag:Olivecrona2017_drug_design; @arxiv:1611.02796].
Both the fine-tuning and reinforcement learning approaches can rediscover known, held-out active molecules.

Reinforcement learning approaches where operations are performed directly on the molecular graph bypass the need to learn the details of SMILES syntax, allowing the model to focus purely on chemistry.
Additionally, they seem to require less training data and generate more valid molecules since they are constrained by design only to graph operations which satisfy chemical valiance rules [@tag:Elton_molecular_design_review].
A reinforcement learning agent developed by Zhou et al. [@doi:10.1038/s41598-019-47148-x] demonstrated superior molecular optimization performance on optimizing the quantitative estimate of drug-likeness (QED) metric and the "penalized logP" metric (logP minus the synthetic accessibility) when compared with other deep learning based approaches such as the Junction Tree VAE [@arxiv:1802.04364], Objective-Reinforced Generative Adversarial Network [@arxiv:1705.10843], and Graph Convolutional Policy Network [@arxiv:1806.02473].
As another example, Zhavoronkov et al. used generative tensorial reinforcement learning to discover inhibitors of discoidin domain receptor 1 (DDR1) [@tag:Zhavoronkov2019_drugs].
In contrast to most previous work, six lead candidates discovered using their approach were synthesized and tested in the lab, with 4/6 achieving some degree of binding to DDR1.
One of the molecules was chosen for further testing and showed promising results in a cancer cell line and mouse model [@tag:Zhavoronkov2019_drugs]. 

In concluding this section, we want to highlight two areas where work is still needed before AI can bring added value to the existing drug discovery process---novelty and synthesizability.
The work of Zhavoronkov et al. is arguably an important milestone and received much fanfare in the popular press, but Walters and Murko have presented a more sober assessment, noting that the generated molecule they choose to test in the lab is very similar to an existing drug that was present in their training data [@doi:10.1038/s41587-020-0418-2].
Small variations of existing molecules are likely not to be much better and may not be patentable.
One way to tackle this problem is to add novelty and diversity metrics to the reward function of reinforcement learning based algorithms.
Novelty should also be taken into account when comparing different models---and thus is included in the proposed GuacaMol benchmark (2019) for accessing generative molecules for molecular design [@doi:10.1021/acs.jcim.8b00839].
The other area which has been pointed to as a key limitation of current approaches is synthesizability [@doi:10.1021/acs.jcim.0c00174; @doi:10.1021/acsmedchemlett.0c00088].
Current heuristics of synthesizability, such as the synthetic accessibility score, are based on a relatively limited domain of chemical data and are too restrictive, so better models of synthesizability should help in this area [@doi:10.1021/acs.jcim.0c00174]. 

As noted before, genetic algorithms use hard-coded rules based on possible chemical reactions to generate molecular structures and therefore may have less trouble generating synthesizable molecules [@doi:10.1021/acs.jmedchem.5b01849].
We note in passing that Jensen (2018) [@doi:10.1039/C8SC05372C] and Yoshikawa et al. (2019) [@doi:10.1246/cl.180665] have both demonstrated genetic algorithms that are competitive with deep learning approaches. 
Progress on overcoming both of these shortcomings is proceeding on many fronts, and we believe the future of deep learning for molecular design is quite bright. 


## Discussion

Despite the disparate types of data and scientific goals in the learning tasks covered above, several challenges are broadly important for deep learning in the biomedical domain.
Here we examine these factors that may impede further progress, ask what steps have already been taken to overcome them, and suggest future research directions.

### Customizing deep learning models reflects a tradeoff between bias and variance

Some of the challenges in applying deep learning are shared with other machine learning methods.
In particular, many problem-specific optimizations described in this review reflect a recurring universal tradeoff---controlling the flexibility of a model in order to maximize predictivity.
Methods for adjusting the flexibility of deep learning models include dropout, reduced data projections, and transfer learning (described below).
One way of understanding such model optimizations is that they incorporate external information to limit model flexibility and thereby improve predictions.
This balance is formally described as a tradeoff between "bias and variance"
[@tag:goodfellow2016deep].

Although the bias-variance tradeoff is common to all machine learning applications, recent empirical and theoretical observations suggest that deep learning models may have uniquely advantageous generalization properties [@tag:Zhang2017_generalization; @tag:Lin2017_why_dl_works].
Nevertheless, additional advances will be needed to establish a coherent theoretical foundation that enables practitioners to better reason about their models from first principles.

#### Evaluation metrics for imbalanced classification

Making predictions in the presence of high class imbalance and differences between training and generalization data is a common feature of many large biomedical datasets, including deep learning models of genomic features, patient classification, disease detection, and virtual screening.
Prediction of transcription factor binding sites exemplifies the difficulties with learning from highly imbalanced data.
The human genome has 3 billion base pairs, and only a small fraction of them are implicated in specific biochemical activities.
Less than 1% of the genome can be confidently labeled as bound for most transcription factors.

Estimating the false discovery rate (FDR) is a standard method of evaluation in genomics that can also be applied to deep learning model predictions of genomic features.
Using deep learning predictions for targeted validation experiments of specific biochemical activities necessitates a more stringent FDR (typically 5--25%).
However, when predicted biochemical activities are used as features in other models, such as gene expression models, a low FDR may not be necessary.

What is the correspondence between FDR metrics and commonly used classification metrics such as AUPR and AUROC? AUPR evaluates the average precision, or equivalently, the average FDR across all recall thresholds.
This metric provides an overall estimate of performance across all possible use cases, which can be misleading for targeted validation experiments.
For example, classification of TF binding sites can exhibit a recall of 0% at 10% FDR and AUPR greater than 0.6.
In this case, the AUPR may be competitive, but the predictions are ill-suited for targeted validation that can only examine a few of the highest-confidence predictions.
Likewise, AUROC evaluates the average recall across all false positive rate (FPR) thresholds, which is often a highly misleading metric in class-imbalanced domains [@doi:10.1145/1143844.1143874; @doi:10.1038/nmeth.3945].
Consider a classification model with recall of 0% at FDR less than 25% and 100% recall at FDR greater than 25%.
In the context of TF binding predictions where only 1% of genomic regions are bound by the TF, this is equivalent to a recall of 100% for FPR greater than 0.33%.
In other words, the AUROC would be 0.9967, but the classifier would be useless for targeted validation.
It is not unusual to obtain a chromosome-wide AUROC greater than 0.99 for TF binding predictions but a recall of 0% at 10% FDR.
Consequently, practitioners must select the metric most tailored to their subsequent use case to use these methods most effectively.

#### Formulation of classification labels

Genome-wide continuous signals are commonly formulated into classification labels through signal peak detection.
ChIP-seq peaks are used to identify locations of TF binding and histone modifications.
Such procedures rely on thresholding criteria to define what constitutes a peak in the signal.
This inevitably results in a set of signal peaks that are close to the threshold, not sufficient to constitute a positive label but too similar to positively labeled examples to constitute a negative label.
To avoid an arbitrary label for these examples they may be labeled as "ambiguous".
Ambiguously labeled examples can then be ignored during model training and evaluation of recall and FDR.
The correlation between model predictions on these examples and their signal values can be used to evaluate if the model correctly ranks these examples between positive and negative examples.

#### Formulation of a performance upper bound

In assessing the upper bound on the predictive performance of a deep learning model, it is necessary to incorporate inherent between-study variation inherent to biomedical research [@tag:Errington2014_reproducibility].
Study-level variability limits classification performance and can lead to underestimating prediction error if the generalization error is estimated by splitting a single dataset.
Analyses can incorporate data from multiple labs and experiments to capture between-study variation within the prediction model mitigating some of these issues.

### Uncertainty quantification

Deep learning based solutions for biomedical applications could substantially benefit from guarantees on the reliability of predictions and a quantification of uncertainty.
Due to biological variability and precision limits of equipment, biomedical data do not consist of precise measurements but of estimates with noise.
Hence, it is crucial to obtain uncertainty measures that capture how noise in input values propagates through deep neural networks.
Such measures can be used for reliability assessment of automated decisions in clinical and public health applications, and for guarding against model vulnerabilities in the face of rare or adversarial cases [@tag:ghahramani_protect].
Moreover, in fundamental biological research, measures of uncertainty help researchers distinguish between true regularities in the data and patterns that are false or merely anecdotal.
There are two main uncertainties that one can calculate: epistemic and aleatoric [@tag:uncertainty_types].
Epistemic uncertainty describes uncertainty about the model, its structure, or its parameters.
This uncertainty is caused by insufficient training data or by a difference in the training set and testing set distributions, so it vanishes in the limit of infinite data.
On the other hand, aleatoric uncertainty describes uncertainty inherent in the observations.
This uncertainty is due to noisy or missing data, so it vanishes with the ability to observe all independent variables with infinite precision.
A good way to represent aleatoric uncertainty is to design an appropriate loss function with an uncertainty variable.
In the case of data-dependent aleatoric uncertainty, one can train the model to increase its uncertainty when it is incorrect due to noisy or missing data, and in the case of task-dependent aleatoric uncertainty, one can optimize for the best uncertainty parameter for each task [@tag:uncertainty_multi_task].
Meanwhile, there are various methods for modeling epistemic uncertainty, outlined below.

In classification tasks, confidence calibration is the problem of using classifier scores to predict class membership probabilities that match the true membership likelihoods.
These membership probabilities can be used to assess the uncertainty associated with assigning the example to each of the classes.
Guo et al. [@tag:guo_calibration] observed that contemporary neural networks are poorly calibrated and provided a simple recommendation for calibration: temperature scaling, a single parameter special case of Platt scaling [@tag:platt_scaling].
In addition to confidence calibration, there is early work from Chryssolouris et al. [@tag:Chryssolouris1996_confidence] that described a method for obtaining confidence intervals with the assumption of normally distributed error for the neural network.
More recently, Hendrycks and Gimpel discovered that incorrect or out-of-distribution examples usually have lower maximum softmax probabilities than correctly classified examples, allowing for effective detection of misclassified examples [@tag:out_dist_baseline].
Liang et al. used temperature scaling and small perturbations to further separate the softmax scores of correctly classified examples and the scores of out-of-distribution examples, allowing for more effective detection [@tag:temp_out_dist].
This approach outperformed the baseline approaches by a large margin, establishing a new state-of-the-art performance.

An alternative approach for obtaining principled uncertainty estimates from deep learning models is to use Bayesian neural networks.
Deep learning models are usually trained to obtain the most likely parameters given the data.
However, choosing the single most likely set of parameters ignores the uncertainty about which set of parameters (among the possible models that explain the given dataset) should be used.
This sometimes leads to uncertainty in predictions when the chosen likely parameters produce high-confidence but incorrect results.
On the other hand, the parameters of Bayesian neural networks are modeled as full probability distributions.
This Bayesian approach comes with a whole host of benefits, including better calibrated confidence estimates [@tag:ai_safety] and more robustness to adversarial and out-of-distribution examples [@tag:strong_adversary].
Unfortunately, modeling the full posterior distribution for the model’s parameters given the data is usually computationally intractable.
One popular method for circumventing this high computational cost is called test-time dropout [@tag:Gal2015_dropout], where an approximate posterior distribution is obtained using variational inference.
Gal and Ghahramani showed that a stack of fully connected layers with dropout between the layers is equivalent to approximate inference in a Gaussian process model [@tag:Gal2015_dropout].
The authors interpret dropout as a variational inference method and apply their method to convolutional neural networks.
This is simple to implement and preserves the possibility of obtaining cheap samples from the approximate posterior distribution.
Operationally, obtaining model uncertainty for a given case becomes as straightforward as leaving dropout turned on and predicting multiple times.
The spread of the different predictions is a reasonable proxy for model uncertainty.
This technique has been successfully applied in an automated system for detecting diabetic retinopathy [@tag:retinopathy_uncertainty], where uncertainty-informed referrals improved diagnostic performance and allowed the model to meet the National Health Service recommended levels of sensitivity and specificity.
The authors also found that entropy performs comparably to the spread obtained via test-time dropout for identifying uncertain cases, and therefore it can be used instead for automated referrals.

Several other techniques have been proposed for effectively estimating predictive uncertainty as uncertainty quantification for neural networks continues to be an active research area.
Recently, McClure and Kriegeskorte observed that test-time sampling improved calibration of the probabilistic predictions, sampling weights led to more robust uncertainty estimates than sampling units, and spike-and-slab sampling was superior to Gaussian dropconnect and Bernoulli dropout [@tag:mcclure_bayesian].
Krueger et al. introduced Bayesian hypernetworks [@tag:bayesian_hypernets] as another framework for approximate Bayesian inference in deep learning, where an invertible generative hypernetwork maps isotropic Gaussian noise to parameters of the primary network allowing for computationally cheap sampling and efficient estimation of the posterior.
Meanwhile, Lakshminarayanan et al. proposed using deep ensembles, which are traditionally used for boosting predictive performance, on standard (non-Bayesian) neural networks to obtain well-calibrated uncertainty estimates that are comparable to those obtained by Bayesian neural networks [@tag:uncertainty_ensembles].
In cases where model uncertainty is known to be caused by a difference in training and testing distributions, domain adaptation-based techniques can help mitigate the problem [@tag:domain_adapt_uncertainty].

Despite the success and popularity of deep learning, some deep learning models can be surprisingly brittle.
Researchers are actively working on modifications to deep learning frameworks to enable them to handle probability and embrace uncertainty.
Most notably, Bayesian modeling and deep learning are being integrated with renewed enthusiasm.
As a result, several opportunities for innovation arise: understanding the causes of model uncertainty can lead to novel optimization and regularization techniques, assessing the utility of uncertainty estimation techniques on various model architectures and structures can be very useful to practitioners, and extending Bayesian deep learning to unsupervised settings can be a significant breakthrough [@tag:gal_thesis].
Unfortunately, uncertainty quantification techniques are underutilized in the computational biology communities and largely ignored in the current deep learning for biomedicine literature.
Thus, the practical value of uncertainty quantification in biomedical domains is yet to be appreciated.

### Interpretation

As deep learning models achieve state-of-the-art performance in a variety of domains, there is a growing need to make the models more interpretable.
Interpretability matters for two main reasons.
First, a model that achieves breakthrough performance may have identified patterns in the data that practitioners in the field would like to understand.
However, this would not be possible if the model is a black box.
Second, interpretability is important for trust.
If a model is making medical diagnoses, it is important to ensure the model is making decisions for reliable reasons and is not focusing on an artifact of the data.
A motivating example of this can be found in Caruana et al. [@tag:Caruana2015_intelligible], where a model trained to predict the likelihood of death from pneumonia assigned lower risk to patients with asthma, but only because such patients were treated as higher priority by the hospital.
In the context of deep learning, understanding the basis of a model's output is particularly important as deep learning models are unusually susceptible to adversarial examples [@tag:Nguyen2014_adversarial] and can output confidence scores over 99.99% for samples that resemble pure noise.

As the concept of interpretability is quite broad, many methods described as improving the interpretability of deep learning models take disparate and often complementary approaches.

#### Assigning example-specific importance scores

Several approaches ascribe importance on an example-specific basis to the parts of the input that are responsible for a particular output.
These can be broadly divided into perturbation-based approaches and backpropagation-based approaches.

Perturbation-based approaches change parts of the input and observe the impact on the output of the network.
Alipanahi et al. [@tag:Alipanahi2015_predicting] and Zhou & Troyanskaya [@tag:Zhou2015_deep_sea] scored genomic sequences by introducing virtual mutations at individual positions in the sequence and quantifying the change in the output.
Umarov et al. [@doi:10.1371/journal.pone.0171410] used a similar strategy, but with sliding windows where the sequence within each sliding window was substituted with a random sequence.
Kelley et al. [@tag:Kelley2016_basset] inserted known protein-binding motifs into the centers of sequences and assessed the change in predicted accessibility.
Ribeiro et al. [@tag:Ribeiro2016_lime] introduced LIME, which constructs a linear model to locally approximate the output of the network on perturbed versions of the input and assigns importance scores accordingly.
For analyzing images, Zeiler and Fergus [@tag:Zeiler2013_visualizing] applied constant-value masks to different input patches.
More recently, marginalizing over the plausible values of an input has been suggested as a way to more accurately estimate contributions [@tag:Zintgraf2017_visualizing].

A common drawback to perturbation-based approaches is computational efficiency:
each perturbed version of an input requires a separate forward propagation through the network to compute the output.
As noted by Shrikumar et al. [@tag:Shrikumar2017_learning], such methods may also underestimate the impact of features that have saturated their contribution to the output, as can happen when multiple redundant features are present.
To reduce the computational overhead of perturbation-based approaches, Fong and Vedaldi [@tag:Fong2017_perturb] solve an optimization problem using gradient descent to discover a minimal subset of inputs to perturb in order to decrease the predicted probability of a selected class.
Their method converges in many fewer iterations but requires the perturbation to have a differentiable form.

Backpropagation-based methods, in which the signal from a target output neuron is propagated backwards to the input layer, are another way to interpret deep networks that sidestep inefficiencies of the perturbation-based methods.
A classic example of this is calculating the gradients of the output with respect to the input [@tag:Simonyan2013_deep] to compute a "saliency map".
Bach et al. [@tag:Bach2015_on] proposed a strategy called Layerwise Relevance Propagation, which was shown to be equivalent to the element-wise product of the gradient and input [@tag:Shrikumar2017_learning; @tag:Kindermans2016_investigating].
Networks with Rectified Linear Units (ReLUs) create nonlinearities that must be addressed.
Several variants exist for handling this [@tag:Zeiler2013_visualizing; @tag:Springenberg2014_striving].
Backpropagation-based methods are a highly active area of research.
Researchers are still actively identifying weaknesses [@tag:Mahendran2016_salient], and new methods are being developed to address them [@tag:Selvaraju2016_grad;; @tag:Sundararajan2017_axiomatic; @tag:Shrikumar2017_learning].
Lundberg and Lee [@tag:Lundberg2016_an] noted that several importance scoring methods including integrated gradients and LIME could all be considered approximations to Shapely values [@tag:Shapely], which have a long history in game theory for assigning contributions to players in cooperative games.

#### Matching or exaggerating the hidden representation

Another approach to understanding the network's predictions is to find artificial inputs that produce similar hidden representations to a chosen example.
This can elucidate the features that the network uses for prediction and drop the features that the network is insensitive to.
In the context of natural images, Mahendran and Vedaldi [@tag:Mahendran2014_understanding] introduced the "inversion" visualization, which uses gradient descent and backpropagation to reconstruct the input from its hidden representation.
The method required placing a prior on the input to favor results that resemble natural images.
For genomic sequence, Finnegan and Song [@tag:Finnegan2017_maximum] used a Markov chain Monte Carlo algorithm to find the maximum-entropy distribution of inputs that produced a similar hidden representation to the chosen input.

A related idea is "caricaturization", where an initial image is altered to exaggerate patterns that the network searches for [@tag:Mahendran2016_visualizing].
This is done by maximizing the response of neurons that are active in the network, subject to some regularizing constraints.
Mordvintsev et al. [@tag:Mordvintsev2015_inceptionism] leveraged caricaturization to generate aesthetically pleasing images using neural networks.

#### Activation maximization

Activation maximization can reveal patterns detected by an individual neuron in the network by generating images which maximally activate that neuron, subject to some regularizing constraints.
This technique was first introduced in Ehran et al. [@tag:Ehran2009_visualizing] and applied in subsequent work [@tag:Simonyan2013_deep; @tag:Mordvintsev2015_inceptionism; @tag:Yosinksi2015_understanding; @tag:Mahendran2016_visualizing].
Lanchantin et al. [@tag:Lanchantin2016_motif] applied class-based activation maximization to genomic sequence data.
One drawback of this approach is that neural networks often learn highly distributed representations where several neurons cooperatively describe a pattern of interest.
Thus, visualizing patterns learned by individual neurons may not always be informative.

#### RNN-specific approaches

Several interpretation methods are specifically tailored to recurrent neural network architectures.
The most common form of interpretability provided by RNNs is through attention mechanisms, which have been used in diverse problems such as image captioning and machine translation to select portions of the input to focus on generating a particular output [@tag:Bahdanu2014_neural; @tag:Xu2015_show].
Deming et al. [@tag:Deming2016_genetic] applied the attention mechanism to models trained on genomic sequence.
Attention mechanisms provide insight into the model's decision-making process by revealing which portions of the input are used by different outputs.
Singh et al. used a hierarchy of attention layers to locate important genome positions and signals for predicting gene expression from histone modifications [@tag:Singh2017_attentivechrome].
In the clinical domain, Choi et al.
[@tag:Choi2016_retain] leveraged attention mechanisms to highlight which aspects of a patient's medical history were most relevant for making diagnoses.
Choi et al. [@tag:Choi2016_gram] later extended this work to take into account the structure of disease ontologies and found that the concepts represented by the model aligned with medical knowledge.
Note that interpretation strategies that rely on an attention mechanism do not provide insight into the logic used by the attention layer.

Visualizing the activation patterns of the hidden state of a recurrent neural network can also be instructive.
Early work by Ghosh and Karamcheti [@tag:Ghosh1992_sequence] used cluster analysis to study hidden states of comparatively small networks trained to recognize strings from a finite state machine.
More recently, Karpathy et al. [@tag:Karpathy2015_visualizing] showed the existence of individual cells in LSTMs that kept track of quotes and brackets in character-level language models.
To facilitate such analyses, LSTMVis [@tag:Strobelt2016_visual] allows interactive exploration of the hidden state of LSTMs on different inputs.

Another strategy, adopted by Lanchatin et al. [@tag:Lanchantin2016_motif] looks at how the output of a recurrent neural network changes as longer and longer subsequences are supplied as input to the network, where the subsequences begin with just the first position and end with the entire sequence.
In a binary classification task, this can identify those positions which are responsible for flipping the output of the network from negative to positive.
If the RNN is bidirectional, the same process can be repeated on the reverse sequence.
As noted by the authors, this approach was less effective at identifying motifs compared to the gradient-based backpropagation approach of Simonyan et al.
[@tag:Simonyan2013_deep], illustrating the need for more sophisticated strategies to assign importance scores in recurrent neural networks.

Murdoch and Szlam [@tag:Murdoch2017_automatic] showed that the output of an LSTM can be decomposed into a product of factors, where each factor can be interpreted as the contribution at a particular timestep.
The contribution scores were then used to identify key phrases from a model trained for sentiment analysis and obtained superior results compared to scores derived via a gradient-based approach.

#### Latent space manipulation

Interpretation of embedded or latent space features learned through generative unsupervised models can reveal underlying patterns otherwise masked in the original input.
Embedded feature interpretation has been emphasized mostly in image and text based applications [@tag:Radford_dcgan; @tag:word2vec], but applications to genomic and biomedical domains are increasing.

For example, Way and Greene trained a VAE on gene expression from The Cancer Genome Atlas (TCGA) [@doi:10.1038/ng.2764] and use latent space arithmetic to rapidly isolate and interpret gene expression features descriptive of high grade serous ovarian cancer subtypes [@tag:WayGreene2017_tybalt].
The most differentiating VAE features were representative of biological processes that are known to distinguish the subtypes.
Latent space arithmetic with features derived using other compression algorithms were not as informative in this context [@tag:WayGreene2017_eval].
Embedding discrete chemical structures with autoencoders and interpreting the learned continuous representations with latent space arithmetic has also facilitated predicting drug-like compounds [@tag:Gomezb2016_automatic].
Furthermore, embedding biomedical text into lower dimensional latent spaces have improved name entity recognition in a variety of tasks including annotating clinical abbreviations, genes, cell lines, and drug names [@doi:10.3390/info6040848; @doi:10.1155/2014/240403; @doi:10.18653/v1/w15-3822; @doi:10.18653/v1/w15-3810].

Other approaches have used interpolation through latent space embeddings learned by GANs to interpret unobserved intermediate states.
For example, Osokin et al. trained GANs on two-channel fluorescent microscopy images to interpret intermediate states of protein localization in yeast cells [@tag:Osokin2017_biogan].
Goldsborough et al. trained a GAN on fluorescent microscopy images and used latent space interpolation and arithmetic to reveal underlying responses to small molecule perturbations in cell lines [@tag:Goldsborough2017_cytogan].

#### Miscellaneous approaches

It can often be informative to understand how the training data affects model learning.
Toward this end, Koh and Liang [@tag:Koh2017_understanding] used influence functions, a technique from robust statistics, to trace a model's predictions back through the learning algorithm to identify the datapoints in the training set that had the most impact on a given prediction.
A more free-form approach to interpretability is to visualize the activation patterns of the network on individual inputs and on subsets of the data.
ActiVis and CNNvis [@tag:Kahng2017_activis; @tag:Liu2016_towards] are two frameworks that enable interactive visualization and exploration of large-scale deep learning models.
An orthogonal strategy is to use a knowledge distillation approach to replace a deep learning model with a more interpretable model that achieves comparable performance.
Towards this end, Che et al. [@tag:Che2015_distill] used gradient boosted trees to learn interpretable healthcare features from trained deep models.

Finally, it is sometimes possible to train the model to provide justifications for its predictions.
Lei et al. [@tag:Lei2016_rationalizing] used a generator to identify "rationales", which are short and coherent pieces of the input text that produce similar results to the whole input when passed through an encoder.
The authors applied their approach to a sentiment analysis task and obtained substantially superior results compared to an attention-based method.

#### Future outlook

While deep learning lags behind most Bayesian models in terms of interpretability, the interpretability of deep learning is comparable to or exceeds that of many other widely-used machine learning methods such as random forests or SVMs.
While it is possible to obtain importance scores for different inputs in a random forest, the same is true for deep learning.
Similarly, SVMs trained with a nonlinear kernel are not easily interpretable because the use of the kernel means that one does not obtain an explicit weight matrix.
Finally, it is worth noting that some simple machine learning methods are less interpretable in practice than one might expect.
A linear model trained on heavily engineered features might be difficult to interpret as the input features themselves are difficult to interpret.
Similarly, a decision tree with many nodes and branches may also be difficult for a human to make sense of.

There are several directions that might benefit the development of interpretability techniques.
The first is the introduction of gold standard benchmarks that different interpretability approaches could be compared against, similar in spirit to how the ImageNet [@doi:10.1007/s11263-015-0816-y] and CIFAR [@tag:krizhevsky-2009] datasets spurred the development of deep learning for computer vision.
It would also be helpful if the community placed more emphasis on domains outside of computer vision.
Computer vision is often used as the example application of interpretability methods, but it is not the domain with the most pressing need.
Finally, closer integration of interpretability approaches with popular deep learning frameworks would make it easier for practitioners to apply and experiment with different approaches to understanding their deep learning models.

### Data limitations

A lack of large-scale, high-quality, correctly labeled training data has impacted deep learning in nearly all applications we have discussed.
The challenges of training complex, high-parameter neural networks from few examples are obvious, but uncertainty in the labels of those examples can be just as problematic.
In genomics labeled data may be derived from an experimental assay with known and unknown technical artifacts, biases, and error profiles.
It is possible to weight training examples or construct Bayesian models to account for uncertainty or non-independence in the data, as described in the TF binding example above.
As another example, Park et al. [@doi:10.1371/journal.pcbi.1002957] estimated shared non-biological signal between datasets to correct for non-independence related to assay platform or other factors in a Bayesian integration of many datasets.
However, such techniques are rarely placed front and center in any description of methods and may be easily overlooked.

For some types of data, especially images, it is straightforward to augment training datasets by splitting a single labeled example into multiple examples.
For example, an image can easily be rotated, flipped, or translated and retain its label [@doi:10.1101/095794].
3D MRI and 4D fMRI (with time as a dimension) data can be decomposed into sets of 2D images [@doi:10.1101/070441].
This can greatly expand the number of training examples but artificially treats such derived images as independent instances and sacrifices the structure inherent in the data.
CellCnn trains a model to recognize rare cell populations in single-cell data by creating training instances that consist of subsets of cells that are randomly sampled with replacement from the full dataset [@tag:Arvaniti2016_rare_subsets].

Simulated or semi-synthetic training data has been employed in multiple biomedical domains, though many of these ideas are not specific to deep learning.
Training and evaluating on simulated data, for instance, generating synthetic TF binding sites with position weight matrices [@tag:Shrikumar2017_reversecomplement] or RNA-seq reads for predicting mRNA transcript boundaries [@doi:10.1101/125229], is a standard practice in bioinformatics.
This strategy can help benchmark algorithms when the available gold standard dataset is imperfect, but it should be paired with an evaluation on real data, as in the prior examples [@tag:Shrikumar2017_reversecomplement; @doi:10.1101/125229].
In rare cases, models trained on simulated data have been successfully applied directly to real data [@doi:10.1101/125229].

Data can be simulated to create negative examples when only positive training instances are available.
DANN [@doi:10.1093/bioinformatics/btu703] adopts this approach to predict the pathogenicity of genetic variants using semi-synthetic training data from Combined Annotation-Dependent Depletion (CADD)
[@doi:10.1038/ng.2892].
Though our emphasis here is on the training strategy, it should be noted that logistic regression outperformed DANN when distinguishing known pathogenic mutations from likely benign variants in real data.
Similarly, a somatic mutation caller has been trained by injecting mutations into real sequencing datasets [@tag:Torracinta2016_sim; @doi:10.1101/093534].

In settings where the experimental observations are biased toward positive instances, such as MHC protein and peptide ligand binding affinity [@doi:10.1101/054775], or the negative instances vastly outnumber the positives, such as high-throughput chemical screening [@tag:Lusci2015_irv], training datasets have been augmented by adding additional instances and assuming they are negative.
There is some evidence that this can improve performance [@tag:Lusci2015_irv], but in other cases it was only beneficial when the real training datasets were extremely small [@doi:10.1101/054775].
Overall, training with simulated and semi-simulated data is a valuable idea for overcoming limited sample sizes but one that requires more rigorous evaluation on real ground-truth datasets before we can recommend it for widespread use.
There is a risk that a model will easily discriminate synthetic examples but not generalize to real data.

Multimodal, multi-task, and transfer learning, discussed in detail below, can also combat data limitations to some degree.
There are also emerging network architectures, such as Diet Networks for high-dimensional SNP data [@tag:Romero2017_diet].
These use multiple networks to drastically reduce the number of free parameters by first flipping the problem and training a network to predict parameters (weights) for each input (SNP) to learn a feature embedding.
This embedding (e.g. from principal component analysis, per class histograms, or a word2vec [@tag:word2vec] generalization) can be learned directly from input data or take advantage of other datasets or domain knowledge.
Additionally, in this task the features are the examples, an important advantage when it is typical to have 500 thousand or more SNPs and only a few thousand patients.
Finally, this embedding is of a much lower dimension, allowing for a large reduction in the number of free parameters.
In the example given, the number of free parameters was reduced from 30 million to 50 thousand, a factor of 600.

### Hardware limitations and scaling

Efficiently scaling deep learning is challenging, and there is a high computational cost (e.g. time, memory, and energy) associated with training neural networks and using them to make predictions.
This is one of the reasons why neural networks have only recently found widespread use [@tag:Schmidhuber2014_dnn_overview].

Many have sought to curb these costs, with methods ranging from the very applied (e.g. reduced numerical precision [@tag:Gupta2015_prec; @tag:Bengio2015_prec; @tag:Sa2015_buckwild; @tag:Hubara2016_qnn]) to the exotic and theoretic (e.g. training small networks to mimic large networks and ensembles [@tag:Caruana2014_need; @tag:Hinton2015_dark_knowledge]).
The largest gains in efficiency have come from computation with GPUs [@tag:Raina2009_gpu; @tag:Vanhoucke2011_cpu; @tag:Seide2014_parallel; @tag:Hadjas2015_cc; @tag:Edwards2015_growing_pains; @tag:Schmidhuber2014_dnn_overview], which excel at the matrix and vector operations so central to deep learning.
The massively parallel nature of GPUs allows additional optimizations, such as accelerated mini-batch gradient descent [@tag:Vanhoucke2011_cpu; @tag:Seide2014_parallel; @tag:Su2015_gpu; @tag:Li2014_minibatch].
However, GPUs also have limited memory, making networks of useful size and complexity difficult to implement on a single GPU or machine [@tag:Raina2009_gpu; @tag:Krizhevsky2013_nips_cnn].
This restriction has sometimes forced computational biologists to use workarounds or limit the size of an analysis.
Chen et al. [@tag:Chen2016_gene_expr] inferred the expression level of all genes with a single neural network, but due to memory restrictions they randomly partitioned genes into two separately analyzed halves.
In other cases, researchers limited the size of their neural network [@tag:Wang2016_protein_contact] or the total number of training instances [@tag:Gomezb2016_automatic].
Some have also chosen to use standard central processing unit (CPU) implementations rather than sacrifice network size or performance [@tag:Yasushi2016_cgbvs_dnn].

While steady improvements in GPU hardware may alleviate this issue, it is unclear whether advances will occur quickly enough to keep pace with the growing biological datasets and increasingly complex neural networks.
Much has been done to minimize the memory requirements of neural networks [@tag:CudNN; @tag:Caruana2014_need; @tag:Gupta2015_prec; @tag:Bengio2015_prec; @tag:Sa2015_buckwild; @tag:Chen2015_hashing; @tag:Hubara2016_qnn], but there is also growing interest in specialized hardware, such as field-programmable gate arrays (FPGAs) [@tag:Edwards2015_growing_pains; @tag:Lacey2016_dl_fpga] and application-specific integrated circuits (ASICs) [@arxiv:1704.04760].
Less software is available for such highly specialized hardware [@tag:Lacey2016_dl_fpga].
But specialized hardware promises improvements in deep learning at reduced time, energy, and memory [@tag:Edwards2015_growing_pains].
Specialized hardware may be a difficult investment for those not solely interested in deep learning, but for those with a deep learning focus these solutions may become popular.

Distributed computing is a general solution to intense computational requirements and has enabled many large-scale deep learning efforts.
Some types of distributed computation [@tag:Mapreduce; @tag:Graphlab] are not suitable for deep learning [@tag:Dean2012_nips_downpour], but much progress has been made.
There now exist a number of algorithms [@tag:Dean2012_nips_downpour; @tag:Sa2015_buckwild], tools [@tag:Moritz2015_sparknet; @tag:Meng2016_mllib; @tag:TensorFlow], and high-level libraries [@tag:Keras; @tag:Elephas] for deep learning in a distributed environment, and it is possible to train very complex networks with limited infrastructure [@tag:Coates2013_cots_hpc].
Besides handling very large networks, distributed or parallelized approaches offer other advantages, such as improved ensembling [@tag:Sun2016_ensemble] or accelerated hyperparameter optimization [@tag:Bergstra2011_hyper; @tag:Bergstra2012_random].

Cloud computing, which has already seen wide adoption in genomics [@tag:Schatz2010_dna_cloud], could facilitate easier sharing of the large datasets common to biology [@tag:Gerstein2016_scaling; @tag:Stein2010_cloud], and may be key to scaling deep learning.
Cloud computing affords researchers flexibility, and enables the use of specialized hardware (e.g. FPGAs, ASICs, GPUs) without major investment.
As such, it could be easier to address the different challenges associated with the multitudinous layers and architectures available [@tag:Krizhevsky2014_weird_trick].
Though many are reluctant to store sensitive data (e.g. patient electronic health records) in the cloud, secure, regulation-compliant cloud services do exist [@tag:RAD2010_view_cc].

### Data, code, and model sharing

A robust culture of data, code, and model sharing would speed advances in this domain.
The cultural barriers to data sharing in particular are perhaps best captured by the use of the term "research parasite" to describe scientists who use data from other researchers [@doi:10.1056/NEJMe1516564].
A field that honors only discoveries and not the hard work of generating useful data will have difficulty encouraging scientists to share their hard-won data.
It's precisely those data that would help to power deep learning in the domain.
Efforts are underway to recognize those who promote an ecosystem of rigorous sharing and analysis [@doi:10.1038/ng.3830].

The sharing of high-quality, labeled datasets will be especially valuable.
In addition, researchers who invest time to preprocess datasets to be suitable for deep learning can make the preprocessing code (e.g. Basset [@tag:Kelley2016_basset] and variationanalysis [@tag:Torracinta2016_deep_snp])
and cleaned data (e.g. MoleculeNet [@tag:Wu2017_molecule_net]) publicly available to catalyze further research.
However, there are complex privacy and legal issues involved in sharing patient data that cannot be ignored.
Solving these issues will require increased understanding of privacy risks and standards specifying acceptable levels.
In some domains high-quality training data has been generated privately, i.e. high-throughput chemical screening data at pharmaceutical companies.
One perspective is that there is little expectation or incentive for this private data to be shared.
However, data are not inherently valuable.
Instead, the insights that we glean from them are where the value lies.
Private companies may establish a competitive advantage by releasing data sufficient for improved methods to be developed.
Recently, Ramsundar et al. did this with an open source platform DeepChem, where they released four privately generated datasets [@doi:10.1021/acs.jcim.7b00146].

Code sharing and open source licensing is essential for continued progress in this domain.
We strongly advocate following established best practices for sharing source code, archiving code in repositories that generate digital object identifiers, and open licensing [@doi:10.1126/science.aah6168] regardless of the minimal requirements, or lack thereof, set by journals, conferences, or preprint servers.
In addition, it is important for authors to share not only code for their core models but also scripts and code used for data cleaning (see above)
and hyperparameter optimization.
These improve reproducibility and serve as documentation of the detailed decisions that impact model performance but may not be exhaustively captured in a manuscript's methods text.

Because many deep learning models are often built using one of several popular software frameworks, it is also possible to directly share trained predictive models.
The availability of pre-trained models can accelerate research, with image classifiers as an apt example.
A pre-trained neural network can be quickly fine-tuned on new data and used in transfer learning, as discussed below.
Taking this idea to the extreme, genomic data has been artificially encoded as images in order to benefit from pre-trained image classifiers [@tag:Poplin2016_deepvariant].
"Model zoos"---collections of pre-trained models---are not yet common in biomedical domains but have started to appear in genomics applications [@tag:Angermueller2016_single_methyl; @tag:Dragonn].
However, it is important to note that sharing models trained on individual data requires great care because deep learning models can be attacked to identify examples used in training.
One possible solution to protect individual samples includes training models under differential privacy [@doi:10.1145/2976749.2978318], which has been used in the biomedical domain [@doi:10.1101/159756].
We discussed this issue as well as recent techniques to mitigate these concerns in the patient categorization section.

DeepChem [@tag:AltaeTran2016_one_shot; @tag:DeepChem; @tag:Wu2017_molecule_net] and DragoNN (Deep RegulAtory GenOmic Neural Networks) [@tag:Dragonn] exemplify the benefits of sharing pre-trained models and code under an open source license.
DeepChem, which targets drug discovery and quantum chemistry, has actively encouraged and received community contributions of learning algorithms and benchmarking datasets.
As a consequence, it now supports a large suite of machine learning approaches, both deep learning and competing strategies, that can be run on diverse test cases.
This realistic, continual evaluation will play a critical role in assessing which techniques are most promising for chemical screening and drug discovery.
Like formal, organized challenges such as the ENCODE-DREAM *in vivo*
Transcription Factor Binding Site Prediction Challenge [@tag:Dream_tf_binding], DeepChem provides a forum for the fair, critical evaluations that are not always conducted in individual methodological papers, which can be biased toward favoring a new proposed algorithm.
Likewise DragoNN offers not only code and a model zoo but also a detailed tutorial and partner package for simulating training data.
These resources, especially the ability to simulate datasets that are sufficiently complex to demonstrate the challenges of training neural networks but small enough to train quickly on a CPU, are important for training students and attracting machine learning researchers to problems in genomics and healthcare.

### Multimodal, multi-task, and transfer learning

The fact that biomedical datasets often contain a limited number of instances or labels can cause poor performance of deep learning algorithms.
These models are particularly prone to overfitting due to their high representational power.
However, transfer learning techniques, also known as domain adaptation, enable transfer of extracted patterns between different datasets and even domains.
This approach consists of training a model for the base task and subsequently reusing the trained model for the target problem.
The first step allows a model to take advantage of a larger amount of data and/or labels to extract better feature representations.
Transferring learned features in deep neural networks improves performance compared to randomly initialized features even when pre-training and target sets are dissimilar.
However, transferability of features decreases as the distance between the base task and target task increases [@tag:Yosinski2014].

In image analysis, previous examples of deep transfer learning applications proved large-scale natural image sets [@tag:Russakovsky2015_imagenet] to be useful for pre-training models that serve as generic feature extractors for various types of biological images [@tag:Zhang2015_multitask_tl; @tag:Zeng2015; @tag:Angermueller2016_dl_review; @tag:Pawlowski2016].
More recently, deep learning models predicted protein sub-cellular localization for proteins not originally present in a training set [@tag:Parnamaa2017].
Moreover, learned features performed reasonably well even when applied to images obtained using different fluorescent labels, imaging techniques, and different cell types [@tag:Kraus2017_deeploc].
However, there are no established theoretical guarantees for feature transferability between distant domains such as natural images and various modalities of biological imaging.
Because learned patterns are represented in deep neural networks in a layer-wise hierarchical fashion, this issue is usually addressed by fixing an empirically chosen number of layers that preserve generic characteristics of both training and target datasets.
The model is then fine-tuned by re-training top layers on the specific dataset in order to re-learn domain-specific high level concepts (e.g. fine-tuning for radiology image classification [@tag:Rajkomar2017_radiographs]).
Fine-tuning on specific biological datasets enables more focused predictions.

In genomics, the Basset package [@tag:Kelley2016_basset] for predicting chromatin accessibility was shown to rapidly learn and accurately predict on new data by leveraging a model pre-trained on available public data.
To simulate this scenario, authors put aside 15 of 164 cell type datasets and trained the Basset model on the remaining 149 datasets.
Then, they fine-tuned the model with one training pass of each of the remaining datasets and achieved results close to the model trained on all 164 datasets together.
In another example, Min et al. [@tag:Min2016_deepenhancer] demonstrated how training on the experimentally-validated FANTOM5 permissive enhancer dataset followed by fine-tuning on ENCODE enhancer datasets improved cell type-specific predictions, outperforming state-of-the-art results.
In drug design, general RNN models trained to generate molecules from the ChEMBL database have been fine-tuned to produce drug-like compounds for specific targets [@tag:Segler2017_drug_design; @tag:Olivecrona2017_drug_design].

Related to transfer learning, multimodal learning assumes simultaneous learning from various types of inputs, such as images and text.
It can capture features that describe common concepts across input modalities.
Generative graphical models like RBMs, deep Boltzmann machines, and DBNs, demonstrate successful extraction of more informative features for one modality (images or video) when jointly learned with other modalities (audio or text) [@tag:Ngiam2011].
Deep graphical models such as DBNs are well-suited for multimodal learning tasks because they learn a joint probability distribution from inputs.
They can be pre-trained in an unsupervised fashion on large unlabeled data and then fine-tuned on a smaller number of labeled examples.
When labels are available, convolutional neural networks are ubiquitously used because they can be trained end-to-end with backpropagation and demonstrate state-of-the-art performance in many discriminative tasks [@tag:Angermueller2016_dl_review].

Jha et al. [@tag:Jha2017_integrative_models] showed that integrated training delivered better performance than individual networks.
They compared a number of feed-forward architectures trained on RNA-seq data with and without an additional set of CLIP-seq, knockdown, and over-expression based input features.
The integrative deep model generalized well for combined data, offering a large performance improvement for alternative splicing event estimation.
Chaudhary et al. [@tag:Chaudhary2017_multiom_liver_cancer] trained a deep autoencoder model jointly on RNA-seq, miRNA-seq, and methylation data from TCGA to predict survival subgroups of hepatocellular carcinoma patients.
This multimodal approach that treated different omic data types as different modalities outperformed both traditional methods (principal component analysis)
and single-omic models.
Interestingly, multi-omic model performance did not improve when combined with clinical information, suggesting that the model was able to capture redundant contributions of clinical features through their correlated genomic features.
Chen et al. [@tag:Chen2015_trans_species] used deep belief networks to learn phosphorylation states of a common set of signaling proteins in primary cultured bronchial cells collected from rats and humans treated with distinct stimuli.
By interpreting species as different modalities representing similar high-level concepts, they showed that DBNs were able to capture cross-species representation of signaling mechanisms in response to a common stimuli.
Another application used DBNs for joint unsupervised feature learning from cancer datasets containing gene expression, DNA methylation, and miRNA expression data [@tag:Liang2015_exprs_cancer].
This approach allowed for the capture of intrinsic relationships in different modalities and for better clustering performance over conventional k-means.

Multimodal learning with CNNs is usually implemented as a collection of individual networks in which each learns representations from single data type.
These individual representations are further concatenated before or within fully-connected layers.
FIDDLE [@tag:Eser2016_fiddle] is an example of a multimodal CNN that represents an ensemble of individual networks that take NET-seq, MNase-seq, ChIP-seq, RNA-seq, and raw DNA sequence as input to predict transcription start sites.
The combined model radically improves performance over separately trained datatype-specific networks, suggesting that it learns the synergistic relationship between datasets.

Multi-task learning is an approach related to transfer learning.
In a multi-task learning framework, a model learns a number of tasks simultaneously such that features are shared across them.
DeepSEA [@tag:Zhou2015_deep_sea] implemented multi-task joint learning of diverse chromatin factors from raw DNA sequence.
This allowed a sequence feature that was effective in recognizing binding of a specific TF to be simultaneously used by another predictor for a physically interacting TF.
Similarly, TFImpute [@tag:Qin2017_onehot] learned information shared across transcription factors and cell lines to predict cell-specific TF binding for TF-cell line combinations.
Yoon et al. [@tag:Yoon2016_cancer_reports] demonstrated that predicting the primary cancer site from cancer pathology reports together with its laterality substantially improved the performance for the latter task, indicating that multi-task learning can effectively leverage the commonality between two tasks using a shared representation.
Many studies employed multi-task learning to predict chemical bioactivity [@tag:Dahl2014_multi_qsar; @tag:Ramsundar2015_multitask_drug] and drug toxicity [@tag:Mayr2016_deep_tox; @tag:Hughes2016_macromol_react].
Kearnes et al. [@tag:Kearnes2016_admet] systematically compared single-task and multi-task models for ADMET properties and found that multi-task learning generally improved performance.
Smaller datasets tended to benefit more than larger datasets.

Multi-task learning is complementary to multimodal and transfer learning.
All three techniques can be used together in the same model.
For example, Zhang et al. [@tag:Zhang2015_multitask_tl] combined deep model-based transfer and multi-task learning for cross-domain image annotation.
One could imagine extending that approach to multimodal inputs as well.
A common characteristic of these methods is better generalization of extracted features at various hierarchical levels of abstraction, which is attained by leveraging relationships between various inputs and task objectives.

Despite demonstrated improvements, transfer learning approaches pose challenges.
There are no theoretically sound principles for pre-training and fine-tuning.
Best practice recommendations are heuristic and must account for additional hyper-parameters that depend on specific deep architectures, sizes of the pre-training and target datasets, and similarity of domains.
However, similarity of datasets and domains in transfer learning and relatedness of tasks in multi-task learning are difficult to access.
Most studies address these limitations by empirical evaluation of the model.
Unfortunately, negative results are typically not reported.
A deep CNN trained on natural images boosts performance in radiographic images [@tag:Rajkomar2017_radiographs].
However, due to differences in imaging domains, the target task required either re-training the initial model from scratch with special pre-processing or fine-tuning of the whole network on radiographs with heavy data augmentation to avoid overfitting.
Exclusively fine-tuning top layers led to much lower validation accuracy (81.4 versus 99.5).
Fine-tuning the aforementioned Basset model with more than one pass resulted in overfitting [@tag:Kelley2016_basset].
DeepChem successfully improved results for low-data drug discovery with one-shot learning for related tasks.
However, it clearly demonstrated the limitations of cross-task generalization across unrelated tasks in one-shot models, specifically nuclear receptor assays and patient adverse reactions [@tag:AltaeTran2016_one_shot].

In the medical domain, multimodal, multi-task and transfer learning strategies not only inherit most methodological issues from natural image, text, and audio domains, but also pose domain-specific challenges.
There is a compelling need for the development of privacy-preserving transfer learning algorithms, such as Private Aggregation of Teacher Ensembles [@tag:Papernot2017_pate].
We suggest that these types of models deserve deeper investigation to establish sound theoretical guarantees and determine limits for the transferability of features between various closely related and distant learning tasks.


## Conclusions

Deep learning-based methods now match or surpass the previous state of the art in a diverse array of tasks in patient and disease categorization, fundamental biological study, genomics, and treatment development.
Returning to our central question: given this rapid progress, has deep learning transformed the study of human disease? Though the answer is highly dependent on the specific domain and problem being addressed, we conclude that deep learning has not yet realized its transformative potential or induced a strategic inflection point.
Despite its dominance over competing machine learning approaches in many of the areas reviewed here and quantitative improvements in predictive performance, deep learning has not yet definitively "solved" these problems.

As an analogy, consider recent progress in conversational speech recognition.
Since 2009 there have been drastic performance improvements with error rates dropping from more than 20% to less than 6% [@tag:Speech_recognition] and finally approaching or exceeding human performance in the past year [@arxiv:1610.05256; @arxiv:1703.02136].
The phenomenal improvements on benchmark datasets are undeniable, but greatly reducing the error rate on these benchmarks did not fundamentally transform the domain.
Widespread adoption of conversational speech technologies will require solving the problem, i.e. methods that surpass human performance, and persuading users to adopt them [@tag:Speech_recognition].
We see parallels in healthcare, where achieving the full potential of deep learning will require outstanding predictive performance as well as acceptance and adoption by biologists and clinicians.
These experts will rightfully demand rigorous evidence that deep learning has impacted their respective disciplines---elucidated new biological mechanisms and improved patient outcomes---to be convinced that the promises of deep learning are more substantive than those of previous generations of artificial intelligence.

Some of the areas we have discussed are closer to surpassing this lofty bar than others, generally those that are more similar to the non-biomedical tasks that are now monopolized by deep learning.
In medical imaging, diabetic retinopathy [@doi:10.1001/jama.2016.17216], diabetic macular edema [@doi:10.1001/jama.2016.17216], tuberculosis [@doi:10.1148/radiol.2017162326], and skin lesion [@doi:10.1038/nature21056] classifiers are highly accurate and comparable to clinician performance.

In other domains, perfect accuracy will not be required because deep learning will primarily prioritize experiments and assist discovery.
For example, in chemical screening for drug discovery, a deep learning system that successfully identifies dozens or hundreds of target-specific, active small molecules from a massive search space would have immense practical value even if its overall precision is modest.
In medical imaging, deep learning can point an expert to the most challenging cases that require manual review [@doi:10.1148/radiol.2017162326], though the risk of false negatives must be addressed.
In protein structure prediction, errors in individual residue-residue contacts can be tolerated when using the contacts jointly for 3D structure modeling.
Improved contact map predictions [@tag:Wang2016_protein_contact] have led to notable improvements in fold and 3D structure prediction for some of the most challenging proteins, such as membrane proteins [@arxiv:1704.07207].

Conversely, the most challenging tasks may be those in which predictions are used directly for downstream modeling or decision-making, especially in the clinic.
As an example, errors in sequence variant calling will be amplified if they are used directly for GWAS.
In addition, the stochasticity and complexity of biological systems implies that for some problems, for instance predicting gene regulation in disease, perfect accuracy will be unattainable.

We are witnessing deep learning models achieving human-level performance across a number of biomedical domains.
However, machine learning algorithms, including deep neural networks, are also prone to mistakes that humans are much less likely to make, such as misclassification of adversarial examples [@arxiv:1312.6199; @arxiv:1412.6572], a reminder that these algorithms do not understand the semantics of the objects presented.
It may be impossible to guarantee that a model is not susceptible to adversarial examples, but work in this area is continuing [@arxiv:1611.03814; @arxiv:1704.01155].
Cooperation between human experts and deep learning algorithms addresses many of these challenges and can achieve better performance than either individually [@arxiv:1606.05718].
For sample and patient classification tasks, we expect deep learning methods to augment clinicians and biomedical researchers.

We are optimistic about the future of deep learning in biology and medicine.
It is by no means inevitable that deep learning will revolutionize these domains, but given how rapidly the field is evolving, we are confident that its full potential in biomedicine has not been explored.
We have highlighted numerous challenges beyond improving training and predictive accuracy, such as preserving patient privacy and interpreting models.
Ongoing research has begun to address these problems and shown that they are not insurmountable.
Deep learning offers the flexibility to model data in its most natural form, for example, longer DNA sequences instead of k-mers for transcription factor binding prediction and molecular graphs instead of pre-computed bit vectors for drug discovery.
These flexible input feature representations have spurred creative modeling approaches that would be infeasible with other machine learning techniques.
Unsupervised methods are currently less-developed than their supervised counterparts, but they may have the most potential because of how expensive and time-consuming it is to label large amounts of biomedical data.
If future deep learning algorithms can summarize very large collections of input data into interpretable models that spur scientists to ask questions that they did not know how to ask, it will be clear that deep learning has transformed biology and medicine.


## Methods

### Continuous collaborative manuscript drafting

We recognized that deep learning in precision medicine is a rapidly developing area.
Hence, diverse expertise was required to provide a forward-looking perspective.
Accordingly, we collaboratively wrote this review in the open, enabling anyone with expertise to contribute.
We wrote the manuscript in markdown and tracked changes using git.
Contributions were handled through GitHub, with individuals submitting "pull requests" to suggest additions to the manuscript.
This collaborative writing approach was later generalized into [Manubot](https://manubot.org/) [@doi:10.1371/journal.pcbi.1007128].

Manubot supports citations of persistent identifiers, such as DOIs, PubMed Central IDs, PubMed IDs, arXiv IDs, and URLs.
This reduces one major barrier to writing collaboratively, which is syncing reference managers between participants.
In addition, Manubot uses continuous integration to build and deploy manuscripts.
This allows for automated error checking of proposed changes to catch malformated citations and invalid syntax.
Originally, the Deep Review used Travis CI for continuous integration, but in 2020 switched to GitHub Actions, which became the default for Manubot manuscripts.

For version 1.0 of the Deep Review, author order was randomized as described in [version 1.0] [@tag:techblog-perkel].
However, this was a one-time manual process.
Starting with version 2.0, we began shuffling authors for every manuscript version.
Manubot allowed us to automate this process, using the Git commit hash as a random seed to ensure reproducible ordering.

### Author contributions

#### Version 2.0

We continued using the open repository on the GitHub version control platform ([`greenelab/deep-review`](https://github.com/greenelab/deep-review)) [@url:https://github.com/greenelab/deep-review], which was established to write the version 1.0 manuscript.

  Drafted one or more subsections: Brock C. Christensen, Joshua J. Levy, Alexander J. Titus. 

  Drafted sub-sections, edited the manuscript, reviewed pull requests, and coordinated co-authors: Casey S. Greene. 

  Edited the manuscript, reviewed pull requests, and developed Manubot: Daniel S. Himmelstein. 


##### Version 2.0 competing interests

|Author|Competing Interests|Last Reviewed|
|---|---|---|
|Daniel S. Himmelstein|None|2020-03-10|
|Brock C. Christensen|None|2020-03-05|
|Joshua J. Levy|None|2020-03-04|
|Casey S. Greene|None|2020-03-10|
|Alexander J. Titus|None|2020-03-07|

##### Version 2.0 funding statement

We acknowledge funding from the Gordon and Betty Moore Foundation award GBMF4552 (C.S.G. and D.S.H.);
the National Institutes of Health awards R01HG010067 (C.S.G. and D.S.H.), R01CA237170 (C.S.G), T32LM012204 (A.J.T.), R01CA216265 (B.C.C.);
the Burroughs Wellcome Fund Big Data in the Life Sciences training grant at Dartmouth (J.L.L,);
and the Dartmouth College Neukom Institute for Computational Science CompX award (B.C.C.).

#### Version 1.0

We created an open repository on the GitHub version control platform ([`greenelab/deep-review`](https://github.com/greenelab/deep-review)) [@url:https://github.com/greenelab/deep-review].
Here, we engaged with numerous authors from papers within and outside of the area.
The manuscript was drafted via GitHub commits by individuals who met the ICMJE standards of authorship.
These were individuals who contributed to the review of the literature;
drafted the manuscript or provided substantial critical revisions;
approved the final manuscript draft; and agreed to be accountable in all aspects of the work.
Individuals who did not contribute in all of these ways, but who did participate, are acknowledged below.
We grouped authors into the following four classes of approximately equal contributions and randomly ordered authors within each contribution class.
Drafted multiple sub-sections along with extensive editing, pull request reviews, or discussion: Travers Ching, Brett K. Beaulieu-Jones, Alexandr A. Kalinin, Brian T. Do, Gregory P. Way, Enrico Ferrero, Paul-Michael Agapow, Michael Zietz, Michael M. Hoffman.
Edited the manuscript, reviewed pull requests, and developed Manubot: Daniel S. Himmelstein.
Drafted one or more sub-sections: Wei Xie, Gail L. Rosen, Benjamin J. Lengerich, Johnny Israeli, Jack Lanchantin, Stephen Woloszynek, Anne E. Carpenter, Avanti Shrikumar, Jinbo Xu, Evan M. Cofer, Christopher A. Lavender, Srinivas C. Turaga, Amr M. Alexandari, Zhiyong Lu.
Drafted sub-sections, edited the manuscript, reviewed pull requests, and coordinated co-authors: Anthony Gitter, Casey S. Greene.
Revised specific sub-sections or supervised drafting one or more sub-sections: David J. Harris, Dave DeCaprio, Yanjun Qi, Anshul Kundaje, Yifan Peng, Laura K. Wiley, Marwin H.S. Segler, Simina M. Boca, S. Joshua Swamidass, Austin Huang.

##### Version 1.0 competing interests

|Author|Competing Interests|Last Reviewed|
|---|---|---|
|Travers Ching|None|2017-05-26|
|Daniel S. Himmelstein|None|2017-05-26|
|Brett K. Beaulieu-Jones|None|2017-05-26|
|Alexandr A. Kalinin|None|2017-05-26|
|Brian T. Do|None|2017-05-26|
|Gregory P. Way|None|2017-05-26|
|Enrico Ferrero|Full-time employee of GlaxoSmithKline.|2017-05-26|
|Paul-Michael Agapow|None|2017-05-26|
|Michael Zietz|None|2017-05-26|
|Michael M. Hoffman|None|2017-05-26|
|Wei Xie|None|2017-05-26|
|Gail L. Rosen|None|2017-05-26|
|Benjamin J. Lengerich|None|2017-05-26|
|Johnny Israeli|None|2017-05-26|
|Jack Lanchantin|None|2017-05-26|
|Stephen Woloszynek|None|2017-05-26|
|Anne E. Carpenter|None|2017-05-26|
|Avanti Shrikumar|None|2017-05-26|
|Jinbo Xu|None|2017-05-26|
|Evan M. Cofer|None|2017-05-26|
|Christopher A. Lavender|None|2017-05-26|
|Srinivas C. Turaga|None|2017-05-26|
|Amr M. Alexandari|None|2017-05-26|
|Zhiyong Lu|None|2017-05-26|
|David J. Harris|None|2017-05-26|
|Dave DeCaprio|None|2017-05-26|
|Yanjun Qi|None|2017-05-26|
|Anshul Kundaje|Advisory Board of Deep Genomics Inc.|2017-05-26|
|Yifan Peng|None|2017-05-26|
|Laura K. Wiley|None|2017-05-26|
|Marwin H.S. Segler|None|2017-05-26|
|Simina M. Boca|None|2017-05-26|
|S. Joshua Swamidass|None|2017-05-26|
|Austin Huang|None|2017-05-26|
|Anthony Gitter|None|2017-05-26|
|Casey S. Greene|None|2017-05-26|

##### Version 1.0 funding statement

We acknowledge funding from the Gordon and Betty Moore Foundation awards GBMF4552 (C.S.G. and D.S.H.) and GBMF4563 (D.J.H.);
the Howard Hughes Medical Institute (S.C.T.);
the National Institutes of Health awards DP2GM123485 (A.K.), P30CA051008 (S.M.B.), R01AI116794 (B.K.B.), R01GM089652 (A.E.C.), R01GM089753 (J.X.), R01LM012222 (S.J.S.), R01LM012482 (S.J.S.), R21CA220398 (S.M.B.), T32GM007753 (B.T.D.), T32HG000046 (G.P.W.), and U54AI117924 (A.G.);
the National Institutes of Health Intramural Research Program and National Library of Medicine (Y.P. and Z.L.);
the National Science Foundation awards 1245632 (G.L.R.), 1531594 (E.M.C.), and 1564955 (J.X.);
the Natural Sciences and Engineering Research Council of Canada award RGPIN-2015-3948 (M.M.H.);
and the Roy and Diana Vagelos Scholars Program in the Molecular Life Sciences (M.Z.).

### Acknowledgements

We gratefully acknowledge Christof Angermueller, Kumardeep Chaudhary, Gökcen Eraslan, Mikael Huss, Bharath Ramsundar and Xun Zhu for their discussion of the manuscript and reviewed papers on GitHub.
We would like to thank Aaron Sheldon, who contributed text but did not formally approve the manuscript.
We would like to thank Anna Greene for a careful proofreading of the manuscript in advance of the first submission.
We would like to thank Sebastian Raschka for clarifying edits to the abstract and introduction.
We would like to thank Robert Gieseke, Ruibang Luo, Stephen Ra, Sourav Singh, and GitHub user snikumbh for correcting typos, formatting, and references.


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>

<!-- Define citation tags below -->
[@tag:Abe]: doi:10.1101/gr.634603
[@tag:Abramoff2016_dr]: doi:10.1167/iovs.16-19964
[@tag:Agarwal2015_targetscan]: doi:10.7554/eLife.05005
[@tag:Aitchison2017]: url:http://papers.nips.cc/paper/6940-model-based-bayesian-inference-of-neural-activity-and-connectivity-from-all-optical-interrogation-of-a-neural-circuit
[@tag:Alipanahi2015_predicting]: doi:10.1038/nbt.3300
[@tag:AltaeTran2016_one_shot]: doi:10.1021/acscentsci.6b00367
[@tag:Amit2017_breast_mri]: doi:10.1117/12.2249981
[@tag:Angermueller2016_dl_review]: doi:10.15252/msb.20156651
[@tag:Angermueller2016_single_methyl]: doi:10.1186/s13059-017-1189-z
[@tag:Angermueller2017]: doi:10.1186/s13059-017-1189-z
[@tag:Artemov2016_clinical]: doi:10.1101/095653
[@tag:Arvaniti2016_rare_subsets]: doi:10.1101/046508
[@tag:Asgari]: doi:10.1371/journal.pone.0141287
[@tag:Bach2015_on]: doi:10.1371/journal.pone.0130140
[@tag:Bahdanu2014_neural]: arxiv:1409.0473
[@tag:Bar2015_nonmed_tl]: doi:10.1117/12.2083124
[@tag:Barash2010_splicing_code]: doi:10.1038/nature09000
[@tag:Baskin2015_drug_disc]: doi:10.1080/17460441.2016.1201262
[@tag:Baxt1991_myocardial]: doi:10.7326/0003-4819-115-11-843
[@tag:BeaulieuJones2016_ehr_encode]: doi:10.1016/j.jbi.2016.10.007
[@tag:Belkin2019_PNAS]: doi:10.1073/pnas.1903070116
[@tag:Bengio2015_prec]: arxiv:1412.7024
[@tag:Berezikov2011_mirna]: doi:10.1038/nrg3079
[@tag:Bergstra2011_hyper]: url:https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf
[@tag:Bergstra2012_random]: url:http://www.jmlr.org/papers/v13/bergstra12a.html
[@tag:Boza]: doi:10.1371/journal.pone.0178751
[@tag:Bracken2016_mirna]: doi:10.1038/nrg.2016.134
[@tag:Buggenthin2017_imaged_lineage]: doi:10.1038/nmeth.4182
[@tag:Burlina2016_amd]: doi:10.1109/ISBI.2016.7493240
[@tag:Caruana2014_need]: arxiv:1312.6184
[@tag:Caruana2015_intelligible]: doi:10.1145/2783258.2788613
[@tag:Chatterjee2018]: arxiv:1807.09617
[@tag:Chaudhary2017_multiom_liver_cancer]: doi:10.1101/114892
[@tag:Che2015_distill]: arxiv:1512.03542
[@tag:Che2016_rnn]: arxiv:1606.01865
[@tag:Chen2015_hashing]: arxiv:1504.04788
[@tag:Chen2015_trans_species]: doi:10.1093/bioinformatics/btv315
[@tag:Chen2016_exprs_yeast]: doi:10.1186/s12859-015-0852-1
[@tag:Chen2016_gene_expr]: doi:10.1093/bioinformatics/btw074
[@tag:Choi2016_gram]: arxiv:1611.07012
[@tag:Choi2016_retain]: arxiv:1608.05745
[@tag:Chollet2016_xception]: arxiv:1610.02357
[@tag:Christensen2009]: doi:10.1371/journal.pgen.1000602
[@tag:Chryssolouris1996_confidence]: doi:10.1109/72.478409
[@tag:Ciresan2013_mitosis]: doi:10.1007/978-3-642-40763-5_51
[@tag:Coates2013_cots_hpc]: url:http://www.jmlr.org/proceedings/papers/v28/coates13.html
[@tag:Codella2016_ensemble_melanoma]: arxiv:1610.04662
[@tag:Consortium2012_encode]: doi:10.1038/nature11247
[@tag:CudNN]: arxiv:1410.0759
[@tag:Dahl2014_multi_qsar]: arxiv:1406.1231
[@tag:Darst2018]: doi:10.1186/s12863-018-0646-3
[@tag:Dean2012_nips_downpour]: url:http://research.google.com/archive/large_deep_networks_nips2012.html
[@tag:DeepChem]: url:https://github.com/deepchem/deepchem
[@tag:Deming2016_genetic]: arxiv:1605.07156
[@tag:Dhungel2015_struct_pred_mamm]: doi:10.1007/978-3-319-24553-9_74
[@tag:Dhungel2016_mamm]: doi:10.1007/978-3-319-46723-8_13
[@tag:Dhungel2017_mamm_min_interv]: doi:10.1016/j.media.2017.01.009
[@tag:Ding]: doi:10.1186/s12859-015-0753-3
[@tag:Ditzler2]: doi:10.1109/TNNLS.2014.2320415
[@tag:Ditzler3]: doi:10.1109/TNB.2015.2461219
[@tag:Ditzler]: doi:10.1186/s12859-015-0793-8
[@tag:Dragonn]: url:http://kundajelab.github.io/dragonn/
[@tag:Dream_tf_binding]: url:https://www.synapse.org/#!Synapse:syn6131484/wiki/402026
[@tag:Duvenaud2015_graph_conv]: url:http://papers.nips.cc/paper/5954-convolutional-networks-on-graphs-for-learning-molecular-fingerprints
[@tag:Edwards2015_growing_pains]: doi:10.1145/2771283
[@tag:Ehran2009_visualizing]: url:http://www.iro.umontreal.ca/~lisa/publications2/index.php/publications/show/247
[@tag:Elephas]: url:https://github.com/maxpumperla/elephas
[@tag:Elton_molecular_design_review]: doi:10.1039/C9ME00039A
[@tag:Elton2020]: arxiv:2002.05149
[@tag:Errington2014_reproducibility]: doi:10.7554/eLife.04333
[@tag:Eser2016_fiddle]: doi:10.1101/081380
[@tag:Esfahani2016_melanoma]: doi:10.1109/EMBC.2016.7590963
[@tag:Essinger2010_taxonomic]: doi:10.1109/IJCNN.2010.5596644
[@tag:Esteva2017_skin_cancer_nature]: doi:10.1038/nature21056
[@tag:Faruqi]: url:http://alifar76.github.io/sklearn-metrics/
[@tag:Feinberg2018]: doi:10.1056/NEJMra1402513
[@tag:Finnegan2017_maximum]: doi:10.1101/105957
[@tag:Fong2017_perturb]: doi:10.1109/ICCV.2017.371
[@tag:Fraga2005]: doi:10.1073/pnas.0500398102
[@tag:Frosst2017_distilling]: arxiv:1711.09784
[@tag:Fu2019]: doi:10.1109/TCBB.2019.2909237
[@tag:Gal2015_dropout]: arxiv:1506.02142
[@tag:Gargeya2017_dr]: doi:10.1016/j.ophtha.2017.02.008
[@tag:Gaublomme2015_th17]: doi:10.1016/j.cell.2015.11.009
[@tag:Gawad2016_singlecell]: doi:10.1038/nrg.2015.16
[@tag:Geras2017_multiview_mamm]: doi:10.1038/nrg.2015.16
[@tag:Gerstein2016_scaling]: doi:10.1186/s13059-016-0917-0
[@tag:Ghandi2014_enhanced]: doi:10.1371/journal.pcbi.1003711
[@tag:Ghosh1992_sequence]: doi:10.1117/12.140112
[@tag:Glorot2011_domain]: url:http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.231.3442
[@tag:Goldsborough2017_cytogan]: doi:10.1101/227645
[@tag:Gomezb2016_automatic]: arxiv:1610.02415v1
[@tag:Graphlab]: doi:10.14778/2212351.2212354
[@tag:Groop1986_islet]: doi:10.2337/diab.35.2.237
[@tag:Guetterman]: url:https://www.fasebj.org/doi/abs/10.1096/fasebj.30.1_supplement.406.3
[@tag:Gulshan2016_dt]: doi:10.1001/jama.2016.17216
[@tag:Gultepe2014_sepsis]: doi:10.1136/amiajnl-2013-001815
[@tag:Gupta2015_exprs_yeast]: doi:10.1101/031906
[@tag:Gupta2015_prec]: arxiv:1502.02551
[@tag:Hadjas2015_cc]: arxiv:1504.04343
[@tag:He2015_images]: arxiv:1512.03385
[@tag:Hinton2006_autoencoders]: doi:10.1126/science.1127647
[@tag:Hinton2015_dark_knowledge]: arxiv:1503.02531
[@tag:Hinton2015_dk]: arxiv:1503.02531v1
[@tag:Hochreiter]: doi:10.1093/bioinformatics/btm247
[@tag:Hoff]: doi:10.1093/nar/gkp327
[@tag:Horton1992_assessment]: doi:10.1093/nar/20.16.4331
[@tag:Horvath2013]: doi:10.1186/gb-2013-14-10-r115
[@tag:Horvath2014]: doi:10.1073/pnas.1412759111
[@tag:Houseman2012]: doi:10.1186/1471-2105-13-86
[@tag:Houseman2016]: doi:10.1186/s12859-016-1140-4
[@tag:Hubara2016_qnn]: arxiv:1609.07061
[@tag:Huddar2016_predicting]: doi:10.1109/ACCESS.2016.2618775
[@tag:Hughes2016_macromol_react]: doi:10.1021/acscentsci.6b00162
[@tag:Iglovikov2017_baa]: doi:10.1101/234120
[@tag:Islam2018]: doi:10.1186/s12919-018-0121-1
[@tag:Ithapu2015_efficient]: doi:10.1016/j.jalz.2015.01.010
[@tag:Jafari2016_skin_lesions]: doi:10.1007/s11548-017-1567-8
[@tag:Jha2017_integrative_models]: doi:10.1101/104869
[@tag:Johnson2017_integ_cell]: arxiv:1705.00092
[@tag:JuanMateu2016_t1d]: doi:10.1530/EJE-15-0916
[@tag:Kahng2017_activis]: arxiv:1704.01942
[@tag:Kalinin2018_pgx]: arxiv:1801.08570
[@tag:Karlin]: doi:10.1128/jb.179.12.3899-3913.1997
[@tag:Karpathy2015_visualizing]: arxiv:1506.02078
[@tag:Katzman2016_deepsurv]: arxiv:1606.00931
[@tag:Kearnes2016_admet]: arxiv:1606.08793
[@tag:Kearnes2016_graph_conv]: doi:10.1007/s10822-016-9938-8
[@tag:Kelley2016_basset]: doi:10.1101/gr.200535.115
[@tag:Keras]: url:https://github.com/fchollet/keras
[@tag:Khwaja2017]: doi:10.1109/BIOCAS.2017.8325078
[@tag:Khwaja2018]: arxiv:1810.01243
[@tag:Kindermans2016_investigating]: arxiv:1611.07270
[@tag:Kizek]: doi:10.1016/j.bjid.2015.08.013
[@tag:Knights]: doi:10.1111/j.1574-6976.2010.00251.x
[@tag:Koh2016_denoising]: doi:10.1101/052118
[@tag:Koh2017_understanding]: arxiv:1703.04730
[@tag:Kooi2016_mamm_lesions]: doi:10.1016/j.media.2016.07.007
[@tag:Kooi2017_mamm_tl]: doi:10.1002/mp.12110
[@tag:Korfiatis2017]: doi:10.1007/s10278-017-0009-z
[@tag:Kraus2017_deeploc]: doi:10.15252/msb.20177551
[@tag:Kresovich2019]: doi:10.1093/jnci/djz020
[@tag:Krizhevsky2013_nips_cnn]: url:https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
[@tag:Krizhevsky2014_weird_trick]: arxiv:1404.5997
[@tag:Kwabi-Addo2007]: doi:10.1158/1078-0432.CCR-07-0085
[@tag:Lacey2016_dl_fpga]: arxiv:1602.04283
[@tag:Laird2010]: doi:10.1038/nrg2732
[@tag:Lakhani2017_radiography]: doi:10.1148/radiol.2017162326
[@tag:Lanchantin2016_motif]: arxiv:1608.03644
[@tag:Lee2016_deeptarget]: arxiv:1603.09123v2
[@tag:Lee2016_emr_oct_amd]: doi:10.1101/094276
[@tag:Lei2016_rationalizing]: arxiv:1606.04155
[@tag:Leibig2016_dr]: doi:10.1101/084210
[@tag:Levy-Jurgenson2018]: doi:10.1101/491357
[@tag:Levy2019]: doi:10.1101/692665
[@tag:Li2014_minibatch]: doi:10.1145/2623330.2623612
[@tag:Li2016_variation]: doi:10.1126/science.aad9417
[@tag:Liang2015_exprs_cancer]: doi:10.1109/TCBB.2014.2377729
[@tag:Lin2017_why_dl_works]: arxiv:1608.08225v3
[@tag:Lipton2015_lstm]: arxiv:1510.07641
[@tag:Lipton2016_missing]: arxiv:1606.04130
[@tag:Lisboa2006_review]: doi:10.1016/j.neunet.2005.10.007
[@tag:Litjens2016_histopath_survey]: doi:10.1038/srep26286
[@tag:Litjens2017_medimage_survey]: doi:10.1016/j.media.2017.07.005
[@tag:Liu2013]: doi:10.1038/nbt.2487
[@tag:Liu2016_sc_transcriptome]: doi:10.12688/f1000research.7223.1
[@tag:Liu2016_towards]: arxiv:1604.07043
[@tag:Liu]: doi:10.1371/journal.pone.0053253
[@tag:Lodato2015_neurons]: doi:10.1126/science.aab1785
[@tag:Lowe2012_kaggle]: url:http://blogs.sciencemag.org/pipeline/archives/2012/12/11/did_kaggle_predict_drug_candidate_activities_or_not
[@tag:Lundberg2016_an]: arxiv:1611.07478
[@tag:Lusci2013_rnn]: doi:10.1021/ci400187y
[@tag:Lusci2015_irv]: doi:10.1186/s13321-015-0110-6
[@tag:Ma2015_qsar_merck]: doi:10.1021/ci500747n
[@tag:Maaten2008_tsne]: url:http://www.jmlr.org/papers/v9/vandermaaten08a.html
[@tag:Mahendran2014_understanding]: arxiv:1412.0035
[@tag:Mahendran2016_salient]: doi:10.1007/978-3-319-46466-4_8
[@tag:Mahendran2016_visualizing]: doi:10.1007/s11263-016-0911-8
[@tag:Mahmood]: doi:10.1016/S0140-6736(13)61752-3
[@tag:Mapreduce]: doi:10.1145/1327452.1327492
[@tag:Mayr2016_deep_tox]: doi:10.3389/fenvs.2015.00080
[@tag:McHardy2]: doi:10.7717/peerj.1603
[@tag:McHardy]: doi:10.1038/nmeth976
[@tag:Meissner2008]: doi:10.1038/nature07107
[@tag:Meng2016_mllib]: arxiv:1505.06807
[@tag:Metaphlan]: doi:10.1038/nmeth.2066
[@tag:Min2016_deepenhancer]: doi:10.1109/BIBM.2016.7822593
[@tag:Momeni2018]: doi:10.1101/438341
[@tag:Montavon2018_visualization]: doi:10.1016/j.dsp.2017.10.011
[@tag:Mordvintsev2015_inceptionism]: url:http://googleresearch.blogspot.co.uk/2015/06/inceptionism-going-deeper-into-neural.html
[@tag:Moritz2015_sparknet]: arxiv:1511.06051
[@tag:Mrzelj]: url:https://repozitorij.uni-lj.si/IzpisGradiva.php?id=85515
[@tag:Murdoch2017_automatic]: arxiv:1702.02540
[@tag:Murdoch2019]: doi:10.1073/pnas.1900654116
[@tag:NIH2016_genome_cost]: url:https://www.genome.gov/27565109/the-cost-of-sequencing-a-human-genome/
[@tag:Nazor2012]: doi:10.1016/j.stem.2012.02.013
[@tag:Nemati2016_rl]: doi:10.1109/EMBC.2016.7591355
[@tag:Ngiam2011]: url:https://ai.stanford.edu/~ang/papers/icml11-MultimodalDeepLearning.pdf
[@tag:Nguyen2014_adversarial]: arxiv:1412.1897v4
[@tag:Ni2018]: doi:10.1101/385849
[@tag:Nie2016_3d_survival]: doi:10.1007/978-3-319-46723-8_25
[@tag:Nih_curiosity]: url:https://www.nigms.nih.gov/Education/Documents/curiosity.pdf
[@tag:Olivecrona2017_drug_design]: arxiv:1704.07555
[@tag:Osokin2017_biogan]: arxiv:1708.04692
[@tag:Pan2018]: doi:10.1101/438218
[@tag:Papernot2017_pate]: url:https://openreview.net/forum?id=HkwoSDPgg
[@tag:Park2016_deepmirgene]: arxiv:1605.00017
[@tag:Parnamaa2017]: doi:10.1534/g3.116.033654
[@tag:Pawlowski2016]: doi:10.1101/085118
[@tag:Peng2019]: doi:10.1101/527044
[@tag:Pereira2016_docking]: doi:10.1021/acs.jcim.6b00355
[@tag:PerezSianes2016_screening]: doi:10.1007/978-3-319-40126-3_2
[@tag:Phymm]: doi:10.1038/nmeth.1358
[@tag:Poplin2016_deepvariant]: doi:10.1101/092890
[@tag:Pratt2016_dr]: doi:10.1016/j.procs.2016.07.014
[@tag:Qin2017_onehot]: doi:10.1371/journal.pcbi.1005403
[@tag:Qiu2017_graph_embedding]: doi:10.1101/110668
[@tag:Qiu2018]: doi:10.1101/406066
[@tag:Quach2017]: doi:10.18632/aging.101168
[@tag:Quang2017_factor]: doi:10.1101/151274
[@tag:RAD2010_view_cc]: doi:10.1145/1721654.1721672
[@tag:Radford_dcgan]: arxiv:1511.06434v2
[@tag:Ragoza2016_protein]: arxiv:1612.02751
[@tag:Raina2009_gpu]: doi:10.1145/1553374.1553486
[@tag:Rajkomar2017_radiographs]: doi:10.1007/s10278-016-9914-9
[@tag:Rakhlin2018_histology]: doi:10.1101/259911
[@tag:Ramsundar2015_multitask_drug]: arxiv:1502.02072
[@tag:Ranganath2016_deep]: arxiv:1608.02158
[@tag:Relton2010]: doi:10.1371/journal.pmed.1000356
[@tag:Ribeiro2016_lime]: arxiv:1602.04938
[@tag:Robertson2005]: doi:10.1038/nrg1655
[@tag:Rogers2010_fingerprints]: doi:10.1021/ci100050t
[@tag:Romero2017_diet]: url:https://openreview.net/pdf?id=Sk-oDY9ge
[@tag:Rosenberg2015_synthetic_seqs]: doi:10.1016/j.cell.2015.09.054
[@tag:Roth2015_view_agg_cad]: doi:10.1109/TMI.2015.2482920
[@tag:Rudin2019]: doi:10.1038/s42256-019-0048-x
[@tag:Russakovsky2015_imagenet]: doi:10.1007/s11263-015-0816-y
[@tag:Sa2015_buckwild]: pmcid:PMC4907892
[@tag:Salas2018]: doi:10.1186/s13059-018-1448-7
[@tag:Salas2018_GR]: doi:10.1101/gr.233213.117
[@tag:Salzberg]: doi:10.1186/1471-2105-11-544
[@tag:Schatz2010_dna_cloud]: doi:10.1038/nbt0710-691
[@tag:Schmidhuber2014_dnn_overview]: doi:10.1016/j.neunet.2014.09.003
[@tag:Scotti2016_missplicing]: doi:10.1038/nrg.2015.3
[@tag:Sculley2018]: url:https://openreview.net/pdf?id=rJWF0Fywf
[@tag:Segata]: doi:10.1371/journal.pcbi.1004977
[@tag:Segler2017_drug_design]: arxiv:1701.01329
[@tag:Seide2014_parallel]: doi:10.1109/ICASSP.2014.6853593
[@tag:Selvaraju2016_grad]: arxiv:1610.02391
[@tag:Serden]: doi:10.1016/S0168-8510(02)00208-7
[@tag:Setty2015_seqgl]: doi:10.1371/journal.pcbi.1004271
[@tag:Shaham2016_batch_effects]: doi:10.1093/bioinformatics/btx196
[@tag:Shapely]: doi:10.1515/9781400881970-018
[@tag:Shen2017_medimg_review]: doi:10.1146/annurev-bioeng-071516-044442
[@tag:Shen2019]: doi:10.1016/j.eswa.2019.01.048
[@tag:Shin2016_cad_tl]: doi:10.1109/TMI.2016.2528162
[@tag:Shrikumar2017_learning]: arxiv:1704.02685
[@tag:Shrikumar2017_reversecomplement]: doi:10.1101/103663
[@tag:Silver2016_alphago]: doi:10.1038/nature16961
[@tag:Simonyan2013_deep]: arxiv:1312.6034
[@tag:Singh2016_deepchrome]: arxiv:1607.02078
[@tag:Singh2016_tsk]: doi:10.1109/TCBB.2016.2609918
[@tag:Singh2017_attentivechrome]: arxiv:1708.00339
[@tag:Sonderby]: doi:10.1007/978-3-319-21233-3_6
[@tag:Soueidan]: doi:10.1515/metgen-2016-0001
[@tag:Spark]: doi:10.1145/2934664
[@tag:Speech_recognition]: url:http://www.businessinsider.com/ibm-edges-closer-to-human-speech-recognition-2017-3
[@tag:Springenberg2014_striving]: arxiv:1412.6806
[@tag:Stein2010_cloud]: doi:10.1186/gb-2010-11-5-207
[@tag:Stenstrom2005_latent]: doi:10.2337/diabetes.54.suppl_2.S68
[@tag:Stormo2000_dna]: doi:10.1093/bioinformatics/16.1.16
[@tag:Stratnikov]: doi:10.1186/2049-2618-1-11
[@tag:Strobelt2016_visual]: arxiv:1606.07461
[@tag:Su2015_gpu]: arxiv:1507.01239
[@tag:Subramanian2016_bace1]: doi:10.1021/acs.jcim.6b00290
[@tag:Sumita2018]: doi:10.1021/acscentsci.8b00213
[@tag:Sun2016_ensemble]: arxiv:1606.00575
[@tag:Sundararajan2017_axiomatic]: arxiv:1703.01365
[@tag:Sutskever]: arxiv:1409.3215
[@tag:Swamidass2009_irv]: doi:10.1021/ci8004379
[@tag:TAC-ELM]: doi:10.1142/S0219720012500151
[@tag:Tan2014_psb]: doi:10.1142/9789814644730_0014
[@tag:Tan2015_adage]: doi:10.1128/mSystems.00025-15
[@tag:Tan2016_eadage]: doi:10.1101/078659
[@tag:TensorFlow]: arxiv:1603.04467
[@tag:Teschendorff2017]: doi:10.2217/epi-2016-0153
[@tag:Tian2019]: doi:10.1186/s12864-019-5488-5
[@tag:Titus2017]: doi:10.1093/hmg/ddx275
[@tag:Torracinta2016_deep_snp]: doi:10.1101/097469
[@tag:Torracinta2016_sim]: doi:10.1101/079087
[@tag:Tu1996_anns]: doi:10.1016/S0895-4356(96)00002-9
[@tag:Unterthiner2014_screening]: url:http://www.bioinf.at/publications/2014/NIPS2014a.pdf
[@tag:Vamathevan2019]: doi:10.1038/s41573-019-0024-5
[@tag:Vanhoucke2011_cpu]: url:https://research.google.com/pubs/pub37631.html
[@tag:Vera2016_sc_analysis]: doi:10.1146/annurev-genet-120215-034854
[@tag:Vervier]: doi:10.1093/bioinformatics/btv683
[@tag:Wallach2015_atom_net]: arxiv:1510.02855
[@tag:Wang2016_breast_cancer]: arxiv:1606.05718
[@tag:Wang2016_methyl]: doi:10.1038/srep19598
[@tag:Wang2016_protein_contact]: doi:10.1371/journal.pcbi.1005324
[@tag:Wasson1985_clinical]: doi:10.1056/NEJM198509263131306
[@tag:WayGreene2017_eval]: arxiv:1711.04828
[@tag:WayGreene2017_tybalt]: doi:10.1101/174474
[@tag:Wilhelm-Benartzi2013]: doi:10.1038/bjc.2013.496
[@tag:Wu2017_molecule_net]: doi:10.1039/C7SC02664A
[@tag:Xiang]: doi:10.1016/S0167-9473(99)00098-5
[@tag:Xiong2011_bayesian]: doi:10.1093/bioinformatics/btr444
[@tag:Xiong2015_splicing_code]: doi:10.1126/science.1254806
[@tag:Xu2015_show]: arxiv:1502.03044
[@tag:Yasushi2016_cgbvs_dnn]: doi:10.1002/minf.201600045
[@tag:Yoon2016_cancer_reports]: doi:10.1007/978-3-319-47898-2_21
[@tag:Yosinksi2015_understanding]: arxiv:1506.06579
[@tag:Yosinski2014]: url:https://papers.nips.cc/paper/5347-how-transferable-are-features-in-deep-neural-networks
[@tag:Yu2016_melanoma_resnet]: doi:10.1109/TMI.2016.2642839
[@tag:Zeiler2013_visualizing]: arxiv:1311.2901
[@tag:Zeng2015]: doi:10.1186/s12859-015-0553-9
[@tag:Zeng2016_convolutional]: doi:10.1093/bioinformatics/btw255
[@tag:Zhang2015_multitask_tl]: doi:10.1145/2783258.2783304
[@tag:Zhang2017_generalization]: arxiv:1611.03530v2
[@tag:Zhang2019]: doi:10.1186/s12885-019-5932-6
[@tag:Zhavoronkov2019_drugs]: doi:10.1038/s41587-019-0224-x
[@tag:Zhou2015_deep_sea]: doi:10.1038/nmeth.3547
[@tag:Zhu2016_advers_mamm]: doi:10.1101/095786
[@tag:Zhu2016_mult_inst_mamm]: doi:10.1101/095794
[@tag:Zintgraf2017_visualizing]: arxiv:1702.04595
[@tag:ai_safety]: arxiv:1606.06565
[@tag:bayesian_hypernets]: arxiv:1710.04759
[@tag:blast]: doi:10.1016/S0022-2836(05)80360-2
[@tag:carlisle]: url:https://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/
[@tag:domain_adapt_uncertainty]: arxiv:1505.07818
[@tag:gal_thesis]: url:http://www.cs.ox.ac.uk/people/yarin.gal/website/thesis/thesis.pdf
[@tag:ghahramani_protect]: arxiv:1707.02476
[@tag:goodfellow2016deep]: url:http://www.deeplearningbook.org
[@tag:guo_calibration]: arxiv:1706.04599
[@tag:krizhevsky-2009]: url:https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf
[@tag:li2016joint]: url:https://dl.acm.org/citation.cfm?id=3061018
[@tag:lmat]: doi:10.1093/bioinformatics/btt389
[@tag:matis]: doi:10.1016/S0097-8485(96)80015-5
[@tag:mcclure_bayesian]: arxiv:1611.01639
[@tag:nbc]: doi:10.1093/bioinformatics/btq619
[@tag:onecodex]: url:https://www.onecodex.com/
[@tag:out_dist_baseline]: arxiv:1610.02136
[@tag:platt_scaling]: url:http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.41.1639
[@tag:retinopathy_uncertainty]: doi:10.1038/s41598-017-17876-z
[@tag:strong_adversary]: arxiv:1705.07263
[@tag:techblog-perkel]: url:https://blogs.nature.com/naturejobs/2018/02/20/techblog-manubot-powers-a-crowdsourced-deep-learning-review/
[@tag:temp_out_dist]: arxiv:1706.02690
[@tag:timestamps]: url:https://blog.dhimmel.com/irreproducible-timestamps/
[@tag:uncertainty_ensembles]: arxiv:1612.01474
[@tag:uncertainty_multi_task]: arxiv:1705.07115
[@tag:uncertainty_types]: arxiv:1703.04977
[@tag:wgsquikr]: doi:10.1371/journal.pone.0091784
[@tag:word2vec]: arxiv:1301.3781
[@tag:world2004international]: url:http://www.who.int/classifications/icd/en/
[@tag:yok]: doi:10.1186/1471-2105-12-20
