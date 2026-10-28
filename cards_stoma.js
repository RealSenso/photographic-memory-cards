/* StoMA knowledge plates (topics 02+). Loaded after cards_data.js and appended to it. */
window.MASTER_CARDS_DATA = (window.MASTER_CARDS_DATA || []).concat(
[
  {
    "id": 30201,
    "subject": "StoMA",
    "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
    "topicTitle": "02 \u00b7 Conditioning, Bayes & Independence",
    "cardNumber": "01",
    "category": "CONDITIONAL PROBABILITY",
    "highlighterClass": "highlight-cyan",
    "title": "Conditional Probability & Reduced Sample Space",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30201\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"16\" width=\"208\" height=\"112\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"28\" y=\"28\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03a9</text><ellipse cx=\"140\" cy=\"72\" rx=\"68\" ry=\"44\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\" transform=\"rotate(0 140 72)\"/><text x=\"180\" y=\"50\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">B</text><ellipse cx=\"80\" cy=\"72\" rx=\"54\" ry=\"40\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" stroke-dasharray=\"3 3\" transform=\"rotate(0 80 72)\"/><text x=\"46\" y=\"54\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A</text><path d=\"M 104,44 A 54,40 0 0,1 126,72 A 54,40 0 0,1 104,100 A 68,44 0 0,1 104,44 Z\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"115\" y=\"73\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A \u2229 B</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(A | B) = Area(A \u2229 B) / Area(B)</text></svg>",
    "drawingCaption": "Conditioning on B discards all outcomes outside B and rescales the remaining probability mass by 1/P(B)",
    "coreTranslation": [
      "<strong>Definition:</strong> For $B \\in \\mathcal{F}$ with $\\mathbb{P}(B) > 0$, the conditional probability of $A$ given $B$ is $\\mathbb{P}(A \\mid B) = \\frac{\\mathbb{P}(A \\cap B)}{\\mathbb{P}(B)}$.",
      "<strong>Bona Fide Measure:</strong> The set function $A \\mapsto \\mathbb{P}(A \\mid B)$ satisfies all Kolmogorov axioms on $(\\Omega, \\mathcal{F})$: $\\mathbb{P}(B \\mid B) = 1$, non-negativity, and countable additivity.",
      "<strong>Scale Normalization:</strong> Conditioning restricts the universe of discourse to $B$, dividing all joint probabilities within $B$ by $\\mathbb{P}(B)$ to preserve their exact relative likelihoods."
    ],
    "math": "$$\\mathbb{P}(A \\mid B) = \\frac{\\mathbb{P}(A \\cap B)}{\\mathbb{P}(B)}, \\quad \\mathbb{P}(B) > 0; \\qquad \\mathbb{P}(\\Omega \\mid B) = \\mathbb{P}(B \\mid B) = 1$$",
    "personalConnection": "Cropping a digital photograph: zooming into frame B discards all external pixels, re-scaling the cropped region to 100% full screen.",
    "examTrap": "Conditioning on events with P(B) = 0 is undefined in Kolmogorov's elementary setting. Continuous conditioning requires conditional expectation on \u03c3-algebras (Borel-Kolmogorov paradox)."
  },
  {
    "id": 30202,
    "subject": "StoMA",
    "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
    "topicTitle": "02 \u00b7 Conditioning, Bayes & Independence",
    "cardNumber": "02",
    "category": "CHAIN RULE",
    "highlighterClass": "highlight-amber",
    "title": "The Multiplication Rule & Probability Chain Rule",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30202\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"24\" width=\"52\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"42.0\" y=\"41.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A\u2081</text><line x1=\"68\" y1=\"38\" x2=\"92\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30202)\"/><text x=\"80\" y=\"32\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(A\u2081)</text><rect x=\"92\" y=\"24\" width=\"62\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"123.0\" y=\"41.0\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A\u2082 | A\u2081</text><line x1=\"154\" y1=\"38\" x2=\"178\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30202)\"/><text x=\"166\" y=\"32\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(A\u2082|A\u2081)</text><rect x=\"178\" y=\"24\" width=\"48\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"202.0\" y=\"41.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">...</text><line x1=\"115\" y1=\"52\" x2=\"115\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30202)\"/><rect x=\"30\" y=\"80\" width=\"180\" height=\"34\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"100.0\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A_n | (A\u2081 \u2229 ... \u2229 A_{n-1})</text><text x=\"120\" y=\"132\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Sequential factorization into 1 marginal and (n - 1) conditionals</text></svg>",
    "drawingCaption": "Any joint intersection decomposes sequentially into one marginal factor and n-1 conditional stages",
    "coreTranslation": [
      "<strong>Two-Event Form:</strong> $\\mathbb{P}(A \\cap B) = \\mathbb{P}(A)\\,\\mathbb{P}(B \\mid A) = \\mathbb{P}(B)\\,\\mathbb{P}(A \\mid B)$.",
      "<strong>General Chain Rule:</strong> For any sequence $A_1, \\dots, A_n$ with $\\mathbb{P}(\\bigcap_{i=1}^{n-1} A_i) > 0$, the joint probability factorizes as $\\mathbb{P}(\\bigcap_{i=1}^n A_i) = \\mathbb{P}(A_1) \\prod_{k=2}^n \\mathbb{P}(A_k \\mid \\bigcap_{j=1}^{k-1} A_j)$.",
      "<strong>Permutation Invariance:</strong> Any permutation of indices yields mathematically identical joint probability, but choosing causal/chronological orders simplifies computation."
    ],
    "math": "$$\\mathbb{P}\\left(\\bigcap_{i=1}^n A_i\\right) = \\mathbb{P}(A_1) \\prod_{k=2}^n \\mathbb{P}\\left(A_k \\;\\middle|\\; \\bigcap_{j=1}^{k-1} A_j\\right)$$",
    "personalConnection": "Drawing four consecutive aces from an un-shuffled deck: (4/52) \u00d7 (3/51) \u00d7 (2/50) \u00d7 (1/49). Each card drawn conditions the state of the remaining deck.",
    "examTrap": "Forgetting to check whether intermediate conditioning histories have strictly positive probability: P(A\u2081 \u2229 ... \u2229 A_{k-1}) > 0 is mandatory at every step."
  },
  {
    "id": 30203,
    "subject": "StoMA",
    "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
    "topicTitle": "02 \u00b7 Conditioning, Bayes & Independence",
    "cardNumber": "03",
    "category": "TOTAL PROBABILITY",
    "highlighterClass": "highlight-emerald",
    "title": "Law of Total Probability: Partition Decomposition",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30203\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"18\" width=\"200\" height=\"100\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"70\" y1=\"18\" x2=\"70\" y2=\"118\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"120\" y1=\"18\" x2=\"120\" y2=\"118\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"170\" y1=\"18\" x2=\"170\" y2=\"118\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"45\" y=\"30\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">B\u2081</text><text x=\"95\" y=\"30\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">B\u2082</text><text x=\"145\" y=\"30\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">B\u2083</text><text x=\"195\" y=\"30\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">B\u2084</text><ellipse cx=\"120\" cy=\"75\" rx=\"75\" ry=\"30\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\" transform=\"rotate(0 120 75)\"/><text x=\"120\" y=\"75\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Event A = \u22c3 (A \u2229 B\u1d62)</text><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(A) = \u2211 P(A | B\u1d62) P(B\u1d62)  (pairwise disjoint union)</text></svg>",
    "drawingCaption": "Partition {B\u1d62} slices event A into disjoint sub-events whose masses sum to the unconditional probability",
    "coreTranslation": [
      "<strong>Partition Criterion:</strong> Collection $\\{B_1, \\dots, B_n\\}$ partitions $\\Omega$ if $B_i \\cap B_j = \\emptyset$ for $i \\ne j$, $\\bigcup_{i=1}^n B_i = \\Omega$, and $\\mathbb{P}(B_i) > 0$.",
      "<strong>Disjoint Splitting:</strong> Any event $A$ decomposes into mutually exclusive pieces $A = \\bigcup_{i=1}^n (A \\cap B_i)$, yielding $\\mathbb{P}(A) = \\sum_{i=1}^n \\mathbb{P}(A \\mid B_i)\\,\\mathbb{P}(B_i)$.",
      "<strong>Strategic Tool:</strong> Allows computing difficult unconditional probabilities by conditioning on hidden or latent regimes where $\\mathbb{P}(A \\mid B_i)$ is elementary."
    ],
    "math": "$$\\mathbb{P}(A) = \\sum_{i=1}^n \\mathbb{P}(A \\mid B_i)\\,\\mathbb{P}(B_i) \\quad \\text{where } \\bigcup_{i=1}^n B_i = \\Omega, \\; B_i \\cap B_j = \\emptyset$$",
    "personalConnection": "Measuring the total timber in a national forest by dividing the map into distinct climatic zones B\u1d62 and multiplying area by local tree density.",
    "examTrap": "Overlooking missing partition coverage: if \u2211 P(B\u1d62) < 1, the partition has an uncounted gap, strictly underestimating P(A)."
  },
  {
    "id": 30204,
    "subject": "StoMA",
    "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
    "topicTitle": "02 \u00b7 Conditioning, Bayes & Independence",
    "cardNumber": "04",
    "category": "BAYESIAN INVERSION",
    "highlighterClass": "highlight-purple",
    "title": "Bayes\u2019 Theorem: Inverting Cause and Effect",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30204\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"80\" height=\"32\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"64.0\" y=\"39.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Prior: P(B_k)</text><line x1=\"104\" y1=\"36\" x2=\"136\" y2=\"36\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30204)\"/><text x=\"120\" y=\"28\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Evidence A</text><rect x=\"136\" y=\"20\" width=\"80\" height=\"32\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"176.0\" y=\"35.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Posterior:</text><text x=\"176.0\" y=\"45.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(B_k | A)</text><rect x=\"24\" y=\"70\" width=\"192\" height=\"46\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"84\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(A | B_k) \u00b7 P(B_k)   [Likelihood \u00d7 Prior]</text><line x1=\"36\" y1=\"92\" x2=\"204\" y2=\"92\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120\" y=\"106\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2211 P(A | B\u1d62) \u00b7 P(B\u1d62)   [Total Evidence P(A)]</text><text x=\"120\" y=\"132\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Posterior \u221d Likelihood \u00d7 Prior</text></svg>",
    "drawingCaption": "Inverts conditional direction from likelihood P(A|B) to posterior belief P(B|A) given observed evidence",
    "coreTranslation": [
      "<strong>Formal Statement:</strong> For partition $\\{B_i\\}$ and event $A$ with $\\mathbb{P}(A) > 0$: $\\mathbb{P}(B_k \\mid A) = \\frac{\\mathbb{P}(A \\mid B_k)\\,\\mathbb{P}(B_k)}{\\sum_{i} \\mathbb{P}(A \\mid B_i)\\,\\mathbb{P}(B_i)}$.",
      "<strong>Prior to Posterior:</strong> Updates initial belief $\\mathbb{P}(B_k)$ (prior) through likelihood $\\mathbb{P}(A \\mid B_k)$ upon observing evidence $A$.",
      "<strong>Denominator as Normalizer:</strong> The denominator is the unconditional evidence mass $\\mathbb{P}(A)$, ensuring $\\sum_k \\mathbb{P}(B_k \\mid A) = 1$."
    ],
    "math": "$$\\mathbb{P}(B_k \\mid A) = \\frac{\\mathbb{P}(A \\mid B_k)\\,\\mathbb{P}(B_k)}{\\sum_{i=1}^n \\mathbb{P}(A \\mid B_i)\\,\\mathbb{P}(B_i)} = \\frac{\\mathbb{P}(A \\mid B_k)\\,\\mathbb{P}(B_k)}{\\mathbb{P}(A)}$$",
    "personalConnection": "A medical diagnostic test: observing symptoms A (evidence) and calculating the updated likelihood of underlying illness B_k (cause).",
    "examTrap": "The Base Rate Fallacy: confusing test reliability P(A|B) with disease certainty P(B|A). If the prior P(B) is 0.1%, a 99% accurate test still yields >95% false alarms!"
  },
  {
    "id": 30205,
    "subject": "StoMA",
    "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
    "topicTitle": "02 \u00b7 Conditioning, Bayes & Independence",
    "cardNumber": "05",
    "category": "INDEPENDENCE",
    "highlighterClass": "highlight-cyan",
    "title": "Independence vs Conditional Independence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30205\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"18\" width=\"98\" height=\"98\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"65\" y=\"32\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Marginal: A \u22a5 B</text><ellipse cx=\"50\" cy=\"72\" rx=\"24\" ry=\"24\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(0 50 72)\"/><ellipse cx=\"80\" cy=\"72\" rx=\"24\" ry=\"24\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(0 80 72)\"/><text x=\"42\" y=\"74\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A</text><text x=\"88\" y=\"74\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">B</text><text x=\"65\" y=\"106\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(A \u2229 B) = P(A)P(B)</text><rect x=\"126\" y=\"18\" width=\"98\" height=\"98\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"175\" y=\"32\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Conditional: A \u22a5 B | C</text><rect x=\"160\" y=\"44\" width=\"30\" height=\"20\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"175.0\" y=\"57.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">C</text><line x1=\"175\" y1=\"64\" x2=\"150\" y2=\"84\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30205)\"/><line x1=\"175\" y1=\"64\" x2=\"200\" y2=\"84\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30205)\"/><rect x=\"136\" y=\"84\" width=\"28\" height=\"20\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"150.0\" y=\"97.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A</text><rect x=\"186\" y=\"84\" width=\"28\" height=\"20\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"200.0\" y=\"97.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">B</text><text x=\"175\" y=\"110\" font-size=\"6.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(A\u2229B|C)=P(A|C)P(B|C)</text><text x=\"120\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Marginal independence does NOT imply conditional independence (and vice-versa)</text></svg>",
    "drawingCaption": "Marginal independence and conditional independence are strictly separate properties with zero automatic implication",
    "coreTranslation": [
      "<strong>Marginal Independence:</strong> $A \\perp B \\iff \\mathbb{P}(A \\cap B) = \\mathbb{P}(A)\\,\\mathbb{P}(B)$, which is equivalent to $\\mathbb{P}(A \\mid B) = \\mathbb{P}(A)$ when $\\mathbb{P}(B) > 0$.",
      "<strong>Conditional Independence:</strong> $A \\perp B \\mid C \\iff \\mathbb{P}(A \\cap B \\mid C) = \\mathbb{P}(A \\mid C)\\,\\mathbb{P}(B \\mid C)$.",
      "<strong>Zero Implication:</strong> Events independent marginally can become dependent given evidence (collider conditioning); events dependent marginally can become independent given their common cause."
    ],
    "math": "$$A \\perp B \\iff \\mathbb{P}(A \\cap B) = \\mathbb{P}(A)\\mathbb{P}(B); \\qquad A \\perp B \\mid C \\iff \\mathbb{P}(A \\cap B \\mid C) = \\mathbb{P}(A \\mid C)\\mathbb{P}(B \\mid C)$$",
    "personalConnection": "Reading skill and shoe size in children: strongly dependent. But conditioning on Age (C), reading level and shoe size become conditionally independent.",
    "examTrap": "Berkson's Paradox: conditioning on common success (e.g. college admissions) creates artificial negative correlation between two independent skills."
  },
  {
    "id": 30206,
    "subject": "StoMA",
    "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
    "topicTitle": "02 \u00b7 Conditioning, Bayes & Independence",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Bernstein\u2019s Pairwise vs Mutual Independence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30206\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"48\" height=\"40\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"40.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Face</text><text x=\"40.0\" y=\"48.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1\n(R, G)</text><rect x=\"70\" y=\"20\" width=\"48\" height=\"40\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"94.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Face</text><text x=\"94.0\" y=\"48.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">2\n(R, B)</text><rect x=\"124\" y=\"20\" width=\"48\" height=\"40\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"148.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Face</text><text x=\"148.0\" y=\"48.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">3\n(G, B)</text><rect x=\"178\" y=\"20\" width=\"48\" height=\"40\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"202.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Face 4\n(R,</text><text x=\"202.0\" y=\"48.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">G, B)</text><rect x=\"16\" y=\"72\" width=\"210\" height=\"48\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"84\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(R) = P(G) = P(B) = 2/4 = 1/2</text><text x=\"120\" y=\"97\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(R \u2229 G) = P(Face 4) + P(Face 1) = 2/4 = 1/4 = P(R)P(G)  [Pairwise OK]</text><text x=\"120\" y=\"110\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(R \u2229 G \u2229 B) = P(Face 4) = 1/4  \u2260  P(R)P(G)P(B) = 1/8  [Mutual FAILS!]</text><text x=\"120\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Bernstein's classic counterexample: 3 pairwise independent events failing mutual independence</text></svg>",
    "drawingCaption": "Pairwise independence checks (n choose 2) pairs; mutual independence requires all 2^n - n - 1 equations",
    "coreTranslation": [
      "<strong>Tetrahedron Setup:</strong> 4 faces with equal probability $1/4$: Face 1 has colors $\\{R, G\\}$, Face 2 $\\{R, B\\}$, Face 3 $\\{G, B\\}$, Face 4 $\\{R, G, B\\}$.",
      "<strong>Pairwise Independence Holds:</strong> $\\mathbb{P}(R) = \\mathbb{P}(G) = \\mathbb{P}(B) = 2/4 = 1/2$. For any pair, $\\mathbb{P}(R \\cap G) = 1/4 = \\mathbb{P}(R)\\,\\mathbb{P}(G)$.",
      "<strong>Mutual Independence Fails:</strong> $\\mathbb{P}(R \\cap G \\cap B) = 1/4$ (Face 4), whereas $\\mathbb{P}(R)\\,\\mathbb{P}(G)\\,\\mathbb{P}(B) = (1/2)^3 = 1/8 \\ne 1/4$."
    ],
    "math": "$$\\mathbb{P}(R \\cap G) = \\frac{1}{4} = \\mathbb{P}(R)\\mathbb{P}(G), \\quad \\text{yet} \\quad \\mathbb{P}(R \\cap G \\cap B) = \\frac{1}{4} \\ne \\mathbb{P}(R)\\mathbb{P}(G)\\mathbb{P}(B) = \\frac{1}{8}$$",
    "personalConnection": "Three secret keys: possessing any two keys tells you nothing about the lock code, but all three together open the lock instantly.",
    "examTrap": "Assuming pairwise independence implies mutual independence! For n events, mutual independence requires verifying all 2^n - n - 1 non-trivial subset intersection equations."
  },
  {
    "id": 30301,
    "subject": "StoMA",
    "topicId": "03_Discrete_and_Continuous_Random_Variables",
    "topicTitle": "03 \u00b7 Discrete & Continuous RVs",
    "cardNumber": "01",
    "category": "FOUNDATIONAL RV & CDF",
    "highlighterClass": "highlight-cyan",
    "title": "The Random Variable & Cumulative Distribution Function (CDF)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30301\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30301)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30301)\"/><path d=\"M 24,114 L 60,114 C 90,114 110,80 130,55 C 150,30 170,26 210,26\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"24\" y1=\"26\" x2=\"215\" y2=\"26\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"3 3\"/><text x=\"16\" y=\"28\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"16\" y=\"115\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><text x=\"130\" y=\"16\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">F_X(x) = P(X \u2264 x)</text><line x1=\"130\" y1=\"55\" x2=\"130\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"130\" cy=\"55\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"130\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Non-decreasing, right-continuous, limits 0 and 1</text></svg>",
    "drawingCaption": "The CDF F_X(x) completely characterizes any random variable's law and is always non-decreasing and right-continuous",
    "coreTranslation": [
      "<strong>Measurable Mapping:</strong> A random variable $X: \\Omega \\to \\mathbb{R}$ is a measurable function satisfying $\\{\\omega : X(\\omega) \\le x\\} \\in \\mathcal{F}$ for all $x \\in \\mathbb{R}$.",
      "<strong>CDF Definition:</strong> $F_X(x) \\triangleq \\mathbb{P}(X \\le x) = \\mathbb{P}(\\{\\omega \\in \\Omega : X(\\omega) \\le x\\})$.",
      "<strong>Four Invariants:</strong> (1) Non-decreasing: $x_1 \\le x_2 \\implies F(x_1) \\le F(x_2)$; (2) Right-continuous: $\\lim_{h \\downarrow 0} F(x+h) = F(x)$; (3) $\\lim_{x \\to -\\infty} F(x) = 0$; (4) $\\lim_{x \\to \\infty} F(x) = 1$."
    ],
    "math": "$$F_X(x) = \\mathbb{P}(X \\le x), \\quad \\lim_{h \\downarrow 0} F_X(x+h) = F_X(x), \\quad F_X(-\\infty) = 0, \\quad F_X(\\infty) = 1$$",
    "personalConnection": "A cumulative water reservoir gauge reading total liters accumulated up to ground elevation x: it cannot drain backwards, and fills to 100%.",
    "examTrap": "Assuming CDFs must be continuous everywhere. Jump discontinuities F(x) - F(x\u207b) = P(X = x) occur at every discrete atom; only RIGHT-continuity is universally guaranteed!"
  },
  {
    "id": 30302,
    "subject": "StoMA",
    "topicId": "03_Discrete_and_Continuous_Random_Variables",
    "topicTitle": "03 \u00b7 Discrete & Continuous RVs",
    "cardNumber": "02",
    "category": "DISCRETE RVs",
    "highlighterClass": "highlight-amber",
    "title": "Discrete Random Variables, PMF & Step CDF",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30302\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30302)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30302)\"/><line x1=\"24\" y1=\"114\" x2=\"60\" y2=\"114\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"60\" y1=\"114\" x2=\"60\" y2=\"85\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"60\" cy=\"85\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"60\" cy=\"114\" r=\"2.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"60\" y1=\"85\" x2=\"110\" y2=\"85\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"110\" y1=\"85\" x2=\"110\" y2=\"48\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"110\" cy=\"48\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"110\" cy=\"85\" r=\"2.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"110\" y1=\"48\" x2=\"170\" y2=\"48\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"170\" y1=\"48\" x2=\"170\" y2=\"26\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"170\" cy=\"26\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"170\" cy=\"48\" r=\"2.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"170\" y1=\"26\" x2=\"215\" y2=\"26\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"60\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2081</text><text x=\"110\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2082</text><text x=\"170\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2083</text><text x=\"76\" y=\"70\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">jump = p(x\u2081)</text><text x=\"126\" y=\"36\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">jump = p(x\u2082)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Staircase CDF: jump height equals PMF probability mass</text></svg>",
    "drawingCaption": "The CDF of a discrete random variable is a pure step staircase whose jump heights equal PMF values p_X(x_k)",
    "coreTranslation": [
      "<strong>Countable Support:</strong> $X$ takes values in countable set $\\{x_1, x_2, \\dots\\}$, characterized by PMF $p_X(x) = \\mathbb{P}(X = x) \\ge 0$ with $\\sum_k p_X(x_k) = 1$.",
      "<strong>Staircase CDF:</strong> $F_X(x) = \\sum_{x_k \\le x} p_X(x_k)$. Jumps occur precisely at atoms: $F_X(x_k) - F_X(x_k^-) = p_X(x_k)$.",
      "<strong>Canonical Roster:</strong> $\\text{Bernoulli}(p)$, $\\text{Binomial}(n, p)$, $\\text{Geometric}(p)$, $\\text{Poisson}(\\lambda)$, $\\text{Negative Binomial}(r, p)$, $\\text{Hypergeometric}$."
    ],
    "math": "$$p_X(x_k) \\ge 0, \\quad \\sum_{k} p_X(x_k) = 1, \\qquad F_X(x_k) - \\lim_{\\epsilon \\downarrow 0} F_X(x_k - \\epsilon) = \\mathbb{P}(X = x_k)$$",
    "personalConnection": "Depositing cash into a vending machine in discrete coin increments: account balance rises in sharp vertical leaps with every coin.",
    "examTrap": "Interval evaluation traps: P(a < X \u2264 b) = F(b) - F(a), whereas P(a \u2264 X \u2264 b) = F(b) - F(a) + P(X = a). With discrete variables, strict vs weak inequalities drastically change the answer!"
  },
  {
    "id": 30303,
    "subject": "StoMA",
    "topicId": "03_Discrete_and_Continuous_Random_Variables",
    "topicTitle": "03 \u00b7 Discrete & Continuous RVs",
    "cardNumber": "03",
    "category": "CONTINUOUS RVs",
    "highlighterClass": "highlight-emerald",
    "title": "Continuous Random Variables & Probability Density Function (PDF)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30303\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30303)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30303)\"/><path d=\"M 24,114 Q 80,114 100,90 Q 120,25 130,25 Q 140,25 160,90 Q 180,114 215,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><path d=\"M 100,90 Q 120,25 130,25 Q 140,25 150,62 L 150,114 L 100,114 Z\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"100\" y1=\"90\" x2=\"100\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><line x1=\"150\" y1=\"62\" x2=\"150\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"100\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a</text><text x=\"150\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">b</text><text x=\"125\" y=\"80\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(a \u2264 X \u2264 b)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Continuous density: Area under curve = probability; single points have probability 0</text></svg>",
    "drawingCaption": "Probabilities correspond to areas under the PDF curve; single real points have exactly zero probability mass",
    "coreTranslation": [
      "<strong>Absolute Continuity:</strong> $X$ is continuous if there exists non-negative integrable $f_X(x)$ such that $F_X(x) = \\int_{-\\infty}^x f_X(t)\\,dt$ for all $x$.",
      "<strong>Calculus Fundamental:</strong> $f_X(x) = \\frac{d}{dx} F_X(x)$ almost everywhere, with $\\int_{-\\infty}^\\infty f_X(x)\\,dx = 1$.",
      "<strong>Point Mass Zero:</strong> $\\mathbb{P}(X = c) = \\int_c^c f_X(t)\\,dt = 0$ for every single $c \\in \\mathbb{R}$. Probabilities are only non-zero over intervals of positive length."
    ],
    "math": "$$F_X(x) = \\int_{-\\infty}^x f_X(t)\\,dt, \\quad f_X(x) = F_X'(x), \\quad \\mathbb{P}(X = c) = 0 \\quad \\forall c \\in \\mathbb{R}$$",
    "personalConnection": "Linear density of a thin steel rod: an infinitesimally thin point slice has 0 grams of mass, but integrating density over any segment yields positive weight.",
    "examTrap": "Believing probability density f_X(x) cannot exceed 1! Densities can be arbitrarily large (e.g. Uniform[0, 0.1] has f(x) = 10). Only PROBABILITIES are bounded by 1."
  },
  {
    "id": 30304,
    "subject": "StoMA",
    "topicId": "03_Discrete_and_Continuous_Random_Variables",
    "topicTitle": "03 \u00b7 Discrete & Continuous RVs",
    "cardNumber": "04",
    "category": "CANONICAL CONTINUOUS",
    "highlighterClass": "highlight-purple",
    "title": "Exponential Distribution & Memoryless Invariance",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30304\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30304)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30304)\"/><path d=\"M 24,30 Q 60,90 120,108 Q 170,113 215,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"16\" y=\"30\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bb</text><line x1=\"70\" y1=\"80\" x2=\"70\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><line x1=\"130\" y1=\"106\" x2=\"130\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"70\" y=\"125\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">t</text><text x=\"130\" y=\"125\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">t + s</text><text x=\"160\" y=\"50\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(X > t + s | X > t) = P(X > s)</text><text x=\"160\" y=\"68\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">e^{-\u03bb(t+s)} / e^{-\u03bbt} = e^{-\u03bbs}</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Exponential is the ONLY continuous distribution with the memoryless property</text></svg>",
    "drawingCaption": "The exponential distribution forgets all past elapsed waiting time, maintaining a constant hazard rate",
    "coreTranslation": [
      "<strong>Density & Survival:</strong> $f_X(t) = \\lambda e^{-\\lambda t} \\mathbf{1}_{\\{t \\ge 0\\}}$ with survival function $\\mathbb{P}(X > t) = e^{-\\lambda t}$. Mean $\\mathbb{E}[X] = 1/\\lambda$, variance $\\operatorname{Var}(X) = 1/\\lambda^2$.",
      "<strong>Memoryless Invariant:</strong> $\\mathbb{P}(X > t + s \\mid X > t) = \\mathbb{P}(X > s)$ for all $s, t \\ge 0$. The item does not age or wear out over time.",
      "<strong>Unique Characterization:</strong> The Exponential distribution is the ONLY continuous distribution on $[0, \\infty)$ possessing memoryless property (Geometric is the only discrete one)."
    ],
    "math": "$$\\mathbb{P}(X > t + s \\mid X > t) = \\frac{e^{-\\lambda(t+s)}}{e^{-\\lambda t}} = e^{-\\lambda s} = \\mathbb{P}(X > s)$$",
    "personalConnection": "A brand new lightbulb with constant microscopic failure rate: having operated for 200 hours without failing gives zero evidence that it will burn out any sooner in the next hour.",
    "examTrap": "Applying the memoryless property to aging physical machinery (car engines, human organs). Most real systems exhibit wear-out (Weibull with shape k > 1), where hazard rate strictly increases."
  },
  {
    "id": 30305,
    "subject": "StoMA",
    "topicId": "03_Discrete_and_Continuous_Random_Variables",
    "topicTitle": "03 \u00b7 Discrete & Continuous RVs",
    "cardNumber": "05",
    "category": "GAUSSIAN FOUNDATION",
    "highlighterClass": "highlight-cyan",
    "title": "Gaussian (Normal) Distribution & Canonical Standardization",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30305\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30305)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30305)\"/><path d=\"M 30,114 Q 80,114 100,85 Q 120,25 125,25 Q 130,25 150,85 Q 170,114 220,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"125\" y1=\"25\" x2=\"125\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"125\" y=\"125\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc</text><line x1=\"100\" y1=\"85\" x2=\"100\" y2=\"114\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 2\"/><line x1=\"150\" y1=\"85\" x2=\"150\" y2=\"114\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 2\"/><text x=\"100\" y=\"125\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc - \u03c3</text><text x=\"150\" y=\"125\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc + \u03c3</text><text x=\"125\" y=\"65\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">68.3% mass</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Symmetric around mean \u03bc, inflection points at \u03bc \u00b1 \u03c3, standard CDF \u03a6(z)</text></svg>",
    "drawingCaption": "The bell curve is completely governed by mean \u03bc and variance \u03c3\u00b2, standardizing via Z = (X - \u03bc)/\u03c3",
    "coreTranslation": [
      "<strong>Density Form:</strong> $f_X(x) = \\frac{1}{\\sqrt{2\\pi}\\sigma} \\exp\\left(-\\frac{(x - \\mu)^2}{2\\sigma^2}\\right)$ on $\\mathbb{R}$. Inflection points occur exactly at $x = \\mu \\pm \\sigma$.",
      "<strong>Z-Score Standardization:</strong> If $X \\sim \\mathcal{N}(\\mu, \\sigma^2)$, then $Z = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1)$, with CDF $\\Phi(z) = \\frac{1}{\\sqrt{2\\pi}}\\int_{-\\infty}^z e^{-u^2/2}du$.",
      "<strong>Symmetry & Tail:</strong> $\\Phi(-z) = 1 - \\Phi(z)$. The tail satisfies Mill's ratio bound: $\\left(\\frac{1}{z} - \\frac{1}{z^3}\\right) \\frac{e^{-z^2/2}}{\\sqrt{2\\pi}} < 1 - \\Phi(z) < \\frac{1}{z} \\frac{e^{-z^2/2}}{\\sqrt{2\\pi}}$."
    ],
    "math": "$$X \\sim \\mathcal{N}(\\mu, \\sigma^2) \\implies Z = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1), \\quad \\Phi(-z) = 1 - \\Phi(z)$$",
    "personalConnection": "Random microscopic measurement errors in high-precision laboratory balances: countless independent micro-disturbances sum to a perfect symmetric bell curve.",
    "examTrap": "Attempting to evaluate \u03a6(z) symbolically by elementary integration. The integral has no closed-form elementary antiderivative; express solutions strictly in terms of \u03a6(z) or Q(z)."
  },
  {
    "id": 30306,
    "subject": "StoMA",
    "topicId": "03_Discrete_and_Continuous_Random_Variables",
    "topicTitle": "03 \u00b7 Discrete & Continuous RVs",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Mixed Random Variable & Lebesgue Splitting",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30306\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30306)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30306)\"/><line x1=\"24\" y1=\"114\" x2=\"60\" y2=\"114\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"60\" y1=\"114\" x2=\"60\" y2=\"85\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"60\" cy=\"85\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"60\" cy=\"114\" r=\"2.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><text x=\"40\" y=\"95\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">jump = 0.3</text><line x1=\"60\" y1=\"85\" x2=\"160\" y2=\"50\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"160\" y1=\"50\" x2=\"160\" y2=\"26\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"160\" cy=\"26\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"160\" cy=\"50\" r=\"2.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"160\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"185\" y=\"38\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">jump = 0.3</text><line x1=\"160\" y1=\"26\" x2=\"215\" y2=\"26\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">E[X] = \u2211 x\u1d62 P(X=x\u1d62) + \u222b x f_c(x) dx = 0(0.3) + 1(0.3) + \u222b 0.4x dx = 0.5</text></svg>",
    "drawingCaption": "Mixed random variables possess both jump atoms and continuous densities; expectations sum discrete and integral parts",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Waiting time $X$ has point mass $\\mathbb{P}(X=0) = 0.3$, point mass $\\mathbb{P}(X=1) = 0.3$, and uniform density $f_c(x) = 0.4$ for $x \\in (0, 1)$.",
      "<strong>CDF Structure:</strong> $F_X(x)$ jumps from 0 to 0.3 at $x=0$, rises linearly with slope 0.4 to 0.7 at $x=1^-$, then jumps by 0.3 to 1.0 at $x=1$.",
      "<strong>Expectation Evaluation:</strong> $\\mathbb{E}[X] = \\sum_k x_k \\mathbb{P}(X=x_k) + \\int_0^1 x f_c(x)\\,dx = 0(0.3) + 1(0.3) + \\int_0^1 0.4 x\\,dx = 0.3 + 0.2 = 0.5$."
    ],
    "math": "$$F_X(x) = \\alpha F_{\\text{disc}}(x) + (1-\\alpha) F_{\\text{cont}}(x), \\quad \\mathbb{E}[X] = \\sum_k x_k \\mathbb{P}(X=x_k) + \\int x f_c(x)\\,dx$$",
    "personalConnection": "An insurance claim policy with a $500 deductible and a $10,000 maximum cap: exact 0 payout for minor damage, continuous claims in between, and a lump spike at $10,000.",
    "examTrap": "Applying \u222b x f(x)dx alone without accounting for point mass jumps! Disregarding atoms F(x) - F(x\u207b) completely invalidates expected values and variances."
  },
  {
    "id": 30401,
    "subject": "StoMA",
    "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
    "topicTitle": "04 \u00b7 Transformations of Random Variables",
    "cardNumber": "01",
    "category": "CDF METHOD",
    "highlighterClass": "highlight-cyan",
    "title": "The CDF Method for Transformations Y = g(X)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30401\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"80\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"56.0\" y=\"37.0\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X ~ f_X(x)</text><line x1=\"96\" y1=\"34\" x2=\"134\" y2=\"34\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30401)\"/><text x=\"115\" y=\"26\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Y = g(X)</text><rect x=\"134\" y=\"20\" width=\"90\" height=\"28\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"179.0\" y=\"37.0\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Find f_Y(y)</text><rect x=\"16\" y=\"62\" width=\"208\" height=\"26\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"74.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Step 1: F_Y(y) = P(Y \u2264 y) =</text><text x=\"120.0\" y=\"83.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(g(X) \u2264 y) = \u222b_{g(x)\u2264y} f_X(x) dx</text><rect x=\"16\" y=\"94\" width=\"208\" height=\"26\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"106.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Step 2: Differentiate: f_Y(y) =</text><text x=\"120.0\" y=\"115.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">d/dy [F_Y(y)]  (by FTC / Leibniz)</text><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">The CDF method works for ALL transformations without requiring monotonicity</text></svg>",
    "drawingCaption": "Universal two-step protocol: compute cumulative probability F_Y(y) = P(g(X) \u2264 y) and differentiate",
    "coreTranslation": [
      "<strong>Universal 2-Step Protocol:</strong> Step 1: express the CDF of $Y$ directly in terms of $X$: $F_Y(y) = \\mathbb{P}(Y \\le y) = \\mathbb{P}(g(X) \\le y) = \\int_{\\{x : g(x) \\le y\\}} f_X(x)\\,dx$.",
      "<strong>Differentiation Step:</strong> Step 2: differentiate $F_Y(y)$ with respect to $y$ (via Fundamental Theorem of Calculus or Leibniz rule) to find density $f_Y(y) = F_Y'(y)$.",
      "<strong>Universal Validity:</strong> Works unconditionally for any measurable $g$ (monotonic, non-monotonic, multi-to-one, piecewise) without requiring invertibility."
    ],
    "math": "$$F_Y(y) = \\mathbb{P}(g(X) \\le y) = \\int_{\\{x: g(x) \\le y\\}} f_X(x)\\,dx, \\qquad f_Y(y) = \\frac{d}{dy} F_Y(y)$$",
    "personalConnection": "Pouring fluid through a shaped glass funnel: measuring the accumulated liquid volume below height y directly from the incoming flow.",
    "examTrap": "Differentiating without determining the valid support of Y! You must track y \u2208 g(supp(X)); omitting indicator functions 1_{y \u2208 support} leads to invalid densities with infinite integrals."
  },
  {
    "id": 30402,
    "subject": "StoMA",
    "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
    "topicTitle": "04 \u00b7 Transformations of Random Variables",
    "cardNumber": "02",
    "category": "JACOBIAN FORMULA",
    "highlighterClass": "highlight-amber",
    "title": "Monotonic Transformation & The 1D Jacobian",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30402\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30402)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30402)\"/><path d=\"M 40,105 Q 80,95 130,55 Q 180,25 210,25\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"180\" y=\"20\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y = g(x)</text><line x1=\"70\" y1=\"114\" x2=\"70\" y2=\"100\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><line x1=\"90\" y1=\"114\" x2=\"90\" y2=\"88\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"80\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">dx</text><line x1=\"24\" y1=\"100\" x2=\"70\" y2=\"100\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><line x1=\"24\" y1=\"88\" x2=\"90\" y2=\"88\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"16\" y=\"94\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">dy</text><text x=\"150\" y=\"85\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_Y(y)|dy| = f_X(x)|dx|</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f_Y(y) = f_X(g\u207b\u00b9(y)) \u00b7 |dx/dy| = f_X(g\u207b\u00b9(y)) / |g'(x)|</text></svg>",
    "drawingCaption": "Conserving probability mass across differential slices: f_Y(y)|dy| = f_X(x)|dx|",
    "coreTranslation": [
      "<strong>1-to-1 Mapping:</strong> If $g$ is strictly monotonic and continuously differentiable on the support of $X$, the inverse $x = g^{-1}(y)$ exists uniquely.",
      "<strong>Mass Conservation:</strong> Probability in an infinitesimal interval must match: $f_Y(y)|dy| = f_X(x)|dx| \\implies f_Y(y) = f_X(g^{-1}(y)) \\left|\\frac{dx}{dy}\\right|$.",
      "<strong>Reciprocal Derivative Form:</strong> Expressing via derivative of $g$: $f_Y(y) = \\frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}$ for all $y$ in the image of $g$."
    ],
    "math": "$$f_Y(y) = f_X\\left(g^{-1}(y)\\right) \\left| \\frac{d}{dy} g^{-1}(y) \\right| = \\frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}, \\quad y \\in g(\\text{supp}(X))$$",
    "personalConnection": "Stretching a rubber band: where the rubber stretches thin (|g'| > 1), the local density of ink marks drops inversely to preserve total ink mass.",
    "examTrap": "Omitting the absolute value |dx/dy| for strictly decreasing functions (e.g. Y = -X or Y = 1/X). Probabilities and densities must NEVER be negative!"
  },
  {
    "id": 30403,
    "subject": "StoMA",
    "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
    "topicTitle": "04 \u00b7 Transformations of Random Variables",
    "cardNumber": "03",
    "category": "MULTI-BRANCH MAPPINGS",
    "highlighterClass": "highlight-emerald",
    "title": "Non-Monotonic Transformations & Multi-Branch Sums",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30403\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30403)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30403)\"/><path d=\"M 50,25 Q 120,115 190,25\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"195\" y=\"25\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y = x\u00b2</text><line x1=\"24\" y1=\"55\" x2=\"215\" y2=\"55\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"3 3\"/><text x=\"16\" y=\"55\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y</text><line x1=\"75\" y1=\"55\" x2=\"75\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><line x1=\"165\" y1=\"55\" x2=\"165\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"75\" cy=\"55\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"165\" cy=\"55\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"75\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">-\u221ay</text><text x=\"165\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">+\u221ay</text><text x=\"120\" y=\"85\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Two roots x\u2081 and x\u2082 contribute</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f_Y(y) = \u2211 f_X(x\u2096) / |g'(x\u2096)| = [f_X(\u221ay) + f_X(-\u221ay)] / (2\u221ay)</text></svg>",
    "drawingCaption": "When g is multi-to-one, the output density sums the probability contributions across all preimage branches",
    "coreTranslation": [
      "<strong>Piecewise Monotonicity:</strong> If $g(x) = y$ has multiple discrete roots $\\{x_1, \\dots, x_k\\}$, split the domain into monotonic segments.",
      "<strong>Branch Summation:</strong> Total density sums contributions from every root: $f_Y(y) = \\sum_{k} f_X(x_k) \\left|\\frac{dx_k}{dy}\\right| = \\sum_{k} \\frac{f_X(x_k)}{|g'(x_k)|}$.",
      "<strong>Canonical Square Law:</strong> For $Y = X^2$, roots are $x = \\pm\\sqrt{y}$, yielding $f_Y(y) = \\frac{1}{2\\sqrt{y}} [f_X(\\sqrt{y}) + f_X(-\\sqrt{y})] \\mathbf{1}_{\\{y > 0\\}}$."
    ],
    "math": "$$f_Y(y) = \\sum_{x_k \\in g^{-1}(y)} \\frac{f_X(x_k)}{|g'(x_k)|}; \\quad Y = X^2 \\implies f_Y(y) = \\frac{f_X(\\sqrt{y}) + f_X(-\\sqrt{y})}{2\\sqrt{y}}\\,\\mathbf{1}_{\\{y>0\\}}$$",
    "personalConnection": "Two mountain streams feeding into a single river: the river's water flow rate is the sum of the flow rates from each separate tributary.",
    "examTrap": "Missing branches when g(x) is even or periodic (e.g. Y = |X|, Y = X\u2074, Y = cos X). Every real root x_k contributing to y must be included in the sum!"
  },
  {
    "id": 30404,
    "subject": "StoMA",
    "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
    "topicTitle": "04 \u00b7 Transformations of Random Variables",
    "cardNumber": "04",
    "category": "GENERATIVE TRANSFORM",
    "highlighterClass": "highlight-purple",
    "title": "Probability Integral Transform & Inverse CDF Sampling",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30404\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30404)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30404)\"/><path d=\"M 24,114 C 70,114 90,80 120,60 C 150,40 180,26 215,26\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"16\" y=\"26\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"16\" y=\"115\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><line x1=\"24\" y1=\"60\" x2=\"120\" y2=\"60\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"24\" y1=\"60\" x2=\"120\" y2=\"60\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30404)\"/><line x1=\"120\" y1=\"60\" x2=\"120\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"120\" y1=\"60\" x2=\"120\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30404)\"/><circle cx=\"120\" cy=\"60\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"16\" y=\"60\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">U</text><text x=\"120\" y=\"126\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X = F\u207b\u00b9(U)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">U ~ Unif(0, 1) \u21d2 X = F\u207b\u00b9(U) has exact distribution F</text></svg>",
    "drawingCaption": "Universal algorithm for sampling random variables: apply the quantile function F\u207b\u00b9 to Uniform(0, 1)",
    "coreTranslation": [
      "<strong>Uniformization Theorem:</strong> If $X$ has continuous CDF $F_X$, the transformed variable $U \\triangleq F_X(X)$ is strictly distributed as $\\text{Uniform}(0, 1)$.",
      "<strong>Inverse Sampling Principle:</strong> Conversely, if $U \\sim \\text{Uniform}(0, 1)$, then $X \\triangleq F_X^{-1}(U)$ has exact CDF $F_X$. This is the basis of all computer random number generators.",
      "<strong>Generalized Inverse:</strong> For CDFs with flat zones or jumps, the quantile function $F_X^{-1}(u) \\triangleq \\inf\\{x : F_X(x) \\ge u\\}$ preserves universality."
    ],
    "math": "$$U = F_X(X) \\sim \\text{Uniform}(0, 1); \\qquad U \\sim \\text{Uniform}(0, 1) \\implies X = F_X^{-1}(U) \\sim F_X$$",
    "personalConnection": "A standardized grading curve: raw test scores X map into uniform percentile ranks U from 0% to 100%; knowing someone's percentile rank inverts back to their exact score.",
    "examTrap": "Applying F_X(X) ~ Uniform(0, 1) to discrete random variables! For discrete distributions, F_X(X) takes only discrete values and is emphatically NOT uniform."
  },
  {
    "id": 30405,
    "subject": "StoMA",
    "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
    "topicTitle": "04 \u00b7 Transformations of Random Variables",
    "cardNumber": "05",
    "category": "CANONICAL TRANSFORM",
    "highlighterClass": "highlight-cyan",
    "title": "Gaussian Square: Derivation of \u03c7\u2081\u00b2 Density",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30405\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30405)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30405)\"/><path d=\"M 28,25 Q 32,80 60,95 Q 110,110 215,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"140\" y=\"45\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Y = Z\u00b2,  Z ~ N(0, 1)</text><text x=\"140\" y=\"62\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f_Y(y) = (2\u03c0y)^{-1/2} e^{-y/2}</text><text x=\"140\" y=\"78\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Gamma(1/2, 1/2) \u2261 \u03c7\u2081\u00b2</text><text x=\"40\" y=\"30\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">y \u2192 0\u207a asymptote</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Squaring standard normal produces Chi-Square with 1 degree of freedom</text></svg>",
    "drawingCaption": "Squaring a standard normal random variable produces the Chi-Square distribution with 1 degree of freedom",
    "coreTranslation": [
      "<strong>Derivation:</strong> For $Z \\sim \\mathcal{N}(0, 1)$ and $Y = Z^2$, apply 2-branch formula: $f_Y(y) = \\frac{1}{2\\sqrt{y}}[f_Z(\\sqrt{y}) + f_Z(-\\sqrt{y})]$.",
      "<strong>Symmetry Simplification:</strong> Gaussian symmetry $f_Z(\\sqrt{y}) = f_Z(-\\sqrt{y}) = \\frac{1}{\\sqrt{2\\pi}} e^{-y/2}$ yields $f_Y(y) = \\frac{1}{\\sqrt{2\\pi y}} e^{-y/2} \\mathbf{1}_{\\{y > 0\\}}$.",
      "<strong>Gamma Identification:</strong> Matches standard Gamma PDF $\\frac{\\lambda^\\alpha}{\\Gamma(\\alpha)} y^{\\alpha - 1} e^{-\\lambda y}$ with $\\alpha = 1/2, \\lambda = 1/2$ (using $\\Gamma(1/2) = \\sqrt{\\pi}$)."
    ],
    "math": "$$Y = Z^2, \\; Z \\sim \\mathcal{N}(0, 1) \\implies f_Y(y) = \\frac{1}{\\sqrt{2\\pi y}} e^{-y/2}\\,\\mathbf{1}_{\\{y > 0\\}} \\sim \\chi_1^2 \\equiv \\text{Gamma}\\left(\\tfrac{1}{2}, \\tfrac{1}{2}\\right)$$",
    "personalConnection": "Kinetic energy of a gas particle with 1D thermal Gaussian velocity v: energy E = (1/2) m v\u00b2 clusters heavily near 0 with an exponential decay tail.",
    "examTrap": "Worrying that f_Y(y) \u2192 \u221e as y \u2192 0\u207a. An integrable pole (y^{-1/2}) is completely legal for continuous probability densities; the integral remains strictly equal to 1."
  },
  {
    "id": 30406,
    "subject": "StoMA",
    "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
    "topicTitle": "04 \u00b7 Transformations of Random Variables",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Tangent Transform & The Cauchy Law",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30406\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"70\" cy=\"72\" rx=\"38\" ry=\"38\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(0 70 72)\"/><line x1=\"70\" y1=\"72\" x2=\"108\" y2=\"72\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"108\" y1=\"18\" x2=\"108\" y2=\"126\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"118\" y=\"25\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">x = tan \u03b8</text><line x1=\"70\" y1=\"72\" x2=\"108\" y2=\"42\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"84\" y=\"64\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b8</text><circle cx=\"108\" cy=\"42\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"116\" y=\"44\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X</text><rect x=\"136\" y=\"36\" width=\"92\" height=\"54\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"182.0\" y=\"62.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_X(x) = \\frac{1}{\\pi(1+x\u00b2)}\nHeavy</text><text x=\"182.0\" y=\"71.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Tails\nE[|X|] = \u221e</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Uniform angle \u03b8 ~ Unif(-\u03c0/2, \u03c0/2) produces Cauchy density with undefined mean</text></svg>",
    "drawingCaption": "Uniform angular projection generates the standard Cauchy distribution whose heavy tails destroy the mean",
    "coreTranslation": [
      "<strong>Projection Setup:</strong> Angle $\\Theta \\sim \\text{Uniform}(-\\pi/2, \\pi/2)$ with density $f_\\Theta(\\theta) = 1/\\pi$. Define shoreline coordinate $X = \\tan(\\Theta)$.",
      "<strong>Jacobian Step:</strong> Inverse is $\\theta = \\arctan(x)$, with derivative $\\left|\\frac{d\\theta}{dx}\\right| = \\frac{1}{1 + x^2}$.",
      "<strong>Standard Cauchy PDF:</strong> $f_X(x) = f_\\Theta(\\arctan x) \\left|\\frac{d\\theta}{dx}\\right| = \\frac{1}{\\pi (1 + x^2)}$ on $\\mathbb{R}$. The integral $\\int_{-\\infty}^\\infty |x| f_X(x)dx = \\infty$, so $\\mathbb{E}[X]$ does not exist!"
    ],
    "math": "$$X = \\tan\\Theta, \\; \\Theta \\sim \\text{Unif}\\left(-\\tfrac{\\pi}{2}, \\tfrac{\\pi}{2}\\right) \\implies f_X(x) = \\frac{1}{\\pi (1 + x^2)}, \\quad \\mathbb{E}[X] \\text{ does not exist!}$$",
    "personalConnection": "A spinning lighthouse beam shining onto a straight infinite coastline: the location of the illuminated light spot on the shore obeys the Cauchy distribution.",
    "examTrap": "Claiming E[X] = 0 by symmetry! For Cauchy, the positive tail integral is +\u221e and the negative tail is -\u221e. The expression \u221e - \u221e is undefined, so the expected value does not exist."
  },
  {
    "id": 30501,
    "subject": "StoMA",
    "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
    "topicTitle": "05 \u00b7 Expectation, Variance & MGFs",
    "cardNumber": "01",
    "category": "EXPECTATION & LOTUS",
    "highlighterClass": "highlight-cyan",
    "title": "Expectation, LOTUS & Universal Linearity",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30501\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"30\" y1=\"95\" x2=\"210\" y2=\"75\" stroke=\"#000000\" stroke-width=\"2.0\"/><polygon points=\"120,85 110,110 130,110\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"120\" y=\"125\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Pivot: E[X]</text><rect x=\"45\" y=\"78\" width=\"20\" height=\"14\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"55\" y=\"88\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2081</text><rect x=\"180\" y=\"58\" width=\"20\" height=\"14\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"190\" y=\"68\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2082</text><rect x=\"24\" y=\"20\" width=\"192\" height=\"30\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"34.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Linearity: E[aX + bY] = a</text><text x=\"120.0\" y=\"43.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[X] + b E[Y]  (Always holds!)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">LOTUS: E[g(X)] = \u222b g(x) f_X(x) dx without finding distribution of g(X)</text></svg>",
    "drawingCaption": "Expectation is the probability center of mass; linearity holds unconditionally without independence",
    "coreTranslation": [
      "<strong>Center of Mass:</strong> $\\mathbb{E}[X] \\triangleq \\int_\\Omega X(\\omega) d\\mathbb{P}(\\omega) = \\int_{-\\infty}^\\infty x\\,dF_X(x)$. Exists if and only if $\\mathbb{E}[|X|] < \\infty$.",
      "<strong>LOTUS:</strong> To compute the expected value of $g(X)$, you do NOT need the density of $g(X)$: $\\mathbb{E}[g(X)] = \\int_{-\\infty}^\\infty g(x) f_X(x)\\,dx$ (Law of the Unconscious Statistician).",
      "<strong>Universal Linearity:</strong> $\\mathbb{E}[\\sum_{i=1}^n c_i X_i] = \\sum_{i=1}^n c_i \\mathbb{E}[X_i]$ holds for ANY random variables, requiring ZERO independence assumptions."
    ],
    "math": "$$\\mathbb{E}[g(X)] = \\int_{-\\infty}^\\infty g(x) f_X(x)\\,dx, \\qquad \\mathbb{E}\\left[\\sum_{i=1}^n c_i X_i\\right] = \\sum_{i=1}^n c_i \\mathbb{E}[X_i]$$",
    "personalConnection": "Center of mass of a physical balance beam: the combined center of mass of several objects is always the weighted sum of their individual centers.",
    "examTrap": "Assuming E[g(X)] = g(E[X]). By Jensen's inequality, this holds only for linear/affine functions; for non-linear convex g, E[g(X)] \u2265 g(E[X])."
  },
  {
    "id": 30502,
    "subject": "StoMA",
    "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
    "topicTitle": "05 \u00b7 Expectation, Variance & MGFs",
    "cardNumber": "02",
    "category": "TAIL PROBABILITY",
    "highlighterClass": "highlight-amber",
    "title": "Tail Sum Integral Formula for Non-Negative RVs",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30502\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30502)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30502)\"/><path d=\"M 24,35 Q 80,45 130,85 Q 180,110 215,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><path d=\"M 24,35 Q 80,45 130,85 Q 180,110 215,114 L 24,114 Z\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.0\"/><text x=\"16\" y=\"35\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"120\" y=\"75\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Area = E[X]</text><text x=\"160\" y=\"40\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(X > t)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">For non-negative RVs (X \u2265 0): E[X] = \u222b\u2080^\u221e P(X > t) dt = \u2211_{k=1}^\u221e P(X \u2265 k)</text></svg>",
    "drawingCaption": "The expected value of a non-negative random variable equals the integral of its survival function",
    "coreTranslation": [
      "<strong>Continuous Tail Formula:</strong> For any non-negative random variable $X \\ge 0$, $\\mathbb{E}[X] = \\int_0^\\infty \\mathbb{P}(X > t)\\,dt$.",
      "<strong>Discrete Integer Formula:</strong> For non-negative integer-valued random variables $X \\in \\{0, 1, 2, \\dots\\}$, $\\mathbb{E}[X] = \\sum_{k=1}^\\infty \\mathbb{P}(X \\ge k)$.",
      "<strong>Higher Moments Extension:</strong> $\\mathbb{E}[X^p] = \\int_0^\\infty p t^{p-1} \\mathbb{P}(X > t)\\,dt$ for any $p > 0$ and $X \\ge 0$."
    ],
    "math": "$$X \\ge 0 \\implies \\mathbb{E}[X] = \\int_0^\\infty \\mathbb{P}(X > t)\\,dt = \\sum_{k=1}^\\infty \\mathbb{P}(X \\ge k) \\quad (X \\in \\mathbb{N}_0)$$",
    "personalConnection": "Measuring the volume of a wedding cake by slicing it horizontally into layers from bottom to top rather than cutting vertical wedges.",
    "examTrap": "Applying the one-sided tail integral to random variables with negative values. For general RVs on \u211d, E[X] = \u222b\u2080^\u221e P(X > t)dt - \u222b_{-\u221e}^0 P(X < t)dt."
  },
  {
    "id": 30503,
    "subject": "StoMA",
    "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
    "topicTitle": "05 \u00b7 Expectation, Variance & MGFs",
    "cardNumber": "03",
    "category": "SECOND MOMENTS",
    "highlighterClass": "highlight-emerald",
    "title": "Variance, Covariance & Bilinear Expansion",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30503\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"64.0\" y=\"37.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var(X) = E[(X-\u03bc)\u00b2]\n=</text><text x=\"64.0\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[X\u00b2] - (E[X])\u00b2</text><rect x=\"128\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"176.0\" y=\"37.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Cov(X,Y) =\nE[XY]</text><text x=\"176.0\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">- E[X]E[Y]</text><rect x=\"16\" y=\"68\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"82\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var(X\u2081 + ... + X_n) = \u2211 Var(X\u1d62) + 2 \u2211_{i &lt; j} Cov(X\u1d62, X_j)</text><text x=\"120\" y=\"98\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">If uncorrelated: Var(\u2211 X\u1d62) = \u2211 Var(X\u1d62)</text><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Variance scales quadratically: Var(aX + b) = a\u00b2 Var(X)</text></svg>",
    "drawingCaption": "Variance measures squared dispersion; sum variance includes all pairwise covariance cross-terms",
    "coreTranslation": [
      "<strong>Definitions:</strong> $\\operatorname{Var}(X) \\triangleq \\mathbb{E}[(X - \\mu)^2] = \\mathbb{E}[X^2] - (\\mathbb{E}[X])^2 \\ge 0$. Covariance: $\\operatorname{Cov}(X, Y) \\triangleq \\mathbb{E}[(X - \\mu_X)(Y - \\mu_Y)]$.",
      "<strong>Quadratic Scaling:</strong> $\\operatorname{Var}(aX + b) = a^2 \\operatorname{Var}(X)$. Additive constants shift position without altering spread.",
      "<strong>Bilinear Expansion:</strong> $\\operatorname{Var}(\\sum_{i=1}^n X_i) = \\sum_{i=1}^n \\operatorname{Var}(X_i) + 2 \\sum_{i < j} \\operatorname{Cov}(X_i, X_j)$. If pairwise uncorrelated, cross-terms vanish."
    ],
    "math": "$$\\operatorname{Var}\\left(\\sum_{i=1}^n X_i\\right) = \\sum_{i=1}^n \\operatorname{Var}(X_i) + 2 \\sum_{1 \\le i < j \\le n} \\operatorname{Cov}(X_i, X_j)$$",
    "personalConnection": "Investment portfolio volatility: total portfolio risk is not merely the sum of asset risks, but is governed primarily by their mutual correlation.",
    "examTrap": "Assuming Cov(X, Y) = 0 implies independence! Zero covariance only means no LINEAR relationship. Deterministic non-linear pairs (e.g. Y = X\u00b2) can have Cov(X, Y) = 0."
  },
  {
    "id": 30504,
    "subject": "StoMA",
    "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
    "topicTitle": "05 \u00b7 Expectation, Variance & MGFs",
    "cardNumber": "04",
    "category": "GENERATING FUNCTIONS",
    "highlighterClass": "highlight-purple",
    "title": "Moment Generating Functions (MGF) & Uniqueness",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30504\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30504)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30504)\"/><path d=\"M 30,110 Q 120,105 120,80 Q 120,40 180,25\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><circle cx=\"120\" cy=\"80\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"105\" y=\"80\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(0, 1)</text><text x=\"170\" y=\"38\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">M_X(t) = E[e^{tX}]</text><line x1=\"70\" y1=\"114\" x2=\"70\" y2=\"25\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 2\"/><line x1=\"170\" y1=\"114\" x2=\"170\" y2=\"25\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 2\"/><text x=\"120\" y=\"126\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">open interval (-h, h) around 0</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">M_X'(0) = E[X],  M_X''(0) = E[X\u00b2];  X \u22a5 Y \u21d2 M_{X+Y}(t) = M_X(t) M_Y(t)</text></svg>",
    "drawingCaption": "The MGF generates all moments via derivatives at 0; identity of MGFs uniquely determines the distribution",
    "coreTranslation": [
      "<strong>Definition:</strong> $M_X(t) \\triangleq \\mathbb{E}[e^{tX}]$. If $M_X(t) < \\infty$ on $(-h, h)$ around $t=0$, then $\\mathbb{E}[X^k] = M_X^{(k)}(0)$ for all $k \\ge 1$.",
      "<strong>Convolution Factorization:</strong> For independent random variables $X \\perp Y$, $M_{X+Y}(t) = \\mathbb{E}[e^{t(X+Y)}] = M_X(t) M_Y(t)$. Sums of RVs become products of MGFs.",
      "<strong>Uniqueness Theorem:</strong> If $M_X(t) = M_Y(t)$ in an open neighborhood around $0$, then $X$ and $Y$ have the exact same probability distribution."
    ],
    "math": "$$M_X(t) = \\mathbb{E}[e^{tX}] = \\sum_{k=0}^\\infty \\frac{t^k}{k!} \\mathbb{E}[X^k], \\quad X \\perp Y \\implies M_{X+Y}(t) = M_X(t) M_Y(t)$$",
    "personalConnection": "A genetic fingerprint: an analytical formula that uniquely encodes the entire infinite sequence of moments for a probability distribution.",
    "examTrap": "Assuming the MGF always exists! Heavy-tailed distributions (Cauchy, Pareto, Log-Normal) have M_X(t) = \u221e for all t > 0. In such cases, use the Characteristic Function \u03c6_X(t) = E[e^{itX}]."
  },
  {
    "id": 30505,
    "subject": "StoMA",
    "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
    "topicTitle": "05 \u00b7 Expectation, Variance & MGFs",
    "cardNumber": "05",
    "category": "DISCRETE GENERATING",
    "highlighterClass": "highlight-cyan",
    "title": "Probability Generating Function (PGF) & Branching",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30505\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"75\" cy=\"72\" rx=\"42\" ry=\"42\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(0 75 72)\"/><line x1=\"30\" y1=\"72\" x2=\"120\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30505)\"/><line x1=\"30\" y1=\"72\" x2=\"30\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30505)\"/><text x=\"118\" y=\"72\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Re(s)</text><text x=\"75\" y=\"26\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Im(s)</text><text x=\"75\" y=\"52\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">|s| \u2264 1</text><circle cx=\"117\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"117\" y=\"84\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s=1</text><rect x=\"130\" y=\"24\" width=\"96\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"178.0\" y=\"45.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">G_X(s) = E[s^X]\n=</text><text x=\"178.0\" y=\"54.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2211 P(X=k) s^k</text><rect x=\"130\" y=\"74\" width=\"96\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"178.0\" y=\"95.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[X] = G_X'(1)\nVar</text><text x=\"178.0\" y=\"104.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= G''(1)+G'(1)-(G')\u00b2</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Random Sums / Branching: G_{\u2211_{i=1}^N X\u1d62}(s) = G_N(G_X(s))</text></svg>",
    "drawingCaption": "For integer random variables, the PGF always converges on the unit disk; random sums compose PGFs",
    "coreTranslation": [
      "<strong>Definition:</strong> For $X \\in \\mathbb{N}_0$, $G_X(s) \\triangleq \\mathbb{E}[s^X] = \\sum_{k=0}^\\infty p_k s^k$. Always converges absolutely for all $|s| \\le 1$ with $G_X(1) = 1$.",
      "<strong>Probability Extraction:</strong> $\\mathbb{P}(X = k) = \\frac{1}{k!} G_X^{(k)}(0)$. Moments: $\\mathbb{E}[X] = G_X'(1)$ and $\\operatorname{Var}(X) = G_X''(1) + G_X'(1) - (G_X'(1))^2$.",
      "<strong>Random Sums (Branching):</strong> If $S_N = \\sum_{i=1}^N X_i$ with $X_i$ i.i.d. and independent of $N$, then $G_{S_N}(s) = G_N(G_X(s))$ (functional composition)."
    ],
    "math": "$$G_X(s) = \\mathbb{E}[s^X] = \\sum_{k=0}^\\infty \\mathbb{P}(X=k) s^k, \\quad \\mathbb{E}[X] = G_X'(1), \\quad G_{\\sum_{i=1}^N X_i}(s) = G_N(G_X(s))$$",
    "personalConnection": "Russian nesting dolls (Matryoshka): composing G_N with G_X places the offspring distribution directly inside the parent population count.",
    "examTrap": "Evaluating moments at s = 0 instead of s = 1! G_X(0) = P(X = 0), while expectations and variances require derivatives evaluated at s = 1."
  },
  {
    "id": 30506,
    "subject": "StoMA",
    "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
    "topicTitle": "05 \u00b7 Expectation, Variance & MGFs",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Zero Covariance \u2260 Independence (Y = X\u00b2)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30506\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30506)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30506)\"/><circle cx=\"60\" cy=\"45\" r=\"5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"32\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(-1, 1)</text><circle cx=\"120\" cy=\"114\" r=\"5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"102\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(0, 0)</text><circle cx=\"180\" cy=\"45\" r=\"5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"180\" y=\"32\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(1, 1)</text><path d=\"M 40,30 Q 120,130 200,30\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" stroke-dasharray=\"3 3\"/><text x=\"120\" y=\"68\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Cov(X, X\u00b2) = E[X\u00b3] - E[X]E[X\u00b2] = 0 - 0 = 0</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Zero covariance does NOT imply independence! Y is completely determined by X</text></svg>",
    "drawingCaption": "Symmetric non-linear relationships yield exactly zero covariance while being 100% deterministic",
    "coreTranslation": [
      "<strong>Symmetric Setup:</strong> Let $X \\in \\{-1, 0, 1\\}$ with equal probability $1/3$ each. Let $Y = X^2$.",
      "<strong>Covariance Evaluation:</strong> By symmetry, $\\mathbb{E}[X] = 0$ and $\\mathbb{E}[XY] = \\mathbb{E}[X^3] = \\frac{(-1)^3 + 0^3 + 1^3}{3} = 0$. Thus $\\operatorname{Cov}(X, Y) = 0 - 0 = 0$.",
      "<strong>Complete Dependence:</strong> $\\mathbb{P}(X=0, Y=1) = 0 \\ne \\mathbb{P}(X=0)\\mathbb{P}(Y=1) = \\frac{1}{3} \\times \\frac{2}{3} = \\frac{2}{9}$. Knowing $X$ determines $Y$ with 100% certainty!"
    ],
    "math": "$$\\mathbb{E}[X] = 0, \\quad \\mathbb{E}[X^3] = 0 \\implies \\operatorname{Cov}(X, X^2) = 0; \\quad \\mathbb{P}(X=0, X^2=1) = 0 \\ne \\tfrac{2}{9}$$",
    "personalConnection": "A parabolic satellite dish: knowing horizontal coordinate X dictates vertical focus coordinate Y = X\u00b2 with exact precision, yet linear correlation registers 0.",
    "examTrap": "Assuming uncorrelated variables are independent! Covariance measures ONLY linear association; quadratic, circular, or higher-order dependencies have Cov = 0."
  },
  {
    "id": 30601,
    "subject": "StoMA",
    "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
    "topicTitle": "06 \u00b7 Probability Inequalities",
    "cardNumber": "01",
    "category": "MOMENT BOUND",
    "highlighterClass": "highlight-cyan",
    "title": "Markov\u2019s Inequality: The Foundation of Concentration",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30601\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30601)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30601)\"/><line x1=\"24\" y1=\"114\" x2=\"190\" y2=\"28\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"3 3\"/><text x=\"195\" y=\"25\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">y = x</text><line x1=\"24\" y1=\"114\" x2=\"110\" y2=\"114\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"110\" y1=\"114\" x2=\"110\" y2=\"68\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"110\" y1=\"68\" x2=\"215\" y2=\"68\" stroke=\"#000000\" stroke-width=\"2.2\"/><circle cx=\"110\" cy=\"68\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"110\" cy=\"114\" r=\"2.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"16\" y=\"68\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">a</text><text x=\"110\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">a</text><text x=\"160\" y=\"54\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">a \u00b7 1_{X \u2265 a} \u2264 X</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Taking expectations: a P(X \u2265 a) \u2264 E[X] \u21d2 P(X \u2265 a) \u2264 E[X] / a  (X \u2265 0)</text></svg>",
    "drawingCaption": "The step indicator a 1_{X \u2265 a} lies everywhere below X; taking expectations proves P(X \u2265 a) \u2264 E[X]/a",
    "coreTranslation": [
      "<strong>Hypothesis & Bound:</strong> For any non-negative random variable $X \\ge 0$ and any threshold $a > 0$, $\\mathbb{P}(X \\ge a) \\le \\frac{\\mathbb{E}[X]}{a}$.",
      "<strong>Indicator Proof:</strong> Observe that $a \\mathbf{1}_{\\{X \\ge a\\}} \\le X \\mathbf{1}_{\\{X \\ge a\\}} \\le X$. Taking expectations preserves monotonicity: $a \\mathbb{E}[\\mathbf{1}_{\\{X \\ge a\\}}] = a \\mathbb{P}(X \\ge a) \\le \\mathbb{E}[X]$.",
      "<strong>Master Engine:</strong> Markov is the foundational engine generating Chebyshev (via $\\phi(u)=u^2$), Chernoff (via $\\phi(u)=e^{tu}$), and all higher-order concentration inequalities."
    ],
    "math": "$$X \\ge 0, \\; a > 0 \\implies a\\,\\mathbf{1}_{\\{X \\ge a\\}} \\le X \\implies \\mathbb{P}(X \\ge a) \\le \\frac{\\mathbb{E}[X]}{a}$$",
    "personalConnection": "Average wealth in a society: if mean wealth is $50,000, at most 10% of citizens can possess $500,000 or more, otherwise the total wealth would exceed the mean.",
    "examTrap": "Applying Markov directly to random variables with negative values! Markov strictly requires X \u2265 0. For general variables, apply Markov to |X|, (X - \u03bc)\u00b2, or e^{tX}."
  },
  {
    "id": 30602,
    "subject": "StoMA",
    "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
    "topicTitle": "06 \u00b7 Probability Inequalities",
    "cardNumber": "02",
    "category": "VARIANCE BOUND",
    "highlighterClass": "highlight-amber",
    "title": "Chebyshev\u2019s Inequality & Variance Dispersion",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30602\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30602)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30602)\"/><path d=\"M 30,114 Q 80,114 100,85 Q 120,25 125,25 Q 130,25 150,85 Q 170,114 220,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"125\" y1=\"25\" x2=\"125\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"125\" y=\"125\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc</text><line x1=\"75\" y1=\"55\" x2=\"75\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"175\" y1=\"55\" x2=\"175\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"75\" y=\"125\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc - k\u03c3</text><text x=\"175\" y=\"125\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc + k\u03c3</text><path d=\"M 30,114 Q 60,114 75,100 L 75,114 Z\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.0\"/><path d=\"M 175,100 Q 190,114 220,114 L 175,114 Z\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.0\"/><text x=\"120\" y=\"50\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(|X - \u03bc| \u2265 k\u03c3) \u2264 1 / k\u00b2</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Universal dispersion bound: at least (1 - 1/k\u00b2) mass lies within k standard deviations</text></svg>",
    "drawingCaption": "Chebyshev bounds deviation from the mean: tail probability outside k standard deviations is at most 1/k\u00b2",
    "coreTranslation": [
      "<strong>Formal Statement:</strong> For any random variable with mean $\\mu$ and finite variance $\\sigma^2$, $\\mathbb{P}(|X - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(X)}{\\epsilon^2}$.",
      "<strong>Canonical Form ($k\\sigma$):</strong> Setting $\\epsilon = k\\sigma$, $\\mathbb{P}(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$.",
      "<strong>Distribution-Free Guarantee:</strong> Holds for ANY distribution: at least $75\\%$ of mass lies within $2\\sigma$ ($k=2$), and at least $88.89\\%$ lies within $3\\sigma$ ($k=3$), regardless of skewness."
    ],
    "math": "$$\\mathbb{P}(|X - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(X)}{\\epsilon^2}, \\qquad \\mathbb{P}(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$$",
    "personalConnection": "Factory quality control: regardless of how defective or skewed machine tolerances are, at least 96% of items must lie within 5 standard deviations (failure rate \u2264 4%).",
    "examTrap": "Using Chebyshev when a 1-sided bound is required. For 1-sided deviations P(X - \u03bc \u2265 \u03b5), Cantelli's inequality gives the strictly sharper bound \u03c3\u00b2 / (\u03c3\u00b2 + \u03b5\u00b2)."
  },
  {
    "id": 30603,
    "subject": "StoMA",
    "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
    "topicTitle": "06 \u00b7 Probability Inequalities",
    "cardNumber": "03",
    "category": "EXPONENTIAL CONCENTRATION",
    "highlighterClass": "highlight-emerald",
    "title": "The Chernoff Bound & Exponential Moment Optimization",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30603\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30603)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30603)\"/><path d=\"M 35,30 Q 100,105 130,105 Q 160,105 210,30\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><circle cx=\"130\" cy=\"105\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"130\" y1=\"105\" x2=\"130\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"130\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">t* (optimal tilt)</text><text x=\"130\" y=\"92\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">inf_{t > 0} e^{-ta} M_X(t)</text><text x=\"120\" y=\"16\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(X \u2265 a) \u2264 e^{-ta} M_X(t)  \u2200 t > 0</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Exponential Markov bound optimized over t > 0 gives exponential tail decay</text></svg>",
    "drawingCaption": "Applying Markov to e^{tX} and optimizing over tilt parameter t > 0 delivers sharp exponential concentration",
    "coreTranslation": [
      "<strong>Exponential Markov Step:</strong> For any $t > 0$, $\\mathbb{P}(X \\ge a) = \\mathbb{P}(e^{tX} \\ge e^{ta}) \\le \\frac{\\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t)$.",
      "<strong>Convex Dual Optimization:</strong> Squeezing over all $t > 0$ yields the sharpest bound: $\\mathbb{P}(X \\ge a) \\le \\inf_{t > 0} \\exp(-(ta - \\log M_X(t)))$.",
      "<strong>Legendre-Fenchel Conjugate:</strong> Exponent $-I(a) \\triangleq -\\sup_{t > 0}(ta - \\Lambda_X(t))$ is the convex conjugate of the cumulant MGF, giving exponential decay $O(e^{-n I(a)})$ for sample sums."
    ],
    "math": "$$\\mathbb{P}(X \\ge a) \\le \\inf_{t > 0} e^{-ta} M_X(t) = \\exp\\left(-\\sup_{t > 0}[ta - \\Lambda_X(t)]\\right)$$",
    "personalConnection": "Focusing an optical laser: tuning parameter t sharpens the probability bound until it reaches the absolute tightest physical focus point.",
    "examTrap": "Forgetting the constraint t > 0 for upper tails (and t < 0 for lower tails P(X \u2264 a)). Plugging negative t into an upper-tail bound flips the inequality direction!"
  },
  {
    "id": 30604,
    "subject": "StoMA",
    "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
    "topicTitle": "06 \u00b7 Probability Inequalities",
    "cardNumber": "04",
    "category": "CONVEXITY",
    "highlighterClass": "highlight-purple",
    "title": "Jensen\u2019s Inequality: Secant Dominance & Convexity",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30604\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30604)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30604)\"/><path d=\"M 40,105 Q 120,110 190,30\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"195\" y=\"30\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g(x)</text><line x1=\"55\" y1=\"100\" x2=\"175\" y2=\"45\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"115\" y1=\"114\" x2=\"115\" y2=\"96\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><circle cx=\"115\" cy=\"96\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"115\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">E[X]</text><text x=\"80\" y=\"96\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g(E[X])</text><circle cx=\"115\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"80\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[g(X)]</text><line x1=\"115\" y1=\"72\" x2=\"115\" y2=\"96\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"155\" y=\"85\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g(E[X]) \u2264 E[g(X)]</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">For convex g, secants lie above the curve: the function of the mean is below the mean of the function</text></svg>",
    "drawingCaption": "For any convex function g, the secant line lies above the curve, ensuring g(E[X]) \u2264 E[g(X)]",
    "coreTranslation": [
      "<strong>Convexity Definition:</strong> Function $g$ is convex if $g(\\lambda x + (1-\\lambda)y) \\le \\lambda g(x) + (1-\\lambda)g(y)$ for all $\\lambda \\in [0, 1]$.",
      "<strong>Jensen\u2019s Statement:</strong> If $g$ is convex and expectations exist, $g(\\mathbb{E}[X]) \\le \\mathbb{E}[g(X)]$.",
      "<strong>Supporting Hyperplane Proof:</strong> At $\\mu = \\mathbb{E}[X]$, a tangent subgradient $c$ satisfies $g(x) \\ge g(\\mu) + c(x - \\mu)$. Taking expectations: $\\mathbb{E}[g(X)] \\ge g(\\mu) + c(0) = g(\\mathbb{E}[X])$."
    ],
    "math": "$$g \\text{ convex} \\implies g(\\mathbb{E}[X]) \\le \\mathbb{E}[g(X)]; \\qquad g \\text{ concave} \\implies \\mathbb{E}[g(X)] \\le g(\\mathbb{E}[X])$$",
    "personalConnection": "Driving with varying speeds: traveling 100 miles at 40 mph then 100 miles at 60 mph takes longer than driving constant 50 mph because travel time T(v) = D/v is strictly convex.",
    "examTrap": "Reversing the inequality for concave functions! For concave functions like log(x) or \u221ax, E[g(X)] \u2264 g(E[X]) (which directly proves the Arithmetic-Geometric Mean AM-GM inequality)."
  },
  {
    "id": 30605,
    "subject": "StoMA",
    "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
    "topicTitle": "06 \u00b7 Probability Inequalities",
    "cardNumber": "05",
    "category": "CANONICAL BOUNDS",
    "highlighterClass": "highlight-cyan",
    "title": "Cauchy-Schwarz & Hoeffding\u2019s Concentration Inequality",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30605\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"96\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"64.0\" y=\"40.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Cauchy-Schwarz:\n|E[XY]|\u00b2 \u2264</text><text x=\"64.0\" y=\"49.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[X\u00b2]E[Y\u00b2]\n(Equality \u21d4 Y = cX)</text><rect x=\"128\" y=\"20\" width=\"96\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"176.0\" y=\"40.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Hoeffding's Lemma:\nX \u2208 [a, b],</text><text x=\"176.0\" y=\"49.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[X]=0\nM_X(t) \u2264 e^{t\u00b2(b-a)\u00b2/8}</text><rect x=\"16\" y=\"72\" width=\"208\" height=\"42\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"86\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Hoeffding's Inequality (Sums of Bounded Independent RVs):</text><text x=\"120\" y=\"102\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(\u2211 (X\u1d62 - \u03bc\u1d62) \u2265 t) \u2264 exp( - 2t\u00b2 / \u2211 (b\u1d62 - a\u1d62)\u00b2 )</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Cauchy-Schwarz bounds correlations (|\u03c1| \u2264 1); Hoeffding bounds tails of bounded sums</text></svg>",
    "drawingCaption": "Cauchy-Schwarz bounds inner products; Hoeffding provides sub-Gaussian tails for bounded independent sums",
    "coreTranslation": [
      "<strong>Cauchy-Schwarz:</strong> $|\\mathbb{E}[XY]|^2 \\le \\mathbb{E}[X^2]\\,\\mathbb{E}[Y^2]$. Equality holds if and only if $Y = c X$ almost surely for some constant $c$. Guarantees correlation $|\\rho_{X,Y}| \\le 1$.",
      "<strong>Hoeffding's Lemma:</strong> If $X \\in [a, b]$ with $\\mathbb{E}[X] = 0$, its MGF satisfies sub-Gaussian proxy $M_X(t) \\le \\exp\\left(\\frac{t^2(b - a)^2}{8}\\right)$.",
      "<strong>Hoeffding\u2019s Inequality:</strong> For independent $X_i \\in [a_i, b_i]$, $\\mathbb{P}(\\sum_{i=1}^n (X_i - \\mu_i) \\ge t) \\le \\exp\\left(-\\frac{2t^2}{\\sum_{i=1}^n (b_i - a_i)^2}\\right)$."
    ],
    "math": "$$|\\mathbb{E}[XY]|^2 \\le \\mathbb{E}[X^2]\\mathbb{E}[Y^2], \\quad \\mathbb{P}\\left(\\sum_{i=1}^n (X_i - \\mu_i) \\ge t\\right) \\le \\exp\\left(-\\frac{2t^2}{\\sum_{i=1}^n (b_i - a_i)^2}\\right)$$",
    "personalConnection": "Geometric dot product: the shadow cast by vector X onto Y cannot exceed the product of their lengths (|cos \u03b8| \u2264 1).",
    "examTrap": "Applying Hoeffding to dependent variables! Mutual independence of X\u2081,...,X_n is strictly mandatory to factorize the joint MGF in Hoeffding's proof."
  },
  {
    "id": 30606,
    "subject": "StoMA",
    "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
    "topicTitle": "06 \u00b7 Probability Inequalities",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Chernoff vs Chebyshev on Coin Flips",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30606\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30606)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30606)\"/><path d=\"M 30,35 Q 70,75 120,95 Q 170,105 215,110\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"3 3\"/><text x=\"200\" y=\"100\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Chebyshev: 4/n</text><path d=\"M 30,35 Q 45,95 70,112 L 215,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/><text x=\"90\" y=\"80\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Chernoff: e^{-n/8}</text><rect x=\"110\" y=\"24\" width=\"114\" height=\"46\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"167.0\" y=\"46.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">For n = 100:\nChebyshev: \u2264 0.04</text><text x=\"167.0\" y=\"55.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(4%)\nChernoff: \u2264 3.7 \u00d7 10\u207b\u2076</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Chernoff delivers exponential concentration; Chebyshev provides only weak polynomial decay</text></svg>",
    "drawingCaption": "Chebyshev gives weak O(1/n) polynomial bounds; Chernoff harnesses all moments to achieve exponential decay",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Let $S_n \\sim \\text{Binomial}(n, 1/2)$, so $\\mu = n/2$ and $\\sigma^2 = n/4$. Bound tail $\\mathbb{P}(S_n \\ge \\frac{3}{4}n)$ ($\\ge 25\\%$ excess).",
      "<strong>Chebyshev Evaluation:</strong> $\\mathbb{P}(S_n - n/2 \\ge n/4) \\le \\frac{\\sigma^2}{(n/4)^2} = \\frac{n/4}{n^2/16} = \\frac{4}{n}$ (slow polynomial rate $O(1/n)$).",
      "<strong>Chernoff Evaluation:</strong> Hoeffding gives $\\exp(-2(n/4)^2 / n) = \\exp(-n/8)$. For $n=100$: Chebyshev gives $\\le 0.04$, while Chernoff gives $\\le e^{-12.5} \\approx 3.7 \\times 10^{-6}$!"
    ],
    "math": "$$\\mathbb{P}\\left(S_n \\ge \\tfrac{3}{4}n\\right) \\le \\frac{4}{n} \\quad (\\text{Chebyshev}) \\quad \\text{vs} \\quad \\exp\\left(-\\frac{n}{8}\\right) \\quad (\\text{Chernoff/Hoeffding})$$",
    "personalConnection": "A structural safety factor: Chebyshev guarantees the bridge stands with 96% confidence, while Chernoff proves the failure probability is under four in a million.",
    "examTrap": "Using Chebyshev for large sample sizes (n >> 100). Chebyshev captures only 2nd moments, missing the exponential destructive cancellation across independent terms."
  },
  {
    "id": 30701,
    "subject": "StoMA",
    "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
    "topicTitle": "07 \u00b7 Joint, Marginal & Conditional Distributions",
    "cardNumber": "01",
    "category": "JOINT CDF",
    "highlighterClass": "highlight-cyan",
    "title": "Joint Cumulative Distribution Function & 2D Rectangle Measure",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30701\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30701)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30701)\"/><rect x=\"60\" y=\"45\" width=\"90\" height=\"50\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"105\" y=\"70\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(a &lt; X \u2264 b, c &lt; Y \u2264 d)</text><circle cx=\"60\" cy=\"95\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"50\" y=\"102\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(a, c)</text><circle cx=\"150\" cy=\"95\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"160\" y=\"102\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(b, c)</text><circle cx=\"60\" cy=\"45\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"50\" y=\"40\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(a, d)</text><circle cx=\"150\" cy=\"45\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"160\" y=\"40\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(b, d)</text><rect x=\"24\" y=\"18\" width=\"192\" height=\"22\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"28.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u0394_{a,c}^{b,d} F = F(b, d) -</text><text x=\"120.0\" y=\"36.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">F(a, d) - F(b, c) + F(a, c) \u2265 0</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2D CDF must satisfy 2-monotonicity: all rectangle probabilities must be non-negative</text></svg>",
    "drawingCaption": "The 2D rectangle formula computes cell probability by inclusion-exclusion of quadrant corners",
    "coreTranslation": [
      "<strong>Joint CDF:</strong> $F_{X,Y}(x, y) \\triangleq \\mathbb{P}(X \\le x, Y \\le y)$ evaluates the cumulative measure of infinite lower-left quadrant $(-\\infty, x] \\times (-\\infty, y]$.",
      "<strong>2D Rectangle Measure:</strong> Probability in $(a, b] \\times (c, d]$ is $\\mathbb{P}(a < X \\le b, c < Y \\le d) = F(b, d) - F(a, d) - F(b, c) + F(a, c) \\ge 0$.",
      "<strong>2-Monotonicity Axiom:</strong> Increasing in $x$ and $y$ separately is NOT enough! The 2D cross-difference must be non-negative for every rectangle."
    ],
    "math": "$$\\mathbb{P}(a < X \\le b, c < Y \\le d) = F_{X,Y}(b, d) - F_{X,Y}(a, d) - F_{X,Y}(b, c) + F_{X,Y}(a, c) \\ge 0$$",
    "personalConnection": "Measuring the area of an interior floor tile by subtracting left and bottom border carpets and restoring the doubly subtracted corner piece.",
    "examTrap": "Assuming coordinate-wise monotonicity guarantees a valid 2D CDF. Functions exist where \u2202F/\u2202x \u2265 0 and \u2202F/\u2202y \u2265 0, yet the rectangle measure evaluates to a negative number!"
  },
  {
    "id": 30702,
    "subject": "StoMA",
    "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
    "topicTitle": "07 \u00b7 Joint, Marginal & Conditional Distributions",
    "cardNumber": "02",
    "category": "CONTINUOUS 2D",
    "highlighterClass": "highlight-amber",
    "title": "Joint Probability Density Function & Probability as Volume",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30702\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"40,110 140,110 200,75 100,75\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"120\" y=\"102\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Region A in xy-plane</text><path d=\"M 80,95 L 80,45 Q 120,30 160,40 L 160,85 L 80,95 Z\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120\" y=\"58\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Volume = P((X, Y) \u2208 A)</text><text x=\"165\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">z = f_{X,Y}(x, y)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Joint density: Probability is volume under 2D surface; f(x, y) = \u2202\u00b2F / \u2202x\u2202y</text></svg>",
    "drawingCaption": "The joint PDF f_{X,Y}(x, y) defines a surface whose volume above any 2D region A equals P((X, Y) \u2208 A)",
    "coreTranslation": [
      "<strong>Mixed Derivative:</strong> If $F_{X,Y}$ is differentiable, the joint PDF is $f_{X,Y}(x, y) = \\frac{\\partial^2 F_{X,Y}(x, y)}{\\partial x \\partial y}$.",
      "<strong>Volume Representation:</strong> For any Borel region $A \\subseteq \\mathbb{R}^2$, $\\mathbb{P}((X, Y) \\in A) = \\iint_A f_{X,Y}(x, y)\\,dx\\,dy$.",
      "<strong>Normalization:</strong> $f_{X,Y}(x, y) \\ge 0$ everywhere and total volume $\\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f_{X,Y}(x, y)\\,dx\\,dy = 1$."
    ],
    "math": "$$f_{X,Y}(x, y) = \\frac{\\partial^2 F_{X,Y}(x, y)}{\\partial x \\partial y}, \\qquad \\mathbb{P}((X, Y) \\in A) = \\iint_A f_{X,Y}(x, y)\\,dx\\,dy$$",
    "personalConnection": "A topographical relief map of sand on a tabletop: the probability of a falling drop hitting zone A is the exact physical volume of sand standing directly over A.",
    "examTrap": "Swapping integration order in non-rectangular domains without adjusting boundaries! For coupled domains like 0 \u2264 x \u2264 y \u2264 1, \u222b\u2080\u00b9 dx \u222b_x\u00b9 dy = \u222b\u2080\u00b9 dy \u222b\u2080^y dx."
  },
  {
    "id": 30703,
    "subject": "StoMA",
    "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
    "topicTitle": "07 \u00b7 Joint, Marginal & Conditional Distributions",
    "cardNumber": "03",
    "category": "MARGINALIZATION",
    "highlighterClass": "highlight-emerald",
    "title": "Marginal Distributions: Collapsing Dimensions",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30703\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"115\" cy=\"65\" rx=\"45\" ry=\"28\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(20 115 65)\"/><text x=\"115\" y=\"65\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_{X,Y}(x, y)</text><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30703)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30703)\"/><line x1=\"70\" y1=\"65\" x2=\"70\" y2=\"114\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 2\"/><line x1=\"160\" y1=\"65\" x2=\"160\" y2=\"114\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 2\"/><path d=\"M 70,114 Q 115,85 160,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"115\" y=\"96\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_X(x) = \u222b f(x, y) dy</text><path d=\"M 24,40 Q 42,65 24,90\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"40\" y=\"35\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f_Y(y) = \u222b f(x, y) dx</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Marginalization collapses dimensions by integrating out the unwanted variable</text></svg>",
    "drawingCaption": "Marginals project joint densities onto 1D coordinate axes by integrating out the orthogonal variable",
    "coreTranslation": [
      "<strong>Continuous Marginalization:</strong> $f_X(x) = \\int_{-\\infty}^\\infty f_{X,Y}(x, y)\\,dy$ and $f_Y(y) = \\int_{-\\infty}^\\infty f_{X,Y}(x, y)\\,dx$.",
      "<strong>Discrete Marginalization:</strong> $p_X(x) = \\sum_{y} p_{X,Y}(x, y)$ and $p_Y(y) = \\sum_{x} p_{X,Y}(x, y)$ (row and column sums).",
      "<strong>Correlation Erasure:</strong> Marginals retain only single-variable laws, discarding all mutual dependence structure. Infinite distinct joints share the same marginals."
    ],
    "math": "$$f_X(x) = \\int_{-\\infty}^\\infty f_{X,Y}(x, y)\\,dy, \\qquad p_X(x) = \\sum_{y} p_{X,Y}(x, y)$$",
    "personalConnection": "A 2D shadow of a flying bird: the shadow on the ground collapses vertical altitude while preserving horizontal ground position.",
    "examTrap": "Neglecting dependent boundary limits during integration! If the support is triangular 0 \u2264 y \u2264 x \u2264 1, then f_X(x) = \u222b\u2080^x f(x, y)dy, NOT \u222b\u2080\u00b9!"
  },
  {
    "id": 30704,
    "subject": "StoMA",
    "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
    "topicTitle": "07 \u00b7 Joint, Marginal & Conditional Distributions",
    "cardNumber": "04",
    "category": "CONDITIONAL DENSITIES",
    "highlighterClass": "highlight-purple",
    "title": "Conditional Density: Slicing and Renormalizing",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30704\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30704)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30704)\"/><ellipse cx=\"120\" cy=\"65\" rx=\"55\" ry=\"30\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(0 120 65)\"/><ellipse cx=\"120\" cy=\"65\" rx=\"35\" ry=\"18\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(0 120 65)\"/><line x1=\"140\" y1=\"25\" x2=\"140\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.8\"/><circle cx=\"140\" cy=\"65\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"140\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X = x</text><rect x=\"150\" y=\"40\" width=\"80\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"190.0\" y=\"57.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Slice profile:\nf_{Y|X}(y|x)</text><text x=\"190.0\" y=\"65.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">=\nf(x, y) / f_X(x)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Conditional PDF is the 1D slice along X=x re-normalized by 1/f_X(x) to integrate to 1</text></svg>",
    "drawingCaption": "The conditional PDF f_{Y|X}(y|x) is a 1D cross-sectional slice of the joint surface normalized to area 1",
    "coreTranslation": [
      "<strong>Formal Definition:</strong> For any $x$ with $f_X(x) > 0$, the conditional PDF of $Y$ given $X=x$ is $f_{Y \\mid X}(y \\mid x) \\triangleq \\frac{f_{X,Y}(x, y)}{f_X(x)}$.",
      "<strong>Bona Fide 1D Density:</strong> For fixed $x$, the function $y \\mapsto f_{Y \\mid X}(y \\mid x)$ is a valid density on $\\mathbb{R}$: non-negative and integrates to $\\int_{-\\infty}^\\infty f_{Y \\mid X}(y \\mid x)\\,dy = 1$.",
      "<strong>Cross-Section Geometry:</strong> Taking a knife slice across the 2D density mountain along $X=x$, dividing by marginal $f_X(x)$ to restore unit area."
    ],
    "math": "$$f_{Y \\mid X}(y \\mid x) = \\frac{f_{X,Y}(x, y)}{f_X(x)}, \\quad f_X(x) > 0; \\qquad \\int_{-\\infty}^\\infty f_{Y \\mid X}(y \\mid x)\\,dy = 1$$",
    "personalConnection": "A CT scan slice through a medical patient: isolating the 2D organ profile at a fixed longitudinal position x.",
    "examTrap": "Borel-Kolmogorov Paradox: conditioning continuous distributions on measure-zero curves g(X,Y)=0 depends on the coordinate parametrization! Slicing is well-defined along coordinate projections."
  },
  {
    "id": 30705,
    "subject": "StoMA",
    "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
    "topicTitle": "07 \u00b7 Joint, Marginal & Conditional Distributions",
    "cardNumber": "05",
    "category": "INDEPENDENCE",
    "highlighterClass": "highlight-cyan",
    "title": "Independence: Factorization & The Product Support Test",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30705\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"25\" width=\"85\" height=\"65\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"66\" y=\"57\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">S_X \u00d7 S_Y\n(Product Set)</text><text x=\"66\" y=\"102\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Independent OK</text><polygon points=\"140,90 210,90 210,25\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"185\" y=\"70\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Coupled Support\n0 \u2264 y \u2264 x \u2264 1</text><text x=\"175\" y=\"102\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Coupled \u21d2 Dependent!</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Independence REQUIRES: (1) density factorizes f(x, y)=g(x)h(y) AND (2) support is a product set</text></svg>",
    "drawingCaption": "Independence requires both algebraic density factorization and an uncoupled Cartesian product support",
    "coreTranslation": [
      "<strong>Definition:</strong> $X \\perp Y \\iff F_{X,Y}(x, y) = F_X(x) F_Y(y)$ for all $x, y$, equivalent to $f_{X,Y}(x, y) = f_X(x) f_Y(y)$ almost everywhere.",
      "<strong>Product Support Requirement:</strong> Independence strictly REQUIRES the support $\\operatorname{supp}(X, Y)$ to be a Cartesian product set $S_X \\times S_Y$ (e.g. a rectangle).",
      "<strong>Factorization Test:</strong> If $f_{X,Y}(x, y) = g(x) h(y)$ AND the support is a product set, then $X \\perp Y$, with marginals proportional to $g(x)$ and $h(y)$."
    ],
    "math": "$$X \\perp Y \\iff f_{X,Y}(x, y) = f_X(x) f_Y(y) \\quad \\forall (x, y) \\in S_X \\times S_Y$$",
    "personalConnection": "A standard chessboard: choosing a rank (1-8) and a file (A-H) are completely independent; on a triangular board, the choice of rank restricts available files.",
    "examTrap": "Declaring independence when f(x, y) = 4xy on coupled domain 0 \u2264 x \u2264 y \u2264 1! Even though the algebraic formula factorizes, coupled boundary limits destroy independence instantly."
  },
  {
    "id": 30706,
    "subject": "StoMA",
    "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
    "topicTitle": "07 \u00b7 Joint, Marginal & Conditional Distributions",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Triangular Support & Dependent Marginals",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30706\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30706)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30706)\"/><polygon points=\"40,114 180,114 180,25\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"40\" y1=\"114\" x2=\"180\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"2 2\"/><text x=\"110\" y=\"60\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">y = x</text><text x=\"180\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"40\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><text x=\"24\" y=\"25\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"130\" y=\"85\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_{X,Y} = 2</text><rect x=\"24\" y=\"20\" width=\"100\" height=\"48\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"74.0\" y=\"43.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_X(x) = 2x, x\u2208[0,1]\nf_Y(y) = 2(1-y),</text><text x=\"74.0\" y=\"51.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y\u2208[0,1]\nf_{Y|X}(y|x) = 1/x\n\u21d2 Y|X ~ Unif[0, x]</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f_{X,Y} \u2260 f_X f_Y \u21d2 strongly dependent; conditional expectation E[Y|X=x] = x/2</text></svg>",
    "drawingCaption": "Uniform density on a triangle produces non-uniform marginals and conditional uniform distributions",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Uniform density on triangle $T = \\{(x, y) : 0 \\le y \\le x \\le 1\\}$. Area is $1/2$, so $f_{X,Y}(x, y) = 2 \\cdot \\mathbf{1}_{\\{0 \\le y \\le x \\le 1\\}}$.",
      "<strong>Marginal Integrals:</strong> $f_X(x) = \\int_0^x 2\\,dy = 2x$ on $[0, 1]$. $f_Y(y) = \\int_y^1 2\\,dx = 2(1 - y)$ on $[0, 1]$. Product $f_X f_Y = 4x(1-y) \\ne 2 \\implies X \\not\\perp Y$.",
      "<strong>Conditional Uniformity:</strong> $f_{Y \\mid X}(y \\mid x) = \\frac{2}{2x} = \\frac{1}{x} \\mathbf{1}_{\\{0 \\le y \\le x\\}}$, so $Y \\mid X=x \\sim \\text{Uniform}[0, x]$ with $\\mathbb{E}[Y \\mid X=x] = x/2$."
    ],
    "math": "$$f_{X,Y} = 2, \\quad f_X(x) = 2x, \\quad f_Y(y) = 2(1-y); \\quad f_{Y \\mid X}(y \\mid x) = \\frac{1}{x}\\,\\mathbf{1}_{\\{0 \\le y \\le x\\}}$$",
    "personalConnection": "Breaking a stick at point X, then picking a point Y uniformly on the broken piece: Y is bounded by X and cannot be independent of X.",
    "examTrap": "Integrating y from 0 to 1 when finding f_X(x)! Because y \u2264 x, integrating past x includes forbidden empty territory, producing an erroneous constant marginal."
  },
  {
    "id": 30801,
    "subject": "StoMA",
    "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
    "topicTitle": "08 \u00b7 Multiple RVs & Order Statistics",
    "cardNumber": "01",
    "category": "EXTREME VALUES",
    "highlighterClass": "highlight-cyan",
    "title": "Order Statistics & Extremes: Sample Minimum and Maximum",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30801\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"72\" x2=\"220\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.8\"/><circle cx=\"40\" cy=\"72\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"40\" y=\"60\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X_{(1)}</text><text x=\"40\" y=\"86\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Min</text><circle cx=\"80\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"80\" y=\"60\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X_{(2)}</text><circle cx=\"120\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"60\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">...</text><circle cx=\"160\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"160\" y=\"60\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X_{(n-1)}</text><circle cx=\"200\" cy=\"72\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"60\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X_{(n)}</text><text x=\"200\" y=\"86\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Max</text><rect x=\"20\" y=\"18\" width=\"96\" height=\"32\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"68.0\" y=\"33.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Max: P(X_{(n)}</text><text x=\"68.0\" y=\"42.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2264 x)\n= [F(x)]^n</text><rect x=\"124\" y=\"18\" width=\"96\" height=\"32\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"172.0\" y=\"33.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Min: P(X_{(1)} ></text><text x=\"172.0\" y=\"42.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">x)\n= [1 - F(x)]^n</text><text x=\"120\" y=\"114\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_{X_{(n)}}(x) = n [F(x)]^{n-1} f(x),   f_{X_{(1)}}(x) = n [1 - F(x)]^{n-1} f(x)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Sample extremes: Max requires all X\u1d62 \u2264 x; Min requires all X\u1d62 > x</text></svg>",
    "drawingCaption": "The sample maximum requires every item to be below x; the sample minimum requires every item to exceed x",
    "coreTranslation": [
      "<strong>Ascending Sort:</strong> For i.i.d. $X_1, \\dots, X_n \\sim F$, sorting in ascending order yields order statistics $X_{(1)} \\le X_{(2)} \\le \\dots \\le X_{(n)}$.",
      "<strong>Sample Maximum:</strong> $X_{(n)} \\le x \\iff$ every $X_i \\le x$. By independence, $F_{X_{(n)}}(x) = [F(x)]^n$, so $f_{X_{(n)}}(x) = n [F(x)]^{n-1} f(x)$.",
      "<strong>Sample Minimum:</strong> $X_{(1)} > x \\iff$ every $X_i > x$. Thus $\\mathbb{P}(X_{(1)} > x) = [1 - F(x)]^n$, giving $F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n$."
    ],
    "math": "$$F_{X_{(n)}}(x) = [F(x)]^n, \\qquad F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n, \\qquad f_{X_{(1)}}(x) = n[1-F(x)]^{n-1} f(x)$$",
    "personalConnection": "Weakest link of a chain: the entire chain snaps as soon as its weakest link fails (minimum X_{(1)}); a flood wall fails when the highest wave tops it (maximum X_{(n)}).",
    "examTrap": "Differentiating 1 - [1 - F(x)]^n and losing the negative sign from the inner derivative! -n[1 - F(x)]^{n-1}(-f(x)) = +n[1 - F(x)]^{n-1}f(x)."
  },
  {
    "id": 30802,
    "subject": "StoMA",
    "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
    "topicTitle": "08 \u00b7 Multiple RVs & Order Statistics",
    "cardNumber": "02",
    "category": "ORDER DENSITIES",
    "highlighterClass": "highlight-amber",
    "title": "General Marginal Density of the k-th Order Statistic",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30802\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"72\" x2=\"220\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.8\"/><rect x=\"25\" y=\"45\" width=\"75\" height=\"54\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.1\" stroke-dasharray=\"2 2\"/><text x=\"62\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(k - 1) items</text><text x=\"62\" y=\"80\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">prob: [F(x)]^{k-1}</text><rect x=\"105\" y=\"40\" width=\"30\" height=\"64\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"58\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1 item</text><text x=\"120\" y=\"80\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f(x)dx</text><rect x=\"140\" y=\"45\" width=\"75\" height=\"54\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.1\" stroke-dasharray=\"2 2\"/><text x=\"177\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(n - k) items</text><text x=\"177\" y=\"80\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">prob: [1-F(x)]^{n-k}</text><text x=\"120\" y=\"25\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_{X_{(k)}}(x) = \\frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1-F(x)]^{n-k} f(x)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Multinomial placement: (k-1) to left, exactly 1 in [x, x+dx], and (n-k) to right</text></svg>",
    "drawingCaption": "Trisection of the real line into left tail, pivot element in [x, x+dx], and right tail via multinomial counting",
    "coreTranslation": [
      "<strong>Trisection Probability:</strong> Probability that 1 item lies in $[x, x+dx]$ is $f(x)dx$, $(k-1)$ items lie in $(-\\infty, x)$ with probability $F(x)$, and $(n-k)$ items lie in $(x, \\infty)$ with probability $1 - F(x)$.",
      "<strong>Combinatorial Multiplicity:</strong> There are $\\frac{n!}{(k-1)! 1! (n-k)!} = k \\binom{n}{k}$ distinct assignments of the $n$ samples to these three zones.",
      "<strong>General Marginal PDF:</strong> $f_{X_{(k)}}(x) = \\frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)$."
    ],
    "math": "$$f_{X_{(k)}}(x) = \\frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x) = k \\binom{n}{k} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)$$",
    "personalConnection": "Median score on an entrance exam: (k-1) students score below, exactly 1 student sits at the pivot cut-off, and (n-k) students score above.",
    "examTrap": "Forgetting the trailing density factor f(x)! Without f(x), the expression is a discrete binomial probability mass, NOT a continuous probability density function."
  },
  {
    "id": 30803,
    "subject": "StoMA",
    "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
    "topicTitle": "08 \u00b7 Multiple RVs & Order Statistics",
    "cardNumber": "03",
    "category": "JOINT ORDER STATS",
    "highlighterClass": "highlight-emerald",
    "title": "Joint Density of All n Order Statistics & The n! Permutation",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30803\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30803)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30803)\"/><line x1=\"40\" y1=\"114\" x2=\"180\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3 3\"/><text x=\"165\" y=\"25\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2081 = x\u2082</text><polygon points=\"40,114 180,114 180,25\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"130\" y=\"85\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Ordered Cone:\nx\u2081 &lt; x\u2082 &lt; ... &lt; x_n</text><rect x=\"24\" y=\"20\" width=\"100\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"74.0\" y=\"41.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Joint Density:\nn! \u220f</text><text x=\"74.0\" y=\"50.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f(x\u1d62)\non x\u2081 &lt; x\u2082 &lt; ... &lt; x_n</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Sorting folds all n! sample permutations into a single ordered cone; density scales by n!</text></svg>",
    "drawingCaption": "Sorting folds the n-dimensional hypercube into a single ordered simplex cone, multiplying density by n!",
    "coreTranslation": [
      "<strong>Joint Density Formula:</strong> $f_{X_{(1)}, \\dots, X_{(n)}}(x_1, \\dots, x_n) = n! \\prod_{i=1}^n f(x_i) \\cdot \\mathbf{1}_{\\{x_1 < x_2 < \\dots < x_n\\}}$.",
      "<strong>Origin of $n!$:</strong> There are $n!$ distinct permutations of the original unordered vector $(X_1, \\dots, X_n)$ that sort into the identical ordered list $(x_1, \\dots, x_n)$.",
      "<strong>Induced Dependence:</strong> Even though raw samples $X_i$ are independent, order statistics $X_{(1)}, \\dots, X_{(n)}$ are STRONGLY DEPENDENT through the ordering constraints $X_{(1)} < \\dots < X_{(n)}$."
    ],
    "math": "$$f_{X_{(1)},\\dots,X_{(n)}}(x_1, \\dots, x_n) = n! \\prod_{i=1}^n f(x_i) \\cdot \\mathbf{1}_{\\{x_1 < x_2 < \\dots < x_n\\}}$$",
    "personalConnection": "Folding a paper fan: folding an n-dimensional sheet along all diagonals collapses n! identical symmetric wedges into one single compact ordered cone of volume 1/n!.",
    "examTrap": "Omitting the factor n! in joint calculations. Without n!, integrating over the ordered domain x\u2081 < ... < x_n yields 1/n! instead of the required probability 1."
  },
  {
    "id": 30804,
    "subject": "StoMA",
    "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
    "topicTitle": "08 \u00b7 Multiple RVs & Order Statistics",
    "cardNumber": "04",
    "category": "UNIFORM ORDER",
    "highlighterClass": "highlight-purple",
    "title": "Uniform Order Statistics & The Beta Distribution",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30804\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"72\" x2=\"220\" y2=\"72\" stroke=\"#000000\" stroke-width=\"2.0\"/><circle cx=\"20\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"20\" y=\"86\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><circle cx=\"220\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"220\" y=\"86\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><circle cx=\"60\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"60\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">U_{(1)}</text><circle cx=\"110\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"110\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">U_{(k)}</text><circle cx=\"170\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"170\" y=\"60\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">U_{(n)}</text><text x=\"110\" y=\"88\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[U_{(k)}] = k / (n + 1)</text><rect x=\"20\" y=\"20\" width=\"200\" height=\"26\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"36.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">U_{(k)} ~ Beta(k, n - k + 1)   on [0, 1]</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">n uniform points divide [0, 1] into (n+1) equal-mean spacings of length 1/(n+1)</text></svg>",
    "drawingCaption": "Order statistics of Uniform(0, 1) follow exact Beta distributions; expected spacing between all points is 1/(n+1)",
    "coreTranslation": [
      "<strong>Beta Distribution Law:</strong> For $U_1, \\dots, U_n \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Uniform}(0, 1)$, $f_{U_{(k)}}(u) = \\frac{n!}{(k-1)!(n-k)!} u^{k-1} (1-u)^{n-k} \\sim \\text{Beta}(k, n - k + 1)$.",
      "<strong>Expected Position:</strong> $\\mathbb{E}[U_{(k)}] = \\frac{k}{n+1}$, and variance $\\operatorname{Var}(U_{(k)}) = \\frac{k(n - k + 1)}{(n+1)^2(n+2)}$.",
      "<strong>Equal Mean Spacings:</strong> The $n$ order statistics partition $[0, 1]$ into $(n+1)$ sub-intervals (spacings) whose expected lengths are all IDENTICAL: $\\mathbb{E}[D_i] = \\frac{1}{n+1}$."
    ],
    "math": "$$U_{(k)} \\sim \\text{Beta}(k, n - k + 1), \\qquad \\mathbb{E}[U_{(k)}] = \\frac{k}{n+1}, \\qquad \\operatorname{Var}(U_{(k)}) = \\frac{k(n - k + 1)}{(n+1)^2(n+2)}$$",
    "personalConnection": "Dropping n random markers along a 1 km running track: on average, the markers cut the track into (n+1) segments of exactly equal length 1/(n+1) km.",
    "examTrap": "Believing edge spacings 0 to U_{(1)} and U_{(n)} to 1 behave differently from interior spacings. All (n+1) spacings are identically distributed with expected length 1/(n+1)."
  },
  {
    "id": 30805,
    "subject": "StoMA",
    "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
    "topicTitle": "08 \u00b7 Multiple RVs & Order Statistics",
    "cardNumber": "05",
    "category": "EXPONENTIAL ORDER",
    "highlighterClass": "highlight-cyan",
    "title": "Exponential Order Statistics & Independent Spacings",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30805\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"72\" x2=\"220\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.8\"/><circle cx=\"20\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"20\" y=\"86\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><circle cx=\"70\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"70\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X_{(1)}</text><circle cx=\"130\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"130\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X_{(2)}</text><circle cx=\"200\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X_{(3)}</text><line x1=\"20\" y1=\"88\" x2=\"70\" y2=\"88\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"45\" y=\"100\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W\u2081 ~ Exp(3\u03bb)</text><line x1=\"70\" y1=\"88\" x2=\"130\" y2=\"88\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"100\" y=\"100\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W\u2082 ~ Exp(2\u03bb)</text><line x1=\"130\" y1=\"88\" x2=\"200\" y2=\"88\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"165\" y=\"100\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W\u2083 ~ Exp(\u03bb)</text><rect x=\"20\" y=\"18\" width=\"200\" height=\"26\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"30.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Spacings W_k = X_{(k)} - X_{(k-1)}</text><text x=\"120.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">~ Exp((n - k + 1)\u03bb) are INDEPENDENT</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Maximum mean: E[X_{(n)}] = (1/\u03bb) \u2211_{j=1}^n (1/j) \u2248 (log n + \u03b3) / \u03bb</text></svg>",
    "drawingCaption": "Exponential order statistics decompose into mutually independent exponential spacings with accelerating rates",
    "coreTranslation": [
      "<strong>Exponential Setup:</strong> Let $X_1, \\dots, X_n \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Exp}(\\lambda)$.",
      "<strong>Independent Spacings:</strong> The spacings $W_k = X_{(k)} - X_{(k-1)}$ (with $X_{(0)} = 0$) are MUTUALLY INDEPENDENT Exponential RVs with parameter $(n - k + 1)\\lambda$.",
      "<strong>Harmonic Mean Sum:</strong> $\\mathbb{E}[X_{(k)}] = \\frac{1}{\\lambda} \\sum_{j=1}^k \\frac{1}{n - j + 1}$. The maximum has expected value $\\mathbb{E}[X_{(n)}] = \\frac{1}{\\lambda} \\sum_{j=1}^n \\frac{1}{j} \\approx \\frac{\\ln n + \\gamma}{\\lambda}$."
    ],
    "math": "$$W_k = X_{(k)} - X_{(k-1)} \\sim \\text{Exp}((n - k + 1)\\lambda) \\text{ independent}; \\quad \\mathbb{E}[X_{(n)}] = \\frac{1}{\\lambda} \\sum_{j=1}^n \\frac{1}{j}$$",
    "personalConnection": "Lightbulb array: all n bulbs race to burn out first at collective rate n\u03bb; once one burns out, remaining (n-1) race at rate (n-1)\u03bb, down to the final survivor.",
    "examTrap": "Applying independent spacings to non-exponential variables! The independent spacings property is a UNIQUE signature of the memoryless exponential distribution."
  },
  {
    "id": 30806,
    "subject": "StoMA",
    "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
    "topicTitle": "08 \u00b7 Multiple RVs & Order Statistics",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: System Reliability via Minimum of Exponentials",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30806\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"72\" x2=\"45\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"45\" y=\"58\" width=\"40\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"65.0\" y=\"75.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">T\u2081~Exp(\u03bb\u2081)</text><line x1=\"85\" y1=\"72\" x2=\"105\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"105\" y=\"58\" width=\"40\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"125.0\" y=\"75.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">T\u2082~Exp(\u03bb\u2082)</text><line x1=\"145\" y1=\"72\" x2=\"165\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"165\" y=\"58\" width=\"40\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"185.0\" y=\"75.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">T_n~Exp(\u03bb_n)</text><line x1=\"205\" y1=\"72\" x2=\"225\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"20\" y=\"18\" width=\"200\" height=\"28\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"31.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">T_{sys} = min(T\u2081, ..., T_n) ~</text><text x=\"120.0\" y=\"40.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Exp(\u2211 \u03bb\u1d62),   E[T_{sys}] = 1 / \u2211 \u03bb\u1d62</text><text x=\"120\" y=\"114\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(Component k fails first) = \u03bb_k / \u2211 \u03bb\u1d62</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Series reliability: multiply survival functions P(T\u1d62 > t) = exp(-\u03bb\u1d62 t); rates sum linearly</text></svg>",
    "drawingCaption": "The minimum of independent exponentials is exponential with sum of rates; failure identity is proportional to rate",
    "coreTranslation": [
      "<strong>Series Setup:</strong> System of $n$ components in series with independent lifetimes $T_i \\sim \\text{Exp}(\\lambda_i)$. System fails at $T_{\\text{sys}} = \\min(T_1, \\dots, T_n)$.",
      "<strong>Survival Product:</strong> $\\mathbb{P}(T_{\\text{sys}} > t) = \\prod_{i=1}^n \\mathbb{P}(T_i > t) = \\prod_{i=1}^n e^{-\\lambda_i t} = \\exp(-(\\sum_{i=1}^n \\lambda_i) t)$.",
      "<strong>Failure Probability:</strong> The system lifetime is strictly $\\text{Exp}(\\sum_{i=1}^n \\lambda_i)$, and component $k$ is the one that causes system failure with probability $\\frac{\\lambda_k}{\\sum_{i=1}^n \\lambda_i}$."
    ],
    "math": "$$T_{\\text{sys}} = \\min_{1 \\le i \\le n} T_i \\sim \\text{Exp}\\left(\\sum_{i=1}^n \\lambda_i\\right), \\qquad \\mathbb{P}(T_k = \\min T_i) = \\frac{\\lambda_k}{\\sum_{i=1}^n \\lambda_i}$$",
    "personalConnection": "A sprint race among n runners: the winning time is distributed as the minimum, and each runner's chance of winning is directly proportional to their running speed \u03bb_k.",
    "examTrap": "Attempting convolution integration to find the minimum of lifetimes! Always compute minimums via the product of survival functions P(T_i > t)\u2014convolution is for SUMS, not minimums."
  },
  {
    "id": 30901,
    "subject": "StoMA",
    "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
    "topicTitle": "09 \u00b7 Sums & Jacobian Transformations",
    "cardNumber": "01",
    "category": "CONVOLUTION",
    "highlighterClass": "highlight-cyan",
    "title": "The Convolution Formula for Sums of Independent RVs",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30901\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30901)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30901)\"/><line x1=\"40\" y1=\"114\" x2=\"160\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"145\" y=\"25\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">x + y = z</text><circle cx=\"100\" cy=\"70\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"125\" y=\"70\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(x, z - x)</text><line x1=\"100\" y1=\"70\" x2=\"100\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"100\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x</text><rect x=\"24\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"72.0\" y=\"37.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Continuous:\nf_Z(z) =</text><text x=\"72.0\" y=\"45.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u222b f_X(x) f_Y(z-x) dx</text><rect x=\"128\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"176.0\" y=\"37.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Discrete:\nP(Z=k) =</text><text x=\"176.0\" y=\"45.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2211 P(X=j) P(Y=k-j)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Convolution integrates joint mass along the diagonal line x + y = z</text></svg>",
    "drawingCaption": "The density of Z = X + Y integrates joint density along the diagonal slice x + y = z",
    "coreTranslation": [
      "<strong>Continuous Convolution:</strong> For independent $X \\perp Y$, the density of $Z = X + Y$ is $(f_X * f_Y)(z) = \\int_{-\\infty}^\\infty f_X(x) f_Y(z - x)\\,dx$.",
      "<strong>Discrete Convolution:</strong> For independent integer RVs, $\\mathbb{P}(Z = k) = \\sum_{j=-\\infty}^\\infty \\mathbb{P}(X = j)\\,\\mathbb{P}(Y = k - j)$.",
      "<strong>Algebraic Properties:</strong> Convolution is commutative ($f_X * f_Y = f_Y * f_X$) and associative ($(f_X * f_Y) * f_W = f_X * (f_Y * f_W)$)."
    ],
    "math": "$$f_{X+Y}(z) = (f_X * f_Y)(z) = \\int_{-\\infty}^\\infty f_X(x) f_Y(z - x)\\,dx = \\int_{-\\infty}^\\infty f_X(z - y) f_Y(y)\\,dy$$",
    "personalConnection": "Sliding an audio filter across an audio signal: reversing one signal in time (z - x) and integrating total overlap energy at time delay z.",
    "examTrap": "Neglecting to adjust integration limits for non-negative variables! If X, Y \u2265 0, then 0 \u2264 x \u2264 z; integrating from -\u221e to \u221e without truncating limits produces severe calculation errors."
  },
  {
    "id": 30902,
    "subject": "StoMA",
    "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
    "topicTitle": "09 \u00b7 Sums & Jacobian Transformations",
    "cardNumber": "02",
    "category": "2D JACOBIAN",
    "highlighterClass": "highlight-amber",
    "title": "2D Multivariate Jacobian Transformation Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30902\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"30,90 70,80 80,105 40,115\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"55\" y=\"98\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">dx dy</text><line x1=\"85\" y1=\"95\" x2=\"125\" y2=\"95\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30902)\"/><text x=\"105\" y=\"85\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g(X, Y)</text><polygon points=\"140,85 195,70 210,110 155,125\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"175\" y=\"98\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">du dv = |J| dx dy</text><rect x=\"24\" y=\"20\" width=\"192\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">J(u, v) = det [ \u2202x/\u2202u  \u2202x/\u2202v ;  \u2202y/\u2202u  \u2202y/\u2202v</text><text x=\"120.0\" y=\"49.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">]\nf_{U,V}(u, v) = f_{X,Y}(x(u, v), y(u, v)) \u00b7 |J(u, v)|</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">The Jacobian determinant scales differential area: |J(u, v)| = 1 / |J(x, y)|</text></svg>",
    "drawingCaption": "Multivariate 2D mappings scale local area elements by the absolute determinant of the coordinate Jacobian",
    "coreTranslation": [
      "<strong>Bijective Smooth Mapping:</strong> Let $(U, V) = g(X, Y)$ be an invertible, continuously differentiable mapping from $S \\subset \\mathbb{R}^2$ to $T \\subset \\mathbb{R}^2$.",
      "<strong>Jacobian Determinant:</strong> $J(u, v) \\triangleq \\det \\begin{bmatrix} \\partial x/\\partial u & \\partial x/\\partial v \\\\ \\partial y/\\partial u & \\partial y/\\partial v \\end{bmatrix}$. Reciprocal identity: $J(u, v) = [J(x, y)]^{-1}$.",
      "<strong>Transformed Density:</strong> $f_{U,V}(u, v) = f_{X,Y}(x(u, v), y(u, v)) |J(u, v)| \\cdot \\mathbf{1}_{\\{(u, v) \\in T\\}}$."
    ],
    "math": "$$f_{U,V}(u, v) = f_{X,Y}\\left(x(u, v), y(u, v)\\right) \\left| \\det \\frac{\\partial(x, y)}{\\partial(u, v)} \\right|$$",
    "personalConnection": "Mercator map projection: flattening spherical latitude and longitude onto a flat map distorts area sizes by the local metric Jacobian determinant.",
    "examTrap": "Inverting forward vs inverse Jacobian! If you calculate the forward derivative matrix \u2202(u,v)/\u2202(x,y), you must DIVIDE by its determinant rather than multiply."
  },
  {
    "id": 30903,
    "subject": "StoMA",
    "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
    "topicTitle": "09 \u00b7 Sums & Jacobian Transformations",
    "cardNumber": "03",
    "category": "RATIO & POLAR",
    "highlighterClass": "highlight-emerald",
    "title": "Ratio Distribution & Polar Coordinate Transformations",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30903\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"70\" cy=\"72\" rx=\"40\" ry=\"40\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(0 70 72)\"/><line x1=\"30\" y1=\"72\" x2=\"110\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30903)\"/><line x1=\"30\" y1=\"72\" x2=\"30\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30903)\"/><line x1=\"70\" y1=\"72\" x2=\"100\" y2=\"45\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"88\" y=\"54\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">r</text><text x=\"78\" y=\"68\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b8</text><text x=\"70\" y=\"126\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dx dy = r dr d\u03b8</text><rect x=\"125\" y=\"30\" width=\"100\" height=\"50\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"175.0\" y=\"54.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Ratio Z = Y / X:\nf_Z(z) = \u222b |x| f_{X,Y}(x,</text><text x=\"175.0\" y=\"62.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">xz) dx\n(Cauchy if X, Y ~ N(0, 1))</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Polar Jacobian is r; Ratio transformation integrates along radial rays y = xz with factor |x|</text></svg>",
    "drawingCaption": "Polar coordinates introduce metric area factor r; ratio distributions integrate radial rays with factor |x|",
    "coreTranslation": [
      "<strong>Ratio Formula:</strong> For $Z = Y / X$, introduce auxiliary $W = X$. Inverse is $x = w, y = wz$ with Jacobian $|J| = |w|$, yielding $f_Z(z) = \\int_{-\\infty}^\\infty |x| f_{X,Y}(x, xz)\\,dx$.",
      "<strong>Polar Coordinates:</strong> $(X, Y) = (R \\cos\\Theta, R \\sin\\Theta)$. The Jacobian determinant is $\\det \\begin{bmatrix} \\cos\\theta & -r\\sin\\theta \\\\ \\sin\\theta & r\\cos\\theta \\end{bmatrix} = r$.",
      "<strong>Polar Density:</strong> $f_{R,\\Theta}(r, \\theta) = r f_{X,Y}(r \\cos\\theta, r \\sin\\theta)$ for $r \\ge 0, \\theta \\in [0, 2\\pi)$."
    ],
    "math": "$$Z = \\frac{Y}{X} \\implies f_Z(z) = \\int_{-\\infty}^\\infty |x|\\,f_{X,Y}(x, xz)\\,dx, \\qquad f_{R,\\Theta}(r, \\theta) = r\\,f_{X,Y}(r\\cos\\theta, r\\sin\\theta)$$",
    "personalConnection": "Marine sonar sweep: scanning targets in range r and angle \u03b8; rings expand in area as 2\u03c0 r dr, introducing the linear geometric weighting factor r.",
    "examTrap": "Forgetting the absolute value factor |x| in the ratio formula! Neglecting |x| violates physical dimensions (density must have units 1/z) and gives wrong integrals."
  },
  {
    "id": 30904,
    "subject": "StoMA",
    "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
    "topicTitle": "09 \u00b7 Sums & Jacobian Transformations",
    "cardNumber": "04",
    "category": "BOX-MULLER",
    "highlighterClass": "highlight-purple",
    "title": "The Box-Muller Transform: Exact Gaussian Simulation",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30904\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"64.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">U\u2081, U\u2082 ~ i.i.d. Unif(0,</text><text x=\"64.0\" y=\"46.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1)\n(Standard uniform)</text><line x1=\"112\" y1=\"38\" x2=\"136\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-30904)\"/><rect x=\"136\" y=\"20\" width=\"88\" height=\"36\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"180.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Z\u2081, Z\u2082 ~ i.i.d. N(0,</text><text x=\"180.0\" y=\"46.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1)\n(Standard normal)</text><rect x=\"16\" y=\"68\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"82\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Z\u2081 = \u221a(-2 ln U\u2081) \u00b7 cos(2\u03c0 U\u2082)</text><text x=\"120\" y=\"98\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Z\u2082 = \u221a(-2 ln U\u2081) \u00b7 sin(2\u03c0 U\u2082)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Radius R\u00b2 = -2 ln U\u2081 ~ Exp(1/2) \u2261 \u03c7\u2082\u00b2; Angle \u0398 = 2\u03c0 U\u2082 ~ Unif(0, 2\u03c0)</text></svg>",
    "drawingCaption": "Converts two independent Uniform(0, 1) variates into two independent standard Gaussian variates in closed form",
    "coreTranslation": [
      "<strong>Motivation:</strong> Gaussian quantile function $\\Phi^{-1}(u)$ has no closed form. Box-Muller bypasses 1D intractability by operating in 2D polar coordinates.",
      "<strong>Construction:</strong> For $U_1, U_2 \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Uniform}(0, 1)$, set radius $R = \\sqrt{-2\\ln U_1}$ (so $R^2 \\sim \\text{Exp}(1/2) \\equiv \\chi_2^2$) and angle $\\Theta = 2\\pi U_2 \\sim \\text{Uniform}(0, 2\\pi)$.",
      "<strong>Exact Normals:</strong> $Z_1 = R \\cos\\Theta$ and $Z_2 = R \\sin\\Theta$ are EXACTLY independent standard normal random variables: $Z_1, Z_2 \\stackrel{\\text{i.i.d.}}{\\sim} \\mathcal{N}(0, 1)$."
    ],
    "math": "$$Z_1 = \\sqrt{-2\\ln U_1}\\cos(2\\pi U_2), \\quad Z_2 = \\sqrt{-2\\ln U_1}\\sin(2\\pi U_2) \\implies Z_1, Z_2 \\stackrel{\\text{i.i.d.}}{\\sim} \\mathcal{N}(0, 1)$$",
    "personalConnection": "Dartboard simulation: choosing a radial distance from center according to a Rayleigh law and a completely random 360\u00b0 angle creates a 2D circularly symmetric Gaussian cloud.",
    "examTrap": "Generating standard normals one at a time and discarding Z\u2082! Box-Muller generates TWO independent normal values per pair of uniforms; saving both doubles computational efficiency."
  },
  {
    "id": 30905,
    "subject": "StoMA",
    "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
    "topicTitle": "09 \u00b7 Sums & Jacobian Transformations",
    "cardNumber": "05",
    "category": "CONVOLUTION STABILITY",
    "highlighterClass": "highlight-cyan",
    "title": "Sum Invariants: Stability of Normal, Poisson & Gamma",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30905\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"208\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"33.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Normals: N(\u03bc\u2081, \u03c3\u2081\u00b2) + N(\u03bc\u2082,</text><text x=\"120.0\" y=\"42.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c3\u2082\u00b2) = N(\u03bc\u2081 + \u03bc\u2082, \u03c3\u2081\u00b2 + \u03c3\u2082\u00b2)</text><rect x=\"16\" y=\"56\" width=\"208\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"73.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Poisson: Pois(\u03bb\u2081) + Pois(\u03bb\u2082) = Pois(\u03bb\u2081 + \u03bb\u2082)</text><rect x=\"16\" y=\"92\" width=\"208\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"105.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Gamma: Gamma(\u03b1\u2081, \u03b2) + Gamma(\u03b1\u2082,</text><text x=\"120.0\" y=\"114.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b2) = Gamma(\u03b1\u2081 + \u03b1\u2082, \u03b2)  [Same \u03b2!]</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Independent sum closures: Gaussians, Poissons, and shared-scale Gammas are closed under addition</text></svg>",
    "drawingCaption": "Independent sums of Gaussians are Gaussian, sums of Poissons are Poisson, and sums of Gammas are Gamma",
    "coreTranslation": [
      "<strong>Gaussian Closure:</strong> If $X_i \\sim \\mathcal{N}(\\mu_i, \\sigma_i^2)$ are independent, $\\sum_{i=1}^n X_i \\sim \\mathcal{N}(\\sum \\mu_i, \\sum \\sigma_i^2)$.",
      "<strong>Poisson Closure:</strong> If $X_i \\sim \\text{Poisson}(\\lambda_i)$ are independent, $\\sum_{i=1}^n X_i \\sim \\text{Poisson}(\\sum \\lambda_i)$.",
      "<strong>Gamma Closure (Shared Rate):</strong> If $X_i \\sim \\text{Gamma}(\\alpha_i, \\beta)$ are independent with IDENTICAL scale $\\beta$, then $\\sum_{i=1}^n X_i \\sim \\text{Gamma}(\\sum \\alpha_i, \\beta)$."
    ],
    "math": "$$\\sum_{i=1}^n \\mathcal{N}(\\mu_i, \\sigma_i^2) = \\mathcal{N}\\left(\\sum \\mu_i, \\sum \\sigma_i^2\\right), \\quad \\sum_{i=1}^n \\text{Pois}(\\lambda_i) = \\text{Pois}\\left(\\sum \\lambda_i\\right)$$",
    "personalConnection": "Combining incoming service calls: two independent streams of Poisson calls with rates \u03bb\u2081 and \u03bb\u2082 merge into a single stream of Poisson calls with rate \u03bb\u2081 + \u03bb\u2082.",
    "examTrap": "Adding Gamma random variables with different scale parameters \u03b2\u2081 \u2260 \u03b2\u2082! The sum of Gammas is Gamma ONLY when the rate/scale parameter is identical across all terms."
  },
  {
    "id": 30906,
    "subject": "StoMA",
    "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
    "topicTitle": "09 \u00b7 Sums & Jacobian Transformations",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Sum of Two Uniforms (The Triangle Law)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-30906\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30906)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-30906)\"/><path d=\"M 40,114 L 120,35 L 200,114\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"120\" y1=\"35\" x2=\"120\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"40\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><text x=\"120\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"200\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">2</text><text x=\"16\" y=\"35\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"70\" y=\"65\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_Z(z) = z</text><text x=\"170\" y=\"65\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_Z(z) = 2 - z</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Convolution of two independent Unif(0, 1) pulses creates a symmetric triangle distribution</text></svg>",
    "drawingCaption": "Convolving two rectangular uniform pulses generates a symmetric triangular probability density",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Let $X, Y \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Uniform}[0, 1]$. Compute the PDF of $Z = X + Y$.",
      "<strong>Convolution Integral:</strong> $f_Z(z) = \\int_0^1 \\mathbf{1}_{\\{0 \\le z - x \\le 1\\}}\\,dx = \\int_{\\max(0, z-1)}^{\\min(1, z)} 1\\,dx$.",
      "<strong>Piecewise Triangle:</strong> For $0 \\le z \\le 1$, $f_Z(z) = z$. For $1 < z \\le 2$, $f_Z(z) = 2 - z$. Mean is $\\mathbb{E}[Z] = 1$, variance $\\operatorname{Var}(Z) = 1/12 + 1/12 = 1/6$."
    ],
    "math": "$$f_{X+Y}(z) = \\begin{cases} z & 0 \\le z \\le 1 \\\\ 2 - z & 1 < z \\le 2 \\\\ 0 & \\text{otherwise} \\end{cases}, \\qquad \\mathbb{E}[Z] = 1, \\; \\operatorname{Var}(Z) = \\tfrac{1}{6}$$",
    "personalConnection": "Rolling two fair dice: the sum of two uniform outcomes forms a triangular frequency peak at 7, tapering linearly toward 2 and 12.",
    "examTrap": "Treating the convolution integral as a single algebraic formula over [0, 2]! The overlap geometry changes at z = 1, splitting the solution into two distinct linear regimes."
  },
  {
    "id": 31001,
    "subject": "StoMA",
    "topicId": "10_Exchangeable_Random_Variables",
    "topicTitle": "10 \u00b7 Exchangeable Random Variables",
    "cardNumber": "01",
    "category": "EXCHANGEABILITY",
    "highlighterClass": "highlight-cyan",
    "title": "Exchangeability: Permutation Invariance of Joint Law",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31001\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"85\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"58.5\" y=\"37.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(X\u2081, X\u2082, ...,</text><text x=\"58.5\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X_n)\nJoint Law P</text><line x1=\"101\" y1=\"38\" x2=\"139\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31001)\"/><text x=\"120\" y=\"28\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Permute \u03c0</text><rect x=\"139\" y=\"20\" width=\"85\" height=\"36\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"181.5\" y=\"37.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(X_{\u03c0(1)}, ...,</text><text x=\"181.5\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X_{\u03c0(n)})\nIdentical Law P</text><rect x=\"24\" y=\"70\" width=\"192\" height=\"46\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">i.i.d.  \u2282  Exchangeable  \u2282  Identically Distributed</text><text x=\"120\" y=\"102\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Order does not matter; variables are symmetric but CAN be dependent</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Exchangeability: Joint distribution is invariant under all permutations \u03c0 \u2208 S_n</text></svg>",
    "drawingCaption": "A sequence is exchangeable if its joint distribution is completely unchanged by any index permutation",
    "coreTranslation": [
      "<strong>Formal Definition:</strong> $(X_1, \\dots, X_n)$ is exchangeable if $(X_1, \\dots, X_n) \\stackrel{d}{=} (X_{\\pi(1)}, \\dots, X_{\\pi(n)})$ for every permutation $\\pi \\in S_n$.",
      "<strong>Hierarchy:</strong> $\\text{i.i.d.} \\subsetneq \\text{Exchangeable} \\subsetneq \\text{Identically Distributed}$. Exchangeability is strictly weaker than i.i.d. because mutual dependence is permitted.",
      "<strong>Equi-marginality:</strong> All $X_i$ share identical marginal distributions $F$, and all pairs $(X_i, X_j)$ share identical joint bivariate laws."
    ],
    "math": "$$(X_1, \\dots, X_n) \\stackrel{d}{=} (X_{\\pi(1)}, \\dots, X_{\\pi(n)}) \\quad \\forall \\pi \\in S_n; \\qquad \\text{i.i.d.} \\subset \\text{Exchangeable}$$",
    "personalConnection": "Dealing hands in poker: whether a royal card is dealt first, third, or fifth, the joint probability of the entire hand configuration remains identical.",
    "examTrap": "Confusing exchangeable with i.i.d.! Exchangeable variables can be strongly correlated (e.g. sampling without replacement from a finite urn)."
  },
  {
    "id": 31002,
    "subject": "StoMA",
    "topicId": "10_Exchangeable_Random_Variables",
    "topicTitle": "10 \u00b7 Exchangeable Random Variables",
    "cardNumber": "02",
    "category": "EQUI-CORRELATION",
    "highlighterClass": "highlight-amber",
    "title": "Equi-Marginality & Universal Pairwise Equi-Correlation",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31002\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"30\" y=\"20\" width=\"180\" height=\"85\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"61.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03a3 =\n[ \u03c3\u00b2    \u03c1\u03c3\u00b2  ...  \u03c1\u03c3\u00b2 ]\n[ \u03c1\u03c3\u00b2   \u03c3\u00b2   ...  \u03c1\u03c3\u00b2</text><text x=\"120.0\" y=\"71.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">]\n[ ...   ...  ...  ... ]\n[ \u03c1\u03c3\u00b2   \u03c1\u03c3\u00b2  ...  \u03c3\u00b2  ]</text><text x=\"120\" y=\"118\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var(X\u1d62) = \u03c3\u00b2   and   Corr(X\u1d62, X_j) = \u03c1  for all i \u2260 j</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Symmetry forces all variances to be equal and all pairwise covariances to be identical</text></svg>",
    "drawingCaption": "Exchangeability imposes compound symmetry: all variances are identical and all pairwise correlations match",
    "coreTranslation": [
      "<strong>Marginal Identity:</strong> By taking $\\pi$ swapping $1$ and $i$, $\\mathbb{P}(X_1 \\le x) = \\mathbb{P}(X_i \\le x)$ for all $i$. All variables have identical mean $\\mu$ and variance $\\sigma^2$.",
      "<strong>Pairwise Equi-Correlation:</strong> By swapping pairs $(1, 2) \\leftrightarrow (i, j)$, $\\operatorname{Cov}(X_i, X_j) = \\operatorname{Cov}(X_1, X_2) \\triangleq c$ for all $i \\ne j$.",
      "<strong>Compound Symmetry Matrix:</strong> The covariance matrix is $\\Sigma = \\sigma^2 [(1 - \\rho) I_n + \\rho \\mathbf{1}\\mathbf{1}^\\top]$, completely parameterized by just two numbers: $\\sigma^2$ and $\\rho$."
    ],
    "math": "$$\\operatorname{Var}(X_i) = \\sigma^2, \\quad \\operatorname{Cov}(X_i, X_j) = \\rho\\sigma^2 \\quad \\forall i \\ne j \\implies \\Sigma = \\sigma^2 \\left[(1-\\rho)I + \\rho \\mathbf{1}\\mathbf{1}^\\top\\right]$$",
    "personalConnection": "A round discussion table of identical twins: each has the exact same baseline reaction and shares the exact same mutual affinity with every other sibling.",
    "examTrap": "Assuming pairwise covariances can vary across indices. In an exchangeable sequence, Cov(X\u2081, X\u2082) MUST equal Cov(X\u2087, X\u2089)\u2014any discrepancy disproves exchangeability."
  },
  {
    "id": 31003,
    "subject": "StoMA",
    "topicId": "10_Exchangeable_Random_Variables",
    "topicTitle": "10 \u00b7 Exchangeable Random Variables",
    "cardNumber": "03",
    "category": "FINITE CORRELATION",
    "highlighterClass": "highlight-emerald",
    "title": "Finite Exchangeability Correlation Bound: \u03c1 \u2265 -1/(n - 1)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31003\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31003)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31003)\"/><line x1=\"60\" y1=\"65\" x2=\"200\" y2=\"65\" stroke=\"#000000\" stroke-width=\"2.5\"/><circle cx=\"60\" cy=\"65\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"50\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">-1/(n - 1)</text><circle cx=\"200\" cy=\"65\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"50\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">+1</text><line x1=\"130\" y1=\"60\" x2=\"130\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"130\" y=\"80\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0 (i.i.d.)</text><rect x=\"24\" y=\"18\" width=\"192\" height=\"22\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"28.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var(\u2211 X\u1d62) = n \u03c3\u00b2 [1 + (n -</text><text x=\"120.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1) \u03c1] \u2265 0 \u21d2 \u03c1 \u2265 -1 / (n - 1)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Finite exchangeable variables can be negatively correlated down to -1/(n - 1)</text></svg>",
    "drawingCaption": "Variance non-negativity of the sum bounds negative correlation: \u03c1 \u2265 -1/(n - 1)",
    "coreTranslation": [
      "<strong>Sum Variance Expansion:</strong> For sum $S_n = \\sum_{i=1}^n X_i$, $\\operatorname{Var}(S_n) = \\sum \\operatorname{Var}(X_i) + \\sum_{i \\ne j} \\operatorname{Cov}(X_i, X_j) = n\\sigma^2 + n(n-1)\\rho\\sigma^2$.",
      "<strong>Positivity Constraint:</strong> Since $\\operatorname{Var}(S_n) \\ge 0$, we have $n\\sigma^2 [1 + (n-1)\\rho] \\ge 0 \\implies \\rho \\ge -\\frac{1}{n-1}$.",
      "<strong>Extreme Negative Attainment:</strong> Equality $\\rho = -\\frac{1}{n-1}$ is achieved when the sum is deterministic: $\\sum_{i=1}^n X_i = c$ almost surely."
    ],
    "math": "$$\\operatorname{Var}\\left(\\sum_{i=1}^n X_i\\right) \\ge 0 \\implies 1 + (n-1)\\rho \\ge 0 \\implies \\rho \\ge -\\frac{1}{n-1}$$",
    "personalConnection": "Cutting a fixed birthday cake among n guests: if guest 1 gets a larger slice, the other slices must collectively shrink, producing mutual negative correlation -1/(n-1).",
    "examTrap": "Believing correlation can never be negative in exchangeable systems. For finite n, negative correlation is completely valid down to the barrier -1/(n-1)."
  },
  {
    "id": 31004,
    "subject": "StoMA",
    "topicId": "10_Exchangeable_Random_Variables",
    "topicTitle": "10 \u00b7 Exchangeable Random Variables",
    "cardNumber": "04",
    "category": "INFINITE EXCHANGEABILITY",
    "highlighterClass": "highlight-purple",
    "title": "Infinite Exchangeability & Non-Negative Correlation",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31004\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"42\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Finite sequence: \u03c1 \u2265 -1 / (n - 1)\nTake n \u2192 \u221e (infinite</text><text x=\"120.0\" y=\"49.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">sequence):\n\u03c1 \u2265 lim_{n \u2192 \u221e} [-1 / (n - 1)] = 0</text><line x1=\"30\" y1=\"85\" x2=\"210\" y2=\"85\" stroke=\"#000000\" stroke-width=\"1.4\"/><line x1=\"100\" y1=\"85\" x2=\"200\" y2=\"85\" stroke=\"#000000\" stroke-width=\"2.5\"/><circle cx=\"100\" cy=\"85\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"100\" y=\"100\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><circle cx=\"200\" cy=\"85\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"100\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"150\" y=\"72\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Valid range for infinite exchangeability: \u03c1 \u2208 [0, 1]</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">An infinitely extendable exchangeable sequence CANNOT be negatively correlated!</text></svg>",
    "drawingCaption": "If an exchangeable sequence is infinitely extendable, its pairwise correlation must be non-negative: \u03c1 \u2265 0",
    "coreTranslation": [
      "<strong>Infinite Extension:</strong> Sequence $(X_1, X_2, \\dots)$ is infinitely exchangeable if every finite subvector $(X_1, \\dots, X_n)$ is exchangeable for all $n \\ge 2$.",
      "<strong>Vanishing Lower Bound:</strong> The bound $\\rho \\ge -\\frac{1}{n-1}$ must hold for arbitrarily large $n$. Taking $n \\to \\infty$ yields $\\rho \\ge 0$.",
      "<strong>Impossibility of Negative Correlation:</strong> You cannot have an infinite family of variables that are all mutually negatively correlated! Mutual conflict cannot scale to infinity."
    ],
    "math": "$$\\rho \\ge -\\frac{1}{n-1} \\quad \\forall n \\ge 2 \\implies \\rho \\ge \\lim_{n \\to \\infty} \\left(-\\frac{1}{n-1}\\right) = 0 \\implies \\rho \\ge 0$$",
    "personalConnection": "Musical harmony: you can tune 2 or 3 instruments to clash out of phase with each other, but you cannot have an infinite orchestra where every pair clashes negatively.",
    "examTrap": "Applying De Finetti or claiming \u03c1 \u2265 0 for a finite sequence! Sampling without replacement from an urn of N balls stops at N; its correlation -1/(N-1) CANNOT be extended to infinity."
  },
  {
    "id": 31005,
    "subject": "StoMA",
    "topicId": "10_Exchangeable_Random_Variables",
    "topicTitle": "10 \u00b7 Exchangeable Random Variables",
    "cardNumber": "05",
    "category": "DE FINETTI THEOREM",
    "highlighterClass": "highlight-cyan",
    "title": "De Finetti\u2019s Representation Theorem: Conditionally i.i.d. Mixtures",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31005\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"80\" y=\"18\" width=\"80\" height=\"28\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"31.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Latent Prior:</text><text x=\"120.0\" y=\"40.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u0398 ~ F(\u03b8)</text><line x1=\"120\" y1=\"46\" x2=\"120\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31005)\"/><text x=\"155\" y=\"58\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Condition on \u0398</text><rect x=\"24\" y=\"70\" width=\"192\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"86.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Given \u0398 = \u03b8:  X\u2081, X\u2082, ... are i.i.d. Bernoulli(\u03b8)\nP(X\u2081=x\u2081,</text><text x=\"120.0\" y=\"94.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">..., X_n=x_n) = \u222b\u2080\u00b9 \u03b8^k (1-\u03b8)^{n-k} dF(\u03b8)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">De Finetti: Every infinite exchangeable binary sequence is a mixture of i.i.d. Bernoulli trials</text></svg>",
    "drawingCaption": "Infinite exchangeability is mathematically equivalent to conditional independence given a latent random parameter",
    "coreTranslation": [
      "<strong>Representation Statement:</strong> Let $(X_1, X_2, \\dots)$ be an infinite exchangeable sequence of binary variables $X_i \\in \\{0, 1\\}$. Then there exists a unique distribution function $F_\\Theta$ on $[0, 1]$ such that given $\\Theta = \\theta$, $X_i$ are i.i.d. $\\text{Bernoulli}(\\theta)$.",
      "<strong>Integral Mixture:</strong> $\\mathbb{P}(X_1 = x_1, \\dots, X_n = x_n) = \\int_0^1 \\theta^{\\sum x_i} (1 - \\theta)^{n - \\sum x_i} dF_\\Theta(\\theta)$.",
      "<strong>Bayesian Foundation:</strong> Justifies Bayesian probability: the 'unknown parameter' $\\Theta$ is mathematically proven to exist as the almost sure limiting frequency $\\Theta = \\lim_{n \\to \\infty} \\frac{1}{n}\\sum_{i=1}^n X_i$."
    ],
    "math": "$$\\mathbb{P}(X_1=x_1, \\dots, X_n=x_n) = \\int_0^1 \\theta^{\\sum x_i} (1-\\theta)^{n - \\sum x_i}\\,dF_\\Theta(\\theta), \\quad \\Theta = \\lim_{n \\to \\infty} \\frac{1}{n}\\sum_{i=1}^n X_i$$",
    "personalConnection": "A factory coin: the coin's bias \u03b8 is chosen once at manufacturing time from prior F_\u0398, after which all tosses with that coin are independent given \u03b8.",
    "examTrap": "Applying De Finetti to finite sequences! De Finetti FAILS for finite exchangeable collections; the infinite horizon is strictly necessary for the representation integral to hold."
  },
  {
    "id": 31006,
    "subject": "StoMA",
    "topicId": "10_Exchangeable_Random_Variables",
    "topicTitle": "10 \u00b7 Exchangeable Random Variables",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: P\u00f3lya\u2019s Urn Scheme & Exchangeability",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31006\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"25\" width=\"60\" height=\"55\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"54\" y=\"45\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">w white</text><text x=\"54\" y=\"62\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">b black</text><line x1=\"84\" y1=\"52\" x2=\"120\" y2=\"52\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31006)\"/><text x=\"102\" y=\"42\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Draw color</text><rect x=\"120\" y=\"35\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"168.0\" y=\"52.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Return ball PLUS\nc balls of</text><text x=\"168.0\" y=\"60.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">same color\n(Reinforcement)</text><rect x=\"24\" y=\"90\" width=\"192\" height=\"28\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"103.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Any sequence of k white and (n-k)</text><text x=\"120.0\" y=\"111.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">black balls has IDENTICAL probability!</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P\u00f3lya's Urn generates an infinite exchangeable sequence; limiting fraction \u0398 ~ Beta(w/c, b/c)</text></svg>",
    "drawingCaption": "Reinforced urn sampling creates an exchangeable process where color count matters, but sequence order is irrelevant",
    "coreTranslation": [
      "<strong>Urn Dynamics:</strong> Start with $w$ white and $b$ black balls. Draw a ball, note its color, and replace it along with $c$ additional balls of the SAME color.",
      "<strong>Exchangeable Proof:</strong> The probability of any specific sequence with $k$ white and $(n - k)$ black balls is identical regardless of order: $\\frac{w(w+c)\\cdots(w+(k-1)c) \\cdot b(b+c)\\cdots(b+(n-k-1)c)}{(w+b)(w+b+c)\\cdots(w+b+(n-1)c)}$.",
      "<strong>Limiting Law:</strong> As $n \\to \\infty$, the proportion of white balls converges almost surely to random variable $\\Theta \\sim \\text{Beta}\\left(\\frac{w}{c}, \\frac{b}{c}\\right)$. For $w=1, b=1, c=1$, $\\Theta \\sim \\text{Uniform}(0, 1)$."
    ],
    "math": "$$\\mathbb{P}(X_1=x_1, \\dots, X_n=x_n) = \\frac{\\prod_{j=0}^{k-1}(w + jc) \\prod_{j=0}^{n-k-1}(b + jc)}{\\prod_{j=0}^{n-1}(w + b + jc)}, \\quad \\Theta \\sim \\text{Beta}\\left(\\tfrac{w}{c}, \\tfrac{b}{c}\\right)$$",
    "personalConnection": "Social media virality: a post with initial upvotes attracts further upvotes proportionally, stabilizing to an exchangeable popularity distribution.",
    "examTrap": "Assuming P\u00f3lya's urn trials are independent. The draws are heavily dependent (positive feedback reinforcement), yet perfectly exchangeable!"
  },
  {
    "id": 31101,
    "subject": "StoMA",
    "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
    "topicTitle": "11 \u00b7 Covariance & Linear Least Squares (LLSE)",
    "cardNumber": "01",
    "category": "COVARIANCE MATRICES",
    "highlighterClass": "highlight-cyan",
    "title": "Covariance Matrix Properties & Positive Semidefiniteness",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31101\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"18\" width=\"192\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"34.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03a3_X = E[(X - \u03bc_X)(X - \u03bc_X)\u1d40] = E[X X\u1d40] - \u03bc_X</text><text x=\"120.0\" y=\"43.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc_X\u1d40\nSymmetric Positive Semidefinite: \u03a3_X \u2ab0 0</text><rect x=\"24\" y=\"60\" width=\"192\" height=\"30\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"74.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2200 v \u2208 \u211d\u207f:   v\u1d40 \u03a3_X v = Var(v\u1d40</text><text x=\"120.0\" y=\"83.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X) \u2265 0   (Eigenvalues \u03bb\u1d62 \u2265 0)</text><rect x=\"24\" y=\"96\" width=\"192\" height=\"26\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"108.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Affine transform: Y = A</text><text x=\"120.0\" y=\"117.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X + b  \u21d2  \u03a3_Y = A \u03a3_X A\u1d40</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Covariance matrices are symmetric positive semidefinite; quadratic forms equal variance</text></svg>",
    "drawingCaption": "The covariance matrix is always symmetric positive semidefinite; its quadratic form measures directional variance",
    "coreTranslation": [
      "<strong>Definition:</strong> For random vector $X \\in \\mathbb{R}^n$, $\\Sigma_X \\triangleq \\mathbb{E}[(X - \\mu_X)(X - \\mu_X)^\\top] = \\mathbb{E}[XX^\\top] - \\mu_X\\mu_X^\\top$.",
      "<strong>Positive Semidefiniteness ($\\Sigma_X \\succeq 0$):</strong> For any deterministic vector $v \\in \\mathbb{R}^n$, $v^\\top \\Sigma_X v = \\operatorname{Var}(v^\\top X) \\ge 0$. All eigenvalues are real and non-negative ($\\lambda_i \\ge 0$).",
      "<strong>Affine Transformation Law:</strong> If $Y = A X + b$, then $\\mu_Y = A\\mu_X + b$ and $\\Sigma_Y = A \\Sigma_X A^\\top$."
    ],
    "math": "$$\\Sigma_X = \\mathbb{E}[(X - \\mu)(X - \\mu)^\\top] \\succeq 0, \\qquad \\Sigma_{AX + b} = A \\Sigma_X A^\\top, \\qquad v^\\top \\Sigma_X v = \\operatorname{Var}(v^\\top X) \\ge 0$$",
    "personalConnection": "Ellipsoid of inertia: the eigenvalues of \u03a3 dictate the lengths of the principal dispersion axes of a multidimensional data cloud.",
    "examTrap": "Writing \u03a3_{AX} = A\u1d40 \u03a3_X A instead of A \u03a3_X A\u1d40! If A is m \u00d7 n, A \u03a3_X A\u1d40 produces the correct m \u00d7 m covariance matrix."
  },
  {
    "id": 31102,
    "subject": "StoMA",
    "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
    "topicTitle": "11 \u00b7 Covariance & Linear Least Squares (LLSE)",
    "cardNumber": "02",
    "category": "ORTHOGONALITY PRINCIPLE",
    "highlighterClass": "highlight-amber",
    "title": "The Orthogonality Principle: Hilbert Space Geometry of Estimation",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31102\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"30\" y1=\"110\" x2=\"210\" y2=\"110\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"200\" y=\"122\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Affine subspace of X</text><line x1=\"60\" y1=\"110\" x2=\"140\" y2=\"35\" stroke=\"#000000\" stroke-width=\"2.0\" marker-end=\"url(#arr-31102)\"/><text x=\"145\" y=\"30\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Target Y</text><line x1=\"60\" y1=\"110\" x2=\"140\" y2=\"110\" stroke=\"#000000\" stroke-width=\"2.0\" marker-end=\"url(#arr-31102)\"/><text x=\"140\" y=\"124\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">LLSE: \u0176</text><line x1=\"140\" y1=\"110\" x2=\"140\" y2=\"35\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"3 3\"/><text x=\"165\" y=\"72\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Error: e = Y - \u0176</text><polygon points=\"140,100 130,100 130,110\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Orthogonality: E[(Y - \u0176) X\u1d40] = 0 and E[Y - \u0176] = 0 (Error is orthogonal to data)</text></svg>",
    "drawingCaption": "The optimal linear estimator projects Y onto the linear subspace of X; error e = Y - \u0176 is orthogonal to X",
    "coreTranslation": [
      "<strong>Geometric Formulation:</strong> Random variables form an inner product space under $\\langle U, V \\rangle = \\mathbb{E}[UV]$. Distance is root-mean-square error $\\|Y - \\hat{Y}\\|_{L^2} = \\sqrt{\\mathbb{E}[|Y - \\hat{Y}|^2]}$.",
      "<strong>Orthogonality Condition:</strong> $\\hat{Y} = AX + b$ minimizes MSE if and only if estimation error $e = Y - \\hat{Y}$ is orthogonal to all observations and affine constants: $\\mathbb{E}[e X^\\top] = 0$ and $\\mathbb{E}[e] = 0$.",
      "<strong>Zero Residual Information:</strong> The error $e$ has zero correlation with $X$, meaning no further linear predictive power remains in the observation."
    ],
    "math": "$$\\mathbb{E}[Y - \\hat{Y}] = 0, \\qquad \\mathbb{E}\\left[(Y - \\hat{Y}) X^\\top\\right] = 0 \\iff \\hat{Y} \\text{ minimizes } \\mathbb{E}\\left[\\|Y - \\hat{Y}\\|^2\\right]$$",
    "personalConnection": "Dropping a perpendicular shadow: the shortest path from a point in the air to a tabletop is the perpendicular drop; any oblique shadow is strictly longer.",
    "examTrap": "Assuming error is independent of X. Orthogonality guarantees ZERO CORRELATION (Cov(e, X) = 0), not independence! Independence holds only under joint Gaussianity."
  },
  {
    "id": 31103,
    "subject": "StoMA",
    "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
    "topicTitle": "11 \u00b7 Covariance & Linear Least Squares (LLSE)",
    "cardNumber": "03",
    "category": "LLSE FORMULA",
    "highlighterClass": "highlight-emerald",
    "title": "The Multivariate Linear Least Squares Estimator (LLSE)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31103\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"41.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Multivariate LLSE:\n\u0176(X) = \u03bc_Y + \u03a3_{YX} \u03a3_X\u207b\u00b9 (X</text><text x=\"120.0\" y=\"51.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">- \u03bc_X)\n(Best linear approximation of Y given X)</text><rect x=\"20\" y=\"72\" width=\"200\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Optimal Gain Matrix: K = \u03a3_{YX} \u03a3_X\u207b\u00b9\nError</text><text x=\"120.0\" y=\"98.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Covariance: \u03a3_e = \u03a3_Y - \u03a3_{YX} \u03a3_X\u207b\u00b9 \u03a3_{XY}</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Requires ONLY first and second moments (means and covariances); no full densities needed</text></svg>",
    "drawingCaption": "The closed-form LLSE requires only first and second moments, adjusting prior mean by optimal gain matrix",
    "coreTranslation": [
      "<strong>Closed-Form Estimator:</strong> $\\hat{Y}_{\\text{LLSE}}(X) = \\mu_Y + \\Sigma_{YX} \\Sigma_X^{-1} (X - \\mu_X)$, where $\\Sigma_{YX} = \\mathbb{E}[(Y - \\mu_Y)(X - \\mu_X)^\\top]$.",
      "<strong>Optimal Kalman Gain:</strong> The matrix $K \\triangleq \\Sigma_{YX} \\Sigma_X^{-1}$ is the optimal linear regression weight matrix.",
      "<strong>Data Parsimony:</strong> LLSE requires ONLY means $\\mu_X, \\mu_Y$ and covariances $\\Sigma_X, \\Sigma_{YX}$. It computes without knowing the underlying probability density functions."
    ],
    "math": "$$\\hat{Y}_{\\text{LLSE}}(X) = \\mu_Y + \\Sigma_{YX}\\Sigma_X^{-1}(X - \\mu_X), \\qquad K = \\Sigma_{YX}\\Sigma_X^{-1}$$",
    "personalConnection": "GPS position filtering: starting at baseline belief \u03bc_Y and correcting position by multiplying sensor error (X - \u03bc_X) by Kalman gain matrix K.",
    "examTrap": "Assuming LLSE is the optimal overall estimator. LLSE is optimal ONLY among affine estimators (c\u1d40X + d). The unconditional MMSE estimator is conditional expectation E[Y|X], which may be highly non-linear."
  },
  {
    "id": 31104,
    "subject": "StoMA",
    "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
    "topicTitle": "11 \u00b7 Covariance & Linear Least Squares (LLSE)",
    "cardNumber": "04",
    "category": "ERROR COVARIANCE",
    "highlighterClass": "highlight-purple",
    "title": "Error Covariance Matrix & Schur Complement Geometry",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31104\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"192\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Error Covariance Matrix \u03a3_e:\n\u03a3_e = E[(Y</text><text x=\"120.0\" y=\"49.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">- \u0176)(Y - \u0176)\u1d40]\n= \u03a3_Y - \u03a3_{YX} \u03a3_X\u207b\u00b9 \u03a3_{XY}</text><rect x=\"24\" y=\"70\" width=\"192\" height=\"40\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Schur Complement of Joint Covariance:\n[ \u03a3_X    \u03a3_{XY} ]\n[</text><text x=\"120.0\" y=\"98.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03a3_{YX} \u03a3_Y    ]   \u21d2  \u03a3_e = \u03a3_Y - \u03a3_{YX} \u03a3_X\u207b\u00b9 \u03a3_{XY} \u2ab0 0</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Information reduction: Observation X always reduces (or preserves) error covariance: \u03a3_e \u2aaf \u03a3_Y</text></svg>",
    "drawingCaption": "The estimation error covariance is the Schur complement of the joint covariance matrix: \u03a3_e = \u03a3_Y - \u03a3_{YX} \u03a3_X\u207b\u00b9 \u03a3_{XY}",
    "coreTranslation": [
      "<strong>Matrix Formula:</strong> $\\Sigma_e \\triangleq \\operatorname{Cov}(Y - \\hat{Y}) = \\Sigma_Y - \\Sigma_{YX} \\Sigma_X^{-1} \\Sigma_{XY}$.",
      "<strong>Monotonic Variance Reduction:</strong> Since $\\Sigma_{YX} \\Sigma_X^{-1} \\Sigma_{XY} \\succeq 0$, the error covariance satisfies $\\Sigma_e \\preceq \\Sigma_Y$ (in the Loewner positive semidefinite order). Observation $X$ can only decrease uncertainty.",
      "<strong>Schur Complement Identity:</strong> $\\Sigma_e$ is precisely the Schur complement of block $\\Sigma_X$ in the joint covariance matrix $\\begin{bmatrix} \\Sigma_X & \\Sigma_{XY} \\\\ \\Sigma_{YX} & \\Sigma_Y \\end{bmatrix}$."
    ],
    "math": "$$\\Sigma_e = \\operatorname{Cov}(Y - \\hat{Y}) = \\Sigma_Y - \\Sigma_{YX}\\Sigma_X^{-1}\\Sigma_{XY} \\preceq \\Sigma_Y$$",
    "personalConnection": "Measuring an object through fog: taking a photo never increases your uncertainty about its shape; error variance drops by the amount captured in \u03a3_{YX} \u03a3_X\u207b\u00b9 \u03a3_{XY}.",
    "examTrap": "Singular \u03a3_X: If \u03a3_X is not invertible (observations are linearly redundant), replace \u03a3_X\u207b\u00b9 with the Moore-Penrose pseudoinverse \u03a3_X\u207a."
  },
  {
    "id": 31105,
    "subject": "StoMA",
    "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
    "topicTitle": "11 \u00b7 Covariance & Linear Least Squares (LLSE)",
    "cardNumber": "05",
    "category": "SCALAR LLSE",
    "highlighterClass": "highlight-cyan",
    "title": "Scalar LLSE & The Pearson Correlation Coefficient",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31105\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31105)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31105)\"/><line x1=\"40\" y1=\"95\" x2=\"200\" y2=\"35\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"180\" y=\"28\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Slope = \u03c1 (\u03c3_Y / \u03c3_X)</text><circle cx=\"120\" cy=\"65\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"52\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(\u03bc_X, \u03bc_Y)</text><rect x=\"24\" y=\"20\" width=\"100\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"74.0\" y=\"36.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u0176 = \u03bc_Y + \u03c1 (\u03c3_Y/\u03c3_X)(X -</text><text x=\"74.0\" y=\"44.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc_X)\nSlope = Cov(X,Y)/Var(X)</text><rect x=\"130\" y=\"20\" width=\"86\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"173.0\" y=\"36.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">MSE = \u03c3_Y\u00b2 (1</text><text x=\"173.0\" y=\"45.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">- \u03c1\u00b2)\nR\u00b2 = \u03c1\u00b2</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Scalar LLSE is the classic linear regression line; MSE drops by factor (1 - \u03c1\u00b2)</text></svg>",
    "drawingCaption": "In 1D, the LLSE is the standard regression line whose residual variance equals \u03c3_Y\u00b2 (1 - \u03c1\u00b2)",
    "coreTranslation": [
      "<strong>Scalar Formula:</strong> $\\hat{Y} = \\mu_Y + \\rho \\frac{\\sigma_Y}{\\sigma_X} (X - \\mu_X)$, where Pearson correlation $\\rho = \\frac{\\operatorname{Cov}(X, Y)}{\\sigma_X \\sigma_Y} \\in [-1, 1]$.",
      "<strong>Slope & Anchor:</strong> The line passes through the bivariate centroid $(\\mu_X, \\mu_Y)$ with regression slope $\\beta = \\frac{\\operatorname{Cov}(X, Y)}{\\operatorname{Var}(X)} = \\rho \\frac{\\sigma_Y}{\\sigma_X}$.",
      "<strong>Residual MSE:</strong> $\\mathbb{E}[(Y - \\hat{Y})^2] = \\sigma_Y^2 (1 - \\rho^2)$. When $|\\rho| = 1$, MSE is 0 (exact prediction); when $\\rho = 0$, $\\hat{Y} = \\mu_Y$ and MSE is $\\sigma_Y^2$."
    ],
    "math": "$$\\hat{Y} = \\mu_Y + \\rho \\frac{\\sigma_Y}{\\sigma_X}(X - \\mu_X), \\qquad \\operatorname{MSE} = \\sigma_Y^2(1 - \\rho^2)$$",
    "personalConnection": "Regression to the mean (Galton): children of exceptionally tall parents (X) are predicted to be above average (Y), but shrunk toward the population mean by factor \u03c1.",
    "examTrap": "Swapping X and Y in the regression slope: the slope for predicting Y from X is \u03c1(\u03c3_Y/\u03c3_X), while the slope for predicting X from Y is \u03c1(\u03c3_X/\u03c3_Y) (which is NOT 1/slope!)."
  },
  {
    "id": 31106,
    "subject": "StoMA",
    "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
    "topicTitle": "11 \u00b7 Covariance & Linear Least Squares (LLSE)",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Signal Estimation in Additive Noise (Wiener Filter)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31106\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"60\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"46.0\" y=\"33.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Signal X\n(Var</text><text x=\"46.0\" y=\"42.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= \u03c3_X\u00b2)</text><line x1=\"76\" y1=\"34\" x2=\"106\" y2=\"34\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31106)\"/><circle cx=\"114\" cy=\"34\" r=\"8\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"114\" y=\"37\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">+</text><line x1=\"114\" y1=\"10\" x2=\"114\" y2=\"26\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31106)\"/><text x=\"114\" y=\"6\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Noise W ~ (0, \u03c3_W\u00b2)</text><line x1=\"122\" y1=\"34\" x2=\"150\" y2=\"34\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31106)\"/><rect x=\"150\" y=\"20\" width=\"66\" height=\"28\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"183.0\" y=\"33.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Observe</text><text x=\"183.0\" y=\"42.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Y\nY = X + W</text><rect x=\"16\" y=\"68\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Optimal Filter: X\u0302(Y) = [ \u03c3_X\u00b2 / (\u03c3_X\u00b2 + \u03c3_W\u00b2) ] \u00b7 Y  (Wiener gain)\nMSE</text><text x=\"120.0\" y=\"97.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= [ \u03c3_X\u00b2 \u03c3_W\u00b2 ] / (\u03c3_X\u00b2 + \u03c3_W\u00b2) = \u03c3_X\u00b2 \u00b7 (1 - SNR / (1 + SNR))</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Signal shrinkage: High SNR (\u03c3_X\u00b2 >> \u03c3_W\u00b2) yields X\u0302 \u2248 Y; Low SNR shrinks X\u0302 \u2192 0</text></svg>",
    "drawingCaption": "Estimating zero-mean signal X from noisy observation Y = X + W shrinks Y by signal-to-noise ratio fraction",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Signal $X$ has mean $0$ and variance $\\sigma_X^2$. Observation is $Y = X + W$, where noise $W$ has mean $0$, variance $\\sigma_W^2$, and $X \\perp W$.",
      "<strong>Covariance Derivation:</strong> $\\operatorname{Var}(Y) = \\sigma_X^2 + \\sigma_W^2$. Cross-covariance is $\\operatorname{Cov}(X, Y) = \\mathbb{E}[X(X + W)] = \\mathbb{E}[X^2] = \\sigma_X^2$.",
      "<strong>Wiener Shrinkage Estimator:</strong> $\\hat{X}(Y) = \\frac{\\sigma_X^2}{\\sigma_X^2 + \\sigma_W^2} Y = \\frac{\\text{SNR}}{1 + \\text{SNR}} Y$. Minimum MSE is $\\frac{\\sigma_X^2 \\sigma_W^2}{\\sigma_X^2 + \\sigma_W^2}$."
    ],
    "math": "$$\\hat{X}(Y) = \\frac{\\sigma_X^2}{\\sigma_X^2 + \\sigma_W^2} Y, \\qquad \\operatorname{MSE} = \\frac{\\sigma_X^2 \\sigma_W^2}{\\sigma_X^2 + \\sigma_W^2} = \\sigma_X^2 \\left(1 - \\frac{\\text{SNR}}{1 + \\text{SNR}}\\right)$$",
    "personalConnection": "Noise-cancelling audio headphones: when music is loud and static is faint (high SNR), pass the audio directly; when music is faint and static dominates, heavily suppress the signal toward zero.",
    "examTrap": "Using raw observation Y as the estimator without shrinkage! Y is unbiased, but has MSE equal to \u03c3_W\u00b2, which is strictly WORSE than the Wiener estimate's MSE."
  },
  {
    "id": 31201,
    "subject": "StoMA",
    "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
    "topicTitle": "12 \u00b7 Conditional Expectation & MMSE",
    "cardNumber": "01",
    "category": "MMSE OPTIMALITY",
    "highlighterClass": "highlight-cyan",
    "title": "Conditional Expectation: The Unconstrained MMSE Estimator",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31201\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M 25,115 Q 120,85 215,115\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"200\" y=\"125\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">L\u00b2(\u03c3(X)) subspace</text><circle cx=\"120\" cy=\"25\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"15\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Target Y</text><line x1=\"120\" y1=\"25\" x2=\"120\" y2=\"93\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"3 3\"/><circle cx=\"120\" cy=\"93\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"106\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[Y | X] (MMSE)</text><text x=\"165\" y=\"55\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Error: Y - E[Y|X]</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">E[Y|X] is the unique projection of Y onto L\u00b2(\u03c3(X)), minimizing unconstrained MSE</text></svg>",
    "drawingCaption": "Conditional expectation E[Y|X] is the optimal unconstrained estimator, minimizing mean squared error over all functions",
    "coreTranslation": [
      "<strong>Optimization Problem:</strong> Find $g^*(X) = \\arg\\min_{g} \\mathbb{E}[(Y - g(X))^2]$ over ALL measurable functions (linear or non-linear).",
      "<strong>Fundamental Theorem:</strong> The unique minimizer is the conditional expectation: $g^*(X) = \\mathbb{E}[Y \\mid X] = \\int y f_{Y \\mid X}(y \\mid X)\\,dy$.",
      "<strong>Random Variable Character:</strong> $\\mathbb{E}[Y \\mid X]$ is NOT a fixed number! It is a random variable measurable with respect to $\\sigma(X)$, taking value $\\mathbb{E}[Y \\mid X=x]$ when $X=x$."
    ],
    "math": "$$\\hat{Y}_{\\text{MMSE}} = \\mathbb{E}[Y \\mid X] = \\arg\\min_{g \\in \\sigma(X)} \\mathbb{E}\\left[(Y - g(X))^2\\right], \\qquad \\mathbb{E}\\left[\\mathbb{E}[Y \\mid X]\\right] = \\mathbb{E}[Y]$$",
    "personalConnection": "A weather forecaster: after observing thermometer and barometer readings X, your optimal forecast for tomorrow's rain Y is the conditional mean of rain given today's exact instruments.",
    "examTrap": "Treating E[Y|X] as a deterministic number! E[Y|X] is a random variable, a function of X. Only when evaluated at a fixed sample realization X = x does it become a constant."
  },
  {
    "id": 31202,
    "subject": "StoMA",
    "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
    "topicTitle": "12 \u00b7 Conditional Expectation & MMSE",
    "cardNumber": "02",
    "category": "ORTHOGONALITY",
    "highlighterClass": "highlight-amber",
    "title": "The Non-Linear Orthogonality Principle: L\u00b2(\u03c3(X))",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31202\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M 30,110 Q 120,80 210,110\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"50\" y1=\"105\" x2=\"120\" y2=\"30\" stroke=\"#000000\" stroke-width=\"2.0\" marker-end=\"url(#arr-31202)\"/><text x=\"125\" y=\"25\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Y</text><line x1=\"50\" y1=\"105\" x2=\"120\" y2=\"88\" stroke=\"#000000\" stroke-width=\"2.0\" marker-end=\"url(#arr-31202)\"/><text x=\"120\" y=\"102\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[Y | X]</text><line x1=\"120\" y1=\"30\" x2=\"120\" y2=\"88\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"3 3\"/><polygon points=\"120,78 110,78 110,88\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/><rect x=\"24\" y=\"20\" width=\"85\" height=\"34\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"66.5\" y=\"36.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Error e = Y -</text><text x=\"66.5\" y=\"44.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[Y|X]\nOrthogonal to all h(X)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Non-linear orthogonality: E[(Y - E[Y|X]) h(X)] = 0 for ALL measurable functions h</text></svg>",
    "drawingCaption": "The MMSE error e = Y - E[Y|X] is orthogonal to every measurable transformation h(X), linear or non-linear",
    "coreTranslation": [
      "<strong>Orthogonality Condition:</strong> For any measurable function $h(X)$ with $\\mathbb{E}[h(X)^2] < \\infty$, $\\mathbb{E}[(Y - \\mathbb{E}[Y \\mid X]) h(X)] = 0$.",
      "<strong>Zero Residual Prediction:</strong> No transformation of $X$\u2014whether $X, X^2, e^X$, or a deep neural network\u2014can extract any further predictive correlation from the residual error.",
      "<strong>Unbiasedness:</strong> Setting $h(X) = 1$ immediately proves $\\mathbb{E}[Y - \\mathbb{E}[Y \\mid X]] = 0$, guaranteeing that the MMSE estimator is unconditionally unbiased."
    ],
    "math": "$$\\mathbb{E}\\left[\\left(Y - \\mathbb{E}[Y \\mid X]\\right) h(X)\\right] = 0 \\quad \\forall h \\in L^2(\\sigma(X))$$",
    "personalConnection": "Complete data exhaustion: a gold miner who has extracted every particle of gold from an ore sample: no acid or mechanical wash can extract any remaining trace.",
    "examTrap": "Confusing LLSE with MMSE orthogonality! LLSE error is orthogonal only to affine functions aX + b; MMSE error is orthogonal to ALL measurable non-linear functions h(X)."
  },
  {
    "id": 31203,
    "subject": "StoMA",
    "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
    "topicTitle": "12 \u00b7 Conditional Expectation & MMSE",
    "cardNumber": "03",
    "category": "TOWER PROPERTY",
    "highlighterClass": "highlight-emerald",
    "title": "The Tower Property & 'Taking Out What is Known'",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31203\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"192\" height=\"32\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"35.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Nested Conditioning:  E[ E[Y | X\u2081, X\u2082] | X\u2081 ] = E[Y |</text><text x=\"120.0\" y=\"44.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X\u2081]\n(Conditioning on LESS information always dominates)</text><rect x=\"24\" y=\"60\" width=\"192\" height=\"32\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"75.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Law of Total Expectation:  E[ E[Y | X] ] = E[Y]\n(Average</text><text x=\"120.0\" y=\"84.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">of local conditional means equals unconditional mean)</text><rect x=\"24\" y=\"100\" width=\"192\" height=\"26\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"112.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Taking out what is known:  E[</text><text x=\"120.0\" y=\"121.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g(X) Y | X ] = g(X) \u00b7 E[Y | X]</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Information hierarchies: coarser information washes out finer details; known factors factor out</text></svg>",
    "drawingCaption": "Nested conditioning preserves the coarser information filter: E[E[Y|X\u2081, X\u2082]|X\u2081] = E[Y|X\u2081]",
    "coreTranslation": [
      "<strong>Tower Property (Total Expectation):</strong> $\\mathbb{E}[\\mathbb{E}[Y \\mid X]] = \\mathbb{E}[Y]$. The expectation of the conditional expectation recovers the unconditional mean.",
      "<strong>Nested Conditioning:</strong> For nested $\\sigma$-algebras $\\mathcal{G}_1 \\subset \\mathcal{G}_2$, $\\mathbb{E}[\\mathbb{E}[Y \\mid \\mathcal{G}_2] \\mid \\mathcal{G}_1] = \\mathbb{E}[Y \\mid \\mathcal{G}_1]$. Conditioning on less information always wins.",
      "<strong>Taking Out What Is Known:</strong> If $g(X)$ is $\\sigma(X)$-measurable, $\\mathbb{E}[g(X) Y \\mid X] = g(X)\\,\\mathbb{E}[Y \\mid X]$. Known variables act as scalars inside the conditional expectation."
    ],
    "math": "$$\\mathbb{E}\\left[\\mathbb{E}[Y \\mid X_1, X_2] \\;\\middle|\\; X_1\\right] = \\mathbb{E}[Y \\mid X_1], \\qquad \\mathbb{E}[g(X) Y \\mid X] = g(X) \\mathbb{E}[Y \\mid X]$$",
    "personalConnection": "A national census: aggregating regional school averages yields the total national average; reporting local data to a high-level authority collapses fine-grained distinctions.",
    "examTrap": "Reversing the tower ordering: E[E[Y|X\u2081]|X\u2081, X\u2082] = E[Y|X\u2081], NOT E[Y|X\u2081, X\u2082]! Finer conditioning cannot invent new information that was already lost."
  },
  {
    "id": 31204,
    "subject": "StoMA",
    "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
    "topicTitle": "12 \u00b7 Conditional Expectation & MMSE",
    "cardNumber": "04",
    "category": "VARIANCE DECOMPOSITION",
    "highlighterClass": "highlight-purple",
    "title": "Law of Total Variance (Eve\u2019s Law): Noise vs Signal",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31204\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"192\" height=\"28\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"37.0\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Total Variance:  Var(Y)</text><rect x=\"24\" y=\"58\" width=\"92\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"70.0\" y=\"79.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[ Var(Y | X) ]\nExpected\nwithin-slice</text><text x=\"70.0\" y=\"87.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">variance\n(Unexplained noise)</text><text x=\"120\" y=\"80\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">+</text><rect x=\"124\" y=\"58\" width=\"92\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"170.0\" y=\"79.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var( E[Y | X] )\nVariance</text><text x=\"170.0\" y=\"87.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">of\nconditional mean\n(Explained signal)</text><text x=\"120\" y=\"118\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">MMSE Error = E[Var(Y | X)] \u2264 Var(Y)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Eve's Law: Var(Y) = E[Var(Y | X)] + Var(E[Y | X]) decomposes total risk into noise and signal</text></svg>",
    "drawingCaption": "Total variance decomposes into expected conditional variance (noise) plus variance of conditional mean (signal)",
    "coreTranslation": [
      "<strong>Formal Decomposition:</strong> $\\operatorname{Var}(Y) = \\mathbb{E}[\\operatorname{Var}(Y \\mid X)] + \\operatorname{Var}(\\mathbb{E}[Y \\mid X])$.",
      "<strong>Signal vs Noise:</strong> $\\operatorname{Var}(\\mathbb{E}[Y \\mid X])$ is the variance explained by observation $X$ (signal), while $\\mathbb{E}[\\operatorname{Var}(Y \\mid X)]$ is the residual unexplained dispersion (noise).",
      "<strong>MMSE Error Formula:</strong> The minimum mean squared estimation error is precisely the expected conditional variance: $\\mathbb{E}[(Y - \\hat{Y}_{\\text{MMSE}})^2] = \\mathbb{E}[\\operatorname{Var}(Y \\mid X)] \\le \\operatorname{Var}(Y)$."
    ],
    "math": "$$\\operatorname{Var}(Y) = \\mathbb{E}\\left[\\operatorname{Var}(Y \\mid X)\\right] + \\operatorname{Var}\\left(\\mathbb{E}[Y \\mid X]\\right), \\qquad \\text{MMSE Error} = \\mathbb{E}\\left[\\operatorname{Var}(Y \\mid X)\\right]$$",
    "personalConnection": "Exam scores across a nation: within-school variance (students differing inside each school) PLUS across-school variance (school district averages differing from each other).",
    "examTrap": "Missing one of the two terms in Eve's law! Forgetting Var(E[Y|X]) or E[Var(Y|X)] creates severe underestimates of total population volatility."
  },
  {
    "id": 31205,
    "subject": "StoMA",
    "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
    "topicTitle": "12 \u00b7 Conditional Expectation & MMSE",
    "cardNumber": "05",
    "category": "MMSE VS LLSE",
    "highlighterClass": "highlight-cyan",
    "title": "MMSE vs LLSE: Non-Linearity & Superiority",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31205\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31205)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31205)\"/><path d=\"M 40,30 Q 120,130 200,30\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"185\" y=\"30\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">MMSE: E[Y|X] = X\u00b2</text><line x1=\"40\" y1=\"75\" x2=\"200\" y2=\"75\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"3 3\"/><text x=\"180\" y=\"85\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">LLSE: \u0176 = E[Y]</text><rect x=\"24\" y=\"20\" width=\"110\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"79.0\" y=\"37.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Symmetric X \u21d2 Cov(X, X\u00b2)=0\nLLSE</text><text x=\"79.0\" y=\"45.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">error = Var(Y)\nMMSE error = 0!</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">MMSE \u2264 LLSE \u2264 Var(Y); LLSE coincides with MMSE if and only if E[Y|X] is affine</text></svg>",
    "drawingCaption": "LLSE is constrained to straight lines; MMSE explores all curves and can achieve zero error when LLSE fails completely",
    "coreTranslation": [
      "<strong>Performance Ordering:</strong> $\\text{MMSE Error} = \\mathbb{E}[(Y - \\mathbb{E}[Y \\mid X])^2] \\le \\text{LLSE Error} \\le \\operatorname{Var}(Y)$.",
      "<strong>Extreme Non-Linear Gap:</strong> When $Y = X^2$ with symmetric $X$, $\\operatorname{Cov}(X, Y) = 0$. LLSE outputs a useless flat line $\\hat{Y} = \\mathbb{E}[Y]$, while MMSE outputs exact parabola $\\mathbb{E}[Y \\mid X] = X^2$ with zero error!",
      "<strong>Coincidence Theorem:</strong> MMSE and LLSE are IDENTICAL if and only if $\\mathbb{E}[Y \\mid X]$ is an affine function of $X$ (which holds automatically for jointly Gaussian systems)."
    ],
    "math": "$$\\mathbb{E}\\left[\\left(Y - \\mathbb{E}[Y \\mid X]\\right)^2\\right] \\le \\mathbb{E}\\left[\\left(Y - \\hat{Y}_{\\text{LLSE}}\\right)^2\\right] \\le \\operatorname{Var}(Y)$$",
    "personalConnection": "Fitting a curve to a circle: a straight ruler (LLSE) fails miserably to follow the circular contour, whereas a flexible spline (MMSE) tracks the contour perfectly.",
    "examTrap": "Assuming LLSE is always a close approximation to MMSE. In non-linear symmetric systems, LLSE has 0% predictive power while MMSE has 100% predictive accuracy."
  },
  {
    "id": 31206,
    "subject": "StoMA",
    "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
    "topicTitle": "12 \u00b7 Conditional Expectation & MMSE",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Random Sums via Eve\u2019s Law (Poisson Thinning)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31206\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"64.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">N ~ Poisson(\u03bb)\nFlips of</text><text x=\"64.0\" y=\"46.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p-coin\nK ~ Binomial(N, p)</text><line x1=\"112\" y1=\"38\" x2=\"136\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31206)\"/><rect x=\"136\" y=\"20\" width=\"88\" height=\"36\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"180.0\" y=\"37.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Condition on N:\nE[K | N]</text><text x=\"180.0\" y=\"45.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= Np\nVar(K | N) = Np(1-p)</text><rect x=\"16\" y=\"68\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"82\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[K] = E[Np] = \u03bbp</text><text x=\"120\" y=\"98\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var(K) = E[Np(1-p)] + Var(Np) = \u03bbp(1-p) + \u03bbp\u00b2 = \u03bbp</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Poisson thinning: Total heads K has Mean = Var = \u03bbp, confirming K ~ Poisson(\u03bbp)</text></svg>",
    "drawingCaption": "Evaluating random sums through conditioning: E[K] = \u03bbp and Var(K) = \u03bbp confirm Poisson thinning",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Number of coin tosses $N \\sim \\text{Poisson}(\\lambda)$. Each flip lands Heads with probability $p$. Total heads is $K = \\sum_{i=1}^N X_i$.",
      "<strong>Conditional Moments:</strong> Given $N$, $K \\mid N \\sim \\text{Binomial}(N, p)$, so $\\mathbb{E}[K \\mid N] = Np$ and $\\operatorname{Var}(K \\mid N) = Np(1-p)$.",
      "<strong>Moments via Total Variance:</strong> $\\mathbb{E}[K] = \\mathbb{E}[Np] = \\lambda p$. $\\operatorname{Var}(K) = \\mathbb{E}[Np(1-p)] + \\operatorname{Var}(Np) = \\lambda p(1-p) + p^2 \\lambda = \\lambda p$. Matches Poisson($\\lambda p$) thinning!"
    ],
    "math": "$$\\mathbb{E}[K] = \\lambda p, \\qquad \\operatorname{Var}(K) = \\mathbb{E}[Np(1-p)] + \\operatorname{Var}(Np) = \\lambda p \\implies K \\sim \\text{Poisson}(\\lambda p)$$",
    "personalConnection": "Customer arrivals at a coffee shop: N visitors arrive per hour (Poisson \u03bb); each buys a pastry with probability p; pastry sales K follow a thinned Poisson law \u03bbp.",
    "examTrap": "Attempting to compute Var(K) as Var(N) \u00d7 Var(X\u1d62)! You must use the Law of Total Variance: E[Var(K|N)] + Var(E[K|N])."
  },
  {
    "id": 31301,
    "subject": "StoMA",
    "topicId": "13_Jointly_Gaussian_Random_Variables",
    "topicTitle": "13 \u00b7 Jointly Gaussian Random Variables",
    "cardNumber": "01",
    "category": "MULTIVARIATE NORMAL",
    "highlighterClass": "highlight-cyan",
    "title": "Multivariate Gaussian PDF & The Mahalanobis Form",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31301\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31301)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31301)\"/><ellipse cx=\"125\" cy=\"65\" rx=\"60\" ry=\"32\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(-25 125 65)\"/><ellipse cx=\"125\" cy=\"65\" rx=\"40\" ry=\"20\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(-25 125 65)\"/><circle cx=\"125\" cy=\"65\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"125\" y=\"52\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc</text><line x1=\"80\" y1=\"85\" x2=\"170\" y2=\"45\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"165\" y=\"35\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">v\u2081 (\u03bb\u2081)</text><rect x=\"24\" y=\"18\" width=\"192\" height=\"26\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"30.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_X(x) = (2\u03c0)^{-n/2} |\u03a3|^{-1/2}</text><text x=\"120.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">exp( - 1/2 (x - \u03bc)\u1d40 \u03a3\u207b\u00b9 (x - \u03bc) )</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Mahalanobis distance (x - \u03bc)\u1d40 \u03a3\u207b\u00b9 (x - \u03bc) = c\u00b2 defines concentric elliptical contours</text></svg>",
    "drawingCaption": "Multivariate Gaussian density contours are concentric ellipsoids oriented along the eigenvectors of \u03a3",
    "coreTranslation": [
      "<strong>Density Formula:</strong> For non-singular $\\Sigma \\succ 0$, $f_{\\mathbf{X}}(\\mathbf{x}) = \\frac{1}{(2\\pi)^{n/2} |\\Sigma|^{1/2}} \\exp\\left(-\\frac{1}{2}(\\mathbf{x} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (\\mathbf{x} - \\boldsymbol{\\mu})\\right)$ on $\\mathbb{R}^n$.",
      "<strong>Mahalanobis Distance:</strong> Level sets of constant probability density are ellipsoids defined by quadratic form $d_M^2(\\mathbf{x}, \\boldsymbol{\\mu}) = (\\mathbf{x} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (\\mathbf{x} - \\boldsymbol{\\mu}) = c^2$.",
      "<strong>Eigenvector Geometry:</strong> Principal axes align with eigenvectors $v_i$ of $\\Sigma$, with half-lengths proportional to standard deviations $\\sqrt{\\lambda_i}$."
    ],
    "math": "$$f_{\\mathbf{X}}(\\mathbf{x}) = \\frac{1}{(2\\pi)^{n/2} |\\Sigma|^{1/2}} \\exp\\left(-\\frac{1}{2}(\\mathbf{x} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1}(\\mathbf{x} - \\boldsymbol{\\mu})\\right), \\quad \\Sigma \\succ 0$$",
    "personalConnection": "Elliptical spiral galaxy: star density falls exponentially with Mahalanobis distance from the galactic nucleus, stretching along principal inertia axes.",
    "examTrap": "Attempting to write density when |\u03a3| = 0 (singular covariance). When variables are linearly dependent, the distribution is degenerate and has no density with respect to Lebesgue measure on \u211d\u207f."
  },
  {
    "id": 31302,
    "subject": "StoMA",
    "topicId": "13_Jointly_Gaussian_Random_Variables",
    "topicTitle": "13 \u00b7 Jointly Gaussian Random Variables",
    "cardNumber": "02",
    "category": "GAUSSIAN DEFINITION",
    "highlighterClass": "highlight-amber",
    "title": "Fundamental Theorem: All Linear Projections are Gaussian",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31302\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"85\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"62.5\" y=\"41.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X ~ N(\u03bc, \u03a3)\nin \u211d\u207f</text><line x1=\"105\" y1=\"38\" x2=\"135\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31302)\"/><text x=\"120\" y=\"28\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">t\u1d40 X</text><rect x=\"135\" y=\"20\" width=\"85\" height=\"36\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"177.5\" y=\"37.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">t\u1d40 X ~ N(t\u1d40\u03bc,</text><text x=\"177.5\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">t\u1d40\u03a3t)\nin \u211d\u00b9</text><rect x=\"20\" y=\"72\" width=\"200\" height=\"36\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">General Linear Map: Y = A X + b  \u21d2  Y ~ N(A\u03bc + b,  A \u03a3</text><text x=\"120.0\" y=\"98.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A\u1d40)\n(Linear operations preserve joint Gaussianity unconditionally)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Fundamental theorem: X is jointly Gaussian if and only if EVERY 1D projection t\u1d40X is Gaussian</text></svg>",
    "drawingCaption": "A random vector is jointly Gaussian iff every one-dimensional projection t\u1d40X is a standard 1D Gaussian",
    "coreTranslation": [
      "<strong>Fundamental Characterization:</strong> $\\mathbf{X}$ is jointly Gaussian if and only if every linear combination $a_1 X_1 + \\dots + a_n X_n = \\mathbf{t}^\\top \\mathbf{X}$ is a 1D Gaussian for all $\\mathbf{t} \\in \\mathbb{R}^n$.",
      "<strong>Linear Transformation Invariance:</strong> If $\\mathbf{X} \\sim \\mathcal{N}(\\boldsymbol{\\mu}, \\Sigma)$ and $Y = A \\mathbf{X} + b$, then $Y$ is strictly Gaussian: $Y \\sim \\mathcal{N}(A\\boldsymbol{\\mu} + b, A \\Sigma A^\\top)$.",
      "<strong>Complete Parametrization:</strong> A joint Gaussian law is 100% specified by its mean vector $\\boldsymbol{\\mu}$ and covariance matrix $\\Sigma$; all higher cumulants are identically zero."
    ],
    "math": "$$\\mathbf{X} \\sim \\mathcal{N}(\\boldsymbol{\\mu}, \\Sigma) \\iff \\mathbf{t}^\\top \\mathbf{X} \\sim \\mathcal{N}\\left(\\mathbf{t}^\\top \\boldsymbol{\\mu}, \\; \\mathbf{t}^\\top \\Sigma \\mathbf{t}\\right) \\quad \\forall \\mathbf{t} \\in \\mathbb{R}^n$$",
    "personalConnection": "Shadows of a 3D cloud: if every 1D shadow cast by a 3D gas cloud from every angle is a bell curve, the 3D cloud itself is an ellipsoidal Gaussian.",
    "examTrap": "Assuming marginally Gaussian variables are jointly Gaussian! Having X ~ N(0, 1) and Y ~ N(0, 1) does NOT imply (X, Y) is jointly Gaussian (e.g. Y = SX with sign flip S)."
  },
  {
    "id": 31303,
    "subject": "StoMA",
    "topicId": "13_Jointly_Gaussian_Random_Variables",
    "topicTitle": "13 \u00b7 Jointly Gaussian Random Variables",
    "cardNumber": "03",
    "category": "GAUSSIAN INDEPENDENCE",
    "highlighterClass": "highlight-emerald",
    "title": "Uncorrelated \u21d4 Independent for Joint Gaussians",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31303\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"192\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Jointly Gaussian + Cov(X\u1d62, X_j) = 0\n\u21d2 \u03a3 is diagonal: \u03a3 =</text><text x=\"120.0\" y=\"49.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">diag(\u03c3\u2081\u00b2, ..., \u03c3_n\u00b2)\n\u21d2 Exponent separates: \u2211 (x\u1d62 - \u03bc\u1d62)\u00b2 / (2\u03c3\u1d62\u00b2)</text><rect x=\"24\" y=\"70\" width=\"192\" height=\"38\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"88.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Density factorizes: f_X(x) = f_{X\u2081}(x\u2081) ...</text><text x=\"120.0\" y=\"97.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">f_{X_n}(x_n)\n\u21d2 X\u2081, ..., X_n are MUTUALLY INDEPENDENT!</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">For JOINTLY Gaussian vectors: Uncorrelated \u21d4 Independent (a unique Gaussian signature)</text></svg>",
    "drawingCaption": "For jointly Gaussian random variables, zero covariance is strictly equivalent to mutual statistical independence",
    "coreTranslation": [
      "<strong>Unique Invariant:</strong> For JOINTLY Gaussian vectors, $\\operatorname{Cov}(X_i, X_j) = 0 \\iff X_i \\perp X_j$. Zero correlation implies statistical independence.",
      "<strong>Factorization Proof:</strong> When covariances are zero, $\\Sigma = \\operatorname{diag}(\\sigma_i^2)$, so $\\Sigma^{-1} = \\operatorname{diag}(1/\\sigma_i^2)$ and $|\\Sigma| = \\prod \\sigma_i^2$. The quadratic form decouples: $(\\mathbf{x}-\\boldsymbol{\\mu})^\\top \\Sigma^{-1}(\\mathbf{x}-\\boldsymbol{\\mu}) = \\sum \\frac{(x_i - \\mu_i)^2}{\\sigma_i^2}$.",
      "<strong>Exclusivity:</strong> This equivalence is FALSE for general non-Gaussian variables (and false for variables that are individually Gaussian but not jointly Gaussian)."
    ],
    "math": "$$\\mathbf{X} \\text{ jointly Gaussian}, \\; \\operatorname{Cov}(X_i, X_j) = 0 \\iff X_i \\perp X_j \\iff f_{\\mathbf{X}}(\\mathbf{x}) = \\prod_{i=1}^n f_{X_i}(x_i)$$",
    "personalConnection": "Orthogonal thermal velocities: molecular velocity components v_x, v_y, v_z in an ideal gas are uncorrelated and therefore completely independent.",
    "examTrap": "Applying this equivalence without verifying JOINT Gaussianity. If joint normality fails, zero covariance tells you nothing about independence."
  },
  {
    "id": 31304,
    "subject": "StoMA",
    "topicId": "13_Jointly_Gaussian_Random_Variables",
    "topicTitle": "13 \u00b7 Jointly Gaussian Random Variables",
    "cardNumber": "04",
    "category": "GAUSSIAN CONDITIONING",
    "highlighterClass": "highlight-purple",
    "title": "Gaussian Conditioning: Exact Normality & MMSE = LLSE",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31304\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"41.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Conditional Law: X\u2081 | X\u2082 = x\u2082 ~ N(\u03bc_{1|2}, \u03a3_{1|2})\n\u03bc_{1|2} = \u03bc\u2081 + \u03a3\u2081\u2082 \u03a3\u2082\u2082\u207b\u00b9 (x\u2082 - \u03bc\u2082)  </text><text x=\"120.0\" y=\"50.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">[Linear in x\u2082 \u21d2 MMSE = LLSE]\n\u03a3_{1|2} = \u03a3\u2081\u2081 - \u03a3\u2081\u2082 \u03a3\u2082\u2082\u207b\u00b9 \u03a3\u2082\u2081       [CONSTANT, independent of x\u2082!]</text><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31304)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31304)\"/><line x1=\"140\" y1=\"70\" x2=\"140\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"140\" y=\"126\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X\u2082 = x\u2082</text><path d=\"M 140,114 Q 160,85 180,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"170\" y=\"95\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">N(\u03bc_{1|2}, \u03a3_{1|2})</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Gaussian conditional mean is linear (MMSE = LLSE); conditional variance is constant</text></svg>",
    "drawingCaption": "Conditioning a Gaussian vector yields another Gaussian: conditional mean is linear (MMSE = LLSE), and covariance is constant",
    "coreTranslation": [
      "<strong>Conditional Law:</strong> If $\\begin{bmatrix} X_1 \\\\ X_2 \\end{bmatrix} \\sim \\mathcal{N}\\left(\\begin{bmatrix}\\mu_1\\\\\\mu_2\\end{bmatrix}, \\begin{bmatrix}\\Sigma_{11}&\\Sigma_{12}\\\\\\Sigma_{21}&\\Sigma_{22}\\end{bmatrix}\\right)$, then $X_1 \\mid X_2 = x_2 \\sim \\mathcal{N}(\\mu_{1|2}, \\Sigma_{1|2})$.",
      "<strong>Linear Conditional Mean:</strong> $\\mu_{1|2} = \\mu_1 + \\Sigma_{12} \\Sigma_{22}^{-1}(x_2 - \\mu_2)$. The conditional mean is strictly affine, proving **MMSE $\\equiv$ LLSE**!",
      "<strong>Constant Conditional Covariance:</strong> $\\Sigma_{1|2} = \\Sigma_{11} - \\Sigma_{12} \\Sigma_{22}^{-1} \\Sigma_{21}$ is completely independent of the observed value $x_2$."
    ],
    "math": "$$X_1 \\mid X_2 = x_2 \\sim \\mathcal{N}\\left(\\mu_1 + \\Sigma_{12}\\Sigma_{22}^{-1}(x_2 - \\mu_2), \\; \\Sigma_{11} - \\Sigma_{12}\\Sigma_{22}^{-1}\\Sigma_{21}\\right)$$",
    "personalConnection": "Linear Kalman Filtering: every updated state estimate is strictly Gaussian; error covariance is independent of measurement values and can be computed offline.",
    "examTrap": "Expecting conditional variance \u03a3_{1|2} to change with observation x\u2082! For Gaussians, measurements shift the mean, but uncertainty reduction is invariant to observed data."
  },
  {
    "id": 31305,
    "subject": "StoMA",
    "topicId": "13_Jointly_Gaussian_Random_Variables",
    "topicTitle": "13 \u00b7 Jointly Gaussian Random Variables",
    "cardNumber": "05",
    "category": "GAUSSIAN ALGEBRA",
    "highlighterClass": "highlight-cyan",
    "title": "Direct Matrix Inversion: Reading Moments from Quadratic Forms",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31305\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Exponent: - 1/2 [ a(x - \u03bc_x)\u00b2 + 2b(x - \u03bc_x)(y - \u03bc_y) +</text><text x=\"120.0\" y=\"46.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">c(y - \u03bc_y)\u00b2 ]\nPrecision Matrix:  \u03a3\u207b\u00b9 = [ a  b ;  b  c ]</text><rect x=\"20\" y=\"64\" width=\"200\" height=\"46\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"86.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Invert 2\u00d72 Matrix:\n\u03a3 = [ a b ; b c ]\u207b\u00b9 = \\frac{1}{ac - b\u00b2} [ c  -b ;  -b  a</text><text x=\"120.0\" y=\"94.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">]\nVar(X) = c / (ac - b\u00b2),   Var(Y) = a / (ac - b\u00b2),   Cov(X,Y) = -b / (ac - b\u00b2)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Read moments instantly without integration: off-diagonal in precision is b, not 2b</text></svg>",
    "drawingCaption": "The quadratic form in the exponent is the precision matrix \u03a3\u207b\u00b9; invert analytically to read all moments instantly",
    "coreTranslation": [
      "<strong>Exponent Identification:</strong> The exponent is $-\\frac{1}{2} (\\mathbf{x} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (\\mathbf{x} - \\boldsymbol{\\mu})$. The matrix of quadratic coefficients IS $\\Sigma^{-1}$!",
      "<strong>2D Analytical Inversion:</strong> If $\\Sigma^{-1} = \\begin{bmatrix} a & b \\\\ b & c \\end{bmatrix}$, then $\\Sigma = \\frac{1}{ac - b^2}\\begin{bmatrix} c & -b \\\\ -b & a \\end{bmatrix}$.",
      "<strong>Direct Moment Extraction:</strong> $\\operatorname{Var}(X) = \\frac{c}{ac - b^2}$, $\\operatorname{Var}(Y) = \\frac{a}{ac - b^2}$, and $\\operatorname{Cov}(X, Y) = \\frac{-b}{ac - b^2}$. Zero integration needed!"
    ],
    "math": "$$-\\frac{1}{2}\\begin{bmatrix}x \\\\ y\\end{bmatrix}^\\top \\begin{bmatrix}a & b \\\\ b & c\\end{bmatrix}\\begin{bmatrix}x \\\\ y\\end{bmatrix} \\implies \\Sigma = \\begin{bmatrix}a & b \\\\ b & c\\end{bmatrix}^{-1} = \\frac{1}{ac - b^2}\\begin{bmatrix}c & -b \\\\ -b & a\\end{bmatrix}$$",
    "personalConnection": "Reading an prescription bottle: the numbers in the quadratic exponent directly specify the precision matrix without needing to recalculate the volume.",
    "examTrap": "Forgetting the factor of 2 in cross-term 2b xy! The off-diagonal element of \u03a3\u207b\u00b9 is b, NOT 2b. The matrix must be symmetric."
  },
  {
    "id": 31306,
    "subject": "StoMA",
    "topicId": "13_Jointly_Gaussian_Random_Variables",
    "topicTitle": "13 \u00b7 Jointly Gaussian Random Variables",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Marginally Normal \u2260 Jointly Normal (Y = S \u00b7 X)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31306\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31306)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31306)\"/><line x1=\"50\" y1=\"100\" x2=\"190\" y2=\"30\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"50\" y1=\"30\" x2=\"190\" y2=\"100\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"180\" y=\"25\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Y = X</text><text x=\"180\" y=\"108\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Y = -X</text><rect x=\"24\" y=\"20\" width=\"100\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"74.0\" y=\"41.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X ~ N(0, 1)\nS = \u00b11 (p = 1/2)\nY</text><text x=\"74.0\" y=\"49.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= S \u00b7 X ~ N(0, 1)\nCov(X, Y) = 0</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Both X, Y ~ N(0, 1) and Cov=0, but P(X+Y=0)=1/2 \u21d2 NOT jointly Gaussian!</text></svg>",
    "drawingCaption": "Classic counterexample: X and Y are each standard normal and uncorrelated, yet completely dependent and not jointly Gaussian",
    "coreTranslation": [
      "<strong>Setup:</strong> Let $X \\sim \\mathcal{N}(0, 1)$ and let $S \\in \\{-1, +1\\}$ with $\\mathbb{P}(S = 1) = \\mathbb{P}(S = -1) = 1/2$ independently of $X$. Define $Y = S \\cdot X$.",
      "<strong>Marginal Normality & Zero Covariance:</strong> By symmetry, $Y \\sim \\mathcal{N}(0, 1)$ and $\\operatorname{Cov}(X, Y) = \\mathbb{E}[S X^2] = \\mathbb{E}[S]\\mathbb{E}[X^2] = 0(1) = 0$.",
      "<strong>Non-Gaussian Joint Law:</strong> The sum $X + Y = X(1 + S)$ equals $2X$ with probability $1/2$, and equals $0$ with probability $1/2$. It has atom $\\mathbb{P}(X + Y = 0) = 1/2$, so $X+Y$ is NOT normal $\\implies (X, Y)$ is NOT jointly Gaussian!"
    ],
    "math": "$$X, Y \\sim \\mathcal{N}(0, 1), \\quad \\operatorname{Cov}(X, Y) = 0, \\quad \\text{yet } \\mathbb{P}(X + Y = 0) = \\tfrac{1}{2} \\implies (X, Y) \\text{ NOT jointly Gaussian!}$$",
    "personalConnection": "An 'X'-shaped target: projection onto either coordinate axis produces a smooth Gaussian shadow, but projection along the diagonal reveals a sharp 50% spike at the origin.",
    "examTrap": "Concluding independence because Cov(X, Y) = 0! They are uncorrelated, but |Y| = |X| (complete deterministic dependence). Joint normality is strictly required for uncorrelated \u21d4 independent."
  },
  {
    "id": 31401,
    "subject": "StoMA",
    "topicId": "14_Random_Sums_and_Walds_Equation",
    "topicTitle": "14 \u00b7 Random Sums & Wald\u2019s Identity",
    "cardNumber": "01",
    "category": "RANDOM SUMS",
    "highlighterClass": "highlight-cyan",
    "title": "Random Sums S_N = \u2211_{i=1}^N X_i & Stopping Times",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31401\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"72\" x2=\"220\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.8\"/><circle cx=\"35\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"35\" y=\"58\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X\u2081</text><circle cx=\"70\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"70\" y=\"58\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X\u2082</text><circle cx=\"105\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"105\" y=\"58\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X\u2083</text><circle cx=\"140\" cy=\"72\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"140\" y=\"58\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">...</text><circle cx=\"175\" cy=\"72\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"175\" y=\"58\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X_N</text><line x1=\"175\" y1=\"35\" x2=\"175\" y2=\"105\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"3 3\"/><text x=\"175\" y=\"26\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Stop N</text><rect x=\"24\" y=\"90\" width=\"192\" height=\"32\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"105.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">S_N = \u2211_{i=1}^\u221e X\u1d62 \u00b7 1_{N \u2265 i}\nEvent {N</text><text x=\"120.0\" y=\"113.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2265 i} = {N \u2264 i-1}\u1d9c is independent of X\u1d62!</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Stopping time N depends only on past history X\u2081, ..., X_{i-1}; no future peering</text></svg>",
    "drawingCaption": "Random sums add a stochastic number of terms N; stopping times decide to halt without peering into the future",
    "coreTranslation": [
      "<strong>Random Sum Formulation:</strong> For i.i.d. $X_i$ with mean $\\mu$ and variance $\\sigma^2$, $S_N = \\sum_{i=1}^N X_i$ sums a random integer number of terms $N \\in \\mathbb{N}_0$.",
      "<strong>Stopping Time Condition:</strong> $N$ is a stopping time with respect to filtration $\\mathcal{F}_n = \\sigma(X_1, \\dots, X_n)$ if $\\{N = n\\} \\in \\mathcal{F}_n$ for all $n$ (halting rule does NOT depend on future outcomes).",
      "<strong>Indicator Independence:</strong> $S_N = \\sum_{i=1}^\\infty X_i \\mathbf{1}_{\\{N \\ge i\\}}$. Crucially, event $\\{N \\ge i\\} = \\{N \\le i-1\\}^c$ depends only on $X_1, \\dots, X_{i-1}$, and is therefore independent of $X_i$."
    ],
    "math": "$$S_N = \\sum_{i=1}^N X_i = \\sum_{i=1}^\\infty X_i\\,\\mathbf{1}_{\\{N \\ge i\\}}, \\qquad \\{N \\ge i\\} \\in \\sigma(X_1, \\dots, X_{i-1}) \\implies \\mathbf{1}_{\\{N \\ge i\\}} \\perp X_i$$",
    "personalConnection": "Blackjack card strategy: deciding whether to draw another card based on your current hand is a stopping time; stopping when the next card would bust you is clairvoyant and impossible.",
    "examTrap": "Applying Wald's identities when N looks into the future! For example, N = argmax_{1 \u2264 i \u2264 5} X_i depends on future terms; Wald's equation fails completely for anticipatory stopping rules."
  },
  {
    "id": 31402,
    "subject": "StoMA",
    "topicId": "14_Random_Sums_and_Walds_Equation",
    "topicTitle": "14 \u00b7 Random Sums & Wald\u2019s Identity",
    "cardNumber": "02",
    "category": "WALD IDENTITIES",
    "highlighterClass": "highlight-amber",
    "title": "Wald\u2019s First Identity: E[S_N] = E[N] \u00b7 E[X]",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31402\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"192\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"41.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Wald's First Identity (Wald's Equation):\nE[ S_N ] = E[N] \u00b7</text><text x=\"120.0\" y=\"50.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[X]\n(Valid for any stopping time with E[N] &lt; \u221e, E[|X|] &lt; \u221e)</text><rect x=\"24\" y=\"72\" width=\"192\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"92.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Indicator Proof:\nE[S_N] = \u2211 E[X\u1d62 1_{N \u2265 i}] = \u2211 E[X\u1d62]</text><text x=\"120.0\" y=\"100.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(N \u2265 i)\n= E[X] \u2211 P(N \u2265 i) = E[X] E[N]  (via tail sum!)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Expected total payout equals expected count E[N] times expected cost per event E[X]</text></svg>",
    "drawingCaption": "The expected value of a random sum equals the expected number of terms times the expected individual value",
    "coreTranslation": [
      "<strong>Theorem Statement:</strong> If $X_i$ are i.i.d. with $\\mathbb{E}[|X|] < \\infty$ and $N$ is a stopping time with $\\mathbb{E}[N] < \\infty$, then $\\mathbb{E}[S_N] = \\mathbb{E}[N]\\,\\mathbb{E}[X]$.",
      "<strong>Indicator Proof:</strong> $\\mathbb{E}[S_N] = \\mathbb{E}[\\sum_{i=1}^\\infty X_i \\mathbf{1}_{\\{N \\ge i\\}}] = \\sum_{i=1}^\\infty \\mathbb{E}[X_i] \\mathbb{P}(N \\ge i) = \\mathbb{E}[X] \\sum_{i=1}^\\infty \\mathbb{P}(N \\ge i) = \\mathbb{E}[X]\\mathbb{E}[N]$.",
      "<strong>Tower Proof (if $N \\perp X$):</strong> By the law of total expectation, $\\mathbb{E}[S_N] = \\mathbb{E}[\\mathbb{E}[S_N \\mid N]] = \\mathbb{E}[N \\mathbb{E}[X]] = \\mathbb{E}[N]\\,\\mathbb{E}[X]$."
    ],
    "math": "$$\\mathbb{E}\\left[\\sum_{i=1}^N X_i\\right] = \\mathbb{E}[N]\\,\\mathbb{E}[X], \\quad \\text{provided } \\mathbb{E}[N] < \\infty, \\; \\mathbb{E}[|X|] < \\infty$$",
    "personalConnection": "Hospital emergency room: an average of E[N] = 40 patients arrive per day, each incurring an average treatment cost of E[X] = $1,500; total expected daily expenditure is $60,000.",
    "examTrap": "Ignoring integrability conditions: if E[N] = \u221e or E[|X|] = \u221e, Wald's equation breaks down and can yield undefined \u221e \u00d7 0 forms."
  },
  {
    "id": 31403,
    "subject": "StoMA",
    "topicId": "14_Random_Sums_and_Walds_Equation",
    "topicTitle": "14 \u00b7 Random Sums & Wald\u2019s Identity",
    "cardNumber": "03",
    "category": "WALD IDENTITIES",
    "highlighterClass": "highlight-emerald",
    "title": "Wald\u2019s Second Identity: Two-Source Variance Decomposition",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31403\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"37.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Wald's Second Identity:\nVar(S_N)</text><text x=\"120.0\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= E[N] Var(X) + (E[X])\u00b2 Var(N)</text><rect x=\"20\" y=\"62\" width=\"96\" height=\"46\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"68.0\" y=\"84.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[ Var(S_N | N) ]\n= E[N \u03c3\u00b2]\n=</text><text x=\"68.0\" y=\"92.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[N] Var(X)\n(Claim variability)</text><rect x=\"124\" y=\"62\" width=\"96\" height=\"46\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"172.0\" y=\"84.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var( E[S_N | N] )\n= Var(N \u03bc)\n=</text><text x=\"172.0\" y=\"92.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc\u00b2 Var(N)\n(Count variability)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Two variance sources: randomness in each step PLUS randomness in the total number of steps</text></svg>",
    "drawingCaption": "The variance of a random sum combines individual claim variability with count volatility via Eve\u2019s Law",
    "coreTranslation": [
      "<strong>Identity Statement:</strong> If $N$ is independent of i.i.d. $X_i$ with finite variances, $\\operatorname{Var}(S_N) = \\mathbb{E}[N]\\operatorname{Var}(X) + (\\mathbb{E}[X])^2 \\operatorname{Var}(N)$.",
      "<strong>Derivation via Total Variance:</strong> $\\operatorname{Var}(S_N) = \\mathbb{E}[\\operatorname{Var}(S_N \\mid N)] + \\operatorname{Var}(\\mathbb{E}[S_N \\mid N]) = \\mathbb{E}[N\\sigma^2] + \\operatorname{Var}(N\\mu) = \\mathbb{E}[N]\\sigma^2 + \\mu^2 \\operatorname{Var}(N)$.",
      "<strong>Zero-Mean Simplification:</strong> If $\\mathbb{E}[X] = 0$, the second term vanishes: $\\operatorname{Var}(S_N) = \\mathbb{E}[N]\\operatorname{Var}(X)$ (holds even when $N$ is a general stopping time)."
    ],
    "math": "$$\\operatorname{Var}\\left(\\sum_{i=1}^N X_i\\right) = \\mathbb{E}[N]\\operatorname{Var}(X) + \\left(\\mathbb{E}[X]\\right)^2 \\operatorname{Var}(N)$$",
    "personalConnection": "Retail inventory risk: total weekly revenue variance stems from two distinct drivers: fluctuating customer foot traffic Var(N) and fluctuating basket size Var(X).",
    "examTrap": "Using Var(S_N) = E[N]Var(X)! Omitting the second term \u03bc\u00b2 Var(N) severely underestimates risk whenever mean E[X] is non-zero."
  },
  {
    "id": 31404,
    "subject": "StoMA",
    "topicId": "14_Random_Sums_and_Walds_Equation",
    "topicTitle": "14 \u00b7 Random Sums & Wald\u2019s Identity",
    "cardNumber": "04",
    "category": "COMPOUND DISTRIBUTIONS",
    "highlighterClass": "highlight-purple",
    "title": "Compound Distributions: Functional Composition of PGFs & MGFs",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31404\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"192\" height=\"40\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Compound MGF:  M_{S_N}(t) = G_N( M_X(t) ) = M_N( ln M_X(t)</text><text x=\"120.0\" y=\"48.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">)\n(Outer function is counter N; inner function is term X)</text><rect x=\"24\" y=\"68\" width=\"192\" height=\"40\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"87.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Compound PGF:  G_{S_N}(s) = G_N( G_X(s) )   [for X\u1d62 \u2208</text><text x=\"120.0\" y=\"96.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2115\u2080]\n(Functional composition evaluates all higher moments)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Functional composition: nested generating functions mirror the nested nature of random sums</text></svg>",
    "drawingCaption": "The generating function of a random sum is the functional composition of the parent and offspring generators",
    "coreTranslation": [
      "<strong>Compound MGF:</strong> $M_{S_N}(t) \\triangleq \\mathbb{E}[e^{t S_N}] = \\mathbb{E}[\\mathbb{E}[e^{t \\sum X_i} \\mid N]] = \\mathbb{E}[(M_X(t))^N] = G_N(M_X(t))$.",
      "<strong>Compound PGF:</strong> For discrete non-negative integer RVs $X_i \\in \\mathbb{N}_0$, $G_{S_N}(s) \\triangleq \\mathbb{E}[s^{S_N}] = G_N(G_X(s))$ (exact nested functional composition).",
      "<strong>Cumulant Generating Function:</strong> $\\log M_{S_N}(t) = \\log G_N(M_X(t))$. Successive derivatives at $t=0$ generate all higher-order cumulants and skewness."
    ],
    "math": "$$M_{S_N}(t) = G_N\\left(M_X(t)\\right), \\qquad G_{S_N}(s) = G_N\\left(G_X(s)\\right) \\quad (X_i \\in \\mathbb{N}_0)$$",
    "personalConnection": "Russian nesting dolls (Matryoshka): the offspring generating function G_X(s) is packed inside the population count doll G_N.",
    "examTrap": "Swapping the composition order: writing M_X(G_N(t)) instead of G_N(M_X(t))! The outer function is always the counter N; the inner function is the term X."
  },
  {
    "id": 31405,
    "subject": "StoMA",
    "topicId": "14_Random_Sums_and_Walds_Equation",
    "topicTitle": "14 \u00b7 Random Sums & Wald\u2019s Identity",
    "cardNumber": "05",
    "category": "BRANCHING PROCESSES",
    "highlighterClass": "highlight-cyan",
    "title": "Galton-Watson Branching Processes & Extinction Probability",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31405\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"120\" cy=\"20\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"10\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Z\u2080 = 1</text><line x1=\"120\" y1=\"20\" x2=\"70\" y2=\"50\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"120\" y1=\"20\" x2=\"170\" y2=\"50\" stroke=\"#000000\" stroke-width=\"1.2\"/><circle cx=\"70\" cy=\"50\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"170\" cy=\"50\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"50\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Z\u2081 ~ \u03be</text><line x1=\"70\" y1=\"50\" x2=\"45\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.0\"/><line x1=\"70\" y1=\"50\" x2=\"95\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.0\"/><line x1=\"170\" y1=\"50\" x2=\"170\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.0\"/><circle cx=\"45\" cy=\"80\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"95\" cy=\"80\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"170\" cy=\"80\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"80\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Z\u2082</text><rect x=\"24\" y=\"96\" width=\"192\" height=\"28\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"109.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[Z_n] = \u03bc\u207f (\u03bc = E[\u03be]);  Extinction</text><text x=\"120.0\" y=\"118.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c0\u2080 = min{s \u2208 [0, 1] : s = G_\u03be(s)}</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Branching process: Subcritical \u03bc &lt; 1 \u21d2 \u03c0\u2080 = 1; Supercritical \u03bc > 1 \u21d2 \u03c0\u2080 &lt; 1</text></svg>",
    "drawingCaption": "Population grows geometrically as E[Z_n] = \u03bc\u207f; extinction probability \u03c0\u2080 is the smallest root of s = G_\u03be(s)",
    "coreTranslation": [
      "<strong>Model Formulation:</strong> $Z_0 = 1$. Generation $n+1$ has size $Z_{n+1} = \\sum_{i=1}^{Z_n} \\xi_{n,i}$ where $\\xi_{n,i} \\stackrel{\\text{i.i.d.}}{\\sim} \\xi$. By Wald's equation, $\\mathbb{E}[Z_n] = \\mu^n$ with $\\mu = \\mathbb{E}[\\xi]$.",
      "<strong>Phase Transition:</strong> (1) If $\\mu < 1$ (subcritical) or $\\mu = 1$ (critical, $\\xi \\not\\equiv 1$), extinction is CERTAIN: $\\pi_0 = 1$; (2) If $\\mu > 1$ (supercritical), survival is possible: $\\pi_0 < 1$.",
      "<strong>Fixed-Point Theorem:</strong> The extinction probability $\\pi_0 = \\mathbb{P}(\\lim Z_n = 0)$ is the SMALLEST non-negative root of the fixed-point equation $s = G_\\xi(s)$ in $[0, 1]$."
    ],
    "math": "$$\\mathbb{E}[Z_n] = \\mu^n \\quad (\\mu = \\mathbb{E}[\\xi]); \\qquad \\pi_0 = \\min \\{s \\in [0, 1] : s = G_\\xi(s)\\}$$",
    "personalConnection": "Viral chain reaction: if basic reproduction number R\u2080 = \u03bc is below 1, the epidemic dies out with 100% certainty; if R\u2080 > 1, the disease has a non-zero probability of permanent endemic survival.",
    "examTrap": "Selecting the trivial root s = 1 when solving s = G(s). The root s = 1 is always a mathematical solution (G(1)=1); the true extinction probability is the SMALLEST root in [0, 1]."
  },
  {
    "id": 31406,
    "subject": "StoMA",
    "topicId": "14_Random_Sums_and_Walds_Equation",
    "topicTitle": "14 \u00b7 Random Sums & Wald\u2019s Identity",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Compound Poisson Claims (The Lundberg Model)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31406\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31406)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31406)\"/><line x1=\"24\" y1=\"110\" x2=\"65\" y2=\"110\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"65\" y1=\"110\" x2=\"65\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.8\"/><circle cx=\"65\" cy=\"80\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"65\" y=\"70\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X\u2081</text><line x1=\"65\" y1=\"80\" x2=\"120\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"120\" y1=\"80\" x2=\"120\" y2=\"45\" stroke=\"#000000\" stroke-width=\"1.8\"/><circle cx=\"120\" cy=\"45\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"35\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">X\u2082</text><line x1=\"120\" y1=\"45\" x2=\"185\" y2=\"45\" stroke=\"#000000\" stroke-width=\"1.8\"/><rect x=\"130\" y=\"60\" width=\"96\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"178.0\" y=\"81.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">N ~ Pois(\u03bb), X\u1d62 ~ Exp(\u03b2)\nE[S_N] =</text><text x=\"178.0\" y=\"89.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bb / \u03b2\nVar(S_N) = 2\u03bb / \u03b2\u00b2 = \u03bb E[X\u00b2]</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Compound Poisson variance: Var(S_N) = \u03bb E[X\u00b2]; count volatility doubles the total variance</text></svg>",
    "drawingCaption": "For compound Poisson processes, total variance equals rate \u03bb times second moment E[X\u00b2]: Var(S_N) = \u03bb E[X\u00b2]",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Claim count $N \\sim \\text{Poisson}(\\lambda)$ (so $\\mathbb{E}[N] = \\lambda, \\operatorname{Var}(N) = \\lambda$). Individual claim amounts $X_i \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Exp}(\\beta)$ with mean $1/\\beta$ and variance $1/\\beta^2$.",
      "<strong>Expected Total Claim:</strong> $\\mathbb{E}[S_N] = \\mathbb{E}[N]\\mathbb{E}[X] = \\lambda \\cdot \\frac{1}{\\beta} = \\frac{\\lambda}{\\beta}$.",
      "<strong>Aggregate Variance:</strong> $\\operatorname{Var}(S_N) = \\lambda(1/\\beta^2) + (1/\\beta)^2 \\lambda = \\frac{2\\lambda}{\\beta^2} = \\lambda \\mathbb{E}[X^2]$. For ANY compound Poisson sum, $\\operatorname{Var}(S_N) = \\lambda \\mathbb{E}[X^2]$!"
    ],
    "math": "$$N \\sim \\text{Pois}(\\lambda) \\implies \\mathbb{E}[S_N] = \\lambda \\mathbb{E}[X], \\qquad \\operatorname{Var}(S_N) = \\lambda \\mathbb{E}[X^2] = \\frac{2\\lambda}{\\beta^2}$$",
    "personalConnection": "Insurance reserve solvency: premium inflows arrive continuously while claim payouts arrive in sudden random compound Poisson jumps, requiring reserves calibrated to \u03bb E[X\u00b2].",
    "examTrap": "Omitting the count variance term: calculating Var(S_N) = \u03bb / \u03b2\u00b2 by treating N as a constant! Because Var(N) = \u03bb, the second term adds another \u03bb/\u03b2\u00b2, exactly doubling the variance."
  },
  {
    "id": 31501,
    "subject": "StoMA",
    "topicId": "15_Modes_of_Convergence_and_Relations",
    "topicTitle": "15 \u00b7 Modes of Convergence",
    "cardNumber": "01",
    "category": "CONVERGENCE MODES",
    "highlighterClass": "highlight-cyan",
    "title": "The Four Modes of Stochastic Convergence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31501\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"60\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"46.0\" y=\"33.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Almost Sure\nX_n</text><text x=\"46.0\" y=\"42.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2192^{a.s.} X</text><line x1=\"76\" y1=\"34\" x2=\"100\" y2=\"34\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31501)\"/><rect x=\"100\" y=\"20\" width=\"60\" height=\"28\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"130.0\" y=\"33.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Probability\nX_n</text><text x=\"130.0\" y=\"42.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2192^{P} X</text><line x1=\"160\" y1=\"34\" x2=\"184\" y2=\"34\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31501)\"/><rect x=\"184\" y=\"20\" width=\"48\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"208.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Dist.\n\u2192^{d}</text><rect x=\"100\" y=\"72\" width=\"60\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"130.0\" y=\"85.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">L^p Mean\nX_n</text><text x=\"130.0\" y=\"94.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2192^{L^p} X</text><line x1=\"130\" y1=\"72\" x2=\"130\" y2=\"48\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31501)\"/><text x=\"145\" y=\"60\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">p \u2265 1</text><text x=\"120\" y=\"118\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Hierarchy: a.s. \u21d2 P \u21d2 d;   L^p \u21d2 L^r \u21d2 P (p > r \u2265 1)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Four distinct topology strengths: a.s. is pointwise almost everywhere; d only matches CDFs</text></svg>",
    "drawingCaption": "The fundamental implication hierarchy: Almost Sure implies Probability implies Distribution; L^p implies Probability",
    "coreTranslation": [
      "<strong>Almost Sure ($X_n \\xrightarrow{a.s.} X$):</strong> $\\mathbb{P}(\\{\\omega : \\lim X_n(\\omega) = X(\\omega)\\}) = 1$ (pointwise path convergence for 100% of outcomes).",
      "<strong>In Probability ($X_n \\xrightarrow{P} X$):</strong> $\\lim_{n \\to \\infty} \\mathbb{P}(|X_n - X| \\ge \\epsilon) = 0$ for all $\\epsilon > 0$ (probability of error vanishes).",
      "<strong>In $L^p$ Mean & Distribution:</strong> In $L^p$: $\\lim \\mathbb{E}[|X_n - X|^p] = 0$. In Distribution ($X_n \\xrightarrow{d} X$): $\\lim F_{X_n}(x) = F_X(x)$ at all continuity points of $F_X$ (weakest mode)."
    ],
    "math": "$$X_n \\xrightarrow{a.s.} X \\implies X_n \\xrightarrow{P} X \\implies X_n \\xrightarrow{d} X; \\qquad X_n \\xrightarrow{L^p} X \\implies X_n \\xrightarrow{L^r} X \\implies X_n \\xrightarrow{P} X \\quad (p > r)$$",
    "personalConnection": "Target archery: almost sure means every arrow lands closer and closer to center; probability allows rare wild shots with vanishing likelihood; distribution means only the spray pattern matches the target.",
    "examTrap": "Assuming convergence in distribution requires a shared sample space! X_n \u2192^d X depends ONLY on CDFs; variables can be defined on completely unrelated probability spaces."
  },
  {
    "id": 31502,
    "subject": "StoMA",
    "topicId": "15_Modes_of_Convergence_and_Relations",
    "topicTitle": "15 \u00b7 Modes of Convergence",
    "cardNumber": "02",
    "category": "CONVERGENCE HIERARCHY",
    "highlighterClass": "highlight-amber",
    "title": "Implication Hierarchy & When the Reverses Hold",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31502\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"32\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"35.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Bridge 1: X_n \u2192^{d} c </text><text x=\"120.0\" y=\"44.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(Constant limit)  \u21d4  X_n \u2192^{P} c</text><rect x=\"20\" y=\"56\" width=\"200\" height=\"32\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"71.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Bridge 2: X_n \u2192^{P} X  AND  |X_n| \u2264 Y</text><text x=\"120.0\" y=\"80.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">with E[Y^p]&lt;\u221e  \u21d2  X_n \u2192^{L^p} X (DCT)</text><rect x=\"20\" y=\"92\" width=\"200\" height=\"32\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"107.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Bridge 3: X_n \u2192^{P} X  \u21d2  \u2203 Subsequence</text><text x=\"120.0\" y=\"116.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">{n_k} s.t. X_{n_k} \u2192^{a.s.} X</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Reverses fail in general, but hold under constant limits, domination, and subsequences</text></svg>",
    "drawingCaption": "Reverses fail in general, but hold under constant limits, Dominated Convergence (DCT), and subsequences",
    "coreTranslation": [
      "<strong>Constant Limit Bridge:</strong> If $X_n \\xrightarrow{d} c$ where $c$ is a deterministic CONSTANT, then $X_n \\xrightarrow{P} c$ (distribution convergence promotes to probability convergence).",
      "<strong>Dominated Convergence Bridge:</strong> If $X_n \\xrightarrow{P} X$ and $|X_n| \\le Y$ with $\\mathbb{E}[Y^p] < \\infty$, then $X_n \\xrightarrow{L^p} X$ (Lebesgue Dominated Convergence Theorem).",
      "<strong>Subsequential Bridge:</strong> If $X_n \\xrightarrow{P} X$, there exists a SUBSEQUENCE $\\{n_k\\}$ such that $X_{n_k} \\xrightarrow{a.s.} X$."
    ],
    "math": "$$X_n \\xrightarrow{d} c \\iff X_n \\xrightarrow{P} c \\quad (c \\text{ constant}); \\qquad X_n \\xrightarrow{P} X \\implies \\exists \\{n_k\\} \\text{ s.t. } X_{n_k} \\xrightarrow{a.s.} X$$",
    "personalConnection": "Refining an optical focus: coarse adjustment (d) generally cannot ensure sharp paths (a.s.), but if you restrict to a target landmark (constant), coarse focus coincides with fine focus.",
    "examTrap": "Assuming X_n \u2192^d X implies X_n \u2192^P X for non-constant X! E.g. let X ~ N(0, 1) and X_n = -X. Then X_n has the same normal distribution, but X_n - X = -2X never converges to 0."
  },
  {
    "id": 31503,
    "subject": "StoMA",
    "topicId": "15_Modes_of_Convergence_and_Relations",
    "topicTitle": "15 \u00b7 Modes of Convergence",
    "cardNumber": "03",
    "category": "COUNTEREXAMPLE",
    "highlighterClass": "highlight-emerald",
    "title": "The Sliding Typewriter: Convergence in Probability \u2260 Almost Sure",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31503\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"35\" x2=\"220\" y2=\"35\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"20\" y=\"48\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><text x=\"220\" y=\"48\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><rect x=\"20\" y=\"26\" width=\"100\" height=\"18\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"70\" y=\"37\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">I\u2081 = [0, 1/2]</text><line x1=\"20\" y1=\"70\" x2=\"220\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.4\"/><rect x=\"120\" y=\"61\" width=\"100\" height=\"18\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"170\" y=\"72\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">I\u2082 = [1/2, 1]</text><line x1=\"20\" y1=\"105\" x2=\"220\" y2=\"105\" stroke=\"#000000\" stroke-width=\"1.4\"/><rect x=\"20\" y=\"96\" width=\"67\" height=\"18\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"53\" y=\"107\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">I\u2083 = [0, 1/3]</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Typewriter sweeps endlessly: P(X_n = 1) = 1/k \u2192 0 (in P), yet limsup X_n(\u03c9) = 1 \u2200\u03c9 (not a.s.)</text></svg>",
    "drawingCaption": "Indicator intervals of shrinking width sweep endlessly across [0, 1]: converges in probability, but diverges almost surely",
    "coreTranslation": [
      "<strong>Typewriter Construction:</strong> On $\\Omega = [0, 1]$ with uniform Lebesgue measure. Let $X_n = \\mathbf{1}_{I_n}$ where intervals $I_n$ of width $1/k$ sweep from left to right across $[0, 1]$ repeatedly.",
      "<strong>Convergence in Probability:</strong> $\\mathbb{P}(|X_n| \\ge \\epsilon) = \\text{Length}(I_n) = 1/k \\to 0$, so $X_n \\xrightarrow{P} 0$.",
      "<strong>Almost Sure Divergence:</strong> Because the intervals sweep past every point $\\omega \\in [0, 1]$ infinitely many times, the sequence of values $X_n(\\omega)$ oscillates between $0$ and $1$ forever for EVERY $\\omega$. Thus $\\mathbb{P}(\\lim X_n = 0) = 0$!"
    ],
    "math": "$$\\mathbb{P}(X_n = 1) = \\frac{1}{k} \\to 0 \\implies X_n \\xrightarrow{P} 0, \\quad \\text{yet } \\limsup_{n \\to \\infty} X_n(\\omega) = 1 \\quad \\forall \\omega \\implies X_n \\not\\xrightarrow{a.s.} 0$$",
    "personalConnection": "A sweeping radar beam: the beam gets thinner and thinner over time (prob \u2192 0), but because it never stops rotating, every target on the radar screen is illuminated periodically forever.",
    "examTrap": "Assuming that P(|X_n| \u2265 \u03b5) \u2192 0 guarantees sample paths settle down. Probability measures only instantaneous mass size; almost sure convergence requires mass to stop wandering across points."
  },
  {
    "id": 31504,
    "subject": "StoMA",
    "topicId": "15_Modes_of_Convergence_and_Relations",
    "topicTitle": "15 \u00b7 Modes of Convergence",
    "cardNumber": "04",
    "category": "COUNTEREXAMPLE",
    "highlighterClass": "highlight-purple",
    "title": "The Escaping Spike: Almost Sure Convergence \u2260 L^p Convergence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31504\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31504)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31504)\"/><line x1=\"160\" y1=\"114\" x2=\"160\" y2=\"30\" stroke=\"#000000\" stroke-width=\"2.2\"/><circle cx=\"160\" cy=\"30\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"160\" y=\"20\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Height = n\u00b2</text><text x=\"160\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">n\u00b2</text><rect x=\"24\" y=\"20\" width=\"110\" height=\"48\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"79.0\" y=\"43.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(X_n = n\u00b2) = 1/n\nP(X_n = 0) = 1 -</text><text x=\"79.0\" y=\"51.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1/n\nX_n(\u03c9) \u2192 0 a.s.\nE[X_n] = n\u00b2(1/n) = n \u2192 \u221e!</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Escaping spike: X_n \u2192 0 a.s., but E[X_n] = n \u2192 \u221e diverges completely (fails L\u00b9)</text></svg>",
    "drawingCaption": "A spike of height n\u00b2 with probability 1/n vanishes almost surely, but its expectation diverges to infinity",
    "coreTranslation": [
      "<strong>Spike Construction:</strong> Let $\\mathbb{P}(X_n = n^2) = 1/n$ and $\\mathbb{P}(X_n = 0) = 1 - 1/n$.",
      "<strong>Almost Sure Zero:</strong> By Borel-Cantelli (using independent trials with $\\sum 1/n^2 < \\infty$), for almost every $\\omega$, $X_n(\\omega) = 0$ for all sufficiently large $n$, so $X_n \\xrightarrow{a.s.} 0$.",
      "<strong>$L^1$ Mean Explosion:</strong> $\\mathbb{E}[|X_n|] = n^2 \\cdot \\frac{1}{n} = n \\to \\infty$. The expectation explodes to infinity even though the variable is zero almost surely!"
    ],
    "math": "$$X_n(\\omega) \\to 0 \\text{ a.s.}, \\quad \\text{yet } \\mathbb{E}[|X_n|] = n \\to \\infty \\implies X_n \\not\\xrightarrow{L^1} 0$$",
    "personalConnection": "A runaway lottery jackpot: the probability of winning shrinks toward zero, but the jackpot prize grows so exponentially that the expected ticket payout explodes to infinity.",
    "examTrap": "Assuming almost sure convergence allows exchanging limit and expectation: lim E[X_n] = E[lim X_n] strictly requires Uniform Integrability or a Dominated Bound (DCT)."
  },
  {
    "id": 31505,
    "subject": "StoMA",
    "topicId": "15_Modes_of_Convergence_and_Relations",
    "topicTitle": "15 \u00b7 Modes of Convergence",
    "cardNumber": "05",
    "category": "ASYMPTOTIC ALGEBRA",
    "highlighterClass": "highlight-cyan",
    "title": "Slutsky\u2019s Theorem & The Continuous Mapping Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31505\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"208\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"33.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Continuous Mapping (CMT):  X_n \u2192 X </text><text x=\"120.0\" y=\"42.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u21d2  g(X_n) \u2192 g(X)  (for continuous g)</text><rect x=\"16\" y=\"54\" width=\"208\" height=\"30\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"68.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Slutsky: X_n \u2192^{d} X   and   Y_n \u2192^{P} c (Constant</text><text x=\"120.0\" y=\"77.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">c)\n(1) X_n + Y_n \u2192^{d} X + c,    (2) X_n \u00b7 Y_n \u2192^{d} c X</text><rect x=\"16\" y=\"90\" width=\"208\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"103.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Ratio Law: X_n / Y_n \u2192^{d}</text><text x=\"120.0\" y=\"112.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">X / c   (for constant c \u2260 0)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Slutsky enables asymptotic hypothesis testing: plug in consistent estimators Y_n \u2192^P c</text></svg>",
    "drawingCaption": "Slutsky preserves distribution convergence under algebraic operations when the second variable converges in probability to a constant",
    "coreTranslation": [
      "<strong>Continuous Mapping Theorem (CMT):</strong> If $X_n \\to X$ in mode (a.s., $P$, or $d$) and $g$ is continuous, then $g(X_n) \\to g(X)$ in the SAME mode.",
      "<strong>Slutsky\u2019s Theorem:</strong> If $X_n \\xrightarrow{d} X$ and $Y_n \\xrightarrow{P} c$ (where $c$ is a deterministic constant): (1) $X_n + Y_n \\xrightarrow{d} X + c$; (2) $X_n Y_n \\xrightarrow{d} c X$; (3) $X_n / Y_n \\xrightarrow{d} X / c$ (if $c \\ne 0$).",
      "<strong>Statistical Powerhouse:</strong> Slutsky allows replacing unknown nuisance parameters (like population variance $\\sigma$) with consistent sample estimates $S_n \\xrightarrow{P} \\sigma$."
    ],
    "math": "$$X_n \\xrightarrow{d} X, \\; Y_n \\xrightarrow{P} c \\implies X_n Y_n \\xrightarrow{d} cX, \\quad \\frac{X_n}{Y_n} \\xrightarrow{d} \\frac{X}{c} \\quad (c \\ne 0)$$",
    "personalConnection": "Calibrating a precision laboratory balance: if your object weight error is Gaussian (X_n \u2192^d N), and tare calibration offset converges to true constant c (Y_n \u2192^P c), total reading error is N + c.",
    "examTrap": "Applying Slutsky when Y_n \u2192^d Y with non-constant Y! If Y is random, X_n + Y_n does NOT necessarily converge to X + Y because distribution convergence tells you nothing about mutual joint alignment."
  },
  {
    "id": 31506,
    "subject": "StoMA",
    "topicId": "15_Modes_of_Convergence_and_Relations",
    "topicTitle": "15 \u00b7 Modes of Convergence",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Asymptotic Normality of Student's t-Statistic",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31506\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"208\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Student's t-Statistic:  T_n = \\frac{\\sqrt{n}(\\bar{X}_n - \u03bc)}{S_n} = \\frac{\\frac{\\sqrt{n}(\\bar{X}_n -</text><text x=\"120.0\" y=\"48.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc)}{\u03c3}}{\\frac{S_n}{\u03c3}}\nNumerator: Z_n \u2192^{d} N(0, 1)  (by Central Limit Theorem)\nDenominator: S_n / \u03c3 \u2192^{P} 1  (by WLLN + CMT)</text><rect x=\"16\" y=\"68\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Apply Slutsky (Ratio with c = 1):\nT_n = Z_n / (S_n/\u03c3)  \u2192^{d}  N(0, 1)</text><text x=\"120.0\" y=\"98.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">/ 1 = N(0, 1)\nStudent's t distribution collapses to Standard Normal!</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Asymptotic normality of Student's t: Slutsky proves T_n \u2192^d N(0, 1) as n \u2192 \u221e</text></svg>",
    "drawingCaption": "Slutsky proves that Student\u2019s t statistic converges in distribution to the standard normal as sample size grows",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> For i.i.d. $X_i \\sim (\\mu, \\sigma^2)$, test statistic is $T_n = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{S_n}$ where $S_n^2 = \\frac{1}{n-1}\\sum (X_i - \\bar{X}_n)^2$.",
      "<strong>Component Decomposition:</strong> Numerator $Z_n = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{\\sigma} \\xrightarrow{d} \\mathcal{N}(0, 1)$ by Central Limit Theorem. Denominator $\\frac{S_n}{\\sigma} \\xrightarrow{P} 1$ by WLLN and Continuous Mapping Theorem.",
      "<strong>Slutsky Ratio Law:</strong> By Slutsky's theorem with constant $c = 1$, $T_n = \\frac{Z_n}{S_n / \\sigma} \\xrightarrow{d} \\frac{\\mathcal{N}(0, 1)}{1} = \\mathcal{N}(0, 1)$. Student's $t$ statistic is asymptotically Gaussian!"
    ],
    "math": "$$T_n = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{S_n} = \\frac{\\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{\\sigma}}{\\frac{S_n}{\\sigma}} \\xrightarrow{d} \\frac{\\mathcal{N}(0, 1)}{1} = \\mathcal{N}(0, 1)$$",
    "personalConnection": "Industrial sample testing: when testing more than 30 samples (n > 30), Student's t critical values become virtually indistinguishable from standard normal z-scores.",
    "examTrap": "Assuming T_n is strictly Gaussian for finite n! T_n has heavier polynomial tails (Student's t) for finite n; it becomes Gaussian ONLY in the asymptotic limit n \u2192 \u221e."
  },
  {
    "id": 31601,
    "subject": "StoMA",
    "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
    "topicTitle": "16 \u00b7 Borel-Cantelli Lemmas & Limsup/Liminf",
    "cardNumber": "01",
    "category": "SET LIMITS",
    "highlighterClass": "highlight-cyan",
    "title": "Limsup (Infinitely Often) vs Liminf (All But Finitely Often)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31601\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"41.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">limsup A_n = {A_n i.o.} = \u22c2_{n=1}^\u221e \u22c3_{k=n}^\u221e</text><text x=\"120.0\" y=\"50.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A_k\n(Outcome \u03c9 occurs in infinitely many events A_n)</text><rect x=\"16\" y=\"70\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"91.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">liminf A_n = {A_n a.b.f.o.} = \u22c3_{n=1}^\u221e \u22c2_{k=n}^\u221e</text><text x=\"120.0\" y=\"100.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A_k\n(Outcome \u03c9 occurs in all but finitely many events A_n)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">De Morgan Duality: (limsup A_n)\u1d9c = liminf A_n\u1d9c; liminf A_n \u2286 limsup A_n always</text></svg>",
    "drawingCaption": "Limsup captures outcomes occurring infinitely often; Liminf captures outcomes occurring in all but finitely many events",
    "coreTranslation": [
      "<strong>Limsup Definition:</strong> $\\limsup_{n \\to \\infty} A_n \\triangleq \\bigcap_{n=1}^\\infty \\bigcup_{k=n}^\\infty A_k = \\{A_n \\text{ i.o.}\\}$ (infinitely often). $\\omega \\in \\limsup A_n \\iff \\omega$ belongs to infinitely many $A_n$.",
      "<strong>Liminf Definition:</strong> $\\liminf_{n \\to \\infty} A_n \\triangleq \\bigcup_{n=1}^\\infty \\bigcap_{k=n}^\\infty A_k = \\{A_n \\text{ a.b.f.o.}\\}$ (all but finitely often). $\\omega \\in \\liminf A_n \\iff \\exists N$ such that $\\omega \\in A_n$ for all $n \\ge N$.",
      "<strong>De Morgan Duality:</strong> $(\\limsup A_n)^c = \\liminf A_n^c$. Furthermore, $\\liminf A_n \\subseteq \\limsup A_n$ always holds."
    ],
    "math": "$$\\limsup_{n \\to \\infty} A_n = \\bigcap_{n=1}^\\infty \\bigcup_{k=n}^\\infty A_k = \\{A_n \\text{ i.o.}\\}, \\qquad \\left(\\limsup A_n\\right)^c = \\liminf A_n^c$$",
    "personalConnection": "Meteor showers: seeing shooting stars infinitely often (limsup) means they never permanently stop; seeing them in all but finitely many seconds (liminf) means they eventually become continuous.",
    "examTrap": "Swapping intersection and union! Limsup is intersection of unions (\u22c2 \u22c3); Liminf is union of intersections (\u22c3 \u22c2). Swapping them completely reverses their mathematical meaning."
  },
  {
    "id": 31602,
    "subject": "StoMA",
    "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
    "topicTitle": "16 \u00b7 Borel-Cantelli Lemmas & Limsup/Liminf",
    "cardNumber": "02",
    "category": "BOREL-CANTELLI 1",
    "highlighterClass": "highlight-amber",
    "title": "The First Borel-Cantelli Lemma: Sum P(A_n) < \u221e \u21d2 P(A_n i.o.) = 0",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31602\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"72.0\" y=\"37.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Finite Sum:\n\u2211_{n=1}^\u221e</text><text x=\"72.0\" y=\"47.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(A_n) &lt; \u221e</text><line x1=\"120\" y1=\"38\" x2=\"144\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31602)\"/><rect x=\"144\" y=\"20\" width=\"72\" height=\"36\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"180.0\" y=\"37.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(A_n i.o.) =</text><text x=\"180.0\" y=\"47.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0\n(Zero prob!)</text><rect x=\"24\" y=\"68\" width=\"192\" height=\"46\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"90.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Proof: P(limsup A_n) = P(\u22c2_{n=1}^\u221e \u22c3_{k=n}^\u221e A_k)\n\u2264 P(\u22c3_{k=n}^\u221e A_k) \u2264</text><text x=\"120.0\" y=\"98.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2211_{k=n}^\u221e P(A_k) \u2192 0  (tail sum of convergent series!)\nNO INDEPENDENCE REQUIRED!</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">First Borel-Cantelli Lemma: Convergent probability sum implies event occurs only finitely many times</text></svg>",
    "drawingCaption": "If the sum of probabilities converges, the events occur infinitely often with probability exactly zero",
    "coreTranslation": [
      "<strong>Theorem Statement:</strong> For ANY sequence of events $\\{A_n\\}$, if $\\sum_{n=1}^\\infty \\mathbb{P}(A_n) < \\infty$, then $\\mathbb{P}(\\limsup A_n) = \\mathbb{P}(A_n \\text{ i.o.}) = 0$.",
      "<strong>Direct Union Bound Proof:</strong> By continuity of measure, $\\mathbb{P}(\\limsup A_n) \\le \\mathbb{P}(\\bigcup_{k=n}^\\infty A_k) \\le \\sum_{k=n}^\\infty \\mathbb{P}(A_k)$. As $n \\to \\infty$, the tail of a convergent series tends to 0.",
      "<strong>ZERO Independence Assumption:</strong> BC1 holds unconditionally for dependent, correlated, or adversarial sequences of events."
    ],
    "math": "$$\\sum_{n=1}^\\infty \\mathbb{P}(A_n) < \\infty \\implies \\mathbb{P}\\left(\\limsup_{n \\to \\infty} A_n\\right) = \\mathbb{P}(A_n \\text{ i.o.}) = 0 \\quad (\\text{NO independence needed})$$",
    "personalConnection": "A leaky faucet: if the total expected number of water drops over all future time is finite (\u2211 P(A_n) < \u221e), the faucet is guaranteed to stop dripping permanently after some finite hour.",
    "examTrap": "Assuming BC1 requires independence! BC1 is a pure measure-theoretic consequence of countable sub-additivity; it requires zero independence."
  },
  {
    "id": 31603,
    "subject": "StoMA",
    "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
    "topicTitle": "16 \u00b7 Borel-Cantelli Lemmas & Limsup/Liminf",
    "cardNumber": "03",
    "category": "BOREL-CANTELLI 2",
    "highlighterClass": "highlight-emerald",
    "title": "The Second Borel-Cantelli Lemma: Independence & Divergence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31603\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Second Borel-Cantelli Lemma (BC2):\nIf {A_n} are INDEPENDENT</text><text x=\"120.0\" y=\"46.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">and \u2211_{n=1}^\u221e P(A_n) = \u221e\n\u21d2 P(limsup A_n) = P(A_n i.o.) = 1</text><rect x=\"20\" y=\"64\" width=\"200\" height=\"48\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"87.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Proof: P( (\u22c3_{k=n}^m A_k)\u1d9c ) = \u220f_{k=n}^m (1 - P(A_k))\n\u2264 \u220f_{k=n}^m exp(-P(A_k))</text><text x=\"120.0\" y=\"95.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= exp( - \u2211_{k=n}^m P(A_k) ) \u2192 0\n\u21d2 P(\u22c3_{k=n}^\u221e A_k) = 1  \u2200n  \u21d2  P(limsup A_n) = 1</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">BC2 strictly requires independence: divergent sum + independence forces event to recur infinitely often</text></svg>",
    "drawingCaption": "If events are mutually independent and their probabilities diverge, the event occurs infinitely often with probability 1",
    "coreTranslation": [
      "<strong>Theorem Statement:</strong> If events $\\{A_n\\}$ are MUTUALLY INDEPENDENT and $\\sum_{n=1}^\\infty \\mathbb{P}(A_n) = \\infty$, then $\\mathbb{P}(\\limsup A_n) = \\mathbb{P}(A_n \\text{ i.o.}) = 1$.",
      "<strong>Product Inequality Proof:</strong> $\\mathbb{P}(\\bigcap_{k=n}^m A_k^c) = \\prod_{k=n}^m (1 - \\mathbb{P}(A_k)) \\le \\prod_{k=n}^m e^{-\\mathbb{P}(A_k)} = \\exp(-\\sum_{k=n}^m \\mathbb{P}(A_k)) \\to 0$. Thus $\\mathbb{P}(\\bigcup_{k=n}^\\infty A_k) = 1$ for all $n$.",
      "<strong>Strict Independence Mandate:</strong> Unlike BC1, BC2 FAILS without independence! Correlated events with divergent sums can fail to occur infinitely often."
    ],
    "math": "$$\\{A_n\\} \\text{ independent}, \\quad \\sum_{n=1}^\\infty \\mathbb{P}(A_n) = \\infty \\implies \\mathbb{P}\\left(\\limsup_{n \\to \\infty} A_n\\right) = 1$$",
    "personalConnection": "Infinite monkeys on typewriters: the probability of typing 'HAMLET' on any attempt is tiny (~10\u207b\u2075\u2070), but independent attempts continue forever (\u2211 p = \u221e), guaranteeing the event occurs with probability 1.",
    "examTrap": "Applying BC2 without independence! If A_n = A for all n with P(A) = 1/2, then \u2211 P(A_n) = \u221e, yet P(A_n i.o.) = P(A) = 1/2 \u2260 1! Independence is indispensable."
  },
  {
    "id": 31604,
    "subject": "StoMA",
    "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
    "topicTitle": "16 \u00b7 Borel-Cantelli Lemmas & Limsup/Liminf",
    "cardNumber": "04",
    "category": "ZERO-ONE LAW",
    "highlighterClass": "highlight-purple",
    "title": "Kolmogorov\u2019s Zero-One Law: Binary Tail Probabilities",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31604\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"20\" width=\"192\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Tail \u03c3-Algebra:  \ud835\udcaf = \u22c2_{n=1}^\u221e \u03c3(X_n, X_{n+1}, ...)\n(Events</text><text x=\"120.0\" y=\"49.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">whose occurrence is unaffected by any finite prefix)</text><rect x=\"24\" y=\"70\" width=\"192\" height=\"42\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"90.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Kolmogorov's Zero-One Law:\nFor independent {X_n}, if E \u2208 \ud835\udcaf  \u21d2  P(E)</text><text x=\"120.0\" y=\"99.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= 0   OR   P(E) = 1\n(Tail events have NO intermediate probabilities!)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Tail events include: convergence of series \u2211 X_n, limsup X_n, and asymptotic frequency limits</text></svg>",
    "drawingCaption": "Any event that does not depend on finite prefixes of an independent sequence has probability strictly 0 or 1",
    "coreTranslation": [
      "<strong>Tail $\\sigma$-Algebra:</strong> $\\mathcal{T} \\triangleq \\bigcap_{n=1}^\\infty \\sigma(X_n, X_{n+1}, \\dots)$. An event $E \\in \\mathcal{T}$ is unaffected by changing the values of any finite prefix $X_1, \\dots, X_M$.",
      "<strong>Kolmogorov's Theorem:</strong> If $\\{X_n\\}$ are independent, then for every tail event $E \\in \\mathcal{T}$, $\\mathbb{P}(E) \\in \\{0, 1\\}$. Tail probabilities are binary: either impossible or certain!",
      "<strong>Canonical Tail Events:</strong> Event $\\{\\sum X_n \\text{ converges}\\}$, $\\{\\lim X_n \\text{ exists}\\}$, $\\{\\limsup X_n \\le c\\}$, and $\\{\\lim \\frac{1}{n}\\sum X_i = \\mu\\}$ are all tail events."
    ],
    "math": "$$\\mathcal{T} = \\bigcap_{n=1}^\\infty \\sigma(X_n, X_{n+1}, \\dots), \\quad \\{X_n\\} \\text{ independent} \\implies \\mathbb{P}(E) \\in \\{0, 1\\} \\quad \\forall E \\in \\mathcal{T}$$",
    "personalConnection": "A coin toss destiny: whether the fraction of heads converges as n \u2192 \u221e cannot be altered by altering the first 100 tosses; its truth is an all-or-nothing tail property.",
    "examTrap": "Assuming event {X\u2081 = 1} is a tail event! The first step X\u2081 is in the prefix, not the tail. Only asymptotic properties invariant to finite prefixes belong to \ud835\udcaf."
  },
  {
    "id": 31605,
    "subject": "StoMA",
    "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
    "topicTitle": "16 \u00b7 Borel-Cantelli Lemmas & Limsup/Liminf",
    "cardNumber": "05",
    "category": "BC1 PROOF METHOD",
    "highlighterClass": "highlight-cyan",
    "title": "Proving Almost Sure Convergence via Borel-Cantelli 1",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31605\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"26\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"36.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Target: Prove X_n \u2192^{a.s.} X</text><line x1=\"120\" y1=\"46\" x2=\"120\" y2=\"60\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31605)\"/><rect x=\"20\" y=\"60\" width=\"200\" height=\"26\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"76.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Define bad events: A_n(\u03b5) = { |X_n - X| \u2265 \u03b5 }</text><line x1=\"120\" y1=\"86\" x2=\"120\" y2=\"100\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31605)\"/><rect x=\"20\" y=\"100\" width=\"200\" height=\"26\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"112.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Show \u2211_{n=1}^\u221e P(|X_n - X| \u2265 \u03b5) &lt;</text><text x=\"120.0\" y=\"121.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u221e  \u2200\u03b5 > 0  \u21d2  P(A_n(\u03b5) i.o.) = 0</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Master recipe: Summability of error probabilities proves almost sure convergence via BC1</text></svg>",
    "drawingCaption": "The standard analytical method for establishing almost sure convergence: show error probability series converges",
    "coreTranslation": [
      "<strong>Equivalence Criterion:</strong> $X_n \\xrightarrow{a.s.} X \\iff \\mathbb{P}(\\limsup_{n \\to \\infty} \\{|X_n - X| \\ge \\epsilon\\}) = 0$ for all $\\epsilon > 0$.",
      "<strong>Sufficient Condition:</strong> By BC1, to prove $X_n \\xrightarrow{a.s.} X$, it is SUFFICIENT to show that $\\sum_{n=1}^\\infty \\mathbb{P}(|X_n - X| \\ge \\epsilon) < \\infty$ for every $\\epsilon > 0$.",
      "<strong>Markov / Chebyshev Synergy:</strong> Combine with Markov's inequality: if $\\mathbb{P}(|X_n - X| \\ge \\epsilon) \\le \\frac{\\mathbb{E}[|X_n - X|^p]}{\\epsilon^p}$ and $\\sum \\mathbb{E}[|X_n - X|^p] < \\infty$, almost sure convergence follows immediately."
    ],
    "math": "$$\\sum_{n=1}^\\infty \\mathbb{P}(|X_n - X| \\ge \\epsilon) < \\infty \\quad \\forall \\epsilon > 0 \\implies X_n \\xrightarrow{\\text{a.s.}} X$$",
    "personalConnection": "Eradicating a disease: if the probability of outbreaks at year n sums to a finite number over all centuries, the disease is guaranteed to disappear permanently with probability 1.",
    "examTrap": "Attempting to check a.s. convergence pointwise by hand! Pathwise limits are analytically intractable; the summable probability test (BC1) is the universal tool."
  },
  {
    "id": 31606,
    "subject": "StoMA",
    "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
    "topicTitle": "16 \u00b7 Borel-Cantelli Lemmas & Limsup/Liminf",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Longest Head Runs in Infinite Coin Tosses",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31606\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"68.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Event A_k:\nBlock k of</text><text x=\"68.0\" y=\"46.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">length L_k\nhas ALL Heads</text><rect x=\"124\" y=\"20\" width=\"96\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"172.0\" y=\"37.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(A_k) = (1/2)^{L_k}\nDisjoint</text><text x=\"172.0\" y=\"45.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">blocks \u21d2\nMutually independent</text><rect x=\"20\" y=\"68\" width=\"200\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Dichotomy by Borel-Cantelli:\n(1) L_k = c log\u2082(k): \u2211 k\u207b\u1d9c &lt; \u221e for c > 1 \u21d2 Finitely</text><text x=\"120.0\" y=\"97.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">many runs (BC1)\n(2) L_k = c log\u2082(k): \u2211 k\u207b\u1d9c = \u221e for c \u2264 1 \u21d2 Infinitely many runs (BC2)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Runs of length (1 - \u03b5) log\u2082(n) occur infinitely often; runs of (1 + \u03b5) log\u2082(n) cease permanently</text></svg>",
    "drawingCaption": "Borel-Cantelli pins down the exact logarithmic growth of the longest streak of heads in infinite coin tosses",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Divide an infinite sequence of fair coin tosses into non-overlapping blocks of length $L_k$. Event $A_k$: block $k$ consists entirely of Heads ($P(A_k) = 2^{-L_k}$). Blocks are independent.",
      "<strong>Case 1 ($L_k = (1+\\epsilon)\\log_2 k$):</strong> $\\mathbb{P}(A_k) = k^{-(1+\\epsilon)}$. Since $\\sum k^{-(1+\\epsilon)} < \\infty$, BC1 proves such runs occur only FINITELY many times.",
      "<strong>Case 2 ($L_k = (1-\\epsilon)\\log_2 k$):</strong> $\\mathbb{P}(A_k) = k^{-(1-\\epsilon)}$. Since $\\sum k^{-(1-\\epsilon)} = \\infty$, BC2 proves such runs occur INFINITELY OFTEN. Thus longest run length in $n$ tosses is $\\approx \\log_2 n$ almost surely!"
    ],
    "math": "$$\\sum_{k=1}^\\infty 2^{-L_k} < \\infty \\implies \\text{finitely often}; \\qquad \\sum_{k=1}^\\infty 2^{-L_k} = \\infty \\implies \\text{infinitely often (a.s.)}$$",
    "personalConnection": "Winning streaks in casino games: in an infinite lifetime of fair betting, you will encounter winning streaks of length log\u2082(n) infinitely many times, but streaks exceeding (1+\u03b5) log\u2082(n) will permanently vanish.",
    "examTrap": "Selecting overlapping blocks and applying BC2! Overlapping blocks are correlated, violating the independence mandate of BC2. Non-overlapping partitioning restores independence."
  },
  {
    "id": 31701,
    "subject": "StoMA",
    "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
    "topicTitle": "17 \u00b7 Laws of Large Numbers (WLLN & SLLN)",
    "cardNumber": "01",
    "category": "WLLN",
    "highlighterClass": "highlight-cyan",
    "title": "The Weak Law of Large Numbers: Dispersion Collapse",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31701\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31701)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31701)\"/><path d=\"M 30,114 Q 80,114 125,70 Q 170,114 220,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3 3\"/><path d=\"M 70,114 Q 100,114 125,40 Q 150,114 180,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\"/><path d=\"M 100,114 Q 115,114 125,20 Q 135,114 150,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"125\" y1=\"20\" x2=\"125\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"125\" y=\"126\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc</text><text x=\"175\" y=\"45\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Var(X\u0304_n) = \u03c3\u00b2 / n \u2192 0</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">WLLN: P(|X\u0304_n - \u03bc| \u2265 \u03b5) \u2264 \u03c3\u00b2 / (n \u03b5\u00b2) \u2192 0 proves convergence in probability</text></svg>",
    "drawingCaption": "The variance of the sample mean shrinks as \u03c3\u00b2/n; Chebyshev\u2019s inequality proves convergence in probability to \u03bc",
    "coreTranslation": [
      "<strong>Theorem Statement:</strong> For i.i.d. $X_i$ with mean $\\mu$ and finite variance $\\sigma^2$, sample mean $\\bar{X}_n = \\frac{1}{n}\\sum_{i=1}^n X_i$ satisfies $\\bar{X}_n \\xrightarrow{P} \\mu$: for all $\\epsilon > 0$, $\\lim_{n \\to \\infty} \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0$.",
      "<strong>Chebyshev Proof:</strong> $\\mathbb{E}[\\bar{X}_n] = \\mu$ and $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$. By Chebyshev, $\\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\epsilon^2} = \\frac{\\sigma^2}{n\\epsilon^2} \\to 0$.",
      "<strong>Relaxation:</strong> Finite variance is not necessary! Khinchin's WLLN requires ONLY $\\mathbb{E}[|X|] < \\infty$ (proved via characteristic functions)."
    ],
    "math": "$$\\bar{X}_n = \\frac{1}{n}\\sum_{i=1}^n X_i \\xrightarrow{P} \\mu, \\qquad \\mathbb{P}\\left(|\\bar{X}_n - \\mu| \\ge \\epsilon\\right) \\le \\frac{\\sigma^2}{n\\epsilon^2} \\to 0$$",
    "personalConnection": "A pollster averaging 1,000 voter responses: the average response has sampling error variance 1,000 times smaller than any single respondent's volatility.",
    "examTrap": "Believing WLLN guarantees paths settle down without wild fluctuations. WLLN guarantees only that at step n, error is unlikely; it does NOT preclude infinite future deviations at later times!"
  },
  {
    "id": 31702,
    "subject": "StoMA",
    "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
    "topicTitle": "17 \u00b7 Laws of Large Numbers (WLLN & SLLN)",
    "cardNumber": "02",
    "category": "SLLN",
    "highlighterClass": "highlight-amber",
    "title": "The Strong Law of Large Numbers: Pathwise Certainty",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31702\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31702)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31702)\"/><line x1=\"24\" y1=\"55\" x2=\"215\" y2=\"55\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"205\" y=\"50\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc + \u03b5</text><line x1=\"24\" y1=\"85\" x2=\"215\" y2=\"85\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"205\" y=\"95\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc - \u03b5</text><line x1=\"24\" y1=\"70\" x2=\"215\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"205\" y=\"70\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc</text><path d=\"M 24,100 Q 50,30 80,80 Q 110,65 140,73 L 215,70\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"120\" y=\"35\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Trajectory enters tube and NEVER leaves!</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">SLLN: P(lim_{n \u2192 \u221e} X\u0304_n = \u03bc) = 1 guarantees 100% of sample paths converge to \u03bc</text></svg>",
    "drawingCaption": "The Strong Law guarantees that 100% of actual sample trajectories permanently converge to the true mean \u03bc",
    "coreTranslation": [
      "<strong>Theorem Statement (Kolmogorov):</strong> Let $X_1, X_2, \\dots$ be i.i.d. with $\\mathbb{E}[|X|] < \\infty$. Then $\\mathbb{P}\\left(\\lim_{n \\to \\infty} \\bar{X}_n = \\mu\\right) = 1$ (Almost Sure convergence).",
      "<strong>Trajectory Geometry:</strong> For almost every sample path $\\omega$, for ANY $\\epsilon > 0$, there exists an integer $N(\\omega)$ such that $|\\bar{X}_n(\\omega) - \\mu| < \\epsilon$ for ALL $n \\ge N(\\omega)$. The path enters the $\\epsilon$-tube and NEVER leaves.",
      "<strong>Fundamental Foundation:</strong> Justifies the frequentist definition of probability: empirical frequencies $\\frac{1}{n}\\sum \\mathbf{1}_{A}$ converge almost surely to true probability $\\mathbb{P}(A)$."
    ],
    "math": "$$\\mathbb{P}\\left(\\lim_{n \\to \\infty} \\frac{1}{n}\\sum_{i=1}^n X_i = \\mu\\right) = 1 \\iff \\mathbb{E}[|X|] < \\infty$$",
    "personalConnection": "Casino house edge: occasional lucky gamblers win on single days, but over millions of cumulative bets, the casino's average profit per game converges with 100% mathematical certainty to the house edge.",
    "examTrap": "Confusing WLLN with SLLN! WLLN is a snapshot statement (prob at time n); SLLN is a full-path statement (the entire future trajectory never strays)."
  },
  {
    "id": 31703,
    "subject": "StoMA",
    "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
    "topicTitle": "17 \u00b7 Laws of Large Numbers (WLLN & SLLN)",
    "cardNumber": "03",
    "category": "SLLN 4TH MOMENT PROOF",
    "highlighterClass": "highlight-emerald",
    "title": "The 4th Moment Proof of the Strong Law via BC1",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31703\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"41.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Step 1: Assume E[X\u2074] &lt; \u221e\nExpand E[ (\u2211 (X\u1d62 - \u03bc))\u2074 ] = n E[(X-\u03bc)\u2074]</text><text x=\"120.0\" y=\"49.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">+ 3n(n-1) (E[(X-\u03bc)\u00b2])\u00b2 \u2264 C n\u00b2\n\u21d2 E[ (X\u0304_n - \u03bc)\u2074 ] \u2264 C / n\u00b2</text><rect x=\"16\" y=\"68\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Step 2: Markov on 4th Power + Borel-Cantelli 1:\nP(|X\u0304_n - \u03bc| \u2265 \u03b5) \u2264 E[(X\u0304_n -</text><text x=\"120.0\" y=\"97.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc)\u2074] / \u03b5\u2074 \u2264 C / (n\u00b2 \u03b5\u2074)\nSum converges: \u2211_{n=1}^\u221e 1/n\u00b2 &lt; \u221e \u21d2 X\u0304_n \u2192^{a.s.} \u03bc !</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">4th moment power gives 1/n\u00b2 decay; summability unlocks Borel-Cantelli 1 to prove SLLN</text></svg>",
    "drawingCaption": "Assuming E[X\u2074] < \u221e achieves O(1/n\u00b2) variance decay, whose summability unlocks Borel-Cantelli 1",
    "coreTranslation": [
      "<strong>4th Moment Expansion:</strong> Assume $\\mathbb{E}[X^4] < \\infty$ and $\\mu = 0$. $\\mathbb{E}[(\\sum X_i)^4] = \\sum \\mathbb{E}[X_i^4] + 6\\sum_{i < j} \\mathbb{E}[X_i^2 X_j^2] = n \\mathbb{E}[X^4] + 3n(n-1)\\sigma^4 \\le C n^2$.",
      "<strong>Fourth Power Decay:</strong> $\\mathbb{E}[(\\bar{X}_n)^4] = \\frac{1}{n^4} \\mathbb{E}[(\\sum X_i)^4] \\le \\frac{C n^2}{n^4} = \\frac{C}{n^2}$.",
      "<strong>Summability via BC1:</strong> By Markov, $\\mathbb{P}(|\\bar{X}_n| \\ge \\epsilon) \\le \\frac{\\mathbb{E}[(\\bar{X}_n)^4]}{\\epsilon^4} \\le \\frac{C}{n^2 \\epsilon^4}$. Since $\\sum_{n=1}^\\infty \\frac{1}{n^2} = \\frac{\\pi^2}{6} < \\infty$, BC1 proves $\\bar{X}_n \\xrightarrow{a.s.} 0$!"
    ],
    "math": "$$\\mathbb{E}\\left[(\\bar{X}_n - \\mu)^4\\right] \\le \\frac{C}{n^2} \\implies \\sum_{n=1}^\\infty \\mathbb{P}\\left(|\\bar{X}_n - \\mu| \\ge \\epsilon\\right) \\le \\sum_{n=1}^\\infty \\frac{C}{n^2 \\epsilon^4} < \\infty \\implies \\bar{X}_n \\xrightarrow{\\text{a.s.}} \\mu$$",
    "personalConnection": "Accelerating brake pad: 2nd moment gives 1/n decay (harmonic series diverges, no BC1); 4th moment gives 1/n\u00b2 decay (quadratic series converges, unlocking BC1).",
    "examTrap": "Chebyshev gives 1/n decay: \u2211 1/n = \u221e (diverges), which CANNOT be plugged into BC1! The 4th moment is essential to force the series to converge."
  },
  {
    "id": 31704,
    "subject": "StoMA",
    "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
    "topicTitle": "17 \u00b7 Laws of Large Numbers (WLLN & SLLN)",
    "cardNumber": "04",
    "category": "KOLMOGOROV SLLN",
    "highlighterClass": "highlight-purple",
    "title": "Kolmogorov\u2019s Sharp SLLN & The Truncation Technique",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31704\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Kolmogorov's Sharp SLLN Criterion:\nX\u1d62 i.i.d. \u21d2 X\u0304_n \u2192^{a.s.} \u03bc  IF AND ONLY IF</text><text x=\"120.0\" y=\"49.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\"> E[|X|] &lt; \u221e\n(Requires NO variance; first moment is necessary and sufficient)</text><rect x=\"20\" y=\"68\" width=\"200\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">The Truncation Method:\nDefine Y\u2099 = X\u2099 \u00b7 1_{|X\u2099| \u2264 n}  (Truncate at n)\n(1) P(X\u2099 \u2260 Y\u2099 i.o.)</text><text x=\"120.0\" y=\"97.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= 0 via BC1 since \u2211 P(|X| > n) \u2264 E[|X|] &lt; \u221e\n(2) Apply Kolmogorov's Maximal Inequality to Y\u2099</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Kolmogorov's truncation removes extreme tails, proving SLLN with zero variance assumptions</text></svg>",
    "drawingCaption": "Finite expectation E[|X|] < \u221e is both necessary and sufficient for the Strong Law to hold",
    "coreTranslation": [
      "<strong>Sharpest Condition:</strong> For i.i.d. $X_i$, $\\bar{X}_n \\xrightarrow{a.s.} \\mu$ IF AND ONLY IF $\\mathbb{E}[|X|] < \\infty$. Finite variance is NOT required!",
      "<strong>Truncation Idea:</strong> Define $Y_n = X_n \\mathbf{1}_{\\{|X_n| \\le n\\}}$. The tails satisfy $\\sum_{n=1}^\\infty \\mathbb{P}(X_n \\ne Y_n) = \\sum_{n=1}^\\infty \\mathbb{P}(|X| > n) \\le \\mathbb{E}[|X|] < \\infty$.",
      "<strong>Equivalence via BC1:</strong> By BC1, $X_n = Y_n$ for all but finitely many $n$ almost surely! Thus $\\bar{X}_n$ and $\\bar{Y}_n$ have identical asymptotic limits."
    ],
    "math": "$$\\bar{X}_n \\xrightarrow{\\text{a.s.}} \\mu \\iff \\mathbb{E}[|X|] < \\infty, \\qquad Y_n = X_n\\,\\mathbf{1}_{\\{|X_n| \\le n\\}} \\implies \\sum_{n=1}^\\infty \\mathbb{P}(X_n \\ne Y_n) \\le \\mathbb{E}[|X|] < \\infty$$",
    "personalConnection": "Filtering rare black swans: trimming off the extreme rare tail above n creates a well-behaved sequence Y\u2099, while BC1 proves you only trimmed finitely many observations.",
    "examTrap": "Assuming variance is required for SLLN. Kolmogorov proved that E[|X|] < \u221e alone suffices; distributions with infinite variance (e.g. Pareto with 1 < \u03b1 \u2264 2) still satisfy SLLN!"
  },
  {
    "id": 31705,
    "subject": "StoMA",
    "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
    "topicTitle": "17 \u00b7 Laws of Large Numbers (WLLN & SLLN)",
    "cardNumber": "05",
    "category": "LAW COMPARISON",
    "highlighterClass": "highlight-cyan",
    "title": "Geometric Contrast: WLLN (Snapshots) vs SLLN (Trajectories)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31705\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"96\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"68.0\" y=\"41.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">WLLN (Snapshot):\nP(|X\u0304_n - \u03bc| \u2265 \u03b5) \u2192</text><text x=\"68.0\" y=\"49.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0\nChecks only step n\n(Can escape at n+1)</text><rect x=\"124\" y=\"20\" width=\"96\" height=\"44\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"172.0\" y=\"41.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">SLLN (Whole path):\nP(\u22c3_{k=n}^\u221e {|X\u0304_k-\u03bc|\u2265\u03b5})</text><text x=\"172.0\" y=\"49.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2192 0\nChecks ALL future k \u2265 n\n(Trapped forever!)</text><line x1=\"20\" y1=\"90\" x2=\"220\" y2=\"90\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"20\" y=\"100\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">n</text><text x=\"120\" y=\"100\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k \u2192 \u221e</text><path d=\"M 20,90 Q 70,70 120,88 L 220,90\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">WLLN controls the vertical slice at n; SLLN controls the entire horizontal tail trajectory</text></svg>",
    "drawingCaption": "WLLN controls a single point in time; SLLN controls the entire infinite tail trajectory from step n onward",
    "coreTranslation": [
      "<strong>WLLN Condition:</strong> $\\lim_{n \\to \\infty} \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0$. Evaluates probability at single vertical slice $n$.",
      "<strong>SLLN Condition:</strong> $\\lim_{n \\to \\infty} \\mathbb{P}\\left(\\bigcup_{k=n}^\\infty \\{|\\bar{X}_k - \\mu| \\ge \\epsilon\\}\\right) = 0$. Evaluates the probability of ANY departure across the entire infinite future $k \\ge n$.",
      "<strong>Strict Superiority:</strong> Because $\\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\mathbb{P}(\\bigcup_{k=n}^\\infty \\{|\\bar{X}_k - \\mu| \\ge \\epsilon\\})$, SLLN trivially implies WLLN."
    ],
    "math": "$$\\text{WLLN}: \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\to 0, \\qquad \\text{SLLN}: \\mathbb{P}\\left(\\bigcup_{k=n}^\\infty \\{|\\bar{X}_k - \\mu| \\ge \\epsilon\\}\\right) \\to 0$$",
    "personalConnection": "A missile guidance path: WLLN says the missile is near target at second 100 (but might veer off at second 101); SLLN guarantees the missile stays locked inside the target crosshair for all seconds t \u2265 100.",
    "examTrap": "Assuming WLLN implies SLLN. Variables can satisfy WLLN while oscillating violently out of the tube infinitely many times (e.g. typewriter sequence)."
  },
  {
    "id": 31706,
    "subject": "StoMA",
    "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
    "topicTitle": "17 \u00b7 Laws of Large Numbers (WLLN & SLLN)",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Catastrophic Failure of the Law of Large Numbers (Cauchy)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31706\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Cauchy Distribution: f(x) = \\frac{1}{\u03c0(1+x\u00b2)}\nCharacteristic Function:</text><text x=\"120.0\" y=\"49.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c6_X(t) = exp(-|t|)\nE[|X|] = \u221e  (First moment fails to exist!)</text><rect x=\"20\" y=\"68\" width=\"200\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Sample Mean of n i.i.d. Cauchy RVs:\n\u03c6_{X\u0304_n}(t) = [\u03c6_X(t/n)]\u207f = [exp(-|t|/n)]\u207f</text><text x=\"120.0\" y=\"97.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= exp(-|t|) = \u03c6_X(t) !\n\u21d2 X\u0304_n has the EXACT SAME Cauchy distribution for ALL n!</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Cauchy fails LLN completely: averaging n Cauchy variables provides ZERO noise reduction!</text></svg>",
    "drawingCaption": "The sample mean of n independent Cauchy variables is identical to a single Cauchy variable; averaging provides zero gain",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Let $X_1, \\dots, X_n \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Cauchy}(0, 1)$ with density $f(x) = \\frac{1}{\\pi(1+x^2)}$. Its characteristic function is $\\phi_X(t) = e^{-|t|}$. First moment $\\mathbb{E}[|X|] = \\infty$.",
      "<strong>Sample Mean Characteristic Function:</strong> $\\phi_{\\bar{X}_n}(t) = [\\phi_X(t/n)]^n = [e^{-|t|/n}]^n = e^{-|t|} = \\phi_X(t)$!",
      "<strong>Zero Averaging Gain:</strong> The sample mean $\\bar{X}_n$ is identically distributed to $X_1$ for every $n$. Averaging 1,000,000 Cauchy variables does NOT concentrate around 0; both WLLN and SLLN fail completely!"
    ],
    "math": "$$\\phi_{\\bar{X}_n}(t) = \\left[\\exp\\left(-\\frac{|t|}{n}\\right)\\right]^n = \\exp(-|t|) \\implies \\bar{X}_n \\stackrel{d}{=} X_1 \\quad \\forall n \\ge 1$$",
    "personalConnection": "A broken clock whose error doubles with every tick: averaging multiple readings produces a result just as wildly erratic as a single glance.",
    "examTrap": "Attempting to apply LLN to Cauchy distributions because the PDF looks symmetric! Symmetry is irrelevant when the tail integral \u222b |x| f(x)dx diverges to infinity."
  },
  {
    "id": 31801,
    "subject": "StoMA",
    "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
    "topicTitle": "18 \u00b7 Characteristic Functions & CLT",
    "cardNumber": "01",
    "category": "FOURIER TRANSFORM",
    "highlighterClass": "highlight-cyan",
    "title": "The Characteristic Function: Universal Fourier Dual",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31801\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"70\" cy=\"72\" rx=\"40\" ry=\"40\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(0 70 72)\"/><line x1=\"25\" y1=\"72\" x2=\"115\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31801)\"/><line x1=\"25\" y1=\"72\" x2=\"25\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31801)\"/><text x=\"112\" y=\"70\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Re</text><text x=\"70\" y=\"24\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Im</text><line x1=\"70\" y1=\"72\" x2=\"98\" y2=\"44\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-31801)\"/><circle cx=\"98\" cy=\"44\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"112\" y=\"40\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">e^{itX}</text><text x=\"70\" y=\"126\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">|\u03c6_X(t)| \u2264 1 (Always bounded!)</text><rect x=\"125\" y=\"25\" width=\"100\" height=\"52\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"175.0\" y=\"50.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c6_X(t) = E[e^{itX}]\n= \u222b e^{itx}</text><text x=\"175.0\" y=\"58.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dF(x)\nALWAYS EXISTS for every distribution</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Universal Fourier dual: bounded by 1, uniformly continuous, exists even for Cauchy</text></svg>",
    "drawingCaption": "The characteristic function \u03c6_X(t) = E[e^{itX}] always exists and is universally bounded by 1 on the real line",
    "coreTranslation": [
      "<strong>Definition:</strong> $\\phi_X(t) \\triangleq \\mathbb{E}[e^{itX}] = \\int_{-\\infty}^\\infty e^{itx} dF_X(x)$ for all $t \\in \\mathbb{R}$.",
      "<strong>Universal Existence:</strong> Because $|e^{itX}| = |\\cos(tX) + i\\sin(tX)| = 1$, the integral $\\int |e^{itx}| dF(x) = \\int 1 dF(x) = 1 < \\infty$ ALWAYS converges. Unlike MGFs, $\\phi_X(t)$ exists for every distribution.",
      "<strong>Fundamental Properties:</strong> (1) $\\phi_X(0) = 1$; (2) $|\\phi_X(t)| \\le 1$; (3) $\\phi_X(-t) = \\overline{\\phi_X(t)}$; (4) Uniformly continuous on $\\mathbb{R}$; (5) $\\phi_{aX+b}(t) = e^{itb}\\phi_X(at)$."
    ],
    "math": "$$\\phi_X(t) = \\mathbb{E}\\left[e^{itX}\\right], \\qquad |\\phi_X(t)| \\le \\mathbb{E}\\left[|e^{itX}|\\right] = 1 \\quad \\forall t \\in \\mathbb{R}, \\qquad \\phi_{aX+b}(t) = e^{itb}\\phi_X(at)$$",
    "personalConnection": "Radio frequency tuning: Fourier decomposition translates any arbitrary time-domain signal into clean, bounded sinusoidal frequencies.",
    "examTrap": "Believing characteristic functions can diverge to infinity like MGFs! Because |e^{itx}| = 1, the characteristic function is universally bounded by 1 everywhere."
  },
  {
    "id": 31802,
    "subject": "StoMA",
    "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
    "topicTitle": "18 \u00b7 Characteristic Functions & CLT",
    "cardNumber": "02",
    "category": "CONTINUITY THEOREM",
    "highlighterClass": "highlight-amber",
    "title": "L\u00e9vy\u2019s Continuity Theorem: Pointwise Fourier Convergence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31802\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31802)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31802)\"/><path d=\"M 24,60 Q 70,30 120,30 Q 170,30 215,60\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><text x=\"170\" y=\"25\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c6_X(t)</text><path d=\"M 24,70 Q 70,35 120,30 Q 170,35 215,70\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3 3\"/><path d=\"M 24,65 Q 70,32 120,30 Q 170,32 215,65\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"2 2\"/><circle cx=\"120\" cy=\"30\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"18\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03c6(0) = 1</text><rect x=\"24\" y=\"85\" width=\"192\" height=\"28\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"98.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">L\u00e9vy: X_n \u2192^{d} X  \u21d4  \u03c6_{X_n}(t)</text><text x=\"120.0\" y=\"107.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2192 \u03c6_X(t) pointwise \u2200t \u2208 \u211d</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Pointwise convergence of characteristic functions is equivalent to convergence in distribution</text></svg>",
    "drawingCaption": "Convergence in distribution is mathematically equivalent to pointwise convergence of characteristic functions",
    "coreTranslation": [
      "<strong>Equivalence Statement:</strong> $X_n \\xrightarrow{d} X \\iff \\lim_{n \\to \\infty} \\phi_{X_n}(t) = \\phi_X(t)$ for all $t \\in \\mathbb{R}$.",
      "<strong>Continuity at Origin:</strong> If $\\lim_{n \\to \\infty} \\phi_{X_n}(t) = g(t)$ pointwise, and $g(t)$ is continuous at $t = 0$, then $g(t)$ is the characteristic function of a valid random variable $X$, and $X_n \\xrightarrow{d} X$.",
      "<strong>Mass Escape Warning:</strong> If $g(t)$ is discontinuous at $t=0$, probability mass escapes to $\\pm\\infty$ (tightness fails) and no limiting random variable exists."
    ],
    "math": "$$X_n \\xrightarrow{d} X \\iff \\lim_{n \\to \\infty} \\phi_{X_n}(t) = \\phi_X(t) \\quad \\forall t \\in \\mathbb{R}$$",
    "personalConnection": "Tuning musical instruments by acoustic frequencies: matching the sound spectrum pointwise ensures the acoustic waveforms sound identical in physical space.",
    "examTrap": "Ignoring continuity at t = 0! For Unif[-n, n], \u03c6(t) = sin(nt)/(nt) \u2192 0 for t \u2260 0 and 1 at t = 0. The limit is discontinuous at 0, signaling mass escape to infinity."
  },
  {
    "id": 31803,
    "subject": "StoMA",
    "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
    "topicTitle": "18 \u00b7 Characteristic Functions & CLT",
    "cardNumber": "03",
    "category": "CENTRAL LIMIT THEOREM",
    "highlighterClass": "highlight-emerald",
    "title": "The Lindeberg-L\u00e9vy Central Limit Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31803\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31803)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31803)\"/><path d=\"M 30,114 Q 80,114 100,85 Q 120,25 125,25 Q 130,25 150,85 Q 170,114 220,114\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"125\" y1=\"25\" x2=\"125\" y2=\"114\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"2 2\"/><text x=\"125\" y=\"126\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><text x=\"175\" y=\"45\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Z_n = \\frac{S_n - n\u03bc}{\u03c3\u221an} \u2192^{d} N(0, 1)</text><rect x=\"24\" y=\"20\" width=\"100\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"74.0\" y=\"37.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c6_{Z_n}(t) = [1 - t\u00b2/(2n) +</text><text x=\"74.0\" y=\"45.0\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">o(t\u00b2/n)]\u207f\n\u2192 exp(-t\u00b2/2) = \u03c6_{N(0,1)}(t)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">CLT: Standardized sum of any i.i.d. variables with finite variance converges to N(0, 1)</text></svg>",
    "drawingCaption": "The standardized sum of i.i.d. variables with finite variance converges in distribution to the standard Gaussian",
    "coreTranslation": [
      "<strong>Theorem Statement:</strong> Let $X_1, X_2, \\dots$ be i.i.d. with mean $\\mu$ and finite variance $\\sigma^2 > 0$. Then $Z_n = \\frac{\\sum_{i=1}^n X_i - n\\mu}{\\sigma \\sqrt{n}} \\xrightarrow{d} \\mathcal{N}(0, 1)$.",
      "<strong>Characteristic Function Proof:</strong> Taylor expansion: $\\phi_{\\frac{X-\\mu}{\\sigma}}(u) = 1 - \\frac{u^2}{2} + o(u^2)$. Standardized sum has CF $\\phi_{Z_n}(t) = \\left[1 - \\frac{t^2}{2n} + o(t^2/n)\\right]^n \\to e^{-t^2/2}$ (the exact CF of $\\mathcal{N}(0, 1)$).",
      "<strong>Universal Invariance:</strong> Holds regardless of the underlying distribution's shape (bimodal, uniform, exponential, discrete) as long as variance $\\sigma^2 < \\infty$."
    ],
    "math": "$$Z_n = \\frac{\\sum_{i=1}^n X_i - n\\mu}{\\sigma \\sqrt{n}} \\xrightarrow{d} \\mathcal{N}(0, 1), \\qquad \\phi_{Z_n}(t) = \\left(1 - \\frac{t^2}{2n} + o\\left(\\frac{t^2}{n}\\right)\\right)^n \\to e^{-t^2/2}$$",
    "personalConnection": "Galton's bean machine (quincunx): thousands of steel balls bouncing randomly off pins collect at the bottom in an immaculate Gaussian bell curve.",
    "examTrap": "Applying CLT to unscaled sums S_n or raw means X\u0304_n! S_n variance explodes to \u221e; X\u0304_n variance collapses to 0. CLT applies ONLY to the \u221an-standardized deviation."
  },
  {
    "id": 31804,
    "subject": "StoMA",
    "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
    "topicTitle": "18 \u00b7 Characteristic Functions & CLT",
    "cardNumber": "04",
    "category": "ASYMPTOTIC CONVERGENCE",
    "highlighterClass": "highlight-purple",
    "title": "Berry-Esseen Bound & The Continuity Correction",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31804\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"208\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Berry-Esseen Theorem (Uniform Rate of Convergence):\nsup_{x \u2208 \u211d} |F_{Z_n}(x) - \u03a6(x)| \u2264</text><text x=\"120.0\" y=\"48.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\\frac{0.4748 \u00b7 E[|X - \u03bc|\u00b3]}{\u03c3\u00b3 \u221an} = O(1/\u221an)\n(Convergence rate is governed by skewness and 1/\u221an)</text><rect x=\"16\" y=\"68\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Continuity Correction for Integer Sums:\nP(a \u2264 S_n \u2264 b) \u2248 \u03a6( \\frac{b + 0.5 - n\u03bc}{\u03c3\u221an} ) - \u03a6(</text><text x=\"120.0\" y=\"97.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\\frac{a - 0.5 - n\u03bc}{\u03c3\u221an} )\n(Shifting limits by \u00b10.5 accounts for discrete histogram steps)</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Berry-Esseen guarantees O(1/\u221an) uniform error; continuity correction fixes discrete steps</text></svg>",
    "drawingCaption": "Berry-Esseen bounds normal approximation error at O(1/\u221an); continuity correction aligns discrete integer steps",
    "coreTranslation": [
      "<strong>Berry-Esseen Bound:</strong> If $\\mathbb{E}[|X - \\mu|^3] = \\rho < \\infty$, then $\\sup_{x \\in \\mathbb{R}} |F_{Z_n}(x) - \\Phi(x)| \\le \\frac{C \\rho}{\\sigma^3 \\sqrt{n}}$ with universal constant $C \\le 0.4748$. Error decays strictly at rate $O(1/\\sqrt{n})$.",
      "<strong>Skewness Sensitivity:</strong> Heavy skewness $\\rho/\\sigma^3$ widens the error bound, requiring larger sample sizes $n$ for normal accuracy.",
      "<strong>Continuity Correction:</strong> For discrete integer sums (Binomial, Poisson), adjust integer bounds by $\\pm 0.5$: $\\mathbb{P}(a \\le S_n \\le b) \\approx \\Phi\\left(\\frac{b + 0.5 - n\\mu}{\\sigma\\sqrt{n}}\\right) - \\Phi\\left(\\frac{a - 0.5 - n\\mu}{\\sigma\\sqrt{n}}\\right)$."
    ],
    "math": "$$\\sup_{x \\in \\mathbb{R}} \\left| F_{Z_n}(x) - \\Phi(x) \\right| \\le \\frac{0.4748 \\cdot \\mathbb{E}[|X - \\mu|^3]}{\\sigma^3 \\sqrt{n}}, \\quad \\mathbb{P}(S_n \\le k) \\approx \\Phi\\left(\\frac{k + 0.5 - n\\mu}{\\sigma\\sqrt{n}}\\right)$$",
    "personalConnection": "Sub-pixel antialiasing on computer screens: rendering staircase-like discrete pixels as smooth curves requires a half-pixel offset (\u00b10.5) to balance areas.",
    "examTrap": "Omitting the continuity correction on exam calculations! For moderate sample sizes (n = 50-100), omitting \u00b10.5 can induce up to 10% calculation error."
  },
  {
    "id": 31805,
    "subject": "StoMA",
    "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
    "topicTitle": "18 \u00b7 Characteristic Functions & CLT",
    "cardNumber": "05",
    "category": "ADVANCED CLT",
    "highlighterClass": "highlight-cyan",
    "title": "Lindeberg vs Lyapunov Conditions for Non-Identical Sums",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31805\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"200\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"40.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Lindeberg Condition (Necessary &amp; Sufficient):\ns_n\u00b2 = \u2211 \u03c3\u1d62\u00b2;   \u2200\u03b5 > 0:  lim_{n \u2192 \u221e} \\frac{1}{s_n\u00b2}</text><text x=\"120.0\" y=\"48.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2211_{i=1}^n E[(X\u1d62 - \u03bc\u1d62)\u00b2 1_{|X\u1d62 - \u03bc\u1d62| \u2265 \u03b5 s_n}] = 0\n(Guarantees no single term dominates total variance)</text><rect x=\"20\" y=\"68\" width=\"200\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"89.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Lyapunov Condition (Stronger, Easier to Check):\nlim_{n \u2192 \u221e} \\frac{\u2211_{i=1}^n E[|X\u1d62 -</text><text x=\"120.0\" y=\"97.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc\u1d62|^{2+\u03b4}]}{(s_n\u00b2)^{(2+\u03b4)/2}} = 0  for some \u03b4 > 0\n\u21d2 Lindeberg condition holds automatically!</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">CLT extends to non-identical variables as long as no single term swamps the aggregate variance</text></svg>",
    "drawingCaption": "Lindeberg and Lyapunov conditions extend the Central Limit Theorem to independent non-identically distributed variables",
    "coreTranslation": [
      "<strong>Setup:</strong> Let $X_i$ be independent with means $\\mu_i$ and variances $\\sigma_i^2$. Total variance is $s_n^2 = \\sum_{i=1}^n \\sigma_i^2$.",
      "<strong>Lindeberg Condition:</strong> For all $\\epsilon > 0$, $\\lim_{n \\to \\infty} \\frac{1}{s_n^2} \\sum_{i=1}^n \\mathbb{E}[(X_i - \\mu_i)^2 \\mathbf{1}_{\\{|X_i - \\mu_i| \\ge \\epsilon s_n\\}}] = 0$. Guarantees $\\frac{\\sum (X_i - \\mu_i)}{s_n} \\xrightarrow{d} \\mathcal{N}(0, 1)$.",
      "<strong>Lyapunov Condition:</strong> If $\\lim_{n \\to \\infty} \\frac{1}{s_n^{2+\\delta}} \\sum_{i=1}^n \\mathbb{E}[|X_i - \\mu_i|^{2+\\delta}] = 0$ for some $\\delta > 0$, then Lindeberg's condition holds automatically."
    ],
    "math": "$$\\text{Lyapunov: } \\lim_{n \\to \\infty} \\frac{\\sum_{i=1}^n \\mathbb{E}[|X_i - \\mu_i|^{2+\\delta}]}{\\left(\\sum_{i=1}^n \\sigma_i^2\\right)^{(2+\\delta)/2}} = 0 \\implies \\frac{\\sum_{i=1}^n (X_i - \\mu_i)}{\\sqrt{\\sum \\sigma_i^2}} \\xrightarrow{d} \\mathcal{N}(0, 1)$$",
    "personalConnection": "Electronic noise floor: thousands of dissimilar microscopic resistors contributing random thermal noise; as long as no single component dominates, the output is Gaussian.",
    "examTrap": "Applying CLT when one giant term dominates the sum! If X\u2081 contributes 90% of total variance, the sum reflects X\u2081's individual distribution and fails CLT."
  },
  {
    "id": 31806,
    "subject": "StoMA",
    "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
    "topicTitle": "18 \u00b7 Characteristic Functions & CLT",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: De Moivre-Laplace CLT on 100 Coin Flips",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31806\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"20\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"41.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Problem: S\u2081\u2080\u2080 ~ Binomial(100, 0.5). Find P(45 \u2264 S\u2081\u2080\u2080 \u2264 55)\nParameters: \u03bc = np = 50,</text><text x=\"120.0\" y=\"49.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\"> \u03c3\u00b2 = np(1-p) = 25 \u21d2 \u03c3 = 5\nContinuity Correction: Expand [45, 55] to [44.5, 55.5]</text><rect x=\"16\" y=\"70\" width=\"208\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"91.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Standardize:\nz\u2081 = (44.5 - 50)/5 = -1.1,   z\u2082 = (55.5 - 50)/5 = +1.1\nP(45 \u2264 S\u2081\u2080\u2080</text><text x=\"120.0\" y=\"99.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2264 55) \u2248 \u03a6(1.1) - \u03a6(-1.1) = 2\u03a6(1.1) - 1\n= 2(0.8643) - 1 = 0.7286  (Exact: 0.72874)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Continuity correction delivers 99.98% accuracy matching the exact Binomial sum</text></svg>",
    "drawingCaption": "Applying the Central Limit Theorem with continuity correction matches exact binomial probability to 4 decimal places",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Toss a fair coin $n = 100$ times ($p = 0.5$). Find $\\mathbb{P}(45 \\le S_{100} \\le 55)$.",
      "<strong>Parameters:</strong> $\\mu = np = 50$, $\\sigma = \\sqrt{np(1-p)} = \\sqrt{25} = 5$.",
      "<strong>Continuity Correction & Evaluation:</strong> Expand to $[44.5, 55.5]$. Standardized bounds: $z_1 = -1.1, z_2 = +1.1$. Probability is $\\Phi(1.1) - \\Phi(-1.1) = 2\\Phi(1.1) - 1 = 2(0.8643) - 1 = 0.7286$ (error vs exact binomial is $< 0.02\\%$)."
    ],
    "math": "$$\\mathbb{P}(45 \\le S_{100} \\le 55) \\approx \\Phi\\left(\\frac{55.5 - 50}{5}\\right) - \\Phi\\left(\\frac{44.5 - 50}{5}\\right) = 2\\Phi(1.1) - 1 \\approx 0.7286$$",
    "personalConnection": "Precinct vote tallies: in a razor-thin 50/50 election, a random sample of 100 votes lands within \u00b15 votes of dead center with 73% probability.",
    "examTrap": "Evaluating without continuity correction: (55 - 50)/5 = 1.0 \u21d2 2\u03a6(1.0) - 1 = 0.6827, introducing an unnecessary 4.6% approximation error."
  },
  {
    "id": 31901,
    "subject": "StoMA",
    "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
    "topicTitle": "19 \u00b7 DTMC & State Classification",
    "cardNumber": "01",
    "category": "MARKOV PROPERTY",
    "highlighterClass": "highlight-cyan",
    "title": "The Markov Property & Row-Stochastic Transition Matrix",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31901\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"50\" cy=\"45\" r=\"14\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"50\" y=\"48\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><circle cx=\"150\" cy=\"45\" r=\"14\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"150\" y=\"48\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">2</text><circle cx=\"100\" cy=\"105\" r=\"14\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"100\" y=\"108\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">3</text><line x1=\"64\" y1=\"45\" x2=\"136\" y2=\"45\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31901)\"/><text x=\"100\" y=\"38\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P\u2081\u2082</text><line x1=\"142\" y1=\"57\" x2=\"108\" y2=\"93\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31901)\"/><text x=\"132\" y=\"78\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P\u2082\u2083</text><line x1=\"92\" y1=\"93\" x2=\"58\" y2=\"57\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31901)\"/><text x=\"68\" y=\"78\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P\u2083\u2081</text><rect x=\"160\" y=\"80\" width=\"72\" height=\"36\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"196.0\" y=\"97.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Row-Stochastic:\nP</text><text x=\"196.0\" y=\"105.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2265 0\n\u2211_j P_{ij} = 1</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Markov Property: Future is conditionally independent of past given the present state</text></svg>",
    "drawingCaption": "The future state depends only on the present state, encoded by row-stochastic matrix P where each row sums to 1",
    "coreTranslation": [
      "<strong>Markov Property:</strong> $\\mathbb{P}(X_{n+1} = j \\mid X_n = i, X_{n-1} = i_{n-1}, \\dots, X_0 = i_0) = \\mathbb{P}(X_{n+1} = j \\mid X_n = i) \\triangleq P_{ij}$.",
      "<strong>Memoryless Future:</strong> Conditioned on current state $X_n$, future evolution $X_{n+1}$ is independent of past history $X_0, \\dots, X_{n-1}$.",
      "<strong>Row-Stochastic Matrix:</strong> $P = [P_{ij}]$ satisfies $P_{ij} \\ge 0$ and $\\sum_{j \\in S} P_{ij} = 1$ for all $i \\in S$ (matrix equation $P \\mathbf{1} = \\mathbf{1}$)."
    ],
    "math": "$$\\mathbb{P}(X_{n+1} = j \\mid X_n = i, X_{n-1} = i_{n-1}, \\dots, X_0 = i_0) = P_{ij}, \\qquad \\sum_{j \\in S} P_{ij} = 1 \\quad \\forall i$$",
    "personalConnection": "Board game of Monopoly: the square you land on next depends strictly on your current square and the dice roll, regardless of what path you traveled in earlier turns.",
    "examTrap": "Assuming matrix columns sum to 1! In general, P is ROW-stochastic (rows sum to 1). A matrix whose columns also sum to 1 is doubly stochastic (a special subclass)."
  },
  {
    "id": 31902,
    "subject": "StoMA",
    "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
    "topicTitle": "19 \u00b7 DTMC & State Classification",
    "cardNumber": "02",
    "category": "CHAPMAN-KOLMOGOROV",
    "highlighterClass": "highlight-amber",
    "title": "Chapman-Kolmogorov Equations: P^{(n)} = P\u207f",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31902\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"40\" cy=\"72\" r=\"12\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"40\" y=\"75\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">i</text><circle cx=\"120\" cy=\"35\" r=\"12\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"38\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k\u2081</text><circle cx=\"120\" cy=\"72\" r=\"12\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"75\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k\u2082</text><circle cx=\"120\" cy=\"108\" r=\"12\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"111\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k\u2083</text><circle cx=\"200\" cy=\"72\" r=\"12\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"75\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">j</text><line x1=\"52\" y1=\"68\" x2=\"108\" y2=\"38\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31902)\"/><line x1=\"132\" y1=\"38\" x2=\"188\" y2=\"68\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31902)\"/><line x1=\"52\" y1=\"72\" x2=\"108\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31902)\"/><line x1=\"132\" y1=\"72\" x2=\"188\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31902)\"/><line x1=\"52\" y1=\"76\" x2=\"108\" y2=\"105\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31902)\"/><line x1=\"132\" y1=\"105\" x2=\"188\" y2=\"76\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31902)\"/><text x=\"80\" y=\"24\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_{ik}^{(m)}</text><text x=\"160\" y=\"24\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_{kj}^{(n)}</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Chapman-Kolmogorov: P_{ij}^{(m+n)} = \u2211_k P_{ik}^{(m)} P_{kj}^{(n)}  \u21d4  P^{(n)} = P\u207f</text></svg>",
    "drawingCaption": "The n-step transition probability matrix is the n-th algebraic matrix power: P^{(n)} = P\u207f",
    "coreTranslation": [
      "<strong>Intermediate Splitting:</strong> To transition from $i$ to $j$ in $(m+n)$ steps, the chain must pass through some intermediate state $k$ at step $m$.",
      "<strong>Chapman-Kolmogorov Formula:</strong> $P_{ij}^{(m+n)} = \\sum_{k \\in S} P_{ik}^{(m)} P_{kj}^{(n)}$ for all $m, n \\ge 1$.",
      "<strong>Matrix Power Representation:</strong> In matrix form, $P^{(n)} = P^n$. Unconditional distribution after $n$ steps is $\\mathbf{p}^{(n)} = \\mathbf{p}^{(0)} P^n$ (where $\\mathbf{p}^{(0)}$ is a row vector)."
    ],
    "math": "$$P_{ij}^{(m+n)} = \\sum_{k \\in S} P_{ik}^{(m)} P_{kj}^{(n)} \\iff P^{(m+n)} = P^m P^n, \\qquad \\mathbf{p}^{(n)} = \\mathbf{p}^{(0)} P^n$$",
    "personalConnection": "Airline route planning: the probability of reaching destination J from origin I in two flights sums the probabilities over all possible intermediate layover hubs K.",
    "examTrap": "Multiplying state distribution from the wrong side: p^{(n)} = p^{(0)} P^n where p^{(0)} is a ROW vector. Writing P^n p^{(0)} causes matrix dimension mismatch!"
  },
  {
    "id": 31903,
    "subject": "StoMA",
    "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
    "topicTitle": "19 \u00b7 DTMC & State Classification",
    "cardNumber": "03",
    "category": "COMMUNICATION CLASSES",
    "highlighterClass": "highlight-emerald",
    "title": "Accessibility, Communication & Class Decomposition",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31903\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"25\" y=\"30\" width=\"85\" height=\"75\" rx=\"8\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"67\" y=\"45\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Class C\u2081 (1 \u2194 2)</text><circle cx=\"45\" cy=\"75\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"45\" y=\"78\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><circle cx=\"90\" cy=\"75\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"90\" y=\"78\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2</text><line x1=\"55\" y1=\"72\" x2=\"80\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31903)\"/><line x1=\"80\" y1=\"78\" x2=\"55\" y2=\"78\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31903)\"/><line x1=\"110\" y1=\"67\" x2=\"145\" y2=\"67\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-31903)\"/><text x=\"127\" y=\"58\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1-way</text><rect x=\"145\" y=\"30\" width=\"70\" height=\"75\" rx=\"8\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"180\" y=\"45\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Class C\u2082</text><circle cx=\"180\" cy=\"75\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"180\" y=\"78\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">3</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Communication (i \u2194 j) partitions states into disjoint classes; irreducible if 1 class</text></svg>",
    "drawingCaption": "Communication is an equivalence relation that partitions the Markov chain into disjoint communicating classes",
    "coreTranslation": [
      "<strong>Accessibility ($i \\to j$):</strong> State $j$ is accessible from $i$ if $P_{ij}^{(n)} > 0$ for some $n \\ge 0$ (path of positive probability).",
      "<strong>Communication ($i \\leftrightarrow j$):</strong> States communicate if $i \\to j$ and $j \\to i$. Communication is an EQUIVALENCE RELATION (reflexive, symmetric, transitive).",
      "<strong>Class Partition & Irreducibility:</strong> State space $S$ partitions into disjoint communicating classes $C_k$. A chain is **irreducible** if it consists of exactly ONE communicating class."
    ],
    "math": "$$i \\to j \\iff \\exists n \\ge 0 \\text{ s.t. } P_{ij}^{(n)} > 0; \\qquad i \\leftrightarrow j \\iff i \\to j \\text{ and } j \\to i; \\qquad S = \\bigcup C_k$$",
    "personalConnection": "Subway transit network: if you can ride from station A to station B and return from B to A, both stations belong to the same connected transit line.",
    "examTrap": "Confusing 1-step transitions with accessibility! P_{ij} = 0 does NOT imply j is inaccessible from i; state j might be reached in 2, 3, or more hops (P_{ij}^{(n)} > 0)."
  },
  {
    "id": 31904,
    "subject": "StoMA",
    "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
    "topicTitle": "19 \u00b7 DTMC & State Classification",
    "cardNumber": "04",
    "category": "RECURRENCE & TRANSIENCE",
    "highlighterClass": "highlight-purple",
    "title": "Recurrence vs Transience: Return Probability f_{ii} & Green Function",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31904\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"96\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"68.0\" y=\"41.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Recurrent State:\nf_{ii} = P(\u03c4_i &lt; \u221e | X\u2080=i) =</text><text x=\"68.0\" y=\"49.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1\n\u2211_{n=1}^\u221e P_{ii}^{(n)} = \u221e\n(Certain infinite returns)</text><rect x=\"124\" y=\"20\" width=\"96\" height=\"44\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"172.0\" y=\"41.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Transient State:\nf_{ii} = P(\u03c4_i &lt; \u221e | X\u2080=i) &lt;</text><text x=\"172.0\" y=\"49.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1\n\u2211_{n=1}^\u221e P_{ii}^{(n)} &lt; \u221e\n(Total visits ~ Geom(1-f))</text><rect x=\"20\" y=\"72\" width=\"200\" height=\"42\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.3\"/><text x=\"120\" y=\"86\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Green Function (Expected Total Visits): G_{ii} = \u2211_{n=0}^\u221e P_{ii}^{(n)}</text><text x=\"120\" y=\"102\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Recurrent: G_{ii} = \u221e;    Transient: G_{ii} = 1 / (1 - f_{ii}) &lt; \u221e</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Every finite-state Markov chain contains at least one recurrent class</text></svg>",
    "drawingCaption": "Recurrent states guarantee return with probability 1 and infinite expected visits; transient states drift away forever",
    "coreTranslation": [
      "<strong>First Return Probability:</strong> Let $\\tau_i \\triangleq \\min\\{n \\ge 1 : X_n = i\\}$. Return probability is $f_{ii} \\triangleq \\mathbb{P}(\\tau_i < \\infty \\mid X_0 = i)$.",
      "<strong>Recurrent ($f_{ii} = 1$):</strong> Returns to state $i$ with probability 1; the chain visits state $i$ infinitely many times almost surely, so $\\sum_{n=1}^\\infty P_{ii}^{(n)} = \\infty$.",
      "<strong>Transient ($f_{ii} < 1$):</strong> Non-zero probability $(1 - f_{ii})$ of never returning; total return visits follow $\\text{Geometric}(1 - f_{ii})$ with finite expectation $\\sum_{n=1}^\\infty P_{ii}^{(n)} = \\frac{f_{ii}}{1 - f_{ii}} < \\infty$."
    ],
    "math": "$$i \\text{ recurrent} \\iff f_{ii} = 1 \\iff \\sum_{n=1}^\\infty P_{ii}^{(n)} = \\infty; \\qquad i \\text{ transient} \\iff f_{ii} < 1 \\iff \\sum_{n=1}^\\infty P_{ii}^{(n)} < \\infty$$",
    "personalConnection": "Boomerang vs paper airplane: a boomerang returns to your hand with 100% certainty (recurrent); a paper airplane drifts away with positive probability and never returns (transient).",
    "examTrap": "Assuming all states in a finite Markov chain can be transient. In ANY finite-state Markov chain, at least ONE state must be recurrent (probability mass has nowhere to escape)."
  },
  {
    "id": 31905,
    "subject": "StoMA",
    "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
    "topicTitle": "19 \u00b7 DTMC & State Classification",
    "cardNumber": "05",
    "category": "PERIODICITY",
    "highlighterClass": "highlight-cyan",
    "title": "State Periodicity & Class Sharing Properties",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31905\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"24\" y=\"25\" width=\"75\" height=\"45\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"61.5\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Set A\n(States</text><text x=\"61.5\" y=\"56.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1, 3)</text><line x1=\"99\" y1=\"42\" x2=\"141\" y2=\"42\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31905)\"/><line x1=\"141\" y1=\"52\" x2=\"99\" y2=\"52\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-31905)\"/><rect x=\"141\" y=\"25\" width=\"75\" height=\"45\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"178.5\" y=\"46.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Set B\n(States</text><text x=\"178.5\" y=\"56.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">2, 4)</text><text x=\"120\" y=\"34\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Step 1</text><text x=\"120\" y=\"62\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Step 2</text><rect x=\"24\" y=\"78\" width=\"192\" height=\"40\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"97.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Period d(i) = gcd{n \u2265 1 : P_{ii}^{(n)} > 0}\nSelf-loop P_{ii} ></text><text x=\"120.0\" y=\"106.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0  \u21d2  d(i) = 1 (Aperiodic!)\nClass Property: i \u2194 j \u21d2 d(i) = d(j)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Periodicity, recurrence, and transience are shared by all states in a communicating class</text></svg>",
    "drawingCaption": "Period is the gcd of all possible return times; periodicity and recurrence are shared class invariants",
    "coreTranslation": [
      "<strong>Period Definition:</strong> Period of state $i$ is $d(i) \\triangleq \\gcd\\{n \\ge 1 : P_{ii}^{(n)} > 0\\}$. If $d(i) = 1$, the state is **aperiodic**.",
      "<strong>Class Invariance Theorem:</strong> Recurrence, transience, and periodicity are **CLASS PROPERTIES**: if $i \\leftrightarrow j$, then $d(i) = d(j)$, and $i$ is recurrent $\\iff j$ is recurrent.",
      "<strong>Self-Loop Shortcut:</strong> If state $i$ has a self-loop ($P_{ii} > 0$), then $1 \\in \\{n : P_{ii}^{(n)} > 0\\}$, so $d(i) = \\gcd(1, \\dots) = 1$ (instantly aperiodic!)."
    ],
    "math": "$$d(i) \\triangleq \\gcd\\{n \\ge 1 : P_{ii}^{(n)} > 0\\}; \\qquad i \\leftrightarrow j \\implies d(i) = d(j) \\text{ and } (i \\text{ rec} \\iff j \\text{ rec})$$",
    "personalConnection": "A grandfather clock pendulum: swinging left then right returns to the starting position only at even ticks n = 2, 4, 6... (period 2).",
    "examTrap": "Defining period as the minimum return time! Period is the GREATEST COMMON DIVISOR of all return times, not the length of the shortest loop."
  },
  {
    "id": 31906,
    "subject": "StoMA",
    "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
    "topicTitle": "19 \u00b7 DTMC & State Classification",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: 1D Random Walk Recurrence (P\u00f3lya\u2019s Theorem)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-31906\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"72\" x2=\"220\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.8\"/><circle cx=\"40\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"40\" y=\"86\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">-2</text><circle cx=\"80\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"80\" y=\"86\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">-1</text><circle cx=\"120\" cy=\"72\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"86\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><circle cx=\"160\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"160\" y=\"86\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">+1</text><circle cx=\"200\" cy=\"72\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"200\" y=\"86\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">+2</text><path d=\"M 120,72 Q 140,50 160,72\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31906)\"/><text x=\"140\" y=\"45\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">p</text><path d=\"M 120,72 Q 100,50 80,72\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-31906)\"/><text x=\"100\" y=\"45\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1-p</text><rect x=\"20\" y=\"18\" width=\"200\" height=\"24\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"29.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P_{00}^{(2n)} = \\binom{2n}{n} p^n</text><text x=\"120.0\" y=\"38.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(1-p)^n ~ \\frac{(4p(1-p))^n}{\\sqrt{\u03c0n}}</text><rect x=\"20\" y=\"96\" width=\"200\" height=\"28\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120.0\" y=\"109.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Symmetric p = 1/2: \u2211 1/\u221an = \u221e \u21d2 RECURRENT (P\u00f3lya</text><text x=\"120.0\" y=\"117.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1921)\nAsymmetric p \u2260 1/2: 4p(1-p) &lt; 1 \u21d2 \u2211 &lt; \u221e \u21d2 TRANSIENT</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1D symmetric random walk returns home with certainty; asymmetric walk drifts away forever</text></svg>",
    "drawingCaption": "Symmetric 1D random walk returns home with probability 1 (recurrent); asymmetric walks are transient",
    "coreTranslation": [
      "<strong>Problem Setup:</strong> Random walk on $\\mathbb{Z}$: $X_{n+1} = X_n + \\xi_n$ where $\\mathbb{P}(\\xi = +1) = p$ and $\\mathbb{P}(\\xi = -1) = 1 - p$. Returns occur only at even steps $2n$.",
      "<strong>Return Probability:</strong> $P_{00}^{(2n)} = \\binom{2n}{n} p^n (1-p)^n$. By Stirling's approximation, $\\binom{2n}{n} \\sim \\frac{4^n}{\\sqrt{\\pi n}}$, so $P_{00}^{(2n)} \\sim \\frac{(4p(1-p))^n}{\\sqrt{\\pi n}}$.",
      "<strong>Dichotomy:</strong> If $p = 1/2$, $4p(1-p) = 1$, so $\\sum P_{00}^{(2n)} \\sim \\sum \\frac{1}{\\sqrt{\\pi n}} = \\infty \\implies$ **RECURRENT**. If $p \\ne 1/2$, $4p(1-p) < 1$, so the series converges geometrically $\\implies$ **TRANSIENT**."
    ],
    "math": "$$P_{00}^{(2n)} \\sim \\frac{(4p(1-p))^n}{\\sqrt{\\pi n}} \\implies \\sum_{n=1}^\\infty P_{00}^{(2n)} = \\begin{cases} \\infty & p = 1/2 \\quad (\\text{Recurrent}) \\\\ < \\infty & p \\ne 1/2 \\quad (\\text{Transient}) \\end{cases}$$",
    "personalConnection": "P\u00f3lya's famous theorem: 'A drunk man will always find his way home (1D is recurrent), but a drunk bird can get lost forever (3D random walk is transient with return probability ~0.34).'",
    "examTrap": "Missing period 2: P_{00}^{(2n+1)} = 0 for all odd steps. Returns require an equal number of left and right steps; only even powers contribute to the return series."
  },
  {
    "id": 32001,
    "subject": "StoMA",
    "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
    "topicTitle": "20 \u00b7 Stationary Distributions & Ergodicity",
    "cardNumber": "01",
    "category": "INVARIANT MEASURES",
    "highlighterClass": "highlight-cyan",
    "title": "Stationary Distribution \u03c0 & Invariant Probability Measure",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32001\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"45\" width=\"52\" height=\"38\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"42.0\" y=\"63.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Vector \u03c0^T\n(\u03c0_1,</text><text x=\"42.0\" y=\"72.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">..., \u03c0_m)</text><line x1=\"68\" y1=\"64\" x2=\"98\" y2=\"64\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32001)\"/><rect x=\"98\" y=\"38\" width=\"48\" height=\"52\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"122.0\" y=\"63.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Matrix</text><text x=\"122.0\" y=\"72.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P\n[P_ij]</text><line x1=\"146\" y1=\"64\" x2=\"176\" y2=\"64\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32001)\"/><rect x=\"176\" y=\"45\" width=\"52\" height=\"38\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"202.0\" y=\"63.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Vector</text><text x=\"202.0\" y=\"72.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c0^T\nUnchanged!</text><text x=\"120\" y=\"110\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03c0^T P = \u03c0^T  \u27fa  \u03c0_j = \u03a3_i \u03c0_i P_ij</text><text x=\"120\" y=\"126\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Left Eigenvector: Dominant Perron-Frobenius eigenvalue \u03bb = 1</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Stationary distribution: if X_0 ~ \u03c0, then X_n ~ \u03c0 for all n \u2265 1</text></svg>",
    "drawingCaption": "The stationary distribution \u03c0 satisfies \u03c0^T P = \u03c0^T: probability mass distributions remain preserved through state transitions",
    "coreTranslation": [
      "<strong>Invariant Probability Measure:</strong> A row probability vector $\\pi = (\\pi_i)_{i \\in S}$ is stationary if $\\pi^\\top P = \\pi^\\top$ with $\\pi_i \\ge 0$ and $\\sum_{i \\in S} \\pi_i = 1$. If initial state $X_0 \\sim \\pi$, then $X_n \\sim \\pi$ for all steps $n \\ge 1$ identically.",
      "<strong>Component-wise Inflow Balance:</strong> Expanding $\\pi^\\top P = \\pi^\\top$ yields $\\pi_j = \\sum_{i \\in S} \\pi_i P_{ij}$ for all states $j \\in S$. The stationary probability mass at state $j$ equals the aggregate probability flux entering $j$ from all predecessor states $i$ weighted by steady-state occupancies.",
      "<strong>Left Eigenvector Formulation:</strong> Mathematically, $\\pi^\\top$ is a normalized left eigenvector of transition matrix $P$ corresponding to the dominant Perron-Frobenius eigenvalue $\\lambda_1 = 1$, ensuring non-negativity and existence for finite stochastic matrices."
    ],
    "math": "$$\\pi^\\top P = \\pi^\\top, \\quad \\sum_{i \\in S} \\pi_i = 1, \\quad \\pi_j = \\sum_{i \\in S} \\pi_i P_{ij} \\quad \\forall j \\in S$$",
    "personalConnection": "Steady-state fluid flow in closed pipe networks: whatever mass flows into junction j from upstream branches must match the mass residing at j.",
    "examTrap": "Confusing left vs right eigenvectors! \u03c0^T P = \u03c0^T is a *left* eigenvector equation. The trivial *right* eigenvector with eigenvalue 1 is the vector of all ones P 1 = 1, which represents row-stochasticity, not the stationary distribution!"
  },
  {
    "id": 32002,
    "subject": "StoMA",
    "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
    "topicTitle": "20 \u00b7 Stationary Distributions & Ergodicity",
    "cardNumber": "02",
    "category": "LIMIT THEOREMS",
    "highlighterClass": "highlight-amber",
    "title": "Fundamental Limit Theorem & Return Time Reciprocal",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32002\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32002)\"/><line x1=\"24\" y1=\"115\" x2=\"24\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32002)\"/><text x=\"225\" y=\"115\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">n</text><text x=\"20\" y=\"22\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_ij^(n)</text><path d=\"M 25,35 Q 70,85 120,68 T 215,65\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/><path d=\"M 25,100 Q 70,45 120,62 T 215,65\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"3 3\"/><path d=\"M 25,75 Q 70,80 120,66 T 215,65\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"25\" y1=\"65\" x2=\"215\" y2=\"65\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 4\"/><circle cx=\"215\" cy=\"65\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"180\" y=\"56\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Limit \u03c0_j = 1/\u03bc_jj</text><text x=\"65\" y=\"28\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Start i=1</text><text x=\"65\" y=\"110\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Start i=2</text><rect x=\"24\" y=\"12\" width=\"105\" height=\"22\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"76.5\" y=\"22.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Irreducible + Aperiodic\n+</text><text x=\"76.5\" y=\"30.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Positive Recurrent</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Fundamental Limit Theorem: P_ij^(n) \u2192 \u03c0_j = 1/E[\u03c4_j | X_0 = j] independent of start state i</text></svg>",
    "drawingCaption": "Under irreducibility, positive recurrence, and aperiodicity, transition probabilities converge to \u03c0_j = 1/\u03bc_jj regardless of initial state i",
    "coreTranslation": [
      "<strong>Convergence Theorem:</strong> For an irreducible, positive recurrent, and aperiodic DTMC, the $n$-step transition probabilities satisfy $\\lim_{n \\to \\infty} P_{ij}^{(n)} = \\pi_j > 0$ for all initial states $i$ and target states $j$. The asymptotic distribution is independent of starting state $X_0 = i$.",
      "<strong>Kac's Return Time Reciprocal:</strong> The unique invariant probability $\\pi_j$ is precisely the reciprocal of the expected first return time to state $j$: $\\pi_j = \\frac{1}{\\mu_{jj}} = \\frac{1}{\\mathbb{E}[\\tau_j \\mid X_0 = j]}$. Rare states with long expected return times have proportionally tiny steady-state probabilities.",
      "<strong>Coupling Proof Paradigm:</strong> The classical Doeblin coupling runs two independent chain copies $X_n, Y_n$ until they collide at stopping time $T = \\inf\\{n: X_n = Y_n\\}$, proving $|P_{ij}^{(n)} - \\pi_j| \\le P(T > n) \\to 0$ exponentially."
    ],
    "math": "$$\\lim_{n \\to \\infty} P_{ij}^{(n)} = \\pi_j = \\frac{1}{\\mu_{jj}} = \\frac{1}{\\mathbb{E}[\\tau_j \\mid X_0 = j]} > 0$$",
    "personalConnection": "Bus stop headway paradox: a commuter waiting for bus route j finds the long-run visit fraction is 1/\u03bc_jj where \u03bc_jj is the average round-trip headway cycle.",
    "examTrap": "Applying the limit theorem to periodic chains! If the chain is bipartite or cyclic (period d > 1), P_ij^(n) does not converge as n \u2192 \u221e but oscillates indefinitely, even though a unique stationary distribution \u03c0 exists!"
  },
  {
    "id": 32003,
    "subject": "StoMA",
    "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
    "topicTitle": "20 \u00b7 Stationary Distributions & Ergodicity",
    "cardNumber": "03",
    "category": "CLASSIFICATION OF STATES",
    "highlighterClass": "highlight-emerald",
    "title": "Positive vs Null Recurrence & Random Walk Drift",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32003\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"16\" y=\"22\" width=\"64\" height=\"96\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"48\" y=\"35\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p &lt; 1/2</text><text x=\"48\" y=\"48\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Pos. Recurrent</text><text x=\"48\" y=\"65\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc_00 &lt; \u221e</text><text x=\"48\" y=\"80\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03c0_i > 0</text><text x=\"48\" y=\"98\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03a3 \u03c0_i = 1 (Exists)</text><rect x=\"88\" y=\"22\" width=\"64\" height=\"96\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120\" y=\"35\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p = 1/2</text><text x=\"120\" y=\"48\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Null Recurrent</text><text x=\"120\" y=\"65\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc_00 = \u221e</text><text x=\"120\" y=\"80\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f_00 = 1</text><text x=\"120\" y=\"98\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03c0_i = 1/\u221e = 0</text><rect x=\"160\" y=\"22\" width=\"64\" height=\"96\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"192\" y=\"35\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p > 1/2</text><text x=\"192\" y=\"48\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Transient</text><text x=\"192\" y=\"65\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f_00 &lt; 1</text><text x=\"192\" y=\"80\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Drift to +\u221e</text><text x=\"192\" y=\"98\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Finite Visits</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Recurrence taxonomy: positive recurrent (finite \u03bc_ii), null recurrent (infinite \u03bc_ii), transient</text></svg>",
    "drawingCaption": "Positive recurrence guarantees a normalizable stationary distribution; null recurrence has probability 1 return but infinite expected return time",
    "coreTranslation": [
      "<strong>Positive Recurrence Criteria:</strong> An irreducible chain is positive recurrent if and only if $\\mu_{ii} = \\mathbb{E}[\\tau_i \\mid X_0 = i] < \\infty$ for some (and hence all) states $i$. In this case and only this case, a valid normalized probability distribution $\\pi$ exists satisfying $\\sum \\pi_i = 1$.",
      "<strong>Null Recurrence & Mass Dispersion:</strong> A chain is null recurrent if return probability is 1 ($f_{ii} = 1$), but expected return time is infinite ($\\mu_{ii} = \\infty$). Stationary equations $\\pi^\\top P = \\pi^\\top$ have non-trivial non-negative solutions, but their sum is infinite, yielding zero probability $\\pi_i = 1/\\infty = 0$ upon normalization.",
      "<strong>Reflected Random Walk Benchmark:</strong> On $\\mathbb{Z}_+$ with $P_{i, i+1} = p$ and $P_{i, i-1} = 1-p$: positive recurrent if $p < 1/2$ (geometric stationary distribution); null recurrent if $p = 1/2$ (symmetric random walk wanders to infinity); transient if $p > 1/2$."
    ],
    "math": "$$\\mu_{ii} < \\infty \\iff \\text{Pos. Recurrent } (\\sum \\pi_i = 1); \\quad \\mu_{ii} = \\infty \\iff \\text{Null Recurrent } (\\pi_i \\equiv 0)$$",
    "personalConnection": "Diffusing gas in an infinite room: molecules return to the origin with probability 1 (recurrence), but take infinite expected time to do so (null recurrence), dissipating density to zero.",
    "examTrap": "Assuming recurrence implies existence of a stationary distribution! On infinite state spaces, symmetric random walks are recurrent (f_00 = 1) but possess NO stationary probability distribution because \u03bc_00 = \u221e."
  },
  {
    "id": 32004,
    "subject": "StoMA",
    "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
    "topicTitle": "20 \u00b7 Stationary Distributions & Ergodicity",
    "cardNumber": "04",
    "category": "BALANCE EQUATIONS",
    "highlighterClass": "highlight-purple",
    "title": "Cut Equations & Detailed Balance Equations",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32004\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"90\" height=\"95\" rx=\"8\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"65\" y=\"35\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Set A</text><circle cx=\"45\" cy=\"60\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"45\" y=\"63\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">i_1</text><circle cx=\"75\" cy=\"85\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"75\" y=\"88\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">i_2</text><rect x=\"130\" y=\"20\" width=\"90\" height=\"95\" rx=\"8\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"175\" y=\"35\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Set A^c</text><circle cx=\"155\" cy=\"60\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"155\" y=\"63\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">j_1</text><circle cx=\"185\" cy=\"85\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"185\" y=\"88\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">j_2</text><line x1=\"120\" y1=\"15\" x2=\"120\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"4 4\"/><text x=\"120\" y=\"12\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">CUT</text><line x1=\"55\" y1=\"60\" x2=\"145\" y2=\"60\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32004)\"/><text x=\"100\" y=\"52\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03a3_{i\u2208A, j\u2208A^c} \u03c0_i P_ij</text><line x1=\"145\" y1=\"78\" x2=\"55\" y2=\"78\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32004)\"/><text x=\"100\" y=\"90\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03a3_{j\u2208A^c, i\u2208A} \u03c0_j P_ji</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Cut equations equate aggregate flux across any cut; detailed balance equates pairwise flows</text></svg>",
    "drawingCaption": "Steady-state probability flux crossing any partition cut must balance; time-reversible chains satisfy pairwise detailed balance",
    "coreTranslation": [
      "<strong>Global Cut Conservation Law:</strong> For any partition of state space $S = A \\cup A^c$, the net steady-state probability flux leaving $A$ must equal the flux entering $A$: $\\sum_{i \\in A} \\sum_{j \\in A^c} \\pi_i P_{ij} = \\sum_{j \\in A^c} \\sum_{i \\in A} \\pi_j P_{ji}$. This generalizes component balance.",
      "<strong>Detailed Balance Condition:</strong> A distribution $\\pi$ satisfies detailed balance if $\\pi_i P_{ij} = \\pi_j P_{ji}$ for all pairs $i, j \\in S$. Any non-negative normalized solution to detailed balance automatically satisfies full balance $\\pi^\\top P = \\pi^\\top$, making the Markov chain time-reversible.",
      "<strong>Birth-Death Process Simplification:</strong> In birth-death chains (transitions only to adjacent neighbors $i \\pm 1$), cut equations between $\\{0, \\dots, i\\}$ and $\\{i+1, \\dots\\}$ reduce directly to pairwise detailed balance $\\pi_i P_{i, i+1} = \\pi_{i+1} P_{i+1, i}$, bypassing full matrix inversion."
    ],
    "math": "$$\\sum_{i \\in A, j \\in A^c} \\pi_i P_{ij} = \\sum_{j \\in A^c, i \\in A} \\pi_j P_{ji}; \\quad \\text{Detailed Balance: } \\pi_i P_{ij} = \\pi_j P_{ji} \\implies \\pi^\\top P = \\pi^\\top$$",
    "personalConnection": "Thermodynamic microscopic reversibility: in thermal equilibrium, every individual forward chemical reaction rate equals its reverse reaction rate.",
    "examTrap": "Thinking all Markov chains satisfy detailed balance! Detailed balance only holds for *reversible* chains (such as trees or birth-death chains). Unidirectional cyclic chains (1 \u2192 2 \u2192 3 \u2192 1) satisfy global balance but violate detailed balance!"
  },
  {
    "id": 32005,
    "subject": "StoMA",
    "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
    "topicTitle": "20 \u00b7 Stationary Distributions & Ergodicity",
    "cardNumber": "05",
    "category": "PERIODICITY & ERGODICITY",
    "highlighterClass": "highlight-cyan",
    "title": "Periodic DTMCs & Ces\u00e0ro Time-Average Convergence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32005\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"50\" cy=\"45\" r=\"14\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"50\" y=\"48\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">0</text><circle cx=\"190\" cy=\"45\" r=\"14\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"190\" y=\"48\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1</text><path d=\"M 64,40 C 100,20 140,20 176,40\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32005)\"/><text x=\"120\" y=\"22\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_01 = 1</text><path d=\"M 176,50 C 140,70 100,70 64,50\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32005)\"/><text x=\"120\" y=\"72\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_10 = 1</text><line x1=\"30\" y1=\"122\" x2=\"215\" y2=\"122\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32005)\"/><line x1=\"30\" y1=\"122\" x2=\"30\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32005)\"/><path d=\"M 35,122 L 55,85 L 75,122 L 95,85 L 115,122 L 135,85 L 155,122 L 175,85 L 195,122 L 210,85\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><path d=\"M 35,122 Q 60,95 100,103 T 210,103\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"30\" y1=\"103\" x2=\"215\" y2=\"103\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"3 3\"/><text x=\"180\" y=\"98\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Ces\u00e0ro Limit = 1/2</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Periodic DTMC: P^(n) oscillates forever, but Ces\u00e0ro time-average (1/N) \u03a3 P^(n) \u2192 \u03c0 = (1/2, 1/2)</text></svg>",
    "drawingCaption": "While periodic chains oscillate without a pointwise limit, their Ces\u00e0ro time average converges unconditionally to \u03c0",
    "coreTranslation": [
      "<strong>Failure of Pointwise Limits:</strong> For an irreducible positive-recurrent chain with period $d > 1$, the state space partitions into cyclic classes $C_0, \\dots, C_{d-1}$. The sequence of transition probabilities $P_{ij}^{(n)}$ oscillates periodically and fails to converge to any single constant.",
      "<strong>Ces\u00e0ro Limit Universality:</strong> Even when periodicity destroys the ordinary limit, the Ces\u00e0ro time-average limit always exists and equals the unique stationary distribution: $\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N P_{ij}^{(n)} = \\pi_j$ for all states $i, j$.",
      "<strong>Stationary Vector Invariance:</strong> The stationary vector $\\pi$ satisfying $\\pi^\\top P = \\pi^\\top$ remains completely valid and unique for periodic positive recurrent chains; periodicity affects pathwise synchronization, not steady-state invariant measures."
    ],
    "math": "$$\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N P_{ij}^{(n)} = \\pi_j \\quad (\\text{holds for both periodic and aperiodic positive recurrent chains})$$",
    "personalConnection": "Traffic light cycle: red and green states oscillate deterministically every 60 seconds (no point limit), yet the long-run fraction of time spent in red is exactly 1/2.",
    "examTrap": "Claiming a periodic chain has no stationary distribution! Periodicity only prevents pointwise convergence lim_{n \u2192 \u221e} P_ij^(n); the stationary distribution \u03c0 still exists and satisfies \u03c0^T P = \u03c0^T uniquely!"
  },
  {
    "id": 32006,
    "subject": "StoMA",
    "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
    "topicTitle": "20 \u00b7 Stationary Distributions & Ergodicity",
    "cardNumber": "06",
    "category": "ERGODIC THEORY",
    "highlighterClass": "highlight-amber",
    "title": "Ergodic Theorem & Strong Law for DTMCs",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32006\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"25\" y1=\"115\" x2=\"220\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32006)\"/><line x1=\"25\" y1=\"115\" x2=\"25\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32006)\"/><text x=\"225\" y=\"115\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">N</text><text x=\"20\" y=\"22\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">f(X_n)</text><path d=\"M 25,95 L 45,45 L 65,100 L 85,35 L 105,75 L 125,50 L 145,80 L 165,60 L 185,72 L 210,68\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/><path d=\"M 25,95 Q 65,70 120,68 T 215,68\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\"/><line x1=\"25\" y1=\"68\" x2=\"215\" y2=\"68\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 4\"/><text x=\"175\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E_\u03c0[f(X)] = \u03a3 \u03c0_j f(j)</text><rect x=\"25\" y=\"15\" width=\"110\" height=\"24\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"80.0\" y=\"26.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Ergodic Equality (a.s.):\nTime</text><text x=\"80.0\" y=\"34.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Average = Space Average</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Ergodic Theorem: (1/N) \u03a3_{n=1}^N f(X_n) \u2192 E_\u03c0[f(X)] almost surely for any bounded function f</text></svg>",
    "drawingCaption": "The long-run time average along a single sample path converges almost surely to the stationary ensemble expectation",
    "coreTranslation": [
      "<strong>Strong Law for DTMCs:</strong> Let $\\{X_n\\}$ be an irreducible positive-recurrent Markov chain with stationary distribution $\\pi$. For any function $f: S \\to \\mathbb{R}$ with $\\sum_i |f(i)| \\pi_i < \\infty$, the sample path time average converges almost surely: $\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N f(X_n) = \\sum_{i \\in S} f(i) \\pi_i$.",
      "<strong>Occupancy Fraction Representation:</strong> Setting indicator reward $f(k) = \\mathbf{1}_{\\{k = j\\}}$, the Ergodic Theorem establishes that the empirical fraction of time spent in state $j$ converges almost surely to $\\pi_j$: $\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N \\mathbf{1}_{\\{X_n = j\\}} = \\pi_j$.",
      "<strong>Long-Run Cost Evaluation:</strong> In queuing and buffer engineering, long-run packet drop rates, average buffer occupancy $\\mathbb{E}[L]$, and operational running costs are computed directly via stationary expectations $\\sum_i f(i) \\pi_i$ without tracking transient distributions."
    ],
    "math": "$$\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N f(X_n) = \\sum_{j \\in S} \\pi_j f(j) = \\mathbb{E}_\\pi[f(X)] \\quad \\text{almost surely}$$",
    "personalConnection": "Monte Carlo MCMC sampling: walking along a Markov chain trajectory and averaging sample outputs produces exact target ensemble expectations.",
    "examTrap": "Applying the Ergodic Theorem to reducible chains! If the chain has multiple communicating recurrent classes, the long-run average lim (1/N) \u03a3 f(X_n) is a random variable dependent on which class the chain was absorbed into, not a single constant!"
  },
  {
    "id": 32101,
    "subject": "StoMA",
    "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
    "topicTitle": "21 \u00b7 Absorption & Mean Hitting Times",
    "cardNumber": "01",
    "category": "ABSORPTION ANALYSIS",
    "highlighterClass": "highlight-cyan",
    "title": "First-Step Analysis for Absorption Probabilities",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32101\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"70\" cy=\"70\" r=\"14\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"70\" y=\"73\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">i</text><line x1=\"82\" y1=\"62\" x2=\"130\" y2=\"35\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32101)\"/><text x=\"102\" y=\"42\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_{iA}</text><rect x=\"132\" y=\"22\" width=\"60\" height=\"24\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"162.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Target A (a=1)</text><line x1=\"84\" y1=\"70\" x2=\"130\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32101)\"/><text x=\"105\" y=\"64\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_ij</text><circle cx=\"142\" cy=\"70\" r=\"12\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"142\" y=\"73\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">j (a_j)</text><line x1=\"82\" y1=\"78\" x2=\"130\" y2=\"105\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32101)\"/><text x=\"102\" y=\"98\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_{iB}</text><rect x=\"132\" y=\"95\" width=\"60\" height=\"24\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"162.0\" y=\"110.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Target B (a=0)</text><rect x=\"15\" y=\"15\" width=\"80\" height=\"22\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"55.0\" y=\"29.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">a_i = \u03a3_j P_ij a_j</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">First-step analysis: decompose absorption probability by conditioning on the first step X_1</text></svg>",
    "drawingCaption": "Absorption probabilities satisfy linear first-step equations a_i = \u03a3_j P_ij a_j anchored by boundary target conditions",
    "coreTranslation": [
      "<strong>Total Probability Decomposition:</strong> To find absorption probability $a_i = P(\\tau_A < \\tau_B \\mid X_0 = i)$, condition on the very first jump $X_1 = j$. By the Markov property, the process restarts from state $j$, yielding linear balance $a_i = \\sum_{j \\in S} P_{ij} a_j$.",
      "<strong>Boundary Pinning Conditions:</strong> The linear system requires explicit boundary values: $a_i = 1$ for all target states $i \\in A$, and $a_i = 0$ for all competing absorbing states $i \\in B$. For transient states $i \\notin A \\cup B$, $a_i$ lies strictly in $(0, 1)$.",
      "<strong>Uniqueness via Maximum Principle:</strong> In finite state spaces where absorption occurs with probability 1 from all transient states, the linear system $(I - Q) a = R_A$ has a unique solution because all eigenvalues of sub-stochastic matrix $Q$ satisfy $|\\lambda| < 1$."
    ],
    "math": "$$a_i = \\sum_{j \\in S} P_{ij} a_j \\quad (i \\notin A \\cup B), \\quad a_i = 1 \\ (i \\in A), \\quad a_i = 0 \\ (i \\in B)$$",
    "personalConnection": "Branching game tree: calculating probability of winning a chess endgame by weighting winning probabilities of all immediate legal first moves.",
    "examTrap": "Forgetting to check boundary conditions! If boundary states a_i = 1 are omitted, the trivial all-zero vector a_i \u2261 0 solves the unconstrained system a = P a. Always specify boundary conditions on absorbing sets!"
  },
  {
    "id": 32102,
    "subject": "StoMA",
    "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
    "topicTitle": "21 \u00b7 Absorption & Mean Hitting Times",
    "cardNumber": "02",
    "category": "HITTING TIMES",
    "highlighterClass": "highlight-amber",
    "title": "Mean Hitting Time First-Step Equations",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32102\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"60\" cy=\"68\" r=\"14\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"71\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">i</text><rect x=\"20\" y=\"22\" width=\"60\" height=\"24\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"50.0\" y=\"37.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Cost: +1 step</text><line x1=\"50\" y1=\"46\" x2=\"55\" y2=\"56\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"74\" y1=\"58\" x2=\"125\" y2=\"40\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32102)\"/><text x=\"98\" y=\"44\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_ij</text><circle cx=\"138\" cy=\"38\" r=\"12\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"138\" y=\"41\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc_j</text><line x1=\"74\" y1=\"78\" x2=\"125\" y2=\"95\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32102)\"/><text x=\"98\" y=\"92\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P_ik</text><circle cx=\"138\" cy=\"98\" r=\"12\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"138\" y=\"101\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc_k</text><rect x=\"170\" y=\"56\" width=\"56\" height=\"26\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"198.0\" y=\"68.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Target</text><text x=\"198.0\" y=\"77.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A\n\u03bc_A = 0</text><line x1=\"150\" y1=\"42\" x2=\"170\" y2=\"62\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"2 2\" marker-end=\"url(#arr-32102)\"/><line x1=\"150\" y1=\"94\" x2=\"170\" y2=\"74\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"2 2\" marker-end=\"url(#arr-32102)\"/><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Mean hitting times: \u03bc_i = 1 + \u03a3_{j \u2209 A} P_ij \u03bc_j for i \u2209 A, with absorbing boundary \u03bc_A = 0</text></svg>",
    "drawingCaption": "Mean hitting times accumulate a +1 cost for the initial step plus weighted downstream expectations: (I - Q) \u03bc = 1",
    "coreTranslation": [
      "<strong>First-Step Time Accumulation:</strong> The expected hitting time to target set $A$, $\\mu_i = \\mathbb{E}[\\tau_A \\mid X_0 = i]$, satisfies $\\mu_i = 1 + \\sum_{j \\in S} P_{ij} \\mu_j$ for $i \\notin A$. The constant '$+1$' accounts for elapsed time of the initial transition step.",
      "<strong>Target Boundary Condition:</strong> By definition, if the chain begins already inside target set $A$, zero additional steps are required: $\\mu_i = 0$ for all $i \\in A$. This provides essential non-homogeneous anchoring for the linear equation system.",
      "<strong>Matrix Formulation:</strong> In vector form over transient states $T$, the system is $\\boldsymbol{\\mu} = \\mathbf{1} + Q \\boldsymbol{\\mu}$, which yields $(I - Q) \\boldsymbol{\\mu} = \\mathbf{1} \\implies \\boldsymbol{\\mu} = (I - Q)^{-1} \\mathbf{1}$, identifying mean hitting time as the row sum of the fundamental matrix."
    ],
    "math": "$$\\mu_i = \\begin{cases} 0 & i \\in A \\\\ 1 + \\sum_{j \\notin A} P_{ij} \\mu_j & i \\notin A \\end{cases} \\iff (I - Q) \\boldsymbol{\\mu} = \\mathbf{1}$$",
    "personalConnection": "GPS navigation rerouting: expected arrival time from intersection i equals 1 minute to traverse the intersection plus the weighted expected arrival time from neighboring intersections.",
    "examTrap": "Omitting the +1 in hitting time calculations! Without +1, the equation becomes \u03bc = Q\u03bc, which gives the useless trivial solution \u03bc = 0. In contrast, absorption probabilities do NOT have +1."
  },
  {
    "id": 32103,
    "subject": "StoMA",
    "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
    "topicTitle": "21 \u00b7 Absorption & Mean Hitting Times",
    "cardNumber": "03",
    "category": "FUNDAMENTAL MATRIX",
    "highlighterClass": "highlight-emerald",
    "title": "Canonical Form & Fundamental Matrix N = (I-Q)^{-1}",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32103\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"25\" y=\"20\" width=\"85\" height=\"85\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.8\"/><rect x=\"25\" y=\"20\" width=\"50\" height=\"50\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"50\" y=\"48\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Q (t\u00d7t)</text><rect x=\"75\" y=\"20\" width=\"35\" height=\"50\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"92\" y=\"48\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">R (t\u00d7r)</text><rect x=\"25\" y=\"70\" width=\"50\" height=\"35\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"50\" y=\"90\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><rect x=\"75\" y=\"70\" width=\"35\" height=\"35\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"92\" y=\"90\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">I_r</text><line x1=\"115\" y1=\"62\" x2=\"142\" y2=\"62\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32103)\"/><rect x=\"145\" y=\"28\" width=\"80\" height=\"70\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"185.0\" y=\"62.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Fundamental Matrix\nN = (I - Q)^{-1}\n=</text><text x=\"185.0\" y=\"70.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">I + Q + Q^2 + ...\nN_ij = E[visits to j]</text><text x=\"120\" y=\"122\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Q^n \u2192 0 as n \u2192 \u221e: transient states are abandoned with probability 1</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Canonical form partitions P into transient block Q and absorbing block R; N = (I - Q)^(-1)</text></svg>",
    "drawingCaption": "The fundamental matrix N = (I - Q)^{-1} sums the geometric series of transient transitions, tallying expected visit counts",
    "coreTranslation": [
      "<strong>Canonical Partitioning:</strong> Reordering states into $t$ transient states followed by $r$ absorbing states formats transition matrix $P$ as $P = \\begin{pmatrix} Q & R \\\\ 0 & I_r \\end{pmatrix}$, where $Q$ governs internal transient jumps and $R$ governs transitions into absorbing sinks.",
      "<strong>Fundamental Matrix Definition:</strong> Because transient states are eventually abandoned ($Q^n \\to 0$ as $n \\to \\infty$), the matrix Neumann series converges: $N = \\sum_{k=0}^\\infty Q^k = (I - Q)^{-1}$, termed the Fundamental Matrix of the absorbing chain.",
      "<strong>Occupancy Counting Meaning:</strong> Entry $N_{ij}$ equals the exact expected number of visits to transient state $j$ prior to absorption, given the process initialized in transient state $i$: $N_{ij} = \\mathbb{E}\\left[\\sum_{n=0}^\\infty \\mathbf{1}_{\\{X_n = j\\}} \\,\\middle|\\, X_0 = i\\right]$."
    ],
    "math": "$$P = \\begin{pmatrix} Q & R \\\\ 0 & I \\end{pmatrix} \\implies N = \\sum_{k=0}^\\infty Q^k = (I - Q)^{-1}, \\quad N_{ij} = \\mathbb{E}[\\text{Visits to } j \\mid X_0 = i]$$",
    "personalConnection": "Video game replay counter: N_ij records how many times a player passes through checkpoint j on attempts originating from stage i before reaching game over or victory.",
    "examTrap": "Forgetting that N_ii \u2265 1 always! When starting in state i, step n=0 counts as a visit to state i (1_{X_0=i} = 1), so the diagonal entries of N are always at least 1, even if Q_ii = 0."
  },
  {
    "id": 32104,
    "subject": "StoMA",
    "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
    "topicTitle": "21 \u00b7 Absorption & Mean Hitting Times",
    "cardNumber": "04",
    "category": "MATRIX ABSORPTION CALCULUS",
    "highlighterClass": "highlight-purple",
    "title": "Absorption Probabilities B = NR & Lifetime Vector",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32104\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"15\" y=\"30\" width=\"55\" height=\"45\" rx=\"0\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"42.5\" y=\"51.5\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Transient Start\nState</text><text x=\"42.5\" y=\"60.0\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">i\n(Vector e_i)</text><line x1=\"70\" y1=\"52\" x2=\"95\" y2=\"52\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32104)\"/><rect x=\"95\" y=\"25\" width=\"55\" height=\"55\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"122.5\" y=\"51.5\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Matrix</text><text x=\"122.5\" y=\"60.5\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">N\nTransient\nVisits\n(t \u00d7 t)</text><line x1=\"150\" y1=\"52\" x2=\"175\" y2=\"52\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-32104)\"/><rect x=\"175\" y=\"25\" width=\"52\" height=\"55\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"201.0\" y=\"51.5\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Matrix R\nEscape</text><text x=\"201.0\" y=\"60.5\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Jumps\n(t \u00d7 r)</text><rect x=\"25\" y=\"92\" width=\"90\" height=\"26\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"70\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">B = N R (Absorption)</text><rect x=\"125\" y=\"92\" width=\"90\" height=\"26\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"170\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">t = N 1 (Time Vector)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Complete absorption calculus: B = NR yields destination probabilities; t = N1 yields expected lifetimes</text></svg>",
    "drawingCaption": "Matrix multiplication resolves all absorption destinations simultaneously: B = NR and total lifetime t = N1",
    "coreTranslation": [
      "<strong>Destination Matrix Product $B = NR$:</strong> The $(t \\times r)$ matrix $B$ provides exact absorption probabilities: $B_{ik} = P(\\text{absorbed in state } k \\mid X_0 = i) = (NR)_{ik}$. Every row of $B$ sums to 1 if absorption occurs with probability 1 from all transient states.",
      "<strong>Expected Time to Absorption Vector:</strong> The total duration spent wandering through all transient states before absorption is obtained by summing expected visits across all transient states: $t_i = \\sum_{j \\in T} N_{ij} = (N \\mathbf{1})_i$.",
      "<strong>Direct Computational Advantage:</strong> Inverting a single $(t \\times t)$ matrix $(I - Q)$ simultaneously evaluates absorption probabilities into all sinks and expected lifetimes from all starting states, eliminating piecemeal linear equations."
    ],
    "math": "$$B = N R \\implies B_{ik} = P(\\text{Absorbed into } k \\mid X_0 = i); \\quad \\mathbf{t} = N \\mathbf{1} \\implies t_i = \\mathbb{E}[\\tau_{\\text{abs}} \\mid X_0 = i]$$",
    "personalConnection": "Hospital patient triage: N tracks average visits to medical wards, R represents discharge vs mortality rates, and NR computes overall survival probability from admission.",
    "examTrap": "Multiplying RN instead of NR! The dimensions must align: N is (t \u00d7 t) and R is (t \u00d7 r), so NR produces a (t \u00d7 r) matrix mapping transient starting states to absorbing destinations. RN is undefined!"
  },
  {
    "id": 32105,
    "subject": "StoMA",
    "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
    "topicTitle": "21 \u00b7 Absorption & Mean Hitting Times",
    "cardNumber": "05",
    "category": "GAMBLER'S RUIN",
    "highlighterClass": "highlight-cyan",
    "title": "Gambler\u2019s Ruin: Difference Equations & Drift Regimes",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32105\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"25\" y1=\"115\" x2=\"215\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32105)\"/><line x1=\"25\" y1=\"115\" x2=\"25\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32105)\"/><text x=\"220\" y=\"115\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">i</text><text x=\"20\" y=\"22\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a_i</text><circle cx=\"25\" cy=\"30\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"25\" y=\"126\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0 (Ruin)</text><circle cx=\"210\" cy=\"115\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"210\" y=\"126\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">N (Win)</text><line x1=\"25\" y1=\"30\" x2=\"210\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"145\" y=\"75\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">p = 1/2 (Linear)</text><path d=\"M 25,30 Q 140,40 210,115\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"3 3\"/><text x=\"80\" y=\"48\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">p &lt; 1/2 (High ruin)</text><path d=\"M 25,30 Q 60,110 210,115\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"2 2\"/><text x=\"100\" y=\"105\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">p > 1/2 (Low ruin)</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Gambler's ruin: linear a_i = 1 - i/N for fair coin; exponential a_i = (\u03c1^i - \u03c1^N)/(1 - \u03c1^N) with \u03c1 = q/p</text></svg>",
    "drawingCaption": "Second-order difference equations yield exact closed-form ruin probabilities across fair and asymmetric coin tosses",
    "coreTranslation": [
      "<strong>Difference Equation Formulation:</strong> Let $a_i$ be the probability of ruin starting with $\\$i$. First-step conditioning gives $a_i = p a_{i+1} + q a_{i-1}$ with boundary conditions $a_0 = 1$ and $a_N = 0$. The characteristic ratio is $\\rho = q/p$.",
      "<strong>Closed-Form Ruin Probability:</strong> Solving the homogeneous difference equation yields $a_i = \\frac{\\rho^i - \\rho^N}{1 - \\rho^N}$ when $p \\ne q$. In a fair game ($p = q = 1/2$, $\\rho = 1$), L'H\u00f4pital's limit yields the linear ruin probability $a_i = 1 - \\frac{i}{N}$.",
      "<strong>Expected Game Duration:</strong> The mean time until the game ends is $\\mu_i = \\frac{i}{q - p} - \\frac{N}{q - p} \\left(\\frac{1 - \\rho^i}{1 - \\rho^N}\\right)$ for $p \\ne q$, simplifying to parabolic duration $\\mu_i = i(N - i)$ for a fair coin ($p = 1/2$)."
    ],
    "math": "$$a_i = \\begin{cases} \\frac{(q/p)^i - (q/p)^N}{1 - (q/p)^N} & p \\ne q \\\\ 1 - \\frac{i}{N} & p = q = \\frac{1}{2} \\end{cases}; \\quad \\mu_i = i(N - i) \\quad (\\text{if } p = 1/2)$$",
    "personalConnection": "Casino betting bankroll: even with a slight house edge (p = 0.49), the exponential ruin formula demonstrates near certainty of bankruptcy before doubling a stake.",
    "examTrap": "Using the biased formula when p = 1/2! Substituting p = q = 1/2 into (\u03c1^i - \u03c1^N)/(1 - \u03c1^N) gives indeterminate 0/0. For p = 1/2, the solution is linear a_i = 1 - i/N, not exponential!"
  },
  {
    "id": 32106,
    "subject": "StoMA",
    "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
    "topicTitle": "21 \u00b7 Absorption & Mean Hitting Times",
    "cardNumber": "06",
    "category": "PATTERN WAITING TIMES",
    "highlighterClass": "highlight-amber",
    "title": "Pattern Waiting Times & The Self-Overlap Paradox",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-32106\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><text x=\"25\" y=\"35\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">HT:</text><circle cx=\"50\" cy=\"32\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"50\" y=\"35\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2205</text><line x1=\"60\" y1=\"32\" x2=\"85\" y2=\"32\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-32106)\"/><text x=\"72\" y=\"26\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H</text><circle cx=\"95\" cy=\"32\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"95\" y=\"35\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H</text><line x1=\"105\" y1=\"32\" x2=\"130\" y2=\"32\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-32106)\"/><text x=\"117\" y=\"26\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">T</text><rect x=\"130\" y=\"20\" width=\"36\" height=\"24\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"148.0\" y=\"35.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">HT</text><path d=\"M 95,22 C 90,8 100,8 97,20\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32106)\"/><text x=\"95\" y=\"6\" font-size=\"6.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H</text><text x=\"190\" y=\"32\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[T_HT] = 4</text><text x=\"25\" y=\"90\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">HH:</text><circle cx=\"50\" cy=\"87\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"50\" y=\"90\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2205</text><line x1=\"60\" y1=\"87\" x2=\"85\" y2=\"87\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-32106)\"/><text x=\"72\" y=\"81\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H</text><circle cx=\"95\" cy=\"87\" r=\"10\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"95\" y=\"90\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H</text><line x1=\"105\" y1=\"87\" x2=\"130\" y2=\"87\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-32106)\"/><text x=\"117\" y=\"81\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H</text><rect x=\"130\" y=\"75\" width=\"36\" height=\"24\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"148.0\" y=\"90.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">HH</text><path d=\"M 95,97 C 80,120 65,120 52,99\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-32106)\"/><text x=\"75\" y=\"122\" font-size=\"7\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">T (Full reset!)</text><text x=\"190\" y=\"87\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">E[T_HH] = 6</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Pattern waiting time paradox: E[T_HH] = 6 > E[T_HT] = 4 due to destructive resets upon mismatch</text></svg>",
    "drawingCaption": "Destructive prefix resets cause equal-probability patterns to exhibit radically different expected arrival times",
    "coreTranslation": [
      "<strong>Prefix State Automata:</strong> Model the occurrence of sequence pattern $W$ as hitting time of an absorbing Markov chain whose states represent the longest matched prefix of $W$. Transitions follow incoming coin tosses.",
      "<strong>The $HT$ vs $HH$ Paradox:</strong> In fair coin tosses, $\\mathbb{E}[T_{HT}] = 4$ whereas $\\mathbb{E}[T_{HH}] = 6$. For $HT$: if an $H$ is followed by $H$, the match prefix remains length 1 ($H$), maintaining forward readiness. For $HH$: if $H$ is followed by $T$, the prefix collapses completely to $\\emptyset$.",
      "<strong>Conway\u2019s Pattern Leading Number Rule:</strong> The expected waiting time for any binary pattern $W$ of length $k$ is $\\mathbb{E}[T_W] = \\sum_{j=1}^k c_j 2^j$, where $c_j = 1$ if the prefix of length $j$ matches the suffix of length $j$ (self-overlap), and 0 otherwise."
    ],
    "math": "$$\\mathbb{E}[T_{HT}] = 4 \\quad \\text{vs} \\quad \\mathbb{E}[T_{HH}] = 6; \\quad \\mathbb{E}[T_W] = \\sum_{j=1}^k c_j 2^j \\quad (\\text{Conway's Theorem})$$",
    "personalConnection": "DNA sequence motif search: searching for repetitive sequences like 'AAA' takes significantly longer than non-overlapping motifs 'ATG' due to wasted partial matches resetting upon mismatches.",
    "examTrap": "Assuming equally likely sequences have equal expected waiting times! At any two consecutive flips, P(HT) = P(HH) = 1/4, but waiting times differ fundamentally due to renewal regeneration: after seeing HH, another H immediately completes the next HH in 1 flip, clustering occurrences together!"
  }
]
);
