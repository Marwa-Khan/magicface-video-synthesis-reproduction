# Research Notes

## 1. Objective

This project reproduces the inference pipeline of MagicFace and
extends the experiment toward frame-based video facial expression
editing.

The goal was to investigate whether a still-image facial expression
editing model could be applied consistently across video frames.

## 2. Original Method

MagicFace performs facial expression editing using Action Units (AUs)
while attempting to preserve the identity of the input subject.

The reproduced pipeline uses Stable Diffusion v1.5 together with
MagicFace's identity and denoising components.

## 3. Reproduction

The original inference implementation was adapted to a Colab-based
environment.

A wrapper script was created to execute the original inference
pipeline while supplying the required local model paths and
environment configuration.

## 4. Expression Editing

The experiments tested individual and combined Action Units,
including examples such as:

- AU12
- AU6
- AU1 + AU2 + AU5

Different AU variation values were tested to investigate expression
editing behaviour.

## 5. Identity Evaluation

Identity similarity was evaluated on representative expression
editing results.

Example observed similarities included:

| Expression | Identity Similarity |
|---|---:|
| AU12_p3_smile | 0.8804 |
| mouth_AU25_AU26 | 0.8512 |
| AU4_p4_brow_lower | 0.8249 |
| sad_AU1_AU4_AU15 | 0.7706 |
| happy_AU6_AU12 | 0.7529 |
| AU12_p6_strong_smile | 0.7517 |

These values indicate that identity preservation varied across
different expression edits.

## 6. Video Experiment

A privately owned input video was processed frame-by-frame.

The original video contained:

- Resolution: 478 × 850
- FPS: approximately 30
- Duration: approximately 8.83 seconds
- Frames: 265

A subset of 27 frames was selected for the demonstration experiment.

Each selected frame was processed independently using the MagicFace
inference pipeline.

The edited frames were subsequently reconstructed into a video.

## 7. Frame-Level Comparison

The 27 original and edited frames were compared using basic pixel-level
statistics.

Observed results:

- Average mean pixel difference: 11.542
- Average changed-pixel percentage: 87.24%
- Maximum observed pixel difference: 238
- Frames with non-zero difference: 27/27

These measurements confirm that the generated frames were
substantially different from their corresponding input frames.

Pixel-level difference alone does not establish that the desired
facial expression was successfully generated; qualitative inspection
and identity/expression metrics are therefore also important.

## 8. Limitations

The video experiment was conducted on a subset of frames rather than
the complete source video.

The source video and generated video outputs are not included in this
public repository because the source material is privately owned.

The experiment should therefore be considered a reproduction and
proof-of-concept extension rather than a complete video synthesis
benchmark.

## 9. Reproducibility

The public repository contains the notebook, wrapper script,
environment requirements, and documentation required to understand
and reproduce the experiment using appropriate input data.

Private input media and generated visual outputs are available only
upon request where permission can be provided.