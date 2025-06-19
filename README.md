🐦 
# Bird Sound Classification on Low-Power Sensor Devices

This project tackles the challenge of identifying bird species based on their calls,  
with the goal of deploying the model on wireless acoustic sensor networks.  
Since these systems have limited computing power, we focused on keeping the model lightweight  
while still achieving accurate results across a range of bird species.

Video Link : https://www.veed.io/view/86e965f1-55ad-4248-8a1c-e0bfdac700f8?panel=share


**Dataset**: [Western Mediterranean Wetland Birds Dataset](https://zenodo.org/record/7505820)  
It contains 5,795 labeled audio clips and over 17,500 spectrograms from 20 bird species recorded in Girona, Spain.

| Model             | Regularizer | Optimizer (LR) | Epochs | Batch Size | Dropout | Accuracy | F1 Score | Recall | Precision |
| ----------------- | ----------- | -------------- | ------ | ---------- | ------- | -------- | -------- | ------ | --------- |
| **AdamW**         | L1          | Adamax (0.01)  | 5      | 128        | 0.3     | 11.85%   | 2.73%    | 9.31%  | 1.66%     |
| **SDG Function**  | L2          | SGD (0.03)     | 9      | 32         | None    | 22.28%   | 11.45%   | 14.94% | 13.31%    |
| **Simple CNN**    | None        | Adam (0.001)   | 7      | 128        | None    | 66.20%   | 17.98%   | 24.32% | 59.80%    |
| **Random Forest** | N/A         | N/A            | N/A    | N/A        | N/A     | 36.30%   | 25.48%   | 29.14% | 27.64%    |

**Insights**
⚙️ AdamW Model

    L1 Regularization aggressively pruned weights, likely causing underfitting.

    Combined with a high learning rate and limited training (5 epochs), the model failed to converge effectively.

    Even with dropout, performance remained poor due to insufficient training time and overly sparse weights.

⚙️ SDG Function

    L2 Regularization helped maintain weight stability.

    Stochastic Gradient Descent is slower to converge, and while 9 epochs offered slightly better results, the model still struggled without dropout.

    Performance improved over AdamW but remained limited due to undertraining and optimizer choice.

⚙️ Simple CNN

    Best overall accuracy and precision, largely due to the Adam optimizer and a relatively deep architecture.

    The lack of dropout or regularization may have caused the model to overfit on dominant classes—reflected by high precision but much lower recall and F1.

    Indicates strong memorization but poor generalization to minority classes.


**Usage of this model**
📦 Requirements

Make sure you have the following installed:
!git clone https://github.com/call_of_the_wild
pip install tensorflow numpy pandas librosa matplotlib scikit-learn pillow
