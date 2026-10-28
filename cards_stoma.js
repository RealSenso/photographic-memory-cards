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
  }
]
);
