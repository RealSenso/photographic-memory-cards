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
  }
]
);
