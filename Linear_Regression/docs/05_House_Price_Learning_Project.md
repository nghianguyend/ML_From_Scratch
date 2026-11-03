# One project: infer a synthetic house-price rule

This is a controlled mathematical experiment, not a real property valuation tool. You will create all data-generation and model code yourself. The specification gives reproducible choices, expected behavior, and checks—not a completed implementation.

## The question

Can your own gradient descent recover a linear size–price relationship, and can you distinguish optimization error from unavoidable observation noise?

Use size s in square metres and price y in **thousands of currency units**. The generating rule is

\[
y_i = 50 + 3s_i + \epsilon_i.
\]

The slope means 3 thousand units per additional square metre. The intercept is a mathematical extrapolation at zero size; it is not a plausible sale price for a zero-size house.

## Stage A — Create a reproducible experiment

1. Create a NumPy random generator with seed 42. Generate 160 sizes independently from a uniform distribution between 30 and 200. Keep them as a floating-point vector of shape (160,).
2. Generate 160 independent standard-normal draws z. Define noise as ε = σz. First use σ = 0; later use σ = 20. Keeping z fixed lets you change noise amplitude without also changing its pattern.
3. Construct prices from the rule above. Record the units and shapes. Do not round targets before training.
4. Using the same generator after those draws, permute example indices once. Use the first 120 indices for training and the remaining 40 for testing. Preserve the pairing of size and price. Record the random seed and draw order.
5. Plot training and test points with different markers. Overlay the known generating line only for diagnosis. Real datasets do not reveal this true line.

**Challenge:** predict the price change when size increases from 80 to 100 m². Explain why the noisy change for two individual houses need not equal the signal change.

**Checks:** correct shapes, 160 distinct index assignments without overlap, all sizes in the specified interval, no nonfinite values. For σ = 0, subtracting 50 + 3s from every target should give zeros within rounding precision.

## Stage B — Scale before training

Large raw sizes produce steep curvature in some parameter directions. Estimate μ = mean(training sizes) and τ = population standard deviation of training sizes (NumPy's default ddof = 0). If τ is zero, do not divide: the slope cannot be identified from constant size.

Define standardized size u = (s − μ)/τ. Apply the same training μ and τ to test and future sizes; do not recompute them on the test set. Keep prices in thousands.

Train the model yhat = a u + c. After fitting, convert back:

\[
w_{\mathrm{raw}}=a/\tau,\qquad b_{\mathrm{raw}}=c-a\mu/\tau.
\]

**Derive this yourself** by substituting u into a u + c and collecting the coefficient of s and the constant term.

**Checks:** mean(u_train) is approximately zero and mean(u_train²) approximately one. At σ = 0 the exact standardized parameters are a = 3τ and c = 50 + 3μ. Raw and standardized predictions must agree after parameter conversion.

## Stage C — Build only what you understand

Implement predictions, full MSE, the two gradients, one simultaneous update, and then the training loop in that order. Before this dataset, pass the tiny numerical checks in the roadmap. Use no automatic differentiation and no regression estimator for your own training routine.

Start with a = c = 0 and α = 0.1 for the standardized one-feature model. Use a maximum of 2,000 iterations as a safety cap; choose and report a stopping tolerance after examining the objective scale. Record the final stopping reason and gradient norm. Do not call a capped run “converged” without additional evidence.

Here the training design columns u and 1 are orthogonal with squared norms m, so the full-MSE Hessian is approximately 2I. The fixed-step stability bound is therefore 0 < α < 1. This bound applies to this standardized one-feature setup, not every regression dataset.

**Challenge:** α = 1/2 has a special property for this exact quadratic with standardized training inputs. Derive the update's parameter-error multiplier and predict what one iteration should do. Test the prediction only after deriving it.

**Checks:** analytic gradients versus central finite differences; finite parameters throughout; decreasing training loss for a suitable step; the final model evaluated again from scratch gives the recorded final loss.

## Stage D — Verify against an independent reference

After your model passes tiny tests, assemble a training design matrix B with one column of standardized sizes and one column of ones. Its shape is (120,2). Use `numpy.linalg.lstsq` as a numerical reference, with `rcond=None`; inspect its returned solution, rank, and singular values. Its returned residual summary is not automatically MSE—calculate MSE yourself from predictions.

Compare the parameter pair [a,c], training predictions, and training MSE from your algorithm with that reference. Tight agreement is reasonable here because the standardized columns are well-conditioned; choose a tolerance consistent with your stopping accuracy. An absolute parameter tolerance around 10⁻⁵ is a possible target after sufficient iterations, not a universal guarantee.

Optional second reference: scikit-learn's `LinearRegression`, using a single feature column and its default intercept. Do not also add a ones column unless you explicitly disable its separate intercept. Compare equivalent data and conventions.

**Expected behavior:** with σ = 0, recover raw slope 3, intercept 50, and approximately zero training/test error. With σ = 20, agree with the sample's least-squares optimum, which generally is not exactly [3,50]. A wrong algorithm can sometimes achieve plausible-looking parameters; use all the checks.

## Stage E — Evaluate predictions, not only parameters

Evaluate your final training and test predictions once. Report MSE and RMSE separately. MSE has squared price units; RMSE is in thousands, so multiplying RMSE by 1,000 converts it to currency units. Also report mean signed residual, using r = prediction − observation throughout.

Create three plots: size versus price with the fitted line; training loss versus update count; residual versus size (optionally residual versus fitted price). Evaluate the line on a sorted grid so it does not zigzag.

Interpretation prompts:

- Positive residual means overprediction. Which examples have the largest absolute errors?
- At the unconstrained training least-squares optimum with an intercept, mean training residual is approximately zero. Why does this not force the mean **test** residual to zero?
- Why is Σ u_i r_i approximately zero on training data at the optimum? Connect it to the slope gradient.
- A curved residual pattern suggests a missing nonlinear relationship. A widening spread suggests nonconstant noise variance. Neither conclusion follows reliably from one or two points.
- With independent noise of standard deviation 20, the noise variance is 400 in squared-thousands units. Finite-sample training MSE need not equal 400; fitting uses some noise, and test error also reflects parameter estimation. Do not enforce 400 as a unit test.

## Stage F — Controlled challenges

| Variation | What to change yourself | Prediction to justify before running |
|---|---|---|
| Learning rate | Try 0.01, 0.1, 0.9, and 1.1 with fixed standardized data | Which converge, oscillate while shrinking, or diverge? Use Hessian eigenvalues. |
| More noise | Keep s and z fixed; compare σ = 0, 10, 20, 50 | Why does the best loss generally rise while individual realized metrics need not be monotonic? |
| Outlier | Add 300 thousand units to one **training** target | How does squaring residuals affect its influence? A central-size outlier and an extreme-size outlier can affect slope differently. |
| Second feature | Generate a varying integer bedroom count and add 15 × bedrooms to the signal | What changes in X, w, gradients, and the Hessian? Standardize feature columns separately. |
| Dependent features | Add a feature equal to 2 × size | Why are parameters nonunique even if predictions match? |
| Model mismatch | Add a small quadratic size term to the generating rule | Why can a correct linear optimizer still show structured residuals? |

## Your final deliverable to yourself

Write a short experiment note containing the generating rule, seed and split, shape contract, your gradient derivation, chosen scaling and α, stopping reason, three verification checks, train/test metrics, and residual interpretation. Include one failed attempt and how you diagnosed it. Be able to reproduce the experiment from a fresh process without notebook hidden state.

**Mastery question:** if your gradient matches finite differences but your reference MSE disagrees, what assumptions or data paths would you inspect next? Ask the debugging skill for one hint only after proposing your own hypotheses.

Reference API: [NumPy least squares](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html), checked 2 November 2026. The numerical experiment specification and exercises are original to this learning pack.
