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
  }
]
);
