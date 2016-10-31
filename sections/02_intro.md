## Introduction

### Potential writing prompt

One potential future that we could imagine is a world in which data, once
gathered, is rapidly integrated into our understanding of living systems. What
we learn is rapidly put to use. Our health-related activities are constantly
monitored (e.g. by wearables) and all of our interactions with health care
systems are extensively tracked. These sources of information are combined to
help to guide our health care and maintenance. We'd be able to compare our state
and trajectory to (anonymized) others, and identify means to improve our health.
These means might contain drug combinations selected based on personalized
predictions.

### If this happens, is deep learning required for any of it? Are we any closer
### because of the advent of deep learning?

*"Categorize" and "treat" sound a bit like PMI goals. Another way to think about
this would be: do we think that deep learning will make much of a difference
for the precision medicine initiative (PMI)?*

### General deep learning introduction

*Definitions, specific architectures, etc.  We may want to clarify what we mean
by "deep" learning when most methods use few hidden layers.*



### Types of biological problems
>Section goal: This section could contain the types of biological problems people have already applied deep learning to, based on the existing literature.  This could be mentioned in two ways:

>1. The type of input data: DNA sequence, protein sequence, clinical data, imaging data, etc.

>2. The output/objective of the model: protein structure/function, protein localization, miRNA/TF target prediction, patient diagnosis/prognosis, drug discovery/prediction, or unsupervised clustering, etc.

In this review, we are interested in the application of deep learning to topics of biomedical importance. This covers a large range of biomedical topics, which we divide into three broad classes based on their applied areas. We then briefly introduce the types of questions, approaches and data which are typical for each class in the application of deep learning.

**Disease and Patient Categorization**

One important topic in the biomedical field is the accurate classify diseases and disease subtypes. In the oncology field, current "gold standard" approaches are limited to either histological approaches, requiring manual human expertise, or shallow molecular markers, such as the cell surface receptors or small panels of genes. One example is the current PAM50 approach in classifying breast cancer, which utilizes the expression of 50 marker genes in order to divide breast cancer patients into six subtypes. Significant heterogeneity still remains within these six subtypes (Mayer et al. 2014). Given the increasing wealth of molecular data available, it seems that a more comprehensive subtyping is possible.

Several studies have used deep learning methods in order to better categorize breast cancer patients. For example, Tan et al. applied denoising autoencoders (DA), an unsupervised approach, in order to cluster breast cancer patients (Tan et al. 2014). Ciresan et al. utilized convolutional neural networks (CNN) to count mitotic divisions in histological images; a feature which is highly correlated with disease outcome (Ciresan et al. 2013). Despite these recent advances, a number of challenges exist in this area of research, such as the integration of disparate types of data, including electronic health records (EHR), imaging and histology data and molecular omics data.

**Fundamental Biological Study**

Broadly speaking, topics in this class aim to answer more fundamental biological questions. Deep learning is especially suited in leveraging the large amounts of data from high throughput omics studies. The development of deep learning techniques and complex network architectures allow researchers to answer fundamental biological questions with unprecedented accuracy. One classic biological problem where machine learning has been extensively applied is the prediction of molecular targets. Recent advances using deep learning have shown higher accuracy in determining molecular targets. For example, Lee et al. used deep recurrent neural networks (RNN) to predict gene targets of micro-RNAs (Lee et al. 2016). Wang et al. used a residual CNN to predict protein-protein contact on a genome-wide scale (Wang et al. 2016). Other biological questions that have been investigated include the prediction of protein secondary structure based on sequence data (Spencer et al. 2015, Lin et al. 2016), recognition of functional genomic elements such as enhancers and promoters (Liu et al. 2016, Li et al. 2015, Kleftogiannis et al. 2014), or predicting the deleterious effects of nucleotide polymorphisms (Quang et al. 2014), etc.

**Treatment Selection and Prediction**

Studies in this category aim to recommend patient treatment or predict treatment outcome. Specifically, a lot of effort in this area aims to identify drug targets, identify drug interactions or predict drug response. One recent approach for predicting drug response is the use of protein structure to predict drug interactions and drug bioactivity through CNN (Wallach et al. 2015). Since CNNs leverage spatial relationships within the data, this particular deep learning framework is well suited to the problem. Drug discovery and drug "repurposing" is another hot topic. Aliper et al. used transcriptomic data to predict which drugs might be repurposed for other diseases through deep fully connected neural networks. In a similar vein, Wang et al. used restricted boltzman machines (RBM) to predict drug molecular targets (Wang et al. 2013).



Refs: 

* Mayer IA, Abramson VG, Lehmann BD, Pietenpol JA. New strategies for triple-negative breast cancer—deciphering the heterogeneity. Clinical cancer research. 2014 Feb 15;20(4):782-90. [@doi:10.1158/1078-0432.CCR-13-0583]
* Tan J, Ung M, Cheng C, Greene CS. Unsupervised feature construction and knowledge extraction from genome-wide assays of breast cancer with denoising autoencoders. In Pacific Symposium on Biocomputing. 2014 Dec. (pp. 132-143). [@doi:10.1142/9789814644730_0014]
* Ciresan DC, Giusti A, Gambardella LM, Schmidhuber J. Mitosis detection in breast cancer histology images with deep neural networks. In International Conference on Medical Image Computing and Computer-assisted Intervention. 2013 Sep 22. (pp. 411-418). Springer Berlin Heidelberg. [@doi:10.1007/978-3-642-40763-5_51]
* Lee B, Baek J, Park S, Yoon S. deepTarget: End-to-end Learning Framework for microRNA Target Prediction using Deep Recurrent Neural Networks. arXiv preprint arXiv:1603.09123. 2016 Mar 30. [@doi:10.1109/icnn.1994.374637]
* Wang S, Sun S, Li Z, Zhang R, Xu J. Accurate De Novo Prediction of Protein Contact Map by Ultra-Deep Learning Model. arXiv preprint arXiv:1609.00680. 2016 Sep 2. [@doi:10.1101/073239]
* Eser U, Churchman LS. FIDDLE: An integrative deep learning framework for functional genomic data inference. bioRxiv. 2016 Jan 1:081380. [@doi:10.1101/081380]
* Spencer M, Eickholt J, Cheng J. A deep learning network approach to ab initio protein secondary structure prediction. IEEE/ACM Transactions on Computational Biology and Bioinformatics (TCBB). 2015 Jan 1;12(1):103-12. [@doi:10.1109/tcbb.2014.2343960]
* Lin Z, Lanchantin J, Qi Y. MUST-CNN: A Multilayer Shift-and-Stitch Deep Convolutional Architecture for Sequence-based Protein Structure Prediction. arXiv preprint arXiv:1605.03004. 2016 May 10. [@doi:10.1038/srep18962]
* Liu F, Li H, Ren C, Bo X, Shu W. PEDLA: predicting enhancers with a deep learning-based algorithmic framework. bioRxiv. 2016 Jan 1:036129. [@doi:10.1101/036129]
* Li Y, Chen CY, Wasserman WW. Deep feature selection: Theory and application to identify enhancers and promoters. In International Conference on Research in Computational Molecular Biology. 2015 Apr 12. (pp. 205-217). Springer International Publishing. [@doi:10.1007/978-3-319-16706-0_20]
* Kleftogiannis D, Kalnis P, Bajic VB. DEEP: a general computational framework for predicting enhancers. Nucleic acids research. 2014 Nov 5:gku1058. [@doi:10.1093/nar/gku1058]
* Quang D, Chen Y, Xie X. DANN: a deep learning approach for annotating the pathogenicity of genetic variants. Bioinformatics. 2014 Oct 22:btu703. [@doi:10.1093/bioinformatics/btu703]
* Vougas KN, Jackson T, Polyzos A, Liontos M, Johnson EO, Georgoulias V, Townsend P, Bartek J, Gorgoulis VG. Deep Learning and Association Rule Mining for Predicting Drug Response in Cancer. bioRxiv. 2016 Jan 1:070490. [@doi:10.1101/070490]
* Wallach I, Dzamba M, Heifets A. AtomNet: A Deep Convolutional Neural Network for Bioactivity Prediction in Structure-based Drug Discovery. arXiv preprint arXiv:1510.02855. 2015 Oct 10.
* Aliper A, Plis S, Artemov A, Ulloa A, Mamoshina P, Zhavoronkov A. Deep learning applications for predicting pharmacological properties of drugs and drug repurposing using transcriptomic data. Molecular pharmaceutics. 2016 May 20. [@doi:10.1021/acs.molpharmaceut.6b00248]
* Wang Y, Zeng J. Predicting drug-target interactions using restricted Boltzmann machines. Bioinformatics. 2013 Jul 1;29(13):i126-34. [@doi:10.1093/bioinformatics/btt234]

