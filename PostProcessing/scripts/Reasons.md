# Reason for what i do
### KDE

#### Crossvalidation 
[Nice ref.](https://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/) 

>There are two classes of approaches to this problem: in the statistics community, it is common to use reference rules, where the optimal bandwidth is estimated from theoretical forms based on assumptions about the data distribution. A common reference rule is Silverman's rule, which is derived for univariate KDE and included within both the Scipy and Statsmodels implementations. Other potential reference rules are ones based on Information Criteria, such as the well-known AIC and BIC.

>In the Machine Learning world, the use of reference rules is less common. Instead, an empirical approach such as cross validation is often used. In cross validation, the model is fit to part of the data, and then a quantitative metric is computed to determine how well this model fits the remaining data. Such an empirical approach to model parameter selection is very flexible, and can be used regardless of the underlying data distribution.
>Because the various reference rules generally depend on (often dubious) assumptions about the underlying distribution of the data, bandwidth selection based in cross-validation can produce more trustworthy results for real-world datasets.

