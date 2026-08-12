## Research paper

> **MagicFace: High-Fidelity Facial Expression Editing with Action-Unit Control**  
> Mengting Wei, Tuomas Varanka, Xingxun Jiang, Huai-Qian Khor, Guoying Zhao  
> University of Oulu  
> [arXiv paper](https://arxiv.org/abs/2501.02260)


# MagicFace: Facial Expression Editing with Action-Unit Control

A research reproduction and video-oriented extension of **MagicFace**, a diffusion-based framework for high-fidelity facial expression editing using Facial Action Units (AUs).

This project was undertaken to reproduce the published MagicFace inference pipeline, evaluate its expression-editing behavior and identity preservation, and investigate its use in a frame-wise video setting.

---

## Project motivation

Facial expression synthesis is an important problem in computer vision, affective computing, and generative modeling.

MagicFace provides explicit control over facial expressions through **Facial Action Units (AUs)** rather than relying only on natural-language prompts. The objective is to modify facial expression while preserving the person's identity, pose, background, and other visual characteristics.

This project focuses on reproducing the published inference pipeline and exploring how an image-based expression editing model behaves when applied independently to video frames.

---

## Research paper

> **MagicFace: High-Fidelity Facial Expression Editing with Action-Unit Control**  
> Mengting Wei, Tuomas Varanka, Xingxun Jiang, Huai-Qian Khor, Guoying Zhao  
> University of Oulu  
> [arXiv paper](https://arxiv.org/abs/2501.02260)

This project is based on the publicly released implementation and pretrained model of the original MagicFace work.

The original MagicFace implementation and research are the work of the authors above. This repository is an **independent reproduction and experimental extension** focused on reproducing the inference pipeline and investigating its application to frame-wise video expression editing.

The original implementation should be cited when using or extending the MagicFace method.

---

## What was reproduced

The project reproduced the following components of the MagicFace workflow:

* Stable Diffusion 1.5 based inference
* MagicFace identity encoder
* MagicFace denoising network
* Action Unit conditioning
* Single-image expression editing
* Multiple AU combinations
* Different AU intensity values
* Identity preservation evaluation
* Frame-wise video expression editing

The original MagicFace architecture contains an identity encoder and an AU-conditioned denoising network. The AU representation contains 12 facial action units used to control expression changes.

---

## Experiments

### 1. Single-image inference

The official MagicFace inference pipeline was successfully executed using the released pretrained model.

Example AU conditions included:

* AU1 + AU4
* AU12
* AU6 + AU12
* AU1 + AU4 + AU15
* AU25 + AU26

Different AU intensity values were also tested.

---

### 2. Identity preservation

Identity preservation was evaluated using facial embedding similarity between the original and edited images.

Example results:

| Expression           | Identity similarity |
| -------------------- | ------------------: |
| AU12 p3 smile        |              0.8804 |
| AU25 + AU26          |              0.8512 |
| AU4 p4 brow lower    |              0.8249 |
| AU1 + AU4 + AU15     |              0.7706 |
| AU6 + AU12           |              0.7529 |
| AU12 p6 strong smile |              0.7517 |

The results indicate that identity information was retained to a substantial degree across the tested edits, while stronger or combined expression modifications could introduce greater identity deviation.

---

## 3. Video experiment

The image-based MagicFace pipeline was extended to a short video experiment using frame-wise processing.

The workflow was:

```text
Input video
    ↓
Frame extraction
    ↓
Frame selection
    ↓
MagicFace AU editing
    ↓
Edited frames
    ↓
Video reconstruction
    ↓
Original vs edited comparison
```

A total of **27 selected frames** were processed.

All 27 frames were successfully generated.

The experiment used the same AU condition across frames to investigate the behavior of frame-wise expression editing.

---

## Quantitative video comparison

Basic pixel-level statistics were computed between the original and edited frames.

Results:

| Metric                            |  Result |
| --------------------------------- | ------: |
| Frames compared                   |      27 |
| Average mean pixel difference     |  11.542 |
| Average changed-pixel percentage  |  87.24% |
| Maximum observed pixel difference |     238 |
| Frames with non-zero difference   | 27 / 27 |

These statistics confirm that the frame-wise pipeline produced substantial image-level changes.

However, pixel-level differences alone do **not** demonstrate correct AU manipulation or temporal consistency. They are therefore treated as basic verification statistics rather than a complete video-quality evaluation.

---

## Qualitative observations

The experiments demonstrated that the pretrained MagicFace model can be executed successfully and can generate visible expression modifications under different AU conditions.

The frame-wise video experiment also demonstrated that the image-based pipeline can be applied independently to multiple video frames.

The main limitation is that the original model performs image-level editing. Applying it independently to consecutive frames does not explicitly model temporal information.

This makes temporal consistency an important area for further investigation.

---

## Limitations

This project does not reproduce the original MagicFace training procedure from scratch.

The original work uses a large-scale training setup and pretrained components. This reproduction therefore focuses on:

* pretrained-model inference
* qualitative reproduction
* identity evaluation
* frame-wise video experimentation

The video experiment should not be interpreted as a reproduction of a dedicated video synthesis model.

Potential issues include:

* temporal flickering
* frame-to-frame appearance variation
* inconsistent expression intensity
* small identity changes
* background or boundary changes

These limitations motivate future work involving temporal consistency mechanisms.

---

## Reproducibility

The repository contains the experimental code and notebook used for the reproduction.

Large model checkpoints are not redistributed in this repository.

The experiments used Google Colab with GPU acceleration and persistent Google Drive storage for model and experiment files.

The notebook has been cleaned of generated outputs so that private experimental data is not embedded in the public repository.

---

## Private experimental data

The original video used for the video experiment is personally owned by the project author and is therefore **not included in this public repository**.

For the same reason, the repository does not contain:

* the original video
* extracted video frames
* edited frames
* generated videos
* private face images

The repository preserves the experiment structure and documentation without redistributing the underlying private media.

Selected results can be made available **for viewing upon request for research or recruitment evaluation**.

Private media and generated outputs may not be redistributed, republished, or reused without permission from the author.

---

## Repository structure

```text
magicface-au-video-reproduction/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── notebooks/
│   └── MagicFace_Reproduction.ipynb
│
├── scripts/
│   ├── run_magicface_inference_wrapper.py
│   ├── run_video_inference.py
│   ├── compute_identity_similarity.py
│   └── compute_frame_statistics.py
│
├── configs/
│   └── experiments.md
│
├── examples/
│   ├── input_images/
│   └── results/
│
├── results/
│   ├── identity_evaluation/
│   └── video_experiment/
│
└── docs/
    └── research_notes.md
```

Private experiment artifacts are intentionally excluded from the repository.

---

## Future work

Possible extensions include:

* AU detection-based expression verification
* stronger identity-preservation evaluation
* background preservation metrics
* temporal consistency metrics
* optical-flow-based temporal analysis
* temporal smoothing
* video diffusion or temporal-attention approaches
* comparison with other facial expression editing methods

The frame-wise experiment provides a starting point for investigating these directions.

---

## Acknowledgements

This project builds upon the published MagicFace research and its publicly released implementation.

The original authors and implementation should be credited when using or extending the underlying method.

This repository documents an independent reproduction and experimental extension rather than claiming authorship of the original MagicFace method.
