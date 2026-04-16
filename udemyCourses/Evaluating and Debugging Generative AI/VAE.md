# Variational Autoencoder (VAE) Overview

## 1. What is a VAE

A **Variational Autoencoder (VAE)** is a type of **autoencoder** (a neural network that learns to compress and reconstruct data) with a probabilistic twist. Instead of encoding input into a fixed vector, it encodes input into a **distribution** over latent representations, allowing it to **generate new data** similar to the original dataset.

---

## 2. Core Components

### Encoder (Inference model)
- Maps input `x` to a **latent distribution**, usually a Gaussian with mean `μ` and variance `σ²`.
- Instead of a single point in latent space, you get a distribution:
  ```
z ~ N(μ(x), σ²(x))
  ```

### Decoder (Generative model)
- Samples `z` from the latent distribution and reconstructs the input `x`:
  ```
x' = Decoder(z)
  ```

---

## 3. Training a VAE

VAEs use **two losses** during training:

1. **Reconstruction Loss**
   - Measures how well the decoder reconstructs the input.
   - Example: Mean Squared Error (MSE) for images.

2. **KL Divergence Loss**
   - Forces the latent distribution to be close to a standard normal distribution `N(0, I)`:
     ```
KL(N(μ, σ²) || N(0,1))
     ```

**Total Loss** = Reconstruction Loss + KL Divergence Loss

---

## 4. Why "Variational"?

The "variational" part comes from **variational inference**, which approximates complex probability distributions. The VAE approximates the true latent distribution with a simpler Gaussian to make training feasible.

---

## 5. Applications
- **Image generation**: creating new faces, digits, etc.
- **Data compression**: learning efficient latent representations.
- **Anomaly detection**: inputs with low reconstruction likelihood may be anomalies.
- **Drug discovery / molecular generation**: generating plausible chemical structures.

---

## 6. Key Intuition
A VAE **learns the underlying structure of the data** rather than memorizing exact samples, allowing generation of new, similar examples.

