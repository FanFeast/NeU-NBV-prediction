# Active vision for Next Best View Planning in outdoor scenes

In this project, we extend the exploration of autonomous robotic tasks in the context of larger outdoor scenes. Building upon the referenced work, we focus on planning views for these expansive environments, addressing questions related to optimal data collection given a set of reference images. A significant contribution of our approach lies in the introduction of a cutscene augmentation method. This innovative technique involves semantically dividing larger outdoor scenes into smaller components. Our model is then trained to predict uncertainty and RGB values for novel poses within these segmented scenes. This cutscene augmentation method serves a dual purpose. First, it effectively increases the size of the dataset by a significant percentage, enhancing the efficiency of the training process, and not overfitting on a scene. Second, and more importantly, it substantially increases the accuracy of novel view predictions. By leveraging this method, our project aims to overcome challenges associated with data collection in large-scale outdoor scenarios, providing a valuable contribution to the broader field of autonomous robotic tasks. Our experiments, using both synthetic and real-world data, demonstrate the effectiveness of our proposed uncertainty-guided approach. The results showcase improved accuracy in scene representations compared to baseline methods, validating the utility and generalizability of our methodology.

## Table of Contents

- [About](#about)

## About

This project is built upon the codebase from the [NeuNBV repository](https://github.com/dmar-bonn/neu-nbv). We have extended and customized it to create our own files and scripts for training, visualizations, and dataset creation. For more details about our specific contributions and research, please visit our website: [Project Website](https://adityarauniyar.com/cutscene.github.io/).

