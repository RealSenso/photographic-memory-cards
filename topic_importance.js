/**
 * Topic Importance Mapping based on IISc PYQ Analysis (Midterms & Endsems)
 * Categories:
 *   - 'red': Extremely Important (High PYQ frequency & point weight, core exam pillars)
 *   - 'orange': Medium Importance (Frequently tested concepts, intermediate proofs & calculations)
 *   - 'yellow': Lowest Importance (Foundational definitions, specialized niche topics, low direct exam weight)
 */

window.TOPIC_IMPORTANCE = {
  // ==========================================
  // CMO (Constrained & Unconstrained Optimization) - 19 Topics
  // ==========================================
  "CMO": {
    "01_Mathematical_Preliminaries_Topology_and_Weierstrass": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Foundational definitions (Weierstrass theorem, open/closed sets); rarely direct standalone questions."
    },
    "02_Multivariate_Taylor_Series_and_Optimality_Conditions": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "First- and second-order necessary/sufficient conditions (FONC/SONC), stationary points."
    },
    "03_Convexity_and_Strong_Convexity": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Appeared in 7/8 years! Coercivity implies global min existence, strong convexity, unique minima."
    },
    "04_Line_Search_Methods_Exact_Armijo_and_Wolfe": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Armijo sufficient decrease condition, curvature condition, backtracking step selection."
    },
    "05_Gradient_Descent_and_Convergence_Analysis": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Tested in 6/8 years! Contraction rate ρ = ((M-m)/(M+m))², exact line search, descent lemma."
    },
    "06_Newtons_Method_and_Hessian_Modifications": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Pure Newton quadratic convergence rate, Levenberg-Marquardt diagonal shift H + τI."
    },
    "07_Conjugate_Direction_and_Conjugate_Gradient_Methods": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Q-conjugacy, expanding subspace theorem, finite n-step termination, Krylov subspaces."
    },
    "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Secant equation B_{k+1}s_k = y_k, rank-1 (SR1) vs rank-2 (BFGS), hereditary positive definiteness."
    },
    "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Tangent cone T(x*), linearized cone V(x*), LICQ and MFCQ constraint qualifications."
    },
    "10_Separating_Hyperplanes_and_Farkas_Lemma": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Hahn-Banach separating hyperplane, Farkas' lemma theorems of alternatives (Ax ≤ 0, c^T x > 0)."
    },
    "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Core centerpiece of constrained optimization! KKT conditions, complementary slackness, sufficiency."
    },
    "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "SONC and SOSC on critical cone d^T ∇²L d > 0; guaranteed 10-15 mark exam question."
    },
    "13_Projections_onto_Convex_Sets": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Projection variational inequality ⟨x - Π_C(x), y - Π_C(x)⟩ ≤ 0; primarily an algorithmic sub-step."
    },
    "14_Gradient_Projection_Algorithm_and_Convergence": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Projected gradient iterations x_{k+1} = Π_C(x_k - α∇f), non-expansiveness property."
    },
    "15_Active_Set_Methods_for_Quadratic_Programming": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Working set tracking, equality-constrained QP subproblem, Lagrange multiplier sign tests."
    },
    "16_Lagrangian_Duality_and_Slaters_Condition": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Dual function g(λ, μ), weak/strong duality, Slater's condition qualification, zero duality gap."
    },
    "17_Wolfe_Duality": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Wolfe dual for convex programs with gradient constraints; rarely asked directly."
    },
    "18_Linear_Programming_Duality_and_Polyhedral_Geometry": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Primal-dual LP formulation, LP complementary slackness, extreme points; major endsem question."
    },
    "19_Penalty_and_Barrier_Methods": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Quadratic penalty method, logarithmic barrier -μ Σ log(-g_i), Hessian ill-conditioning."
    }
  },

  // ==========================================
  // DIP (Digital Image Processing) - 20 Topics
  // ==========================================
  "DIP": {
    "01_Image_Formation_Camera_Geometry_and_Transformations": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Pinhole camera projection matrix P = K[R|t], homogeneous coordinates, affine transformations."
    },
    "02_Color_Theory_and_Color_Spaces": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "RGB, CMY, HSI/HSV color transformations, CIE chromaticity; descriptive/short questions."
    },
    "03_Histograms_Point_Operations_and_Thresholding_Otsu": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Otsu's optimal thresholding maximizing inter-class variance σ_B²(t), gamma correction."
    },
    "04_Binary_Morphology_and_Connected_Components": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Dilation, erosion, opening, closing, hit-or-miss transform, boundary extraction."
    },
    "05_Histogram_Equalization_and_Specification": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Discrete CDF equalization s_k = T(r_k), exact histogram specification; universal Midterm 1 staple."
    },
    "06_LSI_Systems_2D_Convolution_and_Spatial_Filtering": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "2D discrete convolution, separable filter decomposition h = c r^T, Laplacian sharpening."
    },
    "07_2D_Fourier_Transforms_CSFT_DSFT_and_DFT": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "17% of Midterm 2 marks! 2D DFT basis orthogonality, circular vs linear convolution, Parseval theorem."
    },
    "08_Sampling_Theorem_Aliasing_and_Multi_Rate_Conversion": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "2D Whittaker-Shannon sampling theorem, spectral replication on 2D frequency grid, aliasing."
    },
    "09_Discrete_Cosine_Transform_DCT_and_KLT": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "16% of exam marks! DCT energy compaction, KLT/PCA covariance diagonalization & optimal truncation."
    },
    "10_Wavelets_and_Multiresolution_Analysis": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Haar scaling/wavelet functions, 2D Mallat octave subband decomposition (LL, LH, HL, HH)."
    },
    "11_Image_Restoration_Inverse_and_Wiener_Filtering": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "20% of exam marks (#1 highest in DIP)! Inverse filter noise explosion, Wiener MMSE filter derivation, CLS."
    },
    "12_Non_Linear_Restoration_Median_and_Bilateral_Filters": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Median filter order-statistic impulse noise rejection, Bilateral edge-preserving range filter."
    },
    "13_Image_Quality_Assessment_MSE_PSNR_and_SSIM": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "PSNR formula, SSIM structural correlation components; 3% point share in exams."
    },
    "14_Edge_Detection_Gradients_LoG_and_Canny": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "18% of exam marks! Sobel/Prewitt kernels, Laplacian of Gaussian zero-crossings, Canny 4-step pipeline."
    },
    "15_Hough_Transform_for_Lines_and_Circles": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Normal parameterization ρ = x cos θ + y sin θ, parameter accumulator voting, circle detection."
    },
    "16_Corner_Detection_and_Harris_Detector": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Second moment matrix M, eigenvalue ellipse geometry, Harris response R = det(M) - k tr(M)²."
    },
    "17_Scale_Invariant_Feature_Transform_SIFT": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Scale-space DoG pyramid extrema, subpixel refinement, 128-D orientation histogram descriptor."
    },
    "18_Bag_of_Visual_Words_Model": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "k-means visual dictionary clustering, tf-idf weighting, spatial pyramid matching."
    },
    "19_Face_Recognition_Eigenfaces_and_Viola_Jones": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Turk-Pentland Eigenfaces (A^T A trick for high-D images), Viola-Jones integral image & AdaBoost."
    },
    "20_Deep_Learning_and_CNN_Architectures_for_Images": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Receptive field calculation, parameter sharing, transposed convolution, ResNet skip connections."
    }
  },

  // ==========================================
  // LAA (Linear Algebra & Applications) - 18 Topics
  // ==========================================
  "LAA": {
    "01_Vector_Spaces_Subspaces_and_Direct_Sums": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Vector space axioms over F, subspace test, direct sum conditions U ⊕ W (U ∩ W = {0})."
    },
    "02_Linear_Independence_Bases_and_Dimension": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Highest yield in abstract course! Dimension formula dim(U+W) = dim U + dim W - dim(U ∩ W), affine spaces."
    },
    "03_Linear_Maps_Null_Space_Range_and_Matrices": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Fundamental Theorem of Linear Maps (Rank-Nullity dim V = dim null(T) + dim range(T)), matrix representations."
    },
    "04_Invertibility_Isomorphisms_and_Change_of_Basis": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Isomorphism theorem dim V = dim W, change of basis similarity A' = P⁻¹AP, dual space V* basis."
    },
    "05_Polynomials_and_Minimal_Polynomial": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Cayley-Hamilton theorem p_T(T) = 0, minimal polynomial m_T(λ) dividing characteristic polynomial."
    },
    "06_Eigenvalues_Eigenvectors_and_Diagonalization": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Algebraic vs geometric multiplicity, distinct eigenvalues imply linear independence, diagonalizability."
    },
    "07_Commuting_Operators_and_Simultaneous_Diagonalization": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "ST = TS implies shared eigenspaces, simultaneous diagonalization of commuting operators."
    },
    "08_Generalized_Eigenspaces_and_Nilpotent_Operators": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Generalized eigenspaces K_λ = null(T - λI)^{dim V}, nilpotency index, stability lemmas."
    },
    "09_Jordan_Canonical_Form_and_Matrix_Functions": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Jordan block structure J_k(λ), Jordan chain basis, matrix exponential e^{At} for Jordan blocks."
    },
    "10_Inner_Product_Spaces_Norms_and_Orthogonality": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Inner product axioms, Cauchy-Schwarz inequality, parallelogram law, orthogonal complements V = U ⊕ U^⊥."
    },
    "11_Gram_Schmidt_Orthogonal_Projections_and_QR": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Gram-Schmidt process, orthogonal projection operator P_U (P² = P = P*), distance minimization, QR decomposition."
    },
    "12_Adjoints_Self_Adjoint_and_Normal_Operators": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Adjoint operator definition ⟨Tv, w⟩ = ⟨v, T*w⟩, self-adjoint T* = T, normal T*T = TT*, Schur form."
    },
    "13_The_Spectral_Theorem_Real_and_Complex": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Pinnacle theorem of LAA! Real Spectral Theorem (self-adjoint ⟺ orthonormal eigenbasis, real eigenvalues)."
    },
    "14_Positive_Operators_and_Isometries": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Positive operators T ≥ 0 ⟺ ⟨Tv, v⟩ ≥ 0, unique positive square root √T, isometries ‖Tv‖ = ‖v‖."
    },
    "15_Polar_Decomposition_and_Singular_Value_Decomposition": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Polar decomposition T = S√{T*T}, SVD A = UΣV*, Eckart-Young-Mirsky low-rank approximation theorem."
    },
    "16_Pseudoinverse_and_Least_Squares": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Moore-Penrose pseudoinverse A⁺, 4 Penrose conditions, least squares minimum-norm solution x_LS = A⁺b."
    },
    "17_Trace_Determinants_and_Volume": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Trace cyclicity tr(AB) = tr(BA), alternating multilinear determinant, det(e^A) = e^{tr(A)}, volume factor."
    },
    "18_Markov_Chains_and_Consensus_Algorithms": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Perron-Frobenius theorem for non-negative matrices, row-stochastic matrices, graph Laplacian L = D - A."
    }
  },

  // ==========================================
  // StoMA (Stochastic Models & Applications) - 27 Topics
  // ==========================================
  "StoMA": {
    "01_Probability_Spaces_Axioms_and_Continuity_of_Probability": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Kolmogorov axioms, σ-algebra definition, continuity of measure, Boole & Bonferroni inequalities."
    },
    "02_Conditional_Probability_Bayes_Rule_and_Independence": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Law of total probability, Bayes' rule inversion, conditional vs marginal independence."
    },
    "03_Discrete_and_Continuous_Random_Variables": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "CDF 4 fundamental axioms, discrete PMF vs continuous PDF, exponential memorylessness, Gaussian scale."
    },
    "04_Transformations_and_Functions_of_a_Random_Variable": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Sastry's #1 favorite exam trap! Monotone 1D Jacobian vs non-monotone CDF method (Y=X², Y=|X|)."
    },
    "05_Expectation_Variance_Moments_and_Generating_Functions": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Universal linearity, LOTUS, tail sum formula E[X] = ∫ P(X > t) dt, MGF uniqueness & product rule."
    },
    "06_Probability_Inequalities_Markov_Chebyshev_Chernoff": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Markov inequality, Chebyshev dispersion bound, Chernoff bound & exponential tilt, Jensen inequality."
    },
    "07_Joint_Distributions_Marginal_and_Conditional_Distributions": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "100% exam appearance! 2D joint integration over non-rectangular domains, marginals, conditional densities."
    },
    "08_Multiple_Random_Variables_and_Order_Statistics": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Extreme order statistics (min/max), k-th order statistic density, independent exponential spacings."
    },
    "09_Sums_of_Random_Variables_and_Jacobian_Transformations": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Continuous convolution integral, 2D bivariate Jacobian transformation |J|, Box-Muller Gaussian simulation."
    },
    "10_Exchangeable_Random_Variables": {
      tier: "yellow",
      label: "Foundational",
      pyqWeight: "Low",
      reason: "Finite exchangeability correlation bound ρ ≥ -1/(n-1), De Finetti's infinite representation theorem."
    },
    "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Covariance matrix PSD Σ ⪰ 0, orthogonality principle, multivariate LLSE Ŷ = μ_Y + Σ_{YX}Σ_X⁻¹(X - μ_X)."
    },
    "12_Conditional_Expectation_and_MMSE_Estimation": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "MMSE Ŷ = E[Y|X], non-linear orthogonality principle, Tower property, Eve's law of total variance."
    },
    "13_Jointly_Gaussian_Random_Variables": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Multivariate normal density, linear closures, uncorrelated ⟺ independent, affine conditional mean (MMSE = LLSE)."
    },
    "14_Random_Sums_and_Walds_Equation": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Stopping times, Wald's First Identity E[S_N] = E[N]E[X], Wald's Second Identity, Galton-Watson branching."
    },
    "15_Modes_of_Convergence_and_Relations": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Four modes (a.s., P, L^p, d), implication hierarchy, counterexamples (typewriter, escaping spike), Slutsky."
    },
    "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "First Borel-Cantelli Lemma (Σ P(A_n) < ∞), Second Borel-Cantelli Lemma (under independence), 0-1 laws."
    },
    "17_Laws_of_Large_Numbers_WLLN_and_SLLN": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "WLLN via Chebyshev dispersion collapse, SLLN pathwise certainty, Kolmogorov's sharp truncation SLLN."
    },
    "18_Characteristic_Functions_and_Central_Limit_Theorem": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Characteristic function universal existence |φ(t)| ≤ 1, Lévy continuity theorem, Lindeberg-Lévy CLT, Berry-Esseen."
    },
    "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Markov property, transition matrix P, Chapman-Kolmogorov P^{(n+m)} = P^{(n)}P^{(m)}, recurrence criteria."
    },
    "20_DTMC_Stationary_Distributions_and_Limiting_Behavior": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Stationary balance π^T P = π^T, Limiting Distribution Theorem lim P_ij^{(n)} = π_j = 1/μ_jj, Ergodic Theorem."
    },
    "21_Absorption_Probabilities_and_Mean_Hitting_Times": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "First-step analysis a_i = Σ P_ij a_j, mean hitting times μ_i = 1 + Σ P_ij μ_j, Fundamental Matrix N = (I-Q)⁻¹."
    },
    "22_Birth_Death_Chains_and_MCMC": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Birth-death detailed balance π_i p_i = π_{i+1} q_{i+1}, product form distribution, Metropolis-Hastings, Gibbs."
    },
    "23_Random_Processes_Stationarity_and_Ergodicity": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "SSS vs WSS (Gaussian equivalence), ACF properties R_X(0) ≥ |R_X(τ)|, Wiener-Khinchin theorem, LTI filtering."
    },
    "24_Poisson_Processes_Properties_and_Extensions": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Order statistics property (uniform arrivals given count n), thinning into independent streams, Inspection Paradox."
    },
    "25_Random_Walk_Brownian_Motion_and_Gaussian_Processes": {
      tier: "orange",
      label: "Medium",
      pyqWeight: "Medium",
      reason: "Pólya's recurrence theorem (d=1, 2 recurrent, d≥3 transient), Brownian motion axioms, quadratic variation [B]_t = t."
    },
    "26_Martingales_and_Optional_Stopping_Theorem": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Martingale definition E[M_{n+1}|F_n] = M_n, stopping times, Optional Stopping Theorem under 3 conditions, Wald."
    },
    "27_Continuous_Time_Markov_Chains": {
      tier: "red",
      label: "Extremely Imp",
      pyqWeight: "High",
      reason: "Infinitesimal generator Q (Q 1 = 0), Kolmogorov Backward/Forward ODEs, stationary π^T Q = 0^T, birth-death queues."
    }
  }
};

/**
 * Helper to fetch topic importance metadata
 */
window.getTopicImportance = function(subject, topicId) {
  const s = (subject || "").toUpperCase();
  const subKey = s === "STOMA" ? "StoMA" : s;
  const subjMap = window.TOPIC_IMPORTANCE && window.TOPIC_IMPORTANCE[subKey];
  if (!subjMap) return { tier: "orange", label: "Medium", pyqWeight: "Medium", reason: "" };
  return subjMap[topicId] || { tier: "orange", label: "Medium", pyqWeight: "Medium", reason: "" };
};
