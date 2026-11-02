"""DIP topic 20 (CNNs). Everyday picture: a street camera on a pole learning what it sees."""
from street_lib import *

SUBJECT = "DIP"

def grid(x, y, n, s, fill="#ffffff", hl=None):
    out = []
    for i in range(n):
        for j in range(n):
            out.append(R(x + j * s, y + i * s, s, s, "#d9dee7" if hl and hl(i, j) else fill, .6))
    return out

def d3191(c):
    out = grid(10, 14, 6, 9, hl=lambda i, j: 1 <= i <= 3 and 1 <= j <= 3) + [N(37, 78, "input H × W", 6.5), arrow(66, 42, 84, 42, 1)]
    out += grid(90, 24, 3, 9, "#f1f5f9") + [N(103, 62, "K × K filter", 6.5), N(103, 74, "shared weights", 6.5), arrow(122, 42, 140, 42, 1)]
    out += grid(146, 20, 4, 9, hl=lambda i, j: i == 1 and j == 1) + [N(164, 66, "output H′ × W′", 6.5),
            N(120, 94, "H′ = ⌊(H − K + 2P) / S⌋ + 1", 8), N(120, 108, "params = K² C_in F + F", 8),
            N(120, 122, "same filter at every place: finds a pattern anywhere", 7), N(120, 136, "CNN 'convolution' is really cross-correlation", 7)]
    return svg(c, *out)

def d3192(c):
    out = []
    for i, (n, x) in enumerate(((7, 10), (5, 78), (3, 136))):
        s = 8
        out += grid(x, 14 + (7 - n) * s / 2, n, s, hl=(lambda a, b: True) if i == 2 else None)
        if i < 2: out.append(arrow(x + n * s + 2, 42, x + n * s + 12, 42, 1))
    out += [C(222, 42, 4), N(222, 56, "one unit", 6.5), N(36, 78, "5 × 5 RF", 6.5), N(100, 78, "3 × 3", 6.5), N(150, 78, "1", 6.5),
            N(120, 96, "RFₗ = RFₗ₋₁ + (Kₗ − 1) Π Sᵢ", 8), N(120, 110, "two 3×3 convs see 5×5 with 18C² not 25C² weights", 7.5),
            N(120, 124, "pooling 2×2 / 2 halves size, doubles later growth", 7.5), N(120, 138, "count the product of earlier strides", 7.5)]
    return svg(c, *out)

def d3193(c):
    out = [axes(14, 70, 100, 10), axes(14, 70, 100, 10)] if False else [axes(18, 62, 90, 12)]
    out += [L(18, 62, 58, 62, 1.4), L(58, 62, 100, 22, 1.4), N(60, 74, "ReLU", 7), N(30, 12, "max(0, x)", 7, "start"),
            curve([(130 + i * 3, 62 - 40 / (1 + 2.718 ** (-(i - 15) / 4))) for i in range(0, 31)], 1.2) if False else L(130, 60, 170, 24, 1.2),
            N(150, 74, "σ saturates", 6.5), R(176, 20, 54, 46, "#f1f5f9", 1), N(203, 34, "σ′ ≤ ¼", 8), N(203, 48, "¼ⁿ → 0", 7.5), N(203, 60, "vanishing", 6.5),
            N(120, 94, "∂L/∂Wₗ = δₗ aₗ₋₁ᵀ", 8), N(120, 108, "no nonlinearity: stacked convs collapse to one", 7.5),
            N(120, 122, "ReLU gradient is 1 for x > 0; dead units if x < 0", 7.5), N(120, 136, "He init keeps half the units alive", 7.5)]
    return svg(c, *out)

def d3194(c):
    out = []
    names = (("LeNet", 5), ("AlexNet", 8), ("VGG", 19), ("GoogLeNet", 22), ("ResNet", 152))
    for i, (nm, dep) in enumerate(names):
        h = max(6, dep ** .5 * 4.6)
        out += [R(16 + i * 44, 66 - h, 30, h, "#d9dee7" if i == 4 else "#f1f5f9", .8), N(31 + i * 44, 76, nm, 5.5), N(31 + i * 44, 62 - h, str(dep), 6.5)]
    out += [N(120, 94, "depth: 5 → 8 → 16–19 → 22 → 152", 8), N(120, 108, "AlexNet: ReLU, dropout, GPUs;  VGG: only 3×3", 7.5),
            N(120, 122, "1×1 conv mixes channels, cuts parameters", 7.5), N(120, 136, "deeper plain nets trained worse: degradation", 7.5)]
    return svg(c, *out)

def d3195(c):
    return svg(c,
        N(20, 36, "x", 8), arrow(26, 36, 50, 36, 1), R(50, 22, 66, 28, "#f1f5f9", 1), N(83, 34, "F(x)", 8), N(83, 45, "conv · ReLU · conv", 5.5),
        arrow(116, 36, 150, 36, 1), C(158, 36, 7, "#ffffff", 1), N(158, 39, "+", 9), arrow(165, 36, 190, 36, 1), N(202, 36, "y", 8),
        L(34, 36, 34, 70, 1), L(34, 70, 158, 70, 1), arrow(158, 70, 158, 44, 1), N(96, 66, "identity shortcut", 6.5),
        N(120, 92, "y = F(x) + x ,  ∂y/∂x = ∂F/∂x + I", 8), N(120, 106, "learn the residual F = H − x; identity means F → 0", 7.5),
        N(120, 120, "the + I term is a direct path for gradients", 7.5), N(120, 134, "shapes must match, else 1×1 projection on shortcut", 7))

def d3196(c):
    out = grid(10, 12, 7, 8) + [N(38, 76, "224×224×3", 6.5), arrow(70, 40, 88, 40, 1), N(79, 34, "7×7 / 2", 6, "middle")]
    out += grid(94, 18, 4, 9, "#f1f5f9") + [N(112, 62, "112×112×64", 6.5),
            N(190, 22, "H′ = ⌊(224−7+6)/2⌋+1", 7, "middle"), N(190, 36, "= 111 + 1 = 112", 7.5), N(190, 52, "7·7·3·64 = 9 408", 7.5), N(190, 64, "+ 64 biases = 9 472", 7.5),
            N(120, 92, "params do not depend on H or W", 8), N(120, 106, "weight sharing: same filter slides over the frame", 7.5),
            N(120, 120, "forgetting the biases gives 9 408", 7.5), N(120, 134, "counting H·W in the parameters is the usual slip", 7.5)]
    return svg(c, *out)

CARDS = {
3191: dict(d=d3191, stmtKind="DEFINITION",
  statement=r"<b>Convolution layer.</b> Each output unit sees only a $K\times K$ patch of the input and all positions share the same $F$ filters. For input size $H$, padding $P$ and stride $S$ the output size is $H'=\big\lfloor\frac{H-K+2P}{S}\big\rfloor+1$, and the layer has $K^2C_{\rm in}F+F$ parameters, independent of the image size. (Implemented as cross-correlation, without flipping the kernel.)",
  hint="Why does a network that looks at the street frame in small patches need so few weights?",
  breakdown=[r"<strong>$K\times K$ patch = local connectivity.</strong> Each output looks at a small neighbourhood, not the whole frame."],
  conn=r"<strong>One lamp detector, everywhere.</strong> The same small filter slides over the whole street frame, so a lamp-post edge is found wherever it stands, with no extra weights per position.",
  cap="A K × K filter slides over the input frame; each position gives one output value, and the same weights are used at every position."),
3192: dict(d=d3192, stmtKind="DEFINITION",
  statement=r"<b>Receptive field.</b> The input region influencing one unit grows as $\mathrm{RF}_l=\mathrm{RF}_{l-1}+(K_l-1)\prod_{i\lt l}S_i$. $L$ stacked $3\times3$ stride-1 convolutions give $(2L+1)\times(2L+1)$; two of them match one $5\times5$ with $2\cdot9C^2$ rather than $25C^2$ weights. Pooling (e.g. $2\times2$, stride 2) halves the spatial size and adds slight translation invariance.",
  hint="How can a unit deep in the network 'see' a large part of the street from small filters?",
  breakdown=[r"<strong>$\mathrm{RF}_l=\mathrm{RF}_{l-1}+(K_l-1)\prod S_i$ = how far it sees.</strong> Each layer adds its kernel reach, scaled by all earlier strides."],
  conn=r"<strong>From a pixel to a bus.</strong> A first-layer unit sees a three-pixel dot; five layers later a unit sees a window big enough to include a whole bus or a lamp-post.",
  cap="Three stacked layers: one deep unit depends on a 3 × 3 patch of the layer below, which depends on a 5 × 5 patch of the input."),
3193: dict(d=d3193, stmtKind="DEFINITION",
  statement=r"<b>Activations and gradient flow.</b> Without a nonlinearity, stacked convolutions collapse to one linear map. $\mathrm{ReLU}(x)=\max(0,x)$ has gradient 1 for $x\gt0$ and does not saturate; the sigmoid has $\sigma'=\sigma(1-\sigma)\le\tfrac14$, so gradients shrink by at least $4$ per layer. Backpropagation gives $\partial L/\partial W_l=\delta_l\,a_{l-1}^T$.",
  hint="Why did networks with sigmoids stop learning once they got deep?",
  breakdown=[r"<strong>$\max(0,x)$ = ReLU.</strong> Passes positive values unchanged, so its gradient is 1 there and training is fast; units with always-negative input are 'dead'."],
  conn=r"<strong>Passing the signal back.</strong> The camera's error at the output must travel back through every layer to its first filters. With sigmoids it fades to nothing; with ReLU it arrives intact.",
  cap="ReLU is flat then a straight line; the sigmoid saturates, with σ′ ≤ ¼, so the gradient shrinks by ¼ or more each layer."),
3194: dict(d=d3194, stmtKind="HISTORY",
  statement=r"<b>From LeNet to ResNet.</b> LeNet-5 (1998) set the pattern conv, pooling, fully-connected. AlexNet (2012) used ReLU, dropout and GPUs; VGG (2014) showed depth with only $3\times3$ filters; GoogLeNet (2014) used parallel branches and $1\times1$ convolutions $C_{\rm in}\to C_{\rm out}$ to cut parameters; ResNet (2015) added identity skip connections, making 50–152 layers trainable.",
  hint="Why did making a network deeper hurt before skip connections existed?",
  breakdown=[r"<strong>Depth $5\to8\to19\to22\to152$ = the trend.</strong> Each step added something: ReLU and dropout, small filters, 1×1 mixing, skip connections."],
  conn=r"<strong>A better and better street camera.</strong> Each model sees the same frames but with more layers; until skip connections, doubling the depth made the camera worse, even on its training frames.",
  cap="Depth of LeNet, AlexNet, VGG, GoogLeNet and ResNet (5, 8, 19, 22, 152 layers). Only ResNet's skip connections made the last jump trainable."),
3195: dict(d=d3195, stmtKind="THEOREM",
  statement=r"<b>Residual block.</b> Instead of learning $H(x)$, learn $F(x)=H(x)-x$ and output $y=F(x,\{W_i\})+x$. Then $\partial y/\partial x=\partial F/\partial x+I$, so the gradient has a direct path through $+I$ and does not vanish with depth. The shortcut is the identity if shapes match, otherwise a $1\times1$ projection; bottleneck blocks ($1\times1$, $3\times3$, $1\times1$) keep deep nets cheap.",
  hint="What is the easiest thing for a block to learn if it has nothing useful to add?",
  breakdown=[r"<strong>$y=F(x)+x$ = add a correction to the input.</strong> The block only learns what to change; to do nothing, push $F\to0$."],
  conn=r"<strong>Fixing the camera's guess.</strong> The previous layers already give a decent view of the street; each block adds a small correction on top instead of re-describing the whole scene.",
  cap="The input x goes through F(x) (conv, ReLU, conv) and also along an identity shortcut; the two are added to give y = F(x) + x."),
3196: dict(d=d3196, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example (ResNet stem).</b> Input $224\times224\times3$, kernel $7\times7$, stride $2$, padding $3$, $F=64$: $H'=\lfloor(224-7+2\cdot3)/2\rfloor+1=\lfloor223/2\rfloor+1=112$, giving a $112\times112\times64$ map, with $7\cdot7\cdot3\cdot64+64=9\,408+64=9\,472$ parameters.",
  hint="Count the size and the weights of the first layer a street frame meets.",
  breakdown=[r"<strong>$\lfloor(224-7+6)/2\rfloor+1=112$ = output size.</strong> Padding 3 adds 6, the kernel takes 7 away, stride 2 halves (rounding down), plus one."],
  conn=r"<strong>The first layer on one frame.</strong> A 224-pixel frame goes in and 64 feature maps of 112 pixels come out. All 9 472 weights are the same wherever the filter sits on the street.",
  cap="A 224 × 224 × 3 frame goes through 64 filters of size 7 × 7 with stride 2 and padding 3, giving 112 × 112 × 64 and 9 472 parameters."),
}
CARDS[3191]["breakdown"] += [r"<strong>$K^2C_{\rm in}F+F$ = parameters.</strong> One $K\times K\times C_{\rm in}$ filter per output channel, plus a bias each; none depends on $H$ or $W$.",
                             r"<strong>$H'=\lfloor(H-K+2P)/S\rfloor+1$ = output size.</strong> Padding $P$ keeps the border, stride $S$ skips positions. A fully connected layer on a $224\times224\times3$ frame would need about 150 thousand weights per neuron."]
CARDS[3192]["breakdown"] += [r"<strong>$2\cdot(3\times3)\equiv5\times5$ = same view, fewer weights.</strong> $2\cdot9C^2$ against $25C^2$, plus an extra nonlinearity; this is why VGG uses only $3\times3$.",
                             r"<strong>Pooling = shrink and be forgiving.</strong> Max pooling keeps the strongest response and gives slight translation invariance. Count the product of earlier strides, not just kernel sizes."]
CARDS[3193]["breakdown"] += [r"<strong>$\sigma'\le\frac14$ = vanishing gradients.</strong> Each sigmoid layer multiplies the gradient by at most a quarter; ten layers leave under a millionth.",
                             r"<strong>$\partial L/\partial W_l=\delta_la_{l-1}^T$ = what each filter is told.</strong> The error $\delta_l$ from above times the input from below; a dead ReLU gives it zero. He initialisation avoids starting half the units dead."]
CARDS[3194]["breakdown"] += [r"<strong>$1\times1$ conv = channel mixing.</strong> Maps $C_{\rm in}\to C_{\rm out}$ at each pixel with no spatial blur; GoogLeNet used it to cut parameters.",
                             r"<strong>Degradation problem.</strong> Plain deeper nets had worse <i>training</i> error, so it is not overfitting. Skip connections fixed it, giving about 3.6% top-5 error on ImageNet (ensemble)."]
CARDS[3195]["breakdown"] += [r"<strong>$\partial y/\partial x=\partial F/\partial x+I$ = a gradient highway.</strong> The $+I$ passes the error straight back, so it does not vanish however deep the network.",
                             r"<strong>Same shape before adding.</strong> If channels or stride change, use a $1\times1$ projection on the shortcut, not on $F(x)$. Bottleneck blocks (1×1, 3×3, 1×1) keep 152 layers affordable."]
CARDS[3196]["breakdown"] += [r"<strong>$7\cdot7\cdot3\cdot64=9\,408$ = the weights.</strong> A $7\times7\times3$ filter for each of the 64 output channels.",
                             r"<strong>$+64=9\,472$ = add the biases.</strong> Forgetting them gives 9 408. Counting $H\cdot W$ in the total is the common mistake: sharing makes the count independent of the frame size."]

STORY = {
 3191: dict(s="STORY 7 · STEP 19 · LEARNED FILTERS", b="Let the network <b>learn the filters</b> instead of designing them, and slide them over the frame.",
   f=[["3185", "hand-made Haar features"], ["3051", "spatial filtering"]], n=[["3192", "how far it sees"]]),
 3192: dict(s="STORY 7 · STEP 20 · HOW FAR IT SEES", b="Stacked layers and <b>pooling</b> widen each unit's view.",
   f=[["3191", "one layer"]], n=[["3193", "the nonlinearity"]]),
 3193: dict(s="STORY 7 · STEP 21 · KEEP THE SIGNAL", b="<b>ReLU</b> keeps gradients alive; sigmoids let them fade.",
   f=[["3192", "deep stacks"]], n=[["3194", "the history"]]),
 3194: dict(s="STORY 7 · STEP 22 · DEEPER, BUT HOW", b="From LeNet to ResNet: each step solved a problem, <b>skip connections</b> solved depth.",
   f=[["3193", "gradients"]], n=[["3195", "the residual block"]]),
 3195: dict(s="STORY 7 · STEP 23 · LEARN THE CORRECTION", b="<b>y = F(x) + x</b>: the shortcut keeps gradients flowing.",
   f=[["3194", "degradation"]], n=[["3196", "numbers"]]),
 3196: dict(s="STORY 7 · STEP 24 · CHECK BY HAND", b="$112\\times112\\times64$ and $9\\,472$ parameters: the end of the series.",
   f=[["3191", "size and parameter formulas"]], n=[]),
}
FIX = build_fix(CARDS)
