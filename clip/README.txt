#INPUT
clip expects three files
    sample.cna.txt
        chromosome_index	start_position	end_position	major_cn	minor_cn	total_cn
        1	1	4	1	1	2
        1	6	9	1	1	2
        1	11	14	1	1	2
        1	16	19	1	1	2
    sample.snv.txt
        chromosome_index	position	alt_count	ref_count
        1	2	124	373
        1	7	135	369
        1	12	144	381
        1	17	114	369
    sample.purity.txt
        0.9

the sample.purity.txt seems to be an initial estimate only of the percentage of non normal tissue. 

alt_count should be the number of reads observed with variant alleles and ref_count is the number of reads covering the snv

# OUTPUT
In final results, cluster index = 0 indicates clonal mutations, while non-zero cluster indexes indicate subclonal mutations.

The final result for CliP is two-fold:

The subclonal structure, i.e., clustering results: cluster number, the total number of SNVs in each cluster, and the estimated CP for each cluster.
The mutation assignment, i.e., cluster id for each mutation. This output can then serve as the basis for inference of phylogenetic trees.

# MODEL
"Bayesian methods require a large amount of computational resources, a prior knowledge of the number of subclones, and extensive post-processing. Regularized likelihood modeling approach, never explored for subclonal reconstruction, can inherently address these drawbacks. We therefore propose a model-based method, Clonal structure identification through pair-wise Penalization, or CliP, for clustering subclonal mutations without prior knowledge or post-processing. The CliP model is applicable to genomic regions with or without CNAs."

Model
"""In our model, we use $N$ to denote the total number of SNVs in each sample. For each SNV $i$, we use $\left(r_i, n_i\right)$ to denote the number of reads observed with variant alleles and the total number of reads covering the SNV. We suppose that each sample consists of two populations of cells with respect to the $i$-th SNV: one population contains normal cells or cancer cells that do not present this SNV, and the other population represents cancer cells harboring this SNV. We adopt the infinite site assumption (Kimura 1969): (1) there are an infinite number of sites where mutations can occur, (2) every new mutation occurs at a novel site, and (3) there is no recombination. Under this assumption, there is only one alternative variant at each SNV for each sample, which can vary across different samples. Within cancer cells, SNV $i$ may only occur in one or a few cell populations (Fig 1), therefore we introduce $\beta_i$ to denote the cancer cell fraction (CCF) of SNV $i$. With $N$ SNVs, we assume there are $K$ groups of SNVs presenting distinct CCF and $K<<$.

We take advantage of the observed distribution of VAFs across mutations in heterogeneous tumor samples to build our model. We use $b_i^V$ to denote the SNV-specific copy number at the $i$-th SNV. This measurement is distinct from allele-specific copy number when the SNV does not occur in all tumor cells. We then use $c_i^N$ and $c_i^V$ to denote the total copy number for normal and tumor cell respectively, and $\rho \in[0,1]$ to be the tumor cell proportion, i.e., purity in the sample. We define $\phi_i=\rho \beta_i$ as the cellular prevalence (CP) of SNV $i$. The SNVs from a common subclone have identical CP (or CCF) and parameter $\phi_i$ (or equivalently $\beta_i$ ) is of our primary interest.

With the observed data $\left(r_i, n_i\right)$ at each SNV $i$, our model assumes $r_i$ to follow a binomial distribution $\operatorname{Binom}\left(n_i, \theta_i\right)$. The expected proportion of the variant allele at the $i$-th SNV $\theta_i$ is further expressed as:
$$
\theta_i=f\left(\phi_i\right)=\frac{\phi_i b_i^V}{(1-\rho) c_i^N+\rho c_i^V}, \quad i=1, \cdots, N
$$

$$
\ell(\phi)=\sum_{i=1}^N\left[r_i \log f\left(\phi_i\right)+\left(n_i-r_i\right) \log \left(1-f\left(\phi_i\right)\right)\right]
$$
The CP, $\phi=\left(\phi_1, \cdots, \phi_N\right)$ may be estimated by maximizing the corresponding likelihood. However, our primary goal is to identify a homogeneous and sparse structure, i.e., clusters, of the CPs across all SNVs. The penalized estimation is a canonical tool to achieve the homogeneity detection and parameter estimation simultaneously (Hastie et al. 2015). Therefore, we introduce a pair-wise penalty to seek such homogeneity in $\phi$. In order to facilitate the computation, we employ a normal approximation of the binomial random variable, i.e., $\sqrt{n_i}\left(r_i / n_i-\theta_i\right) \sim N\left(0, \theta_i\left(1-\theta_i\right)\right)$. This yields a standard form of penalized objective function with quadratic loss $\tilde{Q}(\phi ; \lambda)$, and the estimator can be obtained by minimizing it over $\phi$, given a tuning parameter $\lambda>0$ that controls the degree of the penalization:
$$
\tilde{Q}(\phi ; \lambda)=\frac{1}{2} \sum_{i=1}^N \frac{n_i\left(f\left(\phi_i\right)-\hat{\theta}_i\right)^2}{f\left(\phi_i\right)\left(1-f\left(\phi_i\right)\right)}+\sum_{1 \leq i<j \leq N} p_\lambda\left(\left|\phi_i-\phi_j\right|\right),
$$
where $\hat{\theta}_i$ is the estimated proportion of variant allele at the $i$-th SNV, and $p_\lambda(\cdot)$ denotes a sparsity pursuing penalty to identify the homogeneity structure in $\phi$, such as LASSO (Tibshirani 1996), SCAD (Fan and Li 2001), and MCP (Zhang et al. 2010) to name a few. Here, we focus on the SCAD penalty that is known to not only enjoy the oracle property but also show improved performance in the model estimation (Fan and Li 2001). Adaptation to other penalty forms will be straightforward.

Input data.
CliP requires information of $c_i^N, c_i^V, r_i, n_i$, and optionally, $\rho$, as its input. Parameters $\rho$ and $c_i^V$ can be obtained using CNA-based deconvolution methods such as ASCAT (Van Loo et al. 2010) and ABSOLUTE (Carter et al. 2012), whereas $c_i^N$ is typically set as 2. In contrast, parameter $b_i^V$ is not directly observed or estimatable using existing CNA software tools. Following a current convention that proved to be effective(Dentro et al. 2017), we assume $b_i^V$ as:
$$
b_i^V=\left[\frac{r_i}{n_i} \frac{1}{\rho}\left(\rho c_i^V+c_i^N(1-\rho)\right)\right]_0, \quad i=1, \cdots, N
$$
where $[\cdot]_0$ rounds $x$ to the nearest positive integer.

Similar to other available methods, CliP currently takes into consideration only the status of
clonal copy number aberrations. CNAs can occur in subclones (Nik-Zainal et al. 2012; JamalHanjani et al. 2014). In rare cases, there may be a subclone where both SNV and subclonal
CNAs happen at the same time. CliP will not be able to account for allele-specific copy number
correctly for this SNV. However, subclonal CNA calling remains challenging."""