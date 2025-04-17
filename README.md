# Coffee Leaf Rust Detection on Low-Resolution Images 🌿
Coffee leaf rust, caused by the fungus *Hemileia vastatrix*, is a serious threat to coffee production, particularly in resource-limited regions in Central America, where the disease spreads more rapidly due to climate change. Early detection is crucial to prevent crop loss, especially since rust lesions are difficult to distinguish from other parts of the leaf in the early stages. Traditional methods rely on high-resolution imaging and computational resources, which are scarce in these areas. To address this, we propose a Convolutional Neural Network (CNN) optimized for low-resolution images, coupled with a high-pass filter to enhance the contrast between rust lesions and leaf features. Our CNN model achieved roughly **94% accuracy** across precision, recall, F1-score, and Dice Coefficient metrics. Compared to larger models like AlexNet and MobileNet V2, our model provides similar detection performance with significantly fewer computational requirements. Our method offers a **scalable, cost-effective solution** for early disease detection in resource-constrained environments.

NOTE: Code was executed in Google Colab. Thus, modifications may be needed to run programs locally. 

## Key Contributions
- **Problem Focus**: CLR detection on *low-resolution* images.
- **Techniques Used**:
  - High-pass filtering to enhance lesion contrast
  - CNN-based classification models trained on downsized images

## Research Paper
This project was published on arXiv in 2024.  
🔗 [Read the full paper on arXiv](https://arxiv.org/abs/2407.14737)

## Recognition
This research received **Honorable Mention** for the 2024 NCWIT Collegiate Award.  
🔗 [NCWIT 2024 Collegiate Award Recipients](https://www.aspirations.org/news/2024-aic-collegiate-award-recipients)
