🐦 
# Bird Sound Classification on Low-Power Sensor Devices

This project tackles the challenge of identifying bird species based on their calls,  
with the goal of deploying the model on wireless acoustic sensor networks.  
Since these systems have limited computing power, we focused on keeping the model lightweight  
while still achieving accurate results across a range of bird species.

Video Link : https://www.veed.io/view/7026e1a4-ad56-4240-a67f-78b5acef44a0?panel=share


**Dataset**: [Western Mediterranean Wetland Birds Dataset](https://zenodo.org/record/7505820)  
It contains 5,795 labeled audio clips and over 17,500 spectrograms from 20 bird species recorded in Girona, Spain.

| Model             | Regularizer | Optimizer (LR) | Epochs | Batch Size | Dropout | Accuracy | F1 Score | Recall | Precision |
| ----------------- | ----------- | -------------- | ------ | ---------- | ------- | -------- | -------- | ------ | --------- |
| **AdamW**         | L1          | Adamax (0.01)  | 5      | 128        | 0.3     | 22.03%   | 5.03%    | 10.96%  | 4.53%     |
| **Adagrad Function**  | L2(0.04)          | Adagrad (0.05)     | 9      | 32         | 0.2    | 63.90%   | 11.11%   | 15.67% | 13.31%    |
| **Simple CNN**    | None        | Adam (0.001)   | 8      | 128        | None    | 40.46%   | 38.28%   | 40.46% | 46.94%    |
| **Random Forest** | N/A         | N/A            | N/A    | N/A        | N/A     | 30.83%   | 22.59%   | 27.25% | 22.59%    |

🔧 Insights Per Model
✅ Simple CNN (Best Balanced Metrics)

    Performance: Achieved the highest F1 Score and balanced precision-recall.

    Optimizer: Adam with a learning rate of 0.001, known for adaptive learning and general reliability.

    Regularization: None — the model may benefit from light regularization to improve generalization.

    Dropout: None — consider adding dropout to prevent overfitting.

📈 Adagrad Function

    High Accuracy: 63.90% accuracy, likely benefiting from Adagrad's ability to adapt learning rates, especially in sparse data.

    Weak F1/Recall: Despite accuracy, the F1 score (11.11%) and recall (15.67%) are low — suggesting poor class balance handling or overfitting to majority class.

    Regularizer: L2 (0.04) helped with generalization.

    Batch Size: 32 — small batches may have helped Adagrad converge better.

🔻 AdamW

    Poor Performance: Accuracy and all other metrics were very low.

    Possible Causes:

        L1 Regularization might have overly penalized weights, causing underfitting.

        High LR (0.01) for Adamax could cause unstable learning.

        Dropout of 0.3 may also have contributed to reduced capacity.

🌲 Random Forest

    Decent Baseline: Classical ML method with 30.83% accuracy.

    No Deep Learning Enhancements: Lower performance vs CNN, but decent for a non-deep model.

    Useful for Comparison: Serves as a useful benchmark for evaluating deep learning gains.


**Usage of this model**
📦 Requirements

Make sure you have the following installed:
!git clone https://github.com/call_of_the_wild
pip install tensorflow numpy pandas librosa matplotlib scikit-learn pillow
